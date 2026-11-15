# img2threejs

- **Type:** skill
- **Category:** 3D and games, design
- **Official URL:** https://img2threejs.io
- **GitHub repo:** https://github.com/img2threejs/img2threejs @ 3e7099e (Apache-2.0; latest commit on 2026-10-27)
- **Price:** Free (Apache-2.0, `github.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a project Claude code read @0c0c49b, re-checked by the wiki 2026-11-14: safe with fixes. Core is stdlib with no network. The npx installer is unpinned: install from the reviewed commit. The img2glb plugin uploads images to a hosted TRELLIS space (README:157) and integrations/vision downloads models from storage.googleapis.com (integrations/vision/reference_vision.py): leave both out.

## Safe install

Safe install (fixes applied):
npx --yes github:img2threejs/img2threejs#0c0c49b install, then the same with doctor. Never run img2 add img2glb; don't run integrations/vision. Hermes: same installer, then the README's ln -sfn line.

## YOLO install

YOLO (your own risk): skips the pin and adds the hosted add-ons.
npx --yes img2threejs@latest install then img2 add img2glb --yes.

## Install notes

Ask the user before installing.
Claude Code: `npx --yes img2threejs@latest install`, check with `npx --yes img2threejs@latest doctor` (README).
Hermes: same installer (writes `~/.hermes/skills/`), then link it into your profile with the `ln -sfn` line in the README (README).
Pin 0c0c49b. Skip the unpinned npx installer; keep the mesh3d add-on (uploads images to a hosted space) and the vision add-on (downloads models) off.
