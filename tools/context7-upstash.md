# Context7 (Upstash)

- **Type:** MCP
- **Category:** developer tools, research
- **Official URL:** https://context7.com
- **GitHub repo:** https://github.com/upstash/context7 @ ceaf5f9 (MIT; pushed 2026-11-02)
- **Price:** Free $0 with 1,000 API calls a month (then 20 bonus calls a day); Pro $10 per seat a month with 2,000 calls per seat, then $5 per 1,000 (context7.com/plans, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light read @ceaf5f9, a review, 2026-11-02): safe. Sends library names and your question to context7.com (hosted endpoint mcp.context7.com, `README.md:59`). Telemetry is metrics on its own HTTP server, off with OTEL_SDK_DISABLED (`packages/mcp/src/lib/telemetry-config.ts:1-3`).

## Safe install

Safe install (fixes applied):
Claude Code (Windows): claude mcp add context7 -e OTEL_SDK_DISABLED=true -- npx -y @upstash/context7-mcp@4.7.0 (version pinned, npm latest on 2026-11-16; OTEL_SDK_DISABLED=true turns its metrics server off, packages/mcp/src/lib/telemetry-config.ts:1-3). Your library names and questions go to context7.com (README.md:59): never put keys or private code in a question. Hermes: same npx command as a plain MCP server with the same env var. claude.ai: no install (use the hosted connector only if you accept the same data rule). Android: no.

## YOLO install

YOLO (your own risk): skips the version pin and the telemetry switch.
claude mcp add context7 -- npx -y @upstash/context7-mcp

## Install notes

Safe, but ask the user before installing.
Claude Code: add the hosted MCP (mcp.context7.com) or run it locally via npx, per its README.
Hermes: works as a plain MCP server.
Windows: npx on Windows. Android: no.
