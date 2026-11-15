# web-artifacts-builder (Anthropic)

- **Type:** skill
- **Category:** building a site
- **Official URL:** https://github.com/anthropics/skills
- **GitHub repo:** [https://github.com/anthropics/skills](https://github.com/anthropics/skills) (Anthropic's official skills repo, per its Agent Skills docs, checked 2026-10-31)
- **Price:** Free
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Anthropic (official first-party skill from `anthropics/skills`; already enabled in the a project project, 2026-10-31): safe. No security findings are recorded.

## Safe install

Safe install (fixes applied):
claude.ai (Windows browser and Android app): built in; nothing to install. Claude Code (Windows): `/plugin marketplace add anthropics/skills` then `/plugin install example-skills@anthropic-agent-skills` (anthropics/skills README:36-48; web-artifacts-builder is in example-skills, .claude-plugin/marketplace.json:40; HEAD 1780c5e read 2026-11-14). The skill's scripts/init-artifact.sh runs `npm install -g pnpm` when pnpm is missing (lines 34-36), a global install: have pnpm on PATH first (`winget install -e --id pnpm.pnpm`) so it never runs. The script then installs Vite, Tailwind and shadcn/ui packages from npm into the new project folder only (lines 59-79, 272-273); it needs bash (Git Bash on Windows).

## YOLO install

YOLO (your own risk): skips installing pnpm yourself first, so the script runs `npm install -g pnpm` globally.
`/plugin marketplace add anthropics/skills` then `/plugin install example-skills@anthropic-agent-skills`

## Install notes

claude.ai: built in; nothing to install (already enabled in the a project project).
Claude Code: /plugin marketplace add anthropics/skills, then /plugin install example-skills@anthropic-agent-skills (anthropics/skills README:36-48, checked 2026-11-14). scripts/init-artifact.sh:34-36 runs npm install -g pnpm when pnpm is missing; install pnpm first to avoid the global install.
