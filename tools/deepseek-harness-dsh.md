# DeepSeek Harness (dsh)

- **Type:** app
- **Category:** developer tools, automation, 3D and games
- **Official URL:** https://deepseek.com/harness
- **GitHub repo:** https://github.com/deepseek-ai/deepseek-harness @ ce7073d (MIT; official DeepSeek org; pushed 2026-10-30; developer preview)
- **Price:** Harness free (MIT). DeepSeek API: deepseek-flash $0.30 per 1M input (cache miss), $1.20 per 1M output at peak, half off-peak; V4-Pro $1.32/$3.96; Search and Fetch $0.75 per 1,000 since 2026-11-01 (api-docs.deepseek.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude doc and targeted read @39163dd3 (2026-11-16): safe with fixes. Its own SAFETY.md says it runs model-written code, loads plugins and is unaudited, and tells you to use a disposable VM or container. The Web UI binds 127.0.0.1:3080 (README.md:27). Fix: follow SAFETY.md: a VM or the spare account, no Creator Mode plugins, review each command. Developer preview.

## Safe install

Safe install (fixes applied):
Disposable VM or the spare YOLO-box account only; npx @deepseek-ai/dsh@0.2.2-rc.1 web; keep the 127.0.0.1 bind; approvals on; no Creator Mode; DeepSeek key in env.

## YOLO install

YOLO (your own risk): skips the VM and approvals.
npx @deepseek-ai/dsh web on your main account with Creator Mode on.

## Install notes

Ask the user before installing.
Windows: needs Node.js; `npx @deepseek-ai/dsh web` opens a Web UI on 127.0.0.1:3080 (README.md:24-27); untested.
