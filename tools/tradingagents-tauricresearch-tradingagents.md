# TradingAgents (TauricResearch/TradingAgents)

- **Type:** library
- **Category:** finance, research
- **Official URL:** https://github.com/TauricResearch/TradingAgents
- **GitHub repo:** https://github.com/TauricResearch/TradingAgents @ c454491 (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); LLM and data APIs cost extra
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @c454491, a review, 2026-11-02): safe. Research only, not advice (`README.md:78`). API keys come from env vars and are masked in errors (`alpha_vantage/common.py:28-35,114`). No order execution found. Needs LLM and data API keys.

## Safe install

Safe install (fixes applied):
Windows (Python 3.11+, pyproject.toml): in a venv `pip install tradingagents-0.7.1-py3-none-any.whl` downloaded from the official GitHub release v0.7.1 (2026-10-27; not on PyPI). Verified: once a day the CLI asks api.github.com for the latest release and api.tauric.ai for notices (cli/updates.py:2-8,30-31 at v0.7.1). Fix: set TRADINGAGENTS_NO_UPDATE_CHECK=1 (cli/updates.py:36). Keys: put your own LLM/data API keys in env vars or .env only (masked in errors, alpha_vantage/common.py:28-35,114). It does not place trades (no order execution found); research only, not advice (README.md:78). Unverified: v0.7.1 beyond updates.py (review read c454491) -> contain: venv, spending-capped API keys. Claude Code: can run it. claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the update-check opt-out and the capped keys.
git clone the repo, pip install ., add keys to .env and run it.

## Install notes

Safe, but ask the user before installing.
Windows: Python in a venv with your own API keys in env vars, per its README (not tested). Android: no.
