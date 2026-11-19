# KanjiVG

- **Type:** dataset
- **Category:** a project
- **Official URL:** https://kanjivg.tagaini.net
- **GitHub repo:** [https://github.com/KanjiVG/kanjivg](https://github.com/KanjiVG/kanjivg) (not in the Notion source; confirmed by web search, 2026-10-31)
- **Price:** Free (CC BY-SA 3.0; `kanjivg.tagaini.net`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot code and data read @9d7220d: safe with the fixes in Safe install. The SVGs are plain path data: no <script>, foreignObject or <!ENTITY> in any of the 11,941 files (searched the whole kanji/ folder). The Python tools (kvg.py, kvg_lookup.py, utils.py, make-index.py) have no network calls and no subprocess calls; they read and write files only in the folder you run them in. Verified behaviour and fixes: (1) each SVG's DOCTYPE points at the W3C SVG 1.0 DTD URL (kanji/04e00.svg:19); Python's own parser does not fetch it (xml.sax stops processing external entities by default since Python 3.7.1, per docs.python.org xml.sax; the repo's parser is plain xml.sax.parse, utils.py:71-73); fix: if you parse the files with another library, turn external DTD/entity loading off (for lxml: resolve_entities=False, no_network=True). (2) clean.py deletes kanjivg*.xml*, kanjivg*.zip, *~ backup files and the stripped/ folder in the current folder (clean.py:15-36), and updatepublic.sh runs gh release create (updatepublic.sh:16); both are maintainer tools; fix: don't run them, use the release files as data. (3) License is CC BY-SA 3.0 (COPYING): you must credit KanjiVG with a link to kanjivg.tagaini.net, and any modified SVGs you publish must stay CC BY-SA. Release r20260714 (2026-07-13 ET) has SHA-256 digests on GitHub for each asset; fix: check the digest after download.

## Safe install

Safe install (fixes applied): Claude Code on Windows: download kanjivg-20260714-main.zip (or -all.zip) from the official release https://github.com/KanjiVG/kanjivg/releases/tag/r20260714, check it in PowerShell with Get-FileHash kanjivg-20260714-main.zip -Algorithm SHA256 against b5df6cd2bc249dd49b8041eb99e38ba9f8dc6b9ea57962a80084b4a315d1a7fc (all.zip: 534bd222052f4960747ff624014e426b08052164a837b15044f58517e85e4db5), unzip into the project's data folder and use the SVGs as data. Don't run clean.py or updatepublic.sh. If code parses the SVGs, use Python's xml.sax/ElementTree (no DTD fetch) or turn external entity and network loading off in other parsers. Add the CC BY-SA 3.0 credit with a link to kanjivg.tagaini.net in the app. No keys, no network after download. claude.ai: upload single SVGs as files. Hermes: same download as data. Android: nothing to install; the SVGs render in the PWA.

## YOLO install

YOLO (your own risk): skips the SHA-256 check and the parser setting. git clone https://github.com/KanjiVG/kanjivg and point the app at the kanji/ folder (README).

## Install notes

Ask the user before adding it. Safe with the fixes in Safe install applied. Data only: kanji stroke-order SVGs for a project lessons; credit KanjiVG (CC BY-SA 3.0).
Official docs: https://kanjivg.tagaini.net
