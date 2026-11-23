# career-ops

- **Type:** plugin
- **Category:** automation, research
- **Official URL:** https://career-ops.org
- **GitHub repo:** https://github.com/career-ops-hq/career-ops @ cb84a49 (MIT per LICENSE; v1.40.0)
- **Price:** Free (MIT, `github.com`, checked 2026-10-31); you pay your AI provider.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-22

## Safety reason

a review bot read @cb84a49: safe with these fixes. Verified 1: installed as a Claude Code plugin it runs a SessionStart hook every session (hooks/hooks.json:5-11) that runs npm install --omit=dev --ignore-scripts into the plugin data folder whenever the dependency list changed (scripts/claude-plugin-session-start.mjs:68,136-144); the repo ships no package-lock.json and package.json uses ^ ranges, so the installed versions float. Fix: don't use the plugin install; run it from a git checkout at cb84a49 (the hook does nothing in a local checkout, scripts/claude-plugin-session-start.mjs:18-20) and keep the package-lock.json your first install writes. Verified 2: npm install runs a postinstall that downloads Playwright Chromium through npx (package.json:93). Fix: npm install --ignore-scripts, then npx playwright install chromium yourself (playwright is pinned to 1.65.0). Verified 3: AGENTS.md:78-82 tells the agent to run node update-system.mjs check on the first message of every session (calls api.github.com and raw.githubusercontent.com, update-system.mjs:202-212); it applies an update only after you say yes (AGENTS.md:91). Fix: answer no (it runs update-system.mjs dismiss) so you stay on the reviewed commit. Verified 4: it never submits applications: AGENTS.md:529 and a runtime guard that refuses to click submit controls (web/src/lib/apply/drive-action.mjs:6,308-333). Verified 5: keys live in .env (.env.example:10,21,51,68 AI providers; :85 Apify; :89 Notion). Fix: one AI provider key only, no Apify or Notion token. No telemetry found (community-asks.mjs:86 states none; no analytics code).

## Safe install

Safe install (fixes applied):
Claude Code on Windows (PowerShell): git clone https://github.com/career-ops-hq/career-ops C:\\career-ops ; cd C:\\career-ops ; git checkout cb84a494debb13c3bb4e99f5a506ad486dfca514 ; npm install --ignore-scripts ; npx playwright install chromium ; then start claude in C:\\career-ops (local checkout, no /plugin install, so no SessionStart hook). Keep the package-lock.json npm wrote and use npm ci later. Put one AI provider key in .env, no APIFY_TOKEN or NOTION_ACCESS_TOKEN. Say no to the update prompt. Use a copy of your CV only; you click Submit yourself.
claude.ai, Hermes, Android: not supported (it runs in a coding CLI with Node; plugin keywords list Claude Code, Codex and opencode).

## YOLO install

YOLO (your own risk): skips the pinned checkout, the lockfile and the update no. Claude Code: /plugin marketplace add career-ops-hq/career-ops then /plugin install career-ops@career-ops (README); the SessionStart hook then npm-installs floating ^ versions whenever they change, and you may accept updates.

## Install notes

Safe with fixes: a local job-search agent (scan job boards, score roles against your CV, tailor CVs and cover letters, track applications) that never submits anything itself (runtime submit guard). Run it from a checkout at cb84a49, not the plugin install, so no SessionStart npm install runs; npm install --ignore-scripts then install Chromium yourself; say no to update prompts; one AI key only. Your CV goes to the AI provider you pick.
