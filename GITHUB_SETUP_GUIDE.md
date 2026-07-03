# GitHub Setup Guide — Non-Technical Path

This guide assumes you have a GitHub account but are not fluent with GitHub.

## Goal

Create one private GitHub repository named:

```text
market-intel-radar-control
```

This repo will hold the Market Intel Radar instruction/control system. Google Drive will continue to hold source documents, decks, reports, exports, and client materials.

---

## Part 1 — Create the Private GitHub Repository

1. Open GitHub in your browser.
2. Sign in.
3. Click the `+` icon in the top right.
4. Choose `New repository`.
5. Repository name:

```text
market-intel-radar-control
```

6. Description:

```text
Instruction and control repository for Market Intel Radar / Knowledge Studio.
```

7. Visibility: choose `Private`.
8. Do not add README, .gitignore, or license if you are uploading this starter pack.
9. Click `Create repository`.
	
---

## Part 2 — Upload the Starter Pack Through the Browser

Use this option first if you do not want to use command line yet.

1. Unzip `market-intel-radar-control-starter.zip` on your computer.
2. Open the new GitHub repository page.
3. Click `uploading an existing file` or `Add file` → `Upload files`.
4. Drag all files and folders from inside the unzipped starter folder into GitHub.
5. At the bottom, write commit message:

```text
Initial Market Intel Radar control repo
```

6. Click `Commit changes`.

Important: upload the contents of the starter folder, not the zip file itself.

---

## Part 3 — Install GitHub Desktop

This is the easier path for daily use.

1. Download and install GitHub Desktop.
2. Sign in using your GitHub account.
3. In GitHub Desktop, choose `File` → `Clone repository`.
4. Select `market-intel-radar-control`.
5. Choose a local path outside Google Drive, for example:

Windows:

```text
C:\Users\<YourName>\Repos\market-intel-radar-control
```

Mac:

```text
/Users/<YourName>/Repos/market-intel-radar-control
```

6. Click `Clone`.

---

## Part 4 — Connect Google Drive Without Putting Git Inside Drive

Install Google Drive for desktop on each machine.

Your machine should look like this:

```text
Local machine
├── Repos/market-intel-radar-control       ← GitHub repo
└── Google Drive/Knowledge Studio          ← Drive files
```

Do not put this inside Google Drive:

```text
Google Drive/market-intel-radar-control    ← avoid this
```

---

## Part 5 — Create Your Local Path File

On each machine, copy:

```text
config/local.paths.example.md
```

Rename the copy to:

```text
config/local.paths.md
```

Edit it with the correct Google Drive path for that machine.

Do not upload `config/local.paths.md` to GitHub. It is ignored by `.gitignore`.

---

## Part 6 — Daily Workflow Using GitHub Desktop

Before working:

1. Open GitHub Desktop.
2. Select `market-intel-radar-control`.
3. Click `Fetch origin`.
4. If it changes to `Pull origin`, click it.

After editing files:

1. Open GitHub Desktop.
2. Review the changed files.
3. Write a short summary, for example:

```text
Update Drive ingestion workflow
```

4. Click `Commit to main`.
5. Click `Push origin`.

---

## Part 7 — Codex Machine Setup

On the dedicated Codex machine:

1. Install Google Drive for desktop.
2. Install GitHub Desktop.
3. Sign in to GitHub Desktop.
4. Clone `market-intel-radar-control` outside Google Drive.
5. Create `config/local.paths.md` on that machine.
6. Start Codex from inside the repo folder.
7. Make sure Codex reads `AGENTS.md` before working.

---

## Part 8 — Simple Rules

- GitHub controls instructions.
- Google Drive stores files.
- Do not upload client files to GitHub.
- Do not upload PDFs, decks, images, or exports to GitHub.
- Use small changes and clear commit messages.
- If something is approved, document it in `07_locked_decisions/locked_decisions.md`.
- If a workflow changes, update the relevant file in `03_workflows/` and add a line to `CHANGELOG.md`.
