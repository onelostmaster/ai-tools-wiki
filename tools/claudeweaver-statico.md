# claudeweaver (statico)

- **Type:** skill
- **Category:** Notion and productivity, developer tools
- **Official URL:** https://github.com/statico/claudeweaver
- **GitHub repo:** https://github.com/statico/claudeweaver @ 8b62eb5 (MIT; committed 2026-10-25; skill + one Go program)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @8b62eb5, a review, 2026-11-02): safe. Loopback only with host and origin checks (`skills/claudeweaver/main.go:41,44,227-235`); opening it up needs -unsafe-listen-any. The agent watches a log in the background (`SKILL.md:191-211`). New repo (few stars).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Claude Code (Windows): add the skill; needs Go to build (`SKILL.md:20`). claude.ai and Android: no.
