# Composio

- **Type:** API
- **Category:** automation, developer tools
- **Official URL:** https://composio.dev
- **GitHub repo:** https://github.com/ComposioHQ/composio @ a0c51b0 (MIT SDKs; cloud closed)
- **Price:** Hobby free (100K tool calls a month), Pro $29/mo + usage (composio.dev, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @a0c51b0 (2026-11-19): caution. Telemetry stops with TELEMETRY_DISABLED=true (ts/packages/core/src/telemetry/Telemetry.ts:179) and the curl|sh CLI (README.md:105) is replaced by pinned pip/npm; both fixed in Safe install. No fix: Composio's closed cloud holds your connected apps' OAuth tokens, and no setting keeps them local; narrow scopes limit what a leak exposes.

## Safe install

Safe install (fixes applied):
Windows: pip install composio==0.30.0 or npm install --save-exact @composio/core@0.27.0 (the versions in the reviewed a0c51b0: python/pyproject.toml:3, ts/packages/core/package.json); never the curl | sh CLI installer (README.md:105). Set the user env var TELEMETRY_DISABLED=true before first use; otherwise the SDK sends telemetry (ts/packages/core/src/telemetry/Telemetry.ts:179). Connect only the apps you need with the narrowest scopes it offers: your app OAuth tokens are held in Composio's cloud (closed), which no setting avoids. Claude Code / Hermes: its MCP with the same narrow app list. Android: no.

## YOLO install

YOLO (your own risk): skips the version pin, the telemetry switch and the narrow-scopes rule.
Windows: curl | sh CLI install from the README, connect apps with default scopes; telemetry stays on.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `pip install composio` or `npm install @composio/core` (README), not the curl | sh CLI; set TELEMETRY_DISABLED=true. Claude Code / Hermes: its MCP, only with narrow app scopes. Android: no.
