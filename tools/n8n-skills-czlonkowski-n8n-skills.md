# n8n-skills (czlonkowski/n8n-skills)

- **Type:** skill
- **Category:** automation
- **Official URL:** https://github.com/czlonkowski/n8n-skills
- **GitHub repo:** https://github.com/czlonkowski/n8n-skills @ e037563 (MIT)
- **Price:** Skills free (MIT); hosted n8n-mcp Free (100 tool calls a day) or Supporter €19/month; self-hosted n8n-mcp free (n8n-mcp.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @e037563 v1.37.1 (2026-11-17): safe with fixes. Hooks fire on SessionStart and some n8n tool calls (hooks/hooks.json) and run local shell only (hooks/*.sh). mcp.json:3-7 adds the hosted api.n8n-mcp.com, which sees your workflows. Fix: pin the commit, turn that server off, self-host n8n-mcp.

## Safe install

Safe install (fixes applied):
/plugin marketplace add czlonkowski/n8n-skills#e037563, /plugin install; /mcp → disable the hosted n8n-mcp; run n8n-mcp yourself per its README pinned at v2.102.0, API key in env.

## YOLO install

YOLO (your own risk): skips the pin and self-hosting.
Install from main and use the hosted n8n-mcp.

## Install notes

Ask the user before installing.
Claude Code: install as a plugin per its README; review the hooks first.
Windows: works in Claude Code on Windows. Android: no.
