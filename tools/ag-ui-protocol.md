# AG-UI protocol

- **Type:** library
- **Category:** developer tools, building a site
- **Official URL:** https://github.com/ag-ui-protocol/ag-ui
- **GitHub repo:** https://github.com/ag-ui-protocol/ag-ui @ 0034593 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @0034593, a review, 2026-11-02): safe. Only its demo "dojo" site loads PostHog (`apps/dojo/instrumentation-client.ts:4`); the SDKs have none.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: `npx create-ag-ui-app my-agent-app` (README). Android: no.
