# Emil Kowalski skills (emil-design-eng, break-ui, mobile-native)

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://github.com/emilkowalski/skills
- **GitHub repo:** [https://github.com/emilkowalski/skills](https://github.com/emilkowalski/skills)
- **Price:** Free (open-source)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (code read, a81dbca, a project a review): Looks safe. Text-only skills. The README installs them with the skills CLI (`npx skills@latest add emilkowalski/skills`), which sends install telemetry to `skills.sh`. Re-checked 2026-11-01 (a review bot and Claude @a81dbca, a review): animation skills are markdown only, no scripts or network calls; 4 zero-width spaces in `improve-animations/PLAN-TEMPLATE.md` only escape code fences; remove-animations edits code (deletes only).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `npx skills@latest add emilkowalski/skills` (README route; the skills CLI sends install telemetry to `skills.sh`, off with `DISABLE_TELEMETRY` or `DO_NOT_TRACK`). Unconfirmed alternative from a review bot: copy `skills/emil-design-eng/` to `~/.claude/skills/`.
Hermes: no confirmed command yet; follow the official docs at https://github.com/emilkowalski/skills (a review bot's unconfirmed route: copy `skills/emil-design-eng/` to `~/.hermes/skills/design/`).
Claude Code (animation skills only): copy `skills/remove-animations`, `skills/improve-animations` and `skills/animation-performance` into `~/.claude/skills/` (Windows: `%USERPROFILE%\.claude\skills\`) and start a new session (a review bot, a review).
Hermes (animation skills, unconfirmed): copy the same three folders into `~/.hermes/skills/` and start a new session.
