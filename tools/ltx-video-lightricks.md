# LTX-Video (Lightricks)

- **Type:** library
- **Category:** generating videos
- **Official URL:** https://github.com/Lightricks/LTX-Video
- **GitHub repo:** https://github.com/Lightricks/LTX-Video @ 50f0aef (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @50f0aef, a review, 2026-11-02): caution. The optional prompt enhancer loads a third-party Hugging Face model with trust_remote_code=True (`ltx_video/inference.py:253-256`; model in `configs/ltxv-2b-0.9.8-distilled-fp8.yaml:12`), which runs that model's own Python code: leave enhance_prompt off.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `python -m pip install -e .[inference]` in a clone (README), NVIDIA GPU; keep enhance_prompt off. Android: no.
