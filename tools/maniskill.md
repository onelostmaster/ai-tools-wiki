# ManiSkill

- **Type:** library
- **Category:** research, 3D and games
- **Official URL:** https://maniskill.ai
- **GitHub repo:** https://github.com/mani-skill/ManiSkill @ 62ff3a5 (Apache-2.0; v3.0.1; moved from haosulab/ManiSkill; commit 2026-08-01)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-22

## Safety reason

a review bot read @62ff3a5: safe with these fixes. No telemetry; no pickle.load or torch.load in the package. Verified 1: network use is only asset and demo downloads (mani_skill/utils/download_asset.py:55 Hugging Face snapshot_download, :118 urlretrieve; utils/download_demo.py:72), and an env or robot that needs missing assets asks y/n before downloading (utils/registration.py:70, agents/base_agent.py:186); the SHA-256 is checked where the source lists one (download_asset.py:125-130). Fix: answer n unless you want that asset; download only through python -m mani_skill.utils.download_asset <id>. Verified 2: assets go to ~/.maniskill (Windows: %USERPROFILE%\.maniskill) unless MS_ASSET_DIR is set (mani_skill/__init__.py:14-16); some datasets are large. Fix: set MS_ASSET_DIR to a folder on a drive with space. Verified 3: demo_manual_control.py:27 (and demo_manual_control_continuous.py:27) runs Python eval() on any extra command-line value starting with @. Fix: only type your own args; don't paste someone else's command with @ values. Verified 4: install pulls GitPython, huggingface_hub, nvidia-ml-py, imageio[ffmpeg] and SAPIEN (setup.py:31-54); GitPython only reads ManiSkill's own repo for commit info (__init__.py:42-45). Fix: own venv, pinned mani_skill==3.0.1. Windows: limited support (README.md:54): CPU sim and rendering only, no GPU-parallel sim. Unverified: rendering on your Windows GPU drivers (Vulkan). Containment: own venv, test one demo first.

## Safe install

Safe install (fixes applied):
Windows (PowerShell): py -3.11 -m venv ms ; ms\\Scripts\\activate ; pip install mani_skill==3.0.1 torch ; $env:MS_ASSET_DIR="D:\\maniskill_assets" (any folder with space). CPU sim only on Windows. Download assets only with python -m mani_skill.utils.download_asset <id>, answer n to download prompts you don't want, and never pass @ values you didn't write to demo_manual_control. No API keys in that venv.
Claude Code: same commands in that venv. Hermes (Linux with NVIDIA GPU): same in a venv plus Vulkan per the official install docs. claude.ai, Android: no.

## YOLO install

YOLO (your own risk): skips the separate venv, version pin and asset folder: pip install --upgrade mani_skill torch (README.md:34-36) into your main Python, assets in ~/.maniskill.

## Install notes

Safe with fixes: GPU-parallel robot manipulation simulator (SAPIEN); no telemetry; it only goes online to download assets, after a y/n prompt. Install pinned 3.0.1 in its own venv, set MS_ASSET_DIR to a roomy folder, and don't pass @ args you didn't write to the manual-control demos (they eval them). Windows: CPU sim only (README.md:54); Linux + NVIDIA for GPU sim.
