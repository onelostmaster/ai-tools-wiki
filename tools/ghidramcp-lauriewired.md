# GhidraMCP (LaurieWired)

- **Type:** MCP
- **Category:** security, developer tools, 3D and games
- **Official URL:** https://github.com/LaurieWired/GhidraMCP
- **GitHub repo:** https://github.com/LaurieWired/GhidraMCP @ 1e98025 (Apache-2.0; pushed 2026-10-10; not a fork)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (light code read @1e98025, sweep 2026-11-02): safe. Backend listens on loopback only (`BackendHttpServer.java:61`) and rejects foreign Host headers (`:36,195-203`); write tools only rename, retype or comment in the open program (`src/ghidra_mcp/server.py:200-258`). The binary's code goes to whichever LLM you use. README installs from git main, unpinned.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Claude Code: `claude mcp add ghidra -- uvx --from git+https://github.com/LaurieWired/GhidraMCP ghidra-mcp --ghidra-server http://127.0.0.1:8080/` (README.md:104); pin a commit. Needs Ghidra 12.1.4+ with the extension.
Windows: works with Ghidra on Windows. Only reverse-engineer software you own or are allowed to.
