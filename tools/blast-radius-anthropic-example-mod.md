# Blast Radius (Anthropic example mod)

- **Type:** plugin
- **Category:** developer tools, security
- **Official URL:** https://code.claude.com/docs/en/plugins/mods/overview
- **GitHub repo:** [https://github.com/anthropics/claude-code-playground](https://github.com/anthropics/claude-code-playground) (claude-code/mods/blast-radius, read at 569c528)
- **Price:** Free (Apache-2.0 open-source code)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a review, 569c528, 2026-10-31) and Claude (re-read, a project, 2026-10-31): Looks safe. Apache-2.0 Anthropic example mod. Like all mods, it runs with your permissions. Previews are read-only (file listings, git status/diff/log, `git clean -n`), with no model or network calls. For migrations it runs the project's own status command (e.g. `python3 manage.py showmigrations`). It shells to bash and sleep (Windows: Git Bash on PATH, unconfirmed).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code (local only), Windows: `git clone https://github.com/anthropics/claude-code-playground.git`, `cd claude-code-playground\claude-code\mods`, `claude plugin marketplace add ./`, then `claude plugin install blast-radius@claude-code-playground-mods --scope user` (`mods/README.md`, per a review bot a review).
Claude Code (local only): with nobody at the keyboard it refuses a held command after 10 minutes, so keep it out of unattended runs (Claude, a review).
