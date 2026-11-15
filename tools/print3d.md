# print3d

- **Type:** MCP
- **Category:** 3D and games
- **Official URL:** https://github.com/mfranzon/print3d
- **GitHub repo:** [https://github.com/mfranzon/print3d](https://github.com/mfranzon/print3d)
- **Price:** Free (open-source code)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude code read @5ce50d5 (2026-11-14): caution. No network or telemetry. No fix: the MCP make tool runs model-written bpy Python in Blender (src/print3d/mcp_server.py:118-140) with no approval step and no setting to add one, so code runs outside Hermes's terminal approvals. Contain: run it only in the Hermes Docker backend, or skip the MCP and run the print3d CLI by hand after reading model.py.

## Safe install

Safe install (fixes applied):
Contain: Hermes Docker backend with Blender inside, or no MCP: read jobs/<slug>/model.py, then run the print3d CLI yourself.

## YOLO install

YOLO (your own risk): skips the container.
Add the print3d MCP to Hermes on your PC's local backend.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Contain: Hermes Docker backend with Blender inside, or no MCP: read jobs/<slug>/model.py, then run the print3d CLI yourself.
