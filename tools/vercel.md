# Vercel

- **Type:** app
- **Category:** building a site, developer tools
- **Official URL:** https://vercel.com
- **GitHub repo:** unknown
- **Price:** Hobby free (personal, non-commercial use only); Pro $20 per user/month with $20 of usage credit, extra usage billed; Enterprise custom (`vercel.com`, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-10-31

## Safety reason

Vercel (official vendor; not code-reviewed: a review bot listed it under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. Vendor docs: it deploys your code to Vercel's hosting under your Vercel account, and the CLI collects telemetry unless you run `vercel telemetry disable` or set `VERCEL_TELEMETRY_DISABLED=1`.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `npm i -g vercel` (Vercel CLI, official npm package `vercel`); docs at [https://vercel.com/docs/cli](https://vercel.com/docs/cli)
Claude Code: turn off CLI telemetry with `vercel telemetry disable` or `VERCEL_TELEMETRY_DISABLED=1` (Vercel docs); never paste Vercel tokens into chat, add them as secrets/env vars.
