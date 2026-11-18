# Mem0

- **Type:** plugin
- **Category:** Notion and productivity, Hermes add-ons
- **Official URL:** https://mem0.ai
- **GitHub repo:** [https://github.com/mem0ai/mem0](https://github.com/mem0ai/mem0)
- **Price:** SDK free (Apache-2.0). The Claude Code plugin needs a Mem0 Platform key. Free plan: 10,000 adds and 1,000 retrievals a month for the first 30 days (model calls on Mem0), or 50,000 adds and 10,000 retrievals a month with your own LLM key; usage-based billing past those limits, with a monthly cap you set. Custom plans by contract (`mem0.ai`, checked 2026-10-31). Hermes OSS mode is free with your own LLM and vector store.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @f1791da v2.2.1 (2026-11-17): safe with fixes. The Claude Code plugin needs a Mem0 Platform key and stores memories on api.mem0.ai (integrations/claude-code-plugin/.claude-plugin/plugin.json). PostHog telemetry is on in the library (mem0/memory/telemetry.py:14-16), the server and the plugin (core/telemetry.py:117); MEM0_TELEMETRY=false stops all three. Fix: OSS library with a local store, telemetry off.

## Safe install

Safe install (fixes applied):
Own venv; pip install mem0ai==2.2.1; env MEM0_TELEMETRY=false; local vector store and your own model key in env; Hermes: hermes plugins install mem0 in OSS mode with MEM0_TELEMETRY=false in ~/.hermes/.env; skip the cloud plugin.

## YOLO install

YOLO (your own risk): skips OSS mode and telemetry off.
Install the cloud plugin with a Platform key and leave telemetry on.

## Install notes

Ask the user before installing. Own venv; pip install mem0ai==2.2.1; env MEM0_TELEMETRY=false; local vector store and your own model key in env; Hermes: hermes plugins install mem0 in OSS mode with MEM0_TELEMETRY=false in ~/.hermes/.env; skip the cloud plugin.
