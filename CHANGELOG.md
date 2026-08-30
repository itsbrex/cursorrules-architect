# Changelog

## [4.2.1](https://github.com/itsbrex/cursorrules-architect/compare/v4.3.0...v4.2.1) (2026-08-30)


### ⚠ BREAKING CHANGES

* **execplan:** deprecate archive in favor of complete

### Features

* add .gitignore integration with configurable respect setting ([7644417](https://github.com/itsbrex/cursorrules-architect/commit/7644417e80da05ca73e2ad0078d80633d811e7fc))
* add batch progress reporting and token-aware docs ([a1fe0be](https://github.com/itsbrex/cursorrules-architect/commit/a1fe0be154657008ce30b74ffd6624220d530c66))
* add Claude 4 family support and update model configurations ([6b30947](https://github.com/itsbrex/cursorrules-architect/commit/6b309476408e94f50e94bdf64e466248e68dd352))
* add comprehensive settings UI with exclusions, output preferences, and visual improvements ([9ee33b6](https://github.com/itsbrex/cursorrules-architect/commit/9ee33b634fdcf12316e9accd46fc483b6cc99e19))
* add configurable researcher mode with auto/on/off settings ([6c160ed](https://github.com/itsbrex/cursorrules-architect/commit/6c160eda55db2baeb50d4f4a22080678ac7aeb47))
* add configurable tree traversal depth with preview and CLI commands ([80de1b8](https://github.com/itsbrex/cursorrules-architect/commit/80de1b830ea854c2fc54f5645de7518cff3c3e3f))
* add DeepSeek tool calling support and improve model configuration ([3b14630](https://github.com/itsbrex/cursorrules-architect/commit/3b14630ef01be348013a4d6e7b88ddd9144d72fd))
* add dynamic thinking mode and improve Gemini configuration ([6133b79](https://github.com/itsbrex/cursorrules-architect/commit/6133b790531254369e259c81ea3f536fa81f0b98))
* add GPT-5 support with Responses API integration ([bfdd7e6](https://github.com/itsbrex/cursorrules-architect/commit/bfdd7e6eb14578dd0feeca7f17c29883f9ef0052))
* add real-time agent progress UI and configurable logging system ([fbc5e1c](https://github.com/itsbrex/cursorrules-architect/commit/fbc5e1c302ec0b64c375a3e81373b28f4610d1ca))
* add researcher mode guards to skip when no tools requested or all fail ([562a269](https://github.com/itsbrex/cursorrules-architect/commit/562a26975011776373e444ffa84dbcef103c5aac))
* add streaming support across all agent providers ([d96ef43](https://github.com/itsbrex/cursorrules-architect/commit/d96ef43477741983d7f6b69add779586c0a5d765))
* add xAI (Grok) model support with dedicated agent package ([5cfff7e](https://github.com/itsbrex/cursorrules-architect/commit/5cfff7eba142624ab6c18e9b2d7ea8121b077826))
* **agents:** add Claude Code SDK adapter ([5d1cf06](https://github.com/itsbrex/cursorrules-architect/commit/5d1cf06e45f808043020ed59c563303c385a2ca7))
* **agents:** enforce provider-native system prompt routing ([94b61bd](https://github.com/itsbrex/cursorrules-architect/commit/94b61bdca5e6d7b2c5f4a41d952c0862bd22a0b7))
* **anthropic:** add Claude Sonnet 5 and Fable 5 ([369ecdc](https://github.com/itsbrex/cursorrules-architect/commit/369ecdc4a43b4b3ea3eb0d0825594d57430faca8))
* **anthropic:** add effort knob support ([32ad7a0](https://github.com/itsbrex/cursorrules-architect/commit/32ad7a0c9e496056e03b592c5e0d74b269c41afa))
* **anthropic:** support claude-opus-4-6 adaptive thinking ([582feec](https://github.com/itsbrex/cursorrules-architect/commit/582feece3323efef93972541478dd7192feaef86))
* **claude-code:** add Claude Agent SDK runtime integration ([9558f06](https://github.com/itsbrex/cursorrules-architect/commit/9558f064ea3248a90abb48e9901f679456e0243e))
* **claude-code:** add runtime execution guardrails ([2543d4b](https://github.com/itsbrex/cursorrules-architect/commit/2543d4bc527fb093abbe2f19d80f2f9e4280d714))
* **claude-code:** modernize model selection and gating ([5806034](https://github.com/itsbrex/cursorrules-architect/commit/5806034f083b07becaf4298e46090b147d236198))
* **cli:** add Claude Code runtime settings ([dd24f18](https://github.com/itsbrex/cursorrules-architect/commit/dd24f184a6c4bc744697b84fcaa31348d54e7307))
* **cli:** add execplan new command group ([ef5e81c](https://github.com/itsbrex/cursorrules-architect/commit/ef5e81cd5baaaffaa5c41c95ec94ce14fdd8ca7a))
* **cli:** add execplan-registry command group ([688b10d](https://github.com/itsbrex/cursorrules-architect/commit/688b10d82dbd0f1b82964d1b54371c76d9b6b89b))
* **cli:** add recursive snapshot file discovery ([7b5d6ff](https://github.com/itsbrex/cursorrules-architect/commit/7b5d6fffe253a40a13285ebf24053fc76f123443))
* **cli:** add snapshot generate command ([1fa4ec2](https://github.com/itsbrex/cursorrules-architect/commit/1fa4ec2e947cf5d14e1a20d57cda948264a8980c))
* **cli:** improve provider scannability in model picker ([befe232](https://github.com/itsbrex/cursorrules-architect/commit/befe23262763aafc6069e6b0fedf0a5b4c3f247e))
* **codex-runtime:** add app-server integration and runtime model presets ([7a97463](https://github.com/itsbrex/cursorrules-architect/commit/7a974637b188f64e7875c9b8c95f9187a460b50d))
* **codex-runtime:** add dynamic model efforts and strict schemas ([39d0509](https://github.com/itsbrex/cursorrules-architect/commit/39d0509490e7d6ab3335b3ac018a3fe339176ec0))
* **codex:** add app-server runtime services ([a0a5200](https://github.com/itsbrex/cursorrules-architect/commit/a0a520028680b5fbc37dfea6fa56aa931cfa429f))
* **codex:** add architect request adapter ([fa8ca9d](https://github.com/itsbrex/cursorrules-architect/commit/fa8ca9de8935f3b863e15140a71cfe49b2f305ac))
* **codex:** add phase-specific runtime exceptions ([555f988](https://github.com/itsbrex/cursorrules-architect/commit/555f988f771065c32675e35066283d69d4263626))
* **codex:** establish runtime foundations ([a062324](https://github.com/itsbrex/cursorrules-architect/commit/a062324dad78f94d370d2fdd017b8cda1c2f809b))
* **codex:** finalize runtime rollout workflow ([864f724](https://github.com/itsbrex/cursorrules-architect/commit/864f7245791ad402a2f2b2799b4320eb9eca2d25))
* **codex:** preserve runtime efforts and refresh Gemini lifecycle ([9c7fae6](https://github.com/itsbrex/cursorrules-architect/commit/9c7fae69d3a77fd5be9a59763ae4dfeb49a82ee1))
* **config:** add Claude Code runtime foundation ([0299fbb](https://github.com/itsbrex/cursorrules-architect/commit/0299fbb87f1bbba2e7314cb2dfc17a6d90d3fae9))
* **core:** add structured outputs, snapshots, and release flow ([9117b73](https://github.com/itsbrex/cursorrules-architect/commit/9117b7365dffdd9550a86606afe623f9611ad09e))
* **deepseek:** migrate provider presets to V4 ([ea4cdc7](https://github.com/itsbrex/cursorrules-architect/commit/ea4cdc71dc7fa9c078bfdc4f243b015929c7cca4))
* **execplan:** add ExecPlan lifecycle tooling and scaffold outputs ([407fb8c](https://github.com/itsbrex/cursorrules-architect/commit/407fb8c3aabe0932d63edb14e4f5d7c665fa42ce))
* **execplan:** add milestone lifecycle CLI and core module ([aa4f96f](https://github.com/itsbrex/cursorrules-architect/commit/aa4f96f44b48f6e4eafdc0664ef2ba5328c6e8a2))
* **execplan:** deprecate archive in favor of complete ([8148fb0](https://github.com/itsbrex/cursorrules-architect/commit/8148fb0de1dd49d6636fa3e882982d12f5429471))
* **execplan:** harden archive flow and add progress listing ([05cbc42](https://github.com/itsbrex/cursorrules-architect/commit/05cbc4269e2b4cb92507dea04c8a8cb51622ce2e))
* **execplan:** make complete the canonical history layout ([abd52a8](https://github.com/itsbrex/cursorrules-architect/commit/abd52a8862932b95f7e50068f34110da96e8d2ce))
* **execplan:** support explicit milestone sequence on create ([7a30867](https://github.com/itsbrex/cursorrules-architect/commit/7a308672e1bb365e7e6d96a43a94ab1ca052e37f))
* implement comprehensive dependency scanning system ([2729d3f](https://github.com/itsbrex/cursorrules-architect/commit/2729d3fc55cfc2cd601bb1eced049e53c0b55a8e))
* **models:** add current provider model presets ([9a5da4a](https://github.com/itsbrex/cursorrules-architect/commit/9a5da4a11f465c34ed51aad9c019ca698eeec558))
* **models:** add GPT-5.5 presets and defaults ([72b7131](https://github.com/itsbrex/cursorrules-architect/commit/72b71312d5ac3fd32858b2bac116fd7df968de52))
* **models:** add GPT-5.5 presets and defaults ([1ecf656](https://github.com/itsbrex/cursorrules-architect/commit/1ecf65695d165c820e29f7034cc9cdc1de390a8c))
* **models:** add latest provider model presets ([4b5b8ca](https://github.com/itsbrex/cursorrules-architect/commit/4b5b8ca357046b73cc587e8418fa5fe52fac59ca))
* **models:** wire Claude Code runtime presets ([efecbcf](https://github.com/itsbrex/cursorrules-architect/commit/efecbcf150c46cbff5e6b2ccb2c5f3ff4d20177d))
* **openai:** add GPT-5.4 mini and nano presets ([269696a](https://github.com/itsbrex/cursorrules-architect/commit/269696a324b7c9967ccb867ac2ee1a84fd98ee22))
* **openai:** add GPT-5.4 mini and nano presets ([e5a435d](https://github.com/itsbrex/cursorrules-architect/commit/e5a435d52a2d4d0cf7d0d6d1284b86dd69c2f9b0))
* **openai:** add GPT-5.6 model family ([c58d036](https://github.com/itsbrex/cursorrules-architect/commit/c58d0361160e2ef7207884eb1b21e0fcff7c004c))
* **outputs:** add configurable .agent scaffold generation ([60684bf](https://github.com/itsbrex/cursorrules-architect/commit/60684bf34540d66b53cbe53760ac220ff3b9896f))
* **outputs:** add rules tree depth and harden snapshot output ([d1335bb](https://github.com/itsbrex/cursorrules-architect/commit/d1335bbefeb2890cec94599f6a3e48fcfaf3569b))
* **outputs:** enable SNAPSHOT.md generation by default ([825b1dd](https://github.com/itsbrex/cursorrules-architect/commit/825b1ddb74dd8d9f237acddd54d0ebfe0cfe34c1))
* **output:** support dynamic rules filename across pipeline ([c425ac7](https://github.com/itsbrex/cursorrules-architect/commit/c425ac740e798289d87f89b35fbd2ed7e3708ec5))
* **phase1:** add profile-gated specialized discovery agents ([d828a99](https://github.com/itsbrex/cursorrules-architect/commit/d828a994c66ae7fe8bc865b305cab667fa2eea49))
* **phase2:** add structured-output mode resolver with legacy fallback ([96d341c](https://github.com/itsbrex/cursorrules-architect/commit/96d341cd699ba34fcb1ccd8d3ca02b934190919f))
* **pipeline:** add project profile snapshot foundation ([219514f](https://github.com/itsbrex/cursorrules-architect/commit/219514f28b9b46c81a34d22c433b9ca4723d68d2))
* **pipeline:** add project-profile gated phase1 discovery ([8a89e20](https://github.com/itsbrex/cursorrules-architect/commit/8a89e20670356c396e5ef7ad7b3f8e619f1b53ff))
* **providers:** add Grok 4.6 and complete DeepSeek efforts ([13ecb9f](https://github.com/itsbrex/cursorrules-architect/commit/13ecb9f955528550df2c3153f6f4a5a9b41f07ad))
* **providers:** add Opus 5 and current Gemini Flash ([c818d52](https://github.com/itsbrex/cursorrules-architect/commit/c818d523846a4d0ea8d967028bf932c698608343))
* **providers:** refresh 2026 model catalogs and runtimes ([1342cea](https://github.com/itsbrex/cursorrules-architect/commit/1342cea8b7e5560f18aa2c3e9c30c912dc053a19))
* **providers:** refresh model registry and capabilities ([ccc535b](https://github.com/itsbrex/cursorrules-architect/commit/ccc535b868e93529ebb85d1075a9c8d905b79a9f))
* **scaffold:** add sync command and harden template writes ([950af28](https://github.com/itsbrex/cursorrules-architect/commit/950af288b6d731bb7ead6c62e7e42412c7a68dce))
* **snapshot:** add robust snapshot sync and pipeline integration ([eb250a0](https://github.com/itsbrex/cursorrules-architect/commit/eb250a0072e37b008ea4fe55a2faa0af991aaea7))
* **xai:** add Grok 4.5 and compatible 4.20 models ([80bf441](https://github.com/itsbrex/cursorrules-architect/commit/80bf441b5ef3f8ab729b294bb1bbbeb696a7dc2d))


### Bug Fixes

* **analysis:** fail fast on final generation errors ([64c862c](https://github.com/itsbrex/cursorrules-architect/commit/64c862c3255cd18e42fa67e03c6af120c7b5e2d3))
* **anthropic:** enforce Opus 5 runtime constraints ([a8e8802](https://github.com/itsbrex/cursorrules-architect/commit/a8e88027ca311c8f4f1a3b4fe13900826bb01e44))
* **anthropic:** honor shared reasoning efforts ([236e24b](https://github.com/itsbrex/cursorrules-architect/commit/236e24b824314a3c6deac3f8a8042f85681bf8de))
* **anthropic:** send output_config via extra_body ([f1f0473](https://github.com/itsbrex/cursorrules-architect/commit/f1f0473e63a791845b6b23fe9d466f50d006e813))
* **anthropic:** stream extended-effort responses ([ad0be67](https://github.com/itsbrex/cursorrules-architect/commit/ad0be67d3c6f153cdb0101c43ff7310894adbca2))
* **ci:** align release-please with vX.Y.Z tag history ([f2d48d6](https://github.com/itsbrex/cursorrules-architect/commit/f2d48d690a12494080af4c623d438d1cf5f49762))
* **claude-code:** defer default CLI resolution to SDK ([27e87fe](https://github.com/itsbrex/cursorrules-architect/commit/27e87feb7ef18e620bb3b94fd7d9879c500e55ad))
* **claude-code:** enforce streaming query timeouts ([3015191](https://github.com/itsbrex/cursorrules-architect/commit/301519114082c456d8dda039c6424d6d7f05fd08))
* **claude-code:** gate pinned Opus 5 by runtime ([9595fa1](https://github.com/itsbrex/cursorrules-architect/commit/9595fa1deb7ec43d86ae52eb8697ee689c0bb96c))
* **claude-code:** keep alias context runtime-owned ([fe1fc2b](https://github.com/itsbrex/cursorrules-architect/commit/fe1fc2ba9ff91d8fe176d32c80a65e9d9d3d8aa4))
* **claude-code:** keep token preflight local ([bb44987](https://github.com/itsbrex/cursorrules-architect/commit/bb449870d7649b1922ca1f9d0f0f1b2964a7ad67))
* **claude-code:** resolve configured cli path ([b6dd91f](https://github.com/itsbrex/cursorrules-architect/commit/b6dd91f03901033c59fa3d364b7a61e27f559f52))
* **claude-code:** scrub inherited API key env ([0841e06](https://github.com/itsbrex/cursorrules-architect/commit/0841e067624ba6556d7be36b7985b3d1ae6fe844))
* **claude-code:** validate sdk default runtime ([7f9deca](https://github.com/itsbrex/cursorrules-architect/commit/7f9deca23e92d7f901e0bf9180b6258faa68af73))
* **cli:** add missing help text for core commands ([9d2c199](https://github.com/itsbrex/cursorrules-architect/commit/9d2c19986286053de09387de56faa5246ab3f873))
* **cli:** condense snapshot sync output to path counts ([ff9717f](https://github.com/itsbrex/cursorrules-architect/commit/ff9717f3819a6f24d5f1452c262feb47d3b96392))
* **cli:** prevent duplicate phase 3 progress rows ([4a9c206](https://github.com/itsbrex/cursorrules-architect/commit/4a9c206808d000a2dbd5c12e22b0faaee274a2c4))
* **codex:** harden large phase transport handling ([bb17497](https://github.com/itsbrex/cursorrules-architect/commit/bb174974c776c5888cc792f451b1227080236d81))
* **codex:** harden runtime launch and wait handling ([3bc0685](https://github.com/itsbrex/cursorrules-architect/commit/3bc0685006d511515a9e6f2a9eb298c90c211cb4))
* **codex:** preserve inherited home state ([23140dc](https://github.com/itsbrex/cursorrules-architect/commit/23140dcac70a1623a52426872d79edbccddb02e8))
* **exclusions:** expand default ignore rules ([acbe9f6](https://github.com/itsbrex/cursorrules-architect/commit/acbe9f6ba959215c0beee84d595c5a881793ca44))
* **exclusions:** scope managed outputs to project root ([d089b55](https://github.com/itsbrex/cursorrules-architect/commit/d089b55bf2c2508cfd3c291147584a5ee6b18232))
* **execplan:** accept canonical .md filenames in id parsing ([062fea3](https://github.com/itsbrex/cursorrules-architect/commit/062fea3bd6efe39d61c153bd3ed937c01646e97f))
* **execplan:** allow read-only plan locks ([290fd67](https://github.com/itsbrex/cursorrules-architect/commit/290fd673ff28617dd488ac0f1eb7bc93b84296e0))
* **execplan:** correct milestone CLI guidance text ([b627543](https://github.com/itsbrex/cursorrules-architect/commit/b627543ed8ecd95b9d5119bb5771e28913d8e76a))
* **execplan:** enforce date token and handle external execplans paths ([6507e1c](https://github.com/itsbrex/cursorrules-architect/commit/6507e1c76ba843a7c05d114cde9848f72069e834))
* **execplan:** harden path resolution and filesystem error handling ([f008389](https://github.com/itsbrex/cursorrules-architect/commit/f0083899861591a89d140ede8d4c10255b162e53))
* **execplan:** reject multiline metadata before YAML serialization ([70cf212](https://github.com/itsbrex/cursorrules-architect/commit/70cf212ee502fa62712330f62ec76a287324ad2c))
* **execplan:** serialize milestone sequence allocation ([66e4d88](https://github.com/itsbrex/cursorrules-architect/commit/66e4d88f02106a9739b7200263c07d6fcddf45a9))
* **execplan:** support block-style YAML front matter lists ([8bf8167](https://github.com/itsbrex/cursorrules-architect/commit/8bf816716f70a016dedf6f40080eba7ac9fdb6a3))
* **execplan:** use structured subtree checks for milestones and archive ([baa1fec](https://github.com/itsbrex/cursorrules-architect/commit/baa1fec12d6355d59ce1b25620e0609c6b91d503))
* **formatters:** expand ExecPlans guidance injection ([35b4a2c](https://github.com/itsbrex/cursorrules-architect/commit/35b4a2cef1e4d781417cefaf81b6eae2c05ce242))
* **models:** add Gemini 3.5 and remap retired presets ([3726b03](https://github.com/itsbrex/cursorrules-architect/commit/3726b0329d6ebb80fb3c935114f10dd1caacfb4e))
* **models:** harden codex and claude runtime selection ([c6d42cb](https://github.com/itsbrex/cursorrules-architect/commit/c6d42cb56ce52e76e940a5ccb6cbe1b603bb32bf))
* **models:** preserve deprecated endpoint behavior ([b5102f2](https://github.com/itsbrex/cursorrules-architect/commit/b5102f2e84a8e09e8a34123631e6db63cdda6309))
* **models:** preserve OpenAI lifecycle compatibility ([4e19179](https://github.com/itsbrex/cursorrules-architect/commit/4e1917970a70fda095fdb3073b8318fa5f504293))
* **openai:** reserve output capacity in input limits ([37ef0d1](https://github.com/itsbrex/cursorrules-architect/commit/37ef0d12552b0a443b16b001bd3ae4e2dae5355f))
* **output:** enforce ExecPlans guidance in generated rules ([a4712e4](https://github.com/itsbrex/cursorrules-architect/commit/a4712e4a81d859d6a4d8ce5a16fbdb0f555b1d45))
* **output:** exclude custom managed files from AGENTS tree ([1c6a28b](https://github.com/itsbrex/cursorrules-architect/commit/1c6a28b02df5289005a00feb5c6bcd6b628c99ef))
* **phase2:** preserve explicit empty structured agents ([121f8e0](https://github.com/itsbrex/cursorrules-architect/commit/121f8e0bf79fb13b60547d040e9512f44a1d6241))
* **pipeline:** exclude managed outputs and normalize agents ([5d0b498](https://github.com/itsbrex/cursorrules-architect/commit/5d0b49833c33d0561891fecc51ea8f2b5f42d0ed))
* **project-profile:** preserve signal files under exclusions ([a561c22](https://github.com/itsbrex/cursorrules-architect/commit/a561c229d41bb497046135d7e7cb357fa5c0fcc6))
* **project-profile:** scope signals to visible scan rules ([6955326](https://github.com/itsbrex/cursorrules-architect/commit/69553269f3b55faf66eb90e10920e38e8091a317))
* **prompts:** refocus analysis prompts on onboarding ([1c48262](https://github.com/itsbrex/cursorrules-architect/commit/1c48262c947664b782df667eb14330412abc3b53))
* **prompts:** use year-only final temporal context ([c559225](https://github.com/itsbrex/cursorrules-architect/commit/c5592250cdfad5392d0cdc049d3ee850c1b3e12a))
* **providers:** align smoke and lifecycle audit ([815d7b8](https://github.com/itsbrex/cursorrules-architect/commit/815d7b8db90fc6518954b8117a9d4dafd866d11d))
* **providers:** enforce current lifecycle constraints ([f65593c](https://github.com/itsbrex/cursorrules-architect/commit/f65593c48b6ef24c76577bf6fc2c600c57debf70))
* **providers:** enforce runtime reasoning contracts ([35bed5e](https://github.com/itsbrex/cursorrules-architect/commit/35bed5e23545ebc240207364ec682bcc50ae0915))
* **providers:** honor model-specific request contracts ([d364f1a](https://github.com/itsbrex/cursorrules-architect/commit/d364f1a4aa1ad8054480d82f59f898378efbeb0d))
* **providers:** secure streams and runtime probes ([bcaf330](https://github.com/itsbrex/cursorrules-architect/commit/bcaf33014b8c48ca92e576ec2d3451c75db6c86a))
* **registry:** enforce strict filename/front-matter id consistency ([246a2d1](https://github.com/itsbrex/cursorrules-architect/commit/246a2d1c23afb736ff9336f7a8be8e233320abe5))
* **registry:** resolve default paths against provided root ([6fe37e4](https://github.com/itsbrex/cursorrules-architect/commit/6fe37e4ae56abd7c880bdb6d63dcf74216b89ee2))
* **snapshot:** make snapshot tree-only with unlimited default depth ([87ab7b0](https://github.com/itsbrex/cursorrules-architect/commit/87ab7b0ddadc26a6229eba237779e68ced671efc))
* **snapshot:** preserve inline comments during sync ([1c4e691](https://github.com/itsbrex/cursorrules-architect/commit/1c4e691247a5b4fbb5956abf0eecfc3f4cc1af48))
* **snapshot:** simplify max-depth tree marker ([1c4f7d1](https://github.com/itsbrex/cursorrules-architect/commit/1c4f7d19d6d0f369f99bcb80d1f04581cd482d7d))
* **structured-outputs:** harden provider schema and parsing flow ([abdda32](https://github.com/itsbrex/cursorrules-architect/commit/abdda32c30cd26876413e779dfeccc4d99a8974b))
* **types:** align phase contracts with pyright ([f7ee725](https://github.com/itsbrex/cursorrules-architect/commit/f7ee725fcb0275c58e3fd8451a3b957f3a9e51d5))
* **xai:** migrate Grok presets to canonical models ([6ba5c56](https://github.com/itsbrex/cursorrules-architect/commit/6ba5c5673e520933c8c184ce861283ec66baa2c1))
* **xai:** reject untranslatable reasoning modes ([3272e39](https://github.com/itsbrex/cursorrules-architect/commit/3272e39afea50623e9f91cc4e59bd8a26f68a0be))


### Documentation

* **claude-code:** document runtime rollout ([44cf0d3](https://github.com/itsbrex/cursorrules-architect/commit/44cf0d321bbeb6786ad72875334f3f5d3951f7cb))
* **execplan:** archive provider model refresh ([42f5a62](https://github.com/itsbrex/cursorrules-architect/commit/42f5a62ba0a262f89eff1003b34588470a96ba24))
* **execplan:** archive provider model refresh ([15d52c9](https://github.com/itsbrex/cursorrules-architect/commit/15d52c98ed4bf6d6d274352c059980152a14b74f))
* **execplan:** complete provider contract baseline ([c02187f](https://github.com/itsbrex/cursorrules-architect/commit/c02187f25776ccd797c3ca075ab733e63fa9a9d2))
* **execplan:** plan provider model refresh ([a48405f](https://github.com/itsbrex/cursorrules-architect/commit/a48405fcc14d81fe9c2f5afc09cf3d88d2bee7c1))
* **models:** complete integration validation ([4680e88](https://github.com/itsbrex/cursorrules-architect/commit/4680e88c4e91bd016dcb82f30725c32e971c0077))
* **providers:** scope Anthropic refusal guidance ([481c3d0](https://github.com/itsbrex/cursorrules-architect/commit/481c3d045cc1b5123de46779fd93e37baf75976c))
* **readme:** make model guidance provider-neutral ([10b439d](https://github.com/itsbrex/cursorrules-architect/commit/10b439dbc9847373ec3a4b1c1455f1051ffc1543))
* **readme:** refresh project overview ([309f2e7](https://github.com/itsbrex/cursorrules-architect/commit/309f2e7539daf27936d4746c363e21deaf1c02ec))
* **readme:** update PyPI install and release guidance ([dce1184](https://github.com/itsbrex/cursorrules-architect/commit/dce1184d495efa7df9de20115db6ed482e38415f))
* remove CLAUDE.md and add phases_output directory ([d8096d7](https://github.com/itsbrex/cursorrules-architect/commit/d8096d706fb2988a4dc8339a447574f53e1b2c1e))
* **templates:** make scaffold templates provider-agnostic ([fe4fb7d](https://github.com/itsbrex/cursorrules-architect/commit/fe4fb7d7e3d18515b72ea49feb62e2edf5de118f))
* update SNAPSHOT documentation for modularized agent packages ([b2cfeb2](https://github.com/itsbrex/cursorrules-architect/commit/b2cfeb260446de1ccea9a0d1d11274b33a39bb79))


### Miscellaneous Chores

* **release:** target 4.2.1 patch release ([a70516c](https://github.com/itsbrex/cursorrules-architect/commit/a70516c5ef0b39bdc078f4cc06863a06f9aeac58))

## [4.3.0](https://github.com/trevor-nichols/agentrules-architect/compare/v4.2.1...v4.3.0) (2026-08-30)


### Features

* **providers:** add Grok 4.6 and complete DeepSeek efforts ([13ecb9f](https://github.com/trevor-nichols/agentrules-architect/commit/13ecb9f955528550df2c3153f6f4a5a9b41f07ad))
* **providers:** add Opus 5 and current Gemini Flash ([c818d52](https://github.com/trevor-nichols/agentrules-architect/commit/c818d523846a4d0ea8d967028bf932c698608343))
* **providers:** refresh model registry and capabilities ([ccc535b](https://github.com/trevor-nichols/agentrules-architect/commit/ccc535b868e93529ebb85d1075a9c8d905b79a9f))


### Bug Fixes

* **anthropic:** enforce Opus 5 runtime constraints ([a8e8802](https://github.com/trevor-nichols/agentrules-architect/commit/a8e88027ca311c8f4f1a3b4fe13900826bb01e44))
* **anthropic:** honor shared reasoning efforts ([236e24b](https://github.com/trevor-nichols/agentrules-architect/commit/236e24b824314a3c6deac3f8a8042f85681bf8de))
* **claude-code:** gate pinned Opus 5 by runtime ([9595fa1](https://github.com/trevor-nichols/agentrules-architect/commit/9595fa1deb7ec43d86ae52eb8697ee689c0bb96c))
* **models:** preserve deprecated endpoint behavior ([b5102f2](https://github.com/trevor-nichols/agentrules-architect/commit/b5102f2e84a8e09e8a34123631e6db63cdda6309))
* **models:** preserve OpenAI lifecycle compatibility ([4e19179](https://github.com/trevor-nichols/agentrules-architect/commit/4e1917970a70fda095fdb3073b8318fa5f504293))
* **openai:** reserve output capacity in input limits ([37ef0d1](https://github.com/trevor-nichols/agentrules-architect/commit/37ef0d12552b0a443b16b001bd3ae4e2dae5355f))
* **providers:** align smoke and lifecycle audit ([815d7b8](https://github.com/trevor-nichols/agentrules-architect/commit/815d7b8db90fc6518954b8117a9d4dafd866d11d))
* **providers:** enforce current lifecycle constraints ([f65593c](https://github.com/trevor-nichols/agentrules-architect/commit/f65593c48b6ef24c76577bf6fc2c600c57debf70))
* **xai:** reject untranslatable reasoning modes ([3272e39](https://github.com/trevor-nichols/agentrules-architect/commit/3272e39afea50623e9f91cc4e59bd8a26f68a0be))


### Documentation

* **execplan:** archive provider model refresh ([42f5a62](https://github.com/trevor-nichols/agentrules-architect/commit/42f5a62ba0a262f89eff1003b34588470a96ba24))
* **execplan:** complete provider contract baseline ([c02187f](https://github.com/trevor-nichols/agentrules-architect/commit/c02187f25776ccd797c3ca075ab733e63fa9a9d2))
* **execplan:** plan provider model refresh ([a48405f](https://github.com/trevor-nichols/agentrules-architect/commit/a48405fcc14d81fe9c2f5afc09cf3d88d2bee7c1))
* **models:** complete integration validation ([4680e88](https://github.com/trevor-nichols/agentrules-architect/commit/4680e88c4e91bd016dcb82f30725c32e971c0077))

## [4.2.1](https://github.com/trevor-nichols/agentrules-architect/compare/v4.2.0...v4.2.1) (2026-07-18)


### Features

* **anthropic:** add Claude Sonnet 5 and Fable 5 ([369ecdc](https://github.com/trevor-nichols/agentrules-architect/commit/369ecdc4a43b4b3ea3eb0d0825594d57430faca8))
* **claude-code:** modernize model selection and gating ([5806034](https://github.com/trevor-nichols/agentrules-architect/commit/5806034f083b07becaf4298e46090b147d236198))
* **codex:** preserve runtime efforts and refresh Gemini lifecycle ([9c7fae6](https://github.com/trevor-nichols/agentrules-architect/commit/9c7fae69d3a77fd5be9a59763ae4dfeb49a82ee1))
* **deepseek:** migrate provider presets to V4 ([ea4cdc7](https://github.com/trevor-nichols/agentrules-architect/commit/ea4cdc71dc7fa9c078bfdc4f243b015929c7cca4))
* **openai:** add GPT-5.6 model family ([c58d036](https://github.com/trevor-nichols/agentrules-architect/commit/c58d0361160e2ef7207884eb1b21e0fcff7c004c))
* **providers:** refresh 2026 model catalogs and runtimes ([1342cea](https://github.com/trevor-nichols/agentrules-architect/commit/1342cea8b7e5560f18aa2c3e9c30c912dc053a19))
* **xai:** add Grok 4.5 and compatible 4.20 models ([80bf441](https://github.com/trevor-nichols/agentrules-architect/commit/80bf441b5ef3f8ab729b294bb1bbbeb696a7dc2d))


### Bug Fixes

* **anthropic:** stream extended-effort responses ([ad0be67](https://github.com/trevor-nichols/agentrules-architect/commit/ad0be67d3c6f153cdb0101c43ff7310894adbca2))
* **claude-code:** keep alias context runtime-owned ([fe1fc2b](https://github.com/trevor-nichols/agentrules-architect/commit/fe1fc2ba9ff91d8fe176d32c80a65e9d9d3d8aa4))
* **providers:** enforce runtime reasoning contracts ([35bed5e](https://github.com/trevor-nichols/agentrules-architect/commit/35bed5e23545ebc240207364ec682bcc50ae0915))
* **providers:** honor model-specific request contracts ([d364f1a](https://github.com/trevor-nichols/agentrules-architect/commit/d364f1a4aa1ad8054480d82f59f898378efbeb0d))
* **providers:** secure streams and runtime probes ([bcaf330](https://github.com/trevor-nichols/agentrules-architect/commit/bcaf33014b8c48ca92e576ec2d3451c75db6c86a))


### Documentation

* **execplan:** archive provider model refresh ([15d52c9](https://github.com/trevor-nichols/agentrules-architect/commit/15d52c98ed4bf6d6d274352c059980152a14b74f))
* **providers:** scope Anthropic refusal guidance ([481c3d0](https://github.com/trevor-nichols/agentrules-architect/commit/481c3d045cc1b5123de46779fd93e37baf75976c))


### Miscellaneous Chores

* **release:** target 4.2.1 patch release ([a70516c](https://github.com/trevor-nichols/agentrules-architect/commit/a70516c5ef0b39bdc078f4cc06863a06f9aeac58))

## [4.2.0](https://github.com/trevor-nichols/agentrules-architect/compare/v4.1.0...v4.2.0) (2026-06-03)


### Features

* **models:** add current provider model presets ([9a5da4a](https://github.com/trevor-nichols/agentrules-architect/commit/9a5da4a11f465c34ed51aad9c019ca698eeec558))


### Bug Fixes

* **models:** add Gemini 3.5 and remap retired presets ([3726b03](https://github.com/trevor-nichols/agentrules-architect/commit/3726b0329d6ebb80fb3c935114f10dd1caacfb4e))
* **models:** harden codex and claude runtime selection ([c6d42cb](https://github.com/trevor-nichols/agentrules-architect/commit/c6d42cb56ce52e76e940a5ccb6cbe1b603bb32bf))
* **xai:** migrate Grok presets to canonical models ([6ba5c56](https://github.com/trevor-nichols/agentrules-architect/commit/6ba5c5673e520933c8c184ce861283ec66baa2c1))


### Documentation

* **readme:** refresh project overview ([309f2e7](https://github.com/trevor-nichols/agentrules-architect/commit/309f2e7539daf27936d4746c363e21deaf1c02ec))

## [4.1.0](https://github.com/trevor-nichols/agentrules-architect/compare/v4.0.0...v4.1.0) (2026-05-08)


### Features

* **agents:** add Claude Code SDK adapter ([5d1cf06](https://github.com/trevor-nichols/agentrules-architect/commit/5d1cf06e45f808043020ed59c563303c385a2ca7))
* **claude-code:** add Claude Agent SDK runtime integration ([9558f06](https://github.com/trevor-nichols/agentrules-architect/commit/9558f064ea3248a90abb48e9901f679456e0243e))
* **claude-code:** add runtime execution guardrails ([2543d4b](https://github.com/trevor-nichols/agentrules-architect/commit/2543d4bc527fb093abbe2f19d80f2f9e4280d714))
* **cli:** add Claude Code runtime settings ([dd24f18](https://github.com/trevor-nichols/agentrules-architect/commit/dd24f184a6c4bc744697b84fcaa31348d54e7307))
* **config:** add Claude Code runtime foundation ([0299fbb](https://github.com/trevor-nichols/agentrules-architect/commit/0299fbb87f1bbba2e7314cb2dfc17a6d90d3fae9))
* **models:** wire Claude Code runtime presets ([efecbcf](https://github.com/trevor-nichols/agentrules-architect/commit/efecbcf150c46cbff5e6b2ccb2c5f3ff4d20177d))


### Bug Fixes

* **analysis:** fail fast on final generation errors ([64c862c](https://github.com/trevor-nichols/agentrules-architect/commit/64c862c3255cd18e42fa67e03c6af120c7b5e2d3))
* **claude-code:** defer default CLI resolution to SDK ([27e87fe](https://github.com/trevor-nichols/agentrules-architect/commit/27e87feb7ef18e620bb3b94fd7d9879c500e55ad))
* **claude-code:** enforce streaming query timeouts ([3015191](https://github.com/trevor-nichols/agentrules-architect/commit/301519114082c456d8dda039c6424d6d7f05fd08))
* **claude-code:** keep token preflight local ([bb44987](https://github.com/trevor-nichols/agentrules-architect/commit/bb449870d7649b1922ca1f9d0f0f1b2964a7ad67))
* **claude-code:** resolve configured cli path ([b6dd91f](https://github.com/trevor-nichols/agentrules-architect/commit/b6dd91f03901033c59fa3d364b7a61e27f559f52))
* **claude-code:** scrub inherited API key env ([0841e06](https://github.com/trevor-nichols/agentrules-architect/commit/0841e067624ba6556d7be36b7985b3d1ae6fe844))
* **claude-code:** validate sdk default runtime ([7f9deca](https://github.com/trevor-nichols/agentrules-architect/commit/7f9deca23e92d7f901e0bf9180b6258faa68af73))


### Documentation

* **claude-code:** document runtime rollout ([44cf0d3](https://github.com/trevor-nichols/agentrules-architect/commit/44cf0d321bbeb6786ad72875334f3f5d3951f7cb))

## [4.0.0](https://github.com/trevor-nichols/agentrules-architect/compare/v3.8.0...v4.0.0) (2026-05-05)


### ⚠ BREAKING CHANGES

* **execplan:** deprecate archive in favor of complete

### Features

* **execplan:** deprecate archive in favor of complete ([8148fb0](https://github.com/trevor-nichols/agentrules-architect/commit/8148fb0de1dd49d6636fa3e882982d12f5429471))

## [3.8.0](https://github.com/trevor-nichols/agentrules-architect/compare/v3.7.0...v3.8.0) (2026-04-25)


### Features

* **models:** add GPT-5.5 presets and defaults ([72b7131](https://github.com/trevor-nichols/agentrules-architect/commit/72b71312d5ac3fd32858b2bac116fd7df968de52))
* **models:** add GPT-5.5 presets and defaults ([1ecf656](https://github.com/trevor-nichols/agentrules-architect/commit/1ecf65695d165c820e29f7034cc9cdc1de390a8c))

## [3.7.0](https://github.com/trevor-nichols/agentrules-architect/compare/v3.6.0...v3.7.0) (2026-04-05)


### Features

* **execplan:** make complete the canonical history layout ([abd52a8](https://github.com/trevor-nichols/agentrules-architect/commit/abd52a8862932b95f7e50068f34110da96e8d2ce))


### Bug Fixes

* **codex:** harden large phase transport handling ([bb17497](https://github.com/trevor-nichols/agentrules-architect/commit/bb174974c776c5888cc792f451b1227080236d81))
* **execplan:** allow read-only plan locks ([290fd67](https://github.com/trevor-nichols/agentrules-architect/commit/290fd673ff28617dd488ac0f1eb7bc93b84296e0))
* **execplan:** serialize milestone sequence allocation ([66e4d88](https://github.com/trevor-nichols/agentrules-architect/commit/66e4d88f02106a9739b7200263c07d6fcddf45a9))
* **snapshot:** simplify max-depth tree marker ([1c4f7d1](https://github.com/trevor-nichols/agentrules-architect/commit/1c4f7d19d6d0f369f99bcb80d1f04581cd482d7d))

## [3.6.0](https://github.com/trevor-nichols/agentrules-architect/compare/v3.5.0...v3.6.0) (2026-03-21)


### Features

* **openai:** add GPT-5.4 mini and nano presets ([269696a](https://github.com/trevor-nichols/agentrules-architect/commit/269696a324b7c9967ccb867ac2ee1a84fd98ee22))
* **openai:** add GPT-5.4 mini and nano presets ([e5a435d](https://github.com/trevor-nichols/agentrules-architect/commit/e5a435d52a2d4d0cf7d0d6d1284b86dd69c2f9b0))

## [3.4.3](https://github.com/trevor-nichols/agentrules-architect/compare/v3.4.2...v3.4.3) (2026-03-11)


### Bug Fixes

* **ci:** align release-please with vX.Y.Z tag history ([f2d48d6](https://github.com/trevor-nichols/agentrules-architect/commit/f2d48d690a12494080af4c623d438d1cf5f49762))
