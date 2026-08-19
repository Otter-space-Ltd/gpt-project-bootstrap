# Reusable Codex + GitHub organization operating system

This file is the detailed half of a two-file bootstrap kit for running multiple related repositories through Codex and one GitHub organization:

- `START-CODEX-ORG.md` is the short block a user copies into a new GPT conversation.
- `CODEX-ORG-OPERATING-SYSTEM.md` is this detailed public blueprint. GPT reads it from the public bootstrap source, interviews the user about its placeholders, and generates organization-specific policy in the user's chosen canonical repository.

This public repository is a reusable template, not an organization's canonical policy and not a grant of authority. When it is opened as a Codex project, the root `AGENTS.md` supplies the bootstrap safety boundary. If `START-CODEX-ORG.md` is pasted elsewhere, GPT must obtain the public bootstrap repository URL before relying on this blueprint. Organization-specific names, people, identifiers, private links, credentials, and generated policy must be written only to the user's chosen repositories, never back into this public template.

The user must not be required to edit this file manually. GPT owns placeholder discovery, questioning, validation, and creation of the filled organization-specific files.

The design has four goals:

1. one authoritative home for organization-wide Codex rules;
2. small project-specific instruction files in every other repository;
3. one clear source of truth for each kind of information; and
4. one explicit, auditable GitHub access policy for Codex that preserves an approved existing route or uses the connector-only baseline when none exists.

