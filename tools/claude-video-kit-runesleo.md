# claude-video-kit (runesleo)

- **Type:** plugin
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/runesleo/claude-video-kit
- **GitHub repo:** https://github.com/runesleo/claude-video-kit @ 3a908d8 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-23); CosyVoice/DashScope and Fish Audio are separate paid services (price not checked)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-24

## Safety reason

a review bot read @3a908d8: safe with these fixes. Plugin manifests declare no hooks and no MCP servers (.claude-plugin/plugin.json); the skill says it never uploads or publishes (SKILL.md:8-10, references/errors-and-privacy.md:17). Verified 1: the production render defaults to the paid CosyVoice cloud backend (scripts/render.sh:68, TTS_BACKEND default cosyvoice; tts_cosyvoice.py:104 reads DASHSCOPE_API_KEY), so your script text goes to Alibaba DashScope; TTS_BACKEND=fish sends it to api.fish.audio (tts.py:36). Fix: set TTS_BACKEND=indextts2 for local narration (README.md:271: nothing leaves the machine), or use a separate low-quota DashScope/Fish key only when you choose cloud narration. Verified 2: the recommended installs are unpinned: npx skills add runesleo/claude-video-kit (SKILL.md:39) and the plugin route through a different repo, runesleo/x-reader (SKILL.md:47, not reviewed here). Fix: clone this repo and check out 3a908d8, then copy skills/video-explainer into .claude/skills yourself (or /plugin marketplace add on that local clone path), never the x-reader marketplace. Verified 3: scripts/requirements.txt uses >= ranges (requests, faster-whisper, python-dotenv, opencc) and align.py:343 loads a faster-whisper model, which downloads from Hugging Face on first run. Fix: pip install inside a venv, pin the versions you get once, and allow network only for that install and first model download. Verified 4: render.sh is bash and the keyless demo needs macOS say (video-explainer.mjs:83). Fix: on Windows run in Git Bash or WSL2; there is no keyless demo on Windows, so use indextts2 or a cloud key. Other: Remotion pinned at 4.0.433 (remotion/package.json:11-16); modal_tts_batch.py is an optional Modal GPU runner that clones index-tts pinned at 830f6f8 (modal_tts_batch.py:56-57) and needs your Modal account: skip it. Child processes use spawn with shell:false (video-explainer.mjs:114,320). No telemetry found. MIT.

## Safe install

Safe install (fixes applied):
Windows + Claude Code: install Node 20+, Python 3.10+, ffmpeg and Git from their official sites. In Git Bash or WSL2: git clone https://github.com/runesleo/claude-video-kit ; cd claude-video-kit ; git checkout 3a908d8ae3a59d9f9aee83604665a4180e347111 ; npm ci --prefix remotion ; python -m venv .venv and activate it ; pip install -r scripts/requirements.txt, then pin the installed versions. Copy skills/video-explainer into your project's .claude/skills folder (no npx skills add, no x-reader marketplace). Set TTS_BACKEND=indextts2 for local narration, or add a separate low-quota DASHSCOPE_API_KEY only when you want cloud narration. Skip modal_tts_batch.py. Keep normal permission prompts on (never --dangerously-skip-permissions).
claude.ai, Hermes, Android: not supported (needs local Node, Python, ffmpeg and Claude Code or Codex).

## YOLO install

YOLO (your own risk): skips the pinned commit, pinned Python packages and local narration. In Claude Code: /plugin marketplace add runesleo/x-reader then /plugin install video-explainer-kit@runesleo (or npx skills add runesleo/claude-video-kit --skill video-explainer), clone the repo for rendering, npm ci --prefix remotion, pip install -r scripts/requirements.txt, and use the default CosyVoice backend with your DASHSCOPE_API_KEY.

## Install notes

Safe with fixes: Claude Code/Codex skill plus Remotion pipeline that turns a brief or script into a reviewed, narrated 9:16 explainer with storyboard, review-receipt and release gates; never uploads. Pin commit 3a908d8, copy the skill folder yourself (no x-reader marketplace), venv for Python, Git Bash or WSL2 on Windows, TTS_BACKEND=indextts2 to keep script text local, skip the Modal runner. Fits the faceless video channel idea.
