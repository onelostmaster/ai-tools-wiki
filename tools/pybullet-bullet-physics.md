# PyBullet (Bullet Physics)

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** http://bulletphysics.org
- **GitHub repo:** https://github.com/bulletphysics/bullet3 @ d3afe76 (zlib, `LICENSE.txt:2`; pushed 2026-10-09)
- **Price:** Free, zlib (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light read of README/LICENSE @d3afe76, a review, 2026-11-02): safe, official Bullet repo, maintained; code not reviewed line by line.

## Safe install

Safe install (fixes applied):
Windows: in a venv, pip install pybullet==3.2.7 (version pinned, PyPI latest on 2026-11-16). PyPI has no Windows wheel for 3.2.7 (Linux wheels plus source only), so on Windows this will compile from source and needs Microsoft C++ Build Tools; use Python 3.10 or 3.11. Hermes (Linux): same command, installs a prebuilt wheel. claude.ai, Android: no.

## YOLO install

YOLO (your own risk): skips the venv and the version pin.
pip install pybullet (README.md:14, 37)

## Install notes

Safe, but ask the user before installing.
Windows: `pip install pybullet` (README.md:14, 37).
