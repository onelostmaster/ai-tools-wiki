# ComfyUI

- **Type:** app
- **Category:** design, generating videos
- **Official URL:** https://www.comfy.org/
- **GitHub repo:** https://github.com/Comfy-Org/ComfyUI @ 17ff1dc (GPL-3.0)
- **Price:** Free (GPL-3.0) (github.com, checked 2026-11-01); partner API nodes cost credits (price unknown)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (pattern scan plus targeted reads @17ff1dc, a review), 2026-11-01; Claude fit review only (scan stands): Looks safe. Listens on localhost by default (`cli_args.py:63`); telemetry flag off (`feature_flags.py:28-31`). Custom nodes are untrusted code; partner API nodes cost credits.

## Safe install

Safe install (fixes applied):
Windows: download ComfyUI_windows_portable_nvidia.7z (or the _amd/_intel build for your GPU) from github.com/Comfy-Org/ComfyUI/releases/tag/v0.43.0, extract it and start run_nvidia_gpu.bat. v0.43.0 (2026-10-27) is the newest release before the reviewed commit 17ff1dc, which is 26 commits after it; v0.44.0 and v0.45.0 are not reviewed. It listens on 127.0.0.1:8188 by default (comfy/cli_args.py:63): do not add --listen, which opens it to your network. Fix: install no custom nodes, because each one is outside code that runs with your user rights and is not covered by this review; get a review per node first. Partner API nodes spend paid credits only if you sign in and use them.

## YOLO install

YOLO (your own risk): skips the v0.43.0 pin and the no-custom-nodes rule.
Comfy Desktop from https://www.comfy.org/download (README; the Desktop app itself was not reviewed) with any custom nodes you like.

## Install notes

Windows: Comfy Desktop from `https://www.comfy.org/download` (NVIDIA GPU recommended) (README). Treat custom nodes as untrusted code.
