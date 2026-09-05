import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
SPEC = importlib.util.spec_from_file_location(
	"fixture_validator", ROOT / "scripts" / "validate_existing_project_fixture.py"
)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ExistingProjectFixtureTests(unittest.TestCase):
	def test_preserves_approved_existing_workflow_and_precedence(self):
		plan = VALIDATOR.validate_scenario(ROOT / "tests" / "fixtures" / "existing-workflow")
		self.assertEqual(
			plan["active_instruction_chain"],
			["AGENTS.override.md", "src/CODEX.md"],
		)
		self.assertEqual(plan["github_access_policy"], "approved-existing-cli")
		self.assertEqual(plan["recommended_alternatives"], [])
		self.assertEqual(plan["proposed_repository_setting_changes"], [])

	def test_unconfigured_scenario_uses_connector_baseline(self):
		plan = VALIDATOR.validate_scenario(ROOT / "tests" / "fixtures" / "unconfigured")
		self.assertEqual(plan["active_instruction_chain"], ["AGENTS.md"])
		self.assertEqual(plan["github_access_policy"], VALIDATOR.CONNECTOR_BASELINE)
		self.assertEqual(plan["recommended_alternatives"], [])


if __name__ == "__main__":
	unittest.main()

