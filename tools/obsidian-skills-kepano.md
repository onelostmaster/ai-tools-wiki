# obsidian-skills (kepano)

- **Type:** skill
- **Category:** Notion and productivity
- **Official URL:** https://github.com/kepano/obsidian-skills
- **GitHub repo:** https://github.com/kepano/obsidian-skills @ 3ccff53 (MIT; by Obsidian's CEO)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @3ccff53, a review, 2026-11-02): safe. Markdown only; the defuddle and knap skills tell the agent to `npm install -g` a CLI if missing (`skills/defuddle/SKILL.md:10`, `skills/knap/SKILL.md:10`), so watch for that install prompt.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): /plugin marketplace add kepano/obsidian-skills#3ccff53 (reviewed commit), then /plugin install obsidian@obsidian-skills (README.md:10-11). Fix: the defuddle and knap skills tell the agent to run npm install -g defuddle / npm install -g knap when the CLI is missing (skills/defuddle/SKILL.md:10, skills/knap/SKILL.md:10); this is a global install and it happens only if you approve that Bash call. Decline it, or use npx knap (knap SKILL.md:10) / install defuddle yourself at a pinned version.
Hermes: copy skills/<name> folders from 3ccff53 into ~/.hermes/skills/<category>/.

## YOLO install

YOLO (your own risk): skips the commit pin and declining the global npm installs.
/plugin marketplace add kepano/obsidian-skills, /plugin install obsidian@obsidian-skills, and approve npm install -g defuddle / knap when asked.

## Install notes

Safe, but ask the user before installing.
Claude Code: via /plugin rather than the npx skills CLI (Claude, a review); decline the global npm installs unless approved.
Hermes: plain SKILL.md folders; drop the folder into `~/.hermes/skills/<category>/<skill>/SKILL.md` (<category>/<skill> = any folder names you choose) (README General install).
