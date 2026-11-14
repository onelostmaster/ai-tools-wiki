# OpusClip

- **Type:** connector
- **Category:** editing, social posting
- **Official URL:** https://www.opus.pro
- **GitHub repo:** unknown
- **Price:** Pro $29/mo monthly (opus.pro, checked 2026-10-31)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-01

## Safety reason

OpusClip (official vendor; not code-reviewed: a review bot recorded 'not vetted yet: closed hosted service, no repo to read', a project a review, 2026-10-30): safe. It holds connected social-account access and can post publicly; its official MCP signs in with OAuth (no API key).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

[claude.ai](http://claude.ai): Settings > Connectors > add a custom connector with `https://mcp.opus.pro/mcp` (OpusClip's official MCP; OAuth sign-in, no API key).
Claude Code: `claude mcp add --transport http opusclip https://mcp.opus.pro/mcp` (OpusClip's docs, via PyPI `opusclip-mcp`).
Android: official OpusClip app on Google Play (Android 12+, some regions only, per OpusClip's help center).
