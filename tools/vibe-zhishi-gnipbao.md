# vibe-zhishi (gnipbao)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/gnipbao/vibe-zhishi
- **GitHub repo:** https://github.com/gnipbao/vibe-zhishi @ fb813f0 (MIT)
- **Price:** Free on GitHub, MIT (LICENSE file, checked 2026-11-22)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-23

## Safety reason

a review bot read @fb813f0: safe with these fixes. Verified 1: references/build.md:26 tells the agent to run npx hyperframes@latest upgrade before rendering, and README.md:73 suggests npx hyperframes skills update; both fetch an unpinned HyperFrames. Fix: use only the pinned npx --yes hyperframes@0.8.183 commands from references/build.md:18,105-121 and tell Claude Code to skip the @latest upgrade check and skills update. Verified 2: the .sh helpers (render.sh, still.sh, clean_frame.sh, hook_strip.sh) are POSIX shell, and make_covers.py:36 defaults Chrome to the macOS path; fonts are macOS system fonts (README.md:95). Fix: on Windows run the helpers in Git Bash or WSL2, set CHROME to your chrome.exe path, and swap in fonts you have. Verified 3: scripts/render.sh:14 needs a separate FrameVelo checkout (FRAMEVELO_DIR, github.com/gnipbao/framevelo, not reviewed here). Fix: leave FRAMEVELO_DIR unset and render with npx --yes hyperframes@0.8.183 render. Verified 4: two optional extras use your accounts: a Douyin-logged-in Chrome through Claude in Chrome for topic research (README.md:97) and the Suno MCP added at user scope (README.md:98). Fix: skip both; song mode also works from your own audio via song_map.py --measure. Other: the starter loads GSAP 3.14.2 from cdn.jsdelivr.net (assets/starter/index.html:6, pinned version); fetch_classic.py only reads zh.wikisource.org (fetch_classic.py:21-22); check_narration.py:57 runs the episode's own narration.js in a node vm with only console exposed; other Python helpers call ffmpeg/ffprobe on local files and delete only their own temp frames (frame_audit.py:179, motion_audit.py:50, make_covers.py:248). No API keys, no telemetry. MIT.

## Safe install

Safe install (fixes applied):
Windows + Claude Code: install Node 22, Python 3.10+, uv, ffmpeg and Google Chrome from their official sites. In a new video workspace folder (Git Bash or WSL2): git clone https://github.com/gnipbao/vibe-zhishi .claude/skills/vibe-zhishi ; cd .claude/skills/vibe-zhishi ; git checkout fb813f0bcdfd8ee2ea546b7b5cfd565644e181ed. Set CHROME to your chrome.exe path. Tell Claude Code: use only npx --yes hyperframes@0.8.183, skip hyperframes@latest upgrade and skills update, no FrameVelo, no Suno MCP, no Douyin Chrome research. Keep normal permission prompts on (never --dangerously-skip-permissions). Run Python helpers with uv run (on Windows use py instead of python3).
claude.ai, Hermes, Android: not supported (needs local Node, ffmpeg, Chrome and Claude Code).

## YOLO install

YOLO (your own risk): skips the pinned commit and pinned HyperFrames. In the workspace: git clone https://github.com/gnipbao/vibe-zhishi .claude/skills/vibe-zhishi, run npx hyperframes skills update, and let Claude Code follow the references as written (including hyperframes@latest upgrade).

## Install notes

Safe with fixes: Claude Code skill that turns a topic into a code-drawn, beat-synced Douyin knowledge short (research, fact-check, HyperFrames build, SFX, frame audits, covers). Pin commit fb813f0 and hyperframes@0.8.183, skip @latest upgrade and skills update, Git Bash or WSL2 for .sh helpers with CHROME set, no FrameVelo, Suno MCP or Douyin Chrome. Chinese-language format; fits the faceless video channel idea.
