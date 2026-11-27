# KapeCut (BrewedOps)

- **Type:** app
- **Category:** generating videos, editing
- **Official URL:** https://github.com/brewed-ops/KapeCut
- **GitHub repo:** https://github.com/brewed-ops/KapeCut @ 06d9708 (MIT, except icons in src/renderer/icons.ts)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-26)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-26

## Safety reason

Not code-reviewed for safety. README: Windows 10/11 installer KapeCut-Setup-<version>.exe from GitHub releases is not code-signed (SmartScreen shows "Windows protected your PC"); it updates itself from Settings > Updates; a Setup window checks for ffmpeg, Claude Code, the KapeCut skill (installed to ~/.claude/skills/kapecut) and Chrome/Edge and shows install commands without running them. From source: Node 24 or 26+, npm ci, npm run dev. Icons (Jiggicons) are licensed for KapeCut only. Repo, license and latest commit confirmed from github.com metadata, 2026-11-26.

## Safe install

Unreviewed: contain it: build from source at the pinned commit 06d9708 (npm ci, npm run dev) inside a Windows Sandbox or VM instead of the unsigned .exe, turn off its self-update, no API keys (it needs none). Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Windows: KapeCut-Setup-<version>.exe from the latest GitHub release (unsigned), or from source with Node 24: npm ci, npm run dev (README).
