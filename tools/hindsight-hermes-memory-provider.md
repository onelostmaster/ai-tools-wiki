# Hindsight (Hermes memory provider)

- **Type:** plugin
- **Category:** Hermes add-ons, Notion and productivity
- **Official URL:** https://hindsight.vectorize.io/sdks/integrations/hermes
- **GitHub repo:** [https://github.com/vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)
- **Price:** Hermes plugin free (MIT); local mode free with your own LLM key. Hindsight Cloud (the setup default) is pay-as-you-go credits, e.g. Retain $10 and Recall $0.75 per million tokens, Reflect $0.05 per call (`docs.hindsight.vectorize.io`, checked 2026-10-31).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @5318be8 (2026-11-15): safe with fixes. The plugin's mode defaults to cloud (hindsight-integrations/hermes/config_schema.py:21), which stores turns at Hindsight Cloud. Setup offers starter templates from the unpinned main branch (templates.py:21), and the step skips on a blank answer (templates.py:93-95). Fix: Local Embedded mode, skip the template. Recalled memories re-enter context, so use it on a trusted profile.

## Safe install

Safe install (fixes applied):
In hermes memory setup choose Local Embedded and leave the starter template blank; your own LLM key in Hermes secrets; use it on one trusted profile, not a web-reading bot.

## YOLO install

YOLO (your own risk): skips local mode and the template skip, so every retained turn goes to Hindsight Cloud.
Accept the setup defaults.

## Install notes

Ask the user before installing. In hermes memory setup choose Local Embedded and leave the starter template blank; your own LLM key in Hermes secrets; use it on one trusted profile, not a web-reading bot.
