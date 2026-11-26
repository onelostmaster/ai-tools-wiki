# Aria (Abhinav-murugan1)

- **Type:** skill
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/Abhinav-murugan1/Aria
- **GitHub repo:** https://github.com/Abhinav-murugan1/Aria @ ffe2a54 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-12)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-25

## Safety reason

a review bot read @ffe2a54: safe with these fixes. Four Claude Code skills (aria, aria-video, aria-voice, aria-launch) plus /aria-* commands that make narrated videos from React/TypeScript code, rendered on your GPU by the raea engine, with local voices (Chatterbox Turbo, Kokoro) and faster-whisper word timing. Its own code has no network calls, no keys and no uploads; the skills tell the agent to confirm before any upload and upload as private (aria/SKILL.md:59), and aria-launch skips .env, key and token files (aria-launch/SKILL.md:60-62). MIT. Verified 1: install.ps1:20 runs 'irm https://raea.io/install.ps1 | iex' when %USERPROFILE%\.raea\\bin\\raea.exe is missing. That installer takes the newest raea release, checks its SHA-256, adds raea to your user PATH and copies raea's skills into %USERPROFILE%\.claude\\skills, replacing same-name folders (raea install.ps1:30-49, 62-64, 79-84). Fix: install raea yourself first from a chosen release zip (below), so line 20 is skipped. Unverified: raea's engine code (shinyobjectz/raea, not reviewed by a review bot); containment: a checksum-checked release zip, no raea skills copied, no keys in its environment. Verified 2: install.ps1:22 and 57-59 permanently set ARIA_ENGINE and add the clone's bin folder to your user PATH. Fix: keep the clone where it is (INSTALL.md:22) and accept these two user settings, or run python tools\\aria.py instead of aria (INSTALL.md:21). Verified 3: plain install.ps1 deletes and recopies the aria, aria-video, aria-voice, aria-launch and aria-brag folders in %USERPROFILE%\.claude\\skills (install.ps1:33-43). Fix: keep nothing of your own under those names, and use one route only (INSTALL.md:39). Verified 4: -Voice installs ~5 GB (CUDA torch 2.6.0, chatterbox-tts 0.1.7, faster-whisper 1.2.1; install.ps1:66-78) and the first narration downloads the Turbo and whisper models (~3 GB, install.ps1:80). Fix: add -Voice only when you want narration, with network on for that first run. Verified 5: INSTALL.md:14 clones main. Fix: check out commit ffe2a54. Needs Windows 10/11 with a DirectX 12 or Vulkan GPU and ffmpeg; voice wants an NVIDIA GPU with ~6 GB VRAM (INSTALL.md:6-7).

## Safe install

Safe install (fixes applied):
Claude Code (Windows, PowerShell): 1) raea engine: from https://github.com/shinyobjectz/raea/releases download raea-<version>-windows-x86_64.zip and its .sha256, compare with (Get-FileHash <zip> -Algorithm SHA256).Hash, extract it and put its raea\\bin folder at "$env:USERPROFILE\.raea\\bin" (so raea.exe is at .raea\\bin\\raea.exe). Don't run the irm | iex line. 2) git clone https://github.com/Abhinav-murugan1/Aria ; cd Aria ; git checkout ffe2a54fb66fb7fa12d4c83618106bfeba0f38c4 ; ./install.ps1 (copies the 4 aria skills and /aria-* commands from this pinned clone, sets ARIA_ENGINE, adds Aria\\bin to your user PATH). Add -Voice only for narration (~5 GB, then ~3 GB of models on the first narration). Open a new terminal, then aria doctor. Don't use the /plugin marketplace route as well, and don't git pull.
claude.ai, Hermes, Android: not supported (needs a local Windows GPU toolchain).

## YOLO install

YOLO (your own risk): skips the pinned commit and the manual raea install. INSTALL.md:13-16 and 31-34: git clone (main), ./install.ps1 -EngineOnly -Voice (runs irm https://raea.io/install.ps1 | iex, which installs the newest raea and its skills), then /plugin marketplace add Abhinav-murugan1/Aria and /plugin install aria@aria.

## Install notes

Safe with fixes: Windows-first Claude Code skills that write a video as React/TypeScript, render it on your GPU with the raea engine and narrate it with local expressive voices and word-timed captions; nothing uploads unless you publish. Install raea yourself from a checksum-checked release zip so install.ps1 skips its irm | iex line, pin ffe2a54, -Voice only when you want narration. Good reference for the faceless video channel idea; Decision Skip kept. raea itself has no wiki row yet.
