# shadcn/ui (+ shadcn MCP server)

- **Type:** library
- **Category:** design, building a site, developer tools
- **Official URL:** https://ui.shadcn.com
- **GitHub repo:** https://github.com/shadcn-ui/ui @ 4aaea19 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @4aaea19, a review / Hermes a review, 2026-11-02): safe. MCP server in `packages/shadcn/src/mcp/index.ts`; registry components are copied into your project as source. awesome-llm-apps starts it unpinned with npx shadcn@latest mcp: pin a version.

## Safe install

Safe install (fixes applied):
Windows (Node.js), in your project folder: `npx shadcn@4.23.0 init`, then `npx shadcn@4.23.0 add <component>`. 4.23.0 (2026-10-27) is the newest CLI; the 15 commits from it to the reviewed 4aaea19 change no packages/shadcn files (GitHub compare), so it is the reviewed CLI and MCP code; the npm package has no install script. Components are copied into your project as source: look at the git diff before you commit. Add only the official registry or registries you trust; a third-party registry's files land in your project the same way. Claude Code: `claude mcp add shadcn -- cmd /c npx -y shadcn@4.23.0 mcp` (pinned, not shadcn@latest; MCP server in packages/shadcn/src/mcp/index.ts). Hermes: same command with hermes mcp add. claude.ai and Android: no.

## YOLO install

YOLO (your own risk): skips the version pin.
npx shadcn@latest init, and npx shadcn@latest mcp for Claude Code

## Install notes

Safe, but ask the user before installing.
Windows: `npx shadcn init`, then `npx shadcn add [component]` (package README). Claude Code: add the shadcn MCP server (pin the version). Hermes: same MCP over `hermes mcp add`. Android: no.
