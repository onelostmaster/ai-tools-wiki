# SoundCraft

- **Type:** app
- **Category:** creative tools, automation
- **Official URL:** https://github.com/storytold/soundcraft
- **GitHub repo:** https://github.com/storytold/soundcraft
- **Price:** Standalone app free, verified online 2026-11-07 at https://getartcraft.com/apps and individual app pages. Optional separate ArtCraft cloud-generation subscriptions not required for local editing. License MIT OR Apache-2.0 (Cargo.toml; GitHub detects Apache-2.0).
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-07

## Safety reason

Targeted source read only, not a full security/dependency/binary audit. Early/active-development editor with file-editing automation and updater code; use disposable copies and backups. No tracking SDK found in targeted runtime scan; this does NOT establish zero telemetry. Update machinery uses pinned external craft-libs dependency (Cargo.toml); consent/defaults and dependency internals not fully reviewed. Do not label updates silent or claim isolation. Agent file access is not a security sandbox. No blanket execution/permission grants; untrusted documents and tool output can carry prompt injection. Update source: crates/ui-egui/src/updates_ui.rs:8:use craft_update:\:updater\::\{Action, Status, Updater\}; Additional evidence: crates/engine/src/file_access.rs:308-324 path access tests (not executed); third-party audio/plugin behavior not fully audited.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

CAUTION: not installed. Ask the user before any install. Official Windows standalone/portable download: https://getartcraft.com/apps/soundcraft. Prefer one standalone app before a suite launcher. Compatible local MCP/CLI required; see repo README for app-specific commands. Windows binaries advertised; integration not tested. Hermes compatibility untested (generic MCP candidate only). claude.ai browser cannot directly execute these local programs; no Android-native support verified. Keep agent approvals on; no YOLO/skip-permissions; non-sensitive file copies, backups, no production keys; review update settings and optional remote/model/provider features before enabling. No install, build, test or repo script run.
