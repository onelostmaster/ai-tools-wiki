# codebase-memory-mcp (DeusData)

- **Type:** MCP
- **Category:** developer tools
- **Official URL:** https://github.com/DeusData/codebase-memory-mcp
- **GitHub repo:** https://github.com/DeusData/codebase-memory-mcp @ 190abae (MIT, `LICENSE:1`)
- **Price:** Free, MIT (github.com, checked 2026-11-03)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @190abae, 2026-11-03): caution. Its install/config step writes hooks into Claude Code settings.json (`src/cli/cli.c:3434-3525`) and a Codex SessionStart hook (`src/cli/cli.c:4336`); a self-update command pulls releases/latest on demand (`src/cli/cli.c:14359`). No telemetry found; daemon update check removed on purpose (`src/daemon/application.c:72-84`); graph UI binds 127.0.0.1 only (`src/ui/http_server.c:13`); install.sh verifies checksums.txt (`install.sh:197-202`) though it is offered as curl|bash (`install.sh:7`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: download install.ps1, read it, then run it (`README.md:81-94`); check the hooks it adds to Claude Code settings.json afterwards. Claude Code and Hermes via MCP. Android: no.
