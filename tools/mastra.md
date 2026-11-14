# Mastra

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://mastra.ai
- **GitHub repo:** https://github.com/mastra-ai/mastra @ 886679e (Apache-2.0, enterprise `ee/` folders separate, `LICENSE.md:1-5`)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); Mastra Platform Starter free, Teams $250/mo (mastra.ai, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @886679e, a review, 2026-11-02): safe. Only the CLI sends PostHog usage events; turn off with MASTRA_TELEMETRY_DISABLED (`packages/cli/src/analytics/index.ts:136`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: `npm create mastra@latest` (README); set MASTRA_TELEMETRY_DISABLED=1. Android: no.
