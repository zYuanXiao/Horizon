---
layout: default
title: "Horizon Summary: 2026-07-01 (EN)"
date: 2026-07-01
lang: en
---

> From 158 items, 15 important content pieces were selected

---

1. [US Lifts Export Controls on Anthropic's Claude Fable 5 and Mythos 5](#item-1) ⭐️ 9.0/10
2. [Google's agents-cli: CLI for AI Agent Development on Google Cloud](#item-2) ⭐️ 8.0/10
3. [OmniRoute: Free AI Gateway with 231+ Providers Gains 387 Stars in a Day](#item-3) ⭐️ 8.0/10
4. [Orca: A Unified World Foundation Model via Next-State Prediction](#item-4) ⭐️ 8.0/10
5. [LiveEdit: Real-Time Diffusion-Based Streaming Video Editing](#item-5) ⭐️ 8.0/10
6. [DIY mmWave Radar Classifies Materials, Aims for Asbestos Detection](#item-6) ⭐️ 8.0/10
7. [ZLUDA 6: Run Unmodified CUDA Apps on Non-Nvidia GPUs](#item-7) ⭐️ 8.0/10
8. [Shot-scraper video records agent demos via Playwright](#item-8) ⭐️ 8.0/10
9. [Sonnet 5 and Fable 5 AI Models Announced](#item-9) ⭐️ 8.0/10
10. [New attack bypasses AI browser guardrails with false arithmetic](#item-10) ⭐️ 8.0/10
11. [audio.cpp Adds VibeVoice 1.5B, Achieves 4x Real-Time TTS](#item-11) ⭐️ 8.0/10
12. [NVIDIA Releases Qwen3.6-27B-NVFP4 for Efficient Local Inference](#item-12) ⭐️ 8.0/10
13. [Huawei Open-Sources OpenPangu-2.0-Flash MoE Model](#item-13) ⭐️ 8.0/10
14. [PageStorm: A Model for Full-Book Creative Writing](#item-14) ⭐️ 8.0/10
15. [Meta reuses old DDR4 memory in new DDR5 servers via custom CXL 2.0 chip](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [US Lifts Export Controls on Anthropic's Claude Fable 5 and Mythos 5](https://twitter.com/AnthropicAI/status/2072106151890809341) ⭐️ 9.0/10

The Department of Commerce has lifted export controls on Anthropic's Claude Fable 5 and Mythos 5 models, allowing their broader deployment after Anthropic implemented new safety classifiers to block cybersecurity tasks. This policy reversal highlights the unpredictability of AI export controls, affecting businesses that rely on frontier models and sparking debate on whether AI regulation should be governed by clear laws rather than executive actions. Claude Fable 5 is Anthropic's most capable widely released model, while Mythos 5 shares the same capabilities but remains in limited release through Project Glasswing. The lifted controls come after a series of letters from Commerce to Anthropic addressing risks.

hackernews · Pragmata · Jun 30, 23:55 · [Discussion](https://news.ycombinator.com/item?id=48740771)

**Background**: Export controls on AI models are used to prevent advanced technology from falling into the hands of adversaries. Anthropic's Claude models are frontier large language models, with Mythos 5 designed for cybersecurity vulnerability discovery. The UK AI Security Institute previously tested Claude Mythos and ranked it highest in cyber range tests.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mythos_5">Mythos 5</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5 - Claude Platform Docs</a></li>

</ul>
</details>

**Discussion**: Community comments express frustration over regulatory unpredictability, with users noting that businesses cannot rely on US frontier models for critical functions. Some highlight that Fable 5 now blocks coding tasks, falling back to Opus 4.8, while others argue that Chinese models have already reduced the impact of export controls.

**Tags**: `#AI regulation`, `#export controls`, `#Anthropic`, `#policy`, `#frontier models`

---

<a id="item-2"></a>
## [Google's agents-cli: CLI for AI Agent Development on Google Cloud](https://github.com/google/agents-cli) ⭐️ 8.0/10

Google released agents-cli, a CLI tool and set of skills that enables any coding assistant to create, evaluate, and deploy AI agents on Google Cloud. It gained 445 stars on GitHub in a single day, reaching 4303 total stars. This tool simplifies the full lifecycle of AI agent development on Google Cloud, making it accessible to developers using popular coding assistants like Gemini CLI, Claude Code, and Cursor. It could accelerate adoption of Google's Agent Platform and reduce friction in deploying production-ready agents. agents-cli is not a coding agent itself but provides CLI commands and skills that enhance coding assistants to build, evaluate, and deploy ADK agents on Google Cloud. It integrates with Google's Agent Platform, Model Garden, and RAG Engine.

github_trending · GitHub Trending · Jul 1, 04:16

**Background**: AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. Google Cloud's Agent Platform provides tools for building, deploying, and managing these agents, including access to models like Gemini and Claude, a RAG engine, and vector search. agents-cli bridges the gap between coding assistants and this platform, enabling a streamlined workflow from development to production.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/google/agents-cli">GitHub - google/agents-cli: The CLI and skills that turn any coding assistant into an expert at creating, evaluating, and deploying AI agents on Google Cloud. · GitHub</a></li>
<li><a href="https://google.github.io/agents-cli/">Unified CLI for the full ADK agent development lifecycle</a></li>
<li><a href="https://developers.googleblog.com/agents-cli-in-agent-platform-create-to-production-in-one-cli/">Agents CLI in Agent Platform: create to production in one CLI - Google Developers Blog</a></li>

</ul>
</details>

**Discussion**: The community response has been highly positive, with many developers praising the tool's integration with existing coding assistants and its potential to simplify agent deployment. Some users expressed interest in support for other cloud providers, but overall sentiment is enthusiastic.

**Tags**: `#AI Agents`, `#Google Cloud`, `#CLI`, `#Python`, `#DevOps`

---

<a id="item-3"></a>
## [OmniRoute: Free AI Gateway with 231+ Providers Gains 387 Stars in a Day](https://github.com/diegosouzapw/OmniRoute) ⭐️ 8.0/10

OmniRoute, a free AI gateway that provides a single endpoint for over 231 AI providers (including 50+ free ones), has rapidly gained 387 stars in one day on GitHub, reaching 8,712 total stars. It features RTK+Caveman stacked token compression saving 15-95% and smart auto-fallback, and integrates with tools like Claude Code, Cursor, and Copilot. OmniRoute simplifies access to a vast array of AI models through a single API, reducing costs via token compression and improving reliability with fallback mechanisms. This could significantly lower barriers for developers integrating AI into their workflows, especially those using multiple providers. The project is written in TypeScript and supports protocols like MCP (Model Context Protocol) and A2A (Agent-to-Agent). It also offers a desktop app and PWA, and claims compatibility with Claude Code, Codex, Cursor, Cline, and Copilot.

github_trending · GitHub Trending · Jul 1, 04:16

**Background**: AI gateways act as intermediaries that route requests to various AI model providers, offering a unified interface. Token compression techniques like RTK (Rust Token Killer) and Caveman reduce the number of tokens sent to or received from LLMs, cutting costs. MCP and A2A are emerging protocols for AI agent interoperability.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/diegosouzapw/OmniRoute">GitHub - diegosouzapw/OmniRoute: Never stop coding. Free AI gateway: one endpoint, 160+ providers (50+ free), connect Claude Code, Codex, Cursor, Cline & Copilot to FREE Claude/GPT/Gemini. RTK+Caveman stacked compression saves 15-95% tokens, smart auto-fallback, MCP/A2A, multimodal APIs, Desktop/PWA. · GitHub</a></li>
<li><a href="https://dev.to/sonim1/token-saving-and-caveman-e1f">Token Saving, and Caveman - DEV Community</a></li>
<li><a href="https://auth0.com/blog/mcp-vs-a2a/">MCP vs A2A: A Guide to AI Agent Communication Protocols</a></li>

</ul>
</details>

**Tags**: `#AI`, `#API Gateway`, `#TypeScript`, `#Open Source`, `#Developer Tools`

---

<a id="item-4"></a>
## [Orca: A Unified World Foundation Model via Next-State Prediction](https://huggingface.co/papers/2606.30534) ⭐️ 8.0/10

Researchers introduced Orca, a world foundation model that learns a unified latent space from multimodal data using next-state-prediction, outperforming specialized baselines on downstream tasks like text generation, image prediction, and embodied action generation. Orca's unified approach to modeling world states could accelerate progress toward general AI systems that understand and interact with the physical world, reducing the need for task-specific models. Orca was pretrained on 125K hours of video and 160M event annotations, using both unconscious learning from continuous videos and conscious learning from language-described events. Its backbone is frozen during downstream tasks, with only lightweight modality-specific decoders being trainable.

huggingface_papers · Hugging Face Papers · Jul 1, 00:00

**Background**: World foundation models aim to create a digital twin of the physical world that AI systems can safely interact with. Unlike traditional next-token or next-frame prediction, next-state-prediction models the underlying state transitions of the world, enabling counterfactual simulation and reasoning about consequences.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/world-models/">What Are World Models and How Are They Built?</a></li>
<li><a href="https://arxiv.org/html/2501.03575v1">Cosmos World Foundation Model Platform for Physical AI</a></li>
<li><a href="https://beykeworkflows.com/ai-world-models-next-state-strategy/">AI World Models: The Strategic Shift from Next Token to Next State</a></li>

</ul>
</details>

**Tags**: `#world model`, `#multimodal learning`, `#foundation model`, `#next-state-prediction`, `#AI`

---

<a id="item-5"></a>
## [LiveEdit: Real-Time Diffusion-Based Streaming Video Editing](https://huggingface.co/papers/2606.26740) ⭐️ 8.0/10

Researchers propose LiveEdit, a streaming video editing framework that achieves real-time frame-by-frame editing at 12.66 FPS using a three-stage distillation pipeline and an AR-oriented mask cache. This work addresses two critical bottlenecks in streaming video editing—long-horizon content preservation and low-latency inference—making it suitable for interactive and augmented reality applications. The three-stage distillation pipeline progressively transfers editing capability from a bidirectional foundation model to an efficient unidirectional streaming editor, while the AR-oriented mask cache reuses region-related computation across frames to reduce redundant processing.

huggingface_papers · Hugging Face Papers · Jun 30, 00:00

**Background**: Streaming video editing requires causal, frame-by-frame processing with strict preservation of unedited regions, which existing streaming generation methods cannot directly handle due to their focus on synthesis. Diffusion models have shown promise in image editing but face latency and consistency challenges when applied to video. LiveEdit introduces a dedicated benchmark for streaming video editing to standardize evaluation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.26740">LiveEdit: Towards Real-Time Diffusion-Based Streaming Video Editing</a></li>
<li><a href="https://huggingface.co/papers/2606.26740">Paper page - LiveEdit: Towards Real-Time Diffusion-Based Streaming Video Editing</a></li>
<li><a href="https://arxiv.org/abs/2606.26740">[2606.26740] LiveEdit: Towards Real-Time Diffusion-Based Streaming Video Editing</a></li>

</ul>
</details>

**Tags**: `#video editing`, `#diffusion models`, `#real-time`, `#streaming`, `#AI/ML`

---

<a id="item-6"></a>
## [DIY mmWave Radar Classifies Materials, Aims for Asbestos Detection](https://gauthier-lechevalier.com/radar) ⭐️ 8.0/10

A DIY project using a 60 GHz mmWave radar sensor successfully classifies common building materials (e.g., wood, drywall, concrete) and explores the feasibility of detecting asbestos in walls. The project is documented with detailed lessons learned, though it did not achieve funding for further development. This project highlights the potential of low-cost mmWave radar for non-destructive material identification, which could revolutionize building inspection and safety. If successful, it could enable affordable, portable asbestos detection, addressing a major health hazard in older buildings. The radar operates at 60 GHz and uses signal processing to generate spectrograms for material classification. The project did not specifically test asbestos detection, focusing instead on classifying common materials, which led to community skepticism about its practical feasibility for asbestos.

hackernews · GL26 · Jun 30, 17:29 · [Discussion](https://news.ycombinator.com/item?id=48736137)

**Background**: mmWave radar uses millimeter-wave frequencies (30-300 GHz) to detect objects and measure properties like dielectric constant, which vary by material. Asbestos detection typically requires lab analysis or specialized handheld devices; a radar-based approach could offer faster, non-invasive screening. The project is part of a broader trend of DIY radar systems for presence detection and imaging.

<details><summary>References</summary>
<ul>
<li><a href="https://sesamedisk.com/mmwave-radar-material-classification-industrial/">Millimeter-Wave Radar for Material - Sesame Disk</a></li>
<li><a href="https://wpnews.pro/news/i-built-a-mmwave-material-classification-radar">I built a mmWave material classification radar — Web Pulse</a></li>
<li><a href="https://calvin.me/diy-mmwave-presence-detectors/">DIY mmWave Presence Detectors – Calvin Bui</a></li>

</ul>
</details>

**Discussion**: Comments are mixed: some praise the technical documentation and lessons learned, while others question the feasibility of asbestos detection, noting that the prototype only classified common materials. One commenter suggests using the radar to find discontinuities rather than classify materials, which could be useful for general inspection.

**Tags**: `#mmWave radar`, `#material classification`, `#asbestos detection`, `#hardware hacking`, `#signal processing`

---

<a id="item-7"></a>
## [ZLUDA 6: Run Unmodified CUDA Apps on Non-Nvidia GPUs](https://vosen.github.io/ZLUDA/blog/zluda-update-q1q2-2026/) ⭐️ 8.0/10

ZLUDA 6 has been released, allowing unmodified CUDA applications to run on non-Nvidia GPUs, now as an open-source weekend project with new features including 32-bit PhysX support. This release expands GPU computing options by enabling CUDA software on AMD and other GPUs, potentially reducing vendor lock-in and benefiting users with non-Nvidia hardware, especially for legacy PhysX games and LLM inference. ZLUDA 6 adds 32-bit PhysX support, which is notable because Nvidia initially planned to remove it from RTX 50 series but later reinstated it after backlash. The project is now a weekend hobby, prioritizing entertaining features over commercial viability.

hackernews · Tiberium · Jun 30, 10:34 · [Discussion](https://news.ycombinator.com/item?id=48730713)

**Background**: ZLUDA is a translation layer that converts CUDA API calls into AMD's ROCm/HIP platform, enabling CUDA applications to run on AMD GPUs without code changes. Nvidia has previously banned the use of translation layers in its CUDA EULA, targeting projects like ZLUDA. PhysX is a physics engine used in games; 32-bit PhysX support is important for older titles.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/nvidias-physx-and-flow-go-open-source-running-legacy-physx-on-rtx-50-may-be-possible-using-wrappers">Nvidia's PhysX and Flow go open source — Running legacy PhysX on RTX 50 may be possible using wrappers | Tom's Hardware</a></li>

</ul>
</details>

**Discussion**: Commenters noted the shift to a weekend project and the amusing prioritization of entertainment. The 32-bit PhysX support was highlighted as particularly interesting given Nvidia's earlier plan to remove it. Users also inquired about LLM performance compared to Vulkan.

**Tags**: `#CUDA`, `#GPU computing`, `#open source`, `#translation layer`, `#PhysX`

---

<a id="item-8"></a>
## [Shot-scraper video records agent demos via Playwright](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 8.0/10

Simon Willison released shot-scraper 1.10 with a new 'shot-scraper video' command that accepts a storyboard.yml file and uses Playwright to record a video of a web application routine. The tool is designed to let coding agents produce visual proof of their work. This tool addresses a practical need in AI agent development by enabling agents to automatically produce demo videos, which helps developers verify that agents actually performed the intended tasks. It bridges the gap between agent execution and human review, potentially improving trust and debugging efficiency. The storyboard.yml file defines server startup, URL, viewport, cursor visibility, wait conditions, JavaScript overrides (e.g., clipboard mocking), and a sequence of scenes with actions like pause and click. The command supports --auth for authenticated sessions and --mp4 for output format.

rss · Simon Willison · Jun 30, 16:54

**Background**: Shot-scraper is a command-line tool for taking automated screenshots of websites, built on Playwright, a browser automation library. Playwright allows controlling Chromium, Firefox, and WebKit with a single API, commonly used for testing and scraping. The new video feature extends shot-scraper's capabilities from static screenshots to dynamic recordings.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/30/shot-scraper-video/">Have your agent record video demos of its work with shot-scraper video</a></li>
<li><a href="https://github.com/simonw/shot-scraper">GitHub - simonw/ shot - scraper : A command -line utility for taking...</a></li>
<li><a href="https://playwright.dev/">Fast and reliable end-to-end testing for modern web apps | Playwright</a></li>

</ul>
</details>

**Tags**: `#developer-tools`, `#AI-agents`, `#testing`, `#playwright`, `#video-recording`

---

<a id="item-9"></a>
## [Sonnet 5 and Fable 5 AI Models Announced](https://www.latent.space/p/ainews-sonnet-5-today-and-fable-5) ⭐️ 8.0/10

Latent Space reports that Sonnet 5 will be released today and Fable 5 tomorrow, indicating new versions of AI models are imminent. These releases suggest significant advancements in AI model capabilities, potentially impacting developers and researchers who rely on these models. The news does not specify the exact improvements or changes in Sonnet 5 and Fable 5, but the rapid succession of releases hints at competitive pressure in the AI model space.

rss · Latent Space · Jul 1, 03:01

**Background**: Sonnet and Fable are likely code names for AI models from a specific organization, possibly Anthropic or another AI lab. The '5' denotes a major version update, typically bringing performance improvements or new features.

**Tags**: `#AI`, `#machine learning`, `#model release`, `#news`

---

<a id="item-10"></a>
## [New attack bypasses AI browser guardrails with false arithmetic](https://arstechnica.com/security/2026/06/ai-browsers-can-be-lulled-into-a-dream-world-where-guardrails-no-longer-apply/) ⭐️ 8.0/10

A new attack demonstrates that telling an LLM a false arithmetic fact, such as 2+2=5, can cause it to ignore safety guardrails and follow forbidden instructions, posing a serious security risk to AI browsers. This attack highlights a fundamental vulnerability in LLM-based browsers, where simple input manipulation can bypass safety measures, potentially leading to harmful outputs or data breaches. It underscores the need for more robust guardrail designs before AI browsers become widely adopted. The attack works by presenting the LLM with a false arithmetic statement (e.g., 2+2=5) that contradicts its training data, creating a 'dream world' where guardrails no longer apply. This technique is distinct from traditional jailbreak methods and exploits the model's reliance on factual consistency.

rss · Ars Technica AI · Jun 30, 20:03

**Background**: LLM guardrails are safety mechanisms designed to prevent harmful, biased, or inappropriate outputs. However, they rely on pattern recognition and can be bypassed by carefully crafted inputs, as shown in recent research on evasion attacks. AI browsers integrate LLMs to assist with web tasks, making them a prime target for such exploits.

<details><summary>References</summary>
<ul>
<li><a href="https://mindgard.ai/resources/bypassing-llm-guardrails-character-and-aml-attacks-in-practice">Bypassing LLM guardrails: character and AML attacks in practice - Mindgard</a></li>
<li><a href="https://arxiv.org/abs/2504.11168">[2504.11168] Bypassing LLM Guardrails: An Empirical Analysis of Evasion Attacks against Prompt Injection and Jailbreak Detection Systems</a></li>
<li><a href="https://milvus.io/ai-quick-reference/can-llm-guardrails-be-bypassed-by-users">Can LLM guardrails be bypassed by users?</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#LLM`, `#guardrail bypass`, `#adversarial attack`, `#browser security`

---

<a id="item-11"></a>
## [audio.cpp Adds VibeVoice 1.5B, Achieves 4x Real-Time TTS](https://www.reddit.com/r/LocalLLaMA/comments/1uk7khq/audiocpp_vibevoice_15b_released_90min_podcast_in/) ⭐️ 8.0/10

The author of audio.cpp released support for Microsoft's VibeVoice 1.5B model, enabling 90-minute podcast generation in 22.95 minutes on an RTX 5090, which is 4.08x faster than real time and 2.86x faster than a Python baseline without quantization. This makes long-form multi-speaker TTS practical for local inference, reducing the need for cloud APIs and Python dependencies, and enabling applications like podcast generation, character chats, and narration on consumer hardware. The benchmark used 10 diffusion steps with no quantization, and the framework currently supports 16 out of 28 planned model families, with the rest running internally and being released gradually after testing.

reddit · r/LocalLLaMA · /u/Acceptable-Cycle4645 · Jul 1, 01:15

**Background**: audio.cpp is a pure C++ inference engine built on ggml, a tensor library for machine learning that enables large models on commodity hardware. VibeVoice is a Microsoft model combining a Qwen2.5-1.5B LLM with acoustic/semantic tokenizers and a diffusion decoder for long-form multi-speaker audio generation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/0xShug0/audio.cpp">GitHub - 0xShug0/ audio . cpp : An all-in-one, pure C++ inference engine...</a></li>
<li><a href="https://huggingface.co/microsoft/VibeVoice-1.5B">microsoft/VibeVoice-1.5B · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/GGML">GGML</a></li>

</ul>
</details>

**Discussion**: The Reddit thread shows active engagement with the author answering technical questions about GPU compatibility, VRAM usage, and future plans for CPU and Metal support. Users express interest in testing on other hardware and appreciate the focus on native local runtime.

**Tags**: `#TTS`, `#C++`, `#ggml`, `#local inference`, `#audio generation`

---

<a id="item-12"></a>
## [NVIDIA Releases Qwen3.6-27B-NVFP4 for Efficient Local Inference](https://www.reddit.com/r/LocalLLaMA/comments/1ujlltn/nvidiaqwen3627bnvfp4_just_dropped/) ⭐️ 8.0/10

NVIDIA has released Qwen3.6-27B-NVFP4, a 4-bit FP4 quantized version of the Qwen3.6-27B model, optimized for efficient local inference on consumer hardware. This release enables high-quality 27B parameter models to run locally on consumer GPUs with reduced memory and compute requirements, making advanced AI more accessible for personal and edge deployments. NVFP4 is a 4-bit floating-point quantization format that retains floating-point semantics with a shared exponent and compact mantissa, offering higher dynamic range than traditional INT4 quantization.

reddit · r/LocalLLaMA · /u/vanbukin · Jun 30, 10:39

**Background**: Quantization reduces model size and inference cost by representing weights and activations with fewer bits. FP4 is an ultra-low precision format that balances efficiency and accuracy, using blockwise microscaling and stochastic rounding to maintain model quality. NVIDIA's NVFP4 specifically leverages the E4M3 FP8 format variant to enable non-power-of-two scaling factors for more accurate tensor encoding.

<details><summary>References</summary>
<ul>
<li><a href="https://build.nvidia.com/spark/nvfp4-quantization">NVFP4 Quantization | DGX Spark</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision Inference | NVIDIA Technical Blog</a></li>
<li><a href="https://www.exxactcorp.com/blog/hpc/what-is-fp8-fp6-fp4">What is FP8, FP6, FP4? | Exxact Blog</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Quantization`, `#NVIDIA`, `#Local Inference`, `#Model Release`

---

<a id="item-13"></a>
## [Huawei Open-Sources OpenPangu-2.0-Flash MoE Model](https://www.reddit.com/r/LocalLLaMA/comments/1ujn5u3/huawei_opensources_openpangu20flash_92b_total6b/) ⭐️ 8.0/10

Huawei has open-sourced OpenPangu-2.0-Flash, a Mixture-of-Experts (MoE) model with 92 billion total parameters and 6 billion active parameters, supporting a 512K token context window. The company also announced a larger 505B total / 18B active flagship model, OpenPangu-2.0-Pro, to be released in July. This release marks a significant contribution to the open-source LLM ecosystem, especially from a major Chinese tech company amid geopolitical tensions. The MoE architecture and long 512K context window make it competitive with other leading open models, potentially accelerating adoption and innovation in long-context applications. The Flash version includes released weights, inference code, and training ops. The upcoming Pro model (505B total, 18B active) is expected to be the flagship. More open-source components are planned later this year.

reddit · r/LocalLLaMA · /u/soteko · Jun 30, 11:58

**Background**: Mixture of Experts (MoE) is an AI model architecture that uses multiple specialized submodels (experts) activated by a gating mechanism, enabling efficient scaling with fewer active parameters per inference. OpenPangu is Huawei's series of large language models, and this open-source release follows a trend of major players like DeepSeek and Alibaba releasing open-weight models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? | NVIDIA Glossary</a></li>
<li><a href="https://www.aimadetools.com/blog/openpangu-2-vs-qwen-3-7/">openPangu 2 . 0 vs Qwen 3.7: Huawei vs Alibaba in the Open -Source...</a></li>

</ul>
</details>

**Discussion**: Community comments on Reddit are generally positive, with users praising the long context and MoE efficiency, though some question the model's quality compared to established open models like Qwen or DeepSeek. There is also discussion about the geopolitical implications and the potential for Huawei to become a major open-source AI contributor.

**Tags**: `#LLM`, `#open-source`, `#MoE`, `#Huawei`, `#long-context`

---

<a id="item-14"></a>
## [PageStorm: A Model for Full-Book Creative Writing](https://www.reddit.com/r/LocalLLaMA/comments/1ujr69g/pagestorm_a_model_built_for_creative_book_writing/) ⭐️ 8.0/10

Pageshift Entertainment released PageStorm Research Preview, a model and dataset for single-turn full-book creative writing, along with a paper on arXiv. This is a significant step toward AI-assisted novel writing, enabling models to generate complete books with coherent plots and character development in a single pass. The model is single-turn only and cannot accept additional prompts after the initial one. The accompanying LongPage dataset provides hierarchical reasoning traces for training models on full-book writing.

reddit · r/LocalLLaMA · /u/XMasterDE · Jun 30, 14:43

**Background**: Traditional LLMs struggle with long-form creative writing due to context length limits and coherence issues. The LongPage dataset addresses this by providing structured reasoning traces from scene-level pacing to multi-arc character development, enabling models to plan and write entire novels.

<details><summary>References</summary>
<ul>
<li><a href="https://pageshift.ai/research/longpage">LongPage</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#creative writing`, `#dataset`, `#research`, `#AI`

---

<a id="item-15"></a>
## [Meta reuses old DDR4 memory in new DDR5 servers via custom CXL 2.0 chip](https://www.reddit.com/r/LocalLLaMA/comments/1ujzf35/meta_fights_soaring_hardware_costs_by_reusing_old/) ⭐️ 8.0/10

Meta has developed a custom CXL 2.0 ASIC called Vistara that allows legacy DDR4-2400 memory to be used alongside new DDR5-6400 in modern servers, reducing hardware costs for AI workloads. This innovation enables Meta to repurpose existing DDR4 memory inventory, significantly cutting capital expenditure on new memory for large-scale AI infrastructure. It also demonstrates a practical application of CXL technology to extend server memory capacity without requiring a full hardware refresh. The Vistara chip uses the CXL 2.0 protocol to attach DDR4 memory to DDR5-only servers, with Panmnesia providing an off-the-shelf CXL controller and switch that enables large memory pools without added latency. Meta's approach differs from typical CXL solutions that bundle DRAM with the controller and often lack DDR4 support.

reddit · r/LocalLLaMA · /u/pulse77 · Jun 30, 19:43

**Background**: CXL (Compute Express Link) is a high-bandwidth, low-latency interconnect protocol based on PCIe, designed for communication between CPUs, memory, and accelerators. DDR4 and DDR5 are different generations of DRAM with incompatible interfaces; DDR5 offers higher bandwidth and lower power but is more expensive. Meta's custom ASIC bridges this gap, allowing older, cheaper DDR4 memory to supplement newer DDR5 systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/dram/meta-fights-soaring-hardware-costs-by-reusing-old-ddr4-server-memory-in-new-ddr5-only-servers-custom-cxl-2-0-chip-marries-legacy-ddr4-2400-with-cutting-edge-ddr5-6400">Meta fights soaring hardware costs by reusing old DDR4 server memory in new DDR5-only servers — custom CXL 2.0 chip marries legacy DDR4-2400 with cutting-edge DDR5-6400 | Tom's Hardware</a></li>
<li><a href="https://www.theregister.com/systems/2026/06/29/zuck-saves-meta-bucks-by-reusing-memory-from-old-servers-with-a-custom-cxl-asic/5263483">Zuck saves Meta bucks by reusing memory from old servers with a custom CXL ASIC</a></li>
<li><a href="https://computeexpresslink.org/blog/animated-videos-illustrate-cxl-technology-and-cxl-2-0-key-features-2387/">Animated Videos Illustrate CXL ® Technology... - Compute Express Link</a></li>

</ul>
</details>

**Discussion**: Reddit commenters discussed the memory bandwidth trade-offs of mixing DDR4 with DDR5, noting that while capacity increases, the slower DDR4 may bottleneck performance. Some praised Meta's cost-saving ingenuity, while others questioned the long-term viability given DDR4's lower speed.

**Tags**: `#CXL`, `#memory`, `#AI infrastructure`, `#hardware`, `#Meta`

---