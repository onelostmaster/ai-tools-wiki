# find-skills (vercel-labs/skills)

- **Type:** skill
- **Category:** developer tools
- **Official URL:** https://github.com/vercel-labs/skills
- **GitHub repo:** [https://github.com/vercel-labs/skills](https://github.com/vercel-labs/skills)
- **Price:** Free (open-source)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, 92a9a34): Use with caution. Its `SKILL.md` tells the agent it can install skills for you with `-g -y`, skipping confirmation. The skills CLI sends install/find events (including the search query) to `skills.sh` (off with `DISABLE_TELEMETRY` or `DO_NOT_TRACK`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

No install steps: the source withholds them until the tool is rated safe. Read the Safety reason and ask the user first.
