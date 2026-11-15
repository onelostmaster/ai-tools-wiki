# React Three Fiber (R3F)

- **Type:** library
- **Category:** generating videos, 3D and games
- **Official URL:** https://r3f.docs.pmnd.rs
- **GitHub repo:** https://github.com/pmndrs/react-three-fiber @ d74622e (tag v9.8.2, 2026-10-14, MIT; packages/fiber; repo confirmed by the npm registry entry for @react-three/fiber 9.8.2)
- **Price:** Free (MIT, per npm, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read of packages/fiber/src @d74622e, tag v9.8. No telemetry, eval, new Function, child_process or WebSocket in the library source; the URLs in it are only doc links in comments and warnings. Network use happens only when the app asks for it: useLoader hands the given URL to the three.js loader (core/hooks.tsx:118, 139), and the React Native build reads blob: URLs with XMLHttpRequest into the Expo cache (native/polyfills.ts:35, not used by a project's web/Remotion setup). The published package has no install scripts (only a prebuild that copies the readme, packages/fiber/package.json); the postinstall at the repo root (package.json:27) is for developing R3F itself. Runtime deps are small, well-known libraries (zustand, its-fine, suspend-react, scheduler, react-use-measure and similar). Note: package.json at the tag still says 9.8.1; the version is bumped at publish.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: in the project folder `npm install -E @react-three/fiber@9.8.2 three@0.186.1` (the reviewed v9.8.2, d74622e; pairs with React 19). useLoader fetches any URL it is given (core/hooks.tsx:118, 139), so load models and textures only from project files. Android: runs in the browser, nothing to install.

## YOLO install

YOLO (your own risk): skips the exact reviewed pins.
`npm install three @react-three/fiber`

## Install notes

Claude Code: `npm install three @react-three/fiber` (official R3F docs); version 9 pairs with React 19. a project pins `@react-three/fiber@9.8.2` with `three@0.186.1` (see the Remotion row).
Loading: useLoader fetches whatever URL you pass through the three.js loader, so load models and textures from your own project files or trusted hosts. The repo's own postinstall (root package.json) is for working on R3F itself and is not in the published npm package.
