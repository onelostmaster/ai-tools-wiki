# Rhubarb Lip Sync

- **Type:** CLI
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/DanielSWolf/rhubarb-lip-sync
- **GitHub repo:** https://github.com/DanielSWolf/rhubarb-lip-sync
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @9b9573c v1.14.0 (2026-11-19): safe with fixes. Offline CLI that turns your audio into mouth-cue timing (rhubarb/src/rhubarb/main.cpp:120); no network, telemetry or installer. Its old speech libraries only parse files you give it, so the fix is to give it only your own audio. Fix: pinned v1.14.0 zip in its own folder, own audio only.

## Safe install

Safe install (fixes applied):
Windows: download Rhubarb-Lip-Sync-1.14.0-Windows.zip from https://github.com/DanielSWolf/rhubarb-lip-sync/releases (README.adoc:126, release v1.14.0), unpack it to its own folder and run rhubarb.exe -o cues.txt your.wav on your own audio. It is offline and has no install step. Skip the Spine and Vegas Pro extras unless you use those apps (README.adoc:61,68). Not a claude.ai, Hermes or Android tool.

## YOLO install

YOLO (your own risk): skips the version pin and the own-audio rule.
Download the latest release zip and run it on any audio.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows desktop/CLI. Not a native claude.ai tool; no Android app in this reviewed repo.
