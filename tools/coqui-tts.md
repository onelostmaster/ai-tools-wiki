# Coqui TTS

- **Type:** library
- **Category:** voice and audio, a project
- **Official URL:** https://github.com/coqui-ai/TTS
- **GitHub repo:** https://github.com/coqui-ai/TTS @ dbf1a08 (MPL-2.0; last push 2024-08-16)
- **Price:** Free, MPL-2.0 (github.com, checked 2026-11-02)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @dbf1a08 (2026-11-16): caution. Model downloads go through the coqui.gateway.scarf.sh tracking gateway (TTS/.models.json:8); XTTS needs a CPML non-commercial acceptance (TTS/utils/manage.py:312-315); checkpoints load with torch.load and no weights_only (TTS/utils/io.py:51). No fix: unmaintained since 2024-02, so nobody patches it. Use the Chatterbox or Kokoro rows.

## Safe install

Safe install (fixes applied):
Use the Chatterbox or Kokoro rows instead. If you must: own venv, pip install TTS==0.22.0, torch 2.6+ so torch.load defaults to weights_only; non-commercial use only for XTTS.

## YOLO install

YOLO (your own risk): skips the venv and pin.
pip install TTS.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: Python; `pip install TTS` (README.md:152). Prefer the maintained Chatterbox or Kokoro rows.
