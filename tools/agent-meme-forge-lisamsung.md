# agent-meme-forge (lisamsung)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/lisamsung/agent-meme-forge
- **GitHub repo:** https://github.com/lisamsung/agent-meme-forge @ 184b06a (v0.1.0, MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-09)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-24

## Safety reason

a review bot read @184b06a (v0.1.0, commit 2026-09-01, still the latest on 2026-11-24; read: pyproject.toml, README.md, skills/generate-meme-gif-pack/SKILL.md, scripts/imagegen_client.py, dense_frames.py, meme_pack.py (network, subprocess and file paths), references/wechat-platform-upload.md; nothing run): safe with these fixes. A Codex skill plus a local Python processor (Pillow, numpy; pyproject.toml) that turns keypose images into WeChat-sized 240x240 GIF sticker packs. No hooks, MCP servers, eval, pickle or shell=True. Verified 1: image generation sends your prompts and reference images with MEME_IMAGE_API_KEY (or OPENAI_API_KEY) to MEME_IMAGE_BASE_URL (or OPENAI_BASE_URL) (imagegen_client.py:64-86), and fetches the result URL the provider returns (imagegen_client.py:107); the key is redacted from error text (imagegen_client.py:78). Fix: set MEME_IMAGE_BASE_URL and MEME_IMAGE_API_KEY explicitly for the one provider you mean, with a spend-capped key. Verified 2: the imagegen-batch command runs Codex's own image_gen.py from ~/.codex/skills/.system/imagegen (or CODEX_HOME / ~/.codex-switcher) with subprocess (meme_pack.py:452-460, 4006-4037); that script is not in this repo; unverified: its behaviour. Fix: use the in-repo imagegen_client.py / dense_frames.py route or Codex's built-in image tool instead of imagegen-batch. Verified 3: the optional WeChat upload runbook drives sticker.weixin.qq.com with a persistent browser profile kept in output/playwright/wechat-sticker-profile (wechat-platform-upload.md:9-21), so your WeChat login stays on disk there. Fix: skip the upload step, or delete that folder after uploading. Other: the README skill install copies into ~/.codex-switcher/skills (README.md:100-101), a non-standard folder; the Claude Code and Hermes variant is a separate skill (generate-meme-gif-pack-ai-studio) not in this repo (SKILL.md:3, 18). Fonts are OFL (assets/fonts/OFL.txt). MIT.

## Safe install

Safe install (fixes applied):
Windows + Codex: git clone https://github.com/lisamsung/agent-meme-forge ; cd agent-meme-forge ; git checkout 184b06a4dca82553ccbc9cef3dba659ead930bf7 ; py -m venv .venv ; .venv\\Scripts\\activate ; pip install -e . (Pillow and numpy only). Copy skills\\generate-meme-gif-pack to %USERPROFILE%\.codex\\skills\. For image generation set MEME_IMAGE_BASE_URL and MEME_IMAGE_API_KEY (a spend-capped key) for the one provider you use; don't use the imagegen-batch command (it runs Codex's own image_gen.py, not in this repo). Skip the WeChat upload runbook, or delete output\\playwright\\wechat-sticker-profile after using it.
Claude Code (Windows): copy the same folder to <project>\.claude\\skills\\ and run the Python scripts from the venv; the Codex image step needs your own endpoint as above.
claude.ai, Hermes, Android: not supported (needs local Python; the Hermes variant is a different, unreviewed skill).

## YOLO install

YOLO (your own risk): skips the pinned commit, the venv, the explicit endpoint and the imagegen-batch caution. Follow README.md:71-102 (pip install -e '.[dev]', cp -R the skill to ~/.codex-switcher/skills) and let Codex run imagegen-batch and the WeChat upload runbook.

## Install notes

Safe with fixes: Codex skill + local Python processor that turns one reference image or concept into a 16/24-sticker animated Chinese WeChat GIF pack (keyposes from an image model, frames rendered locally). Pin 184b06a, venv install, explicit spend-capped image endpoint, no imagegen-batch, skip or clean up the WeChat upload profile. Off-format for a project (scout 0.5).
