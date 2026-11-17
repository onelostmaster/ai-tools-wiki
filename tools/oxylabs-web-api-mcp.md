# Oxylabs Web API MCP

- **Type:** MCP
- **Category:** scraping, research
- **Official URL:** https://github.com/oxylabs/web-api-mcp
- **GitHub repo:** https://github.com/oxylabs/web-api-mcp @ b408c3e (MIT)
- **Price:** MCP free (MIT); needs a paid Oxylabs Web API plan (price not checked, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @b408c3e, a review, 2026-11-02): safe (light read). Needs a paid Oxylabs Web API key (OXYLABS_WEB_API_KEY, `server.py:10`); only adds a client-name header to its own API calls (`server.py:235-262`).

## Safe install

Safe install (fixes applied):
Claude Code (Windows): `uv tool install git+https://github.com/oxylabs/web-api-mcp@b408c3e` (README.md:88 without the pin; pinned to the reviewed commit), set OXYLABS_WEB_API_KEY as a Windows user environment variable, then `claude mcp add oxylabs-web-api --env OXYLABS_WEB_API_KEY=${OXYLABS_WEB_API_KEY} -- oxylabs-web-api-mcp` (README.md:103-110). Keep the key out of client configs and shared pages (README.md:103). Run it over stdio only. Verified: the HTTP example binds --host 0.0.0.0 (README.md:150), which opens your key-backed server to your network. Fix: if you need HTTP, use --host 127.0.0.1. Every search and scrape goes to Oxylabs and is billed to your plan. claude.ai: hosted server https://mcp.oxylabs.io/web-api-mcp with your key as a Bearer header (README.md:36-53). Hermes: same stdio command. Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin.
claude mcp add --transport http --scope user oxylabs-web-api https://mcp.oxylabs.io/web-api-mcp --header "Authorization: Bearer $\{OXYLABS_WEB_API_KEY\}"

## Install notes

Safe, but ask the user before installing.
Claude Code: add as an MCP server with your own Oxylabs key (never on shared pages).
Windows: Python/uv (not tested). Android: no.
