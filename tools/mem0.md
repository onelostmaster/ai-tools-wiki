# Mem0

- **Type:** plugin
- **Category:** Notion and productivity, Hermes add-ons
- **Official URL:** https://mem0.ai
- **GitHub repo:** [https://github.com/mem0ai/mem0](https://github.com/mem0ai/mem0)
- **Price:** SDK free (Apache-2.0). The Claude Code plugin needs a Mem0 Platform key. Free plan: 10,000 adds and 1,000 retrievals a month for the first 30 days (model calls on Mem0), or 50,000 adds and 10,000 retrievals a month with your own LLM key; usage-based billing past those limits, with a monthly cap you set. Custom plans by contract (`mem0.ai`, checked 2026-10-31). Hermes OSS mode is free with your own LLM and vector store.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read, a review / Hermes a review, 753496c, 2026-10-31): Use with caution. The Claude Code plugin uploads your session memories to Mem0 Cloud (`api.mem0.ai`) and needs a Mem0 Platform API key; hooks on SessionStart, every prompt and every tool call; PostHog telemetry on by default in the plugin and the SDK (opt out `MEM0_TELEMETRY=false`). Recalled memories are injected as context (poisoning risk).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: a review bot gave no steps (not Looks safe). The plugin needs a Mem0 Platform API key: add it as a secret/env var, never paste it into chat.
Hermes: if you try it, OSS/self-hosted mode keeps data local: `hermes plugins install mem0`, then `hermes memory setup`, and set `MEM0_TELEMETRY=false` in `~/.hermes/.env`.
