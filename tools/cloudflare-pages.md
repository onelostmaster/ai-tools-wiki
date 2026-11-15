# Cloudflare Pages

- **Type:** app
- **Category:** building a site, developer tools
- **Official URL:** https://pages.cloudflare.com
- **GitHub repo:** unknown (hosted service); its CLI Wrangler: https://github.com/cloudflare/workers-sdk (Apache-2.0; skills-install flow read @4335eac)
- **Price:** Free plan: 500 builds/month, 1 build at a time, 20,000 files per site, 25 MiB per file, 100 projects per account; Pro and Business raise build limits (developers.cloudflare.com/pages/platform/limits, checked 2026-11-14)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Official vendor (Cloudflare) docs, checked 2026-11-14, plus a review bot read of Wrangler's agent-skills install flow @4335eac: safe with the Install notes fixes. Verified risks, each fixed: the Cloudflare GitHub app can be given all your repos (fix: choose "Only select repositories", Cloudflare GitHub integration docs); Wrangler sends usage telemetry, including which AI coding agent ran it (fix: DO_NOT_TRACK=1, which takes precedence over every other setting, packages/wrangler/telemetry.md); Wrangler asks once, in an interactive terminal with a detected agent and never in CI, to install Cloudflare skills into your agents, then offers skill updates (fix: answer No, and set WRANGLER_NO_SKILLS_UPDATE_PROMPTS=true; packages/wrangler/src/agents-skills-install.ts:108-145,164,371). unverified: Cloudflare's hosted build servers; contain: no secrets in the repo or the build settings, since the build output is a public site.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: nothing to install; connect only the Wiki website repo through Cloudflare's Git integration ("Only select repositories"); no secrets in the repo or build settings.
Only if a CLI is needed: in the project folder `npm install -D -E wrangler@4.162.0`; env `DO_NOT_TRACK=1` and `WRANGLER_NO_SKILLS_UPDATE_PROMPTS=true`; answer No to Wrangler's one-time "install Cloudflare skills" prompt.

## YOLO install

YOLO (your own risk): skips single-repo GitHub access, the pinned project-local Wrangler, telemetry off and the No to the skills prompt.
Connect GitHub with "All repositories"; `npm i -g wrangler` and accept its prompts.

## Install notes

Ask the user first. No local install for the Wiki website: connect only the site's repo through Cloudflare's Git integration, choosing "Only select repositories" when GitHub asks. Keep secrets out of the repo. Only if a CLI is needed: project-local `npm install -D -E wrangler@4.162.0`, env `DO_NOT_TRACK=1` and `WRANGLER_NO_SKILLS_UPDATE_PROMPTS=true`, and answer No to the skills prompt.
