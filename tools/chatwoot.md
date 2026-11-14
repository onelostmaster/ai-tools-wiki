# Chatwoot

- **Type:** app
- **Category:** messaging
- **Official URL:** https://developers.chatwoot.com/self-hosted
- **GitHub repo:** [https://github.com/chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) (not in the source; confirmed from Chatwoot's official docs, 2026-10-31)
- **Price:** Free self-host (MIT + enterprise)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code scan, b08081b, a review): Looks safe. Mature self-hosted server (Docker); it phones home (telemetry) by registering with Chatwoot's hub during onboarding. The big app was scanned for telemetry, installers, updaters and keys, not fully read.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Server (Docker): per Chatwoot's official guide, download its `.env` and `docker-compose.yaml` templates, set the Postgres and Redis passwords, run `docker compose run --rm rails bundle exec rails db:chatwoot_prepare`, then `docker compose up -d`. Guide: [https://developers.chatwoot.com/self-hosted/deployment/docker](https://developers.chatwoot.com/self-hosted/deployment/docker)
