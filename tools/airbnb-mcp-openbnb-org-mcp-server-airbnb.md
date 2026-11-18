# Airbnb MCP (openbnb-org/mcp-server-airbnb)

- **Type:** MCP
- **Category:** scraping, research
- **Official URL:** https://github.com/openbnb-org/mcp-server-airbnb
- **GitHub repo:** https://github.com/openbnb-org/mcp-server-airbnb @ d5a8f18 (MIT; unofficial, not Airbnb)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Avoid
- **Safety verdict:** avoid
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @d5a8f18 v0.3.0 (2026-11-17): avoid. It scrapes Airbnb search and listing pages with a Chrome user agent (index.ts:149,324,375). Airbnb Terms of Service 11.1 (5 Feb 2026): "Do not use bots, crawlers, scrapers, or other automated means to access or collect data". The agent can also skip robots.txt per call (index.ts:91,478). No fix: the terms forbid the tool's whole purpose.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not offered.

## Install notes

Do not install: flagged avoid (see Safety reason).
