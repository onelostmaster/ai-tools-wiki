# brief2mp4 (qualixar)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://qualixar.com/learn/guides/brief2mp4-guide
- **GitHub repo:** https://github.com/qualixar/brief2mp4 @ 9935db4 (v0.8.0, MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-16)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-24

## Safety reason

a review bot read @9935db4: safe with these fixes. No hooks or MCP servers in the repo; no API keys used; no shell=True or eval in the Python scripts. Verified 1: the plugin route also installs a second plugin, brief2motion, from the separate repo qualixar/brief2motion (plugin/.claude-plugin/plugin.json:33, .claude-plugin/marketplace.json:46-57; README.md:352), not reviewed here, and the marketplace route is unpinned (README.md:99). install.ps1 does not install brief2motion. Fix: clone this repo at 9935db4 and use the script install (install.ps1 -Claude), not the plugin marketplace. Verified 2: SKILL.md tells the agent to render with npx hyperframes with no version (SKILL.md:159, 3 places), which fetches the newest hyperframes from npm each time, while the scripts pin hyperframes@0.8.216 (film_build.py:24, character_sheet.py:26). Fix: in each project run npm i -D hyperframes@0.8.216 once so npx uses that local pinned copy. Verified 3: install.ps1 is meant to run with -ExecutionPolicy Bypass (install.ps1:3-10; that bypass applies only to that one process) and -InstallTools winget-installs Node, ffmpeg and Git (install.ps1:92). It installs into %USERPROFILE%\.claude by default (install.ps1:31). Fix: install Node 22+, ffmpeg and Git yourself and run install.ps1 -Claude without -InstallTools. Verified 4: scripts/fetch_music.py searches the Openverse API (fetch_music.py:33) and downloads only https links with size caps (fetch_music.py:16, 94-98); search words leave your machine. Fix: none needed; skip it for private briefs. Other: the optional edit pack verifies downloads against SHA256 (edit/install_edit.ps1:156-160); the optional 3D pack pins pip packages (3d/requirements-core.txt) and uses npm ci with a lockfile (3d/install_3d.ps1:86-87). SKILL.md:152 asks the agent to add one line asking for a GitHub star to the first delivery message (text only, no action). MIT.

## Safe install

Safe install (fixes applied):
Windows + Claude Code: install Node 22+ (winget install -e --id OpenJS.NodeJS.LTS), ffmpeg and Git for Windows yourself. Then: git clone https://github.com/qualixar/brief2mp4 ; cd brief2mp4 ; git checkout 9935db44967749f475a3fb6e67abd7f880493293 ; powershell -ExecutionPolicy Bypass -File .\\install.ps1 -Claude (no -InstallTools, no plugin marketplace, so brief2motion is not added). In each video project run npm i -D hyperframes@0.8.216 once before the first render. Skip the 3D and edit packs until you need them (both verify or pin their downloads). Keep normal permission prompts on.
claude.ai, Hermes, Android: not supported (needs local Node, ffmpeg and Claude Code or Codex).

## YOLO install

YOLO (your own risk): skips the pinned commit, the pinned hyperframes and leaving out brief2motion. In Claude Code: /plugin marketplace add qualixar/brief2mp4 then /plugin install brief2mp4@brief2mp4 (also installs brief2motion), or run install.ps1 -InstallTools to let winget install Node, ffmpeg and Git.

## Install notes

Safe with fixes: Claude Code/Codex skill that turns a written brief into a checked MP4 (82 art forms, HyperFrames, Three.js, optional Blender 3D and edit packs). Pin commit 9935db4, script install with install.ps1 -Claude (no plugin marketplace, so no unreviewed brief2motion), install Node/ffmpeg/Git yourself, npm i -D hyperframes@0.8.216 per project. Possible reference for the faceless video channel.
