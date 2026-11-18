# Agno

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://agno.com
- **GitHub repo:** https://github.com/agno-agi/agno @ b21807b (Apache-2.0)
- **Price:** SDK and runtime free (Apache-2.0); Pro control plane $150/mo (agno.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @8b5ce9f v3.2.0 (2026-11-17): safe with fixes. Agents default telemetry=True (libs/agno/agno/agent/agent.py:398-400) and report to os-api.agno.com (api/settings.py:57). AGNO_TELEMETRY=false is read by agents, teams and workflows (agent/_init.py:64, team/_init.py:483, workflow/workflow.py:2796). Fix: that env var, pinned version.

## Safe install

Safe install (fixes applied):
Own venv; pip install agno==3.2.0; env AGNO_TELEMETRY=false; model keys in env.

## YOLO install

YOLO (your own risk): skips telemetry off and the pin.
pip install -U agno with defaults.

## Install notes

Ask the user before installing.
Windows: Python package per its docs (not tested); set AGNO_TELEMETRY=false. Claude Code: can build agents that call Claude models. Android: no.
