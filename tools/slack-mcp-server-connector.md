# Slack MCP server (connector)

- **Type:** connector
- **Category:** messaging
- **Official URL:** https://docs.slack.dev/ai/slack-mcp-server
- **GitHub repo:** unknown
- **Price:** Free to connect; needs a Slack workspace whose admin approves the MCP integration; Slack plan requirement unknown (`docs.slack.dev`, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-10-31

## Safety reason

Slack (official vendor MCP server; not code-reviewed: a review bot listed it under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. Slack's docs: once connected it can search and read the channels, threads and DMs you can see, send and schedule messages and upload files as you; a workspace admin must approve the integration.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

[claude.ai](http://claude.ai): Customize > Connectors > + > Slack, then sign in to your workspace (Slack docs).
Claude Code: `claude plugin install slack` (or `/plugin install slack` in a session), then sign in through OAuth (Slack docs).
