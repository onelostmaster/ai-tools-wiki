# Remotion (framework, v4)

- **Type:** library
- **Category:** generating videos, editing
- **Official URL:** https://www.remotion.dev
- **GitHub repo:** https://github.com/remotion-dev/remotion (official org remotion-dev, same as the official skills and Claude Code plugin repos; given in the liked list, a review; no code read)
- **Price:** Free for individuals, non-profits and companies of up to 3 people; company license: Remotion for Creators $25/mo per seat, Remotion for Automators $0.01 per render ($100/mo minimum), Enterprise from $500/mo (`remotion.dev`, checked 2026-10-31)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-26

## Safety reason

Remotion (official vendor; the framework itself was not code-reviewed: a review bot listed it as already in use, a project a review, 2026-10-31): safe. Its official agent skills and Claude Code plugin were read and rated safe . Renders run in headless Chromium; with no GPU on the cloud machine it uses the swangle renderer (Pipeline & commands).

## Safe install

Safe install (fixes applied):
Windows/Claude Code: in the project folder `npm install -E --no-fund --no-audit remotion@4.0.539 @remotion/cli@4.0.539 @remotion/three@4.0.539 @remotion/media-utils@4.0.539 react@19 react-dom@19 three@0.186.1 @react-three/fiber@9.8.2 typescript @types/react @types/three` (a project's pinned set, about 340 MB), never `npm install -g`. Unverified: the framework code (not reviewed): keep it local to the project folder, no API keys in its env. Cloud renders use software WebGL (set in remotion.config.ts). Licence: free for individuals and companies of up to 3 people. Android: not used.

## YOLO install

YOLO (your own risk): skips the exact pins.
`npx create-video@latest`

## Install notes

Claude Code: new project: `npx create-video@latest` (Remotion docs).
Claude Code: a project's pinned install: `npm install --no-fund --no-audit remotion@4.0.539 @remotion/cli@4.0.539 @remotion/three@4.0.539 @remotion/media-utils@4.0.539 react@19 react-dom@19 three@0.186.1 @react-three/fiber@9.8.2 typescript @types/react @types/three` (rubber-short commands, a project Resources; about 340 MB of `node_modules`).
Claude Code: no GPU in the cloud, so renders use software WebGL (SwiftShader, set in `remotion.config.ts`).
Claude Code: for agent help, add the Remotion agent skills or the Remotion Claude Code plugin (separate rows).
