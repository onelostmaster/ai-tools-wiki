# LTX-Video (Lightricks)

- **Type:** library
- **Category:** generating videos
- **Official URL:** https://github.com/Lightricks/LTX-Video
- **GitHub repo:** https://github.com/Lightricks/LTX-Video @ 50f0aef (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (code read @50f0aef, a review, 2026-11-02): caution. The optional prompt enhancer loads a third-party Hugging Face model with trust_remote_code=True (ltx_video/inference.py:253-256; model in configs/ltxv-2b-0.9.8-distilled-fp8.yaml:12), which runs that model's own Python code: leave enhance_prompt off. Fix-rule re-rate 2026-11-18: every verified risk has its exact fix in Safe install (enhance_prompt left off so no trust_remote_code model is loaded, only official Lightricks weights, pinned 50f0aef); with those fixes applied: safe.

## Safe install

Safe install (fixes applied):
Windows: git clone https://github.com/Lightricks/LTX-Video, git checkout 50f0aef, then python -m pip install -e .[inference] in a venv (NVIDIA GPU). Always run with enhance_prompt off (the default); turning it on loads a third-party Hugging Face model with trust_remote_code=True, which runs that model's own Python code (ltx_video/inference.py:253-256; configs/ltxv-2b-0.9.8-distilled-fp8.yaml:12). Download only the official Lightricks weights. Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin and the enhance_prompt-off rule.
Windows: pip install -e .[inference] from the latest clone and use enhance_prompt; the prompt-enhancer model's remote code runs on your PC.

## Install notes

Ask the user before installing. Safe only with the fixes in Safe install applied.
Windows: python -m pip install -e .[inference] in a clone (README), NVIDIA GPU; keep enhance_prompt off. Android: no.
