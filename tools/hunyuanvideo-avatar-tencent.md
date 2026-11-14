# HunyuanVideo-Avatar (Tencent)

- **Type:** library
- **Category:** generating videos
- **Official URL:** https://github.com/Tencent-Hunyuan/HunyuanVideo-Avatar
- **GitHub repo:** https://github.com/Tencent-Hunyuan/HunyuanVideo-Avatar @ 8c31d0d (2025-12-16, Tencent Hunyuan Community License)
- **Price:** Free model under the Tencent Hunyuan Community License (not open source; not valid in the EU, UK or South Korea); needs a 24 GB+ NVIDIA GPU or paid rented GPU time (github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @8c31d0d, a review, 2026-11-01): Use with caution. os.system ffmpeg commands from file paths (`hymm_sp/sample_gpu_poor.py:99`); Gradio demo opens a public share link on 0.0.0.0, API server on 0.0.0.0:80 with no auth (`hymm_gradio/flask_audio.py:33`); torch.load without weights_only; committed .pyc files; Docker runs --privileged. Licence: not valid in EU/UK/South Korea; output must be labelled AI-generated.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: no official Windows setup; the README guide is Linux only (`README.md:103`) and needs an NVIDIA GPU with at least 24 GB VRAM (`README.md:89`).
Claude Code (local only): Linux GPU machine only, per the README.
