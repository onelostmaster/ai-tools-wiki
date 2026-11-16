# AG2

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://ag2.ai
- **GitHub repo:** https://github.com/ag2ai/ag2 @ 9cfbb69 (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); model calls are paid
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @9cfbb69, a review, 2026-11-02): safe. Telemetry is OpenTelemetry spans you export yourself (`ag2/network/hub/telemetry.py:5-20`); no phone-home found in the paths read.

## Safe install

Safe install (fixes applied):
Windows (Python 3.10+, pyproject.toml:36): in a venv `pip install "ag2[openai]==1.2.2"` (the version at the reviewed 9cfbb69, pyproject.toml:38; on PyPI since 2026-10-27). Telemetry is OpenTelemetry spans that go only where you export them (ag2/network/hub/telemetry.py:5-20). Put model API keys in environment variables, not in committed config files. Agents that run code: keep code execution in Docker or off, not on your own machine. For old AutoGen code use ag2-classic instead (README). claude.ai, Claude Code, Hermes, Android: no direct install (it is a library).

## YOLO install

YOLO (your own risk): skips the version pin (gets 1.3.2 from 2026-11-15, unreviewed) and the venv.
pip install ag2[openai]

## Install notes

Safe, but ask the user before installing.
Windows: `pip install ag2[openai]` (README); `pip install ag2-classic` for old AutoGen code. Android: no.
