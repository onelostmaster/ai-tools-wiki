# Pinokio

- **Type:** app
- **Category:** automation, developer tools
- **Official URL:** https://github.com/pinokiocomputer/pinokio
- **GitHub repo:** https://github.com/pinokiocomputer/pinokio @ 102e5ea (2026-11-01, MIT) · engine https://github.com/pinokiocomputer/pinokiod @ add4a67
- **Price:** Free (MIT, github.com, checked 2026-11-01)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read pinokio @ae5f9f3, pinokiod @fc258db (2026-11-17): caution. The main window turns off webSecurity and contextIsolation and gives subframes the preload (full.js:3504-3508), whose electronAPI sends any IPC message (preload.js:99-103). Community scripts run in your shell with your rights (kernel/shell.js). No fix: those settings are hard-coded; only a separate VM contains them.

## Safe install

Safe install (fixes applied):
Only in a VM or spare PC with no personal files; desktop app from the official GitHub releases; verified scripts only; accept updates manually.

## YOLO install

YOLO (your own risk): skips the VM.
Install on your main PC and run any community script.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: desktop app from the official GitHub releases; exact steps not confirmed beyond the repo.
