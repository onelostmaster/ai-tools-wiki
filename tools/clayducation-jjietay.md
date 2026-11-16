# clayducation (jjietay)

- **Type:** skill
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/jjietay/clayducation
- **GitHub repo:** https://github.com/jjietay/clayducation @ af8dcf0 (v0.5.3; MIT; committed 2026-11-10 10:23 ET, HEAD on 2026-11-11)
- **Price:** Free (MIT LICENSE file); runs locally, no paid API in the code read
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (code read @af8dcf0, 2026-11-11, no-intake review): Caution. The repo's own code is local and clean: no keys or paid APIs, the voice check re-listens with a local Whisper (engine/voicecheck.mjs, engine/tts/hear.py), rendering runs headless Chrome against a 127.0.0.1-only server (engine/make.mjs lines 838, 885). Why caution: the setup (bin/clayducation.mjs) shows its plan and asks before acting, but pipes curl https://astral.sh/uv/install.sh into sh when uv is missing (line 148), clones and npm-installs explainroo from another author unpinned (lines 143-144), and creates symlinks in ~/.claude/skills and ~/.claude/agents (lines 230-252); headless Chrome runs with --no-sandbox (make.mjs 865, 885). bin/update.mjs --apply moves to the newest tag and reruns the setup with --yes, but SKILL.md lines 19-30 tell Claude to ask the user first. agents/clay-kit.md line 64 assumes a separate heat-guard skill that is not in the repo. Correction to the scout note: the voice check uses local Whisper, not ElevenLabs Scribe. Not reviewed: explainroo, the pip and npm dependencies, engine/vendor/three.module.min.js, binary fonts, models and media, tests. No fix: no native Windows route (Linux/macOS only, INSTALL.md) and headless Chrome always runs with --no-sandbox (engine/make.mjs 865, 885) with no setting to change it; both are contained by running it only in a devcontainer or WSL (see Safe install).

## Safe install

Safe install (fixes applied):
Windows: no native install (setup and engine call which, apt/brew and venv/bin paths; INSTALL.md lists Linux and macOS only). Claude Code in a Linux devcontainer or WSL only, with these fixes: (1) manual route from INSTALL.md pinned to the reviewed commit: git clone https://github.com/jjietay/clayducation, git checkout af8dcf0, never npx clayducation; (2) install uv yourself from its official installer first, so the setup never runs its curl https://astral.sh/uv/install.sh | sh (bin/clayducation.mjs line 148); (3) explainroo, which the setup clones and npm-installs unpinned into ~/.explainroo (lines 143-144), is unverified: keep the whole thing in the devcontainer, no keys or logged-in browser profiles in it; (4) the setup symlinks into ~/.claude/skills and ~/.claude/agents (lines 230-252): run the setup with the container's own ~/.claude, not your Windows one; (5) answer Later to every UPDATE notice (bin/update.mjs --apply moves to the newest tag and reruns setup with --yes). No fix: headless Chrome always runs with --no-sandbox (engine/make.mjs lines 865, 885) and there is no setting to turn it off; the container is the containment, and it only loads its own 127.0.0.1 page. claude.ai, Hermes and Android: no install route.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Code-reviewed by a review bot @af8dcf0 (v0.5.3) (caution). No native Windows support: the setup and engine call which, sudo apt or brew and venv/bin/python paths, and INSTALL.md lists only Linux and macOS steps; on Windows it would need WSL, which the repo does not document. If you try it, use the manual route in INSTALL.md pinned to the reviewed commit (git clone, git checkout af8dcf0) rather than npx clayducation, and install uv yourself from its official installer instead of letting the setup pipe it into sh. The setup also clones and npm-installs explainroo (a separate repo by another author, unpinned, not reviewed) into ~/.explainroo and downloads Whisper and Kokoro models. When the skill prints an UPDATE notice, say Later until the new release is reviewed (Update now moves to the newest tag and reruns the setup with --yes). Needs Node 22+, Chrome or Chromium, ffmpeg, Python 3.12; Chatterbox voice needs an NVIDIA GPU (Kokoro runs on CPU); Manim needs LaTeX. Safer path for our projects: borrow the listen-back voice check idea (engine/voicecheck.mjs plus a local Whisper re-listen in engine/tts/hear.py) rather than installing.
