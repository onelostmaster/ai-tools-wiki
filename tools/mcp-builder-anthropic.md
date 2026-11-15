# mcp-builder (Anthropic)

- **Type:** skill
- **Category:** developer tools
- **Official URL:** https://github.com/anthropics/skills/tree/main/skills/mcp-builder
- **GitHub repo:** https://github.com/anthropics/skills @ ca45fc4 (folder skills/mcp-builder; latest commit 2026-10-28)
- **Price:** Free (Apache-2.0, github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

a review bot (vendor repo read @ca45fc4, a review, 2026-11-02): safe. Anthropic's own skill (Apache-2.0): guidance plus `reference/` and `scripts/` for evaluating a server you build; no hooks or keys.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
claude.ai: already available on paid plans (anthropics/skills `README.md:55`).
Claude Code: `/plugin marketplace add anthropics/skills` then `/plugin install example-skills@anthropic-agent-skills` (`.claude-plugin/marketplace.json`).
