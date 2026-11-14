# Anatomy skill

- **Type:** skill
- **Category:** editing, design
- **Official URL:** https://github.com/wheresryan22/anatomy
- **GitHub repo:** [https://github.com/wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)
- **Price:** Free (open-source code)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a review, 2026-10-28): Looks safe. Node built-ins only; scripts only talk to a local headless Chrome (`scripts/drive.mjs`); the gallery publish script (`scripts/publish.mjs`) only pushes via gh when run with `--submit`.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `npx skills add wheresryan22/anatomy -g -a claude-code` or `git clone https://github.com/wheresryan22/anatomy.git ~/.claude/skills/anatomy`
Hermes: unconfirmed: clone into `~/.hermes/skills/creative/anatomy/`, then start a new session
