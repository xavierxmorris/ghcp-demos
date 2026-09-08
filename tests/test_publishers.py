from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PWSH = shutil.which("pwsh")
BASH = (
    str(Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Git" / "bin" / "bash.exe")
    if os.name == "nt" else shutil.which("bash")
)
RUNTIMES = {"powershell": PWSH, "bash": BASH}


class PublisherPrivacyTests(unittest.TestCase):
    def exercise(
        self, runtime: str, *, row: str = "ghcp-demo-14-example|Generic private demo|private",
        remote: str = "ABSENT", flags: tuple[str, ...] = (), extra_env: dict | None = None,
    ) -> tuple[subprocess.CompletedProcess, list[dict]]:
        executable = RUNTIMES[runtime]
        if executable is None or not Path(executable).is_file():
            self.skipTest(f"{runtime} is unavailable; its publisher behavior is not exercised here")
        with tempfile.TemporaryDirectory(prefix="publisher-contract-") as directory:
            root = Path(directory)
            filename = "push-all.ps1" if runtime == "powershell" else "push-all.sh"
            shutil.copyfile(ROOT / filename, root / filename)
            # No final newline deliberately covers both publishers' last-row handling.
            (root / "repos.txt").write_text(row, encoding="utf-8")
            (root / "ghcp-demo-14-example" / ".git").mkdir(parents=True)
            fake_bin = root / "fake-bin"
            fake_bin.mkdir()
            double = root / "cli_double.py"
            shutil.copyfile(ROOT / "tests" / "publisher_cli_double.py", double)
            for tool in ("gh", "git"):
                if runtime == "powershell":
                    wrapper = fake_bin / (tool + ".ps1")
                    wrapper.write_text(
                        f'& $env:PUBLISHER_TEST_PYTHON $env:PUBLISHER_TEST_DOUBLE {tool} @args\nexit $LASTEXITCODE\n',
                        encoding="utf-8",
                    )
                else:
                    wrapper = fake_bin / tool
                    wrapper.write_text(
                        f'#!/usr/bin/env bash\nexec "$PUBLISHER_TEST_PYTHON" "$PUBLISHER_TEST_DOUBLE" {tool} "$@"\n',
                        encoding="utf-8",
                    )
                wrapper.chmod(0o755)
            environment = dict(os.environ)
            environment.update({
                "PATH": str(fake_bin) + os.pathsep + environment["PATH"],
                "GH_HOST": "github.com",
                "PUBLISHER_TEST_PYTHON": sys.executable,
                "PUBLISHER_TEST_DOUBLE": str(double),
                "PUBLISHER_TEST_BIN": str(fake_bin),
                "PUBLISHER_TEST_SCRIPT": str(root / filename),
                "PUBLISHER_TEST_LOG": str(root / "calls.jsonl"),
                "PUBLISHER_TEST_STATE": str(root / "state.json"),
                "PUBLISHER_TEST_REMOTE": remote,
            })
            environment.pop("BASH_ENV", None)
            environment.update(extra_env or {})
            if runtime == "powershell":
                probe = subprocess.run(
                    [executable, "-NoProfile", "-NonInteractive", "-Command", "(Get-Command gh).Source; (Get-Command git).Source"],
                    env=environment, cwd=root, capture_output=True, text=True, timeout=30,
                )
                expected = [fake_bin / "gh.ps1", fake_bin / "git.ps1"]
                self.assertEqual(probe.returncode, 0, probe.stdout + probe.stderr)
                self.assertEqual([Path(line).resolve() for line in probe.stdout.splitlines()], [p.resolve() for p in expected],
                                 "Refusing the test instead of calling real publishing tools")
                command = [executable, "-NoProfile", "-NonInteractive", "-File", str(root / filename), *flags]
            else:
                # Git for Windows' launcher prepends its real git directory to PATH.
                prefix = (
                    'export PATH="$(cygpath -u "$PUBLISHER_TEST_BIN"):$PATH"; hash -r; '
                    if os.name == "nt" else 'export PATH="$PUBLISHER_TEST_BIN:$PATH"; hash -r; '
                )
                probe_command = (
                    'cygpath -w "$(command -v gh)"; cygpath -w "$(command -v git)"'
                    if os.name == "nt" else "command -v gh; command -v git"
                )
                probe = subprocess.run(
                    [executable, "--noprofile", "--norc", "-c", prefix + probe_command],
                    env=environment, cwd=root, capture_output=True, text=True, timeout=30,
                )
                self.assertEqual(probe.returncode, 0, probe.stdout + probe.stderr)
                self.assertEqual([Path(line).resolve() for line in probe.stdout.splitlines()],
                                 [(fake_bin / name).resolve() for name in ("gh", "git")],
                                 "Refusing the test instead of calling real publishing tools")
                run_command = 'exec "$BASH" "$PUBLISHER_TEST_SCRIPT" "$@"'
                command = [executable, "--noprofile", "--norc", "-c", prefix + run_command, "publisher-test", *flags]
            result = subprocess.run(command, env=environment, cwd=root, capture_output=True, text=True, timeout=90)
            log = root / "calls.jsonl"
            calls = [json.loads(line) for line in log.read_text().splitlines()] if log.exists() else []
            return result, calls

    @staticmethod
    def creates(calls: list[dict]) -> list[dict]:
        return [call for call in calls if call["tool"] == "gh" and call["args"][:2] == ["repo", "create"]]

    @staticmethod
    def pushes(calls: list[dict]) -> list[dict]:
        return [call for call in calls if call["tool"] == "git" and call["args"][:1] == ["push"]]

    def test_private_entry_is_created_privately_before_any_content_push(self) -> None:
        for runtime in RUNTIMES:
            with self.subTest(runtime=runtime):
                result, calls = self.exercise(runtime)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertEqual(len(self.creates(calls)), 1)
                self.assertIn("--private", self.creates(calls)[0]["args"])
                self.assertNotIn("--push", self.creates(calls)[0]["args"])
                self.assertEqual(len(self.pushes(calls)), 1)
                view_index = next(i for i, call in enumerate(calls) if call["args"][:2] == ["repo", "view"])
                push_index = next(i for i, call in enumerate(calls) if call["args"][:1] == ["push"])
                self.assertLess(view_index, push_index)

    def test_existing_private_entry_is_not_recreated(self) -> None:
        for runtime in RUNTIMES:
            with self.subTest(runtime=runtime):
                result, calls = self.exercise(runtime, remote="PRIVATE")
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertFalse(self.creates(calls))
                self.assertEqual(len(self.pushes(calls)), 1)

    def test_private_entry_refuses_existing_public_target(self) -> None:
        for runtime in RUNTIMES:
            with self.subTest(runtime=runtime):
                result, calls = self.exercise(runtime, remote="PUBLIC")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("non-private", result.stderr)
                self.assertFalse(self.creates(calls))
                self.assertFalse(self.pushes(calls))

    def test_private_creation_is_verified_before_push(self) -> None:
        for runtime in RUNTIMES:
            with self.subTest(runtime=runtime):
                result, calls = self.exercise(runtime, extra_env={"PUBLISHER_TEST_CREATED_VISIBILITY": "PUBLIC"})
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("non-private", result.stderr)
                self.assertFalse(self.pushes(calls))

    def test_wrong_or_multiple_push_urls_refuse_publication(self) -> None:
        for runtime in RUNTIMES:
            for origin in (
                "https://github.com/another-owner/public-repo.git",
                "https://github.com/test-owner/ghcp-demo-14-example.git\nhttps://github.com/another-owner/public.git",
            ):
                with self.subTest(runtime=runtime, origin=origin):
                    result, calls = self.exercise(runtime, remote="PRIVATE", extra_env={"PUBLISHER_TEST_ORIGIN": origin})
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn("push URL", result.stderr)
                    self.assertFalse(self.pushes(calls))

    def test_metadata_failure_is_not_treated_as_an_absent_repository(self) -> None:
        for runtime in RUNTIMES:
            for flag in ("PUBLISHER_TEST_API_FAIL", "PUBLISHER_TEST_BAD_METADATA"):
                with self.subTest(runtime=runtime, failure=flag):
                    result, calls = self.exercise(runtime, extra_env={flag: "1"})
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse(self.creates(calls))
                    self.assertFalse(self.pushes(calls))

    def test_legacy_two_column_default_and_private_flag_are_preserved(self) -> None:
        for runtime in RUNTIMES:
            with self.subTest(runtime=runtime, visibility="default"):
                result, calls = self.exercise(runtime, row="ghcp-demo-14-example|Generic demo")
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("--public", self.creates(calls)[0]["args"])
            for row in ("ghcp-demo-14-example|Generic demo", "ghcp-demo-14-example|Generic demo|public"):
                with self.subTest(runtime=runtime, row=row):
                    flag = "-Private" if runtime == "powershell" else "--private"
                    result, calls = self.exercise(runtime, row=row, flags=(flag,))
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertIn("--private", self.creates(calls)[0]["args"])

    def test_bad_visibility_and_extra_columns_fail_before_publication(self) -> None:
        for runtime in RUNTIMES:
            for suffix in ("|PRIVATE", "|privte", "|", "|private|extra"):
                with self.subTest(runtime=runtime, suffix=suffix):
                    result, calls = self.exercise(runtime, row="ghcp-demo-14-example|Generic demo" + suffix)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse(self.creates(calls))
                    self.assertFalse(self.pushes(calls))


if __name__ == "__main__":
    unittest.main()
