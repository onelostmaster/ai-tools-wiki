# Social Media Skills (charlie947)

- **Type:** skill
- **Category:** social posting
- **Official URL:** https://github.com/charlie947/social-media-skills
- **GitHub repo:** https://github.com/charlie947/social-media-skills @ 10ca79c (MIT; plugin 1.1.0; HEAD on 2026-11-12; 17 skills; not the same as the 106-skill "Social Media Skills" row)
- **Price:** Free (MIT LICENSE, checked at commit 10ca79c on 2026-11-12); Apify and Gemini usage, if you use reels-scripting, is billed by them.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-12

## Safety reason

a review bot (code read @10ca79c, 2026-11-12, no-intake review): Safe. The plugin is 17 markdown skills and nothing else: no hooks, no MCP server, no commands, agents or scripts in skills/ (.claude-plugin/marketplace.json). Every skill carries the same guard lines: never print credentials, and drafting or saving never authorises publishing, sending or account changes (e.g. post-writer SKILL.md line 15). Network use is only on request: reels-scripting has the agent write a small Node script that calls Apify's Instagram Reel scraper and Gemini 2.5 Flash with your own keys, asks before costs and skips comments (SKILL.md lines 22-60); niche-research browses Reddit, X and Google for the last 7 days (lines 51-70). voice-builder writes about-me.md and voice.md in your project. Caveat: the marketplace source is the repo root, so the author's test script (runs a Codex app-server) and validate-skills.sh are copied too, but nothing calls them. No telemetry.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Code-reviewed by a review bot @10ca79c (plugin social-media-skills 1.1.0, safe). Claude Code on Windows: /plugin marketplace add charlie947/social-media-skills then /plugin install social-media-skills (README lines 113-122). claude.ai: zip one skill folder and upload it in Customize > Skills (README). Nothing runs at install; it adds 17 text skills. reels-scripting only works if you give it your own APIFY_API_TOKEN and GOOGLE_AI_API_KEY (paid services) and Node.js; keep keys in environment variables, never paste them in chat. Do not run tests/test-codex-portability.py or validate-skills.sh: they are the author's own checks. Installs are unpinned, so later versions arrive without a review.
