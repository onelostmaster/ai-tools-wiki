# stickman-video-director (kaomei)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/kaomei/stickman-video-director
- **GitHub repo:** https://github.com/kaomei/stickman-video-director @ 7fa6a9a (MIT)
- **Price:** Free on GitHub, MIT (LICENSE file, checked 2026-11-20); image, voice and video services it connects bill separately (README FAQ)
- **Decision:** Later
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-20

## Safety reason

Not code-reviewed for safety. Unverified: the skill scripts and the agent-led setup (README Step 1 has the agent install missing tools itself) -> Contain: pinned commit, manual install guide instead of agent self-install, no keys. README states image, voice and video engines (Gemini, ElevenLabs, Google Flow) bill your own accounts. Commit and LICENSE confirmed on github.com, 2026-11-20.

## Safe install

Unreviewed: contain it: clone into a separate project folder on Windows, git checkout 7fa6a9a, follow skills/directing-stickman-videos/references/installation-troubleshooting.md by hand instead of letting the agent self-install, add no API keys until reviewed, keep Claude Code's normal permission prompts on (never --dangerously-skip-permissions). Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Contain it: clone into a separate project folder on Windows, git checkout 7fa6a9a, follow skills/directing-stickman-videos/references/installation-troubleshooting.md by hand instead of letting the agent self-install, add no API keys until reviewed, keep Claude Code's normal permission prompts on (never --dangerously-skip-permissions).
