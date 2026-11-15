# roadmap-skill (shiquda)

- **Type:** MCP
- **Category:** Notion and productivity, developer tools
- **Official URL:** https://github.com/shiquda/roadmap-skill
- **GitHub repo:** https://github.com/shiquda/roadmap-skill @ 3bd7b07 (MIT; committed 2026-03-18; MCP server + 4 agent skills)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @3bd7b07, a review, 2026-11-02): safe.; data is local JSON in ~/.roadmap-skill (`src/utils/path-helpers.ts:10`, `src/storage/index.ts:22`); no telemetry, hooks or install scripts found. The npm build was not compared with the repo.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: Claude Desktop or Claude Code MCP entry `npx -y roadmap-skill` (`README.md:87`), needs Node. claude.ai and Android: no (local MCP). Hermes: plain MCP server, untested.
