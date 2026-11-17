# Aura Autopilot

- **Type:** plugin
- **Category:** 3D and games, developer tools
- **Official URL:** https://tryaura.dev/autopilot
- **GitHub repo:** https://github.com/ramenvr/autopilot @ 48966d1 (Apache-2.0)
- **Price:** Free, open source (Apache-2.0); the Claude Code path uses your Claude subscription; the editor plugin uses an Aura plan (price unknown) or your own API keys (github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @1ebf2a5 (2026-11-16): safe with fixes. Run sharing to app.tryaura.dev is on unless AUTOPILOT_SHARE=0 or you untick it in setup (autopilot/telemetry.py:43-53). Model-written harness code runs in bubblewrap only on Linux; on Windows it is a plain child process (autopilot/sandbox.py:106). AUTOPILOT_SANDBOX=bwrap refuses to run without bubblewrap (lines 107-108). Fix: Linux or WSL with that setting.

## Safe install

Safe install (fixes applied):
Linux or WSL: env AUTOPILOT_SHARE=0 and AUTOPILOT_SANDBOX=bwrap, install bubblewrap; untick run sharing in setup; then autopilot connect claude. Native Windows only inside the spare YOLO-box account.

## YOLO install

YOLO (your own risk): skips sharing off and the sandbox, so harness code runs as you and runs upload.
Install on Windows with defaults.

## Install notes

Ask the user before installing.
Claude Code (local only): no install steps given (the source withholds them until the tool is rated safe); the README connects it with `autopilot connect claude` (user-scope MCP). Set `AUTOPILOT_SHARE=0` first. No Hermes support.
