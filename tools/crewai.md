# CrewAI

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://crewai.com
- **GitHub repo:** https://github.com/crewAIInc/crewAI @ 86dca29 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02); CrewAI AMP Basic free with 50 runs a month, Enterprise custom (crewai.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (light code read @86dca29, a review, 2026-11-02): caution. Anonymous telemetry to `telemetry.crewai.com:4319` (`lib/crewai/src/crewai/telemetry/constants.py:9`) unless OTEL_SDK_DISABLED, CREWAI_DISABLE_TELEMETRY or CREWAI_DISABLE_TRACKING is set (`lib/crewai-core/src/crewai_core/telemetry.py:354-359`); share_crew=True also sends task content (`telemetry/telemetry.py:307`). README CLI setup uses the uv curl | sh installer.

## Safe install

Safe install (fixes applied):
Windows: in a venv, pip install crewai==<release matching 86dca29> (README); do not use the uv curl | sh installer from the README. Set the user env var CREWAI_DISABLE_TELEMETRY=true (or OTEL_SDK_DISABLED=true) before first use; otherwise it sends anonymous telemetry to telemetry.crewai.com:4319 (lib/crewai/src/crewai/telemetry/constants.py:9; lib/crewai-core/src/crewai_core/telemetry.py:354-359). Keep share_crew=False (the default) so task content is never sent (telemetry/telemetry.py:307). Android: no.

## YOLO install

YOLO (your own risk): skips the version pin and the telemetry switch.
Windows: uv curl | sh installer then uv tool install crewai (README); anonymous telemetry stays on.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `uv tool install crewai` (README); set CREWAI_DISABLE_TELEMETRY=true and keep share_crew off. Android: no.
