# Market Intel Radar — Agent Instructions

This repository controls the operating instructions, workflows, role cards, prompt packs, locked decisions, and quality gates for the Market Intel Radar / Knowledge Studio environment.

## Core Architecture

GitHub is the source of truth for instructions.
Google Drive is the source of truth for project files, documents, source assets, client materials, exports, and bulky files.

Do not treat Google Drive as the instruction control layer.
Do not store client documents, source PDFs, decks, spreadsheets, exports, credentials, or large media files in this repo.

## Before Starting Any Task

1. Read `00_boot/project_boot.md`.
2. Read the relevant role file from `02_roles/`.
3. Check `07_locked_decisions/locked_decisions.md`.
4. If the task touches Google Drive, check `06_drive_maps/google_drive_structure.md` and `06_drive_maps/folder_contracts.md`.
5. If the task creates or modifies instructions, update `CHANGELOG.md`.
6. If the task produces a reusable method, add it to the relevant workflow, quality gate, prompt pack, or template.

## Non-Negotiables

- Do not reinvent approved copy, structures, brand rules, project flows, or role logic.
- Do not move or rename Google Drive files unless explicitly instructed.
- Treat documents as inputs; topics, reusable knowledge, decision logs, and operating instructions are the product.
- Prefer small, reviewable changes over sweeping rewrites.
- When uncertain, produce a review note rather than silently changing the system.
- Maintain a clear distinction between source material, working notes, approved decisions, and reusable outputs.

## Commit Discipline

Use clear commit messages such as:

- `Update Knowledge Studio ingestion workflow`
- `Add Codex machine bootstrap guide`
- `Refine no-reinvention quality gate`
- `Document Drive folder contracts`

Avoid vague commit messages such as `updates`, `fix`, or `changes`.

## Main References

- Project boot: `00_boot/project_boot.md`
- Session protocol: `00_boot/session_start_protocol.md`
- Constitution: `01_constitution/chatgpt_native_constitution.md`
- Operating principles: `01_constitution/operating_principles.md`
- Drive map: `06_drive_maps/google_drive_structure.md`
- Locked decisions: `07_locked_decisions/locked_decisions.md`
- Quality gates: `04_quality_gates/`
