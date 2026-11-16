# Google ADK (adk-python)

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://github.com/google/adk-python
- **GitHub repo:** https://github.com/google/adk-python @ 3565ad3 (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); Gemini or other model calls are paid
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @3565ad3, a review, 2026-11-02): safe. Tracing is OpenTelemetry you point somewhere yourself (`src/google/adk/telemetry/`); no phone-home found (posthog only as a third-party pin in `constraints-3.11.txt:1486`).

## Safe install

Safe install (fixes applied):
Windows (Python 3.11+, pyproject.toml:15): in a venv `pip install google-adk==2.13.0` (the version at the reviewed 3565ad3, src/google/adk/version.py:16; on PyPI since 2026-10-23). Telemetry is OpenTelemetry that goes only where you point it (src/google/adk/telemetry/); configure no exporter and nothing leaves. Put the Gemini or other model key in an environment variable or an untracked .env. claude.ai, Claude Code, Hermes, Android: no direct install (it is a library).

## YOLO install

YOLO (your own risk): skips the version pin (gets 2.14.1 from 2026-11-12, unreviewed) and the venv.
pip install google-adk

## Install notes

Safe, but ask the user before installing.
Windows: `pip install google-adk` (README). Android: no.
