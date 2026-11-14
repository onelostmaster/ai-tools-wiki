# OpenSEO

- **Type:** plugin
- **Category:** research, building a site
- **Official URL:** https://www.openseo.so
- **GitHub repo:** [https://github.com/every-app/open-seo](https://github.com/every-app/open-seo)
- **Price:** Hosted: free trial with $0.50 credit; Base $10/mo (includes $10 usage), Pro $30/mo, Agency $200/mo; data at DataForSEO price +28% (openseo.so, checked 2026-11-02). Self-host: app free, your own DataForSEO account ($1 free credit, $50 minimum top-up; dataforseo.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (scanned for telemetry, installers, updaters and keys, not fully read; a project a review, 1523750): Looks safe. The Claude plugin is 12 text-only skills plus a hosted MCP at `app.openseo.so/mcp` with OAuth; the hosted plan adds a 28% fee on DataForSEO data; self-hosting sends an anonymized telemetry heartbeat unless `OPENSEO_TELEMETRY_DISABLED=1`.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `/plugin marketplace add every-app/open-seo` then `/plugin install openseo@openseo` (a review bot, a review); the hosted MCP signs in with OAuth.
Hermes: unconfirmed (a review bot): add an http MCP server for `https://app.openseo.so/mcp`.
Self-hosting: bring your own DataForSEO key as a secret/env var, never in chat; set `OPENSEO_TELEMETRY_DISABLED=1` to stop the heartbeat.
