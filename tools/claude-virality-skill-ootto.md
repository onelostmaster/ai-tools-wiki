# claude-virality-skill (Ootto)

- **Type:** skill
- **Category:** social posting
- **Official URL:** https://github.com/Ootto-AI/claude-virality-skill
- **GitHub repo:** [https://github.com/Ootto-AI/claude-virality-skill](https://github.com/Ootto-AI/claude-virality-skill)
- **Price:** Free (MIT)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, 542ed54, a review): Looks safe. Text only, no code; the Ootto upsell is only in the README and the skill works without it.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): git clone https://github.com/Ootto-AI/claude-virality-skill, git checkout 542ed54 (the reviewed commit, a review), then copy the virality folder to %USERPROFILE%\.claude\\skills\\virality. Text only, no code; the Ootto upsell is only in the README.

## YOLO install

YOLO (your own risk): skips the commit pin.
git clone https://github.com/Ootto-AI/claude-virality-skill && copy claude-virality-skill\\virality to %USERPROFILE%\.claude\\skills\\ (follows main).

## Install notes

Claude Code: `git clone https://github.com/Ootto-AI/claude-virality-skill && cp -r claude-virality-skill/virality ~/.claude/skills/`
Hermes: `hermes skills install Ootto-AI/claude-virality-skill/virality` (the source marks this command unconfirmed)
