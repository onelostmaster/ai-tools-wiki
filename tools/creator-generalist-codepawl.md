# creator-generalist (codepawl)

- **Type:** skill
- **Category:** 3D and games, generating videos
- **Official URL:** https://github.com/codepawl/creator-generalist
- **GitHub repo:** https://github.com/codepawl/creator-generalist @ 7235f50 (MIT; HEAD on 2026-11-14, latest commit on 2026-11-12 ET; plugins 2d-generalist 0.12.3, 3d-generalist 0.11.8)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-13)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read @7235f50, 2026-11-14, no-intake review): Safe, with content caveats. 272 files: five plugins of SKILL.md files and Markdown references plus Python/Node helper scripts (render checks, contact sheets, foley, transcription, game probes). Plugin manifests (.claude-plugin/marketplace.json and five plugin.json files) declare no hooks and no MCP servers. Scanned every .py, .mjs and .sh script: subprocesses are only ffmpeg, ffprobe, yt-dlp, nvidia-smi and the scripts themselves (plus a PowerShell speech call in a Windows test, test_watch_video.py line 397); no eval, shell=True, curl-pipe-to-shell or obfuscated code. Network only to documented hosts: api.elevenlabs.io (generate_elevenlabs.py line 31, your own key), fal.ai (fal_foley.py line 29, your own key), Openverse, archive.org, OpenGameArt, incompetech, myinstants, YouTube via yt-dlp, and Hugging Face/PyTorch model downloads; keys are read from env or your own config files and are not sent elsewhere. No prompt-injection phrases found in the Markdown. Caveats: fetch_web.py line 9 says myinstants clips have no licence, and YouTube downloads are their owners' copyrighted videos, so check licences before using clips in the faceless channel; INSTALL.md asks the agent to install tools after you say yes. Replaces the earlier not-reviewed status.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): `git clone https://github.com/codepawl/creator-generalist`, `git -C creator-generalist checkout 7235f50` (the reviewed commit), then in Claude Code `/plugin marketplace add ./creator-generalist` (local folder) and `/plugin install <name>@creator-generalist` only for the plugins you want (INSTALL.md:31-37). Keep marketplace auto-update off. When INSTALL.md's audit asks to install Blender, Node/Playwright, yt-dlp or other system-wide tools, answer no to each one you do not need. ElevenLabs and fal.ai keys go in environment variables (generate_elevenlabs.py:31, fal_foley.py:29), only if you want those features. Clips from myinstants carry no licence (fetch_web.py:9) and YouTube clips belong to their owners: use neither in published videos without a licence.

## YOLO install

YOLO (your own risk): skips the commit pin, the local marketplace and the per-tool no answers.
/plugin marketplace add codepawl/creator-generalist
/plugin install <name>@creator-generalist (each of the five plugins)

## Install notes

Code-reviewed by a review bot @7235f50 (safe, with the content caveats below). Five Claude Code plugins in one marketplace: 3d-generalist, 2d-generalist, game-generalist, watch-video, design-sound. Claude Code on Windows: in Claude Code type /plugin marketplace add codepawl/creator-generalist, then /plugin install <name>@creator-generalist for only the plugins you want (INSTALL.md lines 31-37). Keep auto-update off so a later version is not pulled in without a new review. The helper scripts need Python 3.10+, ffmpeg/ffprobe, and for some steps Blender, Node.js with Playwright, or yt-dlp; INSTALL.md tells the agent to run an audit script and ask before installing anything system-wide, so say no to anything you do not need. Optional paid keys: ElevenLabs (ELEVENLABS_API_KEY or ~/.config/elevenlabs/api_key.txt) and fal.ai (FAL_KEY) for design-sound; use your own keys only if you want those features. Some watch-video and design-sound steps download large local AI models (Hugging Face) and want an NVIDIA GPU. claude.ai and Android: not a fit (the scripts need a local computer).
