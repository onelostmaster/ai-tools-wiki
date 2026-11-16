# claude-figma-stack (Ootto)

- **Type:** app
- **Category:** social posting, automation
- **Official URL:** https://github.com/Ootto-AI/claude-figma-stack
- **GitHub repo:** https://github.com/Ootto-AI/claude-figma-stack @ 8813d75 (MIT; read by a review bot and Claude, a review)
- **Price:** Free (MIT, github.com, checked 2026-10-31); needs a Composio account and key.
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @55b8a6b (2026-11-15): safe with fixes, Skip. It replies and DMs through Composio (official Instagram API). The Action runs every 20 min (lead-monitor.yml:9) and pushes handled-comment IDs to your repo (lines 61-66). A non-empty dm_default DMs every new DM (comment_monitor.py:237-246); comments with no rule are deferred (line 106). Fix: private repo, seed first, dm_default empty, rules only for keywords you chose.

## Safe install

Safe install (fixes applied):
Private fork at 55b8a6b; run comment_monitor.py seed once; in auto_responses.json set dm_default to "" and keep only your own keyword rules; Composio key and IG IDs as GitHub secrets. Or delete the cron line and run scan / send by hand.

## YOLO install

YOLO (your own risk): skips the private repo, seed and empty default, so it auto-DMs everyone and publishes commenter IDs.
Fork publicly and enable the Action as the README says.

## Install notes

Ask the user before installing. Private fork at 55b8a6b; run comment_monitor.py seed once; in auto_responses.json set dm_default to "" and keep only your own keyword rules; Composio key and IG IDs as GitHub secrets. Or delete the cron line and run scan / send by hand.
