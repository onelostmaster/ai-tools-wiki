# impeccable

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://github.com/pbakaus/impeccable
- **GitHub repo:** [https://github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable)
- **Price:** Free (open-source)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @d41d986 (2026-11-16): safe with fixes. Hooks fetch a prebuilt engine checked against engine-checksums.txt (skills/impeccable/scripts/impeccable:14, 73-79). Live mode's Apply runs codex or claude with approvals off (README:72) unless IMPECCABLE_LIVE_COPY_AGENT=chat. Fix: set that, or copy the skill folder only (no hooks). Fits the website project.

## Safe install

Safe install (fixes applied):
Env IMPECCABLE_LIVE_COPY_AGENT=chat; then npx impeccable@4.9.2 install, or copy skills/impeccable at d41d986 into ~/.claude/skills (no hooks); live mode only on a local checkout.

## YOLO install

YOLO (your own risk): skips the Apply switch, so live Apply runs an agent with approvals off.
npx impeccable install with defaults.

## Install notes

Ask the user before installing.
No install steps: the source withholds them until the tool is rated safe. Read the Safety reason and ask the user first.
