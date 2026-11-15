# Emscripten (emsdk)

- **Type:** CLI
- **Category:** developer tools, coding
- **Official URL:** https://emscripten.org
- **GitHub repo:** https://github.com/emscripten-core/emsdk
- **Price:** Free (open source)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Official upstream (emscripten-core), MIT or UIUC/NCSA. a project Claude review (phase1-libraries.md sections 3 and 7): build tool only, digest-pinned image, no code copied into the repo; user OK via PR #4 (2026-11-06). Not re-read by a review bot.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: no local install; build in GitHub Actions with the emscripten/emsdk Docker image pinned by digest (`image: emscripten/emsdk@sha256:<digest>`), as a project's bench-web.yml does. Android: nothing needed.

## YOLO install

YOLO (your own risk): skips the digest-pinned container.
Local `./emsdk install latest` then `./emsdk activate latest` (emscripten.org).

## Install notes

Claude Code / Windows: use the emscripten/emsdk Docker image pinned by digest in a GitHub Actions workflow (as a project bench-web.yml does), or emsdk install/activate locally per emscripten.org. Nothing needed on Android.
