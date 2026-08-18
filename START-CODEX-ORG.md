# Copy and paste this into GPT

Help me establish the Codex + GitHub multi-repository system defined in `CODEX-ORG-OPERATING-SYSTEM.md`. Be an interactive setup guide; assume no prerequisites.

First determine whether I have the intended GitHub account, organization-owner authority, organization, and canonical/base repository, including its name, visibility, and default branch. Guide me one human action at a time, wait for confirmation, and give current direct links and official instructions. If needed, help me create the [organization](https://github.com/account/organizations/new), initialize the canonical repository with a README/default branch, and upload `CODEX-ORG-OPERATING-SYSTEM.md` and this file through GitHub's web UI.

Guide me to install the official [GitHub plugin](https://chatgpt.com/plugins/plugin_connector_1p_1a69035c238881919c4190932b2df699), obtain owner approval if required, scope it to that organization only—not personal or unrelated repositories—and configure the intended read/write actions and app permissions. Explain authorization choices and never request credentials or tokens. I may perform necessary pre-connector GitHub UI steps; you must not use browser automation, Git/CLI networking, `gh`, SSH, HTTPS credentials, or direct APIs.

Then verify through the connector that you can enumerate exactly the intended organization and read the canonical repository. Fetch and read `CODEX-ORG-OPERATING-SYSTEM.md` completely. Inventory its applicable placeholders, ask me for values in small coherent batches, and maintain an answer ledger; never ask me to edit it.

Perform its strictly read-only audit, including repositories, `AGENTS.md` files, Issues/Projects, roles, connector scope, Codex installation, and local workspace. Resolve initial checkout before activating the connector-only rule. Present the smallest plan and exact targets for approval. After approval, instantiate the system through the connector, verify every external write, and complete the audit checklist. Never widen scope, publish code, deploy, release, delete, or modify production without separate explicit authorization.
