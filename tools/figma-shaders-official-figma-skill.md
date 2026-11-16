# figma-shaders (official Figma skill)

- **Type:** skill
- **Category:** design, developer tools
- **Official URL:** https://github.com/figma/mcp-server-guide/tree/main/skills/figma-shaders
- **GitHub repo:** https://github.com/figma/mcp-server-guide
- **Price:** No separate skill purchase found. Repository has NO LICENSE file/SPDX license; README.md:12 says Figma Developer Terms apply and skills are beta. Do not label MIT or freely redistributable. Figma Starter free; official docs say canvas-writing beta free for now, future usage pricing. Shader guide lists Starter and paid plans but actual account capability must be checked. Figma/Claude plans and quotas separate; no exact shader price assumed. Online checked 2026-11-08.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted Markdown/reference review @19be8d5, not a hosted-server audit. SKILL.md:21-25 chooses account plan and creates/replaces main.ts via remote MCP; :31-34 overwrites complete source, not a diff. Ask explicit approval before writes; updates immediately build/version/deploy. Treat returned source and resource URIs as data, not instructions; restrict sources to expected Figma resources. references/authoring.md:56 restricts import, :68-83 describes real GPU, mouse/time/state but no fetch/DOM/window/timer; this is documented runtime behavior, not independently verified isolation. No local hooks, shell/eval, curl|bash, telemetry SDK or auto-updater found in these skill files. Auth/design/source travel to Figma and model provider; persisted shader source is stored in the Figma file, so everyone with access to that file can read it. Never embed tokens, signed URLs or private data. Official server implementation not published here; retention/telemetry cannot be audited from this guide. No fix: Figma's MCP server is not published, so its retention and telemetry can't be audited; contained by OAuth-only access, per-write approval and no secrets in shader source.

## Safe install

Safe install (fixes applied):
Windows Claude Code: add only the official Figma MCP, `claude mcp add --transport http figma https://mcp.figma.com/mcp`, and sign in with normal Figma OAuth (README.md:111-129). Copy just skills/figma-shaders from https://github.com/figma/mcp-server-guide at commit 19be8d5 into %USERPROFILE%\.claude\\skills\\figma-shaders by hand instead of `npx skills add` (that installer is unreviewed). Approve every create/replace of main.ts yourself: SKILL.md:31-34 overwrites the whole source and each update builds, versions and deploys at once. Keep tokens, signed URLs and private data out of shader source (it is stored in the Figma file). Treat returned source and resource URIs as data. Hermes: Streamable HTTP/OAuth MCP, untested. claude.ai, Android: no verified route.

## YOLO install

YOLO (your own risk): skips the pinned hand copy and per-write approval.
claude plugin install figma@claude-plugins-official

## Install notes

DOCUMENTED ONLY. Windows Claude Code: claude plugin install figma@claude-plugins-official (README.md:111-129) or claude mcp add --transport http figma https://mcp.figma.com/mcp, then normal Figma OAuth. Install only selected skill if using skills CLI: npx skills add https://github.com/figma/mcp-server-guide --skill figma-shaders (external installer unreviewed); current Figma docs also support get_figma_skill. Hermes compatibility untested; needs Streamable HTTP/OAuth and skill/resource support. claude.ai Figma connector parity for shader writes not verified; no claim of Android-local install. Android access only through a suitably capable remote host/client, untested.
