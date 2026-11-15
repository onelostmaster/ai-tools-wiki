# Upload-Post MCP

- **Type:** MCP
- **Category:** social posting
- **Official URL:** https://www.upload-post.com
- **GitHub repo:** [https://github.com/Upload-Post/upload-post-mcp](https://github.com/Upload-Post/upload-post-mcp)
- **Price:** Free: 10 uploads/mo, 2 profiles, no TikTok; Basic $24/mo ($16/mo yearly) (upload-post.com, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read, 8d27ca1, a project a review, 2026-10-30): Looks safe. Server-side confirm gate before any publish or DM; talks only to `upload-post.com` hosts; no telemetry, eval or shell. Caveat: local npx mode can upload any local file path as media; the hosted mode refuses paths.

## Safe install

Safe install (fixes applied):
Use the hosted server, not local npx: it refuses local file paths (src/tools/upload.ts:520, checked at HEAD 1844d6c on 2026-11-14), which removes the "upload any local file" risk of local mode. claude.ai: Customize > Connectors > + Add > Add custom connector, paste https://mcp.upload-post.com/mcp, sign in with OAuth (README.md:23). Claude Code (Windows): `claude mcp add --transport http upload-post https://mcp.upload-post.com/mcp` (README.md:23), then OAuth; never paste the API key into chat. Android: use it through claude.ai. Hermes: unconfirmed route, a mcp_servers: entry with url https://mcp.upload-post.com/mcp, then /reload-mcp. Connect only the social accounts you want it to post to.

## YOLO install

YOLO (your own risk): skips the hosted-only rule (local npx mode can upload any absolute local file path, src/tools/upload.ts:625).
Install the official Upload-Post plugin from the Claude directory (README.md:23).

## Install notes

[claude.ai](http://claude.ai): no confirmed command yet; the source records the hosted MCP URL `https://mcp.upload-post.com/mcp`; follow the official docs at [https://www.upload-post.com](https://www.upload-post.com)
Claude Code: `claude mcp add --transport http upload-post https://mcp.upload-post.com/mcp`, then OAuth
Hermes: unconfirmed: `mcp_servers:` entry with url `https://mcp.upload-post.com/mcp` in `~/.hermes/config.yaml`, then `/reload-mcp`
