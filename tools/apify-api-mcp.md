# Apify (API + MCP)

- **Type:** MCP
- **Category:** research, scraping
- **Official URL:** https://apify.com
- **GitHub repo:** [https://github.com/apify/apify-mcp-server](https://github.com/apify/apify-mcp-server)
- **Price:** Free plan with $5/mo prepaid usage; Starter $19/mo; Instagram Scraper $2.70 per 1,000 results on Free, $2.30 on Starter (`apify.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (code read of the MCP server, a review, d819bf8): Use with caution. Segment telemetry + Sentry on by default (opt out `?telemetry-enabled=false` or `TELEMETRY_ENABLED=false`); search sends a model-written use-case to Apify; Actors are third-party code with their own pricing; scraped comments are untrusted text (injection risk); scraping breaks IG/TikTok terms.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

No install steps: the source withholds them until the tool is rated safe. Read the Safety reason and ask the user first.
Apify API (already in use in a project): nothing to install; keep the Apify token in secrets/env vars and never paste it into chat
Tip (2026-11-01, from a project): price an actor's media add-on per item before running it (a project reports the Instagram reel scraper's video add-on at USD 0.02 per MB), and test with real links, not the actor's demo input.
