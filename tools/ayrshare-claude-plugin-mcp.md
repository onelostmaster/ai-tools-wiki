# Ayrshare Claude plugin + MCP

- **Type:** plugin
- **Category:** social posting
- **Official URL:** https://www.ayrshare.com
- **GitHub repo:** [https://github.com/ayrshare/ayrshare-social-media-api-claude-plugin](https://github.com/ayrshare/ayrshare-social-media-api-claude-plugin)
- **Price:** Premium $149/mo; Launch $299/mo with 28-day trial (ayrshare.com, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a review, 48cc040): Looks safe. Skills and Markdown only, plus a PreToolUse hook that forces an ask before any publish, comment, DM or ad action; the MCP is the hosted `https://api.ayrshare.com/mcp` with the key from env. `/ayrshare:setup` writes the API key to `~/.claude/settings.json` in plaintext.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `claude plugin marketplace add ayrshare/ayrshare-social-media-api-claude-plugin` then `claude plugin install ayrshare@ayrshare`
Keys: `/ayrshare:setup` stores the API key in plaintext in `~/.claude/settings.json`; prefer a secret/env var and never paste the key into chat
