# Anatomy skill

- **Type:** skill
- **Category:** editing, design
- **Official URL:** https://github.com/wheresryan22/anatomy
- **GitHub repo:** [https://github.com/wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)
- **Price:** Free (open-source code)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, a review, 2026-10-28): Looks safe. Node built-ins only; scripts only talk to a local headless Chrome (`scripts/drive.mjs`); the gallery publish script (`scripts/publish.mjs`) only pushes via gh when run with `--submit`.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): git clone https://github.com/wheresryan22/anatomy.git %USERPROFILE%\.claude\\skills\\anatomy, then start a new session. This skips the skills CLI and its install telemetry to skills.sh. Never run scripts/publish.mjs with --submit unless you want it pushed to the gallery via gh . Hermes: clone into ~/.hermes/skills/creative/anatomy/.

## YOLO install

YOLO (your own risk): skips the plain clone.
npx skills add wheresryan22/anatomy -g -a claude-code (sends install telemetry to skills.sh unless DISABLE_TELEMETRY=1 is set).

## Install notes

Claude Code: `npx skills add wheresryan22/anatomy -g -a claude-code` or `git clone https://github.com/wheresryan22/anatomy.git ~/.claude/skills/anatomy`
Hermes: unconfirmed: clone into `~/.hermes/skills/creative/anatomy/`, then start a new session
