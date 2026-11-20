# kamiya-codec

- **Type:** library
- **Category:** a project
- **Official URL:** https://github.com/fasiha/kamiya-codec
- **GitHub repo:** https://github.com/fasiha/kamiya-codec @ f53fc32 (4.16.1; Unlicense; confirmed via the npm package's repository field and github.com 2026-11-19)
- **Price:** Free (Unlicense; checked 2026-11-19)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

a review bot code read: safe. Pure string-conjugation code in three TypeScript files (index.ts 851 lines, adjective.ts 129, hiragana.ts 41); the only import is ./hiragana (index.ts:1). No runtime dependencies and no preinstall, install or postinstall scripts in package.json (only test, format, bundle, build). The published bundles dist/kamiya.cjs, dist/kamiya.min.mjs and dist/kamiya.min.js contain no require, import(), fetch, XMLHttpRequest, child_process, process., eval or Function( calls (searched 2026-11-19), and the npm tarball's .ts sources and dist/ folder are byte-identical to the repo at f53fc32. No verified risk, so no fix is needed beyond pinning the version.

## Safe install

Safe install (fixes applied): Claude Code on Windows (or a project container), in a project folder, not global: npm install kamiya-codec@4.16.1 --save-exact. Check that package-lock.json shows integrity sha512-1AwY8W6KQ8/+U99Sm7Q9dNeExKpKZvOXnyCj2adg9yKBZJzXvmqN7ePn2tp8hHmu2t8CB74h+m9GF7LonfacfA== (npm registry, checked 2026-11-19). No API keys needed; no network after install. claude.ai and Android: not installable; use its conjugation output in cards. Hermes: same npm command on the Hermes host.

## YOLO install

YOLO (your own risk): skips the version pin and integrity check: npm install kamiya-codec (latest).

## Install notes

Safe as reviewed (no fixes needed beyond the pinned version). Japanese verb and adjective conjugation and deconjugation (conjugate, conjugateAuxiliaries, verbDeconjugate, adjConjugate, adjDeconjugate), based on Taeko Kamiya's handbooks; works offline.
Official repo: https://github.com/fasiha/kamiya-codec (linked from the npm package). In a project container, npm installs last one session.
