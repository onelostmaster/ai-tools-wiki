# mcp-for-blender

- **Type:** MCP
- **Category:** 3D and games
- **Official URL:** https://github.com/ahujasid/mcp-for-blender
- **GitHub repo:** https://github.com/ahujasid/mcp-for-blender @ 992233b (MIT)
- **Price:** Free (MIT per PyPI `mcp-for-blender`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (code read @992233b) and Claude (@992233b), 2026-11-01: caution. execute_blender_code runs any Python unsandboxed by default (safe mode opt-in, BLENDER_MCP_SAFE_MODE=1); add-on updater pulls `addon.py` from GitHub main; installers pipe curl/irm to a shell; points at a hosted premium endpoint. Telemetry with prompts/screenshots only with consent; PyPI README (2026-10-31): anonymous usage record by default, DISABLE_TELEMETRY=true turns it off.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code (local only): no install steps given (the source withholds them until the tool is rated safe); needs the Blender desktop app. Set BLENDER_MCP_SAFE_MODE=1 and DISABLE_TELEMETRY=true if used.
