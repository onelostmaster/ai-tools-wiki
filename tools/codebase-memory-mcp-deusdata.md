# codebase-memory-mcp (DeusData)

- **Type:** MCP
- **Category:** developer tools
- **Official URL:** https://github.com/DeusData/codebase-memory-mcp
- **GitHub repo:** https://github.com/DeusData/codebase-memory-mcp @ 190abae (MIT, `LICENSE:1`)
- **Price:** Free, MIT (github.com, checked 2026-11-03)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (light code read @190abae, 2026-11-03): caution. Its install/config step writes hooks into Claude Code settings.json (src/cli/cli.c:3434-3525) and a Codex SessionStart hook (src/cli/cli.c:4336); a self-update command pulls releases/latest on demand (src/cli/cli.c:14359). No telemetry found; daemon update check removed on purpose (src/daemon/application.c:72-84); graph UI binds 127.0.0.1 only (src/ui/http_server.c:13); install.sh verifies checksums.txt (install.sh:197-202) though it is offered as curl|bash (install.sh:7). Fix-rule re-rate 2026-11-18: every verified risk has its exact fix in Safe install (install.ps1 read before running at 190abae, unwanted hooks removed from settings.json afterwards, self-update never run); with those fixes applied: safe.

## Safe install

Safe install (fixes applied):
Windows: download install.ps1 from https://github.com/DeusData/codebase-memory-mcp at commit 190abae, read it, then run it (README.md:81-94); do not pipe an install script straight into a shell. Its config step will write hooks into Claude Code settings.json (src/cli/cli.c:3434-3525) and a Codex SessionStart hook (src/cli/cli.c:4336): afterwards open %USERPROFILE%\.claude\\settings.json and remove any hook you don't want. Don't run its self-update command (it pulls releases/latest, src/cli/cli.c:14359); update by repeating these steps at a newer reviewed commit. Graph UI is 127.0.0.1 only (src/ui/http_server.c:13); no telemetry found. Claude Code and Hermes via MCP. Android: no.

## YOLO install

YOLO (your own risk): skips reading the script, the hook check and the no-self-update rule.
Windows: run the README's one-line installer and keep the hooks it writes; update with its self-update command (latest release).

## Install notes

Ask the user before installing. Safe only with the fixes in Safe install applied.
Windows: download install.ps1, read it, then run it (README.md:81-94); check the hooks it adds to Claude Code settings.json afterwards. Claude Code and Hermes via MCP. Android: no.
