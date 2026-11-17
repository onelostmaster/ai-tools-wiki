# webapp-testing (Anthropic)

- **Type:** skill
- **Category:** developer tools, building a site
- **Official URL:** https://github.com/anthropics/skills/tree/main/skills/webapp-testing
- **GitHub repo:** https://github.com/anthropics/skills @ ca45fc4 (folder skills/webapp-testing; latest commit 2026-10-28)
- **Price:** Free (Apache-2.0, github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (vendor repo read @ca45fc4, a review, 2026-11-02): safe. Anthropic's own skill (Apache-2.0). `scripts/with_server.py:68-71` runs the server command you give it with shell=True, so only pass your own commands.

## Safe install

Safe install (fixes applied):
claude.ai: already built in on paid plans (anthropics/skills README.md:55).
Claude Code (Windows): /plugin marketplace add anthropics/skills, then /plugin install example-skills@anthropic-agent-skills (installs all 12 example skills, .claude-plugin/marketplace.json), or copy only skills/webapp-testing from reviewed commit ca45fc4 into ~/.claude/skills. Fix: scripts/with_server.py:68-71 runs the --server command with shell=True, so only pass your own dev-server commands, never text from a web page or issue. Needs Playwright (pip install playwright, then playwright install chromium). Reviewed commit ca45fc4; HEAD e4bb5d9 not reviewed.

## YOLO install

YOLO (your own risk): skips copying only the one folder.
Install the whole example-skills plugin.

## Install notes

Safe, but ask the user before installing.
claude.ai: already available on paid plans (anthropics/skills `README.md:55`).
Claude Code: `/plugin marketplace add anthropics/skills` then `/plugin install example-skills@anthropic-agent-skills` (`.claude-plugin/marketplace.json`).
