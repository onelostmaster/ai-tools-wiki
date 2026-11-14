# LangGraph

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://github.com/langchain-ai/langgraph
- **GitHub repo:** https://github.com/langchain-ai/langgraph @ 3c916d7 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02); LangSmith Plus $39 per seat a month (langchain.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @3c916d7, a review, 2026-11-02): safe. The langgraph CLI sends usage analytics unless LANGGRAPH_CLI_NO_ANALYTICS=1 (`libs/cli/langgraph_cli/analytics.py:89`); the library itself has none. LangSmith tracing only when you set its env vars.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: `pip install -U langgraph` (README); set LANGGRAPH_CLI_NO_ANALYTICS=1 if you use the CLI. Android: no.
