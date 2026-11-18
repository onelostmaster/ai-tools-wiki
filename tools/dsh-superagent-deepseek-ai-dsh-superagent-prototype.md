# dsh-superagent (deepseek-ai/dsh-superagent-prototype)

- **Type:** app
- **Category:** developer tools, automation
- **Official URL:** https://github.com/deepseek-ai/dsh-superagent-prototype
- **GitHub repo:** https://github.com/deepseek-ai/dsh-superagent-prototype @ 6337fc8 (MIT; v0.1.0)
- **Price:** Free, MIT (github.com, checked 2026-11-02); model costs extra
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @8c32a9d v0.1.0 (2026-11-17): safe with fixes. Research prototype, not a DeepSeek product (README.md:3). Default accept mode is observe (docs/002-authorization.md:98); the panel answers only 127.0.0.1 (src/app/http.ts:77); it never enables auto-merge as the agent account (docs/003-execution.md:86). Workers run model-written commands. Fix: WSL on a test repo, stay in observe.

## Safe install

Safe install (fixes applied):
WSL only; clone at 8c32a9d; pnpm install, pnpm check; a test repo and a bot GitHub account with no merge rights; keep accept mode observe.

## YOLO install

YOLO (your own risk): skips the test repo and observe mode.
Point it at real repos in auto mode.

## Install notes

Ask the user before installing.
Windows: WSL only, per its README (not tested); keep it in observe mode on a test repo. Android: no.
