# Pake

- **Type:** CLI
- **Category:** developer tools, building a site
- **Official URL:** https://pake.run
- **GitHub repo:** https://github.com/tw93/Pake @ 8163adf (GPL-3.0 with an output exception; HEAD on 2026-11-14, latest commit on 2026-11-14 04:13 ET; version 3.18.0)
- **Price:** Free (GPL-3.0, `github.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read @8163adf, 2026-11-14, no-intake review): Caution. About 6,200 lines of TypeScript CLI (bin/) plus a Rust/Tauri app shell (src-tauri/); no telemetry or analytics, no obfuscated payloads. Network: icon lookups send the target domain to logo.dev, Brandfetch, Clearbit, Google favicons and favicon.is using publishable keys embedded in the source (bin/options/icon.ts lines 85-88, 518-538); the Rust installer (winget Rustlang.Rustup on Windows, rustup.rs script elsewhere, bin/helpers/rust.ts lines 70-117) runs only after an interactive yes (bin/builders/BaseBuilder.ts lines 157-180) and never under --json. Built apps: withGlobalTauri on and csp null (src-tauri/tauri.conf.json lines 6, 14), but remote IPC is limited to the literal configured origin (src-tauri/src/app/config.rs lines 150-192), with downloads, notifications and shell open. dist/cli.js is a committed build artifact that CI checks against bin/ (.github/workflows/quality-and-test.yml lines 130-138); not diffed here. Why caution: the plugin's SKILL.md tells agents to npm install -g pake-cli unpinned (plugins/pake/skills/pake/SKILL.md line 17) and on ENV_MISSING to 'install and rerun' (line 41), so an agent may install software without asking. The repo's .claude/settings.json hook only applies inside a checkout and just prints a reminder. Replaces the earlier not-reviewed status.

## Safe install

Safe install (fixes applied):
Windows (Claude Code): install Node 20.9+, Rust (winget install Rustlang.Rustup), the Visual Studio C++ Build Tools and WebView2 yourself first, then pnpm install -g pake-cli@3.18.0 (pins the reviewed 8163adf release). Always pass --icon with your own icon file; otherwise the site's domain goes to logo.dev, Brandfetch, Clearbit, Google favicons and favicon.is (bin/options/icon.ts lines 85-88, 518-538). If you add the plugin (/plugin marketplace add tw93/Pake, /plugin install pake@pake), tell Claude to ask you before installing anything, because its SKILL.md tells it to npm install -g pake-cli unpinned (line 17) and to 'install and rerun' on ENV_MISSING (line 41). Wrap only sites you trust: the wrapped origin gets downloads, notifications and open-link commands (src-tauri/src/app/config.rs lines 150-192). Android: no.

## YOLO install

YOLO (your own risk): skips the version pin, the own-icon flag and the ask-first rule.
Windows: npm install -g pake-cli; answer yes to 'Rust not detected. Install now?' (winget install Rustlang.Rustup).

## Install notes

Code-reviewed by a review bot @8163adf (caution; see Safety reason). Claude Code on Windows: needs Node 20.9+, Rust (rustup) and the Visual Studio C++ Build Tools plus WebView2; install those yourself first, then pnpm install -g pake-cli@3.18.0 (pins the reviewed version; npm works too). The plugin (/plugin marketplace add tw93/Pake, then /plugin install pake@pake) adds only a skill: no hooks, no MCP server. Its SKILL.md tells the agent to npm install -g pake-cli (unpinned) when missing and, on ENV_MISSING, to 'install and rerun': tell Claude to ask you before installing anything. If Rust is missing, an interactive run asks 'Rust not detected. Install now?' and on yes runs winget install Rustlang.Rustup; --json runs never install. Without --icon, Pake sends the site's domain to icon services (logo.dev, Brandfetch, Clearbit, Google favicons); pass --icon with your own file to avoid that. The built app gives the wrapped site's own origin (only) access to Pake's app commands such as downloads, notifications and opening links; wrap only sites you trust. claude.ai and Android: not a fit (builds desktop apps on a local computer).
