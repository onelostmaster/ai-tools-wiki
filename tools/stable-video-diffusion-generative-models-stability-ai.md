# Stable Video Diffusion / generative-models (Stability AI)

- **Type:** library
- **Category:** generating videos
- **Official URL:** https://github.com/Stability-AI/generative-models
- **GitHub repo:** https://github.com/Stability-AI/generative-models @ e8cd657 (MIT code; weights under the Stability community licence; last commit 2025-12-16)
- **Price:** Free code (MIT); weights under the Stability AI community licence (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @e8cd657, a review, 2026-11-02): caution. Runs eval() on config strings (`sgm/util.py:25`) and loads checkpoints with torch.load (`sgm/util.py:205`): use only official weights. Research repo, no commit since 2025-12. Weights carry Stability's community licence (check before commercial use).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: no official Windows steps; Python + NVIDIA GPU per its README (not tested). Android: no.
