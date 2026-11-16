# claudeweaver (statico)

- **Type:** skill
- **Category:** Notion and productivity, developer tools
- **Official URL:** https://github.com/statico/claudeweaver
- **GitHub repo:** https://github.com/statico/claudeweaver @ 8b62eb5 (MIT; committed 2026-10-25; skill + one Go program)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (code read @8b62eb5, a review, 2026-11-02): safe. Loopback only with host and origin checks (`skills/claudeweaver/main.go:41,44,227-235`); opening it up needs -unsafe-listen-any. The agent watches a log in the background (`SKILL.md:191-211`). New repo (few stars).

## Safe install

Safe install (fixes applied):
Windows Claude Code: install Go 1.22 or later (SKILL.md:17), git clone https://github.com/statico/claudeweaver and git checkout 8b62eb5 (reviewed; still HEAD on 2026-11-15), and copy skills/claudeweaver to %USERPROFILE%\.claude\\skills\\claudeweaver. Skip the Tailscale phone overlay and the iOS Shortcut. Not a claude.ai, Hermes or Android tool.

## YOLO install

YOLO (your own risk): skips the commit pin.
npx skills add statico/claudeweaver (README.md:20)

## Install notes

Safe, but ask the user before installing.
Claude Code (Windows): add the skill; needs Go to build (`SKILL.md:20`). claude.ai and Android: no.
