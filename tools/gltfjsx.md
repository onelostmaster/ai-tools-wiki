# gltfjsx

- **Type:** CLI
- **Category:** generating videos, 3D and games
- **Official URL:** https://github.com/pmndrs/gltfjsx
- **GitHub repo:** https://github.com/pmndrs/gltfjsx @ f4fbfa2 (master, 2024-11-04, package.json 6.5.2, MIT). npm latest is 6.5.3, published the same day; its gitHead c7d88c9 is not on GitHub, so 6.5.3 itself was not read.
- **Price:** Free (MIT)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (code read of cli.js and src/ @f4fbfa2, 2026-11-02, hourly run with no new intake): Looks safe. It is a local command-line converter: it reads the model file you pass, writes one .jsx or .tsx file (and a -transformed.glb with --transform), and prints to the console. No telemetry, eval, new Function, child_process or shell calls in cli.js or src/. Network use only happens if a .gltf file references external buffers or textures by URL (bundled GLTFLoader uses three's FileLoader, src/bin/GLTFLoader.js:1504). No install scripts in the package itself (scripts are build and test only); the optional sharp dependency downloads a prebuilt libvips at install. Dependencies are mainstream (gltf-transform, three 0.159.0, prettier, meshoptimizer, draco3dgltf). MIT licence.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `npx gltfjsx model.glb` (usage from the npm README; `model.glb` is your GLTF/GLB model file). Official docs: https://www.npmjs.com/package/gltfjsx
Note: run it only on model files you trust, since a .gltf file can point to extra buffer or texture URLs that get fetched. The --transform option pulls in sharp, whose install downloads a prebuilt image library.
Tip (2026-11-08, from a project): 6.5.2 in its own folder; sharp needs its own install script for prebuilt libvips; output imports drei useGLTF.
