# Hallmark

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://www.usehallmark.com/
- **GitHub repo:** https://github.com/Nutlope/hallmark @ 4f6a46c (MIT; latest commit on 2026-10-29)
- **Price:** Free (MIT, github.com, checked 2026-11-01); optional AI image generation uses your own Together AI key (paid usage, price unknown)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @4f6a46c) and Claude (@4f6a46c), 2026-11-01: Looks safe. Markdown skill plus local Node scripts. Only outside calls: Together AI image generation when a TOGETHER_API_KEY is set (scripts/imagegen.mjs:6, 52) and photo downloads limited to Wikimedia Commons. scripts/install-hook.mjs edits .claude/settings.json only when run; SKILL.md line 56 has the agent start your project's dev server to screenshot it (fix: approve that command yourself, see Safe install); scripts/capture.mjs itself only opens a URL in headless Chrome (line 88). Installs via unpinned npx skills add.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): copy skills/hallmark from reviewed commit 4f6a46c of github.com/Nutlope/hallmark into %USERPROFILE%\.claude\\skills\\hallmark and start a new session. Needs Node 18+; the render checks and screenshots also need puppeteer-core and a local Chrome (scripts/capture.mjs:54, 88, headless). Leave TOGETHER_API_KEY unset unless you want Together AI image generation (the only outside call besides Wikimedia Commons photos, scripts/imagegen.mjs:6, 52). Do not run scripts/install-hook.mjs: it adds a PostToolUse hook to .claude/settings.json (with --global, %USERPROFILE%\.claude\\settings.json; lines 14-16, 66). SKILL.md line 56 has the agent start your project's dev server to screenshot it: keep Claude Code asking before each command and approve that one only.
Hermes: unconfirmed: copy the same folder into ~/.hermes/skills/<category>/hallmark/.

## YOLO install

YOLO (your own risk): skips the commit pin, the hook opt-out and per-command approval.
npx skills add nutlope/hallmark -g --agent claude-code (README; unpinned third-party installer) or /plugin marketplace add nutlope/hallmark then /plugin install hallmark@hallmark, at HEAD, plus node scripts/install-hook.mjs --global.

## Install notes

Claude Code: `npx skills add nutlope/hallmark -g --agent claude-code` (lands in `~/.claude/skills/hallmark`), or `/plugin marketplace add nutlope/hallmark` then `/plugin install hallmark@hallmark` (README). Needs Node 18+; browser checks also need puppeteer-core and Chrome.
Hermes: unconfirmed: copy `skills/hallmark` into `~/.hermes/skills/` and start a new session.
