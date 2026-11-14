# Context Mode (local Engine plugin)

- **Type:** plugin
- **Category:** developer tools, automation
- **Official URL:** https://github.com/mksglu/context-mode
- **GitHub repo:** https://github.com/mksglu/context-mode
- **Price:** Local Engine free, no account, source-available Elastic License 2.0 (not MIT/OSI open source; LICENSE limits offering it as a substantial hosted/managed service). Verified online 2026-11-07 at contextmode.ai/docs/engine/gateway and /pricing. Optional separate Gateway: 1,000 requests/month free; Pro starts $20/month for 10,000 requests; model usage additional. Gateway forwards conversations to its server and stores searchable session data (README.md:660); not part of this local-code review and not recommended for a first trial.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-07

## Safety reason

Targeted source read @2000abb (v2.1.6), not a full dependency audit. CAUTION: its "sandbox" is output isolation, not a security sandbox. ctx_execute runs model-written code with your user filesystem, network and most environment variables; src/core/tools/execute.ts:188-214, src/core/sandbox/spawn.ts:43-45, env.ts:24-32 (strips preload vars, not general API secrets), README.md:581. Keep agent approvals on and never blanket-allow ctx_execute/ctx_batch. Raw outputs/session data persist locally; avoid indexing secrets, protect ~/.context-mode and backups. Retrieved content can still contain prompt injection: output filtering is not a trust boundary. Hooks: plugins/claude-code/hooks/claude-code.json:3-48 runs Node on PostToolUse, PreToolUse, SessionStart, UserPromptSubmit; adapters/claude-code.ts:208 can deny oversized calls and redirect, rather than grant permissions. MCP is local stdio (plugins/claude-code/.claude-plugin/plugin.json:7-15). No telemetry SDK found in targeted src scan; local usage stats. Network: explicit URL indexing via core/sandbox/fetch.ts:144-149 rejects private resolved addresses and checks redirect hops; doctor/upgrade contact GitHub/npm (core/contracts/constants.ts:486,547; core/ops/doctor-env.ts:92). ctx_upgrade can invoke host updates/regenerate config (core/tools/upgrade.ts:67-107): explicit tool, not evidence of silent auto-updating. No npm postinstall/preinstall, no curl|bash installer or direct eval found in targeted source scan; shell/code execution itself is an advertised feature. Storage: core/store/db.ts:123 creates project storage; constants.ts:131,168 gives context.db and ~/.context-mode. No database encryption layer seen; this is not a secret vault. Dependency and bundled-binary audit not performed.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

NOT installed; ask the user first. Windows Claude Code: requires Node >=24.15.0 and Git for Windows/Git Bash (README.md:56). Documented install commands, NOT executed: claude plugin marketplace add mksglu/context-mode ; claude plugin install context-mode@context-mode (README.md:63-64). Bundled plugin version 2.1.6. Update via claude plugin update context-mode@context-mode (README.md:69). claude.ai/Android: no supported local hook/plugin route. Hermes: not in the 10 supported agent adapters; generic MCP is not enough to promise equivalent integration (entries/server.ts:239 requires recognized agent for project resolution). No a scout post. Before any trial: clean disposable/test repo, approvals enabled (no skip-permissions/YOLO), minimal environment with no production keys, no blanket permission for script execution, local-only Engine (do not configure Gateway), review stored outputs and upgrade requests.
