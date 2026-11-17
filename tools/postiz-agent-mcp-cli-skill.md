# Postiz agent (MCP + CLI + skill)

- **Type:** MCP
- **Category:** social posting
- **Official URL:** https://postiz.com
- **GitHub repo:** [https://github.com/gitroomhq/postiz-agent](https://github.com/gitroomhq/postiz-agent)
- **Price:** Self-host free (AGPL); cloud from $29/mo, 7-day trial, no free plan (postiz.com, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @01ab1fe (2026-11-16): safe with fixes. The skill tells the agent to run npm install -g postiz (skills/postiz/SKILL.md:11) and to push agent-media (lines 807-814). postiz auth:login opens the server's URL through a shell exec (src/commands/auth.ts:48-52); API-key auth skips that. It posts to your social accounts. Fix: pinned npx, POSTIZ_API_KEY, delete the agent-media lines, ask before each post.

## Safe install

Safe install (fixes applied):
Copy the skill at 01ab1fe; replace npm install -g postiz with npx -y postiz@2.0.27; delete SKILL.md lines 807-814; set POSTIZ_API_KEY in env (no auth:login); ask before every post.

## YOLO install

YOLO (your own risk): skips the pin, key auth and post approval.
npm install -g postiz, postiz auth:login, let the agent post.

## Install notes

Ask the user before installing. Copy the skill at 01ab1fe; replace npm install -g postiz with npx -y postiz@2.0.27; delete SKILL.md lines 807-814; set POSTIZ_API_KEY in env (no auth:login); ask before every post.
