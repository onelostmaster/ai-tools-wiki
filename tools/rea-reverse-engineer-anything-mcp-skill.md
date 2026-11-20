# REA (Reverse Engineer Anything) MCP + skill

- **Type:** MCP
- **Category:** Hermes add-ons, research, developer tools
- **Official URL:** https://rea.tools
- **GitHub repo:** https://github.com/morluto/rea @ 9bea563 (2026-11-02; npm rea-agents 6.8.0; MIT; not a fork; the earlier post card read "morutao/rea", which does not exist)
- **Price:** Free, MIT (LICENSE, checked 2026-11-02). Optional engines: Ghidra free; Hopper and IDA Pro are paid (prices not checked, not needed for JavaScript/Electron).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @9bea563 rea-agents 6.8.0 (2026-11-19): safe with fixes. No telemetry; updates only via rea update (src/application/Update.ts:125,136); no npm postinstall (package.json:288 is prepare only). Decompiled text reaching the agent is data like any web page: Claude Code's permission prompts gate every action it asks for. Fix: pinned npx setup, review each config change, decline Hopper, approvals on, copies of targets.

## Safe install

Safe install (fixes applied):
Windows (Claude Code): from a folder outside any project, run npx rea-agents@6.8.0 setup (pins the reviewed 9bea563 release; the Claude plugin launcher pins an exact version too, scripts/plugin-mcp-launcher.mjs lines 8-25). Choose only Claude Code (or Hermes) and read each proposed MCP config change before saying yes. Do not use the curl | bash install.sh. Update only with rea update when you choose (src/application/Update.ts lines 125, 136). Decline the Hopper download (src/application/HopperReleaseFeed.ts lines 19-23). Use only on apps you own or whose licence allows it; DISCLAIMER.md bans DRM/anti-cheat bypass and cheats. Keep Claude Code's permission prompts on (never --dangerously-skip-permissions) so text inside a decompiled target can't trigger actions; decompile copies of target files; keep other API keys out of its MCP config. Android: no.

## YOLO install

YOLO (your own risk): skips the version pin and the per-change config review.
Claude Code: npx rea-agents setup with the defaults.

## Install notes

Ask the user before installing.
Claude Code: npx rea-agents setup from a trusted folder outside any project, choose only Claude Code and review the proposed config changes (README Quick start); also ships as a Claude Code plugin (.claude-plugin/plugin.json). Use the npm route, not install.sh. Windows works (native Ghidra on Windows is experimental).
Hermes: listed as a supported client (docs/installation.md:652); same setup, pick Hermes.
Use only on your own apps or ones whose licence allows it.
