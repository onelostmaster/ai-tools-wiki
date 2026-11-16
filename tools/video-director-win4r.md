# video-director (win4r)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/win4r/video-director
- **GitHub repo:** https://github.com/win4r/video-director @ 02d1912 (MIT LICENSE file; committed 2026-11-07 08:07 ET, HEAD on 2026-11-10; was 4747e5c when added)
- **Price:** Free, MIT (github.com, checked 2026-11-05)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (code read @02d1912, 2026-11-10, no-intake review): Safe. A markdown skill (video-director/SKILL.md, 390 lines, plus references/*.md) and two Python QA scripts; no hooks, no MCP config, no settings.json, nothing asks for keys or tells the agent to skip permissions. scripts/check_timeline.py (308 lines) imports only json, math, re, sys and pathlib (lines 18-22) and just reads a timeline.json and prints checks. scripts/qa_video.py (708 lines) imports standard modules plus numpy and Pillow (lines 33-43); its only subprocess calls run ffprobe/ffmpeg on the given video with argument lists, not a shell (lines 49, 66, 91, 209, 261); it writes stills in a temp folder and report.json/report.md only into the --out folder (lines 552, 582, 691, 698); no network calls. evals/*/place-files.sh (3 lines each) only copy sample files into the current folder; the CI workflow runs pytest with read-only permissions. Not reviewed: the demo media files under assets/.

## Safe install

Safe install (fixes applied):
Windows Claude Code: `git clone https://github.com/win4r/video-director`, then `git checkout 02d1912` (the reviewed commit, still HEAD on 2026-11-15), and copy only the inner video-director folder into %USERPROFILE%\.claude\\skills\\ (or a project's .claude\\skills). For the QA scripts: `winget install Gyan.FFmpeg` and, in a venv, `pip install numpy Pillow`. The scripts make no network calls and write only into the --out folder (scripts/qa_video.py:552,582,691,698). Skip evals/*/place-files.sh. Not a claude.ai, Hermes or Android tool.

## YOLO install

YOLO (your own risk): skips the commit pin and the venv.
git clone https://github.com/win4r/video-director && pip install numpy Pillow

## Install notes

Code-reviewed by a review bot @02d1912 (safe). Claude Code on Windows: download the repo at commit 02d1912 (or git clone, then git checkout 02d1912) and copy the inner video-director folder into %USERPROFILE%\.claude\\skills\\ (or a project's .claude\\skills folder). The two QA scripts need Python 3 with numpy and Pillow (pip install numpy Pillow) and ffmpeg/ffprobe on PATH (e.g. winget install Gyan.FFmpeg); they only read your rendered MP4 and timeline.json and write a report into the --out folder. The README recommends a specific Claude model; the skill itself works as plain instructions. Skip the evals folder's place-files.sh scripts unless you run its test cases (they only copy sample files).
