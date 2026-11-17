# Habitat Lab (Meta)

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://aihabitat.org
- **GitHub repo:** https://github.com/facebookresearch/habitat-lab @ 0fb6f43 (MIT; pushed 2026-05-07)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light read of README/LICENSE @0fb6f43, a review, 2026-11-02): safe, official Meta repo; code not reviewed line by line. Uses conda packages from the aihabitat channel (`README.md:94`).

## Safe install

Safe install (fixes applied):
Linux or WSL2 on Windows only (no Windows build listed): in a fresh conda env, conda install habitat-sim withbullet -c conda-forge -c aihabitat, then pip install habitat-lab==0.3.320260507 (version pinned, PyPI latest on 2026-11-16; commands per README.md:91-98). claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the fresh env and the version pin.
conda install habitat-sim withbullet -c conda-forge -c aihabitat && pip install habitat-lab

## Install notes

Safe, but ask the user before installing.
Linux/macOS: `conda install habitat-sim withbullet -c conda-forge -c aihabitat` then `pip install habitat-lab` (README.md:91-98); no Windows build listed.
