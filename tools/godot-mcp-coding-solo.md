# godot-mcp (Coding-Solo)

- **Type:** MCP
- **Category:** 3D and games, developer tools
- **Official URL:** https://github.com/Coding-Solo/godot-mcp
- **GitHub repo:** https://github.com/Coding-Solo/godot-mcp @ 1209744 (MIT; pushed 2026-04-16; not a fork)
- **Price:** Free, MIT (github.com, checked 2026-11-02); Godot is free
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @1209744, sweep 2026-11-02): safe. Calls Godot with argument arrays, not a shell (`src/index.ts:509-528`); launches the editor at `src/index.ts:1020`; no network calls found. run_project runs your own game code. README installs via npx, unpinned.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): claude mcp add godot -e GODOT_PATH="C:\\Path\\To\\Godot.exe" -- npx -y @coding-solo/godot-mcp@0.1.1 (version pinned, npm latest on 2026-11-16; GODOT_PATH per README.md:100). No network calls found and no shell (src/index.ts:509-528). run_project runs your own game code (nothing to fix; it is your code). Needs Node.js and Godot. Hermes: same npx command as a plain MCP server. claude.ai, Android: no.

## YOLO install

YOLO (your own risk): skips the version pin.
claude mcp add godot -- npx @coding-solo/godot-mcp (README.md:92)

## Install notes

Safe, but ask the user before installing.
Claude Code: `claude mcp add godot -- npx @coding-solo/godot-mcp` (README.md:92); pin a version; set GODOT_PATH if Godot is not on PATH (README.md:100).
Windows: Godot is free on Windows; needs Node.js.
