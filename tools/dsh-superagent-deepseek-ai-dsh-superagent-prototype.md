# dsh-superagent (deepseek-ai/dsh-superagent-prototype)

- **Type:** app
- **Category:** developer tools, automation
- **Official URL:** https://github.com/deepseek-ai/dsh-superagent-prototype
- **GitHub repo:** https://github.com/deepseek-ai/dsh-superagent-prototype @ 6337fc8 (MIT; v0.1.0)
- **Price:** Free, MIT (github.com, checked 2026-11-02); model costs extra
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @6337fc8, a review, 2026-11-02): caution. "Not an official DeepSeek product" (`README.md:3`). Default accept mode is observe (`docs/002-authorization.md:98`), panel on 127.0.0.1 (`http.ts:78`), no auto-merge (`delivery.md:10`), but workers run model-written commands (`docs/003-execution.md:47`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: WSL only, per its README (not tested); keep it in observe mode on a test repo. Android: no.
