# Craft Anything (ArtCraft workbench)

- **Type:** app
- **Category:** developer tools, automation
- **Official URL:** https://github.com/storytold/craft-anything
- **GitHub repo:** https://github.com/storytold/craft-anything
- **Price:** Free standalone alpha; online official catalog/repo checked 2026-11-08. MIT OR Apache-2.0 at your option (README.md:410-414; Cargo.toml:8; LICENSE-MIT/LICENSE-APACHE). Fonts/icons/assets retain separate notices; ArtCraft brand assets are trademarks, not covered by the code license (NOTICE). Your coding-agent subscription/API usage, optional image/3D assets, engines and hosting are billed separately by their own providers. Managed tier is future/planned, not a verified current price. No exact paid rate guessed.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Claude code read @b935cb3 (2026-11-18): safe with fixes. Auto mode is on by default (crates/engine/src/settings.rs:107-113,215); in Auto, commands outside the usual build list are allowed (workspace.rs:1185). Every other action goes through its approve tool, and push, publish, system changes and outside deletes are never done unasked (docs/claude-code.md:25-37). Not an OS sandbox. Fix: Auto mode off, per-kind Ask.

## Safe install

Safe install (fixes applied):
Windows signed build from https://getartcraft.com/apps/craft-anything or GitHub Releases; Settings → Auto mode off (auto_mode = false); set commands, web and outside files to Ask per project; never Always on push or delete.

## YOLO install

YOLO (your own risk): skips Auto mode off.
Let builds run in Auto mode with default approvals.

## Install notes

CAUTION: not installed; show Safety reason and obtain approval per install. DOCUMENTED ONLY, not run. Windows: official signed MSI/portable builds are linked at https://getartcraft.com/apps/craft-anything and GitHub Releases (README.md:267-279); use a standalone x64/ARM64 build matching the PC, verify official checksum/signature before trying. Portable settings live beside app per README. Source alternative, requires Rust >=1.97 (README.md:195-208): git clone https://github.com/storytold/craft-anything ; cd craft-anything ; cargo run --release -p craft-anything ; cargo install --path apps/craft-anything-cli. Then documented CLI checks/setup: craft-anything-cli doctor ; craft-anything-cli commands ; craft-anything-cli mcp ; craft-anything-cli setup. Setup is a configuration write, not an action performed here. No cargo build/install or app/doctor/setup/MCP command executed. Claude Code: Windows desktop app launches your installed/signed-in claude as builder, or its local CLI/MCP can be registered after approval. claude.ai browser is not this local builder; no documented equivalent local-execution integration verified. Hermes: explicitly named ACP candidate (README.md:164-166), but only Maki live-verified among that group; Hermes builder integration UNTESTED. Generic MCP access is also a candidate, not tested here. Android: no native mobile builder/agent host verified. Limited WebAssembly file viewer (README.md:355-359) is not the full desktop build workflow; no Android parity claim. First trial: Auto OFF, Clean room ON, disposable owned project, no keys/plugins/remote execution, strict command/network/outside-file/publishing/delete/system approvals; no blanket permissions.
