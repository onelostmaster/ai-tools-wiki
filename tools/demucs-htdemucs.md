# Demucs (htdemucs)

- **Type:** library
- **Category:** voice and audio, video analysis
- **Official URL:** https://pypi.org/project/demucs/
- **GitHub repo:** https://github.com/adefossez/demucs @ 829d218 (2026-10-26, v4.1.0, MIT); homepage listed on PyPI; the original facebookresearch/demucs is archived (GitHub API, checked 2026-11-02), so this fork is the maintained line
- **Price:** Free (MIT)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @829d218, v4.1. Network use is only model download: named models come from the Hugging Face hub under the author's adefossez namespace as safetensors (demucs/hf.py:23, 91-104), falling back to Meta's dl.fbaipublicfiles.com with hash checking (demucs/pretrained.py:19, 60-80; demucs/repo.py:68-69). Subprocesses are only ffmpeg, ffprobe and soundstretch with list arguments, no shell (demucs/audio.py:21, 126, 274; demucs/repitch.py:70-81). No telemetry, eval/exec, hooks or auto-updates. Caveat: legacy .th checkpoints and local training checkpoints are loaded with pickle (torch.load weights_only=False in demucs/repo.py:69, states.py:59, solver.py:107), and safetensors metadata picks the class to import (demucs/hf.py:63-84), so only load models from the official sources.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `pip install demucs` (PyPI)
Models: use only the built-in names (default htdemucs). Don't load hf://<other namespace>/ models, --repo folders or -s checkpoints from untrusted sources: .th checkpoints are unpickled (torch.load weights_only=False) and safetensors metadata names the Python class to import.
