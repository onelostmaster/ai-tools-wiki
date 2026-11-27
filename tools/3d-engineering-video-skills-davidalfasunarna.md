# 3D Engineering Video skills (davidalfasunarna)

- **Type:** skill
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/davidalfasunarna/3d-engineering-video-claude-skills
- **GitHub repo:** https://github.com/davidalfasunarna/3d-engineering-video-claude-skills @ 8978568 (GPL-3.0)
- **Price:** Free on GitHub, GPL-3.0 (github.com, checked 2026-11-26); Higgsfield credits are a separate paid service (price not checked)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-26

## Safety reason

Not code-reviewed for safety. README: needs Claude with skills and code execution, plus a paid Higgsfield account with credits connected as an MCP connector (voice, audio sandbox, GPU); on first use the skill clones the repo and installs Blender as a Python module (about 1 GB) in Claude's workspace; a ~70 s video costs about 75–85 GPU credits plus ~6 per voice take; tested only in the Claude app, not Claude Code. Repo contains no credentials. Repo, license and latest commit confirmed from github.com metadata, 2026-11-26.

## Safe install

Unreviewed: contain it: upload only from the pinned commit 8978568 in claude.ai (its cloud workspace is the sandbox), set a low Higgsfield credit cap before the first render, no other connectors on that chat. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
claude.ai: upload the skill ZIPs (skills/) in Settings → Capabilities → Skills and connect the Higgsfield connector (README).
