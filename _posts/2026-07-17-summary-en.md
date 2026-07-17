---
layout: default
title: "Horizon Summary: 2026-07-17 (EN)"
date: 2026-07-17
lang: en
---

> From 151 items, 15 important content pieces were selected

---

1. [Firefox Compiled to WebAssembly Runs Inside a Browser](#item-1) ⭐️ 9.0/10
2. [Thinking Machines Lab Releases Inkling, a 975B Open-Weights Model](#item-2) ⭐️ 9.0/10
3. [Kimi K3: Largest Open Model with Opus 4.8-Class Performance](#item-3) ⭐️ 9.0/10
4. [Ring-Zero Scales Zero RL to Trillion Parameters](#item-4) ⭐️ 9.0/10
5. [Open Interpreter Gains 661 Stars Daily as Coding Agent for Open Models](#item-5) ⭐️ 8.0/10
6. [Hermes Agent: Open-Source AI Agent That Learns and Grows](#item-6) ⭐️ 8.0/10
7. [Boogu-Image-0.1: Open-Source Multimodal Model Family](#item-7) ⭐️ 8.0/10
8. [GPT-5.6 Codex Bug Can Delete User Files](#item-8) ⭐️ 8.0/10
9. [Linus Torvalds Declares Linux Not Anti-AI](#item-9) ⭐️ 8.0/10
10. [Lila Sciences: Future Lab as Data Center](#item-10) ⭐️ 8.0/10
11. [EU Mandates Google to Share Search Data and Open AI on Android](#item-11) ⭐️ 8.0/10
12. [Hyundai Workers Strike Over Humanoid Robot Deployment Plan](#item-12) ⭐️ 8.0/10
13. [DFlash speeds up Qwen3.6-27B by 2.2x with no quality loss](#item-13) ⭐️ 8.0/10
14. [QLoRA default learning rate 2e-4 causes overfitting on small datasets](#item-14) ⭐️ 8.0/10
15. [ExTernD: Expanded-Rank Ternary Decomposition for LLM Quantization](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Firefox Compiled to WebAssembly Runs Inside a Browser](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter has compiled the full Firefox browser (Gecko engine) to WebAssembly, allowing it to run inside another browser tab. The project used an estimated $25,000 worth of AI tokens (Claude Opus and Fable) and is available on GitHub. This breakthrough demonstrates that even complex native applications like a full web browser can be ported to WebAssembly, opening up new possibilities for running legacy or sandboxed software in the browser. It also showcases the power of AI-assisted programming in tackling massive porting efforts. All network traffic is funneled through a WebSocket-based Wisp protocol via Puter's server, because WebAssembly code cannot open arbitrary network connections. The demo supports end-to-end encryption for HTTPS traffic, and the team had to scale servers to handle Hacker News traffic.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (Wasm) is a low-level binary instruction format that runs in modern web browsers at near-native speed. Traditionally, browsers run JavaScript, but Wasm allows running code compiled from languages like C++ in the browser. The Wisp protocol is a low-overhead protocol for proxying TCP and UDP sockets over a single WebSocket connection, enabling network access for Wasm modules.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.puter.com/labs/firefox-wasm/">Firefox in WebAssembly - developer.puter.com</a></li>
<li><a href="https://github.com/HeyPuter/firefox-wasm">HeyPuter/firefox-wasm: Firefox in WebAssembly - GitHub</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/ wisp - protocol : Wisp is a low-overhead...</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was highly positive, with many commenters impressed by the technical achievement and the use of AI to assist in the porting. Some raised concerns about the cost of proxying traffic and the reliance on Puter's servers, but the team addressed these by noting they had to scale up servers due to demand.

**Tags**: `#WebAssembly`, `#Firefox`, `#browser`, `#compilation`, `#Wisp`

---

<a id="item-2"></a>
## [Thinking Machines Lab Releases Inkling, a 975B Open-Weights Model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 9.0/10

Thinking Machines Lab, led by Mira Murati, released Inkling, an open-weights multimodal Mixture-of-Experts model with 975B total parameters and 41B active parameters, under the Apache-2.0 license. The model was trained on 45 trillion tokens of text, images, audio, and video. This release marks a significant addition to the US open-weights AI ecosystem, offering a competitive alternative to models from China and other open-weight contenders like NVIDIA Nemotron and Gemma 4. Its Apache-2.0 license and multimodal capabilities make it a strong base for fine-tuning and customization. The model card is notably sparse, with minimal training data documentation, and Thinking Machines Lab admits Inkling is not a frontier model but a strong base for fine-tuning via their Tinker platform. A smaller variant, Inkling-Small (276B total, 12B active), is promised but not yet released.

rss · Simon Willison · Jul 16, 15:35

**Background**: Mixture-of-Experts (MoE) is a neural network architecture that divides the model into multiple specialized 'expert' sub-networks, activating only a subset for each input, which reduces computational cost. Open-weights models release trained parameters publicly, allowing anyone to download, modify, and use them, but they may not include full training data or code. The Apache-2.0 license is a permissive open-source license that permits use, modification, and distribution without royalty concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-weights`, `#multimodal`, `#Mixture-of-Experts`, `#Mira Murati`

---

<a id="item-3"></a>
## [Kimi K3: Largest Open Model with Opus 4.8-Class Performance](https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest) ⭐️ 9.0/10

Moonshot AI released Kimi K3, a 2.8-trillion-parameter open-weight model with 50 billion active parameters, achieving performance comparable to Anthropic's Opus 4.8 while priced similarly to Sonnet 5 ($3/$15 per million tokens). As the largest open model ever released, Kimi K3 significantly lowers the cost of frontier-level AI, potentially accelerating commoditization of intelligence and pressuring proprietary model pricing. Kimi K3 uses a Mixture-of-Experts architecture with 2.8T total parameters and 50B active per token, supports a 1-million-token context window, and excels in coding, agentic tasks, long-horizon reasoning, and visual understanding.

rss · Latent Space · Jul 17, 01:46

**Background**: Open-weight models like Kimi K3 allow developers to download and fine-tune the model, unlike closed APIs. The model uses Kimi Delta Attention and Attention Residuals for efficiency. Opus 4.8 is Anthropic's top-tier model, while Sonnet 5 offers a more affordable price-performance point.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://www.marktechpost.com/2026/07/16/moonshot-ai-releases-kimi-k3-a-2-8-trillion-parameter-open-moe-model-with-kimi-delta-attention-and-1m-context/">Moonshot AI Releases Kimi K 3 : A 2 . 8 Trillion... - MarkTechPost</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-8">Introducing Claude Opus 4.8 \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the model's high cost for a Chinese open-weight model ($3/$15 per million tokens) but acknowledge its competitive performance. Some speculate that Chinese labs are commoditizing intelligence to drive hardware sales, while others note the significant investment required.

**Tags**: `#AI`, `#open-source`, `#large language model`, `#Kimi K3`, `#breakthrough`

---

<a id="item-4"></a>
## [Ring-Zero Scales Zero RL to Trillion Parameters](https://huggingface.co/papers/2607.12395) ⭐️ 9.0/10

Researchers present Ring-Zero, a stable pipeline for scaling zero reinforcement learning to 1-trillion-parameter models, demonstrating emergent reasoning behaviors like self-verification and parallel reasoning. This breakthrough validates scaling laws for zero RL at an unprecedented scale, showing that trillion-parameter models can develop advanced reasoning without human-annotated data, potentially transforming AI reasoning capabilities. The pipeline includes algorithmic optimizations like clipped importance sampling, training-inference ratio correction, and mixed-precision control. The resulting model, Ring-2.5-1T-Zero, achieves competitive performance on seven mathematical benchmarks.

huggingface_papers · Hugging Face Papers · Jul 16, 00:00

**Background**: Zero reinforcement learning (zero RL) trains models using verifiable rewards without human-annotated data, enabling chain-of-thought reasoning to emerge. Prior work was limited to small models due to computational constraints, leaving scaling behaviors unexplored.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2510.25528">Zero Reinforcement Learning Towards General Domains</a></li>
<li><a href="https://arxiv.org/abs/2503.18892">SimpleRL-Zoo: Investigating and Taming Zero Reinforcement Learning for ...</a></li>
<li><a href="https://arxiv.org/abs/1905.02363">[1905.02363] Dimension-Wise Importance Sampling Weight Clipping for Sample-Efficient Reinforcement Learning</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#scaling laws`, `#reasoning`, `#large language models`, `#AI research`

---

<a id="item-5"></a>
## [Open Interpreter Gains 661 Stars Daily as Coding Agent for Open Models](https://github.com/openinterpreter/openinterpreter) ⭐️ 8.0/10

Open Interpreter, a coding agent for open models like Kimi K3, has gained 661 stars in a single day, reaching over 66,000 total stars on GitHub. The project is written in Rust and focuses on enabling natural language code execution. This surge indicates strong community interest in AI-assisted development tools that work with open models, potentially lowering barriers for developers to leverage large language models for coding tasks. The use of Rust suggests a focus on performance and safety. Open Interpreter is a fork of OpenAI's Codex, optimized for low-cost models, and runs locally in the terminal. It can read files, edit code, run commands, and escalate actions beyond the sandbox only after user approval.

github_trending · GitHub Trending · Jul 17, 02:43

**Background**: Kimi K3 is an open model with 2.8 trillion parameters, released by Kimi, and is among the largest open models available. Open Interpreter provides a ChatGPT-like interface for executing code across multiple programming languages, acting as a coding agent that bridges natural language and code.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openinterpreter/openinterpreter">GitHub - openinterpreter/openinterpreter: A coding agent for low-cost models · GitHub</a></li>
<li><a href="https://www.openinterpreter.com/">Open Interpreter CLI: open source AI coding agent</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**Tags**: `#coding agent`, `#open models`, `#Rust`, `#AI-assisted development`, `#GitHub trending`

---

<a id="item-6"></a>
## [Hermes Agent: Open-Source AI Agent That Learns and Grows](https://github.com/NousResearch/hermes-agent) ⭐️ 8.0/10

NousResearch released Hermes Agent, an open-source Python AI agent that accumulates 588 stars in one day on GitHub, featuring a built-in learning loop that creates skills from experience and remembers across sessions. This project represents a shift toward autonomous, self-improving AI agents that operate across multiple platforms (CLI, messaging apps, voice), potentially reducing lock-in to single-vendor solutions and enabling long-running, personalized AI assistants. Hermes Agent supports Telegram, Discord, Slack, WhatsApp, Signal, and CLI from a single gateway, includes voice memo transcription, cross-platform conversation continuity, and agent-curated memory with periodic nudges.

github_trending · GitHub Trending · Jul 17, 02:43

**Background**: Hermes Agent is built by Nous Research, the lab behind the Hermes, Nomos, and Psyche model families. Unlike coding copilots tied to an IDE or chatbot wrappers around a single API, this agent is designed to live on your server, remember what it learns, and become more capable over time.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/nousresearch/hermes-agent">GitHub - NousResearch/hermes-agent: The agent that grows with you · GitHub</a></li>
<li><a href="https://hermes-agent.nousresearch.com/">Hermes Agent — The Agent That Grows With You</a></li>
<li><a href="https://hermes-agent.nousresearch.com/docs/">Hermes Agent Documentation | Hermes Agent</a></li>

</ul>
</details>

**Tags**: `#AI`, `#agent`, `#Python`, `#open-source`

---

<a id="item-7"></a>
## [Boogu-Image-0.1: Open-Source Multimodal Model Family](https://huggingface.co/papers/2607.13125) ⭐️ 8.0/10

Boogu-Image-0.1 is an open-source unified multimodal model family that achieves competitive performance in text-to-image generation, instruction-based editing, and bilingual text rendering, with variants including Base, Turbo, Edit, and Edit-Turbo. This work demonstrates that targeted improvements in data quality and training pipelines, along with agentic inference-time scaling, can substantially enhance performance even under constrained compute budgets, advancing open-source multimodal understanding and generation. The base model was trained on only 208.62 million unique images with a theoretical training cost of approximately $400K, yet it matches or surpasses other open-source models and approaches leading closed-source systems like Nano-Banana-Pro and GPT-Image-2.

huggingface_papers · Hugging Face Papers · Jul 16, 00:00

**Background**: Unified multimodal understanding and generation models aim to handle both image comprehension and creation in a single framework. Closed-source systems often achieve strong results through undisclosed system-level integrations, while open-source alternatives typically lag behind. Boogu-Image-0.1 addresses this gap by releasing weights, code, and recipes under Apache 2.0.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2604.16529">Scaling Test-Time Compute for Agentic Coding</a></li>
<li><a href="https://arxiv.org/abs/2604.16529">[2604.16529] Scaling Test-Time Compute for Agentic Coding</a></li>
<li><a href="https://arxiv.org/html/2602.12276">Agentic Test-Time Scaling for WebAgents</a></li>

</ul>
</details>

**Tags**: `#multimodal`, `#text-to-image`, `#open-source`, `#image generation`, `#AI`

---

<a id="item-8"></a>
## [GPT-5.6 Codex Bug Can Delete User Files](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

Thibault Sottiaux reported that GPT-5.6's Codex has a bug where it can delete user files when full access mode is enabled without sandboxing, due to a mistake in overriding the $HOME environment variable. This bug highlights significant safety risks in AI coding agents, especially for developers who grant full file system access without sandboxing, potentially leading to data loss or system damage. The bug occurs when Codex attempts to override $HOME to set a temporary directory but mistakenly deletes $HOME instead. The issue is most common when full access mode is enabled and sandboxing or auto-review is disabled.

rss · Simon Willison · Jul 16, 17:45

**Background**: Codex is an open-source coding agent from OpenAI that runs in the terminal, written in Rust. Full access mode gives the agent unrestricted file system permissions, which can be dangerous without sandboxing. The $HOME environment variable points to the user's home directory; overriding it incorrectly can lead to unintended deletions.

<details><summary>References</summary>
<ul>
<li><a href="https://deepnoodle.ai/blog/sandboxing-ai-coding-agents">The Deep Noodle Blog | Sandboxing AI Coding Agents</a></li>
<li><a href="https://www.theunwindai.com/p/sandboxing-ai-agents-100x-faster">Sandboxing AI Agents, 100 x Faster</a></li>
<li><a href="https://openai.com/index/introducing-the-codex-app/">Introducing the Codex app | OpenAI</a></li>

</ul>
</details>

**Tags**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`, `#bug`

---

<a id="item-9"></a>
## [Linus Torvalds Declares Linux Not Anti-AI](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linus Torvalds, the creator and top maintainer of Linux, publicly stated that Linux is not an anti-AI project and that AI is a clearly useful tool, inviting dissenters to fork or leave. This authoritative endorsement from the top Linux maintainer could influence the open-source community's stance on AI tools, potentially accelerating AI adoption in Linux development and related projects. Torvalds made the statement on the Linux Media Mailing List, emphasizing that AI's usefulness is no longer in question, though other questions like its economic impact remain.

rss · Simon Willison · Jul 16, 13:26

**Background**: Linus Torvalds is the creator and longtime maintainer of the Linux kernel, the core of the Linux operating system. The open-source community has debated the use of AI tools, with some advocating for bans due to concerns about ethics, copyright, or environmental impact.

**Tags**: `#Linux`, `#AI`, `#Open Source`, `#Linus Torvalds`

---

<a id="item-10"></a>
## [Lila Sciences: Future Lab as Data Center](https://www.latent.space/p/the-lab-of-the-future-should-feel) ⭐️ 8.0/10

Lila Sciences proposes transforming scientific laboratories into data centers, using robotics and AI to generate vast amounts of training data from experiments. This approach treats science as the last untapped source of high-quality training data for AI models. This paradigm shift could dramatically accelerate scientific discovery by automating data generation and enabling AI to learn directly from experiments. It may reduce the reliance on internet-sourced data, which is often noisy and limited, and unlock new breakthroughs in fields like chemistry and materials science. Lila Sciences is building an autonomous lab platform that integrates robotics and AI to conduct experiments and collect data at scale. The company aims to create a 'scientific superintelligence' that can generate hypotheses, run experiments, and analyze results without human intervention.

rss · Latent Space · Jul 16, 13:30

**Background**: Traditional AI training relies heavily on data scraped from the internet, which can be noisy and biased. In contrast, scientific experiments produce structured, high-quality data that is ideal for training AI models. Lila Sciences envisions a future where labs operate like automated factories, continuously generating experimental data to feed AI systems, similar to how data centers power cloud computing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lila.ai/">LILA | Scientific Superintelligence</a></li>
<li><a href="https://www.linkedin.com/company/lila-sciences">Lila Sciences | LinkedIn</a></li>
<li><a href="https://www.science.org/doi/10.1126/scirobotics.adm6991">Transforming science labs into automated factories of discovery | Science Robotics</a></li>

</ul>
</details>

**Tags**: `#AI`, `#scientific discovery`, `#robotics`, `#data generation`, `#lab automation`

---

<a id="item-11"></a>
## [EU Mandates Google to Share Search Data and Open AI on Android](https://arstechnica.com/gadgets/2026/07/its-official-eu-will-force-google-to-share-search-data-and-open-up-ai-on-android/) ⭐️ 8.0/10

The European Union has officially mandated Google to share its search data with rivals and open up AI capabilities on Android under the Digital Markets Act, citing competition concerns. This landmark regulation could reshape the digital market by increasing competition, potentially leading to more innovation and consumer choice, while Google warns it may compromise user privacy and security. The mandate requires Google to provide third-party search engines access to its search data and allow alternative AI services on Android devices, with non-compliance risking fines up to 10% of global turnover.

rss · Ars Technica AI · Jul 16, 20:41

**Background**: The Digital Markets Act (DMA) is an EU regulation that targets large digital platforms designated as 'gatekeepers' to ensure fair competition. It entered into force in November 2022 and became applicable in May 2023, with obligations including data sharing and interoperability. Google, as a gatekeeper, must comply with these rules to prevent anti-competitive practices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/EU_Digital_Markets_Act">EU Digital Markets Act</a></li>
<li><a href="https://www.nytimes.com/2025/09/02/technology/google-search-antitrust-decision.html">Google Must Share Search Data With Rivals, Judge Rules in Antitrust...</a></li>
<li><a href="https://ppc.land/google-ordered-to-share-glue-data-system-in-landmark-antitrust-ruling/">Google ordered to share Glue data system in landmark antitrust ruling</a></li>

</ul>
</details>

**Tags**: `#EU regulation`, `#Google`, `#Android`, `#AI`, `#privacy`

---

<a id="item-12"></a>
## [Hyundai Workers Strike Over Humanoid Robot Deployment Plan](https://arstechnica.com/ai/2026/07/fear-of-humanoid-robots-spurs-human-workers-to-strike-at-hyundai-auto-factory/) ⭐️ 8.0/10

Hyundai's plan to deploy 25,000 Boston Dynamics Atlas humanoid robots in its US factories by 2028 has triggered a strike by human workers who fear job displacement. This strike highlights growing tensions between automation and labor, potentially setting a precedent for how humanoid robot adoption is negotiated in manufacturing industries worldwide. The Atlas robot, developed by Boston Dynamics (a Hyundai subsidiary), is designed for industrial tasks like material handling and parts sequencing, with deployment slated to begin in US factories in 2028.

rss · Ars Technica AI · Jul 16, 20:09

**Background**: Humanoid robots like Atlas are bipedal machines designed to work in human environments. Hyundai acquired Boston Dynamics in 2020 and has been integrating Atlas into its manufacturing plans. The strike reflects broader concerns about automation displacing workers in the automotive industry.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Atlas_(robot)">Atlas ( robot ) - Wikipedia</a></li>
<li><a href="https://bostondynamics.com/products/atlas/">Atlas Humanoid Robot | Boston Dynamics</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lRd3VXa0VCR2JqdllkNnJHOXVTZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en">Google News - Hyundai Atlas robot at CES 2026 - Overview</a></li>

</ul>
</details>

**Tags**: `#humanoid robots`, `#labor relations`, `#automation`, `#Hyundai`, `#AI in manufacturing`

---

<a id="item-13"></a>
## [DFlash speeds up Qwen3.6-27B by 2.2x with no quality loss](https://www.reddit.com/r/LocalLLaMA/comments/1uyay0w/dflash_makes_qwen36_27b_22x_faster_with_no/) ⭐️ 8.0/10

A new speculative decoding technique called DFlash achieves 2.2x faster inference on Qwen3.6-27B for structured tasks like coding and JSON generation, while maintaining identical output quality compared to the baseline. This breakthrough significantly reduces inference latency for structured tasks, making local LLM deployment more practical for coding and data processing, and provides a clear trade-off analysis against Multi-Token Prediction (MTP) for different use cases. DFlash drafts 15 tokens in parallel using a lightweight block diffusion model, achieving up to 152 tok/s (3.4x) on JSON tasks, but can drop below baseline on creative text (42 vs 44 tok/s) due to low acceptance rate.

reddit · r/LocalLLaMA · /u/ElmBark · Jul 16, 18:22

**Background**: Speculative decoding accelerates LLM inference by using a small draft model to propose multiple tokens, which a larger target model then verifies in parallel. DFlash is a novel framework that employs a block diffusion model for drafting, while MTP (Multi-Token Prediction) uses the same model to predict multiple tokens at once. Both techniques aim to reduce latency without sacrificing output quality.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2602.06036">[2602.06036] DFlash: Block Diffusion for Flash Speculative Decoding</a></li>
<li><a href="https://github.com/z-lab/dflash">GitHub - z-lab/dflash: DFlash: Block Diffusion for Flash Speculative Decoding · GitHub</a></li>
<li><a href="https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/">The next generation of speculative decoding: DFlash and Spec V2 - LMSYS Org</a></li>

</ul>
</details>

**Tags**: `#speculative decoding`, `#inference optimization`, `#LLM inference`, `#Qwen`, `#local LLM`

---

<a id="item-14"></a>
## [QLoRA default learning rate 2e-4 causes overfitting on small datasets](https://www.reddit.com/r/MachineLearning/comments/1uy1z8b/the_qlora_2e4_default_is_wrong_under_10k_samples/) ⭐️ 8.0/10

A Reddit user discovered that the widely recommended QLoRA learning rate of 2e-4 leads to overfitting on datasets with fewer than 10,000 samples, and reducing it to 1e-4 with more epochs significantly improves evaluation performance. This finding challenges a default setting used in countless QLoRA fine-tuning tutorials and tools, potentially saving practitioners weeks of wasted effort on small datasets and improving model quality. The user reports that with 2e-4, the model overfits within the first epoch, while dropping to 1e-4 and increasing epochs from 3 to 5 produced the best results on datasets under 10k samples. They suggest tuning the learning rate based on dataset size: above 30k samples, 2e-4 is likely fine; under 10k, start at 1e-4 or lower.

reddit · r/MachineLearning · /u/Pretty-Ad774 · Jul 16, 12:50

**Background**: QLoRA is a parameter-efficient fine-tuning method that combines quantization and Low-Rank Adaptation (LoRA) to fine-tune large language models on consumer hardware. The default learning rate of 2e-4 originates from the Alpaca dataset (52k samples) and is widely copied in tutorials and code examples without adjustment for smaller datasets.

<details><summary>References</summary>
<ul>
<li><a href="https://lightning.ai/pages/community/lora-insights/">Finetuning LLMs with LoRA and QLoRA : Insights from... - Lightning AI</a></li>
<li><a href="https://github.com/artidoro/qlora">GitHub - artidoro/qlora: QLoRA: Efficient Finetuning of Quantized LLMs · GitHub</a></li>
<li><a href="https://arxiv.org/pdf/2305.14314">QLORA: Efficient Finetuning of Quantized LLMs Tim Dettmers∗ Artidoro Pagnoni∗</a></li>

</ul>
</details>

**Discussion**: The post received strong community validation with high upvotes and substantive discussion. Many users shared similar experiences of overfitting with 2e-4 on small datasets, while others noted that learning rate schedulers or warmup steps can mitigate the issue. Some debated the optimal learning rate range, with suggestions from 1e-5 to 5e-5 for very small datasets.

**Tags**: `#QLoRA`, `#fine-tuning`, `#learning rate`, `#overfitting`, `#LLM`

---

<a id="item-15"></a>
## [ExTernD: Expanded-Rank Ternary Decomposition for LLM Quantization](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 8.0/10

ExTernD proposes a post-training quantization method that decomposes a weight matrix into two ternary matrices and a diagonal scaling matrix, allowing the inner rank to be arbitrarily large to overcome accuracy limitations of fixed-size ternary quantization. This approach enables ternary quantization of LLMs to achieve accuracy close to higher-bit quantization while requiring only slightly more VRAM than existing methods, potentially making large models more accessible on consumer hardware. The method is validated on the arXiv paper (2607.13511) and claims that the expanded rank does not need to be very large to achieve high accuracy, with only a modest increase in VRAM compared to standard quantization.

reddit · r/MachineLearning · /u/LMTLS5 · Jul 16, 13:31

**Background**: Post-training quantization (PTQ) reduces model size and speeds up inference by converting weights to lower precision without retraining. Ternary quantization maps weights to values in {-α, 0, +α}, typically using 2 bits per weight, but fixed-size ternary matrices often suffer from accuracy loss. ExTernD addresses this by decomposing the matrix to increase representational capacity.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1612.01064">[1612.01064] Trained Ternary Quantization</a></li>
<li><a href="https://www.emergentmind.com/topics/ternary-quantization">Ternary Quantization in Neural Networks</a></li>
<li><a href="https://apxml.com/courses/practical-llm-quantization/chapter-2-post-training-quantization-ptq">Post - Training Quantization (PTQ) for LLMs</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#quantization`, `#ternary`, `#model compression`, `#PTQ`

---