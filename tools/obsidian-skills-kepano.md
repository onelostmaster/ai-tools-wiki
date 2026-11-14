# obsidian-skills (kepano)

- **Type:** skill
- **Category:** Notion and productivity
- **Official URL:** https://github.com/kepano/obsidian-skills
- **GitHub repo:** https://github.com/kepano/obsidian-skills @ 3ccff53 (MIT; by Obsidian's CEO)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @3ccff53, a review, 2026-11-02): safe. Markdown only; the defuddle and knap skills tell the agent to `npm install -g` a CLI if missing (`skills/defuddle/SKILL.md:10`, `skills/knap/SKILL.md:10`), so watch for that install prompt.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Claude Code: via /plugin rather than the npx skills CLI (Claude, a review); decline the global npm installs unless approved.
Hermes: plain SKILL.md folders; drop the folder into `~/.hermes/skills/<category>/<skill>/SKILL.md` (<category>/<skill> = any folder names you choose) (README General install).
