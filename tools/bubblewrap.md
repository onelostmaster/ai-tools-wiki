# Bubblewrap

- **Type:** CLI
- **Category:** building a site, developer tools
- **Official URL:** https://github.com/GoogleChromeLabs/bubblewrap
- **GitHub repo:** https://github.com/GoogleChromeLabs/bubblewrap
- **Price:** Free (Apache-2.0)
- **Decision:** Try
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-15

## Safety reason

Not code-reviewed. Official GoogleChromeLabs repo, Apache-2.0. Claude's a project design run (2026-11-08) did a light read only (README, file tree, manifest). Only needed if a Play Store release is wanted; the advice was PWA first.

## Safe install

Safe install (fixes applied):
Unreviewed: contain it: only if a project PWA needs a Play Store listing. Windows: in a separate project folder, `npm install --save-exact @bubblewrap/cli@1.27.0` (npm latest on 2026-11-15, Node 18+) and run it with npx from that folder, not -g. `bubblewrap init` offers to download a JDK and the Android SDK into its own folder: accept only those official downloads. It creates your Android signing keystore: keep the keystore and its passwords out of git and out of chat, and back it up yourself. No other keys in the environment. Get a review before real use. claude.ai, Hermes and Android: no install route (the built app installs on Android).

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Windows: Node CLI from the official repo README; only if the PWA needs a Play Store listing. Review first.
