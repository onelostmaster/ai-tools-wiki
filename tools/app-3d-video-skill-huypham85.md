# app-3d-video-skill (huypham85)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/huypham85/app-3d-video-skill
- **GitHub repo:** https://github.com/huypham85/app-3d-video-skill @ 0661ec0 (license unclear (github.com reported NOASSERTION))
- **Price:** Free, MIT (LICENSE file @0661ec0; GitHub shows NOASSERTION), checked 2026-11-25
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-25

## Safety reason

a review bot read @0661ec0: safe with these fixes. Two Claude Code skills (app-3d-video and motion-video) that render a 20-second vertical 3D promo for an iOS app with Swift (SceneKit, CoreGraphics, AVFoundation) compiled locally by swiftc. No network calls, no keys, no hooks or MCP server; the only URL is a sample video link in README.md:8. MIT (LICENSE; GitHub shows NOASSERTION only because of its detection). Verified 1: it runs only on macOS with Xcode command line tools (README.md:18-19; mv3d.sh:14 swiftc), so it does not run on Windows, Android, claude.ai or Hermes. No fix for your platforms. Verified 2: README.md:28 clones main with no pin. Fix: check out commit 0661ec0. Verified 3: mv3d.sh:10 and mv.sh:52 load project.env as shell code (source), and mv3d.sh:27 / mv.sh:70 paste the stills beat list into a python -c command. Fix: keep project.env to the five number settings (BPM, DURATION, W, H, FPS) and pass beats as plain numbers only. Verified 4: the renderer deletes an existing file at the output path before writing (video_main.swift:56) and mv3d.sh:28, 36 delete the project's stills/ and check/ folders on each run. Fix: give each render a new output name and keep nothing of your own in those folders.

## Safe install

Safe install (fixes applied):
Not installable on your platforms: it needs macOS with Xcode command line tools (README.md:18-19).
Claude Code (Windows), claude.ai, Hermes, Android: not supported.

## YOLO install

YOLO (your own risk): skips the pinned commit (README.md:27-31 clones main and copies both folders into the skills folder). Same platform limit: no Windows or Android install exists.

## Install notes

Safe with fixes, but macOS-only (Swift, SceneKit, Xcode tools), so it does not run on Windows or Android. If ever used elsewhere: pin 0661ec0, keep project.env to number settings, plain beat numbers, a new output name per render. Decision Skip kept; reference only for the faceless video channel idea.
