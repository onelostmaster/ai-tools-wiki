# Vercel agent-skills (vercel-labs/agent-skills)

- **Type:** skill
- **Category:** building a site, developer tools
- **Official URL:** https://github.com/vercel-labs/agent-skills
- **GitHub repo:** https://github.com/vercel-labs/agent-skills @ 1a2c79d (MIT per README.md:214-216, no LICENSE file)
- **Price:** Free skills (MIT per README); Vercel hosting plans separate (price not checked, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @1a2c79d, a review, 2026-11-02): safe, official vendor. MIT is stated only in `README.md:214-216` (no LICENSE file). The vercel-cli-with-tokens skill uses a Vercel token: keep it in env vars, never on shared pages.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): download the repo at commit 1a2c79d and copy only the skill folders you need from skills/ (9 skills, e.g. react-best-practices, web-design-guidelines) into %USERPROFILE%\.claude\\skills\. This skips the third-party Skills CLI (README.md:174). Verified: web-design-guidelines fetches its rules from the main branch of vercel-labs/web-interface-guidelines at every run (its SKILL.md). Fix: in that SKILL.md replace main with commit 434b7f91364665f2f733b310ec54809bf8f37937 in the URL. vercel-cli-with-tokens uses a Vercel token: keep it in an env var, never in files or shared pages. claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin and the guidelines pin (rules follow main).
npx skills add vercel-labs/agent-skills

## Install notes

Safe, but ask the user before installing.
Claude Code: add the skills you need per its README.
Windows: works in Claude Code on Windows. Android: no.
web-design-guidelines fetches its rules from the main branch of vercel-labs/web-interface-guidelines at every run (its SKILL.md, Guidelines Source). Fix: before installing, replace `main` with commit `434b7f91364665f2f733b310ec54809bf8f37937` in that URL in SKILL.md, and re-review before moving the pin.
