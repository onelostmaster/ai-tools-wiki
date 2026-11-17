# LeRobot (Hugging Face)

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://huggingface.co/docs/lerobot
- **GitHub repo:** https://github.com/huggingface/lerobot @ f5c9bc0 (Apache-2.0; pushed 2026-11-02)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); robot arm kits sold separately (not priced)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light read of README/LICENSE @f5c9bc0, a review, 2026-11-02): safe, official Hugging Face repo, maintained; code not reviewed line by line. Downloads datasets and models from Hugging Face; hardware plugins are separate packages.

## Safe install

Safe install (fixes applied):
Windows or Hermes: in a fresh venv with Python 3.12+ (PyPI requires_python), pip install lerobot==0.7.0 (version pinned, PyPI latest on 2026-11-16; README.md:33), adding only the extras you need, e.g. "lerobot[dataset]" (README.md:37). It downloads datasets and models from Hugging Face; use a read-only HF token only if a gated dataset needs one. Install robot plugins (lerobot_robot_<name>) only from the official Hugging Face org (README.md:141). Reviewed commit f5c9bc0; HEAD is 781d3da (2026-11-16), not reviewed. claude.ai, Android: no.

## YOLO install

YOLO (your own risk): skips the venv, the version pin and the extras limit.
pip install lerobot (README.md:33)

## Install notes

Safe, but ask the user before installing.
Any platform: `pip install lerobot` (README.md:33); Linux first.
