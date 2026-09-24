import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).parents[1]
SPEC = importlib.util.spec_from_file_location(
	"fixture_validator", ROOT / "scripts" / "validate_existing_project_fixture.py"
)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ExistingProjectFixtureTests(unittest.TestCase):
	def test_plans_match_reviewed_fixtures_without_writes(self):
		for name in ("existing-workflow", "unconfigured"):
			with self.subTest(scenario=name):
				# The validator compares the whole plan and before/after file hashes.
				VALIDATOR.validate_scenario(ROOT / "tests" / "fixtures" / name)

	def copy_fixture(self):
		directory = tempfile.TemporaryDirectory()
		self.addCleanup(directory.cleanup)
		root = Path(directory.name) / "scenario"
		shutil.copytree(ROOT / "tests" / "fixtures" / "existing-workflow", root)
		return root

	def test_validator_rejects_a_plan_that_changes_the_approved_route(self):
		root = self.copy_fixture()
		answers_path = root / "scenario.json"
		answers = json.loads(answers_path.read_text())
		answers["approved_codex_github_route"] = "unapproved-route"
		answers_path.write_text(json.dumps(answers))
		with self.assertRaisesRegex(AssertionError, "plan mismatch"):
			VALIDATOR.validate_scenario(root)

	def test_validator_rejects_writes_even_when_the_plan_matches(self):
		root = self.copy_fixture()
		dry_run = VALIDATOR.dry_run

		def writing_planner(path):
			plan = dry_run(path)
			(path / "AGENTS.override.md").write_text("unexpected policy overwrite\n")
			return plan

		with patch.object(VALIDATOR, "dry_run", side_effect=writing_planner):
			with self.assertRaisesRegex(AssertionError, "mutated the fixture"):
				VALIDATOR.validate_scenario(root)


if __name__ == "__main__":
	unittest.main()

