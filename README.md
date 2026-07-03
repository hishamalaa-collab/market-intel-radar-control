# Market Intel Radar Control Repo

This repository is the instruction/control layer for the Market Intel Radar / Knowledge Studio operating system.

## Core Architecture

- **GitHub** is the source of truth for instructions, roles, workflows, prompt packs, locked decisions, and quality gates.
- **Google Drive** is the source of truth for source documents, reports, PDFs, decks, client materials, exports, and bulky assets.

Do not place this Git repository inside Google Drive. Clone it locally on each machine and connect it to Google Drive through local path notes.

## Start Here

1. Read `GITHUB_SETUP_GUIDE.md`.
2. Create a private GitHub repository named `market-intel-radar-control`.
3. Upload this starter pack.
4. Read `AGENTS.md`.
5. On each machine, create your own `config/local.paths.md` based on `config/local.paths.example.md`.

## Daily Use

Before a work session:

1. Pull the latest version from GitHub.
2. Read `00_boot/project_boot.md`.
3. Read the relevant role file in `02_roles/`.
4. Check `07_locked_decisions/locked_decisions.md`.
5. Work in small changes.
6. Commit with a clear message.
7. Push back to GitHub.

## Repository Contents

- `AGENTS.md` — front-door instructions for Codex and other coding agents.
- `00_boot/` — boot protocols and session start rules.
- `01_constitution/` — project constitution and operating principles.
- `02_roles/` — role cards for Director, PM, Designer, Advisor, Architect, and Vault Coordinator.
- `03_workflows/` — repeatable project workflows.
- `04_quality_gates/` — review gates and non-negotiable quality checks.
- `05_prompt_packs/` — reusable prompt patterns.
- `06_drive_maps/` — Google Drive structure and folder contracts.
- `07_locked_decisions/` — approved decisions and active project index.
- `90_templates/` — reusable templates.
- `scripts/` — small helper scripts.

## What Must Not Be Committed

- Client files.
- Raw PDFs, PPTX, DOCX, XLSX, image exports, ZIP files.
- Credentials or API keys.
- Google Drive sync metadata.
- Temporary working files.
- Anything confidential that does not need version-controlled instruction control.
