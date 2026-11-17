# Cloudflare security-audit-skill

- **Type:** skill
- **Category:** security, developer tools
- **Official URL:** https://github.com/cloudflare/security-audit-skill
- **GitHub repo:** https://github.com/cloudflare/security-audit-skill @ c1c8a8c (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @c1c8a8c, a review, 2026-11-02): safe, official vendor. Validators only read files and paths (`validate-findings.cjs:11-13`); the skill tells the agent to work sandboxed with no network (`SKILL.md:31-35`).

## Safe install

Safe install (fixes applied):
Claude Code (Windows): download the repo at commit c1c8a8c and copy the folder skills/security-audit into %USERPROFILE%\.claude\\skills\\ (or the project's .claude\\skills). This skips the third-party Skills CLI (README.md:51-56 uses npx skills add). Needs Node.js for its validators, which only read files (validate-findings.cjs:11-13). Verified: it runs the target's builds and tests only inside an OS sandbox with networking off; without one it leaves findings as needs_validation (README.md:86-90, SKILL.md:31-35). Fix: audit only code you own, and give it a sandbox (devcontainer or VM, no network, no keys) if you want findings confirmed. Reports go to ~/security-audit-skill/<repo>/run-N by default (README.md). claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin and the sandbox.
npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit --global

## Install notes

Safe, but ask the user before installing.
Claude Code: add the skill per its README.
Windows: works in Claude Code on Windows. Android: no.
