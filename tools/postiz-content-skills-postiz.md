# postiz-content-skills (Postiz)

- **Type:** skill
- **Category:** generating videos, social posting, research
- **Official URL:** https://github.com/gitroomhq/postiz-content-skills
- **GitHub repo:** https://github.com/gitroomhq/postiz-content-skills @ 70fcc01 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-25); README list prices per Short about $16 of Seedance clips plus HeyGen and ElevenLabs credits (provider prices not checked)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-26

## Safety reason

a review bot read @70fcc01: safe with these fixes. Seven Claude Code skills plus helper scripts that call HeyGen (generate-video.js:50), EvoLink/Seedance (seedance.js:37) and OpenAI images with your own keys from ~/.content-skills/.env (chmod 600, install-deps.sh:157). load-env.sh:15 uses eval only on names already checked to be letters, digits and _ (:11). Verified 1: install.sh without --skills-only runs install-deps.sh (install.sh:49), which installs unpinned software globally: sudo apt-get ffmpeg and jq (install-deps.sh:66), npm install -g postiz, agent-browser, dataforseo-cli and @elevenlabs/cli (:90-93) plus agent-browser's Chromium (:102), latest openai and pillow into a venv (:84), six third-party skill repos with npx skills add -g (:113-121) and the claude-seo plugin at user scope (:123-124). Fix: run only ./install.sh --skills-only (install.sh:44-46) from the pinned commit and install each tool you actually need yourself at a fixed version after its own review. Verified 2: install.sh moves any existing skill with the same name to <name>.bak-<time> (install.sh:30-35). Fix: check %USERPROFILE%\.claude\\skills for these 7 names first. Verified 3: video-shorts Step 8 schedules the Short to your connected Postiz channels (video-shorts/SKILL.md:184-195), gated on your yes (:178); seo-builder creates WordPress posts with the status from brand.md, default draft (seo-builder-skill/SKILL.md:124). Fix: keep brand.md status 'draft', connect no social channels to Postiz until you choose to, and answer no at the schedule step to keep the file local. Verified 4: seedance.js uploads local reference images to your Postiz media library to get a public URL (seedance.js:99-110). Fix: only pass images you are fine making public, or pass an https URL. Windows only through WSL (README:28). MIT (LICENSE).

## Safe install

Safe install (fixes applied):
Claude Code (Windows, inside WSL; README:28): git clone https://github.com/gitroomhq/postiz-content-skills ; cd postiz-content-skills ; git checkout 70fcc011b65635c4d38f2a021a7adda8d2432409 ; check ~/.claude/skills has no folders named content-setup, gpt-image, heygen-avatar-video, remotion-shorts, seedance-video, seo-builder-skill or video-shorts ; ./install.sh --skills-only . Don't run install.sh or install-deps.sh without --skills-only; install ffmpeg yourself and any CLI you need (postiz, elevenlabs, dataforseo-cli) at a fixed version after its own review. Keys go only in ~/.content-skills/.env. In brand.md keep the WordPress status 'draft'; say no at the Postiz schedule step until you want to post; only give seedance images you'd make public.
claude.ai, Hermes, Android: not supported (local Claude Code skills with shell scripts).

## YOLO install

YOLO (your own risk): skips the pinned commit, the --skills-only limit and the version pins. README: ./install.sh (installs ffmpeg/jq with sudo, four global npm CLIs, Chromium, six third-party skills and the claude-seo plugin, all latest), then /content-setup to enter keys.

## Install notes

Safe with fixes: ./install.sh --skills-only from the pinned commit 70fcc01 inside WSL; no full installer (it does sudo apt, npm -g and npx skills add -g of unpinned third-party tools); keep WordPress status draft and say no at the Postiz schedule step; seedance uploads local images to Postiz to make public URLs. Needs paid HeyGen, EvoLink and OpenAI keys; marketing pipeline, not a fit for the current projects.
