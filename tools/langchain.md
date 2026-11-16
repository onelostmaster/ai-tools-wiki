# LangChain

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://github.com/langchain-ai/langchain
- **GitHub repo:** https://github.com/langchain-ai/langchain @ 2775506 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02); LangSmith Plus $39 per seat a month (langchain.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @2775506, a review, 2026-11-02): safe. LangSmith tracing only when you set its env vars; no default telemetry found.

## Safe install

Safe install (fixes applied):
Windows (Python 3.10+, libs/langchain_v1/pyproject.toml:25): in a venv `pip install langchain==1.4.8` (the version at the reviewed 2775506, libs/langchain_v1/pyproject.toml:24; on PyPI since 2026-11-02). It sends nothing on its own; LangSmith tracing starts only when you set the LangSmith environment variables, so leave them unset unless you want traces uploaded. Put model API keys in environment variables or an untracked .env, never in committed code. claude.ai, Claude Code, Hermes, Android: no direct install (it is a library).

## YOLO install

YOLO (your own risk): skips the version pin (gets 1.5.0 from 2026-11-11, unreviewed) and the venv.
uv add langchain

## Install notes

Safe, but ask the user before installing.
Windows: `uv add langchain` (README) or pip. Android: no.
