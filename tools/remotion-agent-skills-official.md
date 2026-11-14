# Remotion agent skills (official)

- **Type:** skill
- **Category:** generating videos, editing
- **Official URL:** https://github.com/remotion-dev/skills
- **GitHub repo:** [https://github.com/remotion-dev/skills](https://github.com/remotion-dev/skills)
- **Price:** Free for individuals, organizations of up to 3 people and non-profits; paid tiers: Remotion for Creators $25/mo per seat, Remotion for Automators $0.01 per render ($100/mo minimum), Enterprise from $500/mo (`remotion.dev`, checked 2026-10-31)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a project a review, 2026-10-29; unchanged since 30d4553 per a review): Looks safe. Markdown plus 2 local geo-prep scripts, no network or telemetry. The voiceover guide defaults to paid ElevenLabs, and Remotion itself needs a paid company license for for-profit orgs with 4+ employees.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `npx skills add remotion-dev/skills` (README:12). `npx skills` is an unpinned installer, and the skills CLI sends install telemetry to `skills.sh` unless `DISABLE_TELEMETRY` is set .
