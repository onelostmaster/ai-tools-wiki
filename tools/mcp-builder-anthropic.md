# mcp-builder (Anthropic)

- **Type:** skill
- **Category:** developer tools
- **Official URL:** https://github.com/anthropics/skills/tree/main/skills/mcp-builder
- **GitHub repo:** https://github.com/anthropics/skills @ ca45fc4 (folder skills/mcp-builder; latest commit 2026-10-28)
- **Price:** Free (Apache-2.0, github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (vendor repo read @ca45fc4, a review, 2026-11-02): safe. Anthropic's own skill (Apache-2.0): guidance plus `reference/` and `scripts/` for evaluating a server you build; no hooks or keys.

## Safe install

Safe install (fixes applied):
claude.ai: already built in on paid plans (anthropics/skills README.md:55), nothing to install.
Claude Code (Windows): copy only skills/mcp-builder from reviewed commit ca45fc4 into ~/.claude/skills (HEAD is e4bb5d9 on 2026-11-16, not reviewed). The optional scripts/evaluation.py needs pip install anthropic mcp (scripts/requirements.txt) in its own venv, uses your ANTHROPIC_API_KEY from env (evaluation.py:228) and starts whatever -c/-a command you give it for stdio (evaluation.py:311-349, connections.py:76-84): only point it at your own server.
Hermes: copy the same folder into ~/.hermes/skills/<category>/mcp-builder/ (<category> = any folder name you choose).

## YOLO install

YOLO (your own risk): skips copying only the one folder at the reviewed commit.
/plugin marketplace add anthropics/skills, then /plugin install example-skills@anthropic-agent-skills (installs all 12 example skills at HEAD, .claude-plugin/marketplace.json).

## Install notes

Safe, but ask the user before installing.
claude.ai: already available on paid plans (anthropics/skills `README.md:55`).
Claude Code: `/plugin marketplace add anthropics/skills` then `/plugin install example-skills@anthropic-agent-skills` (`.claude-plugin/marketplace.json`).
