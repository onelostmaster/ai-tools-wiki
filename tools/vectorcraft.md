# VectorCraft

- **Type:** app
- **Category:** creative tools, automation
- **Official URL:** https://github.com/storytold/vectorcraft
- **GitHub repo:** https://github.com/storytold/vectorcraft
- **Price:** Standalone app free, verified online 2026-11-07 at https://getartcraft.com/apps and individual app pages. Optional separate ArtCraft cloud-generation subscriptions not required for local editing. License MIT OR Apache-2.0 (Cargo.toml; GitHub detects Apache-2.0).
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Claude code read @dce8a0c (2026-11-18): safe with fixes, same pattern as the other Craft apps. Updates go through craft_update (crates/ui-egui/src/updates_ui.rs:8); the desktop app checks for one at startup. MCP is stdio only (crates/mcp/src/lib.rs:1-5). Its MCP edits files directly. Fix: portable build, copies of your files, updates by hand.

## Safe install

Safe install (fixes applied):
Windows: portable build only from https://getartcraft.com/apps/vectorcraft; work on copies with backups; decline in-app updates and download new builds by hand; AI provider features off, no API keys in it; add its local stdio MCP in Claude Code with tool approvals on.

## YOLO install

YOLO (your own risk): skips copies, backups and manual updates.
Install from getartcraft.com, open your real files and accept in-app updates.

## Install notes

CAUTION: not installed. Ask the user before any install. Official Windows standalone/portable download: https://getartcraft.com/apps/vectorcraft. Prefer one standalone app before a suite launcher. Compatible local MCP/CLI required; see repo README for app-specific commands. Windows binaries advertised; integration not tested. Hermes compatibility untested (generic MCP candidate only). claude.ai browser cannot directly execute these local programs; no Android-native support verified. Keep agent approvals on; no YOLO/skip-permissions; non-sensitive file copies, backups, no production keys; review update settings and optional remote/model/provider features before enabling. No install, build, test or repo script run.
