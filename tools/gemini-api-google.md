# Gemini API (Google)

- **Type:** API
- **Category:** developer tools
- **Official URL:** https://ai.google.dev/gemini-api/docs
- **GitHub repo:** unknown
- **Price:** Free tier on some models (content used to improve Google's products); paid tier per 1M tokens, e.g. Gemini 4 Argon $2 input / $10 output through 2026-11-30, then $4 / $20 (`ai.google.dev`, checked 2026-10-31)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-13

## Safety reason

Gemini (official vendor, Google; not code-reviewed: a review bot listed it under 'not audited', a project a review, 2026-10-31): safe. Google's pricing page: free-tier content is used to improve Google's products; paid-tier content is not. Vetted tools upload to it: earshot's optional critique (off unless `GEMINI_API_KEY` is set; over MCP the agent passes consent itself, a review) and hermes-whatsapp-voice (call audio and memory briefing, a review).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `pip install google-genai` (Python SDK, PyPI); never paste the Gemini API key into chat, add it as a secret/env var.
Hermes: used through plugins such as hermes-whatsapp-voice and hermes-talk (see their rows); they need your own Gemini key as a secret.
