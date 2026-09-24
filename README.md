# GPT Project Bootstrap

A reusable, organization-neutral kit for establishing a consistent Codex + GitHub operating system across multiple repositories.

## Start here

1. Open this repository as the project root in Codex, or give the repository URL to ChatGPT.
2. Ask it to help you establish the system described here.
3. It should read the root `AGENTS.md`, then follow [START-CODEX-ORG.md](START-CODEX-ORG.md) and the full [CODEX-ORG-OPERATING-SYSTEM.md](CODEX-ORG-OPERATING-SYSTEM.md).
4. Expect an interactive setup: the assistant should verify prerequisites, ask for organization-specific decisions in small batches, audit read-only first, and obtain approval before writing.

If you prefer, copy the contents of [START-CODEX-ORG.md](START-CODEX-ORG.md) into a new conversation and include the URL of this repository.

## What each file does

- `AGENTS.md` — safety and routing instructions for an agent operating in this public repository.
- `START-CODEX-ORG.md` — the short prompt that begins an interactive setup.
- `CODEX-ORG-OPERATING-SYSTEM.md` — the detailed reusable blueprint and templates.
- `AUTHORS.md` — author and contributor credits.
- `LICENSE` — the Microsoft Public License (MS-PL).

## Safety boundary

This repository is a public template, not your organization's live policy. It grants no access or authority. Organization-specific names, people, identifiers, private links, credentials, and generated policies belong in your own canonical repository and must not be committed here.

## Validation scope

Run `python -m unittest discover -s tests -v` and `python scripts/check_tracked_text.py` from the repository root. CI runs these once per validation job. The standalone `python scripts/validate_existing_project_fixture.py` command is an optional way to inspect fixture results, not an additional coverage layer.

- The fixture tests execute the Python planner against two synthetic directory trees and compare its complete output with each reviewed `expected-plan.json`. They protect instruction-file precedence, configured fallback selection, preservation of an approved access route, the unconfigured connector baseline, and the proposed-change contract. File hashes check that planning leaves the fixtures unchanged.
- Negative tests ensure the validator rejects a changed access route and catches a planner that overwrites policy even when it returns the expected plan.
- The tracked-text tests use temporary Git repositories to check acceptance of LF text, binary exclusion, rejection of CRLF and missing final newlines, and the tracked-file limit.

These checks validate the Python fixture model and formatting tools. They do not run an agent following the Markdown instructions, prove that the model matches actual Codex instruction loading, or verify a real organization's setup or external permissions. Changes to the blueprint still require review of those instructions; passing planner tests is not evidence that an agent has executed them correctly.

## Authors and licence

Authors are listed in [AUTHORS.md](AUTHORS.md). This project is licensed under the [Microsoft Public License (MS-PL)](LICENSE).
