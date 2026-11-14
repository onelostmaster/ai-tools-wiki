# Claude Animated Shorts (cartoon-3d-short)

- **Type:** skill
- **Category:** generating videos, 3D and games
- **Official URL:** https://github.com/mromidev/claude-animated-shorts
- **GitHub repo:** https://github.com/mromidev/claude-animated-shorts @ e3b817b (2026-11-01, one commit, MIT, not a fork)
- **Price:** Free, MIT (LICENSE, checked 2026-11-02). Remotion is free for individuals and small companies; bigger companies need a paid license (remotion.dev/license, checked 2026-11-02). Heavy Claude usage (several Opus verifier agents per round).
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @e3b817b, a review, 2026-11-02; Claude confirmed): no network calls, telemetry, eval, hooks or install script; only ffmpeg/ffprobe (`templates/audio/mix.py:189`, `templates/scripts/short_qa.py:19,36`). Caution: ships 1,200 frames from another channel marked private study only (`references/STYLE_BIBLE.md:1-2`), author's personal rules in SKILL.md (`SKILL.md:25,27,80`), Remotion bundles fill the disk (`SKILL.md:148`), one-day-old repo.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing. Claude Code: copy the skill folder into ~/.claude/skills/ (no installer). First strip the author's personal rules from SKILL.md, keep references/ out of any public repo, set REMOTION_TMP to a big drive, and confirm any bundle deletion yourself. Needs your own voice file and the free Kenney CC0 kits (not included). Windows works.
