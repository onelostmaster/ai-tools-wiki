# OBS Studio

- **Type:** app
- **Category:** generating videos, design
- **Official URL:** https://github.com/obsproject/obs-studio
- **GitHub repo:** https://github.com/obsproject/obs-studio
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Compute/dependencies and third-party model or asset licenses may add costs. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-07

## Safety reason

Targeted source read, not a full dependency/binary audit; obsproject/obs-studio @7a25c3f. Recording/streaming app, not an agent skill. Built-in Windows update check (frontend/widgets/OBSBasic_Updater.cpp:174-203), official updater endpoints (frontend/updater/updater.cpp:41-42). Network streaming/browser sources/plugins are deliberate features. No analytics SDK found in targeted scan; logs can include private source details, review before sharing.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows desktop/CLI. Not a native claude.ai tool; no Android app in this reviewed repo.
