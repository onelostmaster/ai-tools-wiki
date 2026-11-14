# Letta Code (letta-ai)

- **Type:** CLI
- **Category:** developer tools, Hermes add-ons
- **Official URL:** https://github.com/letta-ai/letta-code
- **GitHub repo:** https://github.com/letta-ai/letta-code @ 9df436c (Apache-2.0; npm @letta-ai/letta-code 0.34.39; formerly MemGPT, letta-ai/letta is now a pointer README)
- **Price:** Letta Code free, Apache-2.0 (github.com, checked 2026-11-03); Letta Cloud plans not checked
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-04

## Safety reason

a review bot (light code read @9df436c, 2026-11-03): caution. Telemetry on by default to api.letta.com with a persistent device ID (`src/telemetry/index.ts:392-404`, `src/backend/api/metadata.ts:69-76,102-117`); it sends input length and command names, not prompt text (`src/telemetry/index.ts:806-821`); opt out with LETTA_CODE_TELEM=0 or DO_NOT_TRACK=1. Auto-update on by default via npm install -g (`src/updater/auto-update.ts:307-308`), off with DISABLE_AUTOUPDATER=1. Letta Cloud is the default backend and stores memory and conversations (`README.md:62,68`); pick local at first launch or `letta backend local`. Agents can self-configure hooks and permissions (`README.md:17`). postinstall only patches vendor files (`package.json:224`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: Node 22+, `npm install -g @letta-ai/letta-code` (a Python wheel for Windows x64 also exists); set LETTA_CODE_TELEM=0 and DISABLE_AUTOUPDATER=1 first and choose the local backend. Works with any model including Claude. Android: chat.letta.com in the browser only.
