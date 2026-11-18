# GitHub CLI (gh)

- **Type:** CLI
- **Category:** developer tools
- **Official URL:** https://cli.github.com
- **GitHub repo:** unknown
- **Price:** Free, open source (`docs.github.com`, checked 2026-10-31); needs a GitHub account
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-17

## Safety reason

GitHub (official vendor; not code-reviewed: a review bot listed GitHub CLI under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. Vendor docs: `gh auth login` signs in to your GitHub account (or gh uses a `GITHUB_TOKEN` env var), and extensions from outside GitHub are not certified by GitHub, so audit an extension's code before installing it.

## Safe install

Safe install (fixes applied):
Windows: winget install --id GitHub.cli (cli.github.com). Sign in with gh auth login in the browser flow; do not paste tokens into chat (a GITHUB_TOKEN env var works too). Install no gh extensions you have not read: extensions are not certified by GitHub (gh manual).
Claude Code: same; ask Claude to use read-only gh commands unless you want it to push or open PRs.

## YOLO install

YOLO (your own risk): skips the extension and read-only limits.
winget install --id GitHub.cli, gh auth login, and install extensions as you like.

## Install notes

Claude Code: no confirmed command yet; follow the official docs at [https://cli.github.com/manual/](https://cli.github.com/manual/)
Claude Code: sign in with `gh auth login` or a `GITHUB_TOKEN` env var (gh manual); never paste tokens into chat, add them as secrets/env vars.
