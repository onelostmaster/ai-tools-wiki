# Bark (Suno)

- **Type:** library
- **Category:** voice and audio
- **Official URL:** https://github.com/suno-ai/bark
- **GitHub repo:** https://github.com/suno-ai/bark @ f4f32d4 (MIT; last push 2024-08-19)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @f4f32d4 (2026-11-16): caution. Weights come from Suno's Hugging Face repo (bark/generation.py:151), unchanged since 2023-10-04 (revision 70a8a7d), and load with torch.load without weights_only (line 212). No fix: the repo is unmaintained since 2024, so nobody patches it. Use the Chatterbox or Kokoro rows. pip install bark is a different package (README.md:169).

## Safe install

Safe install (fixes applied):
Use the Chatterbox or Kokoro rows instead. If you must: own venv, pip install git+https://github.com/suno-ai/bark.git@f4f32d4 (never pip install bark), torch 2.6+ so torch.load defaults to weights_only.

## YOLO install

YOLO (your own risk): skips the pin and the venv.
pip install git+https://github.com/suno-ai/bark.git.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: Python; `pip install git+https://github.com/suno-ai/bark.git` (README.md:171), never `pip install bark`. Prefer the maintained Chatterbox or Kokoro rows.
