# ComfyUI

- **Type:** app
- **Category:** design, generating videos
- **Official URL:** https://www.comfy.org/
- **GitHub repo:** https://github.com/Comfy-Org/ComfyUI @ 17ff1dc (GPL-3.0)
- **Price:** Free (GPL-3.0) (github.com, checked 2026-11-01); partner API nodes cost credits (price unknown)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (pattern scan plus targeted reads @17ff1dc, a review), 2026-11-01; Claude fit review only (scan stands): Looks safe. Listens on localhost by default (`cli_args.py:63`); telemetry flag off (`feature_flags.py:28-31`). Custom nodes are untrusted code; partner API nodes cost credits.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Windows: Comfy Desktop from `https://www.comfy.org/download` (NVIDIA GPU recommended) (README). Treat custom nodes as untrusted code.
