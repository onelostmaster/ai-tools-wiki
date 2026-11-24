# motion-explainer (Marwanenoudouar10)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/Marwanenoudouar10/motion-explainer
- **GitHub repo:** https://github.com/Marwanenoudouar10/motion-explainer @ b0ec17d (MIT)
- **Price:** Free on GitHub, MIT (LICENSE file, checked 2026-11-22); TTS service cost depends on the one you pick
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-23

## Safety reason

a review bot read @b0ec17d (commit 2026-10-24; read: SKILL.md, README.md, references/*.md, assets/template/package.json, every script in assets/template/scripts (doctor.sh, kill-chrome.sh, render/preview/frame/kit/master/entry/roughcut.sh, qa/*, audio/*.py, make_packs.py); nothing run): safe with these fixes. Verified 1: every helper is a bash script that uses nice, pgrep/pkill and source ~/.nvm/nvm.sh (e.g. render.sh:25, kill-chrome.sh:7-10, handoff_diff.py:26), so it does not run in Windows PowerShell or cmd. Fix: use it inside WSL2 (Ubuntu) with Claude Code installed in WSL. Verified 2: package.json pins Remotion 4.0.534, React 19.2.0 and TypeScript 5.9.3 exactly, but the template ships no package-lock.json, so npm install resolves the sub-dependencies fresh in every new project (SKILL.md:47). Fix: run npm install only in the new project folder (as SKILL.md:139 also says), keep the package-lock.json it writes, and copy that lockfile into later projects and use npm ci there. Verified 3: scripts/kill-chrome.sh:10 runs pkill -f chrome-headless-shell, which kills every headless Chrome of that name on the machine, including one from another Remotion project or a Studio render (the script only checks CLI renders, kill-chrome.sh:6-8). Fix: run it only when no other Remotion job is running. Verified 4: README Install (README.md:30) clones into ~/.claude/skills/motion-explainer, a user-level skill that Claude Code offers in every project; it does not install anything else. Fix: clone at the pinned commit b0ec17d. Verified 5: npx remotion browser ensure (references/pipeline.md:12) downloads Remotion's headless Chrome once, and the voice step downloads the whisper.cpp model from huggingface.co/ggerganov (scripts/audio/aligner.py:39). Both are the official sources; no API keys anywhere (voice-over is made by you by hand). Other: doctor.sh only checks tools and prints install lines, changes nothing (doctor.sh:2); the Python helpers are stdlib only and call ffmpeg/ffprobe/whisper-cli on local files; the pipeline runs several Claude subagents (references/orchestration.md), which use your Claude usage. Remotion itself needs a company license for larger companies (README.md:74), free for individuals. MIT.

## Safe install

Safe install (fixes applied):
Windows + Claude Code, in WSL2 (Ubuntu): sudo apt install ffmpeg python3 git ; install Node 20 with nvm ; git clone https://github.com/Marwanenoudouar10/motion-explainer ~/.claude/skills/motion-explainer ; cd ~/.claude/skills/motion-explainer ; git checkout b0ec17d4aab89ff1a812d64af6e4025d5670c0d1. For a narrated film build whisper.cpp from its official GitHub repo (github.com/ggml-org/whisper.cpp) and download ggml-base.en.bin from huggingface.co/ggerganov/whisper.cpp. Run Claude Code in WSL with normal permission prompts (never --dangerously-skip-permissions); let the skill copy the template to a new folder and run npm install only there; keep that package-lock.json and use npm ci with it in later projects. Run scripts/kill-chrome.sh only when no other Remotion job runs.
Windows native PowerShell, claude.ai, Hermes, Android: not supported (bash scripts; needs local Node, ffmpeg and Claude Code).

## YOLO install

YOLO (your own risk): skips the pinned commit and the saved lockfile. In WSL2: git clone https://github.com/Marwanenoudouar10/motion-explainer ~/.claude/skills/motion-explainer, then ask Claude Code for an explainer video and let it run npm install in each new project.

## Install notes

Safe with fixes: Claude Code skill that builds narrated motion-graphics explainer videos in Remotion (research with sources, script, chapters built by subagents, captions, sound, QA, render, -14 LUFS master) from a starter template. Use in WSL2 on Windows, pin commit b0ec17d, npm install only in the new project and reuse its lockfile, permission prompts on, kill-chrome.sh only when nothing else renders. Fits the faceless video channel idea.
