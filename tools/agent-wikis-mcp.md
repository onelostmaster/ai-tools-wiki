# Agent Wikis MCP

- **Type:** MCP
- **Category:** research
- **Official URL:** https://agentwikis.com/
- **GitHub repo:** [https://github.com/tonbistudio/agentwikis-mcp](https://github.com/tonbistudio/agentwikis-mcp)
- **Price:** Free tier; Pro $19.99/mo (agentwikis.com, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a review, 8d9397a / npm 0.2.3): Looks safe. One dependency, no postinstall, shell, eval, fs or telemetry; it only GETs `agentwikis.com/api` and sends the optional `AGENTWIKIS_API_KEY` as a Bearer token. Caveats: `npx -y` is unpinned (pulls latest); hosted wiki text can change unaudited; search queries go to their server; the Pro Hermes skills bundle is not audited.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `claude mcp add agentwikis -- npx -y agentwikis-mcp` (unpinned npx), or no install: point the agent at `https://agentwikis.com/llms.txt`
Hermes: unconfirmed: a `mcp_servers:` entry with `command: npx` and `args: ["-y","agentwikis-mcp"]`, then `/reload-mcp`
Keys: put the optional Pro key in the `AGENTWIKIS_API_KEY` env var; never paste it into chat
