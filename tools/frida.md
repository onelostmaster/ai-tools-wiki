# Frida

- **Type:** CLI
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://frida.re
- **GitHub repo:** https://github.com/frida/frida @ 29016db (wxWindows Library Licence 3.1, `COPYING`)
- **Price:** Free, wxWindows Library Licence 3.1 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (light code read @29016db, a review, 2026-11-02): safe (meta repo only; the engine lives in the frida-gum and frida-core submodules, not read). It injects code into processes by design: use it only on your own apps and games.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: `pip install frida-tools` per frida.re docs (not tested). Android: frida-server on a rooted or test device only.
