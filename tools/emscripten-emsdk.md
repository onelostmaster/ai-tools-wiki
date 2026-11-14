# Emscripten (emsdk)

- **Type:** CLI
- **Category:** developer tools, coding
- **Official URL:** https://emscripten.org
- **GitHub repo:** https://github.com/emscripten-core/emsdk
- **Price:** Free (open source)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-08

## Safety reason

Official upstream (emscripten-core), MIT or UIUC/NCSA. a project Claude review (phase1-libraries.md sections 3 and 7): build tool only, digest-pinned image, no code copied into the repo; user OK via PR #4 (2026-11-06). Not re-read by a review bot.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code / Windows: use the emscripten/emsdk Docker image pinned by digest in a GitHub Actions workflow (as a project bench-web.yml does), or emsdk install/activate locally per emscripten.org. Nothing needed on Android.
