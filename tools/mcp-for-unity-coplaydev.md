# MCP for Unity (CoplayDev)

- **Type:** MCP
- **Category:** 3D and games, developer tools
- **Official URL:** https://github.com/CoplayDev/unity-mcp
- **GitHub repo:** https://github.com/CoplayDev/unity-mcp @ e2fd09c (MIT; latest release v10.3.0, 2026-10-04; old justinpbarnett/unity-mcp redirects here)
- **Price:** Free, MIT (github.com, checked 2026-11-02); asset-generation tools are bring-your-own-key
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @e2fd09c, a review, 2026-11-02): caution. Telemetry is ON by default (random install UUID, platform, Python version to the vendor endpoint; `Server/src/core/telemetry.py:145-152`, payload `:387-396`); opt out with env DISABLE_TELEMETRY=1 (`:186-191`). An execute_code tool runs arbitrary C# in the Editor (`Server/src/services/tools/execute_code.py:1-8`), off by default (only "core" tools on, `Server/src/services/registry/tool_registry.py:31`). Editor window checks GitHub for updates, notify only (`MCPForUnity/Editor/Services/PackageUpdateService.cs:24-26`). HTTP mode defaults to localhost (`Server/src/main.py:164`). No curl | bash or hooks found.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: add the Unity package and MCP server per its README; set DISABLE_TELEMETRY=1 and leave execute_code off.
Windows: Unity 2021.3+ and Python 3.10+ via uv (not tested). Android: no.
