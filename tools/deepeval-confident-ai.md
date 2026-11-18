# DeepEval (Confident AI)

- **Type:** library
- **Category:** developer tools
- **Official URL:** https://github.com/confident-ai/deepeval
- **GitHub repo:** https://github.com/confident-ai/deepeval @ 8b584f2 (Apache-2.0)
- **Price:** Free, Apache-2.0; Confident AI hosted plans (prices not checked today, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (light code read @8b584f2, a review, 2026-11-02): caution. Sends usage events to PostHog unless DEEPEVAL_TELEMETRY_OPT_OUT is set (`deepeval/telemetry/client.py:55-56`, `api.py:64`).

## Safe install

Safe install (fixes applied):
Windows: in a venv, pip install deepeval==<release matching 8b584f2>. Set the user env var DEEPEVAL_TELEMETRY_OPT_OUT=1 before first use; otherwise it sends usage events to PostHog (deepeval/telemetry/client.py:55-56, api.py:64). Claude Code: use it to test prompts and agents you build. Android: no.

## YOLO install

YOLO (your own risk): skips the version pin and the telemetry opt-out.
Windows: pip install deepeval; PostHog usage events stay on.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `pip install deepeval` in a venv; set DEEPEVAL_TELEMETRY_OPT_OUT=1. Claude Code: can test prompts and agents you build.
