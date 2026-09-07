from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.check_index import parse_inventory, validate_index

VALID = "ghcp-demos|Index\nghcp-demo-00-example|Example\n"


class IndexContractTests(unittest.TestCase):
    def test_valid_inventory(self) -> None:
        self.assertEqual(parse_inventory(VALID), ["ghcp-demos", "ghcp-demo-00-example"])

    def test_invalid_inventory_is_rejected(self) -> None:
        cases = [
            "", "ghcp-demos|Index\n", VALID + "ghcp-demo-00-example|Duplicate",
            VALID.replace("00-example", "01-example"),
            VALID.replace("00-example", "../escape"),
            VALID.replace("|Example", "|"),
        ]
        for text in cases:
            with self.subTest(text=text), self.assertRaises(ValueError):
                parse_inventory(text)

    def test_documentation_drift_is_rejected_without_requiring_child_checkouts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "repos.txt").write_text(VALID, encoding="utf-8")
            (root / ".gitignore").write_text("ghcp-demo-*/\n", encoding="utf-8")
            for filename in ("README.md", "FACILITATOR-GUIDE.md"):
                (root / filename).write_text("ghcp-demo-00-example", encoding="utf-8")
            self.assertEqual(len(validate_index(root)), 2)
            (root / "README.md").write_text("Missing demo reference", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "README.md"):
                validate_index(root)


if __name__ == "__main__":
    unittest.main()
