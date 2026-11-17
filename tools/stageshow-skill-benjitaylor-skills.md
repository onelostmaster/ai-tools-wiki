# Stageshow skill (benjitaylor/skills)

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://github.com/benjitaylor/skills
- **GitHub repo:** https://github.com/benjitaylor/skills (stageshow/, MIT)
- **Price:** Free, open source (MIT; third-party asset notices in `stageshow/NOTICE.md`) (github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @8020574) and Claude (@8020574), 2026-11-01: Looks safe. No postinstall, telemetry, eval or remote downloads; deps from npm. Scripts drive local Chrome via playwright-core against the local preview, spawn only Node and Vite (shell: false). Heads-up: tells the agent to run npm install and a dev server; README installer is unpinned; app icons in `assets/app-icons.ts` are not MIT.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): copy the stageshow folder from reviewed commit 8020574 of github.com/benjitaylor/skills into %USERPROFILE%\.claude\\skills\\stageshow and start a new session. Needs Node and a local Chrome. The skill tells the agent to run npm install and a Vite dev server in your project: keep Claude Code asking before each command and say yes to those two only. Filming drives your local Chrome via playwright-core against the local preview, spawning only Node and Vite with shell: false. App icons in assets/app-icons.ts are not MIT: do not ship them.
Hermes: copy the same folder into ~/.hermes/skills/<category>/stageshow/.

## YOLO install

YOLO (your own risk): skips the commit pin and the per-command approval.
npx skills add benjitaylor/skills --skill stageshow (README; unpinned third-party installer), at HEAD, with commands auto-approved.

## Install notes

Claude Code: README route `npx skills add benjitaylor/skills --skill stageshow` (unpinned third-party installer), or copy the `stageshow` folder into `~/.claude/skills/` (Windows: `%USERPROFILE%\.claude\skills\`) and start a new session; needs Node and a local Chrome for filming.
Hermes: unconfirmed: copy the same folder into `~/.hermes/skills/` and start a new session.
