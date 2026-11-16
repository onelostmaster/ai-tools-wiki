# Superpowers

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/obra/superpowers
- **GitHub repo:** [https://github.com/obra/superpowers](https://github.com/obra/superpowers)
- **Price:** Free (open-source)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read, 2ce8aa1, a project a review, 2026-10-31): Looks safe. Skills plus a SessionStart hook that injects the using-superpowers skill into every session. Telemetry: its brainstorm page loads a logo from `primeradiant.com` unless `SUPERPOWERS_DISABLE_TELEMETRY=1` is set.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): `/plugin install superpowers@claude-plugins-official` (README.md:65), and set the user environment variable SUPERPOWERS_DISABLE_TELEMETRY=1 first (PowerShell: `setx SUPERPOWERS_DISABLE_TELEMETRY 1`, then restart Claude Code), which stops the brainstorm page loading its logo from primeradiant.com (skills/brainstorming/scripts/server.cjs:106-108). It will add a SessionStart hook that runs on every startup, clear and compact (hooks/hooks.json); that cannot be turned off while the plugin is on, it is how the plugin loads its skills. The marketplace installs the latest version: reviewed commit 2ce8aa1, HEAD now 22f0b46 (2026-11-03) is not reviewed. Hermes: `hermes plugins install obra/superpowers --enable` (README.md:274) with the same environment variable. claude.ai and Android: no install route.

## YOLO install

YOLO (your own risk): skips the telemetry opt-out (the brainstorm page fetches its logo from primeradiant.com).
/plugin install superpowers@claude-plugins-official

## Install notes

Claude Code: `/plugin install superpowers@claude-plugins-official`
Hermes: `hermes plugins install obra/superpowers --enable` (README:274)
