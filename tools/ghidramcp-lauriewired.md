# GhidraMCP (LaurieWired)

- **Type:** MCP
- **Category:** security, developer tools, 3D and games
- **Official URL:** https://github.com/LaurieWired/GhidraMCP
- **GitHub repo:** https://github.com/LaurieWired/GhidraMCP @ 1e98025 (Apache-2.0; pushed 2026-10-10; not a fork)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @1e98025, sweep 2026-11-02): safe. Backend listens on loopback only (`BackendHttpServer.java:61`) and rejects foreign Host headers (`:36,195-203`); write tools only rename, retype or comment in the open program (`src/ghidra_mcp/server.py:200-258`). The binary's code goes to whichever LLM you use. README installs from git main, unpinned.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): install Ghidra 12.1.4+ and the GhidraMCP extension, then claude mcp add ghidra -- uvx --from git+https://github.com/LaurieWired/GhidraMCP@1e980252087b2479a21b9ca6d82d5829538651a7 ghidra-mcp --ghidra-server http://127.0.0.1:8080/ (pinned to the reviewed commit; README.md:104 uses unpinned main). Backend is loopback only (BackendHttpServer.java:61). The binary's code goes to the LLM you use: only open software you own or are allowed to reverse-engineer. Hermes: same uvx command. claude.ai, Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin.
claude mcp add ghidra -- uvx --from git+https://github.com/LaurieWired/GhidraMCP ghidra-mcp --ghidra-server http://127.0.0.1:8080/ (README.md:104)

## Install notes

Safe, but ask the user before installing.
Claude Code: `claude mcp add ghidra -- uvx --from git+https://github.com/LaurieWired/GhidraMCP ghidra-mcp --ghidra-server http://127.0.0.1:8080/` (README.md:104); pin a commit. Needs Ghidra 12.1.4+ with the extension.
Windows: works with Ghidra on Windows. Only reverse-engineer software you own or are allowed to.
