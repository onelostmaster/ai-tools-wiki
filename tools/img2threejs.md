# img2threejs

- **Type:** skill
- **Category:** 3D and games, design
- **Official URL:** https://img2threejs.io
- **GitHub repo:** https://github.com/img2threejs/img2threejs @ 3e7099e (Apache-2.0; latest commit on 2026-10-27)
- **Price:** Free (Apache-2.0, `github.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a project Claude code read @ 0c0c49b (2026-11-08): core is stdlib, no network; caution for the unpinned npx installer, the mesh3d add-on that uploads images to a hosted space and the vision add-on that downloads models (both kept off). Not re-read by a review bot.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: `npx --yes img2threejs@latest install`, check with `npx --yes img2threejs@latest doctor` (README).
Hermes: same installer (writes `~/.hermes/skills/`), then link it into your profile with the `ln -sfn` line in the README (README).
Pin 0c0c49b. Skip the unpinned npx installer; keep the mesh3d add-on (uploads images to a hosted space) and the vision add-on (downloads models) off.
