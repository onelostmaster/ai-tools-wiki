# aliang-knowledge-video (aliangSSS)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/aliangSSS/aliang-knowledge-video
- **GitHub repo:** https://github.com/aliangSSS/aliang-knowledge-video @ 1687e5e (MIT LICENSE file with an asset note, which is why GitHub calls it unrecognised; HEAD on 2026-11-11)
- **Price:** Free (MIT LICENSE file for code and docs; default background music not covered, sound effects CC0 from Kenney); Remotion is free for individuals and companies of up to 3 people per the repo README (see remotion.dev/license)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (code read @1687e5e, 2026-11-11, no-intake review): Safe. The Python tools under scripts/ (about 1,600 lines) only call local ffmpeg, npm, npx remotion and node through subprocess with argument lists, no shell=True, eval, keys, paid APIs or network calls of their own (scripts/common.py lines 32-54, scripts/render.py lines 34-47, scripts/preview.py line 40). scripts/new_project.py copies the template into the output folder, refuses a non-empty folder without --force (line 72), keeps npm and pip caches and temp files inside the project (lines 82-84), and installs Remotion 4.0.533 and React at exact versions (template/package.json; no lockfile, so sub-dependencies float). Nothing is written to ~/.claude or system folders. Notes: the skill asks Claude to search the web for facts (README), and the default BGM is copyrighted by its author (LICENSE lines 24-31, README licence section). Not reviewed: npm and pip dependencies, the Remotion-downloaded Chrome, binary media and fonts.

## Safe install

Safe install (fixes applied):
Windows Claude Code: `git clone https://github.com/aliangSSS/aliang-knowledge-video`, `git checkout 1687e5e` (the reviewed commit, still HEAD on 2026-11-15), copy the folder to %USERPROFILE%\.claude\\skills\\aliang-knowledge-video\\ and restart Claude Code. Install Node.js 18+ and Python 3.9+ yourself. Create projects with `python scripts/new_project.py <dir> --venv` so numpy, scipy, matplotlib and pillow go into the project's own .venv, never your global Python (scripts/new_project.py:87-91). npm install runs on project creation with exact top-level versions and no lockfile, so sub-dependencies float (scripts/new_project.py:101; template/package.json); after the first install, commit the generated package-lock.json and use `npm ci` for later projects. The first render downloads Chrome Headless Shell (about 270 MB) through Remotion. Replace assets/bgm/default.mp3 with your own track before posting publicly (it is not MIT, LICENSE:24-31). Not a claude.ai, Hermes or Android tool.

## YOLO install

YOLO (your own risk): skips the commit pin, the per-project venv and the lockfile step.
git clone https://github.com/aliangSSS/aliang-knowledge-video && python scripts/new_project.py <dir>

## Install notes

Code-reviewed by a review bot @1687e5e (safe). Claude Code on Windows: git clone the repo, git checkout 1687e5e, and copy the whole folder to %USERPROFILE%\.claude\\skills\\aliang-knowledge-video\\ (or a project's .claude\\skills\), then restart Claude Code. Needs Node.js 18+ and Python 3.9+; each video project takes about 600 MB and the first render downloads Chrome Headless Shell (about 270 MB) through Remotion. The project setup (scripts/new_project.py) runs npm install with exact versions in template/package.json but no lockfile, and with --venv pip-installs numpy, scipy, matplotlib and pillow unpinned into the project's own .venv. For a public channel, swap the default background music for your own track (python tools/prepare_bgm.py <file>): the bundled assets/bgm/default.mp3 is not covered by the MIT licence. Output is Chinese-language by design; English would need edits to the skill text and fonts.
