# Graphiti MCP (Zep)

- **Type:** MCP
- **Category:** Notion and productivity
- **Official URL:** https://help.getzep.com/graphiti/getting-started/mcp-server
- **GitHub repo:** [https://github.com/getzep/graphiti](https://github.com/getzep/graphiti)
- **Price:** Free (Apache-2.0, self-hosted: Docker + FalkorDB or Neo4j); you pay for your own LLM usage (OpenAI by default). Zep Cloud is the separate paid hosted version (`getzep.com`, checked 2026-10-31).
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a review / Hermes a review, 72b5c59, 2026-10-31): Use with caution. PostHog telemetry on by default (opt out `GRAPHITI_TELEMETRY_ENABLED=false`); every memory episode is sent to your LLM provider (OpenAI by default, needs your key) for extraction. No hooks: the agent calls it as an MCP.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: a review bot gave no formal steps (not Looks safe); route if you want it: `docker compose up` in `mcp_server/` with `GRAPHITI_TELEMETRY_ENABLED=false`, then add the MCP URL. It needs an LLM key (OpenAI by default): add it as a secret/env var, never paste it into chat.
Hermes: same server; add its MCP URL in Hermes.
