# x64dbg

- **Type:** app
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://x64dbg.com
- **GitHub repo:** https://github.com/x64dbg/x64dbg @ 79d5716 (GPL-3.0)
- **Price:** Free, open source (x64dbg.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @79d5716, a review, 2026-11-02): safe. Checks for updates only when you pick it in the Help menu (`MainWindow.cpp:2910-2913`, `UpdateChecker.cpp:175`).

## Safe install

Safe install (fixes applied):
Windows: download snapshot_2026-05-27_12-11.zip from the official GitHub release 2026.05.27 (or x64dbg.com), unzip to its own folder and run release\\x96dbg.exe. It checks for updates only when you choose it in the Help menu (MainWindow.cpp:2910-2913, UpdateChecker.cpp:175), so nothing to switch off. Unverified: the snapshot binaries and third-party plugins -> contain: add only plugins you trust, attach only to your own or single-player programs (online games' anti-cheat bans debuggers), and debug unknown malware only in a VM. claude.ai, Claude Code, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the plugin and VM limits.
Unzip the latest snapshot and run x96dbg.exe.

## Install notes

Safe, but ask the user before installing.
Windows: official snapshot from x64dbg.com or GitHub releases. Android: no.
