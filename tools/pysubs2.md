# pysubs2

- **Type:** API
- **Category:** editing, generating videos
- **Official URL:** https://pysubs2.readthedocs.io
- **GitHub repo:** https://github.com/tkarabela/pysubs2 @ 6371ae8 (pysubs2 1.9.1, MIT LICENSE.txt; committed 2026-10-29 20:22 ET, HEAD on 2026-11-10)
- **Price:** Free (MIT)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (code read @6371ae8 = 1.9.1, 2026-11-10, no-intake review): Safe. Pure-Python library, about 4,100 lines under pysubs2/, with no runtime dependencies (pyproject.toml has no dependencies list, only dev and docs groups). No subprocess, os.system, eval/exec, pickle or network code anywhere in the package; imports are standard modules only (e.g. cli.py lines 1-8, ssafile.py lines 3-7). File access is only the paths you pass: SSAFile.load opens the given file to read (ssafile.py line 751) and save writes the given path (line 891). The CLI (cli.py, 225 lines) reads each file you name (line 167) and writes the result back to the same file unless you give an output format or -o folder (lines 172-186), so it can overwrite your input. TTML input is parsed with the standard xml.etree parser (formats/ttml.py line 103); only open TTML files you trust. CI workflows pin actions by commit and publish to PyPI with trusted publishing. Not reviewed: tests/ and docs/.

## Safe install

Safe install (fixes applied):
Windows (Python 3.12 or newer) or Claude Code: in a venv, `pip install pysubs2==1.9.1` (the reviewed release, still the PyPI latest on 2026-11-15; no dependencies, nothing else installs). Command-line tool: always pass `-o <folder>` (or --to), because without it the CLI writes the result back over your input file (cli.py lines 172-186). Open only TTML files you made or trust (plain xml.etree parser, formats/ttml.py line 103). claude.ai, Hermes and Android: Python library, no install route.

## YOLO install

YOLO (your own risk): skips the venv, the version pin and the -o output folder.
pip install pysubs2

## Install notes

Code-reviewed by a review bot @6371ae8 = pysubs2 1.9.1 (safe). Windows (Python 3.12 or newer): pip install pysubs2==1.9.1 (pinned to the reviewed release; no other packages are pulled in). Claude Code on Windows can then use it from Python scripts (import pysubs2) to load, retime, restyle and save SRT/ASS/VTT captions. Careful with the pysubs2 command-line tool: run without --to or -o it rewrites the input subtitle file in place, so work on a copy or pass -o <folder>.
