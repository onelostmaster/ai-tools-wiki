# MCP reference servers (filesystem, fetch, git, memory, sequential thinking, time, everything)

- **Type:** MCP
- **Category:** developer tools
- **Official URL:** https://github.com/modelcontextprotocol/servers
- **GitHub repo:** https://github.com/modelcontextprotocol/servers @ 194cc86 (MIT/Apache-2.0 per server)
- **Price:** Free (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @194cc86, a review / Hermes a review, 2026-11-02): safe. The repo calls them educational reference code, "not production-ready" (`README.md:9`). Filesystem only reaches folders you list; fetch reads any URL the agent picks.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Claude Code: e.g. `npx -y @modelcontextprotocol/server-memory` or `pip install mcp-server-git` (README). Hermes: same commands with `hermes mcp add`. Android: no.
