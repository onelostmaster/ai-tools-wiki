# Logo Design Skill

- **Type:** skill
- **Category:** design
- **Official URL:** https://github.com/kaankiziltug/logo-design-skill
- **GitHub repo:** [https://github.com/kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)
- **Price:** Free (MIT); model tokens only
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, a project a review, 7340903): Looks safe. No network calls, telemetry, eval/exec, obfuscation, postinstall, hooks or install scripts; `SKILL.md` has no prompt injection. The only shell-outs are local SVG-to-PNG renderers (cairosvg, rsvg-convert, Inkscape, headless Chrome with a throwaway profile, Quick Look).

## Safe install

Safe install (fixes applied):
Claude Code: git clone https://github.com/kaankiziltug/logo-design-skill.git, git checkout 7340903 (the reviewed commit, a review), then copy skills/logo-design to %USERPROFILE%\.claude\\skills\\logo-design (README:49-57). Needs Python 3 and one SVG renderer (cairosvg is enough); no keys, no network.

## YOLO install

YOLO (your own risk): skips the commit pin.
/plugin marketplace add kaankiziltug/logo-design-skill then /plugin install logo-design@logo-design-skill (README:49-57; follows main).

## Install notes

[claude.ai](http://claude.ai): no confirmed command yet; follow the official docs at [https://github.com/kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)
Claude Code: `/plugin marketplace add kaankiziltug/logo-design-skill` then `/plugin install logo-design@logo-design-skill`, or `git clone https://github.com/kaankiziltug/logo-design-skill.git && cp -r logo-design-skill/skills/logo-design ~/.claude/skills/logo-design` (README:49-57). Needs Python 3 plus one SVG renderer.
Hermes: unconfirmed (a review bot): copy `skills/logo-design` to `~/.hermes/skills/creative/logo-design/`, then start a new session.
