# OpenAI Agents SDK

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://github.com/openai/openai-agents-python
- **GitHub repo:** https://github.com/openai/openai-agents-python @ e355d69 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02); OpenAI API usage is paid
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @e355d69, a review, 2026-11-02): safe. Tracing is on by default and goes to your own OpenAI account (`tracing/processors.py:46`); turn off with OPENAI_AGENTS_DISABLE_TRACING=1 (`tracing/provider.py:347-351`).

## Safe install

Safe install (fixes applied):
Windows (Python 3.10+, pyproject.toml:6): in a venv `pip install openai-agents==0.24.0` (the version at the reviewed e355d69, pyproject.toml:3; on PyPI since 2026-10-15). Tracing is on by default and uploads traces to your own OpenAI account (tracing/processors.py:46); set `OPENAI_AGENTS_DISABLE_TRACING=1` first (PowerShell: `$env:OPENAI_AGENTS_DISABLE_TRACING='1'`) unless you want them (tracing/provider.py:347-351). Put the OpenAI key in an environment variable, not in code. claude.ai, Claude Code, Hermes, Android: no direct install (it is a library).

## YOLO install

YOLO (your own risk): skips the venv and the tracing opt-out (traces go to your OpenAI account).
pip install openai-agents

## Install notes

Safe, but ask the user before installing.
Windows: `pip install openai-agents` (README). Android: no.
