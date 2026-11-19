# DeepFilterNet

- **Type:** library
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/Rikorose/DeepFilterNet
- **GitHub repo:** https://github.com/Rikorose/DeepFilterNet
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Claude code read @7b14b89 v0.5.6 (2026-11-18): safe with fixes. The Python package downloads model zips from GitHub main (DeepFilterNet/df/enhance.py:253-272) and loads them with torch.load (df/checkpoint.py:77); on torch 2.6+ that load is weights_only. The demo pipes rustup to sh (demo/README.md:5). No telemetry. Fix: own venv with torch 2.6+, pinned package, skip the demo installer.

## Safe install

Safe install (fixes applied):
Own venv; pip install "torch>=2.6" torchaudio; pip install deepfilternet==0.5.6; run on copies of your audio; skip demo/ and its curl|sh; Rust users: rustup from rustup.rs docs.

## YOLO install

YOLO (your own risk): skips the venv, torch 2.6 and the pin.
pip install deepfilternet and run the demo installer.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows CLI or Python library; not an Android tool. No native Claude skill/MCP in this repo.
