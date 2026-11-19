# Stitch skills

- **Type:** skill
- **Category:** design, building a site
- **Official URL:** https://github.com/google-labs-code/stitch-skills
- **GitHub repo:** https://github.com/google-labs-code/stitch-skills @ 0337446 (Apache-2.0; plugins stitch-design, stitch-build, stitch-utilities 1.0.0; committed 2026-08-17 16:20 ET per git log, HEAD on 2026-11-08)
- **Price:** Free (Apache-2.0); needs a Google Stitch API key (Stitch pricing unknown, not checked)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (code read @0337446, 2026-11-08, no-intake review): Caution. Official Google Labs repo; plugin.json files declare skills only (no hooks, no bundled MCP config, no install scripts, no telemetry found). Concerns: upload-to-stitch/SKILL.md:32-45 tells the agent to pull the Stitch API key from MCP config files such as ~/.claude.json (which can hold other servers' secrets) and pass it as --api-key, so it lands in the transcript and process list; upload_to_stitch.py (268 lines) then POSTs base64 files to stitch.googleapis.com (lines 89-113), which is its stated job. extract-static-html/scripts/snapshot.ts launches Puppeteer with --no-sandbox (lines 285-288) and can import and run a user-named --auth-script (lines 340-362); extract_inline_html.ts fetches remote images with an SSRF guard (lines 252-286). fetch-stitch.sh and download-stitch-asset.sh are plain curl downloads to a path you give; verify-setup.sh and validate.js only read local files. Remote Stitch MCP service not reviewed. Fix-rule re-rate 2026-11-18: every verified risk has an exact fix in Safe install (copy pinned skill folders, edit upload-to-stitch/SKILL.md:32-45 so the key is never read from ~/.claude.json or passed as --api-key, Puppeteer snapshot only against your own local site and no --auth-script; the remote Stitch MCP service stays an unverified item contained by not connecting it); with those fixes applied: safe.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): copy only the skill folders you need from plugins/*/skills/ of github.com/google-labs-code/stitch-skills pinned at 0337446 into %USERPROFILE%\.claude\\skills\\ instead of the README's npx plugins add route. Edit upload-to-stitch/SKILL.md lines 32-45 so the agent does not read your key out of ~/.claude.json and pass it as --api-key (that puts the key in the transcript and process list); set your Stitch API key yourself in an environment variable instead. extract-static-html launches Puppeteer with --no-sandbox (scripts/snapshot.ts:285-288) and runs any --auth-script you name (:340-362): only point it at your own local dev site and never pass an auth script you did not write. Needs a Google Stitch account and API key. Unverified: the remote Stitch MCP service (Google-hosted, not in the repo); containment: give it a separate Stitch-only key. Hermes: same skill folders copied into its skills folder. Android / claude.ai: not supported.

## YOLO install

YOLO (your own risk): skips copying single folders, the SKILL.md key edit and the own-site rule.
Claude Code (Windows): run the README's npx plugins add command and let upload-to-stitch pull the key from ~/.claude.json.

## Install notes

Ask the user before installing. Safe only with the fixes in Safe install applied.
Decision Skip for now (needs a Google Stitch account and API key; a project rated it 4/10). If you ever want it in Claude Code on Windows: copy only the skill folders you need from plugins/*/skills/ into %USERPROFILE%\.claude\\skills\\ rather than the README's npx plugins add route (a separate installer CLI). Most skills are instructions only. Skip or edit upload-to-stitch: its SKILL.md (lines 32-45) tells the agent to read your API key out of ~/.claude.json and pass it on the command line; give the key yourself in an environment variable instead. extract-static-html runs Puppeteer (downloads Chromium) with --no-sandbox via npx tsx; only point it at your own local dev site. The Stitch MCP server itself is a separate Google remote service, not reviewed here.
