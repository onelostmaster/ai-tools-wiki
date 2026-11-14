# Vercel AI SDK

- **Type:** library
- **Category:** developer tools, building a site
- **Official URL:** https://ai-sdk.dev
- **GitHub repo:** https://github.com/vercel/ai @ 30548ee (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); model calls are paid
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @30548ee, a review, 2026-11-02): safe. Telemetry is opt-in OpenTelemetry (`packages/ai/src/embed/embed-many.ts:71-72`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: `npm install ai` (package README, Node 22+). Android: no.
