# motion-graphics (Barty-Bart)

- **Type:** skill
- **Category:** generating videos, editing, voice and audio
- **Official URL:** https://github.com/Barty-Bart/motion-graphics
- **GitHub repo:** https://github.com/Barty-Bart/motion-graphics @ 3d83d98 (MIT per LICENSE)
- **Price:** Free on GitHub, MIT; bundled sounds CC0 (github.com, checked 2026-11-25)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-26

## Safety reason

a review bot read @3d83d98: safe with these fixes. Six Claude Code skills (explainer-default, explainer-engaging, explainer-high-energy, motion-broll, object-separation, sound-effects): prompt files plus local Python/Node scripts that render HTML animations to video with Playwright Chromium and ffmpeg. No hooks, no MCP server, no API keys, no pickle or shell=True; the only network use is the installs and downloads below. Verified 1: motion-broll/scripts/setup.sh:11 installs numpy with pip --user, and if that fails with pip --break-system-packages into your system Python; setup.sh:15 runs 'npm install playwright' (no version) and 'npx playwright install chromium' in ./motion. Fix: don't run setup.sh; make a venv and install numpy there, and install a pinned playwright yourself in ./motion (npm install playwright@<version>, then npx playwright install chromium) inside the devcontainer or sandbox. The explainer skills ask for the same unpinned 'npm i playwright' (explainer-default/SKILL.md:133); pin it the same way. Verified 2: object-separation installs torch, transformers, opencv-python-headless, pillow and numpy unpinned into its own venv (object-separation/SKILL.md:17-18) and downloads a facebook/sam2.1 model of 156-898 MB from Hugging Face on first run into ~/.cache/huggingface (SKILL.md:29-31, 57, 161); after that it runs offline and uploads nothing (SKILL.md:8, 168). Fix: pin the pip versions in that venv and do the first run with network on in the sandbox. Verified 3: sound-effects downloads Mixkit preview MP3s with curl from assets.mixkit.co when a cue uses a runtime sound (sound_pass.py:58-66; manifest.json:1227-1671) into <out>/sound-effects-cache; those files are under the Mixkit licence, not CC0 (LICENSES.md). Fix: use only the bundled CC0 kit (pass bundled picks with --swaps) or keep Mixkit files out of anything you commit or publish. Other: sound_pass.py:24 eval()s ffprobe's frame-rate output (a number like 30000/1001 that ffprobe computes, not text from the video), so it is not a code path for the video's contents. 'npx skills add' (README:21) installs all six skills and tracks the repo's main branch, not a pinned commit. Fonts are OFL (engine/fonts/OFL-Geist.txt). MIT.

## Safe install

Safe install (fixes applied):
Claude Code (Windows, Git Bash, inside a devcontainer or sandbox for the first run): git clone https://github.com/Barty-Bart/motion-graphics ; cd motion-graphics ; git checkout 3d83d987d658601d8a1269eb691622bdcd427335 ; copy only the skill folders you want from skills/ to <project>/.claude/skills/ (instead of npx skills add, which tracks main). Needs Node.js, ffmpeg and Python 3. Don't run motion-broll/scripts/setup.sh: py -m venv .venv ; .venv\\Scripts\\activate ; pip install numpy==<version> ; then in ./motion: npm install playwright@<version> ; npx playwright install chromium. object-separation: its own venv with pinned torch, transformers, opencv-python-headless, pillow and numpy; first run with network on to fetch the SAM 2.1 model, then offline. sound-effects: use the bundled CC0 kit only, or keep downloaded Mixkit files out of commits and published videos. No keys needed.
claude.ai, Hermes, Android: not supported (needs local Node, ffmpeg and Python).

## YOLO install

YOLO (your own risk): skips the pinned commit, the venv, the version pins and the Mixkit rule. README: npx skills add Barty-Bart/motion-graphics, then run motion-broll/scripts/setup.sh (pip --user or --break-system-packages numpy, latest playwright) and the skills' own pip and npm lines.

## Install notes

Safe with fixes: six Claude Code skills for explainer videos, motion b-roll over talking-head clips, SAM 2 object separation and a measured sound-effects pass with a bundled CC0 kit. Pin 3d83d98, copy only the skills you want, skip setup.sh (venv + pinned playwright instead), pin object-separation's pip installs, keep Mixkit downloads out of published work. Fits the faceless video channel idea and a project reels.
