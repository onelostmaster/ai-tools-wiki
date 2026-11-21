# motlab (staryone)

- **Type:** CLI
- **Category:** generating videos, editing
- **Official URL:** https://github.com/staryone/motlab
- **GitHub repo:** https://github.com/staryone/motlab @ 9a44f75 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-18)
- **Decision:** Later
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-20

## Safety reason

a review bot code read @9a44f75: safe with the fixes in Safe install. One npm dependency, mediabunny 1.65.2, pinned exactly with a lockfile and no install scripts (package.json, package-lock.json, .npmrc save-exact). No telemetry and no API keys. Local servers bind 127.0.0.1 only (src/editor.js:204,211; src/server.js:78); viewer writes are refused unless Host and Origin are local (editor.js:89-93) and it serves files only inside the project folder (editor.js:182). Verified behaviour and fixes: (1) the npm route always installs globally (npm install -g @motlab/cli, README); fix: use a clone at the pinned commit instead. (2) node install.js runs npm ci (install.js:70), always writes a motlab launcher to ~/.local/bin (motlab.cmd plus a sh launcher on Windows, install.js:84-92) and copies the motlab and motlab-assets skills into ~/.claude/skills by default, replacing existing folders of those names that hold a SKILL.md (install.js:100-115), and records this in ~/.motlab/install.json (install.js:118); it never edits PATH itself, it prints the line to add (install.js:94-96); fix: run it with --dry-run first, and pass --bin <folder> if you want the launcher elsewhere. (3) motlab update fetches origin, fast-forwards and reruns the installer (src/update.js:30-53), which moves you off the reviewed commit; on a detached pinned checkout it stops with 'not on a branch' (update.js:28); fix: don't run motlab update; check out a newer commit only after a new review. (4) Network: get_sfx.py downloads sounds from api.openverse.org (skills/motlab/scripts/get_sfx.py:18,50,71), get_font.py from fonts.google.com (get_font.py:32,58), and the three.js/p5 templates load pinned versions from cdn.jsdelivr.net in headless Chrome (templates/template-three.html:10-11, template-p5.html:9); no fix needed, skip those scripts and templates if you want it offline. (5) Chrome runs headless with a throwaway profile and --enable-unsafe-swiftshader, and adds --no-sandbox only when run as root (src/chrome.js:25,31,37-41); fix: never run it as root or in an elevated (Administrator) terminal. (6) The skill's Python helpers need numpy, scipy and pillow unpinned (skills/motlab/requirements.txt); fix: install them in a venv. The skills tell the agent to ask the user before installing (SKILL.md:30-38; docs/install-for-agents.md:3,50).

## Safe install

Safe install (fixes applied): Claude Code on Windows (needs Node 24+, Chrome and ffmpeg/ffprobe on PATH; normal, not Administrator, terminal): git clone https://github.com/staryone/motlab.git %USERPROFILE%\\motlab && cd %USERPROFILE%\\motlab && git checkout 9a44f75 && node install.js --skill claude --dry-run, read where files go, then node install.js --skill claude. It writes the launcher to %USERPROFILE%\.local\\bin; add that to your user PATH yourself or call node %USERPROFILE%\\motlab\\bin\\motlab.js. Don't run motlab update (it leaves the reviewed commit). Optional Python helpers: python -m venv .venv && .venv\\Scripts\\pip install numpy scipy pillow. Hermes: same clone and pin, then node install.js --skill hermes --dry-run, then without --dry-run. claude.ai: no (needs local Node, Chrome and ffmpeg). Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin, the dry run and the no-update rule. npm install -g @motlab/cli then npx @motlab/cli setup (README); this always installs globally and copies the skills to %USERPROFILE%\.claude\\skills; update with npm install -g @motlab/cli@latest and motlab setup --update.

## Install notes

Ask the user before installing. Safe with the fixes in Safe install applied. Video-as-code engine for Claude Code, Codex and Hermes: canvas scene pages rendered with WebCodecs in headless Chrome, a local review viewer and two agent skills; no keys, no telemetry.
