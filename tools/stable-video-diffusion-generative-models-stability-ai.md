# Stable Video Diffusion / generative-models (Stability AI)

- **Type:** library
- **Category:** generating videos
- **Official URL:** https://github.com/Stability-AI/generative-models
- **GitHub repo:** https://github.com/Stability-AI/generative-models @ e8cd657 (MIT code; weights under the Stability community licence; last commit 2025-12-16)
- **Price:** Free code (MIT); weights under the Stability AI community licence (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (code read @e8cd657, a review, 2026-11-02): caution. Runs eval() on config strings (sgm/util.py:25) and loads checkpoints with torch.load (sgm/util.py:205): use only official weights. Research repo, no commit since 2025-12. Weights carry Stability's community licence (check before commercial use). Fix-rule re-rate 2026-11-18: every verified risk has its exact fix in Safe install (only official Stability AI checkpoints and the repo's own configs loaded, so eval() and torch.load see no third-party input, pinned e8cd657); with those fixes applied: safe.

## Safe install

Safe install (fixes applied):
Windows (no official Windows steps; Python + NVIDIA GPU per its README): git clone https://github.com/Stability-AI/generative-models, git checkout e8cd657, install in a venv. Load only the official Stability AI checkpoints and the repo's own config files: it runs eval() on config strings (sgm/util.py:25) and loads checkpoints with torch.load (sgm/util.py:205), so a third-party config or checkpoint runs code on your PC. Check the Stability community licence before any commercial use of output. Research repo, no commit since 2025-12. Android: no.

## YOLO install

YOLO (your own risk): skips the official-weights-and-configs-only rule.
Windows: clone, install and load any checkpoint or config you find; a malicious one runs code on your PC.

## Install notes

Ask the user before installing. Safe only with the fixes in Safe install applied.
Windows: no official Windows steps; Python + NVIDIA GPU per its README (not tested). Android: no.
