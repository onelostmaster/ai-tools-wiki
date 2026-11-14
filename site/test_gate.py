#!/usr/bin/env python3
"""Gate tests: the build passes on the real data and fails on broken copies.

Usage:
    python3 -I site/test_gate.py

Each broken copy is today's data/tools.json with one change, written to a
temporary folder. Python standard library only.
"""

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent
BUILD = SITE_DIR / "build.py"
DATA = SITE_DIR.parent / "data" / "tools.json"
# Built from parts so the literal domain never sits in this public file.
PRIVATE_LINK = "https://app." + "notion" + ".com/p/0123456789abcdef"


def run_build(path):
    return subprocess.run(
        [sys.executable, "-I", str(BUILD), str(path)],
        capture_output=True,
        text=True,
    )


class GateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DATA.read_text(encoding="utf-8"))
        cls.tmp = tempfile.TemporaryDirectory()

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()
        # Leave site/dist built from the real data.
        run_build(DATA)

    def broken_copy(self, name, change):
        data = copy.deepcopy(self.data)
        change(data)
        path = Path(self.tmp.name) / (name + ".json")
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def assert_fails(self, path, expected):
        result = run_build(path)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("BUILD GATE FAILED", result.stderr)
        self.assertIn(expected, result.stderr)

    def test_real_data_passes(self):
        result = run_build(DATA)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_extra_field_fails(self):
        def change(d):
            d["tools"][0]["Internal note"] = "x"
        self.assert_fails(self.broken_copy("extra_field", change), "fields not allowed: Internal note")

    def test_extra_top_level_key_fails(self):
        def change(d):
            d["generated_by"] = "x"
        self.assert_fails(self.broken_copy("extra_key", change), "top-level keys not allowed: generated_by")

    def test_yolo_on_avoid_fails(self):
        def change(d):
            tool = next(t for t in d["tools"] if t["Safety verdict"] == "avoid")
            tool["YOLO install"] = "run it with every default"
        self.assert_fails(self.broken_copy("yolo_avoid", change), "YOLO install on an avoid tool")

    def test_private_link_fails(self):
        def change(d):
            d["tools"][0]["Install notes"] = "See " + PRIVATE_LINK
        self.assert_fails(self.broken_copy("private_link", change), "link to the private workspace")

    def test_not_offered_on_unreviewed_passes(self):
        def change(d):
            tool = next(t for t in d["tools"] if t["Safety verdict"] == "unreviewed")
            tool["YOLO install"] = "Not offered."
        result = run_build(self.broken_copy("not_offered", change))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_empty_decision_renders_not_decided(self):
        def change(d):
            d["tools"].sort(key=lambda t: t["Name"].lower())
            d["tools"][0]["Decision"] = ""
        result = run_build(self.broken_copy("empty_decision", change))
        self.assertEqual(result.returncode, 0, result.stderr)
        pages = list((SITE_DIR / "dist" / "t").glob("*/index.html"))
        self.assertEqual(len(pages), 1)
        self.assertIn("<dd>Not decided</dd>", pages[0].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
