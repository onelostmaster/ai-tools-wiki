# ElevenLabs Python SDK

- **Type:** library
- **Category:** voice and audio
- **Official URL:** https://github.com/elevenlabs/elevenlabs-python
- **GitHub repo:** [https://github.com/elevenlabs/elevenlabs-python](https://github.com/elevenlabs/elevenlabs-python) (listed on PyPI, checked 2026-10-31; not in the source)
- **Price:** Free SDK; ElevenLabs plan separate
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-17

## Safety reason

ElevenLabs (official SDK; PyPI package `elevenlabs` lists the elevenlabs/elevenlabs-python repo, checked 2026-10-31; not code-reviewed): safe. a project rejected it only as redundant.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): pip install elevenlabs inside a project venv, with ELEVENLABS_API_KEY in an env var, never in chat. Official vendor SDK; nothing to fix.

## YOLO install

Not written yet.

## Install notes

Claude Code: `pip install elevenlabs` (PyPI); keep the API key in an env var/secret, never paste it into chat.
