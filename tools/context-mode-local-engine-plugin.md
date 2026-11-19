# Context Mode (local Engine plugin)

- **Type:** plugin
- **Category:** developer tools, automation
- **Official URL:** https://github.com/mksglu/context-mode
- **GitHub repo:** https://github.com/mksglu/context-mode
- **Price:** Local Engine free, no account, source-available Elastic License 2.0 (not MIT/OSI open source; LICENSE limits offering it as a substantial hosted/managed service). Verified online 2026-11-07 at contextmode.ai/docs/engine/gateway and /pricing. Optional separate Gateway: 1,000 requests/month free; Pro starts $20/month for 10,000 requests; model usage additional. Gateway forwards conversations to its server and stores searchable session data (README.md:660); not part of this local-code review and not recommended for a first trial.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Claude code read @9a1282f v2.2.1 (2026-11-18): safe with fixes. ctx_execute runs model-written code as you, with your files, network and env minus preload vars (README.md:600; src/core/sandbox/env.ts:24-32). Its hook denies Read and points the agent to ctx_execute; it grants nothing (plugins/claude-code/pi/index.js:12582). No telemetry (README.md:588). Fix: never allow-list ctx_execute or ctx_batch_execute, pin.

## Safe install

Safe install (fixes applied):
claude plugin marketplace add mksglu/context-mode#9a1282f, claude plugin install context-mode@context-mode; Node 24.15+ and Git Bash on Windows; keep approval prompts for ctx_execute and ctx_batch_execute; don't index secrets; ctx_purge when done.

## YOLO install

YOLO (your own risk): skips the pin and the approval rule.
Install from main and allow ctx_execute always.

## Install notes

NOT installed; ask the user first. Windows Claude Code: requires Node >=24.15.0 and Git for Windows/Git Bash (README.md:56). Documented install commands, NOT executed: claude plugin marketplace add mksglu/context-mode ; claude plugin install context-mode@context-mode (README.md:63-64). Bundled plugin version 2.1.6. Update via claude plugin update context-mode@context-mode (README.md:69). claude.ai/Android: no supported local hook/plugin route. Hermes: not in the 10 supported agent adapters; generic MCP is not enough to promise equivalent integration (entries/server.ts:239 requires recognized agent for project resolution). No a scout post. Before any trial: clean disposable/test repo, approvals enabled (no skip-permissions/YOLO), minimal environment with no production keys, no blanket permission for script execution, local-only Engine (do not configure Gateway), review stored outputs and upgrade requests.
