# Isaac Lab (NVIDIA)

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://isaac-sim.github.io/IsaacLab
- **GitHub repo:** https://github.com/isaac-sim/IsaacLab @ 171a0a9 (BSD-3 style; pushed 2026-11-02)
- **Price:** Free (BSD-3 style; Isaac Sim is a free NVIDIA download; github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** unreviewed
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude targeted read @7dd36fd (2026-11-17): Isaac Lab code has no telemetry or curl|bash. Unverified: Isaac Sim 6.2, which it needs (README.md:17), is a closed NVIDIA binary from pypi.nvidia.com (docs/_extensions/isaaclab_docs.py:258) -> Contain: own venv or the official container, pinned versions, a GPU box without personal files.

## Safe install

Unreviewed: contain it: dedicated Windows or Linux RTX machine or container; own venv; pip install "isaacsim[all,extscache]==<version from the docs>" --extra-index-url https://pypi.nvidia.com with the docs' exact version; Isaac Lab cloned at 7dd36fd. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Contain it: dedicated Windows or Linux RTX machine or container; own venv; pip install "isaacsim[all,extscache]==<version from the docs>" --extra-index-url https://pypi.nvidia.com with the docs' exact version; Isaac Lab cloned at 7dd36fd.
