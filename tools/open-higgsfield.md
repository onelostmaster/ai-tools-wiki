# Open Higgsfield

- **Type:** app
- **Category:** generating videos
- **Official URL:** https://openhiggsfield.ai
- **GitHub repo:** https://github.com/wide-trace/open-higgsfield @ b16a0ef (no license file despite the "open-source" claim; latest commit on 2026-09-16)
- **Price:** Studio code free to run but has no licence file (all rights reserved by default); generations are billed by the platform whose key you add; uploads need a Vercel Blob token (Vercel pricing applies)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (code read @b16a0ef, 2026-11-11, no-intake review): Caution. The code itself is small and clean: a Next.js app whose server actions alone call the generation API (POST /\{model\}, GET /requests/\{id\}/status) with an 'Authorization: Key id:secret' header (src/generation/platform.ts lines 49-66), the key is kept in an httpOnly cookie for 30 days (src/generation/credentials.ts lines 1-9, actions.ts lines 19-23), and there is no telemetry, eval or extra network call. Reasons for caution: (1) the hosted openhiggsfield.ai is a third-party site that receives your platform key on its server; (2) the /api/blob route hands out Vercel Blob upload tokens to anyone who can reach it, as its own comment says (src/app/api/blob/route.ts line 12), and uploaded files become public URLs; (3) the server logs every request body, including prompts and media URLs (platform.ts lines 55 and 66); (4) no LICENSE file; (5) HF_API_BASE_URL is left unnamed in the README, though model paths such as higgsfield-ai/soul (src/generation/to-platform.ts lines 8-9) point at Higgsfield's own API. Not reviewed: npm dependencies (pnpm-lock.yaml present) and the brand-asset script that drives a local Chromium (not part of normal use). No fix: the repo has no LICENSE file, so reuse rights stay unclear; the key, upload-route and logging risks are fixed in Safe install, so caution stands for the missing licence only.

## Safe install

Safe install (fixes applied):
Windows (local only): install Node.js and pnpm, git clone the repo, git checkout b16a0ef, pnpm install --frozen-lockfile, then pnpm dev -- -H 127.0.0.1 so the unauthenticated /api/blob upload route (src/app/api/blob/route.ts line 12) is reachable only from your PC. Do not paste your platform key into the hosted openhiggsfield.ai (third-party server; the key goes to it, src/generation/platform.ts lines 49-66). Use a Vercel Blob store made only for this and treat every upload as a public URL. Do not share the terminal output: it logs every prompt and media URL (platform.ts lines 55 and 66). unverified: npm dependencies (pnpm-lock.yaml not read); contain it by running it with no other API keys in .env.local. No fix: there is no LICENSE file, so reuse rights stay unclear. Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin, the localhost binding and the separate Blob store.
Windows: pnpm install && pnpm dev, or the hosted openhiggsfield.ai with your key.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Code-reviewed by a review bot @b16a0ef (caution). Prefer running it yourself over pasting a key into the hosted openhiggsfield.ai, which is a third-party site, not Higgsfield. Windows (local only): install Node.js and pnpm, git clone the repo, git checkout b16a0ef, then pnpm install and pnpm dev (localhost:3000). It needs HF_API_BASE_URL (the generation API origin; the README does not name it) and a Vercel Blob read-write token in OPEN_HIGGSFIELD_READ_WRITE_TOKEN, so uploads need a Vercel account. Keep it on localhost: the /api/blob upload route has no login, and the server log prints every prompt and result URL. There is no licence file, so reuse rights are unclear.
