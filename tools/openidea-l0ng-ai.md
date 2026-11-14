# OpenIDEA (l0ng-ai)

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://github.com/l0ng-ai/openidea
- **GitHub repo:** https://github.com/l0ng-ai/openidea @ 4b1614a (Apache-2.0, `README.md:48-50`; Rust/Tauri)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-03)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @4b1614a, a review, 2026-11-03): safe. No telemetry found (LSP telemetry events dropped, `crates/ide-lsp/src/handler.rs:251`). Signed Tauri updater from GitHub releases: one silent startup check, installs only on click (`src/features/app/updates.tsx:86-101`, `src-tauri/src/commands/window.rs:304-345`; endpoint override OPENIDEA_UPDATE_ENDPOINT). The Claude Code panel passes --allow-dangerously-skip-permissions (`crates/ide-agent/src/native/claude/cli.rs:22`) so Bypass mode is selectable; the default mode still asks (`settings.rs:33-37`). Never pick Bypass.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: official build from the GitHub releases page (`README.md:22-26`); works with an existing Claude Code install; keep the agent panel on the default (ask) mode. Android: no.
