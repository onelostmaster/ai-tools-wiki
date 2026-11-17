# cinetic

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/Leonxlnx/cinetic
- **GitHub repo:** https://github.com/Leonxlnx/cinetic @ f4bbfc8 (plugin 1.5.1; MIT; committed 2026-11-06 19:34 ET, HEAD on 2026-11-11; tag v1.5.1 = a6a6a02)
- **Price:** Free (MIT LICENSE file); optional stock-photo API keys are the providers' own
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @f4bbfc8, 2026-11-11, no-intake review): Safe. One skill (skills/cinetic/SKILL.md, references, Remotion and HyperFrames starters) plus local Node, Python and bash helpers; .claude-plugin/plugin.json and marketplace.json only name the plugin (no hooks, no MCP servers, no allowed-tools). Network use is limited to fetching assets on request: scripts/assets.mjs searches Openverse, Wikimedia Commons, NASA, the Art Institute of Chicago, the Met and Mixkit, and sends optional Pexels/Unsplash/Pixabay keys only to their official APIs (lines 772-804) with redaction in messages (line 221); scripts/logos.mjs fetches logos from gilbarbara/logos, svgl, Simple Icons (jsDelivr) and Commons. scripts/hf-finish.sh line 101 evals the output of its own local hf-preflight.cjs; npx -y hyperframes@0.8.79 is pinned; hyperframes-starter has a postinstall that only runs its local setup.mjs (copies files). Writes history files under ~/.cinetic. Not reviewed: earshot (separate repo), the npm/pip dependencies, binary fonts and images, tests.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): git clone https://github.com/Leonxlnx/cinetic.git, git checkout f4bbfc8 (reviewed), copy skills\\cinetic into %USERPROFILE%\.claude\\skills\\ (docs/setup.md manual route) and start a new session. Needs Node, ffmpeg/ffprobe 6+ on PATH (winget install Gyan.FFmpeg), Python 3.11+ in a venv with pip install -r scripts\\requirements.txt, a headless Chromium, and Git Bash for the bash scripts (README). Do not run hyperframes init: it installs its vendor's skills into ~/.claude/skills (docs/setup.md); use new-film.sh --engine hyperframes. Stock keys (PEXELS_API_KEY, UNSPLASH_ACCESS_KEY, PIXABAY_API_KEY) are optional and go in environment variables only; they are sent only to those official APIs (scripts/assets.mjs lines 772-804). It writes history under ~/.cinetic. Sound effects need earshot (separate repo, unreviewed: contain it: install only after its own review).

## YOLO install

YOLO (your own risk): skips the commit pin and the manual copy.
/plugin marketplace add Leonxlnx/cinetic then /plugin install cinetic@cinetic, or npx skills add Leonxlnx/cinetic#v1.5.1 (docs/setup.md; HEAD or the tag, not the reviewed commit).

## Install notes

Code-reviewed by a review bot @f4bbfc8 (plugin 1.5.1, main after the v1.5.1 tag) (safe). Claude Code on Windows, pinned: git clone https://github.com/Leonxlnx/cinetic.git, git checkout f4bbfc8, then copy skills\\cinetic into %USERPROFILE%\.claude\\skills\\ (docs/setup.md manual route). Unpinned alternatives (docs/setup.md): npx skills add Leonxlnx/cinetic#v1.5.1 (tag, not the reviewed commit), or /plugin marketplace add Leonxlnx/cinetic then /plugin install cinetic@cinetic. Needs Node, ffmpeg/ffprobe 6+ on PATH (e.g. winget install Gyan.FFmpeg), Python 3.11+ in a venv with scripts\\requirements.txt (numpy, opencv-python, scipy, soundfile, pyloudnorm, librosa, pillow, fonttools, brotli, uharfbuzz) and a headless Chromium; the scripts are bash, so on Windows follow the README's Git Bash steps. Sound effects need earshot (a separate repo by the same author, not reviewed). Optional stock keys (PEXELS_API_KEY, UNSPLASH_ACCESS_KEY, PIXABAY_API_KEY) go in environment variables only, never in chat. Do not run hyperframes init (docs/setup.md: it installs its vendor's skills into ~/.claude/skills); use new-film.sh --engine hyperframes. A full film takes one to two hours and several hundred thousand tokens (README).
