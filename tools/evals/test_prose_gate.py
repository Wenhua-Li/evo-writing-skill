from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tools" / "scripts" / "check_prose.py"
SPEC = importlib.util.spec_from_file_location("check_prose", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)
RULES = json.loads((ROOT / "skill" / "data" / "prose-gate.json").read_text(encoding="utf-8"))
FIXTURES = json.loads((ROOT / "tools" / "evals" / "prose-gate-fixtures.json").read_text(encoding="utf-8"))


class ProseGateTests(unittest.TestCase):
    def test_clean_fixtures_pass(self):
        for fixture in FIXTURES["clean"]:
            with self.subTest(fixture=fixture["id"]):
                self.assertEqual([], CHECKER.check_text(fixture["text"], RULES))

    def test_blocked_fixtures_report_expected_rules(self):
        for fixture in FIXTURES["blocked"]:
            with self.subTest(fixture=fixture["id"]):
                findings = CHECKER.check_text(fixture["text"], RULES)
                actual = {item["rule"] for item in findings}
                self.assertTrue(set(fixture["rules"]).issubset(actual), actual)

    def test_case_and_inflections_are_checked(self):
        text = "Declaring PROTOCOLS ties saturation trajectories certifications auditing inferring trials rivals refinements leveraging."
        actual = {item["rule"] for item in CHECKER.check_text(text, RULES)}
        self.assertTrue(
            {
                "declared",
                "protocol",
                "tie",
                "saturated",
                "trajectory",
                "certified",
                "audit",
                "inferred",
                "trial",
                "rival",
                "refinement",
                "leverage",
            }.issubset(actual)
        )

    def test_structure_can_be_disabled(self):
        text = "Moreover, one test is used. Moreover, another test is used."
        self.assertEqual([], CHECKER.check_text(text, RULES, include_structure=False))

    def test_all_after_examples_pass(self):
        for path in (ROOT / "skill" / "examples").glob("*.md"):
            with self.subTest(example=path.name):
                collecting = False
                blocks = []
                for line in path.read_text(encoding="utf-8").splitlines():
                    if line.strip() in {"## After", "### After"}:
                        collecting = True
                        blocks.append("")
                    elif line.startswith("#"):
                        collecting = False
                    elif collecting and line.startswith("> "):
                        blocks[-1] += line[2:] + " "
                self.assertTrue(blocks)
                for block in blocks:
                    self.assertEqual([], CHECKER.check_text(block.strip(), RULES))

    def test_install_manifest_is_complete(self):
        lines = [
            line.strip()
            for line in (ROOT / "install-manifest.txt").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        missing = [line for line in lines if not (ROOT / line).is_file()]
        self.assertEqual([], missing)
        required = {
            "skill/data/prose-gate.json",
            "skill/references/style/plain-ec-english.md",
            "skill/references/style/revision-gate.md",
            "tools/scripts/check_prose.py",
            "tools/evals/language-rewrite-cases.json",
            "tools/evals/prose-gate-fixtures.json",
            "tools/evals/test_prose_gate.py",
        }
        self.assertTrue(required.issubset(set(lines)))

    def test_cli_returns_zero_for_clean_standard_input(self):
        process = subprocess.run(
            [sys.executable, str(SCRIPT), "-", "--json"],
            input=FIXTURES["clean"][0]["text"],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(0, process.returncode, process.stderr)
        self.assertTrue(json.loads(process.stdout)["passed"])

    def test_cli_returns_one_and_locations_for_blocked_input(self):
        process = subprocess.run(
            [sys.executable, str(SCRIPT), "-", "--json"],
            input="The method uses grouping rather than full updates.",
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(1, process.returncode, process.stderr)
        result = json.loads(process.stdout)
        item = result["results"][0]["findings"][0]
        self.assertEqual("rather-than", item["rule"])
        self.assertEqual(1, item["line"])
        self.assertGreater(item["column"], 1)


if __name__ == "__main__":
    unittest.main()
