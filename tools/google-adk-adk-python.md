# Google ADK (adk-python)

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://github.com/google/adk-python
- **GitHub repo:** https://github.com/google/adk-python @ 3565ad3 (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); Gemini or other model calls are paid
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @3565ad3, a review, 2026-11-02): safe. Tracing is OpenTelemetry you point somewhere yourself (`src/google/adk/telemetry/`); no phone-home found (posthog only as a third-party pin in `constraints-3.11.txt:1486`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: `pip install google-adk` (README). Android: no.
