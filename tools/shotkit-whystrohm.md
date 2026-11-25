# Shotkit (whystrohm)

- **Type:** plugin
- **Category:** generating videos, editing
- **Official URL:** https://whystrohm.com/shotkit
- **GitHub repo:** https://github.com/whystrohm/shotkit @ 947959e (v3.8.0, Apache-2.0)
- **Price:** Free on GitHub, Apache-2.0 (github.com, checked 2026-11-23); fal generation is paid per job (price not checked)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-24

## Safety reason

a review bot read @947959e: safe with these fixes. Plugin manifests declare no hooks and no MCP servers (.claude-plugin/plugin.json). No telemetry found. Verified 1: generation sends your prompts and frames to fal.ai and bills your fal account, but only with --yes; without it, it prints the plan and price link and sends nothing (tools/generate.py:668, 700-705); the key comes from FAL_KEY or a .env file (generate.py:96-106). Fix: run without --yes first, and use a separate fal key with a low credit limit kept in the project .env (never commit it). Verified 2: the plugin and install routes are unpinned (README.md:155-166), and ./install.sh writes to ~/.claude by default (install.sh:41) unless --project (install.sh:50). Fix: clone and check out 947959e, then ./install.sh --project (or /plugin marketplace add on that local clone path). Verified 3: tools/sk installs unpinned pyyaml and jsonschema into tools/.venv on first use (tools/sk:53). Fix: create that venv yourself and pip install pinned versions, or use --no-deps (install.sh:27) and skip the validators. Verified 4: boards, design cards and exports fetch Google Fonts; only font family names are requested. Fix: none needed; allow fonts.googleapis.com or work offline with fallback fonts. Verified 5: design and export render stills with headless Chrome and retry with --no-sandbox if the first try fails (design.py:209-214, export.py:146-155); the page is your own local plan. Fix: render only boards you made yourself. Other: bash scripts (install.sh, tools/sk); Canvas is a separate macOS-only download (README.md:101), so skip it. Apache-2.0.

## Safe install

Safe install (fixes applied):
Windows + Claude Code: install Python 3.10+, Git and Chrome from their official sites (ffmpeg only if you export clips). In Git Bash or WSL2: git clone https://github.com/whystrohm/shotkit ; cd shotkit ; git checkout 947959eea6281ad7625d6a011d764428028d8043 ; ./install.sh --project --no-deps (from your project folder) ; then, if you want the validators, run python -m venv .claude/shotkit-tools/.venv and install pinned pyyaml and jsonschema into it (pip install pyyaml==<version> jsonschema==<version>). For generation, run tools/generate.py without --yes to see the plan and price, then add --yes with a separate low-credit FAL_KEY in the project .env. Skip Canvas (macOS only). Keep normal permission prompts on.
claude.ai, Hermes, Android: not supported (needs local Python and Claude Code or Codex).

## YOLO install

YOLO (your own risk): skips the pinned commit, project scope and pinned validators. In Claude Code: /plugin install shotkit --marketplace whystrohm/shotkit (older: /plugin marketplace add whystrohm/shotkit then /plugin install shotkit@shotkit), or clone and ./install.sh (installs to ~/.claude). Put your FAL_KEY in .env and generate with --yes.

## Install notes

Safe with fixes: Claude Code/Codex plugin that plans on-brand video shot by shot; paid fal generation only after --yes. Pin commit 947959e, ./install.sh --project, pinned validator venv or --no-deps, Git Bash or WSL2 on Windows, separate low-credit fal key, skip the macOS Canvas. Fits the faceless video channel idea.
