# Chatterbox (Resemble AI)

- **Type:** library
- **Category:** voice and audio, a project, 3D and games
- **Official URL:** https://github.com/resemble-ai/chatterbox
- **GitHub repo:** https://github.com/resemble-ai/chatterbox @ 5de7a54 (MIT; pushed 2026-07-21)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @5de7a54, sweep 2026-11-02): caution. Weights from official ResembleAI Hugging Face repos (`tts_turbo.py:26,208`); Turbo loads with weights_only=True (`:107`) but `vc.py:50` calls torch.load without it. Every output has an inaudible Perth watermark (`tts_turbo.py:319`). Pins torch 2.6.0 and transformers 5.2.0 (`pyproject.toml:18,22`): use its own venv. Clone only voices you may use.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: Python (CUDA or CPU) in its own venv: `pip install chatterbox-tts` (README.md:52).
