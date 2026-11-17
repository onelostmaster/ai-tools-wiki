# mcp-for-blender

- **Type:** MCP
- **Category:** 3D and games
- **Official URL:** https://github.com/ahujasid/mcp-for-blender
- **GitHub repo:** https://github.com/ahujasid/mcp-for-blender @ 992233b (MIT)
- **Price:** Free (MIT per PyPI `mcp-for-blender`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @b6a2ce3 (2026-11-16): safe with fixes. execute_blender_code runs any Python unless BLENDER_MCP_SAFE_MODE=1 turns on an AST allowlist (src/blender_mcp/safe_mode.py:5, 72); it guards the MCP path, so close other local apps that talk to Blender's socket. DISABLE_TELEMETRY=true stops usage events (telemetry.py:117). The add-on updater pulls addon.py from main (bundled/addon.py:7328): skip it.

## Safe install

Safe install (fixes applied):
Env BLENDER_MCP_SAFE_MODE=1 and DISABLE_TELEMETRY=true; MCP via uvx mcp-for-blender==2.3.0; install the bundled addon.py at b6a2ce3 into Blender by hand; never click the add-on update; skip curl|sh and irm|iex installers.

## YOLO install

YOLO (your own risk): skips safe mode, telemetry off and the pin.
Run the README installer and let the add-on update.

## Install notes

Ask the user before installing.
Claude Code (local only): no install steps given (the source withholds them until the tool is rated safe); needs the Blender desktop app. Set BLENDER_MCP_SAFE_MODE=1 and DISABLE_TELEMETRY=true if used.
