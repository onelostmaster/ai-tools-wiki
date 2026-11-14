# Agent Reach

- **Type:** CLI
- **Category:** research
- **Official URL:** https://github.com/Panniantong/Agent-Reach
- **GitHub repo:** [https://github.com/Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
- **Price:** Free (open-source code)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a review, 2026-10-30): Use with caution. Copies your Chrome site cookies into its own headless browser exposed on `localhost` CDP port `9222`; installs the latest OpenCLI extension unpinned with no checksum; sends URLs and queries to Jina/Exa; installs via `curl|sh` uv plus the latest release zip; auto-links its skill into `~/.claude` and `~/.hermes`. No telemetry or exfiltration found.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

No install steps: the source withholds them until the tool is rated safe. Read the Safety reason and ask the user first.
