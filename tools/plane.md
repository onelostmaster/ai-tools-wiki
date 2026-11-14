# Plane

- **Type:** app
- **Category:** Notion and productivity
- **Official URL:** https://plane.so/open-source
- **GitHub repo:** [https://github.com/makeplane/plane](https://github.com/makeplane/plane) (confirmed on Plane's self-hosting docs, 2026-10-31)
- **Price:** Free self-host (AGPL)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code scan, b98e1de, a project a review, 2026-10-31): Looks safe. Mature self-hosted server (Docker); the big app was scanned for telemetry, installers, updaters and keys, not fully read. Instance telemetry is on by default (`apps/api/plane/license/api/views/admin.py:131`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Self-hosted server (Docker): no confirmed command yet; follow the official docs at [https://developers.plane.so/self-hosting/methods/docker-compose](https://developers.plane.so/self-hosting/methods/docker-compose) (instance telemetry is on by default).
