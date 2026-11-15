# GitHub Actions (official actions/*)

- **Type:** library
- **Category:** automation, developer tools
- **Official URL:** https://docs.github.com/en/actions
- **GitHub repo:** https://github.com/actions/checkout (v7.0.1) + actions/setup-node (v7.1.0), actions/cache (v6.1.0), actions/upload-artifact (v7.0.2), actions/download-artifact (v8.0.2); pinned by commit SHA
- **Price:** Free for public repos; private repos use included compute (Free plan $12/month, Pro $18) then $0.006/min Linux 2-core; artifact storage 500 MB on Free (docs.github.com, checked 2026-11-08)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Official vendor (GitHub, MIT); a project Claude review (phase1-libraries.md §8, 2026-11-08): safe. Pinned by commit SHA, read-only token (contents: read). Runner minutes and artifact storage bill the repo owner beyond the plan allowance; anyone with write access can run workflows. Not re-read by a review bot.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: nothing to install locally. In `.github/workflows/*.yml` pin each action to its full release commit SHA (`uses: actions/checkout@<40-char sha> # v7.0.1`) and set `permissions: contents: read` at the top of the workflow, as a project does.

## YOLO install

YOLO (your own risk): skips the SHA pins and the read-only token.
`uses: actions/checkout@v7` with the repo's default token permissions.

## Install notes

Claude Code / Windows: reference each action in `.github/workflows/*.yml` pinned to a full commit SHA (`uses: actions/checkout@<full-sha> # v7.0.1`, where <full-sha> is the release commit) with `permissions: contents: read`, as a project does. Nothing to install locally.
