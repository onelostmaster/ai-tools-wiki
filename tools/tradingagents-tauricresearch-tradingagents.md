# TradingAgents (TauricResearch/TradingAgents)

- **Type:** library
- **Category:** finance, research
- **Official URL:** https://github.com/TauricResearch/TradingAgents
- **GitHub repo:** https://github.com/TauricResearch/TradingAgents @ c454491 (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); LLM and data APIs cost extra
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @c454491, a review, 2026-11-02): safe. Research only, not advice (`README.md:78`). API keys come from env vars and are masked in errors (`alpha_vantage/common.py:28-35,114`). No order execution found. Needs LLM and data API keys.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: Python in a venv with your own API keys in env vars, per its README (not tested). Android: no.
