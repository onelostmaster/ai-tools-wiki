# LangGraph

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://github.com/langchain-ai/langgraph
- **GitHub repo:** https://github.com/langchain-ai/langgraph @ 3c916d7 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02); LangSmith Plus $39 per seat a month (langchain.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @3c916d7, a review, 2026-11-02): safe. The langgraph CLI sends usage analytics unless LANGGRAPH_CLI_NO_ANALYTICS=1 (`libs/cli/langgraph_cli/analytics.py:89`); the library itself has none. LangSmith tracing only when you set its env vars.

## Safe install

Safe install (fixes applied):
Windows (Python 3.10+, libs/langgraph/pyproject.toml:10): in a venv `pip install langgraph==1.2.19` (the version at the reviewed 3c916d7, libs/langgraph/pyproject.toml:7). The library sends nothing on its own; LangSmith tracing starts only when you set the LangSmith environment variables, so leave them unset unless you want traces uploaded. If you use the langgraph CLI, set `LANGGRAPH_CLI_NO_ANALYTICS=1` first (PowerShell: `$env:LANGGRAPH_CLI_NO_ANALYTICS='1'`); without it every CLI command sends OS, OS version and Python version (libs/cli/langgraph_cli/analytics.py:89-95). claude.ai, Claude Code, Hermes, Android: no direct install (it is a library).

## YOLO install

YOLO (your own risk): skips the version pin (gets 1.2.22 from 2026-11-14, unreviewed), the venv and the CLI analytics opt-out.
pip install -U langgraph

## Install notes

Safe, but ask the user before installing.
Windows: `pip install -U langgraph` (README); set LANGGRAPH_CLI_NO_ANALYTICS=1 if you use the CLI. Android: no.
