# ElevenLabs (API, app)

- **Type:** API
- **Category:** voice and audio, a project
- **Official URL:** https://elevenlabs.io
- **GitHub repo:** unknown
- **Price:** Free tier; Starter $6/mo; Creator $22/mo; Pro $99/mo (elevenlabs.io/pricing, checked 2026-10-31)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Claude, a project scout (integration check, 2026-10-31): safe. Official vendor API with no repo to read (a review bot a review); the key is injected by a proxy and never put in the page; text and audio are sent to `api.elevenlabs.io`.

## Safe install

Safe install (fixes applied):
Claude Code (Windows or cloud projects): nothing to install; call api.elevenlabs.io from project code with the key in an environment variable, a project secret or the injecting proxy, never pasted into chat or a page. Hermes: built-in TTS provider; put the key in Hermes secrets. Android: the official ElevenLabs app from Google Play. claude. Every request sends your text or audio to ElevenLabs and spends plan credits (elevenlabs.io/pricing).

## YOLO install

Not written yet.

## Install notes

Claude Code: no install needed; call `api.elevenlabs.io` from project code with the key in an env var/secret or an injecting proxy, never pasted into chat.
Hermes: built in as a TTS provider; keep the key in Hermes secrets.
Android: the official ElevenLabs app from Google Play (per ElevenLabs' help center).
claude.
Tip (2026-11-01, from a project): Scribe speech-to-text works in Claude cloud projects, where Hugging Face models (faster-whisper, earshot's model commands) are blocked.
