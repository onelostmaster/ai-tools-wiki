# Ayrshare Claude plugin + MCP

- **Type:** plugin
- **Category:** social posting
- **Official URL:** https://www.ayrshare.com
- **GitHub repo:** [https://github.com/ayrshare/ayrshare-social-media-api-claude-plugin](https://github.com/ayrshare/ayrshare-social-media-api-claude-plugin)
- **Price:** Premium $149/mo; Launch $299/mo with 28-day trial (ayrshare.com, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, a review, 48cc040): Looks safe. Skills and Markdown only, plus a PreToolUse hook that forces an ask before any publish, comment, DM or ad action; the MCP is the hosted `https://api.ayrshare.com/mcp` with the key from env. `/ayrshare:setup` writes the API key to `~/.claude/settings.json` in plaintext.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): claude plugin marketplace add ayrshare/ayrshare-social-media-api-claude-plugin, then claude plugin install ayrshare@ayrshare. Do not run /ayrshare\:setup\: it writes the API key in plaintext to ~/.claude/settings.json . Set the key as a Windows user env var instead (unverified: the exact variable name; read it from the plugin's MCP config first). Keep its PreToolUse hook on: it asks before every publish, comment, DM or ad action. Never paste the key into chat.

## YOLO install

YOLO (your own risk): skips the env-var key.
Run /ayrshare:setup (key stored in plaintext in settings.json).

## Install notes

Claude Code: `claude plugin marketplace add ayrshare/ayrshare-social-media-api-claude-plugin` then `claude plugin install ayrshare@ayrshare`
Keys: `/ayrshare:setup` stores the API key in plaintext in `~/.claude/settings.json`; prefer a secret/env var and never paste the key into chat
