# robosuite

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://robosuite.ai
- **GitHub repo:** https://github.com/ARISE-Initiative/robosuite @ 5ce6643 (MIT; pushed 2026-07-11)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light read of README/LICENSE @5ce6643, a review, 2026-11-02): not code-reviewed; official project repo (ARISE Initiative), maintained. Built on MuJoCo.

## Safe install

Unreviewed: contain it: in a fresh conda env (conda create -n robosuite python=3.10, per robosuite.ai installation docs), pip install robosuite==1.5.2 (version pinned, PyPI latest on 2026-11-16; reviewed repo commit 5ce6643 is still HEAD), no API keys in that environment. It pulls pynput (keyboard/mouse listener, used for teleoperation, per PyPI requires_dist), so run it only in that env. Windows: officially macOS and Linux; the docs' Windows steps say to copy mujoco.dll from site-packages\\mujoco into site-packages\\robosuite\\utils if you get "mujoco.dll not found". Get a review before real use. claude.ai, Hermes, Android: no.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Any platform: see its README; no Windows steps checked.
