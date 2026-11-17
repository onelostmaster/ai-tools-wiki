# grill-me (mattpocock/skills)

- **Type:** skill
- **Category:** developer tools
- **Official URL:** https://github.com/mattpocock/skills
- **GitHub repo:** https://github.com/mattpocock/skills @ 4ae2317 (MIT; folders `skills/productivity/grill-me` and grilling)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @4ae2317, a review, 2026-11-02): safe. Markdown only; disable-model-invocation, so it runs only when you type /grill-me. The --skill grill-me install gets only a stub (`skills/productivity/grill-me/SKILL.md:7`), so install grilling too.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): copy skills/productivity/grill-me and skills/productivity/grilling from reviewed commit 4ae2317 into ~/.claude/skills (grill-me alone is only a stub, skills/productivity/grill-me/SKILL.md:7). Runs only when you type /grill-me (disable-model-invocation).
Hermes: copy the same two folders into ~/.hermes/skills/<category>/.

## YOLO install

YOLO (your own risk): skips copying only the two folders at the reviewed commit; the plugin updates itself from main (README.md:27).
claude plugin install mattpocock-skills@claude-plugins-official (README.md:35).

## Install notes

Safe, but ask the user before installing.
Claude Code: install both grill-me and grilling (the /plugin route avoids the npx skills CLI).
Hermes: plain SKILL.md folders; drop the folder into `~/.hermes/skills/<category>/<skill>/SKILL.md` (<category>/<skill> = any folder names you choose) (README General install).
