# PdfCraft

- **Type:** app
- **Category:** creative tools, automation
- **Official URL:** https://github.com/storytold/pdfcraft
- **GitHub repo:** https://github.com/storytold/pdfcraft
- **Price:** Standalone app free, verified online 2026-11-07 at https://getartcraft.com/apps and individual app pages. Optional separate ArtCraft cloud-generation subscriptions not required for local editing. License MIT OR Apache-2.0 (Cargo.toml; GitHub detects Apache-2.0).
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Targeted source read only, not a full security/dependency/binary audit. Early/active-development editor with file-editing automation and updater code; use disposable copies and backups. No tracking SDK found in targeted runtime scan; this does NOT establish zero telemetry. Update machinery uses pinned external craft-libs dependency (Cargo.toml); consent/defaults and dependency internals not fully reviewed. Do not label updates silent or claim isolation. Agent file access is not a security sandbox. No blanket execution/permission grants; untrusted documents and tool output can carry prompt injection. Update source: crates/ui-egui/src/platform/updates.rs:6:use craft_update:\:updater\::\{Action, CheckSource, Status, Updater\}; Additional evidence: crates/ui-egui/src/app.rs:137 startup update check defaults true; crates/ui-egui/src/app/commands.rs:29 AI provider features off by default; crates/print/src/spool.rs:22 external printer command on Unix. Review provider storage before enabling any cloud provider. Fix-rule re-rate 2026-11-18: no verified risk lacks a fix; the unverified items (update-check payload, updater dependency internals, telemetry) each have a containment step in Safe install (portable build from the official getartcraft.com page only, work on copies with backups, in-app updates declined and new builds downloaded by hand (contains the unverified update-check payload and the unreviewed craft-libs updater), MCP tool approvals kept per call with no blanket grants, and the per-app items listed in Safe install); with those fixes applied: safe.

## Safe install

Safe install (fixes applied):
Windows: download the standalone portable build only from https://getartcraft.com/apps/pdfcraft (official page for github.com/storytold/pdfcraft); nothing else gets installed. Open only copies of your files and keep backups, because an agent connected over MCP edits files directly. Updates run through craft_update::updater (crates/ui-egui/src/platform/updates.rs:6; the startup update check is on by default, crates/ui-egui/src/app.rs:137); unverified: what the update check sends, so contain it: decline in-app updates and update by downloading a new build from the official page. AI provider features are off by default (crates/ui-egui/src/app/commands.rs:29); leave them off, and unverified: how provider keys are stored, so put no API keys in it. The external printer command is Unix-only (crates/print/src/spool.rs:22) and does not apply on Windows. Claude Code (Windows): add the local stdio MCP command from the repo README as an MCP server; keep tool approvals on and never start it with --dangerously-skip-permissions. Hermes: untested, generic MCP only; keep approvals on. claude.ai, Android: no (local Windows program).

## YOLO install

YOLO (your own risk): skips working on copies and backups and the update containment.
Windows: download from https://getartcraft.com/apps/pdfcraft, open your real files, connect its MCP in Claude Code and accept in-app updates.

## Install notes

CAUTION: not installed. Ask the user before any install. Official Windows standalone/portable download: https://getartcraft.com/apps/pdfcraft. Prefer one standalone app before a suite launcher. Compatible local MCP/CLI required; see repo README for app-specific commands. Windows binaries advertised; integration not tested. Hermes compatibility untested (generic MCP candidate only). claude.ai browser cannot directly execute these local programs; no Android-native support verified. Keep agent approvals on; no YOLO/skip-permissions; non-sensitive file copies, backups, no production keys; review update settings and optional remote/model/provider features before enabling. No install, build, test or repo script run.
