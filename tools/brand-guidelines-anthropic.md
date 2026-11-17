# brand-guidelines (Anthropic)

- **Type:** skill
- **Category:** design
- **Official URL:** https://github.com/anthropics/skills/tree/main/skills/brand-guidelines
- **GitHub repo:** https://github.com/anthropics/skills @ ca45fc4 (folder skills/brand-guidelines; latest commit 2026-10-28)
- **Price:** Free (Apache-2.0, github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (vendor repo read @ca45fc4, a review, 2026-11-02): safe. Anthropic's own skill (Apache-2.0): text only, no scripts, hooks or keys.

## Safe install

Safe install (fixes applied):
claude.ai: already built in on paid plans (anthropics/skills README.md:55), nothing to install.
Claude Code (Windows): copy only skills/brand-guidelines from reviewed commit ca45fc4 into ~/.claude/skills (HEAD is e4bb5d9 on 2026-11-16, not reviewed). Text only, no scripts.
Hermes: copy the same folder into ~/.hermes/skills/<category>/brand-guidelines/ (<category> = any folder name you choose).

## YOLO install

YOLO (your own risk): skips copying only the one folder at the reviewed commit.
/plugin marketplace add anthropics/skills, then /plugin install example-skills@anthropic-agent-skills (installs all 12 example skills at HEAD, .claude-plugin/marketplace.json).

## Install notes

Safe, but ask the user before installing.
claude.ai: already available on paid plans (anthropics/skills `README.md:55`).
Claude Code: `/plugin marketplace add anthropics/skills` then `/plugin install example-skills@anthropic-agent-skills` (`.claude-plugin/marketplace.json`).
