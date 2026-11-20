# Unslop (UI design skill)

- **Type:** skill
- **Category:** design, frontend
- **Official URL:** https://github.com/heydamir/unslop
- **GitHub repo:** https://github.com/heydamir/unslop
- **Price:** Free skill, verified online 2026-11-08 via official GitHub README/LICENSE. CC BY 4.0 (SKILL.md:4,13; README.md:70; LICENSE) allows commercial use with attribution requirements when sharing copied/adapted material; retain original-creator credit, repo/license link and indicate modifications. Not MIT. story.mjs:95 and SKILL.md:207 include a video credit/watermark; preserve applicable attribution. Existing agent/model usage, optional image generation and any dependencies/services have separate costs. No per-run price estimate or paid-service price guessed.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @a6f121e (2026-11-19): safe with fixes. The skill is Markdown plus two optional helpers in skills/unslop/scripts/ (snapshot.mjs runs live pages in Playwright; story.mjs serves a folder and calls ffmpeg -y). Without the scripts folder nothing executes beyond Claude Code's own permission-gated tools. Fix: pinned copy into one project with scripts/ deleted, audit-only first.

## Safe install

Safe install (fixes applied):
Windows Claude Code (Git Bash): git clone https://github.com/heydamir/unslop && cd unslop && git checkout a6f121e, then copy only skills/unslop into one project's .claude/skills/ (not ~/.claude) and delete the copied scripts/ folder so it applies to that project only (README.md:11-18). Start with /unslop in audit-only mode and approve each change. Keep Claude Code's normal permission prompts on (never --dangerously-skip-permissions). Skip the optional Playwright/FFmpeg helpers. If you later want them (separate OK): run snapshot.mjs only on public pages you own, never logged-in apps (it loads the live page and removes script tags only afterwards, snapshot.mjs:35,108); run story.mjs from a dedicated empty folder with public assets only (it serves that folder over 127.0.0.1, story.mjs:360, and deletes/recreates .story-frames, :367); use a fresh output name because ffmpeg runs with -y (:459). Don't connect the image-generation/MCP services references/visuals.md:54-60 suggests. Ignore the macOS brew hint. Keep the CC BY 4.0 credit. claude.ai: paste SKILL.md as guidance. Hermes: untested. Android: view results only.

## YOLO install

YOLO (your own risk): skips the commit pin, project-only scope and audit-first step.
git clone https://github.com/heydamir/unslop && mkdir -p ~/.claude/skills && cp -r unslop/skills/unslop ~/.claude/skills/

## Install notes

CAUTION: not installed; show Safety reason and ask first. Documented only, NOT executed. Claude Code on Windows using Git Bash: git clone https://github.com/heydamir/unslop ; mkdir -p ~/.claude/skills && cp -r unslop/skills/unslop ~/.claude/skills/ (README.md:11-18). For one project copy into .claude/skills/ instead; recommended first trial to limit scope. Invoke /unslop with a specific UI request, e.g. audit only and wait. Optional snapshot/video dependencies (README.md:33-40): npm install -D playwright ; npx playwright install chromium ; ffmpeg separately installed and on PATH. Scripts use Playwright's bundled Chromium when CHROME_PATH/known paths absent; Windows not tested here. Do NOT follow the script's macOS-only brew hint on Windows; select a separately verified Windows FFmpeg distribution only after approval. Codex documented separately; no need to install it for Claude use. claude.ai: no repo-documented upload/packaged-skill workflow verified; Markdown can be supplied as design guidance, but do not promise equivalent local project editing or browser/FFmpeg execution from ordinary browser chat. Hermes: generic SKILL.md is plain Markdown that Hermes can load as guidance, but there are no official Hermes adapter/install instructions here; compatibility untested. Not an MCP server. Android: no native plugin/install route documented; can review generated responsive UI or video on the phone while Windows does the work. No supported Android execution inferred from web output. Before any trial: obtain installation approval; use one project and a Git checkpoint/copy; core audit-only mode first, keep direction approval and normal agent prompts on; preserve brand/accessibility; no automatic dependency installs, MCP connections or paid generation; skip optional scripts initially. If scripts later approved, only public/owned pages, sanitized local story content in a dedicated directory without secrets, controlled network and fresh output paths, no sensitive screenshots or browser profile. Do not run untrusted HTML simply because this is called a skill.
