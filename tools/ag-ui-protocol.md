# AG-UI protocol

- **Type:** library
- **Category:** developer tools, building a site
- **Official URL:** https://github.com/ag-ui-protocol/ag-ui
- **GitHub repo:** https://github.com/ag-ui-protocol/ag-ui @ 0034593 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @0034593, a review, 2026-11-02): safe. Only its demo "dojo" site loads PostHog (`apps/dojo/instrumentation-client.ts:4`); the SDKs have none.

## Safe install

Safe install (fixes applied):
Windows (Node.js), in your own app project: `npm i @ag-ui/core@1.0.3 @ag-ui/client@1.0.3` (the SDK versions at the reviewed 0034593, sdks/typescript/packages/core and client package.json; no install scripts). Skip `npx create-ag-ui-app`: it runs `npx copilotkit@latest` (sdks/typescript/packages/cli/src/build-args.ts:6, index.ts:94), the unpinned CopilotKit CLI, which has its own caution row. The SDKs send no telemetry; only the demo dojo site loads PostHog (apps/dojo/instrumentation-client.ts:4), so don't run the dojo. claude.ai, Claude Code, Hermes, Android: no direct install (it is a library for your own app).

## YOLO install

YOLO (your own risk): skips the version pins and runs the unpinned CopilotKit CLI.
npx create-ag-ui-app my-agent-app

## Install notes

Safe, but ask the user before installing.
Windows: SDK packages pinned; see Safe install (create-ag-ui-app runs the unpinned CopilotKit CLI). Android: no.
