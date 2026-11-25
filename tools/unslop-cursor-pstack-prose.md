# unslop (Cursor pstack, prose)

- **Type:** skill
- **Category:** writing, communication
- **Official URL:** https://github.com/cursor/plugins/tree/main/pstack/skills/unslop
- **GitHub repo:** https://github.com/cursor/plugins/tree/main/pstack/skills/unslop @ 7a58391
- **Price:** Free (MIT License: pstack/LICENSE and plugin.json license field at 7a58391, checked 2026-11-23).
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-24

## Safety reason

Claude code read @7a58391, 2026-11-23: one 2.4 KB SKILL.md, text only. Verified risk: none. a review bot check 2026-11-23 via the GitHub API at 7a583913: the folder holds only SKILL.md (2380 bytes); pstack plugin.json and .cursor-plugin/plugin.json give version 0.15.46 and license MIT; pstack/LICENSE is MIT. SKILL.md:4 sets disable-model-invocation: true.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): ask the user first. Copy SKILL.md from https://github.com/cursor/plugins/tree/main/pstack/skills/unslop at commit 7a58391 into one project's .claude/skills/unslop/. Its rule 24 (SKILL.md:31) allows one hedge word in prose; in this wiki the fix rule wins: every risk is stated definitely.
Cursor: same single file; the full pstack plugin is not reviewed.

## YOLO install

Not written yet.

## Install notes

Ask the user first. Copy SKILL.md into one project's .claude/skills/unslop/. Its rule 24 allows one hedge word in prose; in this wiki the fix rule wins: every risk is stated definitely.
