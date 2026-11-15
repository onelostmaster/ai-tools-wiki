# Zapier (connector)

- **Type:** connector
- **Category:** automation
- **Official URL:** https://zapier.com/mcp
- **GitHub repo:** unknown
- **Price:** Included in every Zapier plan; each successful tool call uses 2 tasks. Free: 100 tasks/month; Professional from $19.99/month; Team from $69/month (`zapier.com`, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Zapier docs (checked 2026-11-14): safe with fixes, Skip (no need). It acts in your connected apps. Fix: switch the server to managed mode, which removes skills and code actions (docs.zapier.com/mcp/manage/switch-modes), so the write_code_action meta-tool is gone; enable only the actions you need (each is its own tool); every action is logged.

## Safe install

Safe install (fixes applied):
Zapier MCP in managed mode; enable only the needed actions; connect only the apps those actions use.

## YOLO install

YOLO (your own risk): skips managed mode, so it can write and run code.
Agentic mode with all actions.

## Install notes

Ask the user before installing. Zapier MCP in managed mode; enable only the needed actions; connect only the apps those actions use.
