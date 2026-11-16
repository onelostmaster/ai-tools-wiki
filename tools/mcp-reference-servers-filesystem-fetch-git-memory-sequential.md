# MCP reference servers (filesystem, fetch, git, memory, sequential thinking, time, everything)

- **Type:** MCP
- **Category:** developer tools
- **Official URL:** https://github.com/modelcontextprotocol/servers
- **GitHub repo:** https://github.com/modelcontextprotocol/servers @ 194cc86 (MIT/Apache-2.0 per server)
- **Price:** Free (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @194cc86, a review / Hermes a review, 2026-11-02): safe. The repo calls them educational reference code, "not production-ready" (`README.md:9`). Filesystem only reaches folders you list; fetch reads any URL the agent picks.

## Safe install

Safe install (fixes applied):
Use the versions from the reviewed 194cc86, which is exactly release v2.2.0 (GitHub compare: identical). Windows Claude Code (Node 24+ for npx servers, src/filesystem/README.md:271; uv for Python ones): filesystem `claude mcp add fs -- cmd /c npx -y @modelcontextprotocol/server-filesystem@2.1.0 "<one project folder>"` (it only reaches folders you list; never list C:\\ or your whole user folder); memory `npx -y @modelcontextprotocol/server-memory@2.0.1` with MEMORY_FILE_PATH set to a file you choose (default is memory.jsonl inside the npx cache folder, src/memory/README.md:243); sequential thinking `@modelcontextprotocol/server-sequential-thinking@2.0.0`; everything `@modelcontextprotocol/server-everything@2.1.0` (test server only); fetch `uvx mcp-server-fetch==2026.10.28` without --ignore-robots-txt or --allow-private-ips (it obeys robots.txt and refuses private and metadata addresses by default, src/fetch/README.md:14,169-176); git `uvx mcp-server-git==2026.10.28 --repository <one repo>` (without --repository it reads and writes any repo it can reach, src/git/README.md:138); time `uvx mcp-server-time==2026.10.28`. Hermes: same commands with hermes mcp add. The repo calls them reference code, not production-ready (README.md:9). claude.ai and Android: no (local MCP).

## YOLO install

YOLO (your own risk): skips the version pins (gets v2.4.0 from 2026-11-11, unreviewed), the folder and --repository limits.
claude mcp add memory -- cmd /c npx -y @modelcontextprotocol/server-memory (and the same unpinned for the others)

## Install notes

Safe, but ask the user before installing.
Claude Code: e.g. `npx -y @modelcontextprotocol/server-memory` or `pip install mcp-server-git` (README). Hermes: same commands with `hermes mcp add`. Android: no.
