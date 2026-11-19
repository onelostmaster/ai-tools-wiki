# magpie (yetone)

- **Type:** app
- **Category:** research
- **Official URL:** https://usemagpie.ai
- **GitHub repo:** https://github.com/yetone/magpie @ 4ae833f (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-11)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-18

## Safety reason

Not code-reviewed by a review bot. A project Tool Scout (Claude, 2026-11-11, README only) rated it 0.5/5 and said avoid for us: it reads Claude Code sign-ins and pings home daily (scout claim, not checked by a review bot). The README confirms it edits each agent's config, stores provider keys and plan sign-ins, and its quick start pipes a downloaded script into the shell. Repo, licence and commit confirmed from github.com metadata, 2026-11-11.

## Safe install

Unreviewed: contain it: run it only in a throwaway VM, Windows Sandbox or Docker container with no real agent configs, keys or plan sign-ins in it, pin the reviewed commit 4ae833f (official repo github.com/yetone/magpie), and give it network only to the model endpoints you test. It edits the coding agents' own config files and handles their keys and sign-ins (README), so never point it at your real Claude Code config. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Do not install: it would take over Claude Code's model settings and sign-ins. README lists Windows, Linux, Docker and Termux (Android) builds.
