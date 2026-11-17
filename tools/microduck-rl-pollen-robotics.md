# microduck_rl (Pollen Robotics)

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://pollen-robotics.com/microduck
- **GitHub repo:** https://github.com/pollen-robotics/microduck_rl (Apache-2.0; pushed 2026-10-31; not reviewed)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); the real Microduck robot is sold by Pollen Robotics (not priced)
- **Decision:** Try
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-16

## Safety reason

a review bot (repo metadata via GitHub API, a review, 2026-11-02): not code-reviewed. Training code; needs an NVIDIA GPU for MuJoCo Warp.

## Safe install

Unreviewed: contain it: clone at the checked commit (git clone https://github.com/pollen-robotics/microduck_rl, then git checkout 0daab16, develop HEAD on 2026-11-16) inside a WSL2 or Docker container with an NVIDIA GPU, no API keys or tokens in that environment, and turn off any experiment logging that sends runs online. Get a review before real use. claude.ai, Hermes, Android: no.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Any platform: NVIDIA GPU needed (mjlab / MuJoCo Warp).
