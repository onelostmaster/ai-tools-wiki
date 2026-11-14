# print3d

- **Type:** MCP
- **Category:** 3D and games
- **Official URL:** https://github.com/mfranzon/print3d
- **GitHub repo:** [https://github.com/mfranzon/print3d](https://github.com/mfranzon/print3d)
- **Price:** Free (open-source code)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a project a review, 2026-10-28): Use with caution. No network or telemetry, but its MCP make tool runs model-written bpy Python in Blender with no approval step (`src/print3d/mcp_server.py:100-113`), i.e. code execution outside Hermes's terminal approvals.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

No install steps: the source withholds them until the tool is rated safe. Read the Safety reason and ask the user first.
