# DeepEval (Confident AI)

- **Type:** library
- **Category:** developer tools
- **Official URL:** https://github.com/confident-ai/deepeval
- **GitHub repo:** https://github.com/confident-ai/deepeval @ 8b584f2 (Apache-2.0)
- **Price:** Free, Apache-2.0; Confident AI hosted plans (prices not checked today, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @8b584f2, a review, 2026-11-02): caution. Sends usage events to PostHog unless DEEPEVAL_TELEMETRY_OPT_OUT is set (`deepeval/telemetry/client.py:55-56`, `api.py:64`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `pip install deepeval` in a venv; set DEEPEVAL_TELEMETRY_OPT_OUT=1. Claude Code: can test prompts and agents you build.
