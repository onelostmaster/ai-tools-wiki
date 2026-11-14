# Claude Code Game Studios

- **Type:** skill
- **Category:** 3D and games, developer tools
- **Official URL:** https://github.com/Donchitos/Claude-Code-Game-Studios
- **GitHub repo:** https://github.com/Donchitos/Claude-Code-Game-Studios @ 05ad7c8 (2026-10-19, still HEAD on 2026-11-02; framework 1.2.0; MIT)
- **Price:** Free (MIT, `github.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read of .claude/settings.json, hooks and scripts @05ad7c8, 2026-11-02, no-intake review): Looks safe. Hooks only check and log inside the project; no secrets read, no eval of input, no uploads. Settings auto-allow only dir and pytest, and deny rm -rf, force push, sudo and .env reads. Only network use: a daily GitHub releases check (update-check.sh:132-139), off with updates.check: false. 74 skills and 49 agents are markdown, skimmed not fully read.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code (local only): `git clone https://github.com/Donchitos/Claude-Code-Game-Studios.git my-game`, open Claude Code in that folder and run `/start` (README).
Windows: needs Git for Windows (for Bash) and Python 3 (README).
Note: reviewed at 05ad7c8 (framework 1.2.0). Once a day the session-start hook asks the GitHub releases API for a newer version (`.claude/hooks/update-check.sh`); turn it off with `updates.check: false` in `project.yaml`.
On Windows the notify hook shows a balloon tip through `powershell.exe`.
