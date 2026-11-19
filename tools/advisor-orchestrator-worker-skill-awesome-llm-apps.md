# advisor-orchestrator-worker skill (awesome-llm-apps)

- **Type:** skill
- **Category:** developer tools, automation
- **Official URL:** https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/advisor-orchestrator-worker
- **GitHub repo:** https://github.com/Shubhamsaboo/awesome-llm-apps @ 6c16b23, folder `agent_skills/advisor-orchestrator-worker` (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); worker model calls are paid
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Claude code read @14c5f8f (2026-11-18): caution. Every worker runs agy --dangerously-skip-permissions (agent_skills/advisor-orchestrator-worker/SKILL.md:47-50); the skill says the flag is required headless and the temp dir "is not a sandbox" (:54-56). No fix: the skill cannot run with approvals on; only a disposable VM contains it.

## Safe install

Safe install (fixes applied):
Only in a disposable VM with no personal files or keys beyond a capped Antigravity login; copy the folder from commit 14c5f8f.

## YOLO install

YOLO (your own risk): skips the VM.
Copy the skill into your main Claude Code and let workers run with skip-permissions.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: only in a throwaway folder or VM; needs the Antigravity CLI (not reviewed). Hermes: same. Android: no.
