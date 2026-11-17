# Scrapling

- **Type:** library
- **Category:** scraping
- **Official URL:** https://scrapling.readthedocs.io/en/latest/
- **GitHub repo:** https://github.com/D4Vinci/Scrapling @ 26dc85a (BSD-3-Clause; latest commit on 2026-10-31)
- **Price:** Free (BSD-3-Clause, `github.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-16

## Safety reason

Not code-reviewed; the post only names it. README: built to bypass anti-bot checks (Cloudflare Turnstile solving, fingerprint spoofing), which can break sites' terms; `scrapling install` downloads browsers and fingerprint tools; the MCP server can keep saved login state; README carries paid proxy and CAPTCHA-solver ads.

## Safe install

Safe install (fixes applied):
Unreviewed: contain it: install it in a venv inside a devcontainer or WSL2 folder pinned to scrapling==0.5.1 (latest on PyPI 2026-11-16) or the row's commit 26dc85a, use the plain HTTP fetcher first, run scrapling install (browser downloads) only inside that container, give it no saved logins, proxies or CAPTCHA-solver keys, and scrape only sites whose terms allow it. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code (local only): `pip install scrapling` (Python 3.10+); browser fetchers need `pip install "scrapling[fetchers]"` then `scrapling install`; the MCP server needs `pip install "scrapling[ai]"` (README).
