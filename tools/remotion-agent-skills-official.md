# Remotion agent skills (official)

- **Type:** skill
- **Category:** generating videos, editing
- **Official URL:** https://github.com/remotion-dev/skills
- **GitHub repo:** [https://github.com/remotion-dev/skills](https://github.com/remotion-dev/skills)
- **Price:** Free for individuals, organizations of up to 3 people and non-profits; paid tiers: Remotion for Creators $25/mo per seat, Remotion for Automators $0.01 per render ($100/mo minimum), Enterprise from $500/mo (`remotion.dev`, checked 2026-10-31)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read, a project a review, 2026-10-29; unchanged since 30d4553 per a review): Looks safe. Markdown plus 2 local geo-prep scripts, no network or telemetry. The voiceover guide defaults to paid ElevenLabs, and Remotion itself needs a paid company license for for-profit orgs with 4+ employees.

## Safe install

Safe install (fixes applied):
Claude Code (Windows, PowerShell): `$env:DISABLE_TELEMETRY=1; npx skills@1.8.1 add remotion-dev/skills` (README:12; pinned installer version, npm latest checked 2026-11-14; DISABLE_TELEMETRY stops the skills CLI install telemetry to skills.sh, a review, #70). The voiceover guide defaults to paid ElevenLabs: say which voice tool to use. For-profit company with 4+ employees: get the Remotion company license first.

## YOLO install

YOLO (your own risk): skips the installer version pin and the telemetry switch.
npx skills add remotion-dev/skills

## Install notes

Claude Code: `npx skills add remotion-dev/skills` (README:12). `npx skills` is an unpinned installer, and the skills CLI sends install telemetry to `skills.sh` unless `DISABLE_TELEMETRY` is set .
