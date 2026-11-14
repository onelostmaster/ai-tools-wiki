# n8n-skills (czlonkowski/n8n-skills)

- **Type:** skill
- **Category:** automation
- **Official URL:** https://github.com/czlonkowski/n8n-skills
- **GitHub repo:** https://github.com/czlonkowski/n8n-skills @ e037563 (MIT)
- **Price:** Skills free (MIT); hosted n8n-mcp Free (100 tool calls a day) or Supporter €19/month; self-hosted n8n-mcp free (n8n-mcp.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @e037563, a review, 2026-11-02): caution. Adds SessionStart and PreToolUse hooks (`hooks/hooks.json`; `session-start.sh:19-40` is local, no network). `mcp.json:3-7` points at the hosted api.n8n-mcp.com, which sees your workflow data; self-host n8n-mcp instead if that matters.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: install as a plugin per its README; review the hooks first.
Windows: works in Claude Code on Windows. Android: no.
