# Letta Code (letta-ai)

- **Type:** CLI
- **Category:** developer tools, Hermes add-ons
- **Official URL:** https://github.com/letta-ai/letta-code
- **GitHub repo:** https://github.com/letta-ai/letta-code @ 9df436c (Apache-2.0; npm @letta-ai/letta-code 0.34.39; formerly MemGPT, letta-ai/letta is now a pointer README)
- **Price:** Letta Code free, Apache-2.0 (github.com, checked 2026-11-03); Letta Cloud plans not checked
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Claude code read @7cd55dc v0.34.65 (2026-11-18): safe with fixes. Telemetry to api.letta.com is on; LETTA_CODE_TELEM=0 or DO_NOT_TRACK=1 stops it (src/telemetry/index.ts:390-397). Auto-update runs npm install -g unless DISABLE_AUTOUPDATER=1 (src/updater/auto-update.ts:308). Letta Cloud is the default backend; letta backend local keeps memory local (README.md:62). Fix: both env vars, local backend, pin.

## Safe install

Safe install (fixes applied):
Env LETTA_CODE_TELEM=0 and DISABLE_AUTOUPDATER=1 first; npm install @letta-ai/letta-code@0.34.65 in a tools folder (no -g); letta backend local at first launch.

## YOLO install

YOLO (your own risk): skips telemetry off, update off and local backend.
npm install -g @letta-ai/letta-code on Letta Cloud.

## Install notes

Ask the user before installing.
Windows: Node 22+, `npm install -g @letta-ai/letta-code` (a Python wheel for Windows x64 also exists); set LETTA_CODE_TELEM=0 and DISABLE_AUTOUPDATER=1 first and choose the local backend. Works with any model including Claude. Android: chat.letta.com in the browser only.
