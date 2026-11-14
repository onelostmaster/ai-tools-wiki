# opencode

- **Type:** CLI
- **Category:** developer tools
- **Official URL:** https://opencode.ai
- **GitHub repo:** https://github.com/anomalyco/opencode @ 21e66f2 (MIT; formerly sst/opencode)
- **Price:** Free, open source (MIT) (github.com, checked 2026-11-01); model providers bill separately
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (pattern scan plus targeted reads @21e66f2, a review), 2026-11-01; Claude fit review only (scan stands): caution. Permissive defaults: most tools incl. bash and file edits run without asking (docs `permissions.mdx:174-177`); README pushes curl | bash installer; update checks are notify-only. New since v2.2.2 (2026-10-29): image_generate is on by default when an image-capable provider is connected (official release notes, PR #60258), so agents can spend image credits unasked. New code not reviewed.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code (local only): no install steps given (the source withholds them until the tool is rated safe); see `https://opencode.ai`.
Any platform: since v2.2.2 the image_generate tool is on by default with an image-capable provider; turn `experimental.image_generate` off if you don't want paid image calls (release notes v2.2.1/v2.2.2).
