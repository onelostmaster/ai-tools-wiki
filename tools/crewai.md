# CrewAI

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://crewai.com
- **GitHub repo:** https://github.com/crewAIInc/crewAI @ 86dca29 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02); CrewAI AMP Basic free with 50 runs a month, Enterprise custom (crewai.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @86dca29, a review, 2026-11-02): caution. Anonymous telemetry to `telemetry.crewai.com:4319` (`lib/crewai/src/crewai/telemetry/constants.py:9`) unless OTEL_SDK_DISABLED, CREWAI_DISABLE_TELEMETRY or CREWAI_DISABLE_TRACKING is set (`lib/crewai-core/src/crewai_core/telemetry.py:354-359`); share_crew=True also sends task content (`telemetry/telemetry.py:307`). README CLI setup uses the uv curl | sh installer.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `uv tool install crewai` (README); set CREWAI_DISABLE_TELEMETRY=true and keep share_crew off. Android: no.
