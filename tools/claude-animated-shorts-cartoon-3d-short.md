# Claude Animated Shorts (cartoon-3d-short)

- **Type:** skill
- **Category:** generating videos, 3D and games
- **Official URL:** https://github.com/mromidev/claude-animated-shorts
- **GitHub repo:** https://github.com/mromidev/claude-animated-shorts @ e3b817b (2026-11-01, one commit, MIT, not a fork)
- **Price:** Free, MIT (LICENSE, checked 2026-11-02). Remotion is free for individuals and small companies; bigger companies need a paid license (remotion.dev/license, checked 2026-11-02). Heavy Claude usage (several Opus verifier agents per round).
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot code read @e3b817b, re-checked by Claude (2026-11-16): safe with fixes, Skip. No network, telemetry, eval, hooks or installer. It ships 1,200 frames from another channel marked private study only (references/STYLE_BIBLE.md:1-2): keep references/ local and out of any public repo. Fix the rest too: strip the author's rules (SKILL.md:25, 27, 80), set REMOTION_TMP to a big drive (SKILL.md:148).

## Safe install

Safe install (fixes applied):
Copy the skill at e3b817b into ~/.claude/skills; delete the author's personal rules at SKILL.md:25, 27 and 80; keep references/ local and private; set REMOTION_TMP to a big drive; confirm any bundle deletion yourself.

## YOLO install

YOLO (your own risk): skips the edits and the private references rule.
Copy the folder as is.

## Install notes

Ask the user before installing. Claude Code: copy the skill folder into ~/.claude/skills/ (no installer). First strip the author's personal rules from SKILL.md, keep references/ out of any public repo, set REMOTION_TMP to a big drive, and confirm any bundle deletion yourself. Needs your own voice file and the free Kenney CC0 kits (not included). Windows works.
