# OpenLIT

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://github.com/openlit/openlit
- **GitHub repo:** https://github.com/openlit/openlit @ 4f095b5 (Apache-2.0)
- **Price:** Free to self-host; hosted plans (prices not checked today, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (light code read @4f095b5, a review, 2026-11-02): caution. Server posts events to us.i.posthog.com unless TELEMETRY_ENABLED=false (`src/client/src/lib/posthog.ts:22-27`, `constants/posthog.ts:3`). README offers a curl | sh installer (`README.md:150`): use Docker or pip instead.

## Safe install

Safe install (fixes applied):
Windows: Docker Desktop, the docker-compose.yml from the repo at commit 4f095b5 with image tags pinned to that release (never the curl | sh installer, README.md:150). Set TELEMETRY_ENABLED=false in the compose env; otherwise the server posts events to us.i.posthog.com (src/client/src/lib/posthog.ts:22-27). Bind the dashboard to localhost only. SDK: pip install openlit==<same release> in a venv. Android: no.

## YOLO install

YOLO (your own risk): skips the version pin, the telemetry switch and localhost binding.
Windows: curl | sh installer from README.md:150; PostHog telemetry stays on.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: Docker or pip (not tested), never the curl | sh installer; set TELEMETRY_ENABLED=false.
