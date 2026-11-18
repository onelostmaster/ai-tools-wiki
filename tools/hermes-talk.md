# hermes-talk

- **Type:** plugin
- **Category:** Hermes add-ons, voice and audio
- **Official URL:** https://github.com/TheSmokeDev/hermes-talk
- **GitHub repo:** [https://github.com/TheSmokeDev/hermes-talk](https://github.com/TheSmokeDev/hermes-talk)
- **Price:** Free code; OpenAI/Grok/Gemini realtime API usage (not verified)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, a project a review): Looks safe. Network only to OpenAI, `x.ai`, Google and ElevenLabs plus 127.0.0.1. Note: it can reuse your Codex ChatGPT login from `~/.codex/auth.json` on an undocumented `chatgpt.com` realtime endpoint.

## Safe install

Safe install (fixes applied):
Hermes: hermes plugins install --ref 7ad833e4fcedb2c9a9947d84d7fd89bdbd15d256 TheSmokeDev/hermes-talk --enable (README:41; pinned to the reviewed commit). Realtime API keys go in Hermes secrets or env vars, never in chat. It can reuse a Codex ChatGPT login from ~/.codex/auth.json on an undocumented chatgpt.com endpoint ; unverified: when it picks that route over your API key, so run it under a Windows user or Hermes profile with no Codex login.

## YOLO install

YOLO (your own risk): skips the commit pin.
hermes plugins install TheSmokeDev/hermes-talk --enable (follows main).

## Install notes

Hermes: `hermes plugins install --ref 7ad833e4fcedb2c9a9947d84d7fd89bdbd15d256 TheSmokeDev/hermes-talk --enable` (README:41). Realtime API keys go in secrets/env vars, never in chat.
