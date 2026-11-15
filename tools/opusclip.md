# OpusClip

- **Type:** connector
- **Category:** editing, social posting
- **Official URL:** https://www.opus.pro
- **GitHub repo:** unknown
- **Price:** Pro $29/mo monthly (opus.pro, checked 2026-10-31)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

OpusClip (official vendor; not code-reviewed: a review bot recorded 'not vetted yet: closed hosted service, no repo to read', a project a review, 2026-10-30): safe. It holds connected social-account access and can post publicly; its official MCP signs in with OAuth (no API key).; a project: posts to all 3 apps since 2026-10-31; check each clip for overlays first (Claude, a review update, 2026-11-01).

## Safe install

Safe install (fixes applied):
claude.ai (Windows browser): Settings > Connectors > add custom connector https://mcp.opus.pro/mcp (official MCP, OAuth sign-in, no API key). Claude Code (Windows): `claude mcp add --transport http opusclip https://mcp.opus.pro/mcp`. Android: official OpusClip app from Google Play. It holds your connected social accounts and posts publicly: a project needs your OK before each post; a project auto-posts since 2026-10-31, so check each clip for overlays first. unverified: closed hosted service (no repo); contain it by connecting only the social accounts each project uses.

## YOLO install

Not written yet.

## Install notes

[claude.ai](http://claude.ai): Settings > Connectors > add a custom connector with `https://mcp.opus.pro/mcp` (OpusClip's official MCP; OAuth sign-in, no API key).
Claude Code: `claude mcp add --transport http opusclip https://mcp.opus.pro/mcp` (OpusClip's docs, via PyPI `opusclip-mcp`).
Android: official OpusClip app on Google Play (Android 12+, some regions only, per OpusClip's help center).
