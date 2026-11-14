# Open Higgsfield

- **Type:** app
- **Category:** generating videos
- **Official URL:** https://openhiggsfield.ai
- **GitHub repo:** https://github.com/wide-trace/open-higgsfield @ b16a0ef (no license file despite the "open-source" claim; latest commit on 2026-09-16)
- **Price:** Studio code free to run but has no licence file (all rights reserved by default); generations are billed by the platform whose key you add; uploads need a Vercel Blob token (Vercel pricing applies)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-12

## Safety reason

a review bot (code read @b16a0ef, 2026-11-11, no-intake review): Caution. The code itself is small and clean: a Next.js app whose server actions alone call the generation API (POST /\{model\}, GET /requests/\{id\}/status) with an 'Authorization: Key id:secret' header (src/generation/platform.ts lines 49-66), the key is kept in an httpOnly cookie for 30 days (src/generation/credentials.ts lines 1-9, actions.ts lines 19-23), and there is no telemetry, eval or extra network call. Reasons for caution: (1) the hosted openhiggsfield.ai is a third-party site that receives your platform key on its server; (2) the /api/blob route hands out Vercel Blob upload tokens to anyone who can reach it, as its own comment says (src/app/api/blob/route.ts line 12), and uploaded files become public URLs; (3) the server logs every request body, including prompts and media URLs (platform.ts lines 55 and 66); (4) no LICENSE file; (5) HF_API_BASE_URL is left unnamed in the README, though model paths such as higgsfield-ai/soul (src/generation/to-platform.ts lines 8-9) point at Higgsfield's own API. Not reviewed: npm dependencies (pnpm-lock.yaml present) and the brand-asset script that drives a local Chromium (not part of normal use).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Code-reviewed by a review bot @b16a0ef (caution). Prefer running it yourself over pasting a key into the hosted openhiggsfield.ai, which is a third-party site, not Higgsfield. Windows (local only): install Node.js and pnpm, git clone the repo, git checkout b16a0ef, then pnpm install and pnpm dev (localhost:3000). It needs HF_API_BASE_URL (the generation API origin; the README does not name it) and a Vercel Blob read-write token in OPEN_HIGGSFIELD_READ_WRITE_TOKEN, so uploads need a Vercel account. Keep it on localhost: the /api/blob upload route has no login, and the server log prints every prompt and result URL. There is no licence file, so reuse rights are unclear.
