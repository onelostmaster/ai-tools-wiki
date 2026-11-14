# REA (Reverse Engineer Anything) MCP + skill

- **Type:** MCP
- **Category:** Hermes add-ons, research, developer tools
- **Official URL:** https://rea.tools
- **GitHub repo:** https://github.com/morluto/rea @ 9bea563 (2026-11-02; npm rea-agents 6.8.0; MIT; not a fork; the earlier post card read "morutao/rea", which does not exist)
- **Price:** Free, MIT (LICENSE, checked 2026-11-02). Optional engines: Ghidra free; Hopper and IDA Pro are paid (prices not checked, not needed for JavaScript/Electron).
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (targeted code read @9bea563, a review, 2026-11-02; not a full audit of ~7,000 files): no telemetry (`src/hopper/HopperDiagnostics.ts:8` is local diagnostics); Claude plugin pins an exact version (`scripts/plugin-mcp-launcher.mjs:8-25`); no npm postinstall (`scripts/prepare.mjs:26-38`); updates only on `rea update` (`src/application/Update.ts:125,136`); JADX jar sha256-pinned. Caution: setup rewrites agents' MCP config and adds workflow instructions (backups, asks first); optional curl|bash `install.sh` (use npm); can download Hopper (`src/application/HopperReleaseFeed.ts:19-23`) and runs decompilers on any target; legal limits (DISCLAIMER.md bans DRM/anti-cheat bypass and cheats).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: npx rea-agents setup from a trusted folder outside any project, choose only Claude Code and review the proposed config changes (README Quick start); also ships as a Claude Code plugin (.claude-plugin/plugin.json). Use the npm route, not install.sh. Windows works (native Ghidra on Windows is experimental).
Hermes: listed as a supported client (docs/installation.md:652); same setup, pick Hermes.
Use only on your own apps or ones whose licence allows it.
