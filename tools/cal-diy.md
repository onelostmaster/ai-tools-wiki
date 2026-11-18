# Cal.diy

- **Type:** app
- **Category:** Notion and productivity
- **Official URL:** https://github.com/calcom/cal.diy
- **GitHub repo:** [https://github.com/calcom/cal.diy](https://github.com/calcom/cal.diy)
- **Price:** Free (MIT)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (scanned for telemetry, installers, updaters and keys, not fully read; a review, a5ee96f): Looks safe. Telemetry is on unless you set `CALCOM_TELEMETRY_DISABLED` (`.env.example:64`).

## Safe install

Safe install (fixes applied):
Self-hosted server (Docker): follow the repo docs at https://github.com/calcom/cal.diy (no confirmed command yet) and set CALCOM_TELEMETRY_DISABLED=1 in .env before first start; telemetry is on otherwise (.env.example:64; a review, a5ee96f).

## YOLO install

YOLO (your own risk): skips the telemetry switch.
The repo's Docker setup with the default .env (telemetry on).

## Install notes

Self-hosted server (Docker): no confirmed command yet; follow the official docs at [https://github.com/calcom/cal.diy](https://github.com/calcom/cal.diy)
