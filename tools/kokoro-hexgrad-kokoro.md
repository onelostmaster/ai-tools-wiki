# Kokoro (hexgrad/kokoro)

- **Type:** library
- **Category:** voice and audio
- **Official URL:** https://github.com/hexgrad/kokoro
- **GitHub repo:** https://github.com/hexgrad/kokoro @ dfb907a (2025-08-06, Apache-2.0)
- **Price:** Free (Apache-2.0, github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @dfb907a, a review, 2026-11-01): Looks safe. Plain inference library; weights and voices download from Hugging Face on first use (`kokoro/model.py:46,67`; `pipeline.py:152`) and load with torch.load weights_only=True (`model.py:68`, `pipeline.py:157`). No telemetry, shell, eval or prompt injection.

## Safe install

Safe install (fixes applied):
Windows: in a fresh virtual environment (python -m venv kokoro-env, then activate it) run pip install kokoro==0.9.4 soundfile (0.9.4 is the newest on PyPI on 2026-11-16; repo HEAD is the reviewed commit dfb907a), then install espeak-ng from the .msi on github.com/espeak-ng/espeak-ng/releases (README.md:89-96). On first use it downloads the model and voices from Hugging Face (kokoro/model.py:46,67; pipeline.py:152) and loads them with torch.load weights_only=True (model.py:68, pipeline.py:157), so nothing else to fix.
Claude Code (Windows): same venv install, called from a local script.

## YOLO install

YOLO (your own risk): skips the virtual environment and the version pin.
pip install kokoro soundfile into your main Python, as the README shows.

## Install notes

Windows: `pip install kokoro>=0.9.4 soundfile`, then install espeak-ng from its GitHub releases .msi (`README.md:89-96`).
Claude Code (local only): same pip install in a local Python environment.
Hermes: call it from a local Python script; no Hermes-specific steps confirmed.
