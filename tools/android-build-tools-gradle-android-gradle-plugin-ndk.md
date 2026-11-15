# Android build tools (Gradle, Android Gradle plugin, NDK)

- **Type:** CLI
- **Category:** developer tools, coding
- **Official URL:** https://developer.android.com/build
- **GitHub repo:** https://github.com/gradle/gradle (Gradle); Android Gradle plugin and NDK: unknown
- **Price:** Free
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Official vendors (Gradle Inc., Apache-2.0; Google Android SDK licence for AGP and NDK). a project Claude review (phase1-libraries.md §7): build time only, Gradle SHA-256 checked, CI fails if any library lands on the release runtime classpath; user OK via PR #4 (2026-11-06). Not re-read by a review bot.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: use the project's Gradle wrapper (`gradlew`), which checks the Gradle download's SHA-256; install AGP and the NDK through Android Studio's SDK Manager or the official SDK command-line tools. CI: the NDK preinstalled on ubuntu-24.04 runners, as a project does; build time only, nothing on the release runtime classpath.

## YOLO install

Not written yet.

## Install notes

Claude Code / Windows: let the project Gradle wrapper fetch Gradle (checksum-verified); Android Studio or the SDK command-line tools install AGP and the NDK (developer.android.com/ndk). In CI, a project uses the NDK preinstalled on ubuntu-24.04 runners.
