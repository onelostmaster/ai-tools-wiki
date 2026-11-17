# ManiSkill

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://maniskill.ai
- **GitHub repo:** https://github.com/mani-skill/ManiSkill @ 62ff3a5 (Apache-2.0; moved from haosulab/ManiSkill; pushed 2026-08-04)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light read of README/LICENSE @62ff3a5, a review, 2026-11-02): not code-reviewed; official project repo, maintained. "Limited support for windows" (`README.md:54`); Linux best.

## Safe install

Unreviewed: contain it: in a fresh venv (Python 3.9+), pip install mani_skill==3.0.1 torch (version pinned, PyPI latest on 2026-11-16; README.md:34-36 at 62ff3a5, still HEAD), no API keys or tokens in that environment, and set up Vulkan per the official installation docs (README.md:39). Windows: CPU sim and rendering only, no GPU sim (README "System Support" table; SAPIEN 3.0.3 has win_amd64 wheels); WSL2 has no rendering. Get a review before real use. claude.ai, Hermes, Android: no (Hermes Linux works with an NVIDIA GPU after a review).

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Linux first; Windows has limited support (README.md:54).
