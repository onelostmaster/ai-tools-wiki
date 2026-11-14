# Hallmark

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://www.usehallmark.com/
- **GitHub repo:** https://github.com/Nutlope/hallmark @ 4f6a46c (MIT; latest commit on 2026-10-29)
- **Price:** Free (MIT, github.com, checked 2026-11-01); optional AI image generation uses your own Together AI key (paid usage, price unknown)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (code read @4f6a46c) and Claude (@4f6a46c), 2026-11-01: Looks safe. Markdown skill plus local Node scripts. Only outside calls: Together AI image generation when a TOGETHER_API_KEY is set (`scripts/imagegen.mjs:6, 52`) and photo downloads limited to Wikimedia Commons. `scripts/install-hook.mjs` edits `.claude/settings.json` only when run; may start your dev server to screenshot it. Installs via unpinned `npx skills add`.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `npx skills add nutlope/hallmark -g --agent claude-code` (lands in `~/.claude/skills/hallmark`), or `/plugin marketplace add nutlope/hallmark` then `/plugin install hallmark@hallmark` (README). Needs Node 18+; browser checks also need puppeteer-core and Chrome.
Hermes: unconfirmed: copy `skills/hallmark` into `~/.hermes/skills/` and start a new session.
