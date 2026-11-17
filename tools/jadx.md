# jadx

- **Type:** app
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://github.com/skylot/jadx
- **GitHub repo:** https://github.com/skylot/jadx @ c5a451e (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @c5a451e, a review, 2026-11-02): safe. The GUI checks for updates by default (`JadxSettingsData.java:53`, `JadxUpdate.kt:39`); turn it off in settings.

## Safe install

Safe install (fixes applied):
Windows: download jadx-gui-1.5.6-with-jre-win.zip (bundles Java) or jadx-1.5.6.zip from the official GitHub release v1.5.6 (2026-07-10) and unzip to its own folder. Verified: the GUI checks for updates on start, on by default (JadxSettingsData.java:53, JadxUpdate.kt:39). Fix: untick the check-for-updates option in Preferences on first start. Unverified: the 1.5.6 binaries (review read source at c5a451e) -> contain: open only APKs you are allowed to decompile. Android: no (it runs on the PC on APK files). Claude Code: can run the jadx CLI. claude.ai, Hermes: no.

## YOLO install

YOLO (your own risk): skips turning off the update check (the GUI keeps contacting GitHub).
Unzip the latest jadx-gui release and run it.

## Install notes

Safe, but ask the user before installing.
Windows: official release zip from GitHub (needs Java); turn off the update check. Android: no (works on APK files on the PC).
