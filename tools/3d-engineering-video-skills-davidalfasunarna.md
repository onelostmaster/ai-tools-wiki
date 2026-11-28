# 3D Engineering Video skills (davidalfasunarna)

- **Type:** skill
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/davidalfasunarna/3d-engineering-video-claude-skills
- **GitHub repo:** https://github.com/davidalfasunarna/3d-engineering-video-claude-skills @ 8978568 (GPL-3.0)
- **Price:** Free on GitHub, GPL-3.0 (github.com, checked 2026-11-26); Higgsfield credits are a separate paid service (price not checked)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-27

## Safety reason

Read: README.md, the three skills/*/SKILL.md, the dist/*.zip contents (identical to skills/ at this commit), kit/box/setup.sh, up.sh, kit/sandbox/final_check.sh, kit/audio/asr.py, and a grep of every script for network, subprocess, eval/exec, delete and key/env use; nothing run): safe with these fixes. Three Claude skills plus a Python kit; everything runs in Claude's cloud code workspace, the Higgsfield sandbox and a rented Higgsfield GPU box, never on your own computer. It asks for no API keys (README: Higgsfield is connected as a connector with your own login), and its subprocess calls pass fixed argument lists to ffmpeg/ffprobe (for example kit/audio/audition.py:13, vo_prep.py:9). Verified 1: on first use the skill clones this repo's newest commit, not a pinned one (skills/3d-engineering-video/SKILL.md:22 and higgsfield-blender-render/SKILL.md:39, git clone --depth 1 with no checkout), so later repo changes run without review. Fix: before zipping, change both clone lines to clone and then git -C ~/3dv-repo checkout 8978568, then rebuild the ZIPs (README: python3 dist/make_dist.py). Verified 2: it spends paid Higgsfield credits on voice takes and a per-second GPU rental; before gpu_rent the skill must show the price, an estimate and a hard limit and wait for your approval, and approval covers one job (higgsfield-blender-render/SKILL.md:14-15). Fix: give a low hard limit at that approval step and keep only the credits for one video in the account. Verified 3: on the rented GPU box setup.sh pipes the uv install script from astral.sh into sh (setup.sh:8), installs unpinned pillow and numpy (setup.sh:11) and fetches a font from google/fonts main (setup.sh:15); asr.py:14 downloads a faster-whisper model in the Higgsfield sandbox. Fix: none needed on your side beyond containment: these run only on the rented box and sandbox, which hold none of your files or keys, and the render skill shuts the box down at the end; don't upload private files to that chat. License GPL-3.0 (LICENSE). README: tested only in the Claude app, English and Indonesian.

## Safe install

Safe install (fixes applied):
claude.ai (Windows browser; the skills then also show in the Android Claude app on the same account): connect the Higgsfield connector first (README). Download the repo at commit 8978568 (github.com/davidalfasunarna/3d-engineering-video-claude-skills/archive/8978568bee82b51a956087b24992b36214931e2e.zip), and in skills/3d-engineering-video/SKILL.md line 22 and skills/higgsfield-blender-render/SKILL.md line 39 add a checkout of 8978568 after the git clone (clone without --depth 1). Zip each of the three skills folders (or run python3 dist/make_dist.py) and upload them in Customize > Skills > Upload a skill. At the credit approval step give a low hard limit; keep only one video's credits in Higgsfield.
Claude Code, Hermes: not supported (README: needs claude.ai skills with code execution plus the Higgsfield connector; tested only in the Claude app).

## YOLO install

YOLO (your own risk): skips the pinned commit in the skill clone lines and the low credit limit. README: upload the three ZIPs from dist/ in Customize > Skills and connect Higgsfield.

## Install notes

Safe with fixes: pin the kit clone in both SKILL.md files to commit 8978568 before zipping (they clone the newest commit on first use); set a low hard credit limit when the skill asks before renting the GPU. Runs only in Claude's cloud workspace and Higgsfield's sandbox and rented GPU; no API keys. Needs a paid Higgsfield account. Fits the faceless video channel: 60-75 s vertical 3D explainer Shorts with AI voice and word-by-word captions.
