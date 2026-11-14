# Habitat Lab (Meta)

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://aihabitat.org
- **GitHub repo:** https://github.com/facebookresearch/habitat-lab @ 0fb6f43 (MIT; pushed 2026-05-07)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light read of README/LICENSE @0fb6f43, a review, 2026-11-02): safe, official Meta repo; code not reviewed line by line. Uses conda packages from the aihabitat channel (`README.md:94`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Linux/macOS: `conda install habitat-sim withbullet -c conda-forge -c aihabitat` then `pip install habitat-lab` (README.md:91-98); no Windows build listed.
