# Firecrawl (API + MCP)

- **Type:** API
- **Category:** scraping, research
- **Official URL:** https://www.firecrawl.dev
- **GitHub repo:** https://github.com/firecrawl/firecrawl (AGPL-3.0, official org, not a fork) + https://github.com/firecrawl/firecrawl-mcp-server @ aa409c9 (MIT)
- **Price:** Free 1,000 credits/month; Hobby $19/month ($16 billed yearly) for 5,000 credits; Standard $99/month ($83 billed yearly) for 100,000 credits; Growth $399/month ($333 billed yearly) for 500,000 credits; paid plans add pay-as-you-go credits in $5 steps up to a monthly cap you set (firecrawl.dev/pricing, checked 2026-11-12)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Firecrawl (official vendor; not code-reviewed: a review bot listed it under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. Hosted scraping: the pages you fetch go through Firecrawl's servers and are billed in credits to your team; connect by browser sign-in or an API key (Firecrawl docs). a review bot noted it overlaps Apify. a review bot (light read of firecrawl-mcp-server @aa409c9, a review, 2026-11-02): the MCP only adds Alexandria as a search source through Firecrawl's own API (`src/alexandria.ts:1-40`, `src/server.ts:625`); only telemetry is a low-cardinality auth log line (`src/service/auth.ts:625-650`); no shell, eval or hooks seen. Caution for the new Alexandria People category: it returns work emails and personal data about real people (12 providers incl. Apollo and People Data Labs), so privacy and anti-spam laws apply.

## Safe install

Safe install (fixes applied):
claude.ai (Windows browser and Android app): add the native Firecrawl connector from Claude's connector list (Firecrawl docs). Claude Code (Windows): `claude mcp add --transport http firecrawl https://mcp.firecrawl.dev/v2/mcp-oauth` and sign in in the browser, so no API key is stored (docs.firecrawl.dev/mcp-server). Leave Alexandria People off unless you ask for it (shared key policy); use zero-data-retention mode to turn Alexandria off entirely. Set a monthly cap on pay-as-you-go credits in the Firecrawl dashboard (firecrawl.dev/pricing).

## YOLO install

Not written yet.

## Install notes

claude.ai: install the native Firecrawl connector in Claude (Firecrawl docs).
Claude Code: add the remote HTTP server `https://mcp.firecrawl.dev/v2/mcp-oauth` and sign in in the browser, no key needed (official docs at https://docs.firecrawl.dev/mcp-server); with an API key use `https://mcp.firecrawl.dev/v2/mcp` instead, and never paste the key into chat, add it as a secret/env var.
Alexandria People (https://www.firecrawl.dev/alexandria/categories/people): contact and company enrichment through the same Firecrawl key and credits; zero-data-retention and anonymous modes turn Alexandria off. Ask the user before using personal contact data.
Shared key policy (user, 2026-11-05): one Firecrawl key for every project and bot (about 1,000 free credits/month). Use TinyFish search and page fetch first; Firecrawl only when TinyFish fails (for example bot-blocked Fandom wikis). Never use Firecrawl for X posts (about 30 credits each) or Instagram (unsupported). Alexandria People contact enrichment stays off unless the user asks.
