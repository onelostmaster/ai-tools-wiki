# AppFlowy

- **Type:** app
- **Category:** Notion and productivity
- **Official URL:** https://github.com/AppFlowy-IO/AppFlowy
- **GitHub repo:** [https://github.com/AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)
- **Price:** Free (AGPL)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (scanned for telemetry, installers, updaters and keys, not fully read; a review, 8fcee27): Looks safe. Phone-home telemetry: a Sentry DSN is set at build (`frontend/appflowy_flutter/lib/env/env.dart:43`).

## Safe install

Safe install (fixes applied):
Windows: install from the official packages page https://docs.appflowy.io/docs/appflowy/install-appflowy/installation-methods/mac-windows-linux-packages. Android: from https://appflowy.com. The official builds send crash reports to Sentry (DSN set at build, frontend/appflowy_flutter/lib/env/env.dart:43; a review, 8fcee27); unverified: whether a setting turns that off, so keep no keys or passwords in AppFlowy pages. Self-host: official guide https://docs.appflowy.io/docs/guides/appflowy/self-hosting-appflowy.

## YOLO install

Not written yet.

## Install notes

Windows: no confirmed command yet; follow the official docs at [https://docs.appflowy.io/docs/appflowy/install-appflowy/installation-methods/mac-windows-linux-packages](https://docs.appflowy.io/docs/appflowy/install-appflowy/installation-methods/mac-windows-linux-packages)
Android: no confirmed command yet; follow the official site at [https://appflowy.com](https://appflowy.com)
Self-hosted server (Docker): no confirmed command yet; follow the official self-hosting guide at [https://docs.appflowy.io/docs/guides/appflowy/self-hosting-appflowy](https://docs.appflowy.io/docs/guides/appflowy/self-hosting-appflowy)
