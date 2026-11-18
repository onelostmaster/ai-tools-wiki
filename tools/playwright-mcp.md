# Playwright MCP

- **Type:** MCP
- **Category:** developer tools
- **Official URL:** https://www.npmjs.com/package/@playwright/mcp
- **GitHub repo:** [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) (confirmed via the npm package @playwright/mcp, 2026-10-31)
- **Price:** Free (Apache-2.0, per npm)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-17

## Safety reason

Microsoft (official npm package `@playwright/mcp`, published by Microsoft's maintainers, Apache-2.0, checked 2026-10-31; not code-reviewed): safe. No project reviewed its code; a project rejected it only as redundant with what it already had installed.

## Safe install

Safe install (fixes applied):
Claude Code: claude mcp add playwright -- npx @playwright/mcp@<exact version npm shows today> (pinned instead of @latest; official package @playwright/mcp by Microsoft). It drives a real browser, so do not sign it in to accounts you do not want the agent to use.

## YOLO install

YOLO (your own risk): skips the version pin.
claude mcp add playwright npx @playwright/mcp@latest (package README on npm).

## Install notes

Claude Code: `claude mcp add playwright npx @playwright/mcp@latest` (from the package README on npm; `@latest` is unpinned)
