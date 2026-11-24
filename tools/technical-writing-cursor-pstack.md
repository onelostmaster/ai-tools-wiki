# technical-writing (Cursor pstack)

- **Type:** skill
- **Category:** writing, documentation
- **Official URL:** https://github.com/cursor/plugins/tree/main/pstack/skills/technical-writing
- **GitHub repo:** https://github.com/cursor/plugins/tree/main/pstack/skills/technical-writing @ 7a58391
- **Price:** Free (MIT License: pstack/LICENSE and plugin.json license field at 7a58391, checked 2026-11-23).
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-23

## Safety reason

Claude code read @7a58391, 2026-11-23: one 4.4 KB SKILL.md, text only. Verified risk: none. a review bot check 2026-11-23 via the GitHub API at 7a583913: the folder holds only SKILL.md (4437 bytes); pstack plugin.json and .cursor-plugin/plugin.json give version 0.15.46 and license MIT; pstack/LICENSE is MIT. SKILL.md:4 sets disable-model-invocation: true; SKILL.md:67 calls the unslop skill.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): ask the user first. Copy this SKILL.md and the pstack unslop SKILL.md, both at commit 7a58391, together into one project's .claude/skills/technical-writing/ and .claude/skills/unslop/ (it calls unslop, SKILL.md:67).
Cursor: same two files; the full pstack plugin is not reviewed.

## YOLO install

Not written yet.

## Install notes

Ask the user first. Copy SKILL.md and the pstack unslop SKILL.md together (it calls unslop, SKILL.md:67) into one project's .claude/skills/.
