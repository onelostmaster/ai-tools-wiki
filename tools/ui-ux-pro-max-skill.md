# ui-ux-pro-max skill

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- **GitHub repo:** [https://github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- **Price:** Free (open-source)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (code read, bf41cbc, a project a review, 2026-10-31): Looks safe. Local CSV design database plus Python search. Optional logo generation sends your prompts to Gemini, AtlasCloud or MuAPI on your own key. Do not copy the optional `stack/` template: it sets `enableAllProjectMcpServers` and `Read(//home/**)`.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill`, then `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill`. Do not copy the optional `stack/` template (see Safety reason).
Hermes: unconfirmed: copy `.claude/skills/ui-ux-pro-max/` to `~/.hermes/skills/design/ui-ux-pro-max/`
All platforms: optional logo generation needs your own Gemini, AtlasCloud or MuAPI key; add it as a secret/env var, never paste keys into chat.
