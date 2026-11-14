# Kokoro (hexgrad/kokoro)

- **Type:** library
- **Category:** voice and audio
- **Official URL:** https://github.com/hexgrad/kokoro
- **GitHub repo:** https://github.com/hexgrad/kokoro @ dfb907a (2025-08-06, Apache-2.0)
- **Price:** Free (Apache-2.0, github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @dfb907a, a review, 2026-11-01): Looks safe. Plain inference library; weights and voices download from Hugging Face on first use (`kokoro/model.py:46,67`; `pipeline.py:152`) and load with torch.load weights_only=True (`model.py:68`, `pipeline.py:157`). No telemetry, shell, eval or prompt injection.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Windows: `pip install kokoro>=0.9.4 soundfile`, then install espeak-ng from its GitHub releases .msi (`README.md:89-96`).
Claude Code (local only): same pip install in a local Python environment.
Hermes: call it from a local Python script; no Hermes-specific steps confirmed.
