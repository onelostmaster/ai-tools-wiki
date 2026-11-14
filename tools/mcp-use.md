# mcp-use

- **Type:** library
- **Category:** developer tools
- **Official URL:** https://github.com/mcp-use/mcp-use
- **GitHub repo:** https://github.com/mcp-use/mcp-use @ 338b9a7 (MIT)
- **Price:** Library free (MIT); Manufact Cloud hosting free tier, then pay as you go, Pro $300/mo (manufact.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @338b9a7, a review / Hermes a review, 2026-11-02): caution. PostHog + Scarf telemetry on unless MCP_USE_ANONYMIZED_TELEMETRY=false (`libraries/python/mcp_use/telemetry/telemetry.py:12-13,139`; `pyproject.toml:30-31`). Starter uses unpinned npx create-mcp-use-app@latest.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: per its README (not tested); set MCP_USE_ANONYMIZED_TELEMETRY=false. Android: no.
