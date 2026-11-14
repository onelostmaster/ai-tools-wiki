# Aura Autopilot

- **Type:** plugin
- **Category:** 3D and games, developer tools
- **Official URL:** https://tryaura.dev/autopilot
- **GitHub repo:** https://github.com/ramenvr/autopilot @ 48966d1 (Apache-2.0)
- **Price:** Free, open source (Apache-2.0); the Claude Code path uses your Claude subscription; the editor plugin uses an Aura plan (price unknown) or your own API keys (github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (code read @48966d1) and Claude (@48966d1), 2026-11-01: caution. Run-data sharing ON by default (`autopilot/telemetry.py`): uploads full LLM calls, recordings and decisions to `app.tryaura.dev`, redacted, even on your own keys; off with AUTOPILOT_SHARE=0. Model-written harness code is exec'd; sandbox isolates only on Linux with bubblewrap (plain child process on Windows). install.sh pipes curl to sh. Writes limited to the run folder.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code (local only): no install steps given (the source withholds them until the tool is rated safe); the README connects it with `autopilot connect claude` (user-scope MCP). Set `AUTOPILOT_SHARE=0` first. No Hermes support.
