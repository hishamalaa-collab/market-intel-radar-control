# Machine Bootstrap

Use this file when connecting a new computer to the Market Intel Radar system.

## Required Setup

1. Install Google Drive for desktop.
2. Install GitHub Desktop.
3. Clone the private GitHub repository outside Google Drive.
4. Create `config/local.paths.md` using `config/local.paths.example.md`.
5. Confirm that Google Drive files are reachable on the machine.
6. Confirm that `AGENTS.md` exists at the root of the repo.
7. Confirm that `scripts/validate_structure.py` passes.

## Recommended Local Folder Layout

```text
<user home>/Repos/market-intel-radar-control
<Google Drive>/Knowledge Studio
<Google Drive>/Market Intel Radar
```

## Do Not

- Do not place the GitHub repo inside Google Drive.
- Do not commit local path files.
- Do not commit source PDFs, decks, spreadsheets, image exports, or client files.
- Do not allow Codex to move or rename Google Drive files without explicit instruction.
