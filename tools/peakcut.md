# PeakCut

- **Type:** app
- **Category:** editing, video
- **GitHub repo:** https://github.com/haziqahmedqasmi/PeakCut @ b3e403e (MIT; commit 2026-11-15 confirmed via GitHub API)
- **Price:** Free (MIT); you pay your own AI provider
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @b3e403e, 2026-11-16: safe with the Install notes fixes. Binds 127.0.0.1 by default (studio/config.py:143); speech-to-text runs locally; no telemetry found. Verified risks, each fixed: update check calls GitHub every minute and shows commit notes with a paste-to-your-AI update sentence (studio/updates.py:59-68; fix: PEAKCUT_UPDATE_CHECK=0, studio/updates.py:22, stay on b3e403e); no sign-in when local, so exposing it shares your AI key (.env.example; fix: keep PEAKCUT_HOST=127.0.0.1, never port-forward 8765). unverified: yt-dlp plugin loading in the library call (studio/media.py:99-103); contain: own venv, no yt-dlp plugin folders. a review bot spot-checked config.py:143 and updates.py:22,59-68 at b3e403e.

## Safe install

Safe install (fixes applied):
Windows: git clone https://github.com/haziqahmedqasmi/PeakCut && cd PeakCut && git checkout b3e403e && python -m venv .venv && .venv\\Scripts\\pip install -r requirements.txt; add PEAKCUT_UPDATE_CHECK=0 and PEAKCUT_HOST=127.0.0.1 to .env (studio/updates.py:22, studio/config.py:143); winget install Gyan.FFmpeg; .venv\\Scripts\\python -m studio.server, open http://127.0.0.1:8765. Keep it in its own venv with no yt-dlp plugin folders; never port-forward 8765; connect no social accounts. claude.ai, Claude Code, Hermes, Android: no (standalone web app).

## YOLO install

YOLO (your own risk): skips the commit pin, the update-check switch and the localhost-only rule.
git clone https://github.com/haziqahmedqasmi/PeakCut, pip install -r requirements.txt, python -m studio.server (follows main, update banner on).

## Install notes

Ask the user first. git clone https://github.com/haziqahmedqasmi/PeakCut, then git checkout b3e403e, python -m venv .venv, .venv pip install -r requirements.txt, put PEAKCUT_UPDATE_CHECK=0 in .env, winget install Gyan.FFmpeg, run python -m studio.server and open 127.0.0.1:8765. First start downloads a 480 MB speech model. Don't connect social accounts: posting needs your own Google/Meta/TikTok developer apps, uploads stay private until each platform audits the app, and Instagram/TikTok need an https redirect (DEPLOY.md:35-53).
