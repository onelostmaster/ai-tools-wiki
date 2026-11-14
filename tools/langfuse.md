# Langfuse

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://github.com/langfuse/langfuse
- **GitHub repo:** https://github.com/langfuse/langfuse @ 0ca8994 (MIT core, ee folders under a separate licence)
- **Price:** Free to self-host; hosted cloud plans (prices not checked today, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @0ca8994, a review, 2026-11-02): caution. Self-host telemetry switch TELEMETRY_ENABLED (`web/src/env.mjs:140`, turn it off); repo postinstall is a dev helper (`package.json:20`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: self-host with Docker (set TELEMETRY_ENABLED=false) or use the hosted cloud. Android: dashboard in a phone browser once hosted.
