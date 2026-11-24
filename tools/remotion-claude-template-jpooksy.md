# remotion-claude-template (jpooksy)

- **Type:** skill
- **Category:** generating videos, building a site
- **Official URL:** https://github.com/jpooksy/remotion-claude-template
- **GitHub repo:** https://github.com/jpooksy/remotion-claude-template @ 3392457 (MIT)
- **Price:** Free on GitHub, MIT (LICENSE file, checked 2026-11-22)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-23

## Safety reason

a review bot read @3392457: safe with these fixes. Verified 1: no network code in the repo: no fetch, http client, child_process or key handling in src/ or scripts/; scripts/convert-ds-icons.mjs only reads .vue icons from ICONS_DIR and writes src/icons (:19-24). Verified 2: package.json pins remotion 4.0.520 and its packages exactly (package.json:11-29), lucide-react uses ^1.17.0 (:16); package-lock.json pins everything from registry.npmjs.org, and esbuild is the only package with an install script (package-lock.json:3431). Fix: npm ci (installs exactly the lockfile), not npm install. Verified 3: CLAUDE.md:22 tells Claude to run npm install itself on a fresh clone and to start npx remotion studio in the background. Fix: run npm ci yourself before opening Claude Code, and keep Claude Code's permission prompts on so you approve each command. Verified 4: the agents and skill read your product's frontend repo, cloned as a sibling folder (README.md:57, CLAUDE.md:48); the agents declare no tool limits in their frontmatter, so they get Claude Code's normal tools. Fix: point it only at a repo you own, with no .env or keys in it. Verified 5: PUBLISH and FINALIZE only write YouTube titles/metadata into drafts/ and wait for you to paste the URL after you upload yourself (SKILL.md:432-493); nothing uploads. .mcp.json.example is a placeholder only (copy it only for an MCP server you trust). Verified 6 (Remotion docs, remotion.dev/docs/miscellaneous/chrome-headless-shell): the first render downloads Chrome Headless Shell from Google; this happens once and is required for rendering. Remotion is free for individuals and companies up to 3 people, others need a company licence (remotion.dev/license).

## Safe install

Safe install (fixes applied):
Windows (Node 18+): git clone https://github.com/jpooksy/remotion-claude-template C:\\Projects\\remotion-claude-template ; cd C:\\Projects\\remotion-claude-template ; git checkout 3392457f9c6cf5508da10fd0c18868c021946685 ; npm ci ; npx remotion studio (preview) ; npx remotion render Example out\\Example.mp4 (first render downloads Chrome Headless Shell once). Clone only your own frontend repo next to it, with no .env or keys.
Claude Code on Windows: run npm ci yourself first, then open Claude Code in that folder with normal permission prompts (never --dangerously-skip-permissions) and approve each command; do not copy .mcp.json.example to .mcp.json unless you trust that server.
claude.ai, Hermes, Android: not supported (needs local Node and Claude Code).

## YOLO install

YOLO (your own risk): skips the pinned commit, npm ci and the permission prompts. Windows: git clone the repo, open Claude Code in it and let it run npm install and npx remotion studio itself as CLAUDE.md:22 says.

## Install notes

Safe with fixes: Remotion 4.0.520 template plus a Claude Code skill and 4 agents for product-demo videos that recreate your app's UI from its frontend repo. Pin commit 3392457, install with npm ci, keep Claude Code's permission prompts on, point it only at a repo you own with no keys. No network code in the repo; the first render downloads Chrome Headless Shell once. Nothing is uploaded; you publish to YouTube yourself.
