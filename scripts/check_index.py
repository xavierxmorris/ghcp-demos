"""Validate the publishing inventory without cloning or publishing any demo."""

from __future__ import annotations

import re
from pathlib import Path

DEMO_NAME = r"ghcp-demo-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*"


def parse_inventory(text: str) -> list[str]:
    names = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        name, separator, description = line.partition("|")
        if not separator or not description.strip():
            raise ValueError(f"repos.txt:{number}: expected name|description")
        if not re.fullmatch(rf"ghcp-demos|{DEMO_NAME}", name):
            raise ValueError(f"repos.txt:{number}: invalid repository name")
        if name in names:
            raise ValueError(f"repos.txt:{number}: duplicate repository {name}")
        names.append(name)
    if len(names) < 2 or names[0] != "ghcp-demos":
        raise ValueError("Inventory must start with ghcp-demos and contain at least one demo")
    numbers = [int(name.split("-")[2]) for name in names[1:]]
    if numbers != list(range(len(numbers))):
        raise ValueError("Demo numbers must be unique, ordered and consecutive from 00")
    return names


def validate_index(root: Path) -> list[str]:
    names = parse_inventory((root / "repos.txt").read_text(encoding="utf-8"))
    expected = set(names[1:])
    for filename in ("README.md", "FACILITATOR-GUIDE.md"):
        documented = set(re.findall(DEMO_NAME, (root / filename).read_text(encoding="utf-8")))
        if documented != expected:
            raise ValueError(
                f"{filename}: missing {sorted(expected - documented)}; "
                f"unlisted {sorted(documented - expected)}"
            )
    if "ghcp-demo-*/" not in (root / ".gitignore").read_text(encoding="utf-8").splitlines():
        raise ValueError("The index must keep child repositories untracked")
    return names


if __name__ == "__main__":
    repositories = validate_index(Path(__file__).resolve().parents[1])
    print(f"Validated the index and {len(repositories) - 1} independent demo entries. Nothing was published.")
