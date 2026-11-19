# IconPark (ByteDance; archived)

- **Type:** library
- **Category:** design, frontend
- **Official URL:** https://iconpark.oceanengine.com
- **GitHub repo:** https://github.com/bytedance/IconPark @8dc132da, 9,034 stars; latest default-branch commit 2023-02-24 02:46 ET; original nonfork; archived=True
- **Price:** Free Apache-2.0 icon library (LICENSE), current official repo metadata; no library fee. unverified: the hosted site's terms and privacy (the source license does not cover them); containment: use the Apache-2.0 source package, not the hosted site.
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Claude code read @8dc132d (2026-11-18): safe with fixes. Archived since 2023-02-24. @icon-park/react 1.4.2 is Apache-2.0 with no install scripts (npm registry; packages/react/package.json:2-4); icons are generated from local data. The root build scripts publish and run rm -rf; never run them. Fix: the npm package pinned, or static SVGs.

## Safe install

Safe install (fixes applied):
npm install @icon-park/react@1.4.2 --ignore-scripts, or copy static SVGs; never run the repo root scripts; prefer the Energy Icons row for new work.

## YOLO install

YOLO (your own risk): skips the pin.
Clone the repo and run its build.

## Install notes

CAUTION: read Safety reason; specific approval required before installation/connection. Documented only in official packages/react/README.md: npm install @icon-park/react --save. Not recommended to build archived root; use reviewed static SVG if needed. Windows/Android web assets; no native Claude/Hermes MCP verified; Hermes compatibility untested.
