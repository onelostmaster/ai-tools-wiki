# wllama

- **Type:** library
- **Category:** a project, research
- **Official URL:** https://github.com/ngxson/wllama
- **GitHub repo:** https://github.com/ngxson/wllama @ c10c211
- **Price:** Free, MIT (github.com/ngxson/wllama, checked 2026-11-07)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a project Claude (phase1-libraries.md §3, 2026-11-06) @ c10c211: safe. MIT WASM llama.cpp binding. User OK via PR #4; Installed 2026-11-08 (built from source by bench-web.yml, PR #7 merged). Repo/commit confirmed on github.com 2026-11-07.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: build from source at commit c10c211 with a project's SHA-pinned bench-web.yml workflow (GitHub Actions); no local install.

## YOLO install

YOLO (your own risk): skips the source build at the reviewed commit c10c211.
`npm install @wllama/wllama` (official npm package, latest 3.13.0 on 2026-11-14).

## Install notes

Windows / Claude Code: build from source at c10c211 with a project `bench-web.yml` workflow (GitHub Actions, SHA-pinned). Do not install elsewhere without a fresh OK.
