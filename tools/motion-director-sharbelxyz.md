# motion-director (sharbelxyz)

- **Type:** skill
- **Category:** generating videos, editing
- **Official URL:** https://github.com/sharbelxyz/motion-director
- **GitHub repo:** https://github.com/sharbelxyz/motion-director @ a21ffbf (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-16)
- **Decision:** Later
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-16

## Safety reason

Not code-reviewed for safety. README (commit a21ffbf): no accounts, no API keys, nothing uploaded; the one-line install is curl ... install.sh | bash and installs into every agent it finds; first run fetches Node 22+, FFmpeg and the HyperFrames renderer with headless Chrome, and a headless browser reads your website for brand assets, stored in ~/motion-director/brands. Repo, license and latest commit confirmed from github.com metadata, 2026-11-16.

## Safe install

Unreviewed: contain it: download the repo at the pinned commit a21ffbf (not the moving main branch), copy only skills/motion-director into one agent's skills folder by hand (never the curl | bash one-liner, which installs into every agent it finds), run it in a sandbox or devcontainer with no API keys, and let it reach the network only for the first-run setup downloads and your own site. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Windows (README): install Node.js 22+ and FFmpeg, then copy skills/motion-director into %USERPROFILE%\.claude\\skills\\ for Claude Code. The curl|bash one-liner is macOS/Linux only and installs into every agent it detects; use the by-hand copy instead.
