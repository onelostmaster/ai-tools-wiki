# Wan2.1 (Wan-Video)

- **Type:** library
- **Category:** generating videos
- **Official URL:** https://github.com/Wan-Video/Wan2.1
- **GitHub repo:** https://github.com/Wan-Video/Wan2.1 @ 9737cba (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); DashScope prompt extender is a paid Alibaba Cloud API
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (code read @9737cba, a review, 2026-11-02): safe. Local by default; the optional prompt extender can send your prompt to Alibaba's DashScope cloud with your API key (`wan/utils/prompt_extend.py:12,213-235`); weights load with torch.load (`wan/modules/t5.py:496`, `vae.py:614`): official weights only.

## Safe install

Safe install (fixes applied):
Windows (NVIDIA GPU): `git clone https://github.com/Wan-Video/Wan2.1` and `git checkout 9737cba` (reviewed; still HEAD on 2026-11-15), make a venv, install PyTorch 2.4 or later (CUDA build from pytorch.org), then `pip install -r requirements.txt` (README.md:99). Unverified: whether flash_attn (requirements.txt) builds on Windows. Download weights only from the official Wan-AI Hugging Face repos, e.g. `huggingface-cli download Wan-AI/Wan2.1-T2V-1.3B --local-dir ./Wan2.1-T2V-1.3B` (README.md:120-124); they load with torch.load (wan/modules/t5.py:496, vae.py:614), so no other weight files. Leave out --use_prompt_extend, or use --prompt_extend_method local_qwen: the dashscope method sends your prompt to Alibaba Cloud and needs DASH_API_KEY (generate.py:185-193,307-319; wan/utils/prompt_extend.py). Don't set DASH_API_KEY. Android: no. Not a Claude or Hermes tool.

## YOLO install

YOLO (your own risk): skips the commit pin, the venv and the local-only prompt rule.
git clone, pip install -r requirements.txt, --use_prompt_extend with dashscope and your DASH_API_KEY.

## Install notes

Safe, but ask the user before installing.
Windows: `pip install -r requirements.txt` in a clone (README), NVIDIA GPU; skip the DashScope extender unless you want cloud prompts. Android: no.
