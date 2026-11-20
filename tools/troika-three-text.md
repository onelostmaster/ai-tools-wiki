# Troika (three-text)

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/protectwise/troika
- **GitHub repo:** https://github.com/protectwise/troika
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @9c89d51 + npm troika-three-text 0.53.1 (2026-11-19): safe with fixes. Default fonts load from Google Fonts and jsDelivr (packages/troika-three-text/README.md:154,361); text.font and configureTextBuilder(\{unicodeFontsURL\}) point them at your host (:363-379). The worker built from a blob is switched off with useWorker:false (:410-417). npm 0.53.1 has no install scripts. Fix: self-hosted fonts, pin.

## Safe install

Safe install (fixes applied):
Windows Claude Code or any three.js web project: npm install troika-three-text@0.53.1 three (packages/troika-three-text/README.md:42,48; the npm package has no install scripts; the repo-root postinstall at package.json:40 only runs if you clone the monorepo, so don't). By default it loads Roboto from the Google Fonts CDN (README.md:154) and unicode fallback fonts from jsDelivr (README.md:361): always set text.font to a font file you host yourself, and set unicodeFontsURL to your own copy (README.md:363-379) if you need fallback glyphs, so no font requests leave your site. Not a claude.ai or Hermes tool. For a strict CSP, also call configureTextBuilder(\{ useWorker: false \}) (README.md:410-417).

## YOLO install

YOLO (your own risk): skips the version pin and self-hosted fonts (fonts load from Google Fonts and jsDelivr).
npm install troika-three-text three

## Install notes

Not installed. Ask the user before any installation, including Try. Browser library for your own three.js pages; runs on Windows and Android browsers with WebGL; unverified: your phone's GPU support (test the page on it). No native Claude skill/MCP in this repo.
