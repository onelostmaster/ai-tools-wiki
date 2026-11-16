# Agent Reach

- **Type:** CLI
- **Category:** research
- **Official URL:** https://github.com/Panniantong/Agent-Reach
- **GitHub repo:** [https://github.com/Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
- **Price:** Free (open-source code)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @c70ae6d = v1.6.1 (2026-11-15): safe with fixes, Skip. Rewritten since the old review: it uses its own browser profile with CDP on 127.0.0.1 only (runtime/browser_watcher.py:90), not your Chrome cookies. The unpinned latest OpenCLI extension (runtime/browser.py:72) is fetched only for browser channels, and no default channel uses one. Fix: pin the release, keep default channels. Web reads go to Jina or Exa.

## Safe install

Safe install (fixes applied):
uv tool install https://github.com/Panniantong/Agent-Reach/releases/download/v1.6.1/agent-reach.zip, then agent-reach setup (default channels only). Never add opencli or boss-agent-cli channels (facebook, instagram, linkedin, reddit, twitter, xiaohongshu, boss).

## YOLO install

YOLO (your own risk): skips the pin and the channel limit, so it pulls the latest OpenCLI extension unverified.
Install from releases/latest as docs/install.md says and add every channel.

## Install notes

Ask the user before installing. uv tool install https://github.com/Panniantong/Agent-Reach/releases/download/v1.6.1/agent-reach.zip, then agent-reach setup (default channels only). Never add opencli or boss-agent-cli channels (facebook, instagram, linkedin, reddit, twitter, xiaohongshu, boss).
