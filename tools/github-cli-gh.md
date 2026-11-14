# GitHub CLI (gh)

- **Type:** CLI
- **Category:** developer tools
- **Official URL:** https://cli.github.com
- **GitHub repo:** unknown
- **Price:** Free, open source (`docs.github.com`, checked 2026-10-31); needs a GitHub account
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-02

## Safety reason

GitHub (official vendor; not code-reviewed: a review bot listed GitHub CLI under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. Vendor docs: `gh auth login` signs in to your GitHub account (or gh uses a `GITHUB_TOKEN` env var), and extensions from outside GitHub are not certified by GitHub, so audit an extension's code before installing it.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: no confirmed command yet; follow the official docs at [https://cli.github.com/manual/](https://cli.github.com/manual/)
Claude Code: sign in with `gh auth login` or a `GITHUB_TOKEN` env var (gh manual); never paste tokens into chat, add them as secrets/env vars.
