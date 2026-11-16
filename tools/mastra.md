# Mastra

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://mastra.ai
- **GitHub repo:** https://github.com/mastra-ai/mastra @ 886679e (Apache-2.0, enterprise `ee/` folders separate, `LICENSE.md:1-5`)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); Mastra Platform Starter free, Teams $250/mo (mastra.ai, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @886679e, a review, 2026-11-02): safe. Only the CLI sends PostHog usage events; turn off with MASTRA_TELEMETRY_DISABLED (`packages/cli/src/analytics/index.ts:136`).

## Safe install

Safe install (fixes applied):
Windows (Node.js 22.13+, packages/core/package.json engines): first set `MASTRA_TELEMETRY_DISABLED=1` (PowerShell: `$env:MASTRA_TELEMETRY_DISABLED='1'`, or set it in your user environment); without it the mastra and create-mastra CLIs send PostHog usage events (packages/create-mastra/src/index.ts:16-20, packages/cli/src/analytics/index.ts:135-140). Then in your own project `npm i @mastra/core@1.82.0-alpha.2 mastra@1.38.0-alpha.2` (the versions at the reviewed 886679e; prerelease builds, no install scripts). Skip `npm create mastra@latest`: it installs the project packages by npm dist-tag at run time, not pinned (packages/create-mastra/src/utils.ts:49-62, packages/cli/src/commands/create/create.ts:347). The Mastra Platform (cloud) is not part of the review. claude.ai, Claude Code, Hermes, Android: no direct install.

## YOLO install

YOLO (your own risk): skips the version pins (gets 1.39.0 / core 1.83.0 from 2026-11-12, unreviewed); telemetry stays off only if you still set MASTRA_TELEMETRY_DISABLED=1.
npm create mastra@latest

## Install notes

Safe, but ask the user before installing.
Windows: set MASTRA_TELEMETRY_DISABLED=1, then pinned packages; see Safe install. Android: no.
