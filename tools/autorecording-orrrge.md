# autoRecording (OrrrGE)

- **Type:** skill
- **Category:** generating videos, editing
- **Official URL:** https://github.com/OrrrGE/autoRecording
- **GitHub repo:** https://github.com/OrrrGE/autoRecording @ 4df00e0 (MIT)
- **Price:** Free on GitHub, MIT (LICENSE file, checked 2026-11-20)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-27

## Safety reason

a review bot read @4df00e0: safe with these fixes. A skill that drives your web app in headless Chromium from a Python story file, renders a 1080p video with ffmpeg and adds narration from a local or remote TTS. Verified 1: demo_env.py setup installs 11 unpinned packages (demo_env.py:31) into its own venv under %USERPROFILE%\.cache\\auto-demo-recording (demo_common.py:24, demo_env.py:199-201), not globally. Fix: create that venv yourself and install the same packages at versions you pin instead of running setup. Verified 2: setup --kokoro and --models download about 350 MB and 3 GB of public models (Kokoro and CAM++ from sherpa-onnx GitHub releases, Whisper large-v3 from Hugging Face; demo_env.py:37-50) with no checksum; the Kokoro archive is unpacked with tarfile's safe 'data' filter only on Python 3.12+ (demo_env.py:186-190). Fix: use Python 3.12 or newer, and pass --kokoro or --models only when you need that voice or the checks. Verified 3: a remote engine sends your caption text and key to OpenAI, ElevenLabs or Alibaba DashScope (demo_tts.py:84, :274-275); demo_env.py key stores keys in plain text in secrets.json in that cache folder (demo_common.py:131-140; on Windows only the profile's access control protects it). Fix: use local Kokoro, or for a remote voice set DEMO_TTS_API_KEY only in that session instead of demo_env.py key. Verified 4: the story file is Python, and its launch() starts the command you write (demo_record.py:470, :486); its wipe list deletes paths only inside the recording's work folder (checked at demo_record.py:472-476). Fix: read launch() before each recording and point it at a throwaway copy of your app, never the live service (SKILL.md Non-negotiables 1). Verified 5: the browser comes from python -m playwright install chromium (demo_env.py:109). Fix: or point it at your installed Edge with demo_env.py set chromium=<path>. MIT (LICENSE).

## Safe install

Safe install (fixes applied):
Claude Code (Windows, Python 3.12+): git clone https://github.com/OrrrGE/autoRecording %USERPROFILE%\.claude\\skills\\autoDemoRecordingSkill ; cd there ; git checkout 4df00e0647aa4f20dc155d975f75bf3e7f45827e ; py -3 -m venv %USERPROFILE%\.cache\\auto-demo-recording\\venv ; then install playwright, httpx, numpy, opencv-python-headless, pillow, soundfile, soxr, scipy, faster-whisper, pypinyin and sherpa-onnx into that venv at versions you pin (name==version) ; py -3 scripts\\demo_env.py setup --kokoro only if you want the local CPU voice ; use your installed Edge via demo_env.py set chromium=<path> or run playwright install chromium. Read each story file's launch() and record only a throwaway copy of your app; for a remote voice set DEMO_TTS_API_KEY in that session only.
claude.ai, Hermes, Android: not supported (needs local Python, ffmpeg and a browser).

## YOLO install

YOLO (your own risk): skips the pinned commit, pinned packages, Python 3.12 extraction filter and the key rule. README: git clone into ~/.claude/skills/autoDemoRecordingSkill, then python3 scripts/demo_env.py setup --models --kokoro

## Install notes

Safe with fixes: clone at commit 4df00e0; install its packages yourself at pinned versions into its own venv instead of demo_env.py setup (setup installs them unpinned); use Python 3.12+ before fetching Kokoro; prefer the local Kokoro voice, and for a remote voice set the key in the session only (demo_env.py key stores it in plain text); read launch() in each story file and record only a throwaway copy of your app. Fits faceless channel explainer videos only for web-app demos.
