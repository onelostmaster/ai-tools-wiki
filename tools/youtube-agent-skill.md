# YouTube Agent skill

- **Type:** plugin
- **Category:** research, editing
- **Official URL:** https://github.com/Jakeschincariol/youtube-agent-skill
- **GitHub repo:** [https://github.com/Jakeschincariol/youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill)
- **Price:** Free (MIT), no API key
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-09

## Safety reason

a review bot (code read, a2feb21, a project a review, 2026-10-31): Looks safe. No network code, telemetry, subprocess/eval/exec, dependencies, hooks or install scripts; the Python tools only read local files you pass. Skills read and write `~/.claude/youtube/voice.md`; /yt-viral suggests yt-dlp for public listings. Nothing publishes.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `/plugin marketplace add Jakeschincariol/youtube-agent-skill` then `/plugin install youtube-agent`, or copy `skills/yt-*` into `~/.claude/skills/`
Hermes: unconfirmed: copy the `skills/yt-*` folders into a category folder of your choice under `~/.hermes/skills/`, then start a new session
