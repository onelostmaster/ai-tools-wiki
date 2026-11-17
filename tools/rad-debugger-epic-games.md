# RAD Debugger (Epic Games)

- **Type:** app
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://github.com/EpicGames/raddebugger
- **GitHub repo:** https://github.com/EpicGames/raddebugger @ 5ddba64 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @5ddba64, a review, 2026-11-02): safe. The RAD Telemetry profiler is built in only with a build flag (`build.bat:28,46`). Alpha software.

## Safe install

Safe install (fixes applied):
Windows: download raddbg.zip from the official GitHub release v0.9.29-alpha (2026-09-30) and unzip to its own folder (no installer). The RAD Telemetry profiler is compiled in only with a build flag (build.bat:28,46), so the release build needs no change. Unverified: the release binaries (the review read source at 5ddba64) -> contain: run it only on your own programs, keep it in its own folder, and use the source build (build.bat) if you want to match the reviewed code. Alpha software: expect crashes. claude.ai, Claude Code, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the source build and runs the newest alpha raddbg.exe straight from the release page.
Download raddbg.exe from the latest release and run it.

## Install notes

Safe, but ask the user before installing.
Windows: official release from GitHub. Android: no.
