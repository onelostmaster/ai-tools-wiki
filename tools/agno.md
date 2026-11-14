# Agno

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://agno.com
- **GitHub repo:** https://github.com/agno-agi/agno @ b21807b (Apache-2.0)
- **Price:** SDK and runtime free (Apache-2.0); Pro control plane $150/mo (agno.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @b21807b, a review, 2026-11-02): caution. Agents, teams and workflows default telemetry=True (`libs/agno/agno/agent/agent.py:396-399`) and report to `os-api.agno.com` (`api/settings.py:57`); turn off with AGNO_TELEMETRY=false (`workflow/workflow.py:2796-2798`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: Python package per its docs (not tested); set AGNO_TELEMETRY=false. Claude Code: can build agents that call Claude models. Android: no.
