# VoiceStudio

- **Type:** app
- **Category:** voice and audio
- **Official URL:** https://github.com/debpalash/VoiceStudio
- **GitHub repo:** [https://github.com/debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)
- **Price:** Free (AGPL)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Claude code read @8f6c113 v0.5.9-beta.6 (2026-11-18): safe with fixes. API binds 127.0.0.1 (backend/main.py:2483,2515). MOSS-TTS v1.5 loads remote code at pinned revisions (backend/engines/moss_tts_v15/main.py:57-59); MOSS-TTS-Nano loads it from main unpinned (backend/services/tts_backend.py:2521-2523). Analytics are opt-in. Fix: run from source, skip curl|sh and the Nano engine.

## Safe install

Safe install (fixes applied):
Clone at 8f6c113 and run from source per README.md:334 (or build the repo's Docker image yourself); never curl … | sh; don't install moss_tts_nano; leave analytics off.

## YOLO install

YOLO (your own risk): skips source builds and the Nano rule.
curl -fsSL https://voicestudio.sh/install | sh with every engine.

## Install notes

Ask the user before installing. Clone at 8f6c113 and run from source per README.md:334 (or build the repo's Docker image yourself); never curl … | sh; don't install moss_tts_nano; leave analytics off.
