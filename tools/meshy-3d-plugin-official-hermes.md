# Meshy 3D plugin (official Hermes)

- **Type:** plugin
- **Category:** Hermes add-ons, 3D and games
- **Official URL:** https://github.com/NousResearch/hermes-official-plugins/tree/main/meshy
- **GitHub repo:** [https://github.com/NousResearch/hermes-official-plugins](https://github.com/NousResearch/hermes-official-plugins)
- **Price:** Free plugin; Meshy credits: Free 100 credits/mo; Pro $20/mo; Premium $40/mo; Ultra $100/mo; Studio $70/mo (`meshy.ai`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a project a review, 2026-10-28): Looks safe. Network only to `api.meshy.ai` plus a bundled MCP run with `npx @meshy-ai/meshy-mcp-server@0.6.5` (`meshy/mcp.json`: pinned, but third-party code that was not reviewed). Credit-costing tools ask you to confirm first.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Hermes: `hermes plugins install meshy` (README:186, per a review bot). Keep any Meshy API key in secrets/env vars; never paste it into chat.
