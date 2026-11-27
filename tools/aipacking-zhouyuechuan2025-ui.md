# aipacking (zhouyuechuan2025-ui)

- **Type:** skill
- **Category:** editing, generating videos
- **Official URL:** https://github.com/zhouyuechuan2025-ui/aipacking
- **GitHub repo:** https://github.com/zhouyuechuan2025-ui/aipacking @ 0a0e914 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-13)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-26

## Safety reason

a review bot read @0a0e914: safe with these fixes. The skill is a Chinese-language workflow plus Node scripts that copy Remotion components into an existing 'Motion Studio / Remotion' job project. No network calls, no eval, no hooks, no MCP server, no keys; ffmpeg and ffprobe are called without a shell (mix-audio.mjs:9, 26). Verified 1: Codex's skill-installer line in docs/AIPACKING.md:10 installs from main, not a fixed commit. Fix: copy skills/aipacking from the pinned commit 0a0e914.; it keeps copies of changed files in .skill-backups/ (:7). Fix: use it only on a copy of the job project committed to git, run the --check step first, then review git diff and reword or delete the added AGENTS.md section before your agent reads it. Verified 3: the root package.json pins exact versions with a package-lock, and .npmrc keeps the npm cache in the repo; npm install is only needed for the repo's own demo, not for the skill. Fix: don't npm install the repo; the skill uses the job project's dependencies. Unverified: scripts/reference-matte.py needs an RVM ONNX model and Python packages that are not in the repo, and no skill file calls it. Contain: don't run it unless you fetch the model yourself from its official project. MIT (LICENSE); bundled workbench code under Apache-2.0 (licenses/Shotcraft.txt).

## Safe install

Safe install (fixes applied):
Claude Code (Windows): git clone https://github.com/zhouyuechuan2025-ui/aipacking ; cd aipacking ; git checkout 0a0e9144180b394a2ad526676e2d701ab3532502 ; copy the whole skills\\aipacking folder (keep its subfolders) into %USERPROFILE%\.claude\\skills\\aipacking. Don't npm install the repo. Before the skill's installer runs, commit your Motion Studio / Remotion job project to git (or use a copy), let it run 'node <skill>\\original\\aipacking\\scripts\\apply-aipacking.mjs <absolute job path> --check' first, then the real install, then review git diff: reword or delete the appended AGENTS.md section and check the validate.mjs change. Don't run reference-matte.py. Needs Node 20+, ffmpeg and ffprobe.
claude.ai, Hermes, Android: not supported (local Node, ffmpeg and a Remotion project).

## YOLO install

YOLO (your own risk): skips the pinned commit and the git-diff review. Codex: '$skill-installer' from https://github.com/zhouyuechuan2025-ui/aipacking/tree/main/skills/aipacking (docs/AIPACKING.md:10).

## Install notes

Safe with fixes: copy skills/aipacking from the pinned commit 0a0e914; run its installer only on a git-committed job project, --check first, then review the diff (it appends an AGENTS.md section worded as your request and edits validate.mjs and the render preflight); no npm install of the repo; don't run reference-matte.py. Chinese-language docs; needs an existing Motion Studio / Remotion job project, so it is a reference more than a drop-in.
