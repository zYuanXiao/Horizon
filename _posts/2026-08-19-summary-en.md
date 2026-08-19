---
layout: default
title: "Horizon Summary: 2026-08-19 (EN)"
date: 2026-08-19
lang: en
---

> From 131 items, 15 important content pieces were selected

---

1. [Mojo Programming Language Open-Sourced Under Apache 2.0](#item-1) ⭐️ 9.0/10
2. [VibeWorlding: Benchmarking Multimodal Agents for 3D World Construction](#item-2) ⭐️ 8.0/10
3. [SA-MRPO: Saturation-Aware Reweighting for Multi-Reward RL](#item-3) ⭐️ 8.0/10
4. [Linux 7.3 Boosts Performance When GPU VRAM Runs Out](#item-4) ⭐️ 8.0/10
5. [Rethinking Database Programming: Non-SQL Schema Definition Sparks Debate](#item-5) ⭐️ 8.0/10
6. [Asana Completes 5 Years of Engineering Work in 2 Weeks with OpenAI Codex](#item-6) ⭐️ 8.0/10
7. [Microsoft Copilot Secret Parameter Enables Password Theft](#item-7) ⭐️ 8.0/10
8. [Alibaba's RISC-V CPU Runs Qwen-3.8 27B at 30 tps](#item-8) ⭐️ 8.0/10
9. [Memory Prices Surge 500% in a Year, 128GB DDR5 Hits $3,399](#item-9) ⭐️ 8.0/10
10. [DeepSeek V4 Flash Q4_K_XL Hits 100 tok/s on 4× RTX 3060](#item-10) ⭐️ 8.0/10
11. [DFlash 2: Parallel Drafting Boosts Speculative Decoding](#item-11) ⭐️ 8.0/10
12. [Qwen3.8-27B hits 124 tps on RTX 3090 via hyper-optimized engine](#item-12) ⭐️ 8.0/10
13. [Anthropic-Cybersecurity-Skills: 817 AI Agent Skills for Security](#item-13) ⭐️ 8.0/10
14. [Unsloth Gains 449 Stars, Adds Support for Qwen3.8 and DeepSeek-V4](#item-14) ⭐️ 8.0/10
15. [omlx: LLM Inference Server with Continuous Batching & SSD Caching for Apple Silicon](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Mojo Programming Language Open-Sourced Under Apache 2.0](https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/) ⭐️ 9.0/10

Modular has open-sourced the Mojo programming language, including its compiler and toolchain, under the Apache 2.0 license. This release follows the recent Mojo 1.0 milestone and fulfills a promise made in May 2023. This open-sourcing is a major milestone for the AI and developer community, as Mojo is designed to combine Python-like syntax with high performance for AI workloads. It could accelerate adoption and foster a broader ecosystem around Mojo, potentially impacting Python-based AI tooling and performance-sensitive applications. Mojo was originally intended to be a superset of Python, but this goal was abandoned around August 2025; it is now its own language. Mojo builds on the MLIR compiler framework, enabling efficient compilation to CPUs, GPUs, TPUs, and other accelerators.

rss · Simon Willison · Aug 18, 21:39

**Background**: Mojo is a systems programming language developed by Modular Inc., designed for high-performance AI infrastructure. It uses a syntax reminiscent of Python but incorporates systems programming features like static typing and a borrow checker, inspired by Rust. The language leverages the MLIR compiler framework to target diverse hardware, making it well-suited for AI applications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License</a></li>

</ul>
</details>

**Discussion**: The community discussion on Lobste.rs and Reddit generally expresses excitement and approval, with many noting the fulfillment of a long-awaited promise. Some users discuss the implications of Mojo no longer being a Python superset, while others highlight the potential benefits of open-sourcing for transparency and community contributions.

**Tags**: `#Mojo`, `#open source`, `#programming language`, `#AI`, `#compiler`

---

<a id="item-2"></a>
## [VibeWorlding: Benchmarking Multimodal Agents for 3D World Construction](https://huggingface.co/papers/2608.15265) ⭐️ 8.0/10

VibeWorlding introduces a unified framework and benchmark, VWE-BENCH, with 2,616 3D assets, 323 seed worlds, and 6,828 multimodal queries, to train and evaluate multimodal agents that construct interactive 3D worlds from user queries. The paper also presents VibeWorlding-Gym, a reinforcement learning post-training framework, and shows that their VibeWorlder-30B-A3B model achieves the best Pass@1 among all evaluated models, surpassing closed-source frontiers. This work addresses a significant gap in evaluating multimodal agents for complex 3D world construction, moving beyond idealized simple queries. By demonstrating that reinforcement learning can boost open-source models to surpass closed-source ones, it has implications for embodied AI and interactive systems, potentially democratizing advanced 3D generation capabilities. The benchmark includes verified queries with ground-truth and unverified queries with carefully designed rubrics. The VibeWorlding-Gym integrates a sandbox environment with MCP tools for asset retrieval, editing, and rendering, and a rubric-based verifier that checks physical feasibility and intent fulfillment. Current frontier MLLMs like GPT-5.5 and Qwen3.8-Max achieve below 60% success rate, with the bottleneck traced to precise 3D world editing.

huggingface_papers · Hugging Face Papers · Aug 18, 00:00

**Background**: Multimodal agents are AI systems that process and reason across multiple data types, such as text, images, and audio, often using external tools. 3D world generation from text is an emerging field, with systems like Meta's WorldGen generating interactive 3D scenes from prompts. Reinforcement learning is a machine learning paradigm where agents learn through trial-and-error interactions with an environment, which has been applied to improve AI agent performance.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Multimodal_and_tool-use_in_AI_agents">Multimodal and tool-use in AI agents</a></li>
<li><a href="https://www.meta.com/blog/worldgen-3d-world-generation-reality-labs-generative-ai-research/">Research Update: WorldGen — From Text to Immersive 3D Worlds</a></li>
<li><a href="https://hackernoon.com/beyond-transformers-the-overlooked-potential-of-reinforcement-learning">Beyond Transformers: The Overlooked Potential of Reinforcement ...</a></li>

</ul>
</details>

**Tags**: `#multimodal agents`, `#3D world generation`, `#benchmark`, `#reinforcement learning`, `#AI`

---

<a id="item-3"></a>
## [SA-MRPO: Saturation-Aware Reweighting for Multi-Reward RL](https://huggingface.co/papers/2608.16072) ⭐️ 8.0/10

The paper introduces SA-MRPO, a method that standardizes each reward objective independently and adaptively discounts saturated objectives based on batch-level saturation estimates, dynamically reallocating optimization effort toward under-optimized goals. It improves the harder correctness objective over GDPO in 12 of 15 benchmark comparisons, with gains up to 5% on AIME24. This work addresses a fundamental limitation in multi-reward RL for LLMs, where fixed weighted sum scalarization leads to inefficient gradient allocation. By focusing on under-optimized objectives, SA-MRPO could improve training efficiency and final performance, benefiting the broader AI alignment and post-training community. SA-MRPO can reverse the sign of an update, not just rescale its magnitude, which is a notable property. It shows consistent improvements across mathematical reasoning, adaptive reasoning, and coding benchmarks, while maintaining performance on easier objectives.

huggingface_papers · Hugging Face Papers · Aug 18, 00:00

**Background**: Group-relative policy optimization methods like GRPO are standard for post-training LLMs, but they typically scalarize multiple rewards with fixed weights before standardization. This can cause rollouts with different reward profiles to receive identical advantages and continue optimizing already-solved objectives. SA-MRPO addresses this by independently standardizing each reward and adaptively discounting saturated ones.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2601.23058v1">From Absolute to Relative: Rethinking Reward Shaping in Group-Based Reinforcement Learning</a></li>
<li><a href="https://cameronrwolfe.substack.com/p/grpo">Group Relative Policy Optimization (GRPO)</a></li>
<li><a href="https://huggingface.co/papers/2601.05242">Paper page - GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#multi-objective optimization`, `#LLM post-training`, `#policy optimization`, `#AI alignment`

---

<a id="item-4"></a>
## [Linux 7.3 Boosts Performance When GPU VRAM Runs Out](https://pixelcluster.dev/VRAM-Overcommit/) ⭐️ 8.0/10

Linux kernel version 7.3 introduces VRAM overcommit improvements that enhance performance when GPU memory is exhausted. This update is particularly notable for its potential to improve LLM inference and shared memory systems. This improvement is significant because it addresses a common bottleneck in GPU-intensive workloads, such as AI inference and gaming, where running out of VRAM often causes severe performance degradation or crashes. It could benefit a wide range of users, from gamers to data scientists, by making systems more resilient and efficient. The update focuses on virtual memory fragmentation and paging mechanisms, potentially allowing the kernel to manage GPU memory more effectively. However, Nvidia GPUs currently lack support for paging, which may limit the benefits for Nvidia users until driver updates are released.

hackernews · flaburgan · Aug 18, 07:51 · [Discussion](https://news.ycombinator.com/item?id=49342719)

**Background**: VRAM overcommit is a technique where the system allows more memory to be allocated than physically available, relying on paging or swapping to handle excess demand. In Linux, overcommit accounting has been a feature for CPU memory, but applying it to GPU memory is relatively new. For LLM inference, GPU memory is critical for storing model weights and activations, and running out of VRAM often leads to out-of-memory errors. Shared memory architectures, such as AMD APUs, can benefit from improved VRAM management by better utilizing available system RAM.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kernel.org/doc/Documentation/vm/overcommit-accounting">kernel .org/doc/Documentation/vm/ overcommit -accounting</a></li>
<li><a href="https://developer.nvidia.com/blog/accelerate-large-scale-llm-inference-and-kv-cache-offload-with-cpu-gpu-memory-sharing/">Accelerate Large-Scale LLM Inference and KV Cache Offload with CPU-GPU Memory Sharing | NVIDIA Technical Blog</a></li>
<li><a href="https://www.spheron.network/blog/dedicated-vs-shared-gpu-memory/">What Is Shared GPU Memory? Dedicated vs Shared (2026) | Spheron Blog</a></li>

</ul>
</details>

**Discussion**: Community comments express excitement about the improvement, with users hoping for upstream integration and noting the lack of Nvidia support for paging. Some users question whether the benefits extend to compute workloads like LLM inference, while others share experiences with shared memory systems and performance diagnostics. Overall sentiment is positive, with anticipation for future kernel updates.

**Tags**: `#Linux kernel`, `#VRAM`, `#GPU memory`, `#performance`, `#open source`

---

<a id="item-5"></a>
## [Rethinking Database Programming: Non-SQL Schema Definition Sparks Debate](https://acadia.engineering/blog/rethinking-database-programming) ⭐️ 8.0/10

The article proposes rethinking database programming by defining schemas in a non-SQL language, challenging the conventional use of SQL for schema definition. This approach aims to offer a more expressive and integrated way to define database structures. This matters because it could influence how developers approach database design, potentially offering more flexibility and expressiveness than SQL. It also sparks a broader discussion about the trade-offs between SQL and alternative approaches, affecting the future of database tooling and interoperability. The article suggests that schemas defined in a non-SQL language can coexist with SQL, but community comments highlight concerns about lagging behind database features, interop issues with custom encodings, and the risks of closed-source licensing. The discussion references PostgreSQL's extensive CREATE TABLE features as a benchmark for what such languages must support.

hackernews · honungsburk · Aug 18, 07:28 · [Discussion](https://news.ycombinator.com/item?id=49342530)

**Background**: SQL is the standard language for relational database management, including schema definition via Data Definition Language (DDL). Alternatives to SQL exist, such as NoSQL databases and query languages like Gremlin or N1QL, but they often sacrifice relational integrity or expressiveness. The article's proposal is part of a broader trend of seeking more developer-friendly or expressive ways to interact with databases.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ionos.com/digitalguide/server/know-how/the-best-sql-alternatives/">What alternatives to SQL are there? - IONOS</a></li>
<li><a href="https://grokipedia.com/page/SQL-92">SQL -92 — Grokipedia</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism about replacing SQL, noting that relational database architecture is proven and composable. Concerns include the difficulty of keeping up with database features, potential interop issues with custom encodings, and the risks of adopting closed-source software with restrictive licenses, as seen with Elm's trajectory.

**Tags**: `#database`, `#SQL`, `#programming-languages`, `#schema`, `#interop`

---

<a id="item-6"></a>
## [Asana Completes 5 Years of Engineering Work in 2 Weeks with OpenAI Codex](https://openai.com/index/asana) ⭐️ 8.0/10

Asana used OpenAI Codex to replace an outdated testing system in just two weeks, a task that was expected to take five years, at a cost of approximately $12,000. This case demonstrates the transformative potential of AI coding tools in modernizing legacy systems, offering significant time and cost savings. It highlights a practical, real-world application that could influence how engineering teams approach large-scale refactoring projects. The project involved replacing an outdated testing system, which typically requires extensive manual effort and domain knowledge. The use of Codex, an AI coding agent, enabled Asana to automate and accelerate the process, achieving in weeks what was estimated to take years.

rss · OpenAI Blog · Aug 18, 07:00

**Background**: OpenAI Codex is a coding agent that can edit code repositories, run tests, and perform code reviews, available in various interfaces like CLI, IDE, and cloud. Legacy system modernization often involves refactoring or replacing outdated components, which is time-consuming and risky, but AI tools like Codex can help streamline these efforts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.goodvibecode.com/tools/codex">OpenAI Codex Review 2026: Features, Pricing & Alternatives</a></li>
<li><a href="https://github.com/openai/codex">GitHub - openai / codex : Lightweight coding agent that runs in your...</a></li>
<li><a href="https://www.testingxperts.com/blog/legacy-system">Legacy System Modernization: Challenges & Best Practices</a></li>

</ul>
</details>

**Tags**: `#AI coding`, `#software engineering`, `#legacy modernization`, `#OpenAI Codex`, `#productivity`

---

<a id="item-7"></a>
## [Microsoft Copilot Secret Parameter Enables Password Theft](https://arstechnica.com/security/2026/08/microsoft-copilot-reveals-secret-input-that-allowed-it-to-be-hacked/) ⭐️ 8.0/10

Researchers discovered a critical vulnerability in Microsoft 365 Copilot for enterprise, where a secret parameter in a URL allowed attackers to steal passwords when a target clicked a malicious link. The vulnerability, named CoSnitch, was disclosed by Varonis researchers and affects Microsoft Copilot Personal. This vulnerability is significant because it affects a widely-used AI product and enables real-world password theft, posing a direct threat to enterprise security. It highlights the growing security risks in AI-powered assistants and the need for robust input validation and access controls. The exploit leverages a hidden 'autorun' parameter in Copilot's URL handling, allowing one-click data exfiltration. The vulnerability was discovered through an unusual source, though the exact method remains undisclosed in the summary.

rss · Ars Technica AI · Aug 18, 13:00

**Background**: Prompt injection is a cybersecurity exploit where innocuous-looking inputs are designed to cause unintended behavior in large language models (LLMs). In this case, the secret parameter likely triggers a prompt injection that overrides Copilot's intended instructions, leading to data leakage. This attack vector is a growing concern for AI security, as highlighted by OWASP and other sources.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/08/microsoft-copilot-reveals-secret-input-that-allowed-it-to-be-hacked/">Microsoft Copilot reveals secret input that allowed it to... - Ars Technica</a></li>
<li><a href="https://getaibook.com/news/cosnitch-exploit-leaks-copilot-data-via-hidden-url-parameter/">CoSnitch Exploit Leaks Copilot Data via Hidden URL Parameter | News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI`, `#Microsoft Copilot`, `#vulnerability`, `#hacking`

---

<a id="item-8"></a>
## [Alibaba's RISC-V CPU Runs Qwen-3.8 27B at 30 tps](https://www.reddit.com/r/LocalLLaMA/comments/1vs0wsl/alibabas_riscv_cpu_xuantie_c950_runs_qwen38_27b/) ⭐️ 8.0/10

Alibaba's XuanTie C950 RISC-V CPU has demonstrated the ability to run the Qwen-3.8 27B large language model at 30 tokens per second, marking a significant performance milestone for CPU-based LLM inference. This achievement challenges the dominance of GPUs in LLM inference, potentially offering a more accessible and cost-effective alternative for deploying large models. It also highlights the growing maturity of the RISC-V ecosystem for AI workloads. The XuanTie C950 is a 5nm, RVA23-compliant RISC-V core with up to 8 cores clocked at 3.2 GHz, achieving a SPECint2006 score of over 70. The Qwen-3.8 27B model is a 27-billion-parameter LLM that scores 52 on the Artificial Analysis Intelligence Index.

reddit · r/LocalLLaMA · /u/DeltaSqueezer · Aug 18, 20:24

**Background**: LLM inference typically relies on GPUs due to their parallel processing capabilities, but CPUs are increasingly being optimized for this task. Tokens per second (TPS) measures the generation speed after the first token, and 30 TPS is considered usable for interactive applications. RISC-V is an open instruction set architecture that has been gaining traction in various computing domains.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnx-software.com/2026/03/25/alibaba-xuantie-c950-a-powerful-rva2364-bit-risc-v-core-for-edge-ai-computing/">Alibaba XuanTie C 950 - A powerful, RVA23-compliant... - CNX Software</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/ Qwen 3 . 8 - 27 B · Hugging Face</a></li>
<li><a href="https://www.gmicloud.ai/en/blog/ttft-llm-speed-metrics">TTFT vs Tokens Per Second : LLM Inference Speed... | GMI Cloud</a></li>

</ul>
</details>

**Tags**: `#RISC-V`, `#LLM inference`, `#CPU performance`, `#Alibaba`, `#Qwen`

---

<a id="item-9"></a>
## [Memory Prices Surge 500% in a Year, 128GB DDR5 Hits $3,399](https://www.reddit.com/r/LocalLLaMA/comments/1vrwsfl/memory_prices_climb_500_in_12_months_up_to_10x/) ⭐️ 8.0/10

Memory prices have climbed 500% in 12 months, with 128GB DDR5 kits now costing $3,399, up to 10 times the lowest ever tracked prices. This dramatic increase is attributed to supply constraints and rising demand, particularly from AI applications. This price surge significantly impacts AI/ML practitioners who rely on local hardware for LLM inference, as memory is a critical component for running large models. It may force users to delay upgrades, seek alternatives like DDR4, or shift to cloud-based solutions, affecting the broader AI hardware ecosystem. The price increase is not uniform; DDR4 prices have also risen by 120-180% due to increased demand from users avoiding expensive DDR5. Recent tracking shows a slight drop in DDR5 prices this week, but discounts are limited to a few vendors, suggesting volatility remains.

reddit · r/LocalLLaMA · /u/johnnyApplePRNG · Aug 18, 17:59

**Background**: Memory prices are influenced by supply-demand dynamics, manufacturing capacity, and market speculation. For local LLM inference, high-capacity memory (e.g., 128GB) is essential for running large models without relying on cloud services, as unified memory on Apple Silicon or high-end GPUs can serve as VRAM. The surge in prices is partly driven by AI's growing demand for memory, alongside traditional PC market cycles.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/ram/memory-prices-climb-500-percent-in-12-months-up-to-10x-the-lowest-ever-tracked-prices-128gb-of-ddr5-now-usd3-399">Memory prices climb 500% in 12 months, up to... | Tom's Hardware</a></li>
<li><a href="https://www.aroged.com/2026/08/17/rammageddon-has-arrived-ram-prices-have-soared-to-crazy-heights-128-gb-ddr5-costs-3399/">RAMmageddon has arrived: RAM prices have soared to... - Aroged</a></li>
<li><a href="https://wccftech.com/ddr5-prices-just-posted-their-first-drop-in-several-months/">DDR 5 Memory Prices Just Took a Noticeable Dive for the First Time...</a></li>

</ul>
</details>

**Discussion**: Community comments on Reddit likely express frustration over rising costs, with some suggesting alternatives like using DDR4 or cloud services. Others may discuss the impact on local LLM projects and speculate on future price trends, with a mix of concern and pragmatic advice.

**Tags**: `#hardware`, `#memory`, `#LLM`, `#pricing`, `#AI infrastructure`

---

<a id="item-10"></a>
## [DeepSeek V4 Flash Q4_K_XL Hits 100 tok/s on 4× RTX 3060](https://www.reddit.com/r/LocalLLaMA/comments/1vrqf4f/running_deepseek_v4_flash_q4_k_xl_at_100_toks/) ⭐️ 8.0/10

A user successfully ran the 144 GiB DeepSeek-V4-Flash-0731 UD-Q4_K_XL GGUF model on four RTX 3060 12GB GPUs with a 368k context window, achieving ~100 tok/s prompt processing and ~10 tok/s generation using llama.cpp build b10181. The breakthrough involves a custom layer distribution using -ncmoe 34 and explicit -ot overrides to place expert layers on GPUs 1-3 while keeping most non-expert tensors on GPU0. This demonstrates that large MoE models (144 GiB) can run on consumer hardware with reasonable performance, pushing the boundaries of local LLM inference. The technique of combining -ncmoe with explicit tensor placement could be adopted by others to run models that would otherwise require expensive enterprise GPUs. The configuration uses -ts 100,1,1,1 to push non-expert tensors to GPU0, while -ot assigns expert layers from blocks 34-42 to GPUs 1-3. Microbatch size (-ub) was the biggest performance lever: increasing from 1024 to 2048 boosted prompt processing from ~63 to ~99 tok/s. The model is mostly in system RAM, so quad-channel memory bandwidth is critical.

reddit · r/LocalLLaMA · /u/syscomua · Aug 18, 14:15

**Background**: DeepSeek V4 Flash is a Mixture-of-Experts (MoE) model, meaning only a subset of parameters are active per token, reducing compute. GGUF quantization (Q4_K_XL) compresses weights to 4-bit, reducing memory footprint. llama.cpp supports multi-GPU inference via tensor splitting and layer distribution, but manual placement can optimize VRAM usage.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/blob/master/docs/multi-gpu.md">llama . cpp /docs/ multi - gpu .md at master · ggml-org/ llama . cpp · GitHub</a></li>
<li><a href="https://insiderllm.com/guides/llm-quantization-explained/">Quantization Explained: What It Means for Local AI | InsiderLLM</a></li>

</ul>
</details>

**Discussion**: The comment mentions that a second version of DeepSeek Flash GGUF quants has been released by the original authors, along with an accompanying llama.cpp PR (https://github.com/ggml-org/llama.cpp/pull/27342). This suggests ongoing improvements and community interest in optimizing this model.

**Tags**: `#llama.cpp`, `#DeepSeek`, `#GGUF`, `#multi-GPU`, `#local LLM`

---

<a id="item-11"></a>
## [DFlash 2: Parallel Drafting Boosts Speculative Decoding](https://www.reddit.com/r/LocalLLaMA/comments/1vs2tz1/dflash_2_keep_drafting_parallel/) ⭐️ 8.0/10

DFlash 2 introduces a novel parallel drafting method for speculative decoding, which could significantly improve LLM inference speed. The approach allows multiple candidate tokens to be drafted simultaneously, reducing latency compared to traditional sequential drafting. This advancement is significant for the AI/ML community as it addresses a key bottleneck in LLM inference, potentially enabling faster and more cost-effective deployment of large models. It could impact a wide range of applications, from real-time chatbots to large-scale batch processing. The method is designed to work with existing speculative decoding frameworks, requiring minimal changes to the target model. The paper likely includes experimental results demonstrating speedups on standard benchmarks, though specific numbers are not provided in the summary.

reddit · r/LocalLLaMA · /u/coder543 · Aug 18, 21:37

**Background**: Speculative decoding is an inference-time optimization for autoregressive large language models (LLMs) that generates multiple tokens per decoding step instead of one. A smaller draft model proposes a sequence of candidate tokens, and the larger target model verifies them in a single forward pass, preserving the original output distribution while cutting latency by roughly two to three times. Parallel drafting methods, like DFlash 2, aim to further improve this process by drafting multiple candidate tokens simultaneously, potentially increasing the acceptance rate and reducing the number of verification steps.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://arxiv.org/pdf/2401.07851">Unlocking Efficiency in Large Language Model Inference</a></li>
<li><a href="https://rits.shanghai.nyu.edu/ai/jetspec-causal-parallel-tree-drafting-hits-9-64x-faster-llm-inference/">JetSpec: Causal Parallel Tree Drafting Hits 9.64x Faster LLM Inference</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#speculative decoding`, `#inference optimization`, `#AI/ML`

---

<a id="item-12"></a>
## [Qwen3.8-27B hits 124 tps on RTX 3090 via hyper-optimized engine](https://www.reddit.com/r/LocalLLaMA/comments/1vrw4sz/i_pushed_qwen3827b_to_124_tps_on_a_single_request/) ⭐️ 8.0/10

A developer released a hyper-optimized inference engine for Qwen3.8-27B on an RTX 3090, achieving 124 tokens per second (tps) on a single request with greedy sampling, up from 90 tps. The update adds GPTQ-int4 quantization for the lm_head and MTP module, a split-KV attention kernel, and a new draft vocabulary covering 97.5% of model outputs. This demonstrates that highly optimized local inference can rival cloud performance on consumer hardware, potentially enabling more accessible and private LLM deployment. The techniques (FP8 KV cache, int8 activations, MTP speculative decoding) could be adopted by the broader community to improve inference efficiency. The engine uses fp8 KV cache, int8 activations, and MTP-4 drafts with a 40k-token draft head, achieving 124 tps greedy and ~114 tps at default sampling. The GPTQ-int4 quantization adds only +0.6% PPL with GSM8K unchanged, and the split-KV kernel is 5x faster at 1.5k context and 10x at 16k. The full 262k context fits with KVarN 4/2-bit KV cache, correct to 240k.

reddit · r/LocalLLaMA · /u/iamMess · Aug 18, 17:35

**Background**: Speculative decoding uses a small draft model to propose multiple tokens, which the target model verifies in parallel, speeding up generation without changing output distribution. MTP (Multi-Token Prediction) is a specific approach where the draft head is trained on the target model's distribution. Quantization reduces model size and memory bandwidth by using lower-precision numbers, but can degrade quality; GPTQ is a popular post-training quantization method. The RTX 3090 has 24GB VRAM and 82 SMs, limiting inference speed, so optimizations like kernel fusion and KV cache compression are crucial.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.plainenglish.io/gemma-4-mtp-local-inference-benchmarks-6711c8589d2f">Gemma 4 MTP Local Inference Benchmarks & Real-World Testing</a></li>
<li><a href="https://effloow.com/articles/gemma-4-mtp-multi-token-prediction-inference-guide-2026">Gemma 4 MTP Drafters: How Multi-Token Prediction... — Effloow</a></li>
<li><a href="https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/">Mastering LLM Techniques: Inference Optimization | NVIDIA Technical...</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#quantization`, `#speculative decoding`, `#RTX 3090`, `#performance optimization`

---

<a id="item-13"></a>
## [Anthropic-Cybersecurity-Skills: 817 AI Agent Skills for Security](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10

A GitHub repository named mukul975/Anthropic-Cybersecurity-Skills has gained over 730 stars in a day, offering 817 structured cybersecurity skills for AI agents. These skills are mapped to six major frameworks and are compatible with multiple AI platforms. This repository addresses the growing need for AI agents to perform cybersecurity tasks with structured, framework-aligned knowledge. Its rapid popularity indicates strong community interest and potential to standardize AI-driven security operations across various tools. The skills cover 29 security domains and follow the agentskills.io open standard, making them usable with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI, and over 20 other platforms. The repository is licensed under Apache 2.0 and includes mappings to MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF, and MITRE F3.

github_trending · GitHub Trending · Aug 19, 01:17

**Background**: AI agents are increasingly used in cybersecurity for tasks like threat detection and response. Frameworks like MITRE ATT&CK and NIST CSF provide structured knowledge of attack and defense techniques, while the agentskills.io standard offers a way to package such knowledge for AI agents. This repository combines these elements, providing a comprehensive resource for developers and security professionals.

<details><summary>References</summary>
<ul>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>
<li><a href="https://github.com/mukul975/Anthropic-Cybersecurity-Skills">GitHub - mukul975/Anthropic-Cybersecurity- Skills : 817 structured...</a></li>
<li><a href="https://www.vectra.ai/topics/mitre-atlas">MITRE ATLAS : AI security framework with 16 tactics and 84 techniques</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#AI agents`, `#MITRE ATT&CK`, `#NIST`, `#open source`

---

<a id="item-14"></a>
## [Unsloth Gains 449 Stars, Adds Support for Qwen3.8 and DeepSeek-V4](https://github.com/unslothai/unsloth) ⭐️ 8.0/10

Unsloth, a Python library for efficient LLM and diffusion model training and inference, gained 449 stars on GitHub today, reaching 73,601 total stars. The project now supports recent models including Qwen3.8, Kimi K3, MiniMax-H3, Gemma 4, DeepSeek-V4, and FLUX. Unsloth's continued growth and rapid adoption of cutting-edge models highlight its importance in the open-source AI ecosystem, enabling developers to fine-tune and run state-of-the-art models locally with reduced resource requirements. This trend reflects the broader movement toward accessible, efficient AI development tools. The repository is written in Python and has 6,648 forks. The local UI supports both LLMs and diffusion models, catering to a wide range of generative AI tasks. The daily star increase of 449 indicates strong community interest and active maintenance.

github_trending · GitHub Trending · Aug 19, 01:17

**Background**: Unsloth is a popular open-source library that optimizes the fine-tuning and inference of large language models and diffusion models, often achieving significant speedups and memory savings. Models like Qwen3.8 and DeepSeek-V4 are recent releases in the rapidly evolving AI landscape, with Qwen3.8 focusing on agentic coding and DeepSeek-V4 offering Pro and Flash variants with 1M context support. FLUX is a professional-grade image generation model known for high-resolution output.

<details><summary>References</summary>
<ul>
<li><a href="https://apidog.com/blog/what-is-qwen-3-8/">What Is Qwen 3 . 8 -Max?</a></li>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 Explained: V 4 -Pro 1.6T vs V 4 -Flash 284B (2026)</a></li>
<li><a href="https://www.datacamp.com/tutorial/flux-ai">Flux AI Image Generator: A Guide With Examples | DataCamp</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#fine-tuning`, `#diffusion models`, `#open-source`, `#Python`

---

<a id="item-15"></a>
## [omlx: LLM Inference Server with Continuous Batching & SSD Caching for Apple Silicon](https://github.com/jundot/omlx) ⭐️ 8.0/10

omlx is a new open-source LLM inference server for Apple Silicon, featuring continuous batching and SSD caching, and is managed from the macOS menu bar. It has gained rapid traction, with 370 stars in a day and over 19,000 total stars. This tool addresses the growing need for efficient local LLM inference on Apple Silicon, potentially improving throughput and reducing latency for developers and researchers. Its popularity indicates strong community interest in optimizing LLM serving on consumer hardware. The server uses continuous batching to schedule new requests as slots free up, and SSD caching offloads hot cache blocks to disk in safetensors format, restoring them on matching prefixes even after restarts. It is written in Python and available on GitHub.

github_trending · GitHub Trending · Aug 19, 01:17

**Background**: Continuous batching is a technique that improves LLM inference throughput by dynamically scheduling requests instead of waiting for a fixed batch to complete. SSD caching helps reduce recomputation by storing intermediate results, which is especially useful on devices with limited RAM like Apple Silicon Macs. This project combines these techniques to offer a user-friendly inference server for macOS users.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/jundot/omlx">jundot/omlx: LLM inference server with continuous batching & SSD ...</a></li>
<li><a href="https://insujang.github.io/2024-01-07/llm-inference-continuous-batching-and-pagedattention/">LLM Inference : Continuous Batching and PagedAttention</a></li>
<li><a href="https://www.anyscale.com/blog/continuous-batching-llm-inference">Achieve 23x LLM Inference Throughput & Reduce p50 Latency</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#inference`, `#Apple Silicon`, `#macOS`, `#open-source`

---