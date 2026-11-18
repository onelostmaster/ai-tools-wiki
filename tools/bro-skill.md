# /bro skill

- **Type:** skill
- **Category:** research
- **Official URL:** https://github.com/luchasarie/bro-skill
- **GitHub repo:** [https://github.com/luchasarie/bro-skill](https://github.com/luchasarie/bro-skill)
- **Price:** Free (open-source code)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, a review, 2026-10-29): Looks safe. `SKILL.md` is a pure prompt that says never use tools and treat pasted text as data. `install.sh` only copies `SKILL.md` into agent skill folders (the curl one-liner path downloads it from `raw.githubusercontent.com`). No code, network or secrets otherwise.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): git clone https://github.com/luchasarie/bro-skill.git, then copy SKILL.md to %USERPROFILE%\.claude\\skills\\bro\\SKILL.md and restart the session (install.sh only does this copy; a review). This skips the curl one-liner. Pure prompt, no code. Hermes: copy SKILL.md to ~/.hermes/skills/<category>/bro/.

## YOLO install

YOLO (your own risk): skips the manual copy.
The README curl one-liner or ./install.sh.

## Install notes

Claude Code: `git clone https://github.com/luchasarie/bro-skill.git && cd bro-skill && ./install.sh` (only copies `SKILL.md`), then restart the session
Hermes: unconfirmed: the same `install.sh` if it detects Hermes, or copy `SKILL.md` to `~/.hermes/skills/<category>/bro/` (`<category>` is any Hermes skill category folder)
