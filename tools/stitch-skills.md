# Stitch skills

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://github.com/google-labs-code/stitch-skills
- **GitHub repo:** https://github.com/google-labs-code/stitch-skills @ 0337446 (Apache-2.0; plugins stitch-design, stitch-build, stitch-utilities 1.0.0; committed 2026-08-17 16:20 ET per git log, HEAD on 2026-11-08)
- **Price:** Free (Apache-2.0); needs a Google Stitch API key (Stitch pricing unknown, not checked)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-10

## Safety reason

a review bot (code read @0337446, 2026-11-08, no-intake review): Caution. Official Google Labs repo; plugin.json files declare skills only (no hooks, no bundled MCP config, no install scripts, no telemetry found). Concerns: upload-to-stitch/SKILL.md:32-45 tells the agent to pull the Stitch API key from MCP config files such as ~/.claude.json (which can hold other servers' secrets) and pass it as --api-key, so it lands in the transcript and process list; upload_to_stitch.py (268 lines) then POSTs base64 files to stitch.googleapis.com (lines 89-113), which is its stated job. extract-static-html/scripts/snapshot.ts launches Puppeteer with --no-sandbox (lines 285-288) and can import and run a user-named --auth-script (lines 340-362); extract_inline_html.ts fetches remote images with an SSRF guard (lines 252-286). fetch-stitch.sh and download-stitch-asset.sh are plain curl downloads to a path you give; verify-setup.sh and validate.js only read local files. Remote Stitch MCP service not reviewed.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Decision Skip for now (needs a Google Stitch account and API key; a project rated it 4/10). If you ever want it in Claude Code on Windows: copy only the skill folders you need from plugins/*/skills/ into %USERPROFILE%\.claude\\skills\\ rather than the README's npx plugins add route (a separate installer CLI). Most skills are instructions only. Skip or edit upload-to-stitch: its SKILL.md (lines 32-45) tells the agent to read your API key out of ~/.claude.json and pass it on the command line; give the key yourself in an environment variable instead. extract-static-html runs Puppeteer (downloads Chromium) with --no-sandbox via npx tsx; only point it at your own local dev site. The Stitch MCP server itself is a separate Google remote service, not reviewed here.
