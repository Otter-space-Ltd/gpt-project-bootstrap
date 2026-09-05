#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path


DEFAULT_ORDER = ("AGENTS.override.md", "AGENTS.md")
CONNECTOR_BASELINE = (
	"Every GitHub read or write by Codex or GPT must use the installed GitHub "
	"connector; offline local Git operations remain allowed."
)


def snapshot(root):
	return {
		str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
		for path in sorted(root.rglob("*"))
		if path.is_file()
	}


def configured_fallbacks(root):
	config = root / ".codex" / "config.json"
	if not config.exists():
		return ()
	return tuple(json.loads(config.read_text())["project_doc_fallback_filenames"])


def instruction_chain(root, working_directory):
	current = root
	chain = []
	for part in Path(working_directory).parts:
		candidates = (*DEFAULT_ORDER, *configured_fallbacks(root))
		active = next((current / name for name in candidates if (current / name).is_file()), None)
		if active:
			chain.append(active.relative_to(root).as_posix())
		current /= part
	candidates = (*DEFAULT_ORDER, *configured_fallbacks(root))
	active = next((current / name for name in candidates if (current / name).is_file()), None)
	if active:
		chain.append(active.relative_to(root).as_posix())
	return chain


def dry_run(root):
	answers = json.loads((root / "scenario.json").read_text())
	chain = instruction_chain(root, answers["working_directory"])
	existing_route = answers.get("approved_codex_github_route")
	policy = existing_route or CONNECTOR_BASELINE
	return {
		"scenario": answers["name"],
		"active_instruction_chain": chain,
		"github_access_policy": policy,
		"recommended_alternatives": [],
		"proposed_file_changes": [
			{
				"path": chain[0],
				"operation": "merge canonical pointer into active source",
				"preserve_existing_content": True,
			}
		],
		"proposed_repository_setting_changes": [],
		"preserved_external_workflows": answers["external_workflows"],
	}


def validate_scenario(root):
	before = snapshot(root)
	actual = dry_run(root)
	expected = json.loads((root / "expected-plan.json").read_text())
	after = snapshot(root)
	if actual != expected:
		raise AssertionError(
			f"{root.name}: dry-run plan mismatch\n"
			f"expected={json.dumps(expected, indent=2)}\n"
			f"actual={json.dumps(actual, indent=2)}"
		)
	if before != after:
		raise AssertionError(f"{root.name}: dry run mutated the fixture")
	return actual


def main():
	fixtures = Path(__file__).parents[1] / "tests" / "fixtures"
	selected = sys.argv[1:] or ["existing-workflow", "unconfigured"]
	for name in selected:
		plan = validate_scenario(fixtures / name)
		print(f"{name}: validated {', '.join(plan['active_instruction_chain'])}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())

