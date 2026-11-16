# Rhubarb Lip Sync

- **Type:** CLI
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/DanielSWolf/rhubarb-lip-sync
- **GitHub repo:** https://github.com/DanielSWolf/rhubarb-lip-sync
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted source read, not a full dependency/binary audit; DanielSWolf/rhubarb-lip-sync @9b9573c. Offline audio-to-mouth-cue CLI; rhubarb/src/rhubarb/main.cpp:120 entry point. No telemetry found in targeted scan; latest commit April 2025, older speech dependencies. Output is timing data, not a finished animated face. Use trusted audio; Windows binary documented. No fix: last commit April 2025 with older speech-recognition dependencies that get no updates; contained by feeding it only your own audio files.

## Safe install

Safe install (fixes applied):
Windows: download Rhubarb-Lip-Sync-1.14.0-Windows.zip from https://github.com/DanielSWolf/rhubarb-lip-sync/releases (README.adoc:126, release v1.14.0), unpack it to its own folder and run `rhubarb.exe -o cues.txt your.wav` on your own audio. It is offline and has no install step. Skip the Spine and Vegas Pro extras unless you use those apps (README.adoc:61,68). Not a claude.ai, Hermes or Android tool.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows desktop/CLI. Not a native claude.ai tool; no Android app in this reviewed repo.
