# satellite.js

- **Type:** library
- **Category:** research, frontend
- **Official URL:** https://shashwatak.github.io/satellite-js/
- **GitHub repo:** https://github.com/shashwatak/satellite-js @ 696b363
- **Price:** Free, MIT (npm and GitHub, checked 2026-11-12)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot read-only scan @ 696b363 (2026-11-12, npm 7.2.0): no runtime dependencies, no install/postinstall scripts, no fetch, eval, new Function or child_process in src/. MIT, official repo, active.

## Safe install

Safe install (fixes applied):
Claude Code (Windows) or any Node project: `npm install satellite.js@7.2.0 --save-exact` (the reviewed version, still the npm latest on 2026-11-14). No runtime dependencies and no install scripts (code read at 696b363), so nothing else runs at install. Skip the optional WASM build, it is not needed. claude.ai, Hermes and Android: it is a code library, use it inside a project, no install route.

## YOLO install

YOLO (your own risk): skips the exact pin.
npm install satellite.js

## Install notes

Claude Code / Windows: npm install satellite.js@7.2.0 (pin exact). Optional WASM build is not needed for normal use.
