---
layout: default
title: "Horizon Summary: 2026-06-15 (EN)"
date: 2026-06-15
lang: en
---

> From 138 items, 15 important content pieces were selected

---

1. [NVIDIA SkillSpector: Security Scanner for AI Agent Skills](#item-1) ⭐️ 8.0/10
2. [LMCache: Fastest KV Cache Layer for LLM Inference](#item-2) ⭐️ 8.0/10
3. [EvoArena & EvoMem: Benchmark and Memory for Dynamic LLM Agents](#item-3) ⭐️ 8.0/10
4. [MiniMax Sparse Attention Boosts Long-Context LLM Efficiency](#item-4) ⭐️ 8.0/10
5. [Yserver: A Modern X11 Server Written in Rust](#item-5) ⭐️ 8.0/10
6. [Atlantic cold blob hints at AMOC collapse risk](#item-6) ⭐️ 8.0/10
7. [Don't Trust Large Context Windows](#item-7) ⭐️ 8.0/10
8. [Why AI hasn’t replaced software engineers, and won’t](#item-8) ⭐️ 8.0/10
9. [Entering the AGI Era of AI Governance](#item-9) ⭐️ 8.0/10
10. [OpenAI Launches Partner Network with $150M Investment](#item-10) ⭐️ 8.0/10
11. [Xiaomi MiMo V2.5 hits 1000-3000 tps with DFlash and persistent kernel](#item-11) ⭐️ 8.0/10
12. [EAGLE speculative decoding merged into llama.cpp](#item-12) ⭐️ 8.0/10
13. [Real-Time Local Voice Chatbot with Qwen3.5-397B](#item-13) ⭐️ 8.0/10
14. [Running DeepSeek V4 Flash on M3 Max Mac with SSD Streaming](#item-14) ⭐️ 8.0/10
15. [Dual DGX Sparks Run DeepSeek V4 Flash at 350 tk/s](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [NVIDIA SkillSpector: Security Scanner for AI Agent Skills](https://github.com/NVIDIA/SkillSpector) ⭐️ 8.0/10

NVIDIA has released SkillSpector, an open-source security scanner for AI agent skills that detects vulnerabilities, malicious patterns, and security risks. The tool is now available on GitHub and has gained over 964 stars in a single day. As AI agents become more autonomous, securing their skills is critical to prevent attacks like prompt injection and data exfiltration. SkillSpector fills a key gap in the AI security ecosystem, especially with NVIDIA's backing and integration into their verified skills pipeline. SkillSpector is written in Python and performs static analysis on agent skill definitions, detecting over 25 threat types including command injection, credential theft, and supply chain risks. It is used by NVIDIA as part of their publication validation pipeline before skills enter the NVIDIA Skills catalog.

github_trending · GitHub Trending · Jun 15, 01:01

**Background**: AI agent skills are modular capabilities that extend an agent's functionality, often defined as prompts or scripts. However, these skills can contain malicious code or vulnerabilities that compromise the agent's security. SkillSpector addresses this by scanning skills before installation, similar to how antivirus software scans files.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/nvidia/skillspector">GitHub - NVIDIA/SkillSpector: Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, and security risks. · GitHub</a></li>
<li><a href="https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/">NVIDIA-Verified Agent Skills Provide Capability Governance for AI Agents | NVIDIA Technical Blog</a></li>
<li><a href="https://docs.nvidia.com/skills/scanning-agent-skills">Scan Agent Skills Before Installation | NVIDIA Skill Documentation</a></li>

</ul>
</details>

**Tags**: `#AI Security`, `#Vulnerability Detection`, `#Python`, `#AI Agents`, `#NVIDIA`

---

<a id="item-2"></a>
## [LMCache: Fastest KV Cache Layer for LLM Inference](https://github.com/LMCache/LMCache) ⭐️ 8.0/10

LMCache, a high-performance KV cache layer for LLMs, has gained 248 stars on GitHub today, reaching 9048 total stars, highlighting its growing popularity for accelerating LLM inference by reducing memory overhead. KV cache is a critical bottleneck in LLM inference, and LMCache's optimized caching layer can significantly reduce latency and memory usage, enabling faster and more cost-effective deployment of large language models in production. LMCache is written in Python and supports integration with popular LLM frameworks; it focuses on reducing memory overhead during inference by efficiently storing and reusing key-value computations.

github_trending · GitHub Trending · Jun 15, 01:02

**Background**: In LLM inference, the key-value (KV) cache stores intermediate attention computations to avoid redundant calculations, which is essential for efficient autoregressive generation. However, the KV cache can grow large, consuming significant GPU memory. LMCache addresses this by providing a fast, memory-efficient caching layer that can be plugged into existing LLM serving systems.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/lmcache/lmcache">GitHub - LMCache/LMCache: LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub</a></li>
<li><a href="https://lmcache.ai/">LMCache</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#KV Cache`, `#Inference Optimization`, `#Python`, `#Machine Learning`

---

<a id="item-3"></a>
## [EvoArena & EvoMem: Benchmark and Memory for Dynamic LLM Agents](https://huggingface.co/papers/2606.13681) ⭐️ 8.0/10

Researchers introduced EvoArena, a benchmark suite modeling progressive environment changes across terminal, software, and social domains, and EvoMem, a patch-based memory paradigm that records structured update histories to help LLM agents reason about environmental evolution. Current LLM agents struggle in dynamic environments, achieving only 39.6% average accuracy on EvoArena; EvoMem improves performance by 1.5% on EvoArena and also boosts standard benchmarks GAIA and LoCoMo by 6.1% and 4.8%, highlighting the need for evolution-aware evaluation and memory. EvoMem is a patch-based memory paradigm that stores memory as structured update histories, enabling agents to reason about environmental changes through memory evolution. It also improves chain-level accuracy by 3.7% on EvoArena, where success requires completing consecutive related subtasks.

huggingface_papers · Hugging Face Papers · Jun 12, 00:00

**Background**: Most LLM agent benchmarks assume static environments, but real-world deployment is dynamic, requiring agents to adapt to changing conditions. EvoArena fills this gap by modeling progressive updates across domains. EvoMem introduces a structured memory approach that tracks how the environment evolves, unlike traditional flat memory.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/papers/2606.13681">EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic ...</a></li>
<li><a href="https://arxiv.org/html/2606.13681">EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic ...</a></li>
<li><a href="https://arxiv.org/pdf/2606.13681">EvoArena: Tracking Memory Evolution for Robust LLM Agents in...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#benchmark`, `#memory evolution`, `#dynamic environments`, `#AI research`

---

<a id="item-4"></a>
## [MiniMax Sparse Attention Boosts Long-Context LLM Efficiency](https://huggingface.co/papers/2606.13392) ⭐️ 8.0/10

MiniMax released a new sparse attention mechanism called MiniMax Sparse Attention (MSA) that uses blockwise sparsity and optimized GPU kernels to achieve 14.2x prefill and 7.6x decoding speedups on H800 GPUs for a 109B-parameter multimodal model at 1M context length. Ultra-long-context capabilities are critical for agentic workflows and code reasoning, but quadratic attention costs limit deployment. MSA provides a practical, hardware-aligned solution that significantly reduces compute while maintaining model quality, enabling more efficient long-context LLM inference. MSA builds on Grouped Query Attention (GQA) with a lightweight Index Branch that selects Top-k key-value blocks per group, and a Main Branch that performs exact block-sparse attention. The co-designed GPU kernel uses exp-free Top-k selection and KV-outer sparse attention to improve tensor-core utilization.

huggingface_papers · Hugging Face Papers · Jun 12, 00:00

**Background**: Standard softmax attention has quadratic complexity with respect to sequence length, making it infeasible for very long contexts. Sparse attention methods reduce this cost by attending only to a subset of tokens. Grouped Query Attention (GQA) groups query heads to reduce memory and computation, and blockwise sparse attention further improves efficiency by operating on blocks of tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.13392">[2606.13392] MiniMax Sparse Attention</a></li>
<li><a href="https://friendli.ai/blog/gqa-vs-mha">Grouped Query Attention ( GQA ) vs. Multi Head Attention ...</a></li>
<li><a href="https://www.emergentmind.com/topics/blockwise-sparse-attention-mechanisms">Blockwise Sparse Attention Mechanisms</a></li>

</ul>
</details>

**Tags**: `#attention mechanism`, `#LLM`, `#efficiency`, `#sparse attention`, `#long context`

---

<a id="item-5"></a>
## [Yserver: A Modern X11 Server Written in Rust](https://github.com/joske/yserver) ⭐️ 8.0/10

Yserver is a new X11 server written in Rust that can already run real window managers like XFCE4, though it lacks multi-screen support and compositor compatibility. This project demonstrates that a modern, memory-safe X11 server is feasible, potentially improving security and performance on Linux desktops. It also revives interest in X11 alternatives beyond Wayland. Yserver drops legacy baggage like multiple screens, which some users criticize as essential for multi-monitor setups. It currently works with XFCE4 when compositing is disabled, but fails with LightDM.

hackernews · Venn1 · Jun 14, 19:10 · [Discussion](https://news.ycombinator.com/item?id=48531394)

**Background**: The X Window System (X11) is a windowing system for Unix-like operating systems, first released in 1984. The reference implementation, X.Org Server, is written in C and has accumulated decades of legacy code. Rust is a modern systems programming language that emphasizes memory safety and concurrency without a garbage collector.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/X11_server">X11 server</a></li>
<li><a href="https://en.wikipedia.org/wiki/X_Window_System">X Window System - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust ( programming language ) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters are impressed that Yserver can run real window managers, but many express concern over the lack of multi-screen support, calling it essential. Some note the historical Y Window System and suggest that Yserver's timing is ironic, arriving after Wayland has already become dominant.

**Tags**: `#Rust`, `#X11`, `#Linux Desktop`, `#Window System`

---

<a id="item-6"></a>
## [Atlantic cold blob hints at AMOC collapse risk](https://www.cnn.com/2026/06/12/climate/cold-blob-atlantic-amoc-ocean-circulation) ⭐️ 8.0/10

Researchers have identified a persistent cold blob in the North Atlantic, just south of Greenland and Iceland, which they attribute to a weakening of the Atlantic Meridional Overturning Circulation (AMOC). This finding suggests the AMOC may be approaching a critical tipping point. An AMOC collapse would trigger severe climate impacts, including substantial cooling in Europe, disruption of rainfall patterns in the Amazon, and acceleration of global warming. This underscores the urgency of addressing climate change to avoid crossing irreversible tipping points. The cold blob is caused by freshwater from melting Greenland ice sheets disrupting the sinking of dense, salty water that drives the AMOC. A 2024 study in Science Advances found that an AMOC collapse could cause the Amazon's dry and wet seasons to reverse.

hackernews · tambourine_man · Jun 14, 14:40 · [Discussion](https://news.ycombinator.com/item?id=48527658)

**Background**: The Atlantic Meridional Overturning Circulation (AMOC) is a major ocean current system that transports warm water northward and cold water southward, playing a key role in regulating global climate. A tipping point is a critical threshold beyond which a system undergoes large, often irreversible changes. Past AMOC shutdowns have occurred during the last ice age due to freshwater influx from melting ice sheets.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Atlantic_meridional_overturning_circulation">Atlantic meridional overturning circulation - Wikipedia</a></li>
<li><a href="https://interactive.carbonbrief.org/amoc-explainer/index.html">AMOC: Is global warming tipping key Atlantic ocean currents towards ‘collapse’?</a></li>
<li><a href="https://climate.mit.edu/ask-mit/what-would-happen-if-atlantic-meridional-overturning-circulation-amoc-collapses-how-likely">What would happen if the Atlantic Meridional Overturning Circulation (AMOC) collapses? How likely is it? | MIT Climate Portal</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern about the slow response to climate change, with some drawing parallels to science fiction scenarios. Others noted that the cold blob's location matches earlier predictions about AMOC weakening, and debated whether it is too late to prevent worst-case outcomes.

**Tags**: `#climate change`, `#AMOC`, `#ocean circulation`, `#global warming`, `#tipping point`

---

<a id="item-7"></a>
## [Don't Trust Large Context Windows](https://garrit.xyz/posts/2026-05-06-dont-trust-large-context-windows) ⭐️ 8.0/10

A blog post argues that large context windows in LLMs degrade performance and reliability, urging caution despite vendor claims. This matters because many users rely on large context windows for complex tasks, and the degradation can lead to unreliable outputs, affecting productivity and trust in AI systems. The author reports that performance degrades significantly beyond 100k tokens, with models losing focus and making errors. Some commenters note that Opus handles up to 500k tokens well, but others agree that irrelevant context harms performance.

hackernews · computersuck · Jun 14, 06:07 · [Discussion](https://news.ycombinator.com/item?id=48524620)

**Background**: Large context windows allow LLMs to process more input at once, but research shows that models struggle to maintain accuracy as context grows, often suffering from 'lost in the middle' effects. This is a known limitation despite marketing claims.

<details><summary>References</summary>
<ul>
<li><a href="https://demiliani.com/2025/11/02/understanding-llm-performance-degradation-a-deep-dive-into-context-window-limits/">Understanding LLM performance degradation: a deep dive into Context Window limits – Stefano Demiliani</a></li>
<li><a href="https://eval.16x.engineer/blog/llm-context-management-guide">LLM Context Management: How to Improve Performance and Lower Costs</a></li>
<li><a href="https://towardsdatascience.com/your-1m-context-window-llm-is-less-powerful-than-you-think/">Your 1M+ Context Window LLM Is Less Powerful Than You Think | Towards Data Science</a></li>

</ul>
</details>

**Discussion**: Commenters share mixed experiences: some find workarounds like recursive agent loops to avoid context bloat, while others report good results with Opus up to 800k tokens. There is agreement that irrelevant context harms performance, and memory systems are often counterproductive.

**Tags**: `#LLMs`, `#context windows`, `#AI reliability`, `#practical AI`

---

<a id="item-8"></a>
## [Why AI hasn’t replaced software engineers, and won’t](https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/#atom-everything) ⭐️ 8.0/10

Arvind Narayanan and Sayash Kapoor published an essay arguing that evidence does not support the narrative that AI will cause mass layoffs in software engineering, citing New York WARN Act data showing zero AI-related layoffs in the first year. This essay challenges the prevailing AI job displacement narrative with data and qualitative analysis, suggesting that even in a field uniquely suited to AI disruption, the core bottlenecks—deciding what to build, verifying output, and deep human understanding—remain resistant to automation. The authors identify three real bottlenecks in software engineering: deciding and specifying what to build, verifying and being accountable for what is delivered, and the deep human understanding of the codebase, business, and environment. They note that AI speeds up typing code but not these higher-level tasks.

rss · Simon Willison · Jun 14, 23:54

**Background**: The Worker Adjustment and Retraining Notification (WARN) Act requires employers with 100 or more employees to provide 60 days advance notice of mass layoffs. In March 2025, New York added an AI disclosure checkbox to WARN filings; in the first full year, not a single company checked it. Arvind Narayanan and Sayash Kapoor are the authors of the book "AI Snake Oil," which critiques inflated AI promises.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_Snake_Oil">AI Snake Oil - Wikipedia</a></li>
<li><a href="https://engineering.princeton.edu/news/2025/01/13/ai-snake-oil-conversation-princeton-ai-experts-arvind-narayanan-and-sayash-kapoor">‘AI Snake Oil’: A conversation with Princeton AI experts Arvind Narayanan and Sayash Kapoor - Princeton Engineering</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software engineering`, `#job displacement`, `#labor economics`

---

<a id="item-9"></a>
## [Entering the AGI Era of AI Governance](https://www.interconnects.ai/p/welcome-to-the-agi-era-of-ai-governance) ⭐️ 8.0/10

The article argues that we have entered the AGI era of AI governance, characterized by irreversible decisions that we were unprepared for. This shift signifies that current AI governance decisions have long-lasting consequences, requiring urgent and careful consideration from policymakers and the public. The author describes the situation as a 'one-way door,' emphasizing that once decisions are made, they cannot be easily reversed. The piece highlights the lack of preparedness for this new era.

rss · Interconnects · Jun 14, 17:43

**Background**: AGI (Artificial General Intelligence) refers to AI systems that can perform any intellectual task that a human can. AI governance involves creating policies and frameworks to manage the development and deployment of AI technologies. The article suggests that recent advances in AI have pushed us into an era where governance decisions carry unprecedented weight.

**Tags**: `#AI governance`, `#AGI`, `#AI policy`, `#technology ethics`

---

<a id="item-10"></a>
## [OpenAI Launches Partner Network with $150M Investment](https://openai.com/index/introducing-openai-partner-network) ⭐️ 8.0/10

OpenAI has announced the launch of the OpenAI Partner Network, a new program backed by a $150 million investment to help global partners accelerate enterprise AI adoption, deployment, and transformation. This initiative signals a strategic shift for OpenAI to deepen its enterprise footprint, potentially accelerating AI integration across industries and creating a robust ecosystem of service providers. The $150 million investment will be used to support partners with resources, training, and go-to-market strategies. The network aims to streamline the deployment of OpenAI's technologies in enterprise environments.

rss · OpenAI Blog · Jun 14, 17:00

**Background**: Enterprise AI adoption often requires specialized expertise and integration support. By creating a formal partner network, OpenAI follows a model common in enterprise software (e.g., Salesforce, AWS) to scale adoption through third-party consultants, system integrators, and resellers.

**Tags**: `#OpenAI`, `#Enterprise AI`, `#AI Adoption`, `#Partnerships`, `#Investment`

---

<a id="item-11"></a>
## [Xiaomi MiMo V2.5 hits 1000-3000 tps with DFlash and persistent kernel](https://www.reddit.com/r/LocalLLaMA/comments/1u5jtr8/xiaomi_is_now_serving_mimo_v25_at_10003000tps/) ⭐️ 8.0/10

Xiaomi announced that its MiMo V2.5 model is now being served at 1000-3000 tokens per second using DFlash and a persistent kernel, and the DFlash model has been released with an open-source release promised soon. This performance claim is significant because it suggests a major leap in LLM inference speed, potentially enabling real-time applications and reducing serving costs, which could influence the broader AI serving ecosystem. The DFlash model is available on Hugging Face, and the persistent kernel technique compiles entire LLM inference into a single fused GPU kernel, eliminating kernel launch overhead. The open-source release is promised but not yet available.

reddit · r/LocalLLaMA · /u/Dany0 · Jun 14, 12:26

**Background**: DFlash is an inference acceleration method that uses hidden states from the target model as input features to bridge the quality of autoregressive decoding with the speed of diffusion LLMs, achieving up to 3x faster inference. Persistent kernel (e.g., Mirage Persistent Kernel) compiles LLM inference into a single megakernel, reducing latency by eliminating per-operator kernel launches and overlapping computation with data movement.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.5">XiaomiMiMo/MiMo-V2.5 - Hugging Face</a></li>
<li><a href="https://docs.vllm.ai/projects/speculators/en/latest/user_guide/algorithms/dflash/">Dflash - Speculators Docs</a></li>
<li><a href="https://github.com/mirage-project/mirage">GitHub - mirage-project/mirage: Mirage Persistent Kernel : Compiling...</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#open-source`, `#performance optimization`, `#Xiaomi`, `#AI serving`

---

<a id="item-12"></a>
## [EAGLE speculative decoding merged into llama.cpp](https://www.reddit.com/r/LocalLLaMA/comments/1u5z4j0/eagle_support_merged_into_llamacpp/) ⭐️ 8.0/10

EAGLE (Extrapolation Algorithm for Greater Language-model Efficiency) speculative decoding support has been merged into the llama.cpp repository, enabling faster LLM inference on local hardware. This integration significantly boosts inference speed for users running LLMs locally via llama.cpp, making advanced speculative decoding accessible to a broad community without sacrificing output quality. EAGLE uses a small draft head trained on the target model's hidden states to predict multiple future tokens, achieving 2-3x speedups over standard autoregressive decoding.

reddit · r/LocalLLaMA · /u/Diablo-D3 · Jun 14, 22:45

**Background**: Speculative decoding is an inference-time optimization that speeds up LLM token generation by using a smaller draft model to propose tokens, which are then verified by the target model. EAGLE is a specific speculative decoding framework that eliminates the need for a separate draft model by leveraging the target model's own hidden states.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/EAGLE_speculative_decoding">EAGLE (speculative decoding)</a></li>
<li><a href="https://arxiv.org/abs/2401.15077">EAGLE : Speculative Sampling Requires Rethinking Feature Uncertainty</a></li>
<li><a href="https://bentoml.com/llm/inference-optimization/speculative-decoding">Speculative decoding | LLM Inference Handbook</a></li>

</ul>
</details>

**Discussion**: The Reddit community expressed enthusiasm about the merge, noting that EAGLE's integration into llama.cpp will make speculative decoding more practical for everyday local LLM use. Some users discussed potential memory overhead and compatibility with different model architectures.

**Tags**: `#llama.cpp`, `#speculative decoding`, `#EAGLE`, `#LLM inference`, `#open source`

---

<a id="item-13"></a>
## [Real-Time Local Voice Chatbot with Qwen3.5-397B](https://www.reddit.com/r/LocalLLaMA/comments/1u5uqsc/voicetovoice_chatbot_update/) ⭐️ 8.0/10

A developer built a near-real-time, interruptible, fully local voice-to-voice chatbot using Qwen3.5-397B, Whisper-small, and Orpheus TTS, running on a single 24GB GPU with 150GB system RAM for MoE experts. This demonstrates that large MoE models can be used for real-time voice interaction on consumer hardware, potentially enabling privacy-preserving, low-latency voice assistants without cloud dependency. The system uses Unsloth's UD-Q3_K_XL quantization for Qwen3.5-397B, Whisper-small for speech-to-text, and Orpheus TTS with a custom SNAC decoder on ONNX, achieving 21.3GB VRAM usage and 131,072 token context.

reddit · r/LocalLLaMA · /u/Responsible_Fig_1271 · Jun 14, 19:45

**Background**: Qwen3.5-397B is a Mixture-of-Experts model with 397 billion total parameters but only 17 billion active per token, allowing efficient inference. Orpheus TTS is an open-source text-to-speech model that produces natural speech. Whisper-small is a lightweight speech recognition model.

<details><summary>References</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/02/16/alibaba-qwen-team-releases-qwen3-5-397b-moe-model-with-17b-active-parameters-and-1m-token-context-for-ai-agents/">Alibaba Qwen Team Releases Qwen 3 . 5 - 397 B MoE ... - MarkTechPost</a></li>
<li><a href="https://andrew.ooo/posts/flash-moe-397b-model-macbook-local-inference/">Flash- MoE : Running a 397 B Parameter Model on... — andrew.ooo</a></li>
<li><a href="https://unsloth.ai/docs/models/qwen3.5/gguf-benchmarks">Qwen3.5 GGUF Benchmarks | Unsloth Documentation</a></li>

</ul>
</details>

**Tags**: `#voice-to-voice`, `#local LLM`, `#real-time`, `#Qwen3.5`, `#chatbot`

---

<a id="item-14"></a>
## [Running DeepSeek V4 Flash on M3 Max Mac with SSD Streaming](https://www.reddit.com/r/LocalLLaMA/comments/1u5mfaq/you_can_run_deepseek_4_flash_on_mac_m3_max_96gb/) ⭐️ 8.0/10

A user successfully runs DeepSeek V4 Flash on an M3 Max Mac with 96GB RAM using antirez's ds4 engine with SSD streaming, achieving ~12 tokens/s. The method requires passing --ssd-streaming and adjusting Metal memory limits. This demonstrates that large Mixture-of-Experts models like DeepSeek V4 Flash can run on consumer Mac hardware without requiring massive RAM, thanks to SSD streaming. It lowers the barrier for local LLM deployment and enables powerful models on laptops. The setup uses antirez's ds4 engine with a custom GGUF file and the --ssd-streaming flag, plus iogpu.wired_limit_mb=86016 to raise Metal allocation. Prefill for 36k tokens takes ~2.5 minutes, but subsequent generation sustains ~12 t/s.

reddit · r/LocalLLaMA · /u/Zeeplankton · Jun 14, 14:20

**Background**: DeepSeek V4 Flash is a Mixture-of-Experts (MoE) model with many parameters, typically requiring large RAM. SSD streaming loads only the necessary expert weights from disk on demand, enabling models larger than RAM to run. The ds4 engine is a specialized inference engine for DeepSeek models, supporting Metal, CUDA, and ROCm.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez/ds4: DeepSeek 4 Flash and PRO local inference engine for Metal, CUDA and ROCm · GitHub</a></li>
<li><a href="https://github.com/quantumnic/ssd-llm">GitHub - quantumnic/ssd-llm: Run 70B+ LLMs on Apple Silicon by using SSD as extended memory — intelligent layer streaming and caching for Mac</a></li>
<li><a href="https://simonwillison.net/2026/Mar/24/streaming-experts/">Streaming experts</a></li>

</ul>
</details>

**Discussion**: The community finds this impressive and validates the feasibility, with some noting similar experiences. Users discuss optimizations like cache safety patches and express interest in trying with other MoE models.

**Tags**: `#DeepSeek`, `#Local LLM`, `#Mac`, `#GGUF`, `#SSD streaming`

---

<a id="item-15"></a>
## [Dual DGX Sparks Run DeepSeek V4 Flash at 350 tk/s](https://www.reddit.com/r/LocalLLaMA/comments/1u5g9pr/dual_dgx_sparks_40tks_single_1m_350_tks_agg/) ⭐️ 8.0/10

A practical guide benchmarks DeepSeek V4 Flash on dual DGX Sparks connected via a $180 ConnectX-7 cable, achieving ~40 tk/s single-stream and ~350 tk/s aggregate throughput with FP8 quantization. This demonstrates that frontier-level MoE models can run locally at usable speeds for agentic workflows, potentially reducing reliance on cloud APIs for high-throughput inference. The setup uses two DGX Sparks with vLLM and FP8 quantization, achieving ~350 tk/s aggregate with 32 concurrent requests at 256k context each, outperforming a single RTX Pro 6000 (46.9 tk/s) and Mac M2 Ultra (29.7 tk/s).

reddit · r/LocalLLaMA · /u/elsung · Jun 14, 09:07

**Background**: DeepSeek V4 Flash is a 284B-parameter MoE model with 13B activated parameters, supporting a 1M-token context window. DGX Spark is NVIDIA's compact desktop AI supercomputer, and ConnectX-7 is a 200 Gbps interconnect cable enabling low-latency multi-node inference.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>
<li><a href="https://www.lenovo.com/us/en/p/accessories-and-software/cables-and-adapters/cables/4x91u42988">PGX ConnectX-7 cable | 4X91U42988 | Lenovo US</a></li>
<li><a href="https://sebastianraschka.com/blog/2025/dgx-impressions.html">Local PyTorch and LLM Dev: DGX Spark ... | Sebastian Raschka, PhD</a></li>

</ul>
</details>

**Discussion**: The Reddit community praised the benchmark as high-value and practical, with discussions focusing on the cost-effectiveness of the $180 cable versus cloud alternatives. Some users noted the need for two DGX Sparks as a limitation.

**Tags**: `#DeepSeek`, `#DGX Spark`, `#MoE`, `#benchmark`, `#local LLM`

---