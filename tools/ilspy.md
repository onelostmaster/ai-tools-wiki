# ILSpy

- **Type:** app
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://github.com/icsharpcode/ILSpy
- **GitHub repo:** https://github.com/icsharpcode/ILSpy @ baeadcd (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (light code read @baeadcd, a review, 2026-11-02): safe. Weekly update check on by default (`UpdateService.cs:59,112`, `UpdateSettings.cs:45`); ilspycmd has --disable-updatecheck (`IlspyCmdProgram.cs:235`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: official release from GitHub; turn off the update check. Android: no.
