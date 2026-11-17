# ILSpy

- **Type:** app
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://github.com/icsharpcode/ILSpy
- **GitHub repo:** https://github.com/icsharpcode/ILSpy @ baeadcd (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @baeadcd, a review, 2026-11-02): safe. Weekly update check on by default (`UpdateService.cs:59,112`, `UpdateSettings.cs:45`); ilspycmd has --disable-updatecheck (`IlspyCmdProgram.cs:235`).

## Safe install

Safe install (fixes applied):
Windows: download ILSpy_windows_selfcontained_11.2.0.10050-x64.zip (or the x64 .msi) from the official GitHub release v11.2 (2026-10-27) and unzip to its own folder. Verified: it checks icsharpcode.github.io/ILSpy/updates.xml automatically, on by default (UpdateSettings.cs:38,45; UpdateService.cs:59). Fix: turn off the automatic update check in its settings on first start; for ilspycmd add --disable-updatecheck (IlspyCmdProgram.cs:235). Unverified: the v11.2 binaries (review read source at baeadcd) -> contain: open only assemblies you are allowed to decompile. claude.ai, Claude Code, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips turning off the update check (it keeps contacting icsharpcode.github.io).
Install the latest ILSpy .msi from the release page and run it.

## Install notes

Safe, but ask the user before installing.
Windows: official release from GitHub; turn off the update check. Android: no.
