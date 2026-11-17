# MuJoCo (Google DeepMind)

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://mujoco.org
- **GitHub repo:** https://github.com/google-deepmind/mujoco @ aeb871b (Apache-2.0; pushed 2026-11-02)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light read of README/LICENSE @aeb871b, a review, 2026-11-02): safe, official Google DeepMind repo, maintained; code not reviewed line by line.

## Safe install

Safe install (fixes applied):
Windows: Python 3.11+ in a venv, pip install mujoco==4.0.1 (version pinned, PyPI latest on 2026-11-16; pulls mujoco-core 4.0.1, which has win_amd64 wheels). Hermes (Linux): same command. claude.ai, Android: no.

## YOLO install

YOLO (your own risk): skips the venv and the version pin.
pip install mujoco (README.md:93)

## Install notes

Safe, but ask the user before installing.
Windows: x86-64 builds (README.md:78); Python `pip install mujoco` (README.md:93).
