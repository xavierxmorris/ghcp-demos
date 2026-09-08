"""Strict gh/git test double. Never contacts GitHub or invokes real Git."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


def main() -> int:
    tool, *arguments = sys.argv[1:]
    log = Path(os.environ["PUBLISHER_TEST_LOG"])
    with log.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps({"tool": tool, "args": arguments}) + "\n")
    state_path = Path(os.environ["PUBLISHER_TEST_STATE"])
    state = json.loads(state_path.read_text()) if state_path.exists() else {
        "created": False, "visibility": os.environ.get("PUBLISHER_TEST_REMOTE", "ABSENT"),
        "origin": os.environ.get("PUBLISHER_TEST_ORIGIN", ""),
    }
    target = "test-owner/ghcp-demo-14-example"
    if tool == "gh":
        if arguments == ["auth", "status"]:
            print("Synthetic authentication successful")
        elif arguments == ["api", "user", "--jq", ".login"]:
            print("test-owner")
        elif arguments[:2] == ["api", "--paginate"]:
            if os.environ.get("PUBLISHER_TEST_API_FAIL") == "1":
                print("Synthetic metadata failure (403); do not create a repository", file=sys.stderr)
                return 1
            if os.environ.get("PUBLISHER_TEST_BAD_METADATA") == "1":
                print("not-a-valid-visibility-record")
            elif state["visibility"] != "ABSENT":
                print(target + "\t" + state["visibility"])
        elif arguments[:3] == ["repo", "create", target]:
            if "--push" in arguments or state["visibility"] != "ABSENT":
                raise AssertionError("Creation must be separate from pushing and only for missing repos")
            state["created"] = True
            state["visibility"] = os.environ.get(
                "PUBLISHER_TEST_CREATED_VISIBILITY", "PRIVATE" if "--private" in arguments else "PUBLIC"
            )
            print("https://github.com/" + target)
        elif arguments == ["repo", "view", target, "--json", "visibility", "--jq", ".visibility"]:
            if state["visibility"] == "ABSENT":
                raise AssertionError("Target should exist before visibility verification")
            print(state["visibility"])
        else:
            raise AssertionError(f"Unexpected mock gh operation: {arguments!r}")
    elif tool == "git":
        if arguments == ["remote"]:
            if state["origin"]:
                print("origin")
        elif arguments[:3] == ["remote", "add", "origin"]:
            state["origin"] = arguments[3]
        elif arguments == ["remote", "get-url", "--push", "--all", "origin"]:
            print(state["origin"])
        elif arguments == ["push", "-u", "origin", "main"]:
            print("Synthetic push; no network used")
        else:
            raise AssertionError(f"Unexpected mock git operation: {arguments!r}")
    else:
        raise AssertionError(f"Unexpected tool: {tool}")
    state_path.write_text(json.dumps(state), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
