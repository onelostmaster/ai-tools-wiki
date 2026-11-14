# Bark (Suno)

- **Type:** library
- **Category:** voice and audio
- **Official URL:** https://github.com/suno-ai/bark
- **GitHub repo:** https://github.com/suno-ai/bark @ f4f32d4 (MIT; last push 2024-08-19)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light read of README @f4f32d4, a review, 2026-11-02): caution. Official Suno repo but unmaintained (last push 2024-08-19). README warns `pip install bark` is a different, non-Suno package (`README.md:169`); install only from the repo. Downloads model weights on first use. Code not reviewed.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: Python; `pip install git+https://github.com/suno-ai/bark.git` (README.md:171), never `pip install bark`. Prefer the maintained Chatterbox or Kokoro rows.
