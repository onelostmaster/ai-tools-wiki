# Context7 (Upstash)

- **Type:** MCP
- **Category:** developer tools, research
- **Official URL:** https://context7.com
- **GitHub repo:** https://github.com/upstash/context7 @ ceaf5f9 (MIT; pushed 2026-11-02)
- **Price:** Free $0 with 1,000 API calls a month (then 20 bonus calls a day); Pro $10 per seat a month with 2,000 calls per seat, then $5 per 1,000 (context7.com/plans, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light read @ceaf5f9, a review, 2026-11-02): safe. Sends library names and your question to context7.com (hosted endpoint mcp.context7.com, `README.md:59`). Telemetry is metrics on its own HTTP server, off with OTEL_SDK_DISABLED (`packages/mcp/src/lib/telemetry-config.ts:1-3`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Claude Code: add the hosted MCP (mcp.context7.com) or run it locally via npx, per its README.
Hermes: works as a plain MCP server.
Windows: npx on Windows. Android: no.
