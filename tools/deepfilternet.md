# DeepFilterNet

- **Type:** library
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/Rikorose/DeepFilterNet
- **GitHub repo:** https://github.com/Rikorose/DeepFilterNet
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted source read, not a full dependency/binary audit; Rikorose/DeepFilterNet @7b14b89. Speech denoising. Downloads model ZIP from GitHub (DeepFilterNet/df/enhance.py:253-272); utils.py:226 extractall; checkpoint.py:77 torch.load. Demo instructions pipe Rust installer to shell (demo/README.md:5). No telemetry found. Use official model/checkpoint only; never run the shell installer from a post. No fix: the pre-built binary and the model files are not audited beyond this targeted source read; contained by using only official release/model downloads and copies of your audio.

## Safe install

Safe install (fixes applied):
Windows (no Python): download deep-filter-0.5.6-x86_64-pc-windows-msvc.exe from https://github.com/Rikorose/DeepFilterNet/releases (README.md:45, release v0.5.6) and run `deep-filter-0.5.6-x86_64-pc-windows-msvc.exe -o out noisy.wav` on copies of 48 kHz WAV files (only 48 kHz WAV is supported, README.md:46). Python route (only if you need it): in a fresh venv `pip install torch torchaudio -f https://download.pytorch.org/whl/cpu/torch_stable.html` then `pip install deepfilternet==0.5.6` (README.md:90-92). It downloads its model ZIP from the official repo (enhance.py:271-272) and loads checkpoints with torch.load (checkpoint.py:77), so never point it at a model or checkpoint from anywhere else. Skip the Rust demo: its instructions pipe an installer into the shell (demo/README.md:5). Not a claude.ai, Hermes or Android tool.

## YOLO install

YOLO (your own risk): skips the venv and version pin.
pip install torch torchaudio deepfilternet

## Install notes

Not installed. Ask the user before any installation, including Try. Windows CLI or Python library; not an Android tool. No native Claude skill/MCP in this repo.
