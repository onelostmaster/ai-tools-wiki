# Apktool

- **Type:** CLI
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://apktool.org
- **GitHub repo:** https://github.com/iBotPeaches/Apktool @ 2062db6 (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @2062db6, a review, 2026-11-02): safe. No telemetry or updater found.

## Safe install

Safe install (fixes applied):
Windows (Java 8+ runtime; the build targets release 8, build.gradle.kts:85): download apktool_3.0.3.jar from the official GitHub release v3.0.3 (2026-07-20) and the Windows wrapper per apktool.org install docs, into one folder on your user PATH. No telemetry or updater found at 2062db6, so nothing to switch off. Unverified: the 3.0.3 jar (review read source at 2062db6) -> contain: work only on APKs you are allowed to modify, in a folder of their own. Android: no (it runs on the PC on APK files). claude.ai, Claude Code (can run the CLI once on PATH), Hermes: no.

## YOLO install

YOLO (your own risk): skips the pinned version.
Download the newest apktool jar and run java -jar apktool.jar.

## Install notes

Safe, but ask the user before installing.
Windows: official jar and wrapper per apktool.org (needs Java). Android: no (works on APK files on the PC).
