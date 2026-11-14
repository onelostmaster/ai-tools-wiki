# Hindsight (Hermes memory provider)

- **Type:** plugin
- **Category:** Hermes add-ons, Notion and productivity
- **Official URL:** https://hindsight.vectorize.io/sdks/integrations/hermes
- **GitHub repo:** [https://github.com/vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)
- **Price:** Hermes plugin free (MIT); local mode free with your own LLM key. Hindsight Cloud (the setup default) is pay-as-you-go credits, e.g. Retain $10 and Recall $0.75 per million tokens, Reflect $0.05 per call (`docs.hindsight.vectorize.io`, checked 2026-10-31).
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, Hermes a review, bc5ea19, 2026-10-31): Use with caution. Setup defaults to Cloud mode, which uploads every retained turn incl. tool calls to `api.hindsight.vectorize.io`; `hermes memory setup` pulls bank templates from the unpinned GitHub main branch and applies them; local-embedded mode can start a daemon via a `uvx hindsight-api` fallback. Retained turns are recalled into context (poisoning risk).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Hermes: a review bot gave no formal steps (not Looks safe); if used, pick Local Embedded in `hermes memory setup` (it takes Hermes's single external memory-provider slot). Local mode needs your own LLM key: add it as a secret/env var, never paste it into chat.
