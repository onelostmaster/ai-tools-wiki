# Essentia (MTG)

- **Type:** library
- **Category:** voice and audio, 3D and games
- **Official URL:** http://essentia.upf.edu
- **GitHub repo:** https://github.com/MTG/essentia @ 33108c7 (AGPL-3.0; last push 2026-10-22)
- **Price:** Free, AGPL-3.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light read of README/LICENSE @33108c7, a review, 2026-11-02): safe, official MTG repo, maintained; code not reviewed line by line. AGPL-3.0: sharing a modified app means sharing its source.

## Safe install

Safe install (fixes applied):
Windows: no Windows pip wheel exists (PyPI 2.1b6.dev1438 has Linux x86_64 and macOS wheels only; README.md:23), so use the official Docker image mtgupf/essentia (README.md:25) or WSL2 Ubuntu with pip install essentia==2.1b6.dev1438 in a venv (version pinned, PyPI latest on 2026-11-16). Hermes (Linux): same pinned pip command. AGPL-3.0: sharing a modified app means sharing its source. Android: library build only (README.md:17), no app. claude.ai: no.

## YOLO install

YOLO (your own risk): skips the venv and the version pin.
pip install essentia (Linux/WSL2, README.md:23)

## Install notes

Safe, but ask the user before installing.
Windows: supported per README.md:17 (pip wheels are for Linux x86_64: `pip install essentia`, README.md:23).
Android: supported by the library build (README.md:17).
