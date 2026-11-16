# Vercel AI SDK

- **Type:** library
- **Category:** developer tools, building a site
- **Official URL:** https://ai-sdk.dev
- **GitHub repo:** https://github.com/vercel/ai @ 30548ee (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); model calls are paid
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @30548ee, a review, 2026-11-02): safe. Telemetry is opt-in OpenTelemetry (`packages/ai/src/embed/embed-many.ts:71-72`).

## Safe install

Safe install (fixes applied):
Windows (Node.js 22+, packages/ai/package.json engines), in your project: `npm i ai@7.0.162` (the version at the reviewed 30548ee, published 2026-11-03; no install script). Telemetry is off unless you turn on experimental_telemetry yourself (OpenTelemetry, packages/ai/src/embed/embed-many.ts:71-72). Put provider API keys in environment variables for your session or an untracked .env, never in committed code. claude.ai, Claude Code, Hermes, Android: no direct install (it is a library for your own app).

## YOLO install

YOLO (your own risk): skips the version pin (gets 7.0.173 from 2026-11-13, unreviewed).
npm install ai

## Install notes

Safe, but ask the user before installing.
Windows: `npm install ai` (package README, Node 22+). Android: no.
