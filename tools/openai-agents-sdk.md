# OpenAI Agents SDK

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://github.com/openai/openai-agents-python
- **GitHub repo:** https://github.com/openai/openai-agents-python @ e355d69 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02); OpenAI API usage is paid
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @e355d69, a review, 2026-11-02): safe. Tracing is on by default and goes to your own OpenAI account (`tracing/processors.py:46`); turn off with OPENAI_AGENTS_DISABLE_TRACING=1 (`tracing/provider.py:347-351`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: `pip install openai-agents` (README). Android: no.
