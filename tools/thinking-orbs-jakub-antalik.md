# thinking-orbs (Jakub Antalik)

- **Type:** library
- **Category:** design, frontend, building a site
- **Official URL:** https://orbs.jakubantalik.com
- **GitHub repo:** https://github.com/Jakubantalik/thinking-orbs @ v0.3.1 (bd204b7; MIT)
- **Price:** Free (MIT LICENSE file and npm license field, checked 2026-11-22)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-22

## Safety reason

Claude code read @de85557 + npm 0.3.1/0.3.2 dist, 2026-11-22: safe with the Install notes fixes. No network, storage or eval in src/ or dist; no install scripts; zero runtime deps. Verified risk, fixed: npm latest 0.3.2 was built from commit 5e7afad, on no branch of the repo (registry gitHead); fix: pin 0.3.1 (= tag v0.3.1, read).

## Safe install

Safe install (fixes applied): React project on Windows (Claude Code or a terminal), inside the project folder, not global: npm install thinking-orbs@0.3.1 --save-exact --ignore-scripts. claude.ai artifacts and plain pages: in a scratch folder run npm pack thinking-orbs@0.3.1, copy dist/engine.es.js (19 KB) with its MIT notice and inline it in the artifact or page; no CDN link. Android: nothing to install; it runs in any page or artifact opened in the browser. Hermes: same npm command in a project folder on the Hermes host. No keys; no network at runtime.

## YOLO install

YOLO (your own risk): skips the 0.3.1 pin and --ignore-scripts: npm install thinking-orbs (gets latest 0.3.2, built from a commit on no branch of the repo).

## Install notes

Ask the user first. React: npm install thinking-orbs@0.3.1 --save-exact --ignore-scripts. Artifacts/plain pages: copy dist/engine.es.js (19 KB) from npm pack thinking-orbs@0.3.1, keep its MIT notice, inline it; no CDN. Runs on any web page or Claude artifact (canvas); React 18+ for the component.
