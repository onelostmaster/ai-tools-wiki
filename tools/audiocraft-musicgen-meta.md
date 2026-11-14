# AudioCraft / MusicGen (Meta)

- **Type:** library
- **Category:** voice and audio, 3D and games
- **Official URL:** https://github.com/facebookresearch/audiocraft
- **GitHub repo:** https://github.com/facebookresearch/audiocraft @ 896ec7c (code MIT; weights CC-BY-NC 4.0; last push 2026-03-03)
- **Price:** Free (code MIT, weights CC-BY-NC 4.0; github.com, checked 2026-11-02); runs on your own GPU
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light read of README/LICENSE/setup @896ec7c, a review, 2026-11-02): safe, official Meta repo; code not reviewed line by line. Weights are CC-BY-NC 4.0 (`README.md:76`, `LICENSE_weights:1`): no use in a paid game or monetized channel. Downloads model weights on first use.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: Python with an NVIDIA GPU; follow the README (`python -m pip install setuptools wheel`, then the audiocraft package; ffmpeg via `conda install "ffmpeg<5" -c conda-forge`). Non-commercial weights only.
