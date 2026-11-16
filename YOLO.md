# YOLO installs

The tool's own defaults: no fixes, no sandbox, at your own risk. Never offered for avoid or unreviewed tools.

- [Ace Data Cloud plugin](tools/ace-data-cloud-plugin.md): YOLO (your own risk): skips the key limits and toolset choice, so the model spends credits freely.
Install from the catalog with your general key and all 17 toolsets.
- [AG-UI protocol](tools/ag-ui-protocol.md): YOLO (your own risk): skips the version pins and runs the unpinned CopilotKit CLI.
npx create-ag-ui-app my-agent-app
- [AG2](tools/ag2.md): YOLO (your own risk): skips the version pin (gets 1.3.2 from 2026-11-15, unreviewed) and the venv.
pip install ag2[openai]
- [Agent Reach](tools/agent-reach.md): YOLO (your own risk): skips the pin and the channel limit, so it pulls the latest OpenCLI extension unverified.
Install from releases/latest as docs/install.md says and add every channel.
- [agent-browser](tools/agent-browser.md): YOLO (your own risk): skips the pin, --ignore-scripts, AGENT_BROWSER_NO_VERSION_CHECK=1, the domain/action/output limits, and the ban on attach modes and plugins.
`npm install -g agent-browser`, then `agent-browser install` (README / agent-browser.dev/installation).
- [AgenticSeek](tools/agenticseek.md): YOLO (your own risk): skips Docker, so model-written shell runs as you.
python3 cli.py on the host with WORK_DIR set to your files.
- [aliang-knowledge-video (aliangSSS)](tools/aliang-knowledge-video-aliangsss.md): YOLO (your own risk): skips the commit pin, the per-project venv and the lockfile step.
git clone https://github.com/aliangSSS/aliang-knowledge-video && python scripts/new_project.py <dir>
- [Anime.js](tools/anime-js.md): YOLO (your own risk): skips the version pin.
npm install animejs
- [Apify (API + MCP)](tools/apify-api-mcp.md): YOLO (your own risk): skips telemetry off, the tool allowlist and price checks.
npx @apify/actors-mcp-server with defaults.
- [Astryx](tools/astryx.md): YOLO (your own risk): skips the pinned version, --ignore-scripts, NO_UPDATE_NOTIFIER=1, the deny rule against global npm, and staying off the hosted MCP and `astryx init --user`.
`npm i -g @astryxdesign/cli` (README), or install the Astryx skill, which tells an agent to run that command when `astryx` is not found (SKILL.md:19).
- [Atheros AI Builder](tools/atheros-ai-builder.md): YOLO (your own risk): skips the project-key-only, Pass-only and read-tool allowlist rules.
claude mcp add atheros --transport http https://mcp.atheros.ai/v1 --header "Authorization: Bearer YOUR_API_KEY"
- [Auto-Editor](tools/auto-editor.md): YOLO (your own risk): skips the firewall block and the review gap; gets the newest release and its skills.
Latest auto-editor-windows-x86_64.exe from the releases page, then npx skills add WyattBlue/auto-editor
- [awesome-llm-apps (Shubhamsaboo)](tools/awesome-llm-apps-shubhamsaboo.md): YOLO (your own risk): skips the commit pin, --ignore-scripts and the settings removal.
git clone https://github.com/Shubhamsaboo/awesome-llm-apps
- [Basic Memory](tools/basic-memory.md): YOLO (your own risk): skips the pin and both switches, so it sends analytics and upgrades itself to prereleases.
uvx basic-memory mcp with defaults.
- [BepInEx](tools/bepinex.md): YOLO (your own risk): skips the game-folder backup and uses the 6.x bleeding-edge build (6.0.0-pre.2 or nightly), unreviewed.
Unzip the 6.x build for your game type into the game folder.
- [Blockbench (JannisX11)](tools/blockbench-jannisx11.md): YOLO (your own risk): skips the plugin restriction.
Installer from blockbench.net, any plugins.
- [Cache Tax](tools/cache-tax.md): YOLO (your own risk): skips the pin and Auto keepwarm off, so pings spend usage after every cold write.
Install from the marketplace with defaults.
- [Camera Controls (three.js)](tools/camera-controls-three-js.md): YOLO (your own risk): skips the version pin.
npm install camera-controls
- [canvas-sketch](tools/canvas-sketch.md): YOLO (your own risk): skips the version pin and project-folder containment.
npm install -g canvas-sketch-cli
- [caveman](tools/caveman.md): YOLO (your own risk): skips the pin, telemetry off and the setup ban.
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/v4.1.0/install.sh | bash and run /caveman-setup.
- [chorono-editor (codie1982)](tools/chorono-editor-codie1982.md): YOLO (your own risk): skips the commit pin and the 127.0.0.1 start command.
git clone https://github.com/codie1982/chorono-editor.git
npm install
npm run dev
- [Claude in Chrome](tools/claude-in-chrome.md): YOLO (your own risk): skips per-action approval.
'Automatically approve' mode in your main Chrome profile.
- [Claude Quickstarts](tools/claude-quickstarts.md): YOLO (your own risk): skips the commit pin, Docker isolation, the no-extra-mounts rule, and skipping Managed Agents and macOS-native samples.
Clone https://github.com/anthropics/claude-quickstarts and follow each sample's README, including the `docker run` that mounts `$HOME/.anthropic` (computer-use-demo/README.md:51-58).
- [claude-3d-animated-shorts (thuann-vn)](tools/claude-3d-animated-shorts-thuann-vn.md): YOLO (your own risk): skips the commit pin.
git clone https://github.com/thuann-vn/claude-3d-animated-shorts %USERPROFILE%\.claude\\skills\\claude-3d-animated-shorts, then scripts/fetch-assets.sh and npm install in engine/
- [claude-code-video-toolkit](tools/claude-code-video-toolkit.md): YOLO (your own risk): skips R2 and the patch, so your voice, photo and video inputs go to public hosts.
Clone and run as the README says.
- [claude-content-skills (Ootto)](tools/claude-content-skills-ootto.md): YOLO (your own risk): skips the skill filter, so the agent follows a live remote installer and wires 24/7 auto-replies.
bash install.sh from the repo.
- [claude-eyes (moritzkremb)](tools/claude-eyes-moritzkremb.md): YOLO (your own risk): skips the commit pin and the SKILL.md section 0 edit, so the agent installs and updates it without asking.
uv tool install git+https://github.com/moritzkremb/claude-eyes && eyes setup --fix && eyes install-skill
- [claude-figma-stack (Ootto)](tools/claude-figma-stack-ootto.md): YOLO (your own risk): skips the private repo, seed and empty default, so it auto-DMs everyone and publishes commenter IDs.
Fork publicly and enable the Action as the README says.
- [claude-instagram-autopilot (Ootto)](tools/claude-instagram-autopilot-ootto.md): YOLO (your own risk): skips the pin, tool limit and narrow commit, so a skip-permissions agent runs with your keys in CI.
Fork and add the secrets as the README says.
- [claude-reflect](tools/claude-reflect.md): YOLO (your own risk): skips the pin and the review, so every queued learning is applied.
Install from the marketplace and use Apply all.
- [claudeweaver (statico)](tools/claudeweaver-statico.md): YOLO (your own risk): skips the commit pin.
npx skills add statico/claudeweaver (README.md:20)
- [Cloudflare Pages](tools/cloudflare-pages.md): YOLO (your own risk): skips single-repo GitHub access, the pinned project-local Wrangler, telemetry off and the No to the skills prompt.
Connect GitHub with "All repositories"; `npm i -g wrangler` and accept its prompts.
- [Context Mode (local Engine plugin)](tools/context-mode-local-engine-plugin.md): YOLO (your own risk): skips the test repo, the per-call approval on ctx_execute/ctx_batch and the clean environment.
claude plugin marketplace add mksglu/context-mode && claude plugin install context-mode@context-mode
- [Craft Anything (ArtCraft workbench)](tools/craft-anything-artcraft-workbench.md): YOLO (your own risk): skips Auto mode off, the approval changes and the signature check; uses the default build and setup.
craft-anything-cli setup
- [creator-generalist (codepawl)](tools/creator-generalist-codepawl.md): YOLO (your own risk): skips the commit pin, the local marketplace and the per-tool no answers.
/plugin marketplace add codepawl/creator-generalist
/plugin install <name>@creator-generalist (each of the five plugins)
- [DeepFilterNet](tools/deepfilternet.md): YOLO (your own risk): skips the venv and version pin.
pip install torch torchaudio deepfilternet
- [Demucs (htdemucs)](tools/demucs-htdemucs.md): YOLO (your own risk): skips the virtual environment and the exact pin (the built-in-models-only rule still applies).
`pip install demucs`
- [E2B](tools/e2b.md): YOLO (your own risk): skips the version pin (gets 2.64.0 from 2026-11-13, unreviewed) and the venv.
pip install e2b
- [earshot](tools/earshot.md): YOLO (your own risk): skips the commit pin, the CPU-only torch index and offline mode.
`git clone https://github.com/Leonxlnx/earshot` then `pip install -e ".[mcp]"` and `claude mcp add earshot -- python -m earshot mcp` (still never set GEMINI_API_KEY).
- [Element 84 Earth Search (STAC API)](tools/element-84-earth-search-stac-api.md): YOLO (your own risk): skips the venv and the version pin.
pip install pystac-client
- [ElevenLabs agent skills](tools/elevenlabs-agent-skills.md): YOLO (your own risk): skips the key and pin, so the skill runs the latest CLI sign-in.
Install with npx skills add elevenlabs/skills and let it onboard.
- [ElevenLabs connector (Claude directory)](tools/elevenlabs-connector-claude-directory.md): YOLO (your own risk): skips the ask-before-video rule and scope limits.
Connect with every permission and generate freely.
- [Emscripten (emsdk)](tools/emscripten-emsdk.md): YOLO (your own risk): skips the digest-pinned container.
Local `./emsdk install latest` then `./emsdk activate latest` (emscripten.org).
- [Energy Icons (SVG library and MCP)](tools/energy-icons-svg-library-and-mcp.md): YOLO (your own risk): skips the version pin and uses the hosted MCP.
npm install energy-icons
claude mcp add --transport http energy-icons https://energyicons.com/mcp
- [Eva Icons (Akveo)](tools/eva-icons-akveo.md): YOLO (your own risk): skips the version pin and the static-files-only rule.
npm i eva-icons
- [F5-TTS (SWivid)](tools/f5-tts-swivid.md): YOLO (your own risk): skips the venv, version pin and the 127.0.0.1 bind.
pip install f5-tts
- [faster-whisper](tools/faster-whisper.md): YOLO (your own risk): skips the virtual environment, the exact pin and offline mode.
`pip install faster-whisper`
- [feathericon (not Feather Icons)](tools/feathericon-not-feather-icons.md): YOLO (your own risk): skips the version pin and --ignore-scripts.
npm install feathericon --save
- [figma-shaders (official Figma skill)](tools/figma-shaders-official-figma-skill.md): YOLO (your own risk): skips the pinned hand copy and per-write approval.
claude plugin install figma@claude-plugins-official
- [Filetree (claude-code-filetree)](tools/filetree-claude-code-filetree.md): YOLO (your own risk): skips the pin, so updates arrive unread.
Install from the marketplace as the README says.
- [find-skills (vercel-labs/skills)](tools/find-skills-vercel-labs-skills.md): YOLO (your own risk): skips the deny and telemetry off.
npx skills add vercel-labs/skills@find-skills -g -y.
- [genjutsu (AThevon)](tools/genjutsu-athevon.md): YOLO (your own risk): skips the commit pin (gets v4.2.0, unreviewed) and the global install from the website.
npx skills add https://genjutsu.athevon.dev -g
- [GitHub Actions (official actions/*)](tools/github-actions-official-actions.md): YOLO (your own risk): skips the SHA pins and the read-only token.
`uses: actions/checkout@v7` with the repo's default token permissions.
- [GitHub Pages](tools/github-pages.md): YOLO (your own risk): skips the SHA pins and the minimal permissions.
Turn on Pages from a branch in the repo settings, or use the starter workflow with tag versions (actions/deploy-pages@v4).
- [gltfjsx](tools/gltfjsx.md): YOLO (your own risk): skips the folder install and the exact reviewed version.
`npx gltfjsx model.glb` (runs npm latest 6.5.3).
- [Google ADK (adk-python)](tools/google-adk-adk-python.md): YOLO (your own risk): skips the version pin (gets 2.14.1 from 2026-11-12, unreviewed) and the venv.
pip install google-adk
- [Google Fonts](tools/google-fonts.md): YOLO (your own risk): skips self-hosting, so every page load sends the viewer's IP and the page URL to Google.
A stylesheet link tag to fonts.googleapis.com in the page head.
- [GPT Image](tools/gpt-image.md): YOLO (your own risk): skips the separate project and budget, so spend has no cap.
Use your main API key.
- [gpu-io](tools/gpu-io.md): YOLO (your own risk): skips the version pin.
npm install gpu-io
- [Graphiti MCP (Zep)](tools/graphiti-mcp-zep.md): YOLO (your own risk): skips telemetry off and the image pin.
docker compose up with the defaults.
- [Gravity UI Icons](tools/gravity-ui-icons.md): YOLO (your own risk): skips the version pin and --ignore-scripts.
npm install --save-dev @gravity-ui/icons
- [GSAP](tools/gsap.md): YOLO (your own risk): skips the version pin and self-hosting.
npm install gsap
- [herdr](tools/herdr.md): YOLO (your own risk): skips the SHA-256 check, the ban on piped installers, and turning off background version and manifest checks.
Windows: `powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"` (README.md:45).
- [herk-edit-kit (nateherkai)](tools/herk-edit-kit-nateherkai.md): YOLO (your own risk): skips the commit pin and the ClickUp-demo/paid-API cautions.
git clone https://github.com/nateherkai/herk-edit-kit && cd herk-edit-kit && npm install && npm run setup
- [Hermes Agent (Nous Research)](tools/hermes-agent-nous-research.md): YOLO (your own risk): skips the container, approvals and script read.
iex (irm https://hermes-agent.nousresearch.com/install.ps1) on the local backend.
- [Hermes Wear OS app](tools/hermes-wear-os-app.md): YOLO (your own risk): skips the tailnet-only bind.
Set watchkit host to 0.0.0.0 on your home LAN.
- [Hindsight (Hermes memory provider)](tools/hindsight-hermes-memory-provider.md): YOLO (your own risk): skips local mode and the template skip, so every retained turn goes to Hindsight Cloud.
Accept the setup defaults.
- [img2threejs](tools/img2threejs.md): YOLO (your own risk): skips the pin and adds the hosted add-ons.
npx --yes img2threejs@latest install then img2 add img2glb --yes.
- [Instagram Agent skill](tools/instagram-agent-skill.md): YOLO (your own risk): skips the commit pin and installs for your user in every project.
/plugin marketplace add Jakeschincariol/instagram-agent-skill
/plugin install instagram-agent
- [LangChain](tools/langchain.md): YOLO (your own risk): skips the version pin (gets 1.5.0 from 2026-11-11, unreviewed) and the venv.
uv add langchain
- [LangGraph](tools/langgraph.md): YOLO (your own risk): skips the version pin (gets 1.2.22 from 2026-11-14, unreviewed), the venv and the CLI analytics opt-out.
pip install -U langgraph
- [last30days skill](tools/last30days-skill.md): YOLO (your own risk): skips the pin and the cookie switches, so it reads your browser's X cookies.
Install the latest skill as its README says and run setup with --allow-browser-cookies.
- [librosa](tools/librosa.md): YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install librosa`
- [Lots of Sounds (lotsofsounds)](tools/lots-of-sounds-lotsofsounds.md): YOLO (your own risk): skips the pin.
/plugin marketplace add lotsofsounds/agent-skills and /plugin install lotsofsounds@lotsofsounds.
- [Manim Community (animation engine)](tools/manim-community-animation-engine.md): YOLO (your own risk): skips the version pin, the update-check opt-out and reading scenes first.
pip install manim
- [Mastra](tools/mastra.md): YOLO (your own risk): skips the version pins (gets 1.39.0 / core 1.83.0 from 2026-11-12, unreviewed); telemetry stays off only if you still set MASTRA_TELEMETRY_DISABLED=1.
npm create mastra@latest
- [MCP reference servers (filesystem, fetch, git, memory, sequential thinking, time, everything)](tools/mcp-reference-servers-filesystem-fetch-git-memory-sequential.md): YOLO (your own risk): skips the version pins (gets v2.4.0 from 2026-11-11, unreviewed), the folder and --repository limits.
claude mcp add memory -- cmd /c npx -y @modelcontextprotocol/server-memory (and the same unpinned for the others)
- [MeshLine (pmndrs)](tools/meshline-pmndrs.md): YOLO (your own risk): skips the version pin.
npm install meshline
- [Microsoft Planetary Computer (STAC API + tiler)](tools/microsoft-planetary-computer-stac-api-tiler.md): YOLO (your own risk): skips the venv and the version pins.
pip install pystac-client planetary-computer
- [MoviePy](tools/moviepy.md): YOLO (your own risk): skips the commit pin (gets PyPI 2.2.1, older than the review) and the venv.
pip install moviepy
- [Neat Icons (SVG library and paid MCP)](tools/neat-icons-svg-library-and-paid-mcp.md): YOLO (your own risk): skips the free-files-only rule and connects the paid hosted MCP.
claude mcp add --transport http neat-icons https://mcp.neaticons.com/mcp --header "Authorization: Bearer YOUR_SEAT_KEY"
- [NumPy](tools/numpy.md): YOLO (your own risk): skips the venv and the version pin.
pip install numpy
- [oh-my-hermes](tools/oh-my-hermes.md): YOLO (your own risk): skips the pin, script read and test profile.
curl -fsSL https://omher.app/install | sh with the auto update mode.
- [OpenAI Agents SDK](tools/openai-agents-sdk.md): YOLO (your own risk): skips the venv and the tracing opt-out (traces go to your OpenAI account).
pip install openai-agents
- [OpenIDEA (l0ng-ai)](tools/openidea-l0ng-ai.md): YOLO (your own risk): skips the checksum and the re-review.
OpenIDEA_0.1.45_x64-setup.exe from the GitHub release.
- [OpenSandbox](tools/opensandbox.md): YOLO (your own risk): skips the version pins, the 127.0.0.1 binding, the deny network policy and the metrics opt-out.
uvx opensandbox-server init-config ~/.sandbox.toml --example docker
uvx opensandbox-server
uv pip install opensandbox
- [Orca (Stably AI)](tools/orca-stably-ai.md): YOLO (your own risk): skips telemetry opt-out, the permission changes and the hook review; runs with the full-access defaults.
https://github.com/stablyai/orca/releases/latest/download/orca-windows-setup.exe
- [Piper (OHF-Voice)](tools/piper-ohf-voice.md): YOLO (your own risk): skips the venv, version pin and 127.0.0.1 binding.
pip install piper-tts && python -m piper.http_server -m en_US-lessac-medium
- [Pixelorama (Orama-Interactive)](tools/pixelorama-orama-interactive.md): YOLO (your own risk): skips the extension restriction.
winget install pixelorama
- [Playwright + Chromium](tools/playwright-chromium.md): YOLO (your own risk): skips the venv and version pin, and downloads every browser.
pip install playwright
playwright install
- [print3d](tools/print3d.md): YOLO (your own risk): skips the container.
Add the print3d MCP to Hermes on your PC's local backend.
- [pykakasi](tools/pykakasi.md): YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install pykakasi`
- [pyloudnorm](tools/pyloudnorm.md): YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install pyloudnorm`
- [PySceneDetect](tools/pyscenedetect.md): YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install --upgrade scenedetect`
- [pysubs2](tools/pysubs2.md): YOLO (your own risk): skips the venv, the version pin and the -o output folder.
pip install pysubs2
- [RapidOCR](tools/rapidocr.md): YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install rapidocr onnxruntime`
- [React Three Fiber (R3F)](tools/react-three-fiber-r3f.md): YOLO (your own risk): skips the exact reviewed pins.
`npm install three @react-three/fiber`
- [rembg](tools/rembg.md): YOLO (your own risk): skips the venv, the version pin and the 127.0.0.1 server bind.
pip install "rembg[cpu,cli]"
rembg s
- [Remotion (framework, v4)](tools/remotion-framework-v4.md): YOLO (your own risk): skips the exact pins.
`npx create-video@latest`
- [Remotion agent skills (official)](tools/remotion-agent-skills-official.md): YOLO (your own risk): skips the installer version pin and the telemetry switch.
npx skills add remotion-dev/skills
- [roadmap-skill (shiquda)](tools/roadmap-skill-shiquda.md): YOLO (your own risk): skips the version pin.
claude mcp add roadmap "npx -y roadmap-skill"
- [Rune Icons (SVG library and local MCP)](tools/rune-icons-svg-library-and-local-mcp.md): YOLO (your own risk): skips the version pin and the local node path.
claude mcp add runeicons -- npx -y runeicons-mcp
- [RustDesk](tools/rustdesk.md): YOLO (your own risk): skips 2FA and the Tailscale whitelist.
Default install with the public ID server and one-time passwords.
- [satellite.js](tools/satellite-js.md): YOLO (your own risk): skips the exact pin.
npm install satellite.js
- [Scrolltide (templates, prompts + MCP)](tools/scrolltide-templates-prompts-mcp.md): YOLO (your own risk): skips reading prompts first and connects the MCP on day one.
claude mcp add --transport http scrolltide https://www.scrolltide.co/api/mcp
- [sgp4 (python-sgp4)](tools/sgp4-python-sgp4.md): YOLO (your own risk): skips the venv and the version pin.
pip install sgp4
- [shadcn/ui (+ shadcn MCP server)](tools/shadcn-ui-shadcn-mcp-server.md): YOLO (your own risk): skips the version pin.
npx shadcn@latest init, and npx shadcn@latest mcp for Claude Code
- [shazamio](tools/shazamio.md): YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install shazamio`
- [Superpowers](tools/superpowers.md): YOLO (your own risk): skips the telemetry opt-out (the brainstorm page fetches its logo from primeradiant.com).
/plugin install superpowers@claude-plugins-official
- [SVG.js](tools/svg-js.md): YOLO (your own risk): skips the version pin and local bundling.
<script src="https://cdn.jsdelivr.net/npm/@svgdotjs/svg.js"></script>
- [taste-skill](tools/taste-skill.md): YOLO (your own risk): skips the commit pin, the ban on install.sh, and deleting the Stop hook, so gate.mjs can run on every Claude Code stop.
Run the repo's `install.sh` from HEAD, leaving the hooks block in SKILL.md.
- [teardown skill](tools/teardown-skill.md): YOLO (your own risk): skips the commit pin and the lockfile install, and installs globally.
npx skills add elvarofficial/teardown -g -a claude-code, then npm install && npx playwright install chromium in the folder (package.json setup script).
- [Terminal Browser](tools/terminal-browser.md): YOLO (your own risk): skips telemetry off and the script read.
curl -fsSL https://terminal-browser.sh/install | bash.
- [Terrain3D (TokisanGames)](tools/terrain3d-tokisangames.md): YOLO (your own risk): skips the project backup.
Install Terrain3D from the Godot Asset Library into your main project.
- [three-bvh-csg (with three-mesh-bvh)](tools/three-bvh-csg-with-three-mesh-bvh.md): YOLO (your own risk): skips the exact pins on the reviewed versions.
`npm install three-bvh-csg three-mesh-bvh`
- [three.js (three@0.186.1)](tools/three-js-three-0-186-1.md): YOLO (your own risk): skips the exact reviewed pin.
`npm install three`
- [Threejs-Awesome-Graphics-Agent-Skills (scottstts)](tools/threejs-awesome-graphics-agent-skills-scottstts.md): YOLO (your own risk): skips the pinned commit and the hand-picked folders.
`npx threejs-awesome-graphics-agent-skills install`
- [tiktok-video-skills](tools/tiktok-video-skills.md): YOLO (your own risk): skips the commit pin and the pinned Playwright.
/plugin marketplace add iart-ai/tiktok-video-skills
/plugin install tiktok-video-skills (README), and use scripts/seek-shot.sh as shipped.
- [TinyFish (MCP + Claude Code plugin + connector)](tools/tinyfish-mcp-claude-code-plugin-connector.md): YOLO (your own risk): skips the wallet deny and the doctor block.
Install the plugin as its README says and allow every tool.
- [Transformers.js (@huggingface/transformers)](tools/transformers-js-huggingface-transformers.md): YOLO (your own risk): skips the exact pin and the pinned model revisions.
`npm install @huggingface/transformers`
- [Troika (three-text)](tools/troika-three-text.md): YOLO (your own risk): skips the version pin and self-hosted fonts (fonts load from Google Fonts and jsDelivr).
npm install troika-three-text three
- [ts-fsrs](tools/ts-fsrs.md): YOLO (your own risk): skips the exact pin and allows the unreviewed native optimizer.
npm install ts-fsrs @open-spaced-repetition/binding
- [tstack (t3dotgg)](tools/tstack-t3dotgg.md): YOLO (your own risk): skips the commit pin and the deny rules that block `gh pr merge` and the GitHub MCP merge tool, so full-send can merge PRs and force-push.
Copy the skills as the README says, without those deny rules.
- [UI SDK (vercel-labs/ui)](tools/ui-sdk-vercel-labs-ui.md): YOLO (your own risk): skips the pin, --ignore-scripts, and the pin-or-self-host rule for web.js.
`npm install @ui-sdk/react @ui-sdk/core` (or the adapter) and `npx skills add vercel-labs/ui --skill ui-sdk` (README).
- [ui-ux-pro-max skill](tools/ui-ux-pro-max-skill.md): YOLO (your own risk): skips leaving out the stack/ template (auto-enables its project MCP servers and allows reading your home folder).
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill, then copy stack/ into the project as stack/docs/SETUP.md describes.
- [Unslop (UI design skill)](tools/unslop-ui-design-skill.md): YOLO (your own risk): skips the commit pin, project-only scope and audit-first step.
git clone https://github.com/heydamir/unslop && mkdir -p ~/.claude/skills && cp -r unslop/skills/unslop ~/.claude/skills/
- [Upload-Post MCP](tools/upload-post-mcp.md): YOLO (your own risk): skips the hosted-only rule (local npx mode can upload any absolute local file path, src/tools/upload.ts:625).
Install the official Upload-Post plugin from the Claude directory (README.md:23).
- [UX/UI Agent Skills (XIAS, plugin87)](tools/ux-ui-agent-skills-xias-plugin87.md): YOLO (your own risk): skips the commit pin (gets v3.1.0, unreviewed).
/plugin marketplace add plugin87/ux-ui-agent-skills then /plugin install ux-ui-agent-skills@ux-ui-agent-skills
- [Vercel](tools/vercel.md): YOLO (your own risk): skips the pinned project-local CLI and telemetry off.
`npm i -g vercel` (Vercel CLI docs).
- [Vercel AI SDK](tools/vercel-ai-sdk.md): YOLO (your own risk): skips the version pin (gets 7.0.173 from 2026-11-13, unreviewed).
npm install ai
- [video-director (win4r)](tools/video-director-win4r.md): YOLO (your own risk): skips the commit pin and the venv.
git clone https://github.com/win4r/video-director && pip install numpy Pillow
- [Video2X](tools/video2x.md): YOLO (your own risk): skips the CLI-only route; the Qt6 GUI's source is not in the reviewed repo (no GUI folder or submodule at 7db9c18), so the GUI is unreviewed.
video2x-qt6-windows-amd64-installer.exe from the 6.4.0 release (README.md:56).
- [Vite](tools/vite.md): YOLO (your own risk): skips the exact reviewed pin.
`npm create vite@latest` (vite.dev Getting Started).
- [VoiceStudio](tools/voicestudio.md): YOLO (your own risk): skips the release download (pipes the official script into PowerShell) and allows the MOSS-TTS engines.
irm https://voicestudio.sh/install.ps1 | iex
- [Wan2.1 (Wan-Video)](tools/wan2-1-wan-video.md): YOLO (your own risk): skips the commit pin, the venv and the local-only prompt rule.
git clone, pip install -r requirements.txt, --use_prompt_extend with dashscope and your DASH_API_KEY.
- [web-artifacts-builder (Anthropic)](tools/web-artifacts-builder-anthropic.md): YOLO (your own risk): skips installing pnpm yourself first, so the script runs `npm install -g pnpm` globally.
`/plugin marketplace add anthropics/skills` then `/plugin install example-skills@anthropic-agent-skills`
- [web-quality-skills](tools/web-quality-skills.md): YOLO (your own risk): skips the exact npx versions and uses the skill's global install.
/plugin marketplace add addyosmani/web-quality-skills
/plugin install web-quality-skills@addy-web-quality-skills
npm install -g @axe-core/cli
- [wllama](tools/wllama.md): YOLO (your own risk): skips the source build at the reviewed commit c10c211.
`npm install @wllama/wllama` (official npm package, latest 3.13.0 on 2026-11-14).
- [yt-dlp](tools/yt-dlp.md): YOLO (your own risk): skips the pin, config and plugin blocks and the no-cookies rule.
pip install -U yt-dlp then yt-dlp --cookies-from-browser chrome URL.
- [Zapier (connector)](tools/zapier-connector.md): YOLO (your own risk): skips managed mode, so it can write and run code.
Agentic mode with all actions.
- [Zernio MCP + Claude plugin](tools/zernio-mcp-claude-plugin.md): YOLO (your own risk): skips unticking the paid ads tools.
/plugin marketplace add zernio-dev/zernio-claude-plugin
/plugin install zernio@zernio
