# claude-content-skills (Ootto)

- **Type:** skill
- **Category:** social posting, research
- **Official URL:** https://github.com/Ootto-AI/claude-content-skills
- **GitHub repo:** [https://github.com/Ootto-AI/claude-content-skills](https://github.com/Ootto-AI/claude-content-skills)
- **Price:** Free (MIT)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @691875a (2026-11-15): safe with fixes. Most of the 58 skills are plain writing guides. Three need leaving out: agent-reach (MUST USE on any URL and tells the agent to follow a live remote install.md, skills/agent-reach/SKILL.md:4-11, 59), content-factory and comment-responder (24/7 unattended public replies and DMs through Composio, content-factory/SKILL.md:42, comment-responder/SKILL.md:48). install.sh only copies files.

## Safe install

Safe install (fixes applied):
Clone at 691875a and copy only the skill folders you want into ~/.claude/skills; leave out agent-reach, content-factory and comment-responder. For web research use the Agent Reach row's Safe install.

## YOLO install

YOLO (your own risk): skips the skill filter, so the agent follows a live remote installer and wires 24/7 auto-replies.
bash install.sh from the repo.

## Install notes

Ask the user before installing. Clone at 691875a and copy only the skill folders you want into ~/.claude/skills; leave out agent-reach, content-factory and comment-responder. For web research use the Agent Reach row's Safe install.
