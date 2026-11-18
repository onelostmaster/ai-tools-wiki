# Figma MCP server

- **Type:** MCP
- **Category:** design
- **Official URL:** https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/
- **GitHub repo:** unknown
- **Price:** Included with Figma plans: Starter and View/Collab seats get up to 20 tool calls/month; Full or Dev seats up to 200/day on Professional/Organization, 600/day on Enterprise; image and Make tools spend Figma AI credits (`developers.figma.com`, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-17

## Safety reason

Figma (official vendor MCP server; not code-reviewed: a review bot listed it under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. Figma's docs: it signs in as you (OAuth) and reaches only files you can access; some tools write to your Figma files, and image and Make tools spend Figma AI credits.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): claude plugin install figma@claude-plugins-official, restart Claude Code and sign in from /plugin (or claude mcp add --transport http figma https://mcp.figma.com/mcp, then /mcp > Authenticate) (Figma docs). It reaches only files you can access; some tools write to your files and image and Make tools spend Figma AI credits, so ask Claude to use read-only tools unless you want edits. It does not connect in Claude Code cloud sessions.

## YOLO install

Not written yet.

## Install notes

Claude Code: `claude plugin install figma@claude-plugins-official`, restart Claude Code, then sign in from `/plugin` (Figma docs).
Claude Code: if plugins are blocked: `claude mcp add --transport http figma https://mcp.figma.com/mcp`, then `/mcp` > Authenticate (Figma docs).
Claude Code (cloud): the Figma server bundled in the account's marketing plugin fails to connect in cloud sessions.
