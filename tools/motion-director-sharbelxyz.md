# motion-director (sharbelxyz)

- **Type:** skill
- **Category:** generating videos, editing
- **Official URL:** https://github.com/sharbelxyz/motion-director
- **GitHub repo:** https://github.com/sharbelxyz/motion-director @ a21ffbf (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-16)
- **Decision:** Later
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-20

## Safety reason

a review bot code read @a21ffbf: safe with the fixes in Safe install. Node standard library only, no npm dependencies of its own (scripts/lib.mjs:1); commands are started as argument lists, not shell strings (scripts/lib.mjs:50-61). The renderer is the third-party HyperFrames CLI, run through npx at the pinned version 0.8.188 (scripts/lib.mjs:12,81) with telemetry off, without installing its own agent skills, and with GEMINI/GOOGLE/HEYGEN keys removed from its environment unless you set MD_ALLOW_CLOUD=1 (scripts/lib.mjs:71-77; SKILL.md:297-301). Brand capture deletes the CLAUDE.md/AGENTS.md/.cursorrules files the capture writes, so captured sites don't feed instructions to your agent (scripts/brand-intake.mjs:134-135). No accounts, no posting, no uploads. Verified behaviour and fixes: (1) the curl | bash one-liner (README.md:26) clones the moving main branch (install.sh:32) and, with no flag, copies the skill into every agent folder it finds, Claude Code, Codex and Hermes (install.sh:49-52); fix: pinned clone at a21ffbf and copy only skills/motion-director by hand into one agent. (2) First run (SKILL.md:20-22,33) runs check-setup --fix, which downloads hyperframes@0.8.188 into the npx cache and HyperFrames' own headless Chrome (scripts/check-setup.mjs:34-45); nothing is installed globally (scripts/check-setup.mjs:6-7). Fix: let it, inside WSL. (3) On native Windows it fails: HyperFrames is started as spawnSync("npx") without a shell (scripts/lib.mjs:81), and Node cannot start the npx.cmd file that way (Node.js docs, child_process: Spawning .bat and .cmd files on Windows); check-setup also calls df (scripts/check-setup.mjs:47) and find-assets calls unzip (scripts/find-assets.mjs:31). Fix: run Claude Code and the skill inside WSL2 Ubuntu. (4) It goes online when you ask for these steps: brand intake opens the site you give in headless Chrome and fetches its YouTube channel images and simple-icons logos from jsdelivr (scripts/brand-intake.mjs:131,188,218,307); find-assets downloads CC0 images from ambientCG, Poly Haven, Wikimedia Commons and Openverse (scripts/find-assets.mjs:26,44,71,82); 3D props load three.js 0.147.0 from jsdelivr (scripts/prop-render.mjs:37-39); a reference URL needs yt-dlp (scripts/ref-style.mjs:33). Fix: only give it your own site and links you choose. (5) cutout.mjs is macOS-only and stops elsewhere (scripts/cutout.mjs:17); fix: supply your own cut-out PNGs. Unverified: the HyperFrames 0.8.188 npm package and its Chrome download were not code-read; containment: WSL2 only, no API keys in that environment, never set MD_ALLOW_CLOUD=1.

## Safe install

Safe install (fixes applied): Claude Code on Windows: use it inside WSL2 Ubuntu (native Windows fails, see Safety reason). In WSL: sudo apt install -y ffmpeg git and Node.js 22 LTS (nodejs.org); install Claude Code in WSL; then git clone https://github.com/sharbelxyz/motion-director ~/src/motion-director && cd ~/src/motion-director && git checkout a21ffbf && mkdir -p ~/.claude/skills && cp -R skills/motion-director ~/.claude/skills/motion-director. Never run install.sh or the curl | bash line. First run: node ~/.claude/skills/motion-director/scripts/check-setup.mjs --fix (downloads pinned hyperframes@0.8.188 and its Chrome into caches only). Keep API keys out of that WSL environment, never set MD_ALLOW_CLOUD=1, and only give brand intake your own site. Hermes: same pinned clone, copy skills/motion-director to ~/.hermes/skills/creative/motion-director (in WSL). claude.ai: no (needs local Node, FFmpeg and Chrome). Android: no.

## YOLO install

YOLO (your own risk): skips the pinned commit, the one-agent copy and the WSL fix. Inside WSL or Linux: curl -fsSL https://raw.githubusercontent.com/sharbelxyz/motion-director/main/install.sh | bash (README.md:26; installs the moving main branch into every agent folder it finds), then say "set up motion director" to your agent.

## Install notes

Ask the user before installing. Safe with the fixes in Safe install applied (WSL2 on Windows, pinned commit a21ffbf, copy into one agent by hand, no API keys, no MD_ALLOW_CLOUD). Renders branded motion graphics, B-roll and transparent overlays locally with pinned HyperFrames; no accounts, nothing uploaded. Possible fit for the faceless video channel's B-roll and overlays.
