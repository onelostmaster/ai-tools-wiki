# T3 Code

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://t3.codes/
- **GitHub repo:** https://github.com/pingdotgg/t3code (MIT)
- **Price:** Free, open source (MIT); you bring your own agent subscription, no tokens resold (t3.codes, checked 2026-11-01).
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (code read @3fd2b855) and Claude (@57d764ea), 2026-11-01: caution. No malware signs. Defaults to full-access mode (Claude runs with bypassPermissions); telemetry on by default incl. hashed account ids (opt out `T3CODE_TELEMETRY_ENABLED=false`); desktop app auto-updates; installers pipe curl/irm to the shell.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: desktop app from the official download page https://t3.codes/download; before use set the runtime mode to supervised and set `T3CODE_TELEMETRY_ENABLED=false`.
Android: Google Play app linked from the official download page https://t3.codes/download.
Claude Code: T3 Code drives the Claude Code already signed in on your computer (`claude auth login`, per t3.codes).
