# Composio

- **Type:** API
- **Category:** automation, developer tools
- **Official URL:** https://composio.dev
- **GitHub repo:** https://github.com/ComposioHQ/composio @ a0c51b0 (MIT SDKs; cloud closed)
- **Price:** Hobby free (100K tool calls a month), Pro $29/mo + usage (composio.dev, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @a0c51b0, a review / Hermes a review, 2026-11-02): caution. Holds your app OAuth tokens in its cloud (third-party storage, broad scopes); SDK telemetry unless TELEMETRY_DISABLED=true (`ts/packages/core/src/telemetry/Telemetry.ts:179`); CLI install is curl | sh (`README.md:105`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `pip install composio` or `npm install @composio/core` (README), not the curl | sh CLI; set TELEMETRY_DISABLED=true. Claude Code / Hermes: its MCP, only with narrow app scopes. Android: no.
