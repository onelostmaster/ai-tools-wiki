# OpenVLA

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://github.com/openvla/openvla
- **GitHub repo:** https://github.com/openvla/openvla @ c8f03f4 (MIT; GitHub marks it a fork of TRI-ML/prismatic-vlms; last push 2025-03-23)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @c8f03f4 (2026-11-17): safe with fixes. No commit since 2025-03-23. Loading uses trust_remote_code=True (README.md:56-62, vla-scripts/deploy.py:77-83), which runs the model repo's .py files. The deploy server binds 0.0.0.0:8000 with no auth (deploy.py:120,132). Fix: pin the HF revision you read, --host 127.0.0.1.

## Safe install

Safe install (fixes applied):
Linux + NVIDIA; clone at c8f03f4, own venv; pass revision="47a0ec7fc4ec123775a391911046cf33cf9ed83f" to both from_pretrained calls after reading its 3 .py files; python vla-scripts/deploy.py --host 127.0.0.1.

## YOLO install

YOLO (your own risk): skips the revision pin and loopback bind.
Load openvla/openvla-7b from main and serve on 0.0.0.0.

## Install notes

Ask the user before installing.
Linux with an NVIDIA GPU per README; no Windows steps checked.
