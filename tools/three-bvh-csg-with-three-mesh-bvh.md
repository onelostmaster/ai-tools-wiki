# three-bvh-csg (with three-mesh-bvh)

- **Type:** library
- **Category:** 3D and games, frontend
- **Official URL:** https://github.com/gkjohnson/three-bvh-csg
- **GitHub repo:** https://github.com/gkjohnson/three-bvh-csg @ 0ac3a84 (v0.0.18) + https://github.com/gkjohnson/three-mesh-bvh @ 1d92383 (v0.9.18)
- **Price:** Free, MIT (github.com/gkjohnson/three-bvh-csg and three-mesh-bvh, checked 2026-11-08)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot npm tarball read 2026-11-08 (0.0.18 + 0.9.18): no install/postinstall scripts, no runtime dependencies (peer three only), no fetch, eval, child_process or fs in shipped code. a project tarball scan agrees. MIT, official non-fork repos, active.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code / Windows: npm install three-bvh-csg@0.0.18 three-mesh-bvh@0.9.18 (pin exact, as a project does in its project package.json). Browser-side library; needs three >= 0.179.
