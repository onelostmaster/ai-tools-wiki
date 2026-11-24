# in-your-own-words (Cursor pstack)

- **Type:** skill
- **Category:** prompting, communication
- **Official URL:** https://github.com/cursor/plugins/tree/main/pstack/skills/in-your-own-words
- **GitHub repo:** https://github.com/cursor/plugins/tree/main/pstack/skills/in-your-own-words @ 7a58391
- **Price:** Free (MIT License: pstack/LICENSE and plugin.json license field at 7a58391, checked 2026-11-23).
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-23

## Safety reason

Claude code read @7a58391, 2026-11-23: one 315-byte SKILL.md, no scripts, hooks or network. Verified risk: none. The full pstack plugin (58 skills, 2 agents, automations) was not reviewed; installing it for this one file is not needed. a review bot check 2026-11-23 via the GitHub API at 7a583913: the folder holds only SKILL.md (315 bytes); pstack plugin.json and .cursor-plugin/plugin.json give version 0.15.46 and license MIT; pstack/LICENSE is MIT. SKILL.md:4 sets disable-model-invocation: true, so it runs only when typed as a slash command.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): ask the user first. Copy SKILL.md from https://github.com/cursor/plugins/tree/main/pstack/skills/in-your-own-words at commit 7a58391 into one project's .claude/skills/in-your-own-words/ and type /in-your-own-words. Don't install the whole pstack plugin for it.
Cursor: same single file into the project's skills folder; the full pstack plugin is not reviewed.

## YOLO install

Not written yet.

## Install notes

Ask the user first. Copy SKILL.md into one project's .claude/skills/in-your-own-words/ and type /in-your-own-words. Don't install the whole pstack plugin for it.
