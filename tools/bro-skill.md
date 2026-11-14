# /bro skill

- **Type:** skill
- **Category:** research
- **Official URL:** https://github.com/luchasarie/bro-skill
- **GitHub repo:** [https://github.com/luchasarie/bro-skill](https://github.com/luchasarie/bro-skill)
- **Price:** Free (open-source code)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a review, 2026-10-29): Looks safe. `SKILL.md` is a pure prompt that says never use tools and treat pasted text as data. `install.sh` only copies `SKILL.md` into agent skill folders (the curl one-liner path downloads it from `raw.githubusercontent.com`). No code, network or secrets otherwise.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `git clone https://github.com/luchasarie/bro-skill.git && cd bro-skill && ./install.sh` (only copies `SKILL.md`), then restart the session
Hermes: unconfirmed: the same `install.sh` if it detects Hermes, or copy `SKILL.md` to `~/.hermes/skills/<category>/bro/` (`<category>` is any Hermes skill category folder)
