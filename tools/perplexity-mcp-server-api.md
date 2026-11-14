# Perplexity (MCP server + API)

- **Type:** MCP
- **Category:** research
- **Official URL:** https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server
- **GitHub repo:** unknown
- **Price:** Pay as you go at Perplexity API rates, e.g. Search API $5 per 1,000 requests ($1 with Fast Search); model calls billed per token (`docs.perplexity.ai`, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-02

## Safety reason

Perplexity (official vendor MCP server; not code-reviewed: a review bot listed it under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. Perplexity's docs: tool calls are billed to your API key or to the API organization you pick at sign-in; keep keys out of shared or committed config files.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `claude mcp add --transport http perplexity https://api.perplexity.ai/mcp`, then run `/mcp` and sign in (Perplexity docs); never paste a Perplexity API key into chat, add it as a secret/env var.
[claude.ai](http://claude.ai): add `https://api.perplexity.ai/mcp` as a custom connector and sign in with Perplexity (Perplexity docs).
