# Composio

- **Type:** API
- **Category:** automation, developer tools
- **Official URL:** https://composio.dev
- **GitHub repo:** https://github.com/ComposioHQ/composio @ a0c51b0 (MIT SDKs; cloud closed)
- **Price:** Hobby free (100K tool calls a month), Pro $29/mo + usage (composio.dev, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (light code read @a0c51b0, a review / Hermes a review, 2026-11-02): caution. Holds your app OAuth tokens in its cloud (third-party storage, broad scopes); SDK telemetry unless TELEMETRY_DISABLED=true (ts/packages/core/src/telemetry/Telemetry.ts:179); CLI install is curl | sh (README.md:105). No fix: your app OAuth tokens are held in Composio's closed cloud and no setting keeps them local; telemetry and the curl | sh installer are fixed in Safe install, and narrow app scopes limit the exposure. Caution stands for the token storage only.

## Safe install

Safe install (fixes applied):
Windows: pip install composio==<release matching a0c51b0> or npm install @composio/core@<same release> (README); never the curl | sh CLI installer (README.md:105). Set the user env var TELEMETRY_DISABLED=true before first use; otherwise the SDK sends telemetry (ts/packages/core/src/telemetry/Telemetry.ts:179). Connect only the apps you need with the narrowest scopes it offers: your app OAuth tokens are held in Composio's cloud (closed), which no setting avoids. Claude Code / Hermes: its MCP with the same narrow app list. Android: no.
No fix: OAuth tokens stored in Composio's cloud.

## YOLO install

YOLO (your own risk): skips the version pin, the telemetry switch and the narrow-scopes rule.
Windows: curl | sh CLI install from the README, connect apps with default scopes; telemetry stays on.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `pip install composio` or `npm install @composio/core` (README), not the curl | sh CLI; set TELEMETRY_DISABLED=true. Claude Code / Hermes: its MCP, only with narrow app scopes. Android: no.
