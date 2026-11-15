# Cloudflare security-audit-skill

- **Type:** skill
- **Category:** security, developer tools
- **Official URL:** https://github.com/cloudflare/security-audit-skill
- **GitHub repo:** https://github.com/cloudflare/security-audit-skill @ c1c8a8c (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (light code read @c1c8a8c, a review, 2026-11-02): safe, official vendor. Validators only read files and paths (`validate-findings.cjs:11-13`); the skill tells the agent to work sandboxed with no network (`SKILL.md:31-35`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Claude Code: add the skill per its README.
Windows: works in Claude Code on Windows. Android: no.
