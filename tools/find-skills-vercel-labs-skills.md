# find-skills (vercel-labs/skills)

- **Type:** skill
- **Category:** developer tools
- **Official URL:** https://github.com/vercel-labs/skills
- **GitHub repo:** [https://github.com/vercel-labs/skills](https://github.com/vercel-labs/skills)
- **Price:** Free (open-source)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude code read @b716f9d (2026-11-14): safe with fixes. Its SKILL.md:100 tells the agent to run npx skills add <owner/repo@skill> -g -y (global, no confirmation): delete that line in a hand copy and deny the command. The skills CLI sends install/find events with the query to skills.sh; off with DISABLE_TELEMETRY=1 or DO_NOT_TRACK=1 (src/telemetry.ts:76).

## Safe install

Safe install (fixes applied):
Hand-copy the skill, delete SKILL.md line 100; deny Bash(npx skills add *) in settings.json; env DISABLE_TELEMETRY=1.

## YOLO install

YOLO (your own risk): skips the deny and telemetry off.
npx skills add vercel-labs/skills@find-skills -g -y.

## Install notes

Ask the user before installing. Hand-copy the skill, delete SKILL.md line 100; deny Bash(npx skills add *) in settings.json; env DISABLE_TELEMETRY=1.
