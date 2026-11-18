# Hex (anomalyco/hex)

- **Type:** app
- **Category:** voice and audio, Notion and productivity
- **Official URL:** https://github.com/anomalyco/hex
- **GitHub repo:** https://github.com/anomalyco/hex @ 54a3a66 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @94cbe24 v3.4.0 (2026-11-17): safe with fixes. Dictation runs locally after the first speech-model download (README.md:10). The updater polls hourly; manifests are unsigned but updates must match SHA-256 and the Anomaly code signature (src/updater.rs:1-15, updater/windows.rs:37). Personal commands reach fetch or child_process only after you trust that config (src/personal_commands.rs:5-7). Fix: DisableUpdates.

## Safe install

Safe install (fixes applied):
Windows x64/ARM64 installer from the official GitHub releases (v3.4.0); reg add HKCU\\SOFTWARE\\Policies\\Anomaly\\Hex /v DisableUpdates /t REG_DWORD /d 1 /f; trust only personal-command configs you wrote.

## YOLO install

YOLO (your own risk): skips the update switch.
Install from releases and let it update itself hourly.

## Install notes

Ask the user before installing.
Windows: x64 or ARM64 installer from the official GitHub releases (`README.md:21-22`); turn updates off (DisableUpdates). Android: no.
