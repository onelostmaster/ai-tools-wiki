# Wan2.1 (Wan-Video)

- **Type:** library
- **Category:** generating videos
- **Official URL:** https://github.com/Wan-Video/Wan2.1
- **GitHub repo:** https://github.com/Wan-Video/Wan2.1 @ 9737cba (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); DashScope prompt extender is a paid Alibaba Cloud API
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @9737cba, a review, 2026-11-02): safe. Local by default; the optional prompt extender can send your prompt to Alibaba's DashScope cloud with your API key (`wan/utils/prompt_extend.py:12,213-235`); weights load with torch.load (`wan/modules/t5.py:496`, `vae.py:614`): official weights only.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: `pip install -r requirements.txt` in a clone (README), NVIDIA GPU; skip the DashScope extender unless you want cloud prompts. Android: no.
