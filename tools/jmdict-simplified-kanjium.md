# jmdict-simplified + kanjium

- **Type:** dataset
- **Category:** a project
- **Official URL:** https://github.com/scriptin/jmdict-simplified
- **GitHub repo:** https://github.com/scriptin/jmdict-simplified @ ed06ae7 (release 3.6.2+20261116213322) · https://github.com/mifunetoshiro/kanjium @ 9ebca45 (both confirmed on github.com 2026-11-19)
- **Price:** Free (JMdict/JMnedict/RADKFILE data: EDRDG licence; Kanjidic, kanjium and other jmdict-simplified files: CC BY-SA 4.0; npm loader MIT; checked 2026-11-19)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

a review bot code and data read: safe with the fixes in Safe install. Both are data you read, not programs: jmdict-simplified releases are JSON files in .zip/.tgz with a SHA-256 digest per asset on the GitHub release; kanjium is text files, a SQLite database (data/kanjidb.sqlite: tables and indexes only, no triggers or views), fonts and 27k PNG images. The optional npm loader @scriptin/jmdict-simplified-loader (3.6.1) only reads a local file with fs.createReadStream and parses it with stream-json (node/packages/jmdict-simplified-loader/src/index.ts:1-2) and has no install scripts. Verified behaviour and fixes: (1) kanjium ships two Ruby helper scripts, and mecab-furigana.rb:8 starts C:/Program Files/MeCab/bin/mecab.exe through IO.popen; fix: don't run data/source_files/raw/*.rb, use the data files only. (2) kanjium's word_segmentation.txt points to a separate third-party GPL script (github.com/hssm/ryuujouji) that is not part of the package; fix: don't fetch or run it. (3) Licences: JMdict, JMnedict and RADKFILE/KRADFILE data are under the EDRDG licence and Kanjidic and the rest of jmdict-simplified under CC BY-SA 4.0 (jmdict-simplified README.md:139-173); kanjium is CC BY-SA 4.0 with EDRDG-derived data (kanjium README.md:15-33); fix: credit EDRDG, jmdict-simplified and kanjium and share any cards built from them under the same licence.

## Safe install

Safe install (fixes applied): any platform (Claude Code on Windows, Hermes): download jmdict-eng-common-3.6.2+20261116213322.json.zip (or jmdict-eng-3.6.2+20261116213322.json.zip for the full set) from https://github.com/scriptin/jmdict-simplified/releases and check its SHA-256 before use (PowerShell: Get-FileHash <file> -Algorithm SHA256): eng-common zip 02dd1b410cbe56dd34c931f08ae3cd7079cb12508a208da0432e959266ea5d1a, eng zip c3c43879681c7e26b7a9113034fa3a94299234a47b3b7e3b3361447576c4932c (GitHub release digests, checked 2026-11-19). kanjium has no releases: take it pinned at commit 9ebca4589565c696e7c39e089e2e928ad65f678c (git clone https://github.com/mifunetoshiro/kanjium then git checkout 9ebca4589565c696e7c39e089e2e928ad65f678c; about 263 MB) and use only data/source_files/raw/accents.txt for pitch accent and data/kanjidb.sqlite opened read-only. Don't run the Ruby scripts in data/source_files/raw or fetch the linked ryuujouji script. Optional JSON loader: npm install @scriptin/jmdict-simplified-loader@3.6.1 --ignore-scripts (no install scripts; pinned). No keys; no network after download. Credit EDRDG, jmdict-simplified and kanjium (CC BY-SA 4.0 / EDRDG licence). claude.ai: upload the unzipped JSON or accents.txt as a file. Android: nothing to install; the glosses and pitch marks go into the cards.

## YOLO install

YOLO (your own risk): skips the hash check and commit pin: download the latest jmdict-eng release zip and git clone https://github.com/mifunetoshiro/kanjium (latest), npm install @scriptin/jmdict-simplified-loader.

## Install notes

Ask the user before adding it. Safe with the fixes in Safe install applied. Offline English glosses (jmdict-simplified, released weekly on Mondays) and pitch accent (kanjium accents.txt, 124,137 words) for a project cards.
Official docs: https://github.com/scriptin/jmdict-simplified and https://github.com/mifunetoshiro/kanjium (GitHub release downloads were blocked in a project sandbox).
