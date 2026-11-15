# Vercel

- **Type:** app
- **Category:** building a site, developer tools
- **Official URL:** https://vercel.com
- **GitHub repo:** unknown
- **Price:** Hobby free, personal or non-commercial use only (Vercel Terms of Service, Hobby Plan section, Last Updated 2026-10-19, checked 2026-11-14); Pro $20 per user/month with $20 of usage credit, extra usage billed; Enterprise custom (vercel.com, checked 2026-10-31). Hobby limits: 100 GB fast data transfer, 100 deployments/day, 200 projects (vercel.com/docs/plans/hobby, checked 2026-11-14)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Vercel (official vendor; not code-reviewed: a review bot listed it under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. Vendor docs: it deploys your code to Vercel's hosting under your Vercel account, and the CLI collects telemetry unless you run `vercel telemetry disable` or set `VERCEL_TELEMETRY_DISABLED=1`.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: Git integration, no CLI; or in the project folder `npm install -D -E vercel@65.16.0` with env `VERCEL_TELEMETRY_DISABLED=1`; tokens only as secrets/env vars. Hobby only for personal or non-commercial sites.

## YOLO install

YOLO (your own risk): skips the pinned project-local CLI and telemetry off.
`npm i -g vercel` (Vercel CLI docs).

## Install notes

Ask the user first. No CLI needed with Vercel's Git integration. If a CLI is needed: project-local `npm install -D -E vercel@65.16.0` (not `npm i -g`), env `VERCEL_TELEMETRY_DISABLED=1` (Vercel CLI telemetry docs). Never paste Vercel tokens into chat; add them as secrets/env vars. Hobby is for personal or non-commercial use only (Terms).
