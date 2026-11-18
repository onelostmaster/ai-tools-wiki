# Plane

- **Type:** app
- **Category:** Notion and productivity
- **Official URL:** https://plane.so/open-source
- **GitHub repo:** [https://github.com/makeplane/plane](https://github.com/makeplane/plane) (confirmed on Plane's self-hosting docs, 2026-10-31)
- **Price:** Free self-host (AGPL)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code scan, b98e1de, a project a review, 2026-10-31): Looks safe. Mature self-hosted server (Docker); the big app was scanned for telemetry, installers, updaters and keys, not fully read. Instance telemetry is on by default (`apps/api/plane/license/api/views/admin.py:131`).

## Safe install

Safe install (fixes applied):
Windows (Docker Desktop): follow the official Docker Compose guide at https://developers.plane.so/self-hosting/methods/docker-compose, keep the web port bound to 127.0.0.1 unless others need it, and switch off instance telemetry in the instance admin settings after setup (it is on by default: apps/api/plane/license/api/views/admin.py:131, a review bot a review). unverified: the exact name of that admin setting.

## YOLO install

YOLO (your own risk): skips the localhost binding and telemetry switch-off.
Follow the official Docker Compose guide as written (telemetry stays on).

## Install notes

Self-hosted server (Docker): no confirmed command yet; follow the official docs at [https://developers.plane.so/self-hosting/methods/docker-compose](https://developers.plane.so/self-hosting/methods/docker-compose) (instance telemetry is on by default).
