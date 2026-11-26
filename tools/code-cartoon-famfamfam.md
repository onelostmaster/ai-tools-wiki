# code-cartoon (famfamfam)

- **Type:** plugin
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/famfamfam/code-cartoon
- **GitHub repo:** https://github.com/famfamfam/code-cartoon @ 76ab9f7 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-24); fal.ai is a separate paid service (price not checked)
- **Decision:** Later
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-25

## Safety reason

a review bot read @76ab9f7: safe with these fixes. A Claude Code plugin with one skill plus local bash/Python scripts (numpy, scipy, pillow) that draw cartoons as code and render MP4 with HyperFrames. No hooks, no MCP server, no eval, pickle or shell=True; drawing, sound and Piper narration run locally (docs/PRIVACY.md). Verified 1: every render command runs HyperFrames through 'npx --yes hyperframes@0.8.164' (scripts/_lib.sh:9-10, scripts/cartoon:34), so npm downloads it without asking, and HyperFrames downloads a headless Chrome on first use (docs/PRIVACY.md, Network access). Fix: keep the pinned 0.8.164 (don't set CARTOON_HF_VERSION) and do the first render with network on, inside the devcontainer or sandbox. Verified 2: 'cartoon gen' sends your prompt, reference pictures, narration text or vocals to Cloudflare Workers AI, fal.ai or an OpenAI-compatible URL you set, with keys read from the environment, ./.env or ~/.config/code-cartoon/keys.env (gen.py:25-41, 66-70); result files are downloaded from the URL the service returns, with a curl fallback (gen.py:375-392). fal calls stop and print the price unless run with --yes (gen.py:336-346; SKILL.md:98), but Cloudflare and OpenAI-compatible calls have no price guard. Fix: leave gen keys unset (everything else works offline); if you use it, a spend-capped fal key in keys.env only, never a project .env, and say yes to each --yes price line yourself. Verified 3: Piper voices download into ~/.cache/code-cartoon/piper on first use (voice.py:12-14, 59-60) and each voice has its own licence (voice.py:61); piper-tts is GPL-3.0 and installed separately. Fix: pick a voice whose MODEL_CARD allows your use before publishing. Other: the README marketplace install tracks the repo's main branch, not a pinned commit. Bundled three.js, GSAP and fonts keep their own licences (THIRD_PARTY_NOTICES.md). MIT.

## Safe install

Safe install (fixes applied):
Claude Code (Windows, Git Bash): git clone https://github.com/famfamfam/code-cartoon ; cd code-cartoon ; git checkout 76ab9f72366308a323ac3d3b9c96616db59683c0 ; copy skills/code-cartoon to <project>/.claude/skills/ (instead of the marketplace install, which tracks main). Needs Node.js 22+, FFmpeg and Python 3.9+: py -m venv .venv ; .venv\\Scripts\\activate ; pip install numpy scipy pillow (add piper-tts only for narration). Leave CARTOON_HF_VERSION unset so HyperFrames stays at 0.8.164. Set no gen keys unless you need AI pictures; then only a spend-capped FAL_KEY in ~/.config/code-cartoon/keys.env, and approve each 'PAID CALL' price line yourself. Check with skills/code-cartoon/scripts/cartoon doctor.
claude.ai, Hermes, Android: not supported (needs local Node, FFmpeg and Python).

## YOLO install

YOLO (your own risk): skips the pinned commit, the venv and the key limits. README: claude plugin marketplace add famfamfam/code-cartoon then claude plugin install code-cartoon@famfamfam, pip install numpy scipy pillow piper-tts, and put any Cloudflare, fal or OpenAI-compatible keys in keys.env.

## Install notes

Safe with fixes: Claude Code skill that draws animated cartoons, explainers and song clips as code (canvas, three.js) and renders MP4 with HyperFrames, with synthesized sound and local Piper narration. Pin 76ab9f7, venv, keep HyperFrames at 0.8.164, no gen keys unless needed (then a spend-capped fal key and approve each price line). Fits the faceless video channel idea; a project kept it for QA ideas.
