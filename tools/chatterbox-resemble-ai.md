# Chatterbox (Resemble AI)

- **Type:** library
- **Category:** voice and audio, a project, 3D and games
- **Official URL:** https://github.com/resemble-ai/chatterbox
- **GitHub repo:** https://github.com/resemble-ai/chatterbox @ 5de7a54 (MIT; pushed 2026-07-21)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @ab55923 = 0.1.7 (2026-11-16): safe with fixes. Weights come from official ResembleAI Hugging Face repos. All loads pass weights_only=True except src/chatterbox/vc.py:50, and the pinned torch 2.6.0 (pyproject.toml:18) defaults torch.load to weights_only, which covers it. Every output carries an inaudible Perth watermark (tts_turbo.py:319). Fix: own venv; clone only voices you have rights to.

## Safe install

Safe install (fixes applied):
Own venv, Python 3.10–3.13: pip install chatterbox-tts==0.1.7 (keeps torch 2.6.0); clone only voices you have the rights to.

## YOLO install

YOLO (your own risk): skips the venv and version pin.
pip install chatterbox-tts into your main Python.

## Install notes

Ask the user before installing.
Windows: Python (CUDA or CPU) in its own venv: `pip install chatterbox-tts` (README.md:52).
