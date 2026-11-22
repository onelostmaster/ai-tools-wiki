# remotion-shorts-skill (social-media-skills)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/social-media-skills/remotion-shorts-skill
- **GitHub repo:** https://github.com/social-media-skills/remotion-shorts-skill @ 6a09634 (MIT)
- **Price:** Free on GitHub, MIT (LICENSE file, checked 2026-11-20); Remotion licence free for individuals and small teams
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-21

## Safety reason

a review bot code read @6a09634: safe with the fixes in Safe install. Rendering is local: render.mjs only reads your short.json, refuses URLs for media (render.mjs:58), copies the files it uses into the project's public/assets/<short name> folder and deletes other files only inside that folder (render.mjs:55,79), and writes to out/<name> (render.mjs:50). No fetch or network code in render.mjs or template/src. setup.mjs copies the template, keeps your changed files as .bak (setup.mjs:42-47), runs npm ci --no-audit --no-fund from the lockfile (setup.mjs:67) and npx remotion browser ensure (setup.mjs:70), with fixed arguments. Packages are pinned exactly (Remotion 4.0.536, React 19.1.1; package.json:10-22) and the only package with an install script is esbuild 0.28.1 (package-lock.json:2563). Verified behaviour and fixes: (1) the README's default install is npx skills add social-media-skills/remotion-shorts-skill -g -a claude-code -y (README.md:15,62): the third-party skills installer, global scope, no prompts, moving main branch; fix: pinned clone at 6a09634 and copy skills/remotion-shorts-skill into %USERPROFILE%\.claude\\skills by hand. (2) setup.mjs downloads about 260 MB of npm packages and a 100-150 MB headless Chrome on first run (setup.mjs:66-70) into the project folder; fix: run it yourself in a dedicated folder, nothing global. (3) Posting goes through WoopSocial, a third-party posting service you sign in to (woopsocial.md:12-33); the skill waits for your yes before posts_create (SKILL.md:144-145,191) and upload.mjs PUTs the MP4 to the session's upload URLs (upload.mjs:43); fix: don't connect WoopSocial and post the MP4 yourself, or if you connect it use the OAuth sign-in, never an api_key in the MCP URL (woopsocial.md:33,35). (4) Remotion's licence: free for individuals and companies of up to 3 people (SKILL.md:34-37). Unverified: Remotion's browser download source and the npx skills installer were not code-read; containment: pinned versions from the lockfile, project folder only, no keys.

## Safe install

Safe install (fixes applied): Claude Code on Windows (Git, Node.js 20+; normal terminal): git clone https://github.com/social-media-skills/remotion-shorts-skill.git %USERPROFILE%\\src\\remotion-shorts-skill && cd %USERPROFILE%\\src\\remotion-shorts-skill && git checkout 6a09634 && xcopy /E /I skills\\remotion-shorts-skill %USERPROFILE%\.claude\\skills\\remotion-shorts-skill. Then make the render project once in its own folder: cd %USERPROFILE%\\src && node %USERPROFILE%\.claude\\skills\\remotion-shorts-skill\\scripts\\setup.mjs remotion-shorts (npm ci from the lockfile plus Remotion's headless browser, both inside that folder). Render with node render.mjs short.json --stills, then node render.mjs short.json. Don't use npx skills add ... -g -y. Don't connect WoopSocial; upload the MP4 to TikTok, Reels or Shorts yourself (if you ever connect it, use the OAuth sign-in, never an api_key in the URL). Codex or Cursor: same pinned clone, copy skills/remotion-shorts-skill into that agent's skills folder. Hermes: same pinned clone, copy to ~/.hermes/skills/creative/remotion-shorts-skill. claude.ai: no (needs local Node). Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin, the hand copy and leaving WoopSocial off. npx skills add social-media-skills/remotion-shorts-skill -g -a claude-code -y (README.md:62; third-party installer, global, no prompts, moving main branch), then let the agent run setup.mjs and connect WoopSocial with claude mcp add --transport http woopsocial https://api.woopsocial.com/mcp (woopsocial.md:30).

## Install notes

Ask the user before installing. Safe with the fixes in Safe install applied (pinned clone at 6a09634 copied into one agent by hand, setup.mjs run in its own project folder, WoopSocial left off and posting done by hand). Turns a topic, data or changelog into 1080x1920 kinetic-text shorts rendered locally with Remotion, with review sheets, a cover and safe-zone checks; no paid API. Remotion is free for individuals and teams up to 3. Good fit for the faceless video channel.
