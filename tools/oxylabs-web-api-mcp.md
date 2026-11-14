# Oxylabs Web API MCP

- **Type:** MCP
- **Category:** scraping, research
- **Official URL:** https://github.com/oxylabs/web-api-mcp
- **GitHub repo:** https://github.com/oxylabs/web-api-mcp @ b408c3e (MIT)
- **Price:** MCP free (MIT); needs a paid Oxylabs Web API plan (price not checked, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @b408c3e, a review, 2026-11-02): safe (light read). Needs a paid Oxylabs Web API key (OXYLABS_WEB_API_KEY, `server.py:10`); only adds a client-name header to its own API calls (`server.py:235-262`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Claude Code: add as an MCP server with your own Oxylabs key (never on shared pages).
Windows: Python/uv (not tested). Android: no.
