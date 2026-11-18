# Langfuse

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://github.com/langfuse/langfuse
- **GitHub repo:** https://github.com/langfuse/langfuse @ 0ca8994 (MIT core, ee folders under a separate licence)
- **Price:** Free to self-host; hosted cloud plans (prices not checked today, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (light code read @0ca8994, a review, 2026-11-02): caution. Self-host telemetry switch TELEMETRY_ENABLED (`web/src/env.mjs:140`, turn it off); repo postinstall is a dev helper (`package.json:20`).

## Safe install

Safe install (fixes applied):
Windows: self-host with Docker Desktop using the repo's docker-compose.yml at commit 0ca8994 with image tags pinned to that release; set TELEMETRY_ENABLED=false in the compose env (web/src/env.mjs:140), otherwise self-host telemetry is on. Bind the web port to localhost. Do not run npm install in the repo itself (the postinstall at package.json:20 is a dev helper you do not need). Or use the hosted Langfuse cloud instead. Android: open the dashboard in a phone browser once hosted.

## YOLO install

YOLO (your own risk): skips the version pin, the telemetry switch and localhost binding.
Windows: docker compose up with the repo defaults; self-host telemetry stays on.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: self-host with Docker (set TELEMETRY_ENABLED=false) or use the hosted cloud. Android: dashboard in a phone browser once hosted.
