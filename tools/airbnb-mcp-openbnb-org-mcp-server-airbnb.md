# Airbnb MCP (openbnb-org/mcp-server-airbnb)

- **Type:** MCP
- **Category:** scraping, research
- **Official URL:** https://github.com/openbnb-org/mcp-server-airbnb
- **GitHub repo:** https://github.com/openbnb-org/mcp-server-airbnb @ d5a8f18 (MIT; unofficial, not Airbnb)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @d5a8f18, a review / Hermes a review, 2026-11-02): caution. Unofficial scraper of Airbnb search and listing pages (`index.ts:189`); checks robots.txt but has an --ignore-robots-txt switch (`index.ts:298`); scraping may break Airbnb's terms.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: build from source (`npm install`, `npm run build`, README) and never use --ignore-robots-txt. Hermes: same over MCP. Android: no.
