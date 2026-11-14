# Cognee (topoteretes)

- **Type:** MCP
- **Category:** research, Hermes add-ons, developer tools
- **Official URL:** https://github.com/topoteretes/cognee
- **GitHub repo:** https://github.com/topoteretes/cognee @ 525b1d1 (Apache-2.0; v1.6.6)
- **Price:** Self-host free, Apache-2.0 (github.com, checked 2026-11-02); hosted plans unknown
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @525b1d1, a review / Hermes a review, 2026-11-02): caution. Telemetry is ON by default to the vendor proxy (`cognee/shared/utils.py:23`, `:408`) and includes a salted hash of your LLM_API_KEY as a stable tracking ID (`:421-441`) plus anonymous and persistent IDs; opt out with TELEMETRY_DISABLED=1 (`:592`). Ships a ready Hermes Agent connection card (`cognee-frontend/src/modules/integrations/agentCards.tsx:141-144`). Uses your own LLM key; no curl | bash found in the paths read.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: add the cognee-mcp server per its README with TELEMETRY_DISABLED=1.
Hermes: connect over MCP (its app has a Hermes Agent card).
Windows: Python or Docker (not tested). Android: no.
