# Superpowers

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/obra/superpowers
- **GitHub repo:** [https://github.com/obra/superpowers](https://github.com/obra/superpowers)
- **Price:** Free (open-source)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (code read, 2ce8aa1, a project a review, 2026-10-31): Looks safe. Skills plus a SessionStart hook that injects the using-superpowers skill into every session. Telemetry: its brainstorm page loads a logo from `primeradiant.com` unless `SUPERPOWERS_DISABLE_TELEMETRY=1` is set.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `/plugin install superpowers@claude-plugins-official`
Hermes: `hermes plugins install obra/superpowers --enable` (README:274)
