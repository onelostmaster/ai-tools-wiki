# three.js (three@0.186.1)

- **Type:** library
- **Category:** 3D and games, generating videos
- **Official URL:** https://threejs.org
- **GitHub repo:** https://github.com/mrdoob/three.js @ 9b4a2ac (tag r186, "r186 (bis)", 2026-09-24, MIT; repo and commit confirmed by the npm registry entry for three 0.186.1)
- **Price:** Free (MIT, per npm, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read of src/ @9b4a2ac, tag r186, published as three 0.186. No telemetry, eval, new Function, child_process or WebSocket in src/. Network use happens only when the app asks for it: FileLoader fetches the URL it is given (loaders/FileLoader.js:141) and ImageBitmapLoader likewise (loaders/ImageBitmapLoader.js:173); credentials are sent only if the app turns withCredentials on (loaders/Loader.js:35). The only globals touched are window.__THREE__ for a duplicate-copy warning (Three.Core.js:178-184) and an optional browser devtools hook that does nothing unless that extension is present (renderers/WebGLRenderer.js:3635). The npm package has no dependencies and no install scripts (package.json; scripts are build, lint and test only). MIT licence.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: in the project folder `npm install -E three@0.186.1` (the reviewed r186 build a project pins); load models and textures only from project files, since FileLoader fetches any URL it is given (loaders/FileLoader.js:141). Android: runs in the browser, nothing to install.

## YOLO install

YOLO (your own risk): skips the exact reviewed pin.
`npm install three`

## Install notes

Claude Code: `npm install three` (npm package `three`); a project pins `three@0.186.1` in its Remotion install (see the Remotion row). Official docs: https://threejs.org/docs/
Loading: FileLoader and ImageBitmapLoader fetch whatever URL you pass them, so load models and textures from your own project files or trusted hosts. Note: npm 'latest' is now 0.187.0; a project stays pinned at 0.186.1 (the reviewed version).
