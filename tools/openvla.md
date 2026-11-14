# OpenVLA

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://github.com/openvla/openvla
- **GitHub repo:** https://github.com/openvla/openvla @ c8f03f4 (MIT; GitHub marks it a fork of TRI-ML/prismatic-vlms; last push 2025-03-23)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light read of README/LICENSE @c8f03f4, a review, 2026-11-02): caution. Quick start loads the model with trust_remote_code=True (`README.md:56`), which runs code from the model repo. No commit in 12+ months. Code not reviewed.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Linux with an NVIDIA GPU per README; no Windows steps checked.
