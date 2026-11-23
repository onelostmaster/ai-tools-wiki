# Scrapling

- **Type:** library
- **Category:** scraping
- **Official URL:** https://scrapling.readthedocs.io/en/latest/
- **GitHub repo:** https://github.com/D4Vinci/Scrapling @ 2998c9e (BSD-3-Clause; v0.5.1; commit 2026-11-17)
- **Price:** Free (BSD-3-Clause, `github.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-22

## Safety reason

a review bot read @2998c9e: safe with these fixes. Verified 1: scrapling install runs python -m playwright install chromium and then playwright install-deps chromium (cli.py:120-140), which installs system packages on Linux/WSL. Fix: skip scrapling install; run python -m playwright install chromium yourself inside the venv. Verified 2: the MCP server's browser_save_state and browser_load_state write and read cookie/local-storage JSON files at any path relative to the server's working folder, overwriting existing files (core/ai/server.py:357-382). Fix: start scrapling-mcp from an empty work folder and load no state file that holds your real logins. Verified 3: browser_open takes a cdp_url and attaches to an already running browser (core/ai/server.py:303-343), and --real-chrome launches your installed Chrome instead of Playwright Chromium (engines/_browsers/_base.py:550). Fix: never pass cdp_url, never start your own Chrome with remote debugging, leave real_chrome off. Verified 4: the MCP server is stdio by default and --http refuses to start without an auth token unless you add --no-auth (cli.py:143-196). Fix: stdio only, never --no-auth. Verified 5: browser_evaluate runs any JavaScript the AI sends on the open page (core/ai/server.py:591-611). Fix: the empty-profile browser from fix 3 keeps that away from your accounts. Verified 6: stealth fetchers offer solve_cloudflare (core/ai/server.py:858) to get past anti-bot checks. Fix: leave it off and scrape only sites whose terms allow it. Verified 7: dependencies use >= ranges (pyproject.toml:63-90), so versions float. Fix: pin scrapling==0.5.1 and pip freeze to a requirements file after the first install. No telemetry found: the only subprocess use is the install command (cli.py:3); the 'analytics' hits are its ad-block list (engines/toolbelt/ad_domains.py).

## Safe install

Safe install (fixes applied):
Claude Code on Windows (PowerShell): mkdir C:\\scrapling-work ; cd C:\\scrapling-work ; py -m venv .venv ; .venv\\Scripts\\pip install "scrapling[ai]==0.5.1" ; .venv\\Scripts\\pip freeze > requirements.lock ; .venv\\Scripts\\python -m playwright install chromium (do not run scrapling install). Add the MCP in stdio mode from that folder: claude mcp add scrapling -- C:\\scrapling-work\.venv\\Scripts\\scrapling-mcp.exe . Never use --http --no-auth, cdp_url or real_chrome; load no saved login state; keep solve_cloudflare off; scrape only sites whose terms allow it.
claude.ai, Hermes, Android: not supported (local Python library and stdio MCP; Hermes compatibility untested).

## YOLO install

YOLO (your own risk): skips the pin, the lockfile and the manual browser step. pip install "scrapling[all]" then scrapling install --force (agent-skill SKILL.md:43-48), which also runs playwright install-deps (system packages on Linux/WSL).

## Install notes

Safe with fixes: Python scraping framework (HTTP fetcher, stealth browsers, crawler, CLI, stdio MCP server, agent skill) with no telemetry. Pin 0.5.1 in a venv, install Chromium with playwright yourself instead of scrapling install, run the MCP over stdio from an empty folder, never attach it to your own Chrome (no cdp_url, no real_chrome) or load your real login state, keep solve_cloudflare off and scrape only sites whose terms allow it.
