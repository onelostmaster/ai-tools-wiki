# Upload-Post MCP

- **Type:** MCP
- **Category:** social posting
- **Official URL:** https://www.upload-post.com
- **GitHub repo:** [https://github.com/Upload-Post/upload-post-mcp](https://github.com/Upload-Post/upload-post-mcp)
- **Price:** Free: 10 uploads/mo, 2 profiles, no TikTok; Basic $24/mo ($16/mo yearly) (upload-post.com, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, 8d27ca1, a project a review, 2026-10-30): Looks safe. Server-side confirm gate before any publish or DM; talks only to `upload-post.com` hosts; no telemetry, eval or shell. Caveat: local npx mode can upload any local file path as media; the hosted mode refuses paths.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

[claude.ai](http://claude.ai): no confirmed command yet; the source records the hosted MCP URL `https://mcp.upload-post.com/mcp`; follow the official docs at [https://www.upload-post.com](https://www.upload-post.com)
Claude Code: `claude mcp add --transport http upload-post https://mcp.upload-post.com/mcp`, then OAuth
Hermes: unconfirmed: `mcp_servers:` entry with url `https://mcp.upload-post.com/mcp` in `~/.hermes/config.yaml`, then `/reload-mcp`
