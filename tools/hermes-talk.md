# hermes-talk

- **Type:** plugin
- **Category:** Hermes add-ons, voice and audio
- **Official URL:** https://github.com/TheSmokeDev/hermes-talk
- **GitHub repo:** [https://github.com/TheSmokeDev/hermes-talk](https://github.com/TheSmokeDev/hermes-talk)
- **Price:** Free code; OpenAI/Grok/Gemini realtime API usage (not verified)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a project a review): Looks safe. Network only to OpenAI, `x.ai`, Google and ElevenLabs plus 127.0.0.1. Note: it can reuse your Codex ChatGPT login from `~/.codex/auth.json` on an undocumented `chatgpt.com` realtime endpoint.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Hermes: `hermes plugins install --ref 7ad833e4fcedb2c9a9947d84d7fd89bdbd15d256 TheSmokeDev/hermes-talk --enable` (README:41). Realtime API keys go in secrets/env vars, never in chat.
