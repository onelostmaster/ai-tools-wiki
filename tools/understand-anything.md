# Understand Anything

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://understand-anything.com/
- **GitHub repo:** https://github.com/Egonex-AI/Understand-Anything @ 5cc4aad (MIT; HEAD on 2026-11-14, latest commit on 2026-11-12 ET; plugin 2.9.8)
- **Price:** Free (MIT, `github.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read @5cc4aad, 2026-11-14, no-intake review): Safe, with caveats. 536 files: one Claude Code plugin (9 skills, 11 agent prompts) plus TypeScript core/dashboard/viewer/MCP packages and Node/Python helper scripts. hooks/hooks.json adds a PostToolUse (Bash) and a SessionStart hook; both read only local files and git rev-parse, and act only if you turned on autoUpdate in .understand-anything/config.json (post-tool-use-auto-update.mjs lines 17-24, 42-46); then they tell Claude to update the graph 'without asking' (lines 48-52), so leave auto-update off unless you want the token spend. Subprocesses are git, node and the plugin's own scripts; no eval, no curl-pipe-to-shell inside the plugin, no obfuscated code. Network: none for analysis itself; the local viewer listens on 127.0.0.1 only with a one-time token (viewer.mjs lines 333, 396); dashboard loads Google Fonts; Figma import calls api.figma.com only with your own token (api-source.ts line 27). Caveats: /understand-dashboard step 4 runs npx --yes on a release tarball (understand-dashboard SKILL.md lines 110-116) that CI builds but no workflow publishes, so that file was not reviewed; first run does pnpm install of npm dependencies (lockfile pinned); the root install.sh/install.ps1 one-liners pull unpinned main. No prompt-injection phrases found beyond the opt-in hook text. Replaces the earlier not-reviewed status.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Code-reviewed by a review bot @5cc4aad (safe, with the caveats in Safety reason). Claude Code on Windows: in Claude Code type /plugin marketplace add Egonex-AI/Understand-Anything, then /plugin install understand-anything (README). Keep plugin auto-update off so a later version is not pulled in without a new review. Needs Node.js; the first /understand run may run pnpm install and build the core package inside the plugin folder. Do not use the curl ... install.sh | bash or install.ps1 one-liners; they are for other agents and fetch the latest main. Leave --auto-update off unless you want it: when on, its hooks tell Claude to re-analyse the graph after every commit without asking, which spends tokens. /understand-dashboard first tries npx --yes on a prebuilt viewer tarball from the GitHub release; say no to that and let it use the local build if you want only reviewed code. It reads your whole repo (large token use; scope to a subfolder on big projects) and writes a .understand-anything folder; do not commit that folder in a private project if you share the repo. claude.ai and Android: not a fit (needs a local computer).
