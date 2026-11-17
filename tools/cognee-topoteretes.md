# Cognee (topoteretes)

- **Type:** MCP
- **Category:** research, Hermes add-ons, developer tools
- **Official URL:** https://github.com/topoteretes/cognee
- **GitHub repo:** https://github.com/topoteretes/cognee @ 525b1d1 (Apache-2.0; v1.6.6)
- **Price:** Self-host free, Apache-2.0 (github.com, checked 2026-11-02); hosted plans unknown
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @5870f15 = 1.6.8 (2026-11-16): safe with fixes. Telemetry is on by default and goes to the vendor proxy (cognee/shared/utils.py:23), with a hashed LLM_API_KEY as an ID (line 406); TELEMETRY_DISABLED=1 stops all of it (line 575). Memory text goes to your own LLM provider.

## Safe install

Safe install (fixes applied):
Env TELEMETRY_DISABLED=1 first; pip install cognee==1.6.8 in its own venv, or cognee-mcp per its README with the same env; LLM key in env, never in chat.

## YOLO install

YOLO (your own risk): skips telemetry off and the pin.
pip install cognee with defaults.

## Install notes

Ask the user before installing.
Claude Code: add the cognee-mcp server per its README with TELEMETRY_DISABLED=1.
Hermes: connect over MCP (its app has a Hermes Agent card).
Windows: Python or Docker (not tested). Android: no.
