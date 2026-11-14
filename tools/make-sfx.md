# make-sfx

- **Type:** MCP
- **Category:** voice and audio, 3D and games
- **Official URL:** https://tuntii.github.io/make-sfx/
- **GitHub repo:** https://github.com/Tuntii/make-sfx @ a80f176 (2026-10-25, still HEAD on 2026-11-02; packages make-sfx-core and make-sfx-mcp 2.1.0, npm latest 2.0.0; MIT; named Tuntii/make-sfx by the scout)
- **Price:** Free (MIT, github.com, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read of packages/core/src and packages/mcp/src @a80f176, v2.1.0, 2026-11-02, no-intake review): Looks safe. No fetch, sockets, child_process, eval or env reads, no telemetry, no install scripts in either package. The DSP engine is a prebuilt WASM blob (packages/core/wasm) given only a no-op import (core/src/wasm.ts:86-88), so it cannot reach files or network; the blob was not rebuilt from engine/ to check it matches. MCP tools write WAV/JSON files to the outputDir the agent passes (mcp/src/utils.ts:66-71). Unpinned npx -y.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: MCP config `{ "mcpServers": { "make-sfx": { "command": "npx", "args": ["-y", "make-sfx-mcp"] } } }` (README); the library is `npm install make-sfx-core`.
Note: the reviewed code is the repo at a80f176 (make-sfx-mcp and make-sfx-core 2.1.0); npm latest on 2026-11-02 is 2.0.0, which was not diffed. `npx -y` fetches the newest npm version on every start, so pin a version (e.g. `make-sfx-mcp@2.0.0`) once you pick one.
Also ships Unity, Unreal and Roblox (Luau) integrations under integrations/ (not reviewed).
