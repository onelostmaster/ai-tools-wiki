# Chatwoot

- **Type:** app
- **Category:** messaging
- **Official URL:** https://developers.chatwoot.com/self-hosted
- **GitHub repo:** [https://github.com/chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) (not in the source; confirmed from Chatwoot's official docs, 2026-10-31)
- **Price:** Free self-host (MIT + enterprise)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code scan, b08081b, a review): Looks safe. Mature self-hosted server (Docker); it phones home (telemetry) by registering with Chatwoot's hub during onboarding. The big app was scanned for telemetry, installers, updaters and keys, not fully read.

## Safe install

Safe install (fixes applied):
Server (Docker, official guide https://developers.chatwoot.com/self-hosted/deployment/docker): download its .env and docker-compose.yaml, set strong Postgres and Redis passwords in .env, docker compose run --rm rails bundle exec rails db:chatwoot_prepare, then docker compose up -d. It registers with Chatwoot's hub during onboarding ; unverified: which .env setting turns that off, so check the .env template for a telemetry switch before first start. Only the telemetry, installer, updater and key paths were scanned.

## YOLO install

YOLO (your own risk): skips the telemetry check.
Same Docker steps with the template defaults apart from the passwords.

## Install notes

Server (Docker): per Chatwoot's official guide, download its `.env` and `docker-compose.yaml` templates, set the Postgres and Redis passwords, run `docker compose run --rm rails bundle exec rails db:chatwoot_prepare`, then `docker compose up -d`. Guide: [https://developers.chatwoot.com/self-hosted/deployment/docker](https://developers.chatwoot.com/self-hosted/deployment/docker)
