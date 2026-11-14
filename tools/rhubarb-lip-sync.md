# Rhubarb Lip Sync

- **Type:** CLI
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/DanielSWolf/rhubarb-lip-sync
- **GitHub repo:** https://github.com/DanielSWolf/rhubarb-lip-sync
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Compute/dependencies and third-party model or asset licenses may add costs. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-07

## Safety reason

Targeted source read, not a full dependency/binary audit; DanielSWolf/rhubarb-lip-sync @9b9573c. Offline audio-to-mouth-cue CLI; rhubarb/src/rhubarb/main.cpp:120 entry point. No telemetry found in targeted scan; latest commit April 2025, older speech dependencies. Output is timing data, not a finished animated face. Use trusted audio; Windows binary documented.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows desktop/CLI. Not a native claude.ai tool; no Android app in this reviewed repo.
