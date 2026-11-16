# Graphiti MCP (Zep)

- **Type:** MCP
- **Category:** Notion and productivity
- **Official URL:** https://help.getzep.com/graphiti/getting-started/mcp-server
- **GitHub repo:** [https://github.com/getzep/graphiti](https://github.com/getzep/graphiti)
- **Price:** Free (Apache-2.0, self-hosted: Docker + FalkorDB or Neo4j); you pay for your own LLM usage (OpenAI by default). Zep Cloud is the separate paid hosted version (`getzep.com`, checked 2026-10-31).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @3a8a78c (2026-11-15): safe with fixes. PostHog telemetry is on unless GRAPHITI_TELEMETRY_ENABLED=false (graphiti_core/telemetry/telemetry.py:22, 36-37). Compose ports bind 127.0.0.1 only (mcp_server/docker/docker-compose.yml:29-31). The default compose uses the :latest image (line 3): pin it. Each memory episode goes to your chosen LLM provider for extraction.

## Safe install

Safe install (fixes applied):
In mcp_server/docker: set GRAPHITI_TELEMETRY_ENABLED=false in .env; replace zepai/knowledge-graph-mcp:latest with the image digest from docker images --digests after one pull; docker compose up; LLM key in .env, never in chat; add http://127.0.0.1:8000 as the MCP URL.

## YOLO install

YOLO (your own risk): skips telemetry off and the image pin.
docker compose up with the defaults.

## Install notes

Ask the user before installing. In mcp_server/docker: set GRAPHITI_TELEMETRY_ENABLED=false in .env; replace zepai/knowledge-graph-mcp:latest with the image digest from docker images --digests after one pull; docker compose up; LLM key in .env, never in chat; add http://127.0.0.1:8000 as the MCP URL.
