# GitHub MCP server (official)

- **Type:** MCP
- **Category:** developer tools
- **Official URL:** https://github.com/github/github-mcp-server
- **GitHub repo:** https://github.com/github/github-mcp-server @ 3366807 (MIT; pushed 2026-11-02)
- **Price:** Free with a GitHub account
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-17

## Safety reason

Claude docs read @67d4dc4 v2.2.0 (2026-11-17): safe with fixes. A token gives the agent whatever it can do on your repos, and issue or PR text can carry prompt injection. --read-only / GITHUB_READ_ONLY=1 drops write tools (README.md:1716-1729); lockdown mode filters public-repo content from people without push access (:1733-1750). Fix: read-only, lockdown, a fine-grained token.

## Safe install

Safe install (fixes applied):
Fine-grained PAT on chosen repos only, stored as a secret; claude mcp add github -e GITHUB_PERSONAL_ACCESS_TOKEN -e GITHUB_READ_ONLY=1 -e GITHUB_LOCKDOWN_MODE=1 -- docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN -e GITHUB_READ_ONLY -e GITHUB_LOCKDOWN_MODE ghcr.io/github/github-mcp-server:v2.2.0.

## YOLO install

YOLO (your own risk): skips read-only, lockdown and the pin.
Classic all-repo token on :latest with write tools on.

## Install notes

Ask the user before installing.
Claude Code: use the remote server or the local binary/Docker image, in read-only mode with a fine-grained token.
Hermes: works as a plain MCP server.
Windows: Docker, binary or remote server. Android: no.
