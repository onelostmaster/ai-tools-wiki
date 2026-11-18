# planning-with-files (OthmanAdi)

- **Type:** skill
- **Category:** developer tools, automation
- **Official URL:** https://github.com/OthmanAdi/planning-with-files
- **GitHub repo:** https://github.com/OthmanAdi/planning-with-files @ b6580cd (v3.27.0; MIT; ships a `.hermes/skills` copy)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @51bf62d v3.28.1 (2026-11-17): safe with fixes. Hooks on 6 events re-inject task_plan.md, findings.md and progress.md (hooks/hooks.json), so text planted in those files reaches the model each turn. session-catchup.py reads ~/.claude/projects only when you run it (scripts/session-catchup.py:129). No network code. Fix: pin, keep plan files in your own repo and review their diffs.

## Safe install

Safe install (fixes applied):
/plugin marketplace add OthmanAdi/planning-with-files#51bf62d, /plugin install; plan files only in repos you control; review their git diff before each session; Hermes: copy .hermes/skills from the same commit.

## YOLO install

YOLO (your own risk): skips the pin and the diff check.
Install from main and let any tool write the plan files.

## Install notes

Ask the user before installing.
Claude Code: per its README.
Hermes: the repo ships a `.hermes/skills` copy.
