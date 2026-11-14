# Hex (anomalyco/hex)

- **Type:** app
- **Category:** voice and audio, Notion and productivity
- **Official URL:** https://github.com/anomalyco/hex
- **GitHub repo:** https://github.com/anomalyco/hex @ 54a3a66 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @54a3a66, a review, 2026-11-02): caution. Self-updater polls anoma.ly every hour; the manifest is unsigned but checked with SHA-256 plus a code signature (`src/updater.rs:1-15,41-45`); turn it off with DisableUpdates. Personal commands can fetch URLs and start programs from your own config (`src/personal_commands.rs:1-8`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: x64 or ARM64 installer from the official GitHub releases (`README.md:21-22`); turn updates off (DisableUpdates). Android: no.