Official background: Codex reads `AGENTS.md` files before work and layers files found from the project root toward the current working directory. A canonical file in a separate sibling repository is **not** inherited automatically; every project repository must explicitly direct Codex to read it. See [OpenAI's AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

---

## 1. Variables GPT must collect

Angle-bracketed values are deliberate prompts for GPT, not fields the user must edit. GPT must inventory them, ask the user only for values relevant to the current stage, preserve an answer ledger, and confirm ambiguous answers. Ask in small coherent batches rather than presenting one large questionnaire.

| Variable | Meaning | Example format |
| --- | --- | --- |
| `<ORG_DISPLAY_NAME>` | Exact human-facing organization name and capitalization | `Example Studio` |
| `<GITHUB_ORG>` | GitHub organization slug | `example-studio` |
| `<CANONICAL_REPO>` | Repository containing the canonical `AGENTS.md` | `example-general` |
| `<DEFAULT_BRANCH>` | Default branch used by the repositories | `main` |
| `<LOCAL_PARENT>` | Local directory containing sibling checkouts | `C:\Repos\Example Studio` |
| `<GITHUB_ACCESS_POLICY>` | Verified policy governing GitHub access by Codex or GPT | Preserve the approved existing policy, otherwise use the connector-only baseline |
| `<TECHNICAL_OPERATOR>` | Person responsible for repository work | `Alex` |
| `<OPERATIONS_ONLY_PEOPLE>` | People who use the operational tracker but not GitHub or code | `Sam` |
| `<OPERATIONS_SYSTEM>` | Optional business/operations tracker | `Asana`, `Linear`, or `None` |
| `<OPERATIONS_REFERENCE>` | Optional authoritative workflow record or URL | project/task URL |
| `<CONNECT_COMMAND>` | Read-only orientation command | `EXAMPLE, CONNECT!` |
| `<SAVE_COMMAND>` | Durable routing/persistence command | `EXAMPLE, SAVE!` |

Organization variables are collected once. Project variables are collected only when that project is onboarded. Template-only placeholders such as `<DANGEROUS_OPERATION_OR_EXTERNAL_SIDE_EFFECT>` become concrete rules in the generated project `AGENTS.md`; the user never replaces them in this blueprint.

After collecting enough information, GPT proposes the exact files and external changes it intends to create. It fills the actual canonical `AGENTS.md`, project `AGENTS.md` files, repository inventory, issues, and settings after user approval. Keep this source blueprint reusable unless the user explicitly asks for an organization-filled copy.

Create and maintain a repository inventory in the canonical repository:

| Repository | Purpose | Local path | Issues enabled | Projects enabled | Root `AGENTS.md` | Deployment method |
| --- | --- | --- | --- | --- | --- | --- |
| `<CANONICAL_REPO>` | Canonical rules and organization-wide documentation | `<LOCAL_PARENT>\<CANONICAL_REPO>` | Yes | As needed | Canonical | N/A |
| `<PROJECT_REPO_1>` | `<PURPOSE>` | `<LOCAL_PARENT>\<PROJECT_REPO_1>` | Yes | Yes | Project-specific | `<ISSUE_OR_DOC>` |

The inventory is a record to verify, not proof that an object still exists. Before reporting a repository, path, branch, file, issue, board, or other object as current, verify that exact object directly in the current turn.

---

## 2. Architecture

Use this structure:

```text
GitHub organization: <GITHUB_ORG>
|
+-- <CANONICAL_REPO>
|   +-- AGENTS.md                         # organization-wide Codex rules
|   +-- CODEX-ORG-OPERATING-SYSTEM.md     # this reusable blueprint
|   +-- optional organization docs
|
+-- <PROJECT_REPO_1>
|   +-- AGENTS.md                         # canonical pointer + project rules
|   +-- source, tests, configuration, docs
|   +-- GitHub Issues / GitHub Project
|
+-- <PROJECT_REPO_2>
    +-- AGENTS.md
    +-- source, tests, configuration, docs
    +-- GitHub Issues / GitHub Project
```

Keep local checkouts as siblings when using a relative canonical reference:

```text
<LOCAL_PARENT>\
|-- <CANONICAL_REPO>\
|-- <PROJECT_REPO_1>\
+-- <PROJECT_REPO_2>\
```

If repositories are not guaranteed to be siblings, replace the relative reference with a discovery method that can be verified locally. Do not silently guess a canonical path.

### Native Codex hierarchy versus this cross-repository hierarchy

Codex natively discovers instruction files inside the current repository's directory hierarchy. This design adds a second, explicit layer:

1. Codex reads the current project's root `AGENTS.md` natively.
2. That file explicitly tells Codex to read `../<CANONICAL_REPO>/AGENTS.md` in full.
3. The canonical file supplies organization-wide policy.
4. The project file then supplies only project-specific additions or explicit, permitted overrides.

The canonical repository must therefore be available locally whenever work begins in a project repository. If it is unavailable, work stops rather than reconstructing policy from memory.

---

## 3. Source-of-truth routing

Define one authoritative destination for every kind of durable information.

| Information | Authoritative destination |
| --- | --- |
| Organization-wide Codex policy | `<CANONICAL_REPO>/AGENTS.md` |
| Project-specific Codex policy | That project's root `AGENTS.md` |
| Source code, tests, configuration, durable technical documentation | Relevant repository |
| Development requirements, technical decisions, implementation progress, test findings, code-level blockers | Relevant GitHub issue or GitHub Project item |
| Organization-level business decisions, ownership, priorities, and operational outcomes | `<OPERATIONS_SYSTEM>`, if one exists |
| High-level operational marker for a software outcome | Optional broad task in `<OPERATIONS_SYSTEM>` linking to the GitHub issue |
| Transient reasoning, routine status chatter, or chat transcript | Do not persist unless it becomes a durable decision or requirement |
| Passwords, tokens, credentials, customer data, production exports, or sensitive logs | None of these systems |

Rules:

- Do not duplicate technical detail in the operations system.
- Do not use a repository document as a substitute for issue discussion or routine progress tracking.
- A broad operations task may say “Add feature X to Project Y” and link to GitHub. Its technical requirements, debugging, commits, tests, and blockers remain in GitHub.
- Close a broad operations task when the business outcome is delivered, which may be later than technical completion.
- Reuse an existing relevant issue before creating a new one.
- Create one issue for each distinct actionable unit of development work.

---

## 4. Identity and role separation

Document who can work in which system. Do not treat Codex as a separate human actor.

Recommended role model:

- `<TECHNICAL_OPERATOR>` uses Codex, repositories, GitHub Issues, and GitHub Projects. They may also use `<OPERATIONS_SYSTEM>`.
- `<OPERATIONS_ONLY_PEOPLE>` use only `<OPERATIONS_SYSTEM>`. They are not expected to access GitHub, understand branches or commits, inspect repositories, or execute coding tasks.
- Codex determines which human it represents from the authenticated connection and the conversation before mutating external state.
- A coding task in the operations system must be assigned to the technical operator, not left unassigned or assigned to an operations-only person.
- Operations-only collaborators may add business requirements, observations, decisions, and questions. Codex translates the implementation consequences into GitHub without copying technical detail back into the operations system.

If everyone in the new organization is technical, simplify this section, but still record system access and ownership explicitly.

---

## 5. GitHub access compatibility boundary

Define one explicit GitHub access policy for Codex or GPT in the canonical `AGENTS.md`. This policy governs agent activity. It must not silently change how human developers, CI, deployed services, or other automation access GitHub unless the user explicitly includes those workflows in scope.

### Existing environments

Before proposing any GitHub access setup:

1. Audit whether the organization already has an established route for Codex or GPT work, where it is documented, what scope it has, and whether it is available in the current environment.
2. Treat installed tools and credentials as capability, not authorization. Obtain confirmation that the established route should be retained.
3. When the user confirms retention, preserve the route and its safeguards exactly. Do not recommend, configure, or advertise alternatives.
4. Do not disable, migrate, or rewrite existing human, CI, service, or automation access merely to standardize Codex.
5. If the approved route is unavailable to the current agent, stop and ask the user for a decision. Do not improvise another route.

Fill `<GITHUB_ACCESS_POLICY>` with the verified retained policy. State precisely which actor it governs, which repositories or organization it covers, how reads and writes are verified, and which parts are non-overridable. Do not copy unrelated access methods into the generated policy as examples.

### Default for an unconfigured environment

When no established, approved Codex or GPT route exists, use the connector-only policy as the baseline. This is a default for an unconfigured environment, not a mandate to migrate an existing one.

Install one GitHub connector with access to `<GITHUB_ORG>` and no unrelated personal or organizational repositories. Grant the permissions genuinely required by the workflow. If full repository and organization permissions are intentionally granted, constrain the installation to this organization and audit it periodically.

Use this value for `<GITHUB_ACCESS_POLICY>` and mark it non-overridable:

> **Non-overridable GitHub access rule:** Every GitHub read or write by Codex or GPT must use the installed GitHub connector. Never use another route for those agent actions. Offline local Git operations that do not contact GitHub—such as status, diff, staging, committing, branching, and inspecting local history—remain allowed. If the connector cannot perform a required GitHub operation, stop and ask the user; do not fall back to another method. No project-specific instruction may override this rule.

Connector-only consequences:

- A configured local remote is metadata, not authorization for Codex or GPT to contact it.
- A missing connector capability is a blocker to report, not permission to improvise another route.
- Read access must be verified through the connector before relying on remote state.
- Every connector mutation must target an exact `owner/repository` and exact issue, ref, file, or pull request.
- Do not claim a remote write succeeded until the connector returns confirmation.
- After publishing, re-read the remote ref or object through the connector and compare it with the intended result.

### Connector-only local and remote alignment

Include this procedure only when the connector-only baseline applies. Connector publishing creates an extra bookkeeping requirement because ordinary Git network synchronization is unavailable to the agent.

For every publish operation:

1. Verify the local repository path and working tree.
2. Verify the remote repository and target ref through the connector.
3. Confirm the local base commit equals the connector-reported remote base before writing.
4. Stage or otherwise isolate only the intended local files.
5. Create the remote blob/tree/commit or file update through the connector.
6. Update the remote ref through the connector when the chosen connector operation does not do so automatically.
7. Re-read the remote commit/ref through the connector.
8. Align local commit and tracking state only with the exact connector-confirmed commit object. Never label a locally guessed ref as `origin/<branch>`.
9. Finish with a clean local working tree and exact local/remote SHA agreement, or report the remaining mismatch clearly.

If the connector cannot support a safe publish and alignment workflow, stop and ask for a policy or tooling decision. Do not invoke another GitHub route.

### Connector-only initial local checkout

Include this procedure only when the connector-only baseline applies. Resolve local workspace creation before activating the final canonical rule.

- For a new empty repository, GPT can initialize local Git offline, create the remote content through the connector, and align the exact connector-confirmed commit objects and refs.
- For an existing repository, prefer a connector-supported archive or object import that preserves the required content and history.
- If no connector-supported import exists, present the choice explicitly: the human performs a one-time initial checkout using a method they approve **before** the canonical connector-only rule is activated, or the repository remains remote-only until suitable tooling exists.
- GPT must never perform or imply an unapproved checkout or credential flow. Once the canonical connector-only rule is active, its no-fallback boundary applies fully to Codex and GPT.

When an approved existing route is retained instead, document and use its established verification and local/remote alignment procedure. Do not copy connector-specific mechanics into that policy unless they actually apply.

---

## 6. Canonical `AGENTS.md` template

Copy the following into `<CANONICAL_REPO>/AGENTS.md`, replace placeholders, and add only organization-wide rules. Keep domain-specific operational workflows in clearly labelled sections or linked authoritative records.

```markdown
# <ORG_DISPLAY_NAME> — canonical Codex working instructions

Preserve the exact capitalization **<ORG_DISPLAY_NAME>**.

## Scope and sources of truth

- This repository is the canonical home for instructions that apply across <ORG_DISPLAY_NAME> repositories.
- Each coding project's GitHub Issues or GitHub Projects board is authoritative for development requirements, technical discussion, implementation progress, testing detail, and code-level blockers.
- The relevant repository is authoritative for source code, tests, configuration, and durable technical documentation.
- <OPERATIONS_SYSTEM> is authoritative for organization-level business decisions, operational work, priorities, ownership, and high-level outcomes. Remove this rule if there is no separate operations system.
- Do not access an external system merely because this repository is open. Access it only when the user explicitly requests it or invokes an opt-in workflow that requires it.
- Never store passwords, access tokens, credentials, customer data, production exports, sensitive logs, or other secrets in chat, issues, project boards, operations systems, repositories, or source control.

## GitHub access policy

<GITHUB_ACCESS_POLICY>

## Freshness and existence checks

- Before reporting that a local path, repository, branch, file, issue, board, or external object currently exists—or linking to it—verify that exact object directly in the current turn.
- Do not infer a parent object's existence from a child-path check.
- Do not treat a configured workspace root, cached repository list, local remote, or earlier discovery result as current proof.
- After the user reports a deletion, rename, move, permission change, or other state change, discard stale discovery results and verify again.

## Cross-project instructions and overrides

- Every new project repository must have a root `AGENTS.md` directing Codex to read this canonical file in full before work, followed by project-specific instructions. For an existing repository, reconcile the currently active root instruction source as described below instead of blindly adding another file.
- If this canonical file cannot be accessed, stop and ask the user. Do not reconstruct it from memory.
- Put generally applicable instruction changes here. Put project-only instructions in that project's `AGENTS.md`.
- Project instructions may add non-conflicting guidance and must never override a non-overridable instruction.
- Any other override must explicitly name the exact canonical instruction, state the replacement, define its scope, and declare itself an override.
- A silent, ambiguous, indirect, or merely contradictory rule is not a valid override. Stop, identify the conflict, and ask the user.

## Work tracking

- Put implementation, review, testing, debugging, and code-level blockers in the relevant GitHub issue or project item.
- Reuse a suitable existing issue. Create a new issue only for distinct actionable work.
- Keep optional development tasks in <OPERATIONS_SYSTEM> broad, assigned to <TECHNICAL_OPERATOR>, and linked to GitHub. Do not mirror technical detail.
- Do not assign repository execution to an operations-only collaborator.
- Avoid duplicate tracking.

## Identity and authority

- Determine which human Codex represents from the authenticated connection and conversation; Codex is not a separate human user.
- Read the complete current record, ownership, dependencies, and relevant fields before administering an external task or issue.
- Do not make destructive, difficult-to-reverse, deployment, release, or production changes without explicit authorization.

## Repository safety and quality

- Preserve unrelated user work and inspect the working tree before editing or staging.
- Use synthetic data for development, tests, fixtures, demonstrations, screenshots, and examples.
- Never expose secrets, customer data, production data, or sensitive configuration through health, readiness, status, or diagnostic endpoints.
- Add or update automated tests for every new or changed endpoint, integration, or other material behavior when reasonably testable. If automation is impractical, document why and perform appropriate manual verification.
- Use tabs for indentation in source files unless an established project formatter requires otherwise.
- Use LF line endings in text files unless the relevant language or platform does not support LF at all.
- Do not claim a local, board, deployment, or external-system change succeeded without direct confirmation.

## Opt-in commands

### `<CONNECT_COMMAND>`

This is strictly read-only.

1. Determine the authenticated person and permitted systems.
2. Determine the relevant project from an explicit repository, the verified current repository, or clear conversation context. Ask if materially ambiguous.
3. Read the canonical and project instructions.
4. Inspect only the operational, GitHub, and local state needed for orientation.
5. Report immediate work, meaningful blockers, and relevant state.
6. Do not mutate external systems, edit files, install dependencies, commit, publish, deploy, or release.

### `<SAVE_COMMAND>`

Persist only durable information established in the current conversation.

- Audit the entire current conversation from its beginning, not only the most recent exchange. Treat an earlier successful SAVE as a checkpoint, but reconcile the full available conversation against live durable records so omissions are caught. Persist only missing or changed information and do not duplicate existing records.
- If conversation compaction or missing context prevents a reliable full audit, use every available conversation summary and live record, then disclose the limitation instead of claiming completion.
- Route business and operational decisions to <OPERATIONS_SYSTEM>, if applicable.
- Route project-specific development requirements, technical discussion, progress, testing details, and code-level blockers to the relevant GitHub issue or project item.
- Put durable technical documentation in the relevant repository when appropriate.
- Do not persist chat transcripts, transient reasoning, routine status, or duplicate information.
- SAVE does not authorize committing, publishing, opening or merging pull requests, deploying, releasing, or changing production. Those require separate instructions.
- If nothing belongs in a durable source of truth, make no write and say so.
```

GPT must review the generated canonical file with the user before publishing it. Remove irrelevant systems, add the organization's real safety invariants, and do not leave contradictory placeholder rules active.

---

## 7. Project instruction template and existing-file reconciliation

For a new repository, create a root `AGENTS.md` from the minimal template below. For an existing repository, treat the template as content to reconcile into the active instruction chain, not as an instruction to overwrite or add a file blindly.

Before proposing an instruction change in an existing repository:

1. Inspect the applicable Codex profile and project configuration, including `project_doc_fallback_filenames` and `project_doc_max_bytes` when configured.
2. Inventory `AGENTS.override.md`, `AGENTS.md`, configured fallback files, and nested instruction files from the project root to the relevant working directories.
3. Determine which single file is active in each directory. Codex checks `AGENTS.override.md` before `AGENTS.md`, then configured fallbacks; a newly added `AGENTS.md` may therefore be ignored when an override is present.
4. Preserve existing instructions and their intent. Merge the canonical pointer and missing project-specific rules into the active source, and present the exact diff for review.
5. Do not delete, rename, replace, or migrate an existing instruction source unless the user explicitly approves that exact change.
6. Check the combined instruction size and precedence for conflicts or truncation.
7. After writing, start a fresh Codex run or use the available instruction-reporting mechanism to verify the sources and order actually loaded.

Use this minimal content for a new root file or as the reconciliation target for an existing active source:

```markdown
# <PROJECT_NAME> — Codex working instructions

Before doing any work in this repository, read the current canonical <ORG_DISPLAY_NAME> instructions at `../<CANONICAL_REPO>/AGENTS.md` in full. If that file cannot be accessed, stop and ask the user. The project-specific instructions in this file are additive and do not override the canonical instructions.

## Project purpose

- <ONE_OR_TWO_SENTENCES_DESCRIBING_THE_PROJECT_AND_ITS_TRUST_BOUNDARY>

## Project-specific safeguards

- <DANGEROUS_OPERATION_OR_EXTERNAL_SIDE_EFFECT>
- <DEPLOYMENT_OR_PRODUCTION_RULE>
- <SECURITY_OR_DATA_BOUNDARY>
- <BEHAVIOR_THAT_MUST_BE_PRESERVED>

## Verification

- Run `<FOCUSED_TEST_COMMAND>` for relevant changes.
- <SAFE_MANUAL_CHECK_IF_NEEDED>
```

Good project-specific rules describe facts that are not generally true elsewhere, for example:

- a service is LAN-only and unauthenticated;
- a command can shut down a real machine;
- a deployment script contains a destructive synchronization flag;
- source was recovered and must be compared with a live system before deployment;
- an integration is intentionally read-only;
- a utility extracts content without verifying a signature;
- an exact timezone, protocol, or behavioral contract must be preserved.

Do not repeat generic secret, testing, GitHub-routing, indentation, line-ending, or synthetic-data rules in every project file. Put them in the canonical file once.

---

## 8. GitHub issue and project conventions

For a new or unconfigured active project repository, enable Issues by default and enable GitHub Projects when a board is useful. For an existing repository, preserve its current Issues, Projects, labels, and workflow settings unless the user approves an exact change after the read-only audit. Do not treat a different established configuration as missing merely because it differs from this baseline.

Each issue should contain:

```markdown
# Imperative, outcome-oriented title

Why this work is needed and any relevant current state.

## Scope

- Concrete included work
- Important constraint or dependency
- Explicit non-goal when ambiguity is likely

## Done when

- Observable acceptance criterion
- Tests, validation, or documentation completed
```

Issue rules:

- Search existing open and closed issues before creating a new one.
- Use one issue per distinct actionable outcome; split work when outcomes can be delivered independently.
- Record durable decisions, requirements, progress, test evidence, and blockers on the issue.
- Link dependent issues and broad operations tasks instead of copying their content.
- Use issue bodies for the stable problem and acceptance criteria; use comments for chronological findings and decisions.
- Close an issue only when its stated outcome and validation are complete. Use `not planned` when deliberately declining it.
- Keep repository-specific technical work in that repository even if an organization-level Project aggregates it.

Useful initial issues for a new or inherited project often include:

- validate recovered or imported code against the live system;
- create a safe, documented deployment method;
- add or repair automated tests;
- document local setup and production verification;
- reconcile installed copies with repository versions;
- remove obsolete or unsafe utilities;
- establish CI, branch protection, and release/rollback practices.

---

## 9. Bootstrap procedure for a new organization

### Phase A — human-guided prerequisites before approved GitHub access

GPT guides the user one step at a time and waits for confirmation after each external action. Never request GitHub credentials or tokens, and never use an access route merely because it is technically available.

1. Confirm the user is signed in to the intended GitHub account and can act as an owner of the target organization.
2. Ask whether the organization already exists. If not, explain the naming and ownership choices and guide the user through [GitHub's organization creation flow](https://github.com/account/organizations/new) using [GitHub's official instructions](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch).
3. Ask for the canonical repository name, visibility, and default branch. Guide the user to create and initialize it with a README so the default branch exists, using [GitHub's repository creation guidance](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).
4. Confirm that GPT can read `START-CODEX-ORG.md` and `CODEX-ORG-OPERATING-SYSTEM.md` from the public bootstrap repository. If the short prompt was pasted without repository context, ask the user for that public repository URL. Do not copy organization-specific values or generated policy back into the public bootstrap repository.
5. Ask whether an established GitHub access route is already used for Codex or GPT work. Audit its documented scope and availability without changing it. If the user confirms that it should be retained, record it in the answer ledger and do not propose alternatives.
6. If no established route exists, guide the user to install the official [GitHub plugin](https://chatgpt.com/plugins/plugin_connector_1p_1a69035c238881919c4190932b2df699). If the direct link has changed, find the current GitHub entry in the [ChatGPT plugin directory](https://chatgpt.com/plugins).
7. When the connector baseline is being established, select only `<GITHUB_ORG>` and the intended organization repositories. Do not authorize personal repositories or another organization. If future repositories must be discovered automatically, choose all repositories **within that organization only**; otherwise select the exact approved repositories and update the installation when onboarding another.
8. Configure plugin availability, app access, action controls, and app permissions for the intended user or role. Plugin availability and GitHub authorization are separate layers. If full read/write permissions are intentional, state that consequence and obtain explicit user confirmation. Follow [OpenAI's plugin-control guidance](https://learn.chatgpt.com/docs/enterprise/apps-and-connectors).
9. If GitHub requires organization-owner approval for a new connector installation, guide the user to approve it before continuing.

### Phase B — GitHub access verification and GPT interview

1. Verify through the approved route that the authenticated identity can see `<GITHUB_ORG>` and the canonical repository within the agreed scope.
2. Inventory the repositories visible through that route and confirm its actual scope. Do not widen or reconfigure the route during this read-only audit.
3. Fetch and read `CODEX-ORG-OPERATING-SYSTEM.md` from the public bootstrap repository in full.
4. Inventory its placeholders and ask the user for the organization-level values in small batches. Do not ask the user to edit the file.
5. Ask whether Codex is installed and whether a local workspace and checkouts exist. If they do, verify the exact paths. If they do not, guide the user with current official Codex setup information and resolve the initial-checkout procedure required by the approved access policy; do not invent `<LOCAL_PARENT>`.
6. Perform a strictly read-only audit of existing repositories, the active instruction chain and its precedence, Issues, Projects, repository settings, and relevant operations systems.
7. Present the proposed organization-specific files, settings, issues, and migrations. Obtain approval before writing.

### Phase C — canonical policy

1. Generate the filled canonical `AGENTS.md` in `<CANONICAL_REPO>` from the user's answers.
2. Add or update the repository inventory without requiring the user to edit this blueprint.
3. Fill `<GITHUB_ACCESS_POLICY>` with the confirmed retained policy or, when none existed, the connector-only baseline. Record its actor and scope separately from human and automation workflows.
4. Record the operations-system reference, identity model, source-of-truth boundary, and safety rules.
5. Commit and publish through the approved GitHub route.
6. Re-read the remote commit through the same route and verify local/remote alignment when a local checkout exists.

### Phase D — onboard each project repository

For each repository:

1. Verify the exact remote repository exists through the approved GitHub route.
2. Verify the exact local checkout exists; do not rely on a configured workspace root alone.
3. Confirm the local checkout corresponds to the intended `owner/repository`.
4. Read the README, source layout, deployment tooling, tests, and external side effects.
5. Inventory the active Codex instruction chain, including overrides, standard files, configured fallbacks, nested files, precedence, and size limits.
6. For a new repository, create the root project `AGENTS.md` from the template. For an existing repository, merge the canonical pointer and missing project-specific constraints into the active instruction source without discarding existing content.
7. Verify the instruction sources and precedence that a fresh Codex run actually loads.
8. Preserve existing Issues and Projects settings unless an exact change was approved; for an unconfigured repository, apply the agreed baseline.
9. Search existing issues and seed only genuinely missing work.
10. Document local setup, verification, deployment, rollback, and production boundaries—or create issues to do so.
11. Publish the instruction change through the approved GitHub route and verify the resulting remote state.
12. Add the repository to the canonical inventory.

### Phase E — governance and engineering baseline

For every active repository, decide and record:

- default branch and branch protection;
- whether direct commits or pull requests are required;
- required reviews and status checks;
- test, lint, formatting, and build commands;
- code-owner or reviewer expectations;
- issue labels, milestones, and project-board fields;
- secret scanning, dependency alerts, and security review;
- deployment authorization, environment boundaries, verification, and rollback;
- release/versioning policy;
- backup or recovery expectations;
- ownership when the technical operator is unavailable.

For an existing repository, treat current settings and automation as evidence to review, not as blank fields to replace. Preserve established decisions unless the user approves a migration. Enforce new or changed decisions through repository settings or automation where possible, then document them in the appropriate source of truth.

---

## 10. Read-only orientation and durable save behavior

The two opt-in commands are deliberately asymmetric:

### CONNECT

- read-only across every system;
- verifies identity and current project context;
- reads current canonical and project instructions;
- inspects only relevant live state;
- reports work and blockers;
- never edits, moves, commits, publishes, deploys, or releases.

### SAVE

- audits the entire current conversation from its beginning, even when SAVE was invoked earlier, and reconciles it against live durable records;
- writes only durable information that is missing or has changed;
- routes each item to its authoritative system;
- reuses existing tasks/issues where appropriate;
- does not dump transcripts or duplicate technical detail;
- does not imply authorization to publish code or mutate production.

Explicit user requests may authorize a particular write without invoking SAVE. They do not automatically authorize adjacent actions such as deployment, merging, deletion, or production mutation.

---

## 11. Freshness, deletion, and rename handling

This is a required anti-staleness discipline:

- Verify the exact local path before linking to it.
- Verify the exact remote object through the approved GitHub route before reporting it.
- Verify local and remote state separately; neither proves the other.
- A child-path check does not prove its parent repository exists in the intended form.
- A workspace configuration entry may remain after a folder is deleted.
- A local folder may remain after a remote repository is deleted or renamed.
- After a user reports a state change, discard cached results and re-check immediately.
- Use language such as “verified locally” or “remotely confirmed through the approved route” when the distinction matters.

When retiring or renaming a repository:

1. confirm the exact target and whether archive, transfer, rename, or deletion is intended;
2. preserve or migrate open issues and project links as required;
3. update the canonical inventory and all canonical pointers;
4. update local checkout names or remove them only with explicit authorization;
5. update workspace configuration and documentation;
6. verify the final local and remote state independently;
7. do not continue listing the retired name from memory.

---

## 12. Security and data rules

At minimum, make these canonical:

- Never commit or paste credentials, tokens, private keys, customer data, production exports, sensitive logs, or live account data.
- Use synthetic data for development, tests, demos, screenshots, fixtures, and examples.
- Keep health and diagnostic endpoints minimal and non-sensitive.
- Mock or isolate destructive and external side effects during testing.
- Require explicit authorization for deployments, releases, production writes, destructive synchronization, account mutations, and difficult-to-reverse actions.
- Treat a technically available permission as capability, not authorization.
- When the connector baseline applies, keep connector scope limited to the intended organization and review it periodically.
- Prefer enforceable controls—branch rules, protected environments, narrowly scoped credentials, test gates—over prose alone.

---

## 13. Maintenance and drift audit

Run this audit after onboarding, after any repository add/remove/rename, after GitHub access-policy or permission changes, and periodically thereafter.

### GitHub access

- [ ] The approved GitHub access policy for Codex or GPT is documented with its actor and scope.
- [ ] The route works for the required reads and writes and exposes only the approved scope.
- [ ] No alternative route was introduced, advertised, or configured during bootstrap.
- [ ] Existing human, CI, service, and automation routes remain unchanged unless an exact migration was approved.
- [ ] When the connector-only baseline applies, the connector is installed for `<GITHUB_ORG>` only and its accessible repository list matches the approved inventory.

### Canonical repository

- [ ] Canonical `AGENTS.md` exists and is readable.
- [ ] Organization name, people, systems, IDs, and links are current.
- [ ] Source-of-truth routing is unambiguous.
- [ ] The approved GitHub access policy and freshness rules are present.
- [ ] Non-overridable rules are clearly marked.
- [ ] The file remains concise enough to fit Codex's active instruction budget.

### Every project repository

- [ ] Exact local and remote repositories have been verified.
- [ ] The active root instruction source exists and is verified.
- [ ] Overrides, configured fallback filenames, nested sources, precedence, and instruction-size limits have been accounted for.
- [ ] Existing instruction content was preserved or changed only through an explicitly approved diff.
- [ ] Canonical pointer resolves from the actual local layout.
- [ ] Project rules contain only project-specific guidance.
- [ ] No silent contradiction with canonical rules exists.
- [ ] Issues and Projects settings match the approved baseline or preserved existing decision.
- [ ] Test and deployment methods are known or have issues.
- [ ] Working tree and remote ref alignment are understood.

### Information hygiene

- [ ] Technical detail is in GitHub, not duplicated in the operations system.
- [ ] Business decisions and outcomes are in the operations system when applicable.
- [ ] Broad development markers link to authoritative GitHub issues.
- [ ] No secrets or live customer/production data are stored in prohibited locations.
- [ ] Closed, deleted, transferred, or renamed repositories are no longer presented as active.

Record audit findings as issues in the affected repository. Put organization-wide policy drift in `<CANONICAL_REPO>`.

---

## 14. Companion bootstrap prompt

The user starts by opening the public bootstrap repository in Codex or by pasting `START-CODEX-ORG.md` and supplying the repository URL. That short prompt instructs GPT to guide the human-only prerequisites, preserve and verify an approved existing GitHub route or establish the connector-only baseline when none exists, fetch this blueprint, conduct the placeholder interview, and then continue from this document.

Keep the companion prompt short enough to paste comfortably, but do not remove any of these controls:

- guide rather than assume prerequisites;
- provide current official links where possible;
- wait for the user after human-only actions;
- never ask for credentials or tokens;
- preserve an approved existing Codex or GPT GitHub route without recommending alternatives;
- use the connector-only baseline when no established route exists and scope it to the intended organization only;
- verify the approved GitHub route before relying on it;
- read this entire file before proposing implementation;
- make GPT, not the user, resolve placeholders;
- audit read-only first and obtain approval before writes;
- verify every external write from live responses.

---

## 15. Decisions that must remain organization-specific

This blueprint intentionally does not decide:

- the implementation details of an approved existing Codex or GPT GitHub workflow; preserve them when retention is confirmed, otherwise use the connector-only baseline;
- which business/operations tracker to use;
- who may administer tasks or repositories;
- whether project work uses direct commits or pull requests;
- branch protections and review count;
- labels, milestones, project-board workflow, and prioritization policy;
- deployment and production-write authority;
- domain-specific safety rules;
- tests and formatters for each technology;
- retention, compliance, and backup requirements.

Choose those explicitly, store each decision in the correct source of truth, and add generally applicable decisions to the canonical `AGENTS.md`. Project-specific decisions belong only in the relevant project's `AGENTS.md`, repository documentation, settings, or issues.

The result should be boring in the best possible way: Codex always knows which rules apply, which system owns each fact, which human it represents, how GitHub may be accessed, what it is authorized to change, and how to prove that a change actually happened.
