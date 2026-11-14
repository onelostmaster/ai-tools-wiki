# Zernio MCP + Claude plugin

- **Type:** plugin
- **Category:** social posting
- **Official URL:** https://zernio.com
- **GitHub repo:** [https://github.com/zernio-dev/zernio-claude-plugin](https://github.com/zernio-dev/zernio-claude-plugin)
- **Price:** First 2 accounts free; then $6/account/mo (3-10), $3 (11-100) (zernio.com, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, 5dfcbb5, a project a review, 2026-10-30): Looks safe (thin client). The plugin is only an `.mcp.json` pointing at `mcp.zernio.com/mcp` with OAuth plus one prompt command; no code. The hosted server holds your social tokens. It includes paid ads tools: untick those.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `/plugin marketplace add zernio-dev/zernio-claude-plugin` then `/plugin install zernio@zernio`; untick the paid ads tools
Hermes: unconfirmed: `mcp_servers:` entry with url `https://mcp.zernio.com/mcp` (OAuth), then `/reload-mcp`
