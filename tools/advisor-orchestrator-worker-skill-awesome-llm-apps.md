# advisor-orchestrator-worker skill (awesome-llm-apps)

- **Type:** skill
- **Category:** developer tools, automation
- **Official URL:** https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/advisor-orchestrator-worker
- **GitHub repo:** https://github.com/Shubhamsaboo/awesome-llm-apps @ 6c16b23, folder `agent_skills/advisor-orchestrator-worker` (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); worker model calls are paid
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @6c16b23, a review / Hermes a review, 2026-11-02): caution. Workers run the Antigravity CLI with --dangerously-skip-permissions in a temp folder (`agent_skills/advisor-orchestrator-worker/SKILL.md:44-53`); the skill itself says that folder "is not a sandbox". Workers can touch anything your user can.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: only in a throwaway folder or VM; needs the Antigravity CLI (not reviewed). Hermes: same. Android: no.
