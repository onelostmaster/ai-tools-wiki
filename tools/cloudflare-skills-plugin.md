# Cloudflare skills plugin

- **Type:** plugin
- **Category:** building a site
- **Official URL:** https://developers.cloudflare.com/agent-setup/claude-code/
- **GitHub repo:** [https://github.com/cloudflare/skills](https://github.com/cloudflare/skills) (not in the source; confirmed on Cloudflare's docs, 2026-10-31)
- **Price:** Free (Apache-2.0); Cloudflare plans separate
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-17

## Safety reason

Cloudflare docs (official vendor plugin, checked 2026-10-31; not code-reviewed): safe. It installs Cloudflare Skills and registers Cloudflare MCP servers that ask for OAuth access to your Cloudflare account; the API server reaches DNS, WAF, R2 and Zero Trust, so grant only the permissions needed.

## Safe install

Safe install (fixes applied):
Claude Code: /plugin marketplace add cloudflare/skills, then /plugin install cloudflare@cloudflare (Cloudflare docs). On the first Cloudflare tool call, approve only the OAuth scopes the task needs (the API server reaches DNS, WAF, R2 and Zero Trust); never paste API tokens into chat. Official vendor plugin.

## YOLO install

Not written yet.

## Install notes

Claude Code: `/plugin marketplace add cloudflare/skills`, then `/plugin install cloudflare@cloudflare` (from Cloudflare's docs). The first Cloudflare tool call asks for OAuth sign-in; never paste API tokens into chat.
