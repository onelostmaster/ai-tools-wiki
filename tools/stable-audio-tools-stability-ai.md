# Stable Audio Tools (Stability AI)

- **Type:** library
- **Category:** voice and audio, 3D and games
- **Official URL:** https://github.com/Stability-AI/stable-audio-tools
- **GitHub repo:** https://github.com/Stability-AI/stable-audio-tools @ 3241adb (MIT; last push 2026-11-01)
- **Price:** Free, MIT code (github.com, checked 2026-11-02); Stable Audio Open weights under Stability's community licence (not re-checked today)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light read of README/LICENSE @3241adb, a review, 2026-11-02): safe, official Stability AI repo, maintained; code not reviewed line by line. Weights download from Hugging Face under Stability's community licence (revenue cap).

## Safe install

Safe install (fixes applied):
Windows (NVIDIA GPU) or Hermes: Python 3.10 (PyPI requires_python >=3.10,<3.11; README.md:6), PyTorch 2.5+. In a fresh folder: pip install uv, git clone https://github.com/Stability-AI/stable-audio-tools.git, git checkout 3241adb (reviewed commit, still HEAD on 2026-11-16), then uv sync (inference only; add --extra ui only for the Gradio UI) (README.md:8-22). Or pip install "stable-audio-tools==0.0.20" in a venv (PyPI latest on 2026-11-16). Model weights download from Hugging Face under Stability's community licence; use a read-only HF token if a gated model asks for one. claude.ai, Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin, the Python 3.10 venv and the inference-only extras.
pip install "stable-audio-tools[train]" (README.md:37)

## Install notes

Safe, but ask the user before installing.
Windows: Python with an NVIDIA GPU; the README uses uv (`pip install uv`, README.md:8), then its documented steps.
