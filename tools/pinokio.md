# Pinokio

- **Type:** app
- **Category:** automation, developer tools
- **Official URL:** https://github.com/pinokiocomputer/pinokio
- **GitHub repo:** https://github.com/pinokiocomputer/pinokio @ 102e5ea (2026-11-01, MIT) · engine https://github.com/pinokiocomputer/pinokiod @ add4a67
- **Price:** Free (MIT, github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read pinokio @102e5ea, pinokiod @add4a67, a review, 2026-11-01): Use with caution. Runs community install scripts in a real shell with your user rights (`kernel/shell.js:12,862`); main window disables webSecurity and context isolation and gives subframes Node (`full.js:3504-3508`); update check on launch, download only after you agree. Launch telemetry is a local record only; peer networking off by default.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: desktop app from the official GitHub releases; exact steps not confirmed beyond the repo.
