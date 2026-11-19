# Cua Spaces plugin

- **Type:** plugin
- **Category:** Hermes add-ons, automation
- **Official URL:** https://github.com/trycua/hermes-cua-spaces
- **GitHub repo:** [https://github.com/trycua/hermes-cua-spaces](https://github.com/trycua/hermes-cua-spaces)
- **Price:** unknown (Cua cloud pricing not verified)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, repo head 82bb8d3, a review): Looks safe. Small (1.6k lines), only shells out to the cua CLI, no telemetry of its own. It needs Cua's own curl/sh installer, which was not reviewed; the cua package has opt-out telemetry.

## Safe install

Safe install (fixes applied):
Hermes (Windows, Git Bash): install Cua first without piping a script into sh: save https://cua.ai/install.sh, read it, then run it (README.md line 19 uses curl | sh). unverified: install.sh and the cua package were not code-reviewed; contain it by using a local Space (no cua auth login needed, README.md line 16) and by not passing --env-from-host with your API keys (README.md line 117). Turn Cua's usage telemetry off with cua telemetry off or CUA_TELEMETRY=0 (README.md line 177; on by default). Then hermes plugins install https://github.com/trycua/hermes-cua-spaces and say yes to the one cua Python package (README.md lines 26-29); the plugin was reviewed at 82bb8d3 and head is now 52e794e (README re-read only). Leave desktop: false (default) unless you want it to install TigerVNC, Playwright Chromium and cua-driver inside the Space (README.md lines 50, 164-170). The Space keeps running after Hermes exits; stop it with cua spaces stop hermes-default (README.md line 69). Claude Code, claude.ai, Android: no.

## YOLO install

YOLO (your own risk): skips reading the installer and the telemetry opt-out.
Hermes: curl -fsSL https://cua.ai/install.sh | sh, cua auth login, then hermes plugins install https://github.com/trycua/hermes-cua-spaces.

## Install notes

Hermes: `hermes plugins install https://github.com/trycua/hermes-cua-spaces`
Hermes: it also needs Cua's own curl/sh installer, which was not reviewed; ask the user before running it.
