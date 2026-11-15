# Transformers.js (@huggingface/transformers)

- **Type:** library
- **Category:** voice and audio, a project
- **Official URL:** https://github.com/huggingface/transformers.js
- **GitHub repo:** https://github.com/huggingface/transformers.js (npm @huggingface/transformers 4.3.2)
- **Price:** Free, Apache-2.0 (github.com/huggingface/transformers.js, checked 2026-11-07)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a project Claude (phase1-libraries.md §4, 2026-11-06) npm 4.3.2: safe. Apache-2.0 (onnxruntime-web MIT). Browser STT for the bench page. User OK via PR #4. Repo confirmed on github.com 2026-11-07.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: in the project folder `npm install -E @huggingface/transformers@4.3.2` (the version a project reviewed); load only the models the project lists, each with a pinned `revision`, so the runtime model download is a fixed, reviewed file.

## YOLO install

YOLO (your own risk): skips the exact pin and the pinned model revisions.
`npm install @huggingface/transformers`

## Install notes

Windows / Claude Code: npm dependency @huggingface/transformers@4.3.2 in bench/web (as a project). Models download at runtime — pin versions and review model sources before any new install.
