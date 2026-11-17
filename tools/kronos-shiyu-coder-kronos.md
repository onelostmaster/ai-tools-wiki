# Kronos (shiyu-coder/Kronos)

- **Type:** library
- **Category:** finance, research
- **Official URL:** https://github.com/shiyu-coder/Kronos
- **GitHub repo:** https://github.com/shiyu-coder/Kronos @ 67b630e (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @67b630e, a review, 2026-11-02): safe. Downloads weights from Hugging Face (`webui/app.py:645-646`); pickle.load only on your own data files (`finetune/dataset.py:42`), so never load pickles from others. The post's AAAI claim is unconfirmed.

## Safe install

Safe install (fixes applied):
Windows (Python 3.10+, README.md:89): download the repo at commit 67b630e, make a venv and `pip install -r requirements.txt` (einops 0.8.1, huggingface_hub 0.33.1, safetensors 0.6.2 pinned; numpy, pandas, torch>=2.0.0 not pinned). Weights load from the official NeoQuasar Hugging Face repos (README.md: NeoQuasar/Kronos-small, Kronos-Tokenizer-base). Verified: finetune/dataset.py:42 uses pickle.load on the data file you give it. Fix: load only pickle files you made yourself, never ones from others. Set HF_HUB_DISABLE_TELEMETRY=1 (huggingface_hub env-var docs). Forecasts are research output, not trading advice. Claude Code: can run it. claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin, the venv and the pickle rule.
git clone the repo and pip install -r requirements.txt

## Install notes

Safe, but ask the user before installing.
Windows: Python in a venv with the Hugging Face weights, per its README (not tested). Android: no.
