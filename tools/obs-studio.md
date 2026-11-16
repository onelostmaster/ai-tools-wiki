# OBS Studio

- **Type:** app
- **Category:** generating videos, design
- **Official URL:** https://github.com/obsproject/obs-studio
- **GitHub repo:** https://github.com/obsproject/obs-studio
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted source read, not a full dependency/binary audit; obsproject/obs-studio @7a25c3f. Recording/streaming app, not an agent skill. Built-in Windows update check (frontend/widgets/OBSBasic_Updater.cpp:174-203), official updater endpoints (frontend/updater/updater.cpp:41-42). Network streaming/browser sources/plugins are deliberate features. No analytics SDK found in targeted scan; logs can include private source details, review before sharing.

## Safe install

Safe install (fixes applied):
Windows: install the official OBS Studio Windows build from the release page of the official repo (https://github.com/obsproject/obs-studio), reviewed source @7a25c3f. Its built-in update check contacts only the official OBS endpoints (OBSBasic_Updater.cpp:174-203, updater.cpp:41-42); approve updates yourself. Add only plugins and browser sources you trust, and read the log for private source names before sharing it. Not a claude.ai, Hermes or Android tool.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows desktop/CLI. Not a native claude.ai tool; no Android app in this reviewed repo.
