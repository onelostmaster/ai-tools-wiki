# Open Higgsfield

- **Type:** app
- **Category:** generating videos
- **Official URL:** https://openhiggsfield.ai
- **GitHub repo:** https://github.com/wide-trace/open-higgsfield @ b16a0ef (no license file despite the "open-source" claim; latest commit on 2026-09-16)
- **Price:** Studio code free to run but has no licence file (all rights reserved by default); generations are billed by the platform whose key you add; uploads need a Vercel Blob token (Vercel pricing applies)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @b16a0ef (2026-11-19, still HEAD): caution. The tree has no LICENSE file (only README, src, scripts, configs). The hosted-key, open /api/blob route (src/app/api/blob/route.ts:12) and prompt logging (src/generation/platform.ts:55,66) are fixed in Safe install. No fix: with no licence the code is all rights reserved, so you have no granted right to run or change it.

## Safe install

Safe install (fixes applied):
Windows (local only): install Node.js and pnpm, git clone the repo, git checkout b16a0ef, pnpm install --frozen-lockfile, then pnpm dev -- -H 127.0.0.1 so the unauthenticated /api/blob upload route (src/app/api/blob/route.ts line 12) is reachable only from your PC. Do not paste your platform key into the hosted openhiggsfield.ai (third-party server; the key goes to it, src/generation/platform.ts lines 49-66). Use a Vercel Blob store made only for this and treat every upload as a public URL. Do not share the terminal output: it logs every prompt and media URL (platform.ts lines 55 and 66). unverified: npm dependencies (pnpm-lock.yaml not read); contain it by running it with no other API keys in .env.local. No fix: there is no LICENSE file, so reuse rights stay unclear. Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin, the localhost binding and the separate Blob store.
Windows: pnpm install && pnpm dev, or the hosted openhiggsfield.ai with your key.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Code-reviewed by a review bot @b16a0ef (caution). Prefer running it yourself over pasting a key into the hosted openhiggsfield.ai, which is a third-party site, not Higgsfield. Windows (local only): install Node.js and pnpm, git clone the repo, git checkout b16a0ef, then pnpm install and pnpm dev (localhost:3000). It needs HF_API_BASE_URL (the generation API origin; the README does not name it) and a Vercel Blob read-write token in OPEN_HIGGSFIELD_READ_WRITE_TOKEN, so uploads need a Vercel account. Keep it on localhost: the /api/blob upload route has no login, and the server log prints every prompt and result URL. There is no licence file, so reuse rights are unclear.
