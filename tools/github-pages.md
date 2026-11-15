# GitHub Pages

- **Type:** app
- **Category:** building a site, developer tools
- **Official URL:** https://pages.github.com
- **GitHub repo:** unknown (hosted service); official deploy actions: https://github.com/actions/deploy-pages and https://github.com/actions/upload-pages-artifact
- **Price:** Free for public repos on GitHub Free; private repos need GitHub Pro, Team or Enterprise. Soft limits: 1 GB site, 100 GB/month bandwidth, 10 builds/hour (no build limit with a custom Actions workflow) (docs.github.com GitHub Pages limits, checked 2026-11-14)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Official vendor (GitHub) docs, checked 2026-11-14: safe with the Install notes fixes. Verified: GitHub Pages is not allowed as free hosting for an online business, e-commerce or SaaS, and not for passwords or card numbers (GitHub Pages limits); a free public tools reference fits. Verified risk, fixed: the deploy workflow needs a token; fix: a custom Actions workflow whose deploy job has only `pages: write` and `id-token: write` (docs: Using custom workflows with GitHub Pages), with each action pinned to a full commit SHA, as on the GitHub Actions row.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: nothing to install. In the public repo, a custom workflow using actions/upload-pages-artifact and actions/deploy-pages pinned to full commit SHAs; deploy job `permissions: pages: write, id-token: write` only; upload only the build output folder.

## YOLO install

YOLO (your own risk): skips the SHA pins and the minimal permissions.
Turn on Pages from a branch in the repo settings, or use the starter workflow with tag versions (actions/deploy-pages@v4).

## Install notes

Ask the user first. Nothing to install locally. Publish from the public site repo with a custom Actions workflow: actions/upload-pages-artifact then actions/deploy-pages, each pinned to a full commit SHA, deploy job permissions `pages: write` and `id-token: write` only. Publish only the build output folder.
