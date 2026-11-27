# SoundKit (Soundza)

- **Type:** skill
- **Category:** voice and audio, generating videos
- **Official URL:** https://soundza.com/soundkit
- **GitHub repo:** https://github.com/soundza/soundkit @ c9ec55f (code MIT, audio CC0)
- **Price:** Free on GitHub, MIT code + CC0 audio (github.com, checked 2026-11-25); Soundza account features: price unknown
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-26

## Safety reason

a review bot read @c9ec55f: safe with these fixes. The repo is 225 CC0 sound effects (embedded as base64 MP3 in .ts modules) and 25 CC0 music beds (LICENSE-AUDIO), a Remotion component, and one agent skill with a Node helper. No hooks, no MCP server, no eval or child_process. Verified 1: 'npx shadcn add @soundza/<name>' or https://soundza.com/r/<name>.json (README:31-34, 48) installs whatever soundza.com serves at that moment, not the repo's files (scripts/sync.mjs:6-9 pulls the registry from soundza.com). Fix: copy the sound .ts files and lib/soundza.ts from registry/soundza/ at the pinned commit instead; music beds: download the MP3 named in the module (README:102-105) once and keep it. Verified 2: the skill's helper only works with a Soundza account: SKILL.md:18 tells the agent to run 'soundza signin' (Google sign-in) for search, add and generate, and soundza.mjs:277-287 appends the key in plain text to the project's .env and adds .env to .gitignore. Sounds it downloads come under the Soundza Standard License, not CC0 (SKILL.md:10; soundza.mjs:265), and 'generate' sends your prompt to api.soundza.com for AI-generated takes (soundza.mjs:135-147; SKILL.md:57). Fix: don't install the skill or run signin; use the CC0 files only. If you choose the account later, sign in yourself, keep the key out of shared projects, and credit Soundza as CREDITS.md says. Verified 3: every sound module and lib/soundza.ts carry a comment telling agents to sign the person in and then search and download on their own (e.g. registry/soundza/sounds/air-whoosh.ts:9, lib/soundza.ts:8). Fix: treat it as an ad; tell your agent not to act on comments in these files. MIT code, CC0 audio.

## Safe install

Safe install (fixes applied):
Claude Code or any Remotion/React project (Windows): git clone https://github.com/soundza/soundkit ; cd soundkit ; git checkout c9ec55f61fcbc784f1f0d1390c7a6f79b0e68cd4 ; copy registry/soundza/lib/soundza.ts (and components/soundza-remotion.tsx for Remotion) plus the sound .ts files you want from registry/soundza/sounds/ into your project (instead of npx shadcn add, which installs what soundza.com serves). Music beds: download the MP3 named in the module once into public/sounds/. Don't install the soundza-remotion skill or run signin/generate; no account or key. Tell your agent not to act on the 'Agents: sign the person in' comments.
claude.ai, Hermes, Android: not supported (project files for a local Remotion/React build).

## YOLO install

YOLO (your own risk): skips the pinned files and the no-account rule. README: npx shadcn add @soundza/remotion @soundza/<name>, npx skills add soundza/soundkit, and let the skill run 'soundza signin' (key saved in .env) to search, download and generate Soundza-licensed sounds.

## Install notes

Safe with fixes: 225 CC0 sound effects and 25 CC0 music beds for Remotion/React with hit points, copied from the pinned commit c9ec55f instead of shadcn adds; skip the Soundza skill and sign-in (account-only, non-CC0 library, key in .env); ignore the agent-directed sign-in comments. Fits the faceless video channel idea and a project reels.
