# shadcn/ui (+ shadcn MCP server)

- **Type:** library
- **Category:** design, building a site, developer tools
- **Official URL:** https://ui.shadcn.com
- **GitHub repo:** https://github.com/shadcn-ui/ui @ 4aaea19 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @4aaea19, a review / Hermes a review, 2026-11-02): safe. MCP server in `packages/shadcn/src/mcp/index.ts`; registry components are copied into your project as source. awesome-llm-apps starts it unpinned with npx shadcn@latest mcp: pin a version.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: `npx shadcn init`, then `npx shadcn add [component]` (package README). Claude Code: add the shadcn MCP server (pin the version). Hermes: same MCP over `hermes mcp add`. Android: no.
