# Kronos (shiyu-coder/Kronos)

- **Type:** library
- **Category:** finance, research
- **Official URL:** https://github.com/shiyu-coder/Kronos
- **GitHub repo:** https://github.com/shiyu-coder/Kronos @ 67b630e (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @67b630e, a review, 2026-11-02): safe. Downloads weights from Hugging Face (`webui/app.py:645-646`); pickle.load only on your own data files (`finetune/dataset.py:42`), so never load pickles from others. The post's AAAI claim is unconfirmed.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: Python in a venv with the Hugging Face weights, per its README (not tested). Android: no.
