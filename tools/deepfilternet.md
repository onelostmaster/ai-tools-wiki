# DeepFilterNet

- **Type:** library
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/Rikorose/DeepFilterNet
- **GitHub repo:** https://github.com/Rikorose/DeepFilterNet
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Compute/dependencies and third-party model or asset licenses may add costs. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-07

## Safety reason

Targeted source read, not a full dependency/binary audit; Rikorose/DeepFilterNet @7b14b89. Speech denoising. Downloads model ZIP from GitHub (DeepFilterNet/df/enhance.py:253-272); utils.py:226 extractall; checkpoint.py:77 torch.load. Demo instructions pipe Rust installer to shell (demo/README.md:5). No telemetry found. Use official model/checkpoint only; never run the shell installer from a post.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows development; browser output may run on Android subject to GPU support. No native Claude skill/MCP in this repo.
