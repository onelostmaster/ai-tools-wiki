# MCP for Unity (CoplayDev)

- **Type:** MCP
- **Category:** 3D and games, developer tools
- **Official URL:** https://github.com/CoplayDev/unity-mcp
- **GitHub repo:** https://github.com/CoplayDev/unity-mcp @ e2fd09c (MIT; latest release v10.3.0, 2026-10-04; old justinpbarnett/unity-mcp redirects here)
- **Price:** Free, MIT (github.com, checked 2026-11-02); asset-generation tools are bring-your-own-key
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @5914ce5 v10.3.0 (2026-11-17): safe with fixes. Telemetry (install UUID, platform) is on by default; DISABLE_TELEMETRY=1 turns it off (Server/src/core/telemetry.py:186-195). execute_code runs any C# in the Editor and sits in the scripting_ext group (services/tools/execute_code.py:31); only core is on by default (tool_registry.py:31). Fix: pin v10.3.0, telemetry off, leave scripting_ext off.

## Safe install

Safe install (fixes applied):
Unity Package Manager git URL https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#v10.3.0; env DISABLE_TELEMETRY=1 for the server; keep the scripting_ext tool group off; Window → MCP for Unity → Configure.

## YOLO install

YOLO (your own risk): skips the pin, telemetry off and the tool-group limit.
Install from #main with every group on.

## Install notes

Ask the user before installing.
Claude Code: add the Unity package and MCP server per its README; set DISABLE_TELEMETRY=1 and leave execute_code off.
Windows: Unity 2021.3+ and Python 3.10+ via uv (not tested). Android: no.
