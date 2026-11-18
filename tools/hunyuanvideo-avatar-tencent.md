# HunyuanVideo-Avatar (Tencent)

- **Type:** library
- **Category:** generating videos
- **Official URL:** https://github.com/Tencent-Hunyuan/HunyuanVideo-Avatar
- **GitHub repo:** https://github.com/Tencent-Hunyuan/HunyuanVideo-Avatar @ 8c31d0d (2025-12-16, Tencent Hunyuan Community License)
- **Price:** Free model under the Tencent Hunyuan Community License (not open source; not valid in the EU, UK or South Korea); needs a 24 GB+ NVIDIA GPU or paid rented GPU time (github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @8c31d0d (2026-11-17): safe with fixes. Gradio demo opens a public share link (hymm_gradio/gradio_audio.py:90); the API server takes 0.0.0.0:80 with no auth (flask_audio.py:265). torch.load without weights_only (hymm_sp/inference.py:144). ffmpeg runs via os.system on your file paths (sample_gpu_poor.py:99). Fix: CLI scripts only, torch 2.6+. Licence excludes EU, UK, South Korea (LICENSE:3).

## Safe install

Safe install (fixes applied):
Linux, NVIDIA 24 GB+; clone at 8c31d0d, own venv with torch 2.6+; delete hymm_sp/**/__pycache__; run scripts/run_single_poor.sh only (never run_gradio.sh or flask_audio.py); plain file names; Docker without --privileged or --net=host; label output AI-generated.

## YOLO install

YOLO (your own risk): skips CLI-only, torch 2.6 and the Docker trims.
Run the Gradio demo with its public link and the README's --privileged container.

## Install notes

Ask the user before installing.
Windows: no official Windows setup; the README guide is Linux only (`README.md:103`) and needs an NVIDIA GPU with at least 24 GB VRAM (`README.md:89`).
Claude Code (local only): Linux GPU machine only, per the README.
