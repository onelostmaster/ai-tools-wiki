# Hermes Agent (Nous Research)

- **Type:** app
- **Category:** automation, Hermes add-ons
- **Official URL:** https://hermes-agent.nousresearch.com
- **GitHub repo:** https://github.com/NousResearch/hermes-agent (MIT; latest release v0.22.6 on 2026-11-02 per Hermes a review; the wiki review @9a56be3; a review bot targeted reads of /learn, write approval and /personality @8468f3c)
- **Price:** Free software (MIT, github.com, checked 2026-10-31). Optional Nous Portal plans: Free $0, Plus $20/month ($22 credits), Super $100, Ultra $200 (portal.nousresearch.com figures as quoted by gethermesagentai.com and jaymountconsulting.com; vendor page not readable without a browser, checked 2026-10-31). Update 2026-11-02 : Nous says every plan now includes one Cloud agent and more usage; the Portal page showed no plan prices today (portal.nousresearch.com, checked 2026-11-02), so the figures above may be out of date. Check the Portal before paying.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude (code review @9a56be3, fix-mode 2026-11-14): safe with fixes. Its SECURITY.md makes the OS the only boundary: run web-reading bots in the Docker backend or Hermes Cloud, not the PC's local backend. Never run hermes debug share (uploads message text to a public paste site); keep plugins.auto_apply off; /skills approval on before /learn; read third-party skills first. Good: deny-by-default chat users, no telemetry.

## Safe install

Safe install (fixes applied):
Download install.ps1 (or install.sh), read it, then run it, or use the MSIX from the official docs. Docker backend for any bot that reads web, X or YouTube; one profile per bot; /skills approval on; plugins.auto_apply off; never hermes debug share.

## YOLO install

YOLO (your own risk): skips the container, approvals and script read.
iex (irm https://hermes-agent.nousresearch.com/install.ps1) on the local backend.

## Install notes

Ask the user before installing.
Windows: in PowerShell run `iex (irm https://hermes-agent.nousresearch.com/install.ps1)` (official README); it installs under `%LOCALAPPDATA%\hermes`. A separate MSIX package is in the official installation docs (https://hermes-agent.nousresearch.com/docs/getting-started/installation).
Android: Termux only, from the signed APT repository in the official Termux guide (https://hermes-agent.nousresearch.com/docs/getting-started/termux), not the desktop installer.
Hermes: after installing run `hermes setup`, or `hermes setup --portal` to sign in to Nous Portal.
Hermes tips : `hermes plugins search <name>` searches the plugin catalog (replace <name> with a word for the plugin you want); `hermes sessions optimize` shrinks state.db and is documented as non-destructive. `hermes plugins install homeassistant --enable` is the official Nous plugin but gives the agent smart-home control, so enable it deliberately. `hermes tools --summary` is not in the docs (unconfirmed).
Setup rules (the wiki code review @9a56be3, 2026-11-01): run it in a container (the Hermes Cloud agent or Hermes's Docker image) for any bot that reads web, X or YouTube content, not on a PC's default local backend. One profile per bot, each with its own bot token and Notion integration. Never run `hermes debug share` (it uploads message text to a public paste site). Leave `plugins.auto_apply` off. Review third-party skills and plugins before adding them.
Hermes tips : `/learn` turns a workflow, docs folder, URL or book into a SKILL.md; the skill write-approval gate is OFF by default, so run `/skills approval on` first and check `/skills diff <id>` before `/skills approve <id>` (<id> = the pending skill's id). `/personality` lists 14 built-in styles, `/personality teacher` picks one, `/personality none` clears it; custom ones go under personalities: in `~/.hermes/config.yaml`, so read any you copy (prompt injection).
