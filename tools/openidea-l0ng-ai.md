# OpenIDEA (l0ng-ai)

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://github.com/l0ng-ai/openidea
- **GitHub repo:** https://github.com/l0ng-ai/openidea @ 4b1614a (Apache-2.0, `README.md:48-50`; Rust/Tauri)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-03)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @4b1614a, a review, 2026-11-03): safe. No telemetry found (LSP telemetry events dropped, `crates/ide-lsp/src/handler.rs:251`). Signed Tauri updater from GitHub releases: one silent startup check, installs only on click (`src/features/app/updates.tsx:86-101`, `src-tauri/src/commands/window.rs:304-345`; endpoint override OPENIDEA_UPDATE_ENDPOINT). The Claude Code panel passes --allow-dangerously-skip-permissions (`crates/ide-agent/src/native/claude/cli.rs:22`) so Bypass mode is selectable; the default mode still asks (`settings.rs:33-37`). Never pick Bypass.

## Safe install

Safe install (fixes applied):
Windows: OpenIDEA_0.1.45_windows_x64_portable.zip from the official GitHub release v0.1.45 (github.com/l0ng-ai/openidea/releases), and check it with `certutil -hashfile OpenIDEA_0.1.45_windows_x64_portable.zip SHA256` against the .sha256 file in the same release. Keep the Claude Code panel on the default ask mode and never pick Bypass (the panel passes --allow-dangerously-skip-permissions, crates/ide-agent/src/native/claude/cli.rs:22; default mode settings.rs:33-37). The updater checks once at startup and installs only when you click (src/features/app/updates.tsx:86-101). Unverified: v0.1.45 is 1,555 commits past the reviewed 4b1614a; contain it: no API keys in its environment beyond your existing Claude Code login, open only your own projects, and get a re-review before relying on it. Not a claude.ai, Hermes or Android tool.

## YOLO install

YOLO (your own risk): skips the checksum and the re-review.
OpenIDEA_0.1.45_x64-setup.exe from the GitHub release.

## Install notes

Safe, but ask the user before installing.
Windows: official build from the GitHub releases page (`README.md:22-26`); works with an existing Claude Code install; keep the agent panel on the default (ask) mode. Android: no.
