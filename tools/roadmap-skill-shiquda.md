# roadmap-skill (shiquda)

- **Type:** MCP
- **Category:** Notion and productivity, developer tools
- **Official URL:** https://github.com/shiquda/roadmap-skill
- **GitHub repo:** https://github.com/shiquda/roadmap-skill @ 3bd7b07 (MIT; committed 2026-03-18; MCP server + 4 agent skills)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (code read @3bd7b07, a review, 2026-11-02): safe.; data is local JSON in ~/.roadmap-skill (`src/utils/path-helpers.ts:10`, `src/storage/index.ts:22`); no telemetry, hooks or install scripts found. The npm build was not compared with the repo.

## Safe install

Safe install (fixes applied):
Windows Claude Code (needs Node.js): `claude mcp add roadmap -- cmd /c npx -y roadmap-skill@0.3.0` (README.md:87 gives `npx -y roadmap-skill` unpinned; 0.3.0 is the latest on npm, 2026-03-14, and matches package.json at the reviewed 3bd7b07). The npm package has no install scripts (package.json scripts). Unverified: that the npm build matches the repo; contained by the version pin. Claude Desktop: same command in the mcpServers entry. Hermes: plain stdio MCP server, not tested. claude.ai and Android: no (local MCP).

## YOLO install

YOLO (your own risk): skips the version pin.
claude mcp add roadmap "npx -y roadmap-skill"

## Install notes

Safe, but ask the user before installing.
Windows: Claude Desktop or Claude Code MCP entry `npx -y roadmap-skill` (`README.md:87`), needs Node. claude.ai and Android: no (local MCP). Hermes: plain MCP server, untested.
