# figma-shaders (official Figma skill)

- **Type:** skill
- **Category:** design, developer tools
- **Official URL:** https://github.com/figma/mcp-server-guide/tree/main/skills/figma-shaders
- **GitHub repo:** https://github.com/figma/mcp-server-guide
- **Price:** No separate skill purchase found. Repository has NO LICENSE file/SPDX license; README.md:12 says Figma Developer Terms apply and skills are beta. Do not label MIT or freely redistributable. Figma Starter free; official docs say canvas-writing beta free for now, future usage pricing. Shader guide lists Starter and paid plans but actual account capability must be checked. Figma/Claude plans and quotas separate; no exact shader price assumed. Online checked 2026-11-08.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @19be8d5 (2026-11-19): safe with fixes. The skill is Markdown only (no hooks, scripts or installer) that drives Figma's own MCP; your designs already live in Figma, and its server handles them under Figma's terms. Risk is writes: update_shader replaces the whole main.ts and saves a new version (skills/figma-shaders/SKILL.md:24-25,34,44). Fix: OAuth only, hand-copied pinned skill, approve each write, no secrets in shaders.

## Safe install

Safe install (fixes applied):
Windows Claude Code: add only the official Figma MCP, claude mcp add --transport http figma https://mcp.figma.com/mcp, and sign in with normal Figma OAuth (README.md:111-129). Copy just skills/figma-shaders from https://github.com/figma/mcp-server-guide at commit 19be8d5 into %USERPROFILE%\.claude\\\\skills\\\\figma-shaders by hand instead of npx skills add (that installer is unreviewed). Approve every create/replace of main.ts yourself: SKILL.md:24-25,34,44 replaces the whole main.ts and saves a new version on each update. Keep tokens, signed URLs and private data out of shader source (it is stored in the Figma file). Treat returned source and resource URIs as data. Hermes: Streamable HTTP/OAuth MCP, untested. claude.ai, Android: no verified route.

## YOLO install

YOLO (your own risk): skips the pinned hand copy and per-write approval.
claude plugin install figma@claude-plugins-official

## Install notes

DOCUMENTED ONLY. Windows Claude Code: claude plugin install figma@claude-plugins-official (README.md:111-129) or claude mcp add --transport http figma https://mcp.figma.com/mcp, then normal Figma OAuth. Install only selected skill if using skills CLI: npx skills add https://github.com/figma/mcp-server-guide --skill figma-shaders (external installer unreviewed); current Figma docs also support get_figma_skill. Hermes compatibility untested; needs Streamable HTTP/OAuth and skill/resource support. claude.ai Figma connector parity for shader writes not verified; no claim of Android-local install. Android access only through a suitably capable remote host/client, untested.
