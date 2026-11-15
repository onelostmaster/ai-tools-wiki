# Notion connector

- **Type:** connector
- **Category:** Notion and productivity
- **Official URL:** https://www.notion.com
- **GitHub repo:** unknown
- **Price:** Included (connector); Notion plan separate
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Notion (official vendor connector; not code-reviewed, 2026-10-31): safe. a project lists it as safe because it is already connected; a project, a project and a project all use it for their hub and memory pages.

## Safe install

Safe install (fixes applied):
claude.ai (Windows browser and Android app): add Notion at claude.ai/customize/connectors (or the Connect card in chat) and, on Notion's consent screen, pick only the pages each project needs instead of the whole workspace. Claude Code: uses the connector added in claude.ai; nothing extra to install. Android: the Claude app uses the same connector once added.

## YOLO install

Not written yet.

## Install notes

claude.ai: add it at `claude.ai/customize/connectors` (or tap the Connect card Claude shows in chat).
Claude Code: connectors added in `claude.ai` are available to Claude Code on the web.
Android: the Claude app on the phone uses the same connector once it is added (a project: works from the phone).
Tip (2026-11-02, from a review bot, also true for the Notion API): table blocks keep their text in child table_row cells, so a reader that prints only rich_text shows README tables as empty; fetch the table rows too.
Tip (2026-11-06, from a project): to add a row to a table with update_content, replace the table's last row with itself plus the new row, with no blank line between them; a blank line leaves the new row outside the table as plain text with escaped bars — re-fetch the page and check.
Tip (2026-11-07, from a review bot): a script that reads blocks through the Notion API must turn an a Notion page page URL into the bare page id first; the blocks API answers HTTP 400 to a raw URL.
