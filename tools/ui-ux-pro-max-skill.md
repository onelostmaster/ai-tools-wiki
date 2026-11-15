# ui-ux-pro-max skill

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- **GitHub repo:** [https://github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- **Price:** Free (open-source)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read, bf41cbc, a project a review, 2026-10-31): Looks safe. Local CSV design database plus Python search. Optional logo generation sends your prompts to Gemini, AtlasCloud or MuAPI on your own key. Do not copy the optional `stack/` template: it sets `enableAllProjectMcpServers` and `Read(//home/**)`.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill` then `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill` (README.md:262-263; HEAD d643997, version 2.15.0, checked 2026-11-14). Do not copy the stack/ folder into a project: stack/.claude/settings.json:3 sets enableAllProjectMcpServers true and :9 allows Read(//home/**), and stack/.mcp.json runs three unpinned @latest npx servers. Optional logo and mockup generation sends prompts to Gemini on your own key: set it as an environment variable, never paste it into chat. Hermes: unconfirmed route, copy the skill folder to ~/.hermes/skills/design/ui-ux-pro-max/. claude.ai and Android: no install route recorded.

## YOLO install

YOLO (your own risk): skips leaving out the stack/ template (auto-enables its project MCP servers and allows reading your home folder).
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill, then copy stack/ into the project as stack/docs/SETUP.md describes.

## Install notes

Claude Code: `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill`, then `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill`. Do not copy the optional `stack/` template (see Safety reason).
Hermes: unconfirmed: copy `.claude/skills/ui-ux-pro-max/` to `~/.hermes/skills/design/ui-ux-pro-max/`
All platforms: optional logo generation needs your own Gemini, AtlasCloud or MuAPI key; add it as a secret/env var, never paste keys into chat.
