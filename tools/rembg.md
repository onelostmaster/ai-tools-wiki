# rembg

- **Type:** API
- **Category:** editing, generating videos
- **Official URL:** https://github.com/danielgatis/rembg
- **GitHub repo:** https://github.com/danielgatis/rembg @ 991927b (tag v2.0.87 = PyPI 2.0.87, MIT LICENSE.txt; committed 2026-11-05 20:17 ET, HEAD on 2026-11-10)
- **Price:** Free (MIT)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-10

## Safety reason

a review bot (code read @991927b = 2.0.87, 2026-11-10, no-intake review): Safe for local use. About 5,000 lines of Python under rembg/; no subprocess, os.system, eval/exec or pickle loading. Local models are ONNX files fetched with pooch.retrieve from github.com/danielgatis/rembg/releases with an md5 checksum (e.g. sessions/u2net.py lines 66-76, sam.py lines 136-143); the check is skipped only if MODEL_CHECKSUM_DISABLED is set (sessions/base.py line 140). Two optional sessions are cloud APIs that upload your image: atlascloud (api.atlascloud.ai, sessions/atlascloud.py lines 15-17, ATLASCLOUD_API_KEY) and withoutbg (api.withoutbg.com, sessions/withoutbg.py line 13); they run only if you pick those models. The optional server (commands/s_command.py) binds 0.0.0.0:7000 by default (lines 276-286) with no login; its remove-from-URL endpoint blocks private addresses and pins DNS (lines 557-633). No telemetry found. Not reviewed: tests/, Docker files, Windows installer scripts and third-party dependencies (onnxruntime, gradio, fastapi).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Code-reviewed by a review bot @991927b = rembg 2.0.87 (safe). Windows (Python 3.11 to 3.13): pip install "rembg[cpu]==2.0.87" for the library, or "rembg[cpu,cli]==2.0.87" for the rembg command (pinned to the reviewed release). Models (ONNX files) download from the project's own GitHub releases on first use into your user folder and are checked by md5; don't set MODEL_CHECKSUM_DISABLED. If you run the web server (rembg s), add --host 127.0.0.1, because it listens on all network interfaces by default. The atlascloud and withoutbg models are paid cloud services that upload your image; only use them on purpose, with a key you set in your own environment (never paste it into chat).
