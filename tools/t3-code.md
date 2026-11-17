# T3 Code

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://t3.codes/
- **GitHub repo:** https://github.com/pingdotgg/t3code (MIT)
- **Price:** Free, open source (MIT); you bring your own agent subscription, no tokens resold (t3.codes, checked 2026-11-01).
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @b5554ac8 (2026-11-16): safe with fixes, Skip. Threads default to full-access (apps/server/src/persistence/Migrations/006_ProjectionThreadSessionRuntimeModeColumns.ts:4), while the server CLI defaults to approval-required (apps/server/src/cli/environment.ts:103). Fix: approval-required. Telemetry off: T3CODE_TELEMETRY_ENABLED=false (apps/desktop/src/backend/DesktopBackendConfiguration.ts:91).

## Safe install

Safe install (fixes applied):
Desktop app from https://t3.codes/download; env T3CODE_TELEMETRY_ENABLED=false before first launch; skip curl|sh and irm|iex installers.

## YOLO install

YOLO (your own risk): skips approval mode and telemetry off.
Install with the one-line installer and keep full access.

## Install notes

Ask the user before installing.
Windows: desktop app from the official download page https://t3.codes/download; before use set the runtime mode to supervised and set `T3CODE_TELEMETRY_ENABLED=false`.
Android: Google Play app linked from the official download page https://t3.codes/download.
Claude Code: T3 Code drives the Claude Code already signed in on your computer (`claude auth login`, per t3.codes).
