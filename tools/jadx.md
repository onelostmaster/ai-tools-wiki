# jadx

- **Type:** app
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://github.com/skylot/jadx
- **GitHub repo:** https://github.com/skylot/jadx @ c5a451e (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (light code read @c5a451e, a review, 2026-11-02): safe. The GUI checks for updates by default (`JadxSettingsData.java:53`, `JadxUpdate.kt:39`); turn it off in settings.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: official release zip from GitHub (needs Java); turn off the update check. Android: no (works on APK files on the PC).
