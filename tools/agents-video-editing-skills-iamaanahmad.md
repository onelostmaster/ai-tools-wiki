# agents-video-editing-skills (iamaanahmad)

- **Type:** skill
- **Category:** editing, generating videos
- **Official URL:** https://github.com/iamaanahmad/agents-video-editing-skills
- **GitHub repo:** https://github.com/iamaanahmad/agents-video-editing-skills @ 981466b (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-26)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-26

## Safety reason

Not code-reviewed for safety. README: npx agents-video-editing-skills --agent claude --rules writes skills and instruction files into the current project; --scope user writes them for every project on the machine; --dry-run shows the files first; a clone install uses python scripts/install.py (Python 3.9+, standard library only); Windows PowerShell supported. Skills use FFmpeg and some need Node.js or Python packages (each skill says which). Repo, license and latest commit confirmed from github.com metadata, 2026-11-26.

## Safe install

Unreviewed: contain it: clone at the pinned commit 981466b, run python scripts/install.py --agent claude --project <sandbox project> --dry-run first, then the same without --dry-run; never --scope user or --rules (they write outside the skill folder); no API keys. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code (Windows): python scripts/install.py --agent claude --project "C:\\path\\to\\project" --dry-run, then without --dry-run (README).
