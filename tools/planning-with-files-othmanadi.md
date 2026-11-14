# planning-with-files (OthmanAdi)

- **Type:** skill
- **Category:** developer tools, automation
- **Official URL:** https://github.com/OthmanAdi/planning-with-files
- **GitHub repo:** https://github.com/OthmanAdi/planning-with-files @ b6580cd (v3.27.0; MIT; ships a `.hermes/skills` copy)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @b6580cd, a review, 2026-11-02): caution. Hooks fire on SessionStart, every prompt, before every Write/Edit/Bash/Read/Glob/Grep, after Write/Edit, PreCompact and Stop (`hooks/hooks.json:4-84`) and inject your plan files, so text planted in `task_plan.md` reaches the model each turn. --replay reads Claude Code transcripts in `~/.claude/projects` (`scripts/session-catchup.py:129`), only when asked. No network code.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: per its README.
Hermes: the repo ships a `.hermes/skills` copy.
