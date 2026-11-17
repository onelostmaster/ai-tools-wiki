# motionbrief (YahyaLendani/motionbrief-claude-skills)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/YahyaLendani/motionbrief-claude-skills
- **GitHub repo:** https://github.com/YahyaLendani/motionbrief-claude-skills @ ed65700 (MIT)
- **Price:** Free, open source (MIT) (github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude (a project Tool Scout, code read @ed65700, 2026-11-01): safe. No network, no shell. No other findings given.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): download the repo at reviewed commit ed65700 (github.com/YahyaLendani/motionbrief-claude-skills/archive/ed65700.zip), unzip it and run powershell -NoProfile -File .\\install.ps1 from the folder (README Quick start). install.ps1 copies skills/motionbrief and the /motion command (.claude/commands/motion.md) into %USERPROFILE%\.claude; add -DryRun first to see the exact copies, or -Project to install into this project only. Then restart Claude Code. The render checks need Node 22+ and a Chrome (README lines 107-110); the static checks need no network.

## YOLO install

YOLO (your own risk): skips the commit pin.
npx skills add YahyaLendani/motionbrief-claude-skills (README Quick start; third-party installer, not reviewed), at HEAD.

## Install notes

Claude Code: copy the skill folder from the official repo into `~/.claude/skills/` (Windows: `%USERPROFILE%\.claude\skills\`) and start a new session (unconfirmed: check the repo README first).
