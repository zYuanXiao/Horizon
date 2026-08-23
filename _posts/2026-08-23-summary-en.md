---
layout: default
title: "Horizon Summary: 2026-08-23 (EN)"
date: 2026-08-23
lang: en
---

> From 121 items, 15 important content pieces were selected

---

1. [OpenAI's Codex Terminal Coding Agent Surges on GitHub](#item-1) ⭐️ 9.0/10
2. [EnvHarness: Dynamic Environment Reshaping for Agent Learning](#item-2) ⭐️ 8.0/10
3. [Zetta: Closed-Loop Harness for Self-Evolving Physical Intelligence](#item-3) ⭐️ 8.0/10
4. [Simulation in AI: 10% Worse, 100x Cheaper, 10000x Faster](#item-4) ⭐️ 8.0/10
5. [Claude's Invisible Watermarking Explained in Video Walkthrough](#item-5) ⭐️ 8.0/10
6. [DFlash 2 in llama.cpp: 2.26x Speedup on Real Coding Tasks](#item-6) ⭐️ 8.0/10
7. [RTX 5090 Runs Qwen3.8-27B at 262K Context with 77 tok/s](#item-7) ⭐️ 8.0/10
8. [Developer Trains 250M LLM from Scratch, Quantizes to 60 MB with Disk-Based Long Context](#item-8) ⭐️ 8.0/10
9. [Single Attention Head Ablation Makes Chess Transformer Miss Queen Sacrifice](#item-9) ⭐️ 8.0/10
10. [DelveRL: Open-Source Roguelike for Training Game-Playing Agents](#item-10) ⭐️ 8.0/10
11. [Evaluation Resolution Artifact Undermines Untrained CNN Brain-Likeness Claims](#item-11) ⭐️ 8.0/10
12. [UBS Projects $4.1T AI Infrastructure Spend by 2028, But Grid Queue Looms](#item-12) ⭐️ 8.0/10
13. [NousResearch's Hermes Agent: Self-Improving AI Agent Goes Viral on GitHub](#item-13) ⭐️ 8.0/10
14. [ECC: Agent Harness Performance Optimization System Gains Traction](#item-14) ⭐️ 8.0/10
15. [Tencent's AI-Infra-Guard: Full-Stack AI Red Teaming Platform](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI's Codex Terminal Coding Agent Surges on GitHub](https://github.com/openai/codex) ⭐️ 9.0/10

OpenAI's Codex, a lightweight terminal-based coding agent written in Rust, has gained significant traction on GitHub, with 1,544 stars today and a total of 113,438 stars. The repository is currently trending on GitHub, indicating a surge in developer interest. This release highlights OpenAI's continued investment in AI-powered software engineering tools, offering developers a practical way to integrate AI into their terminal workflows. The high star count and rapid growth suggest strong community demand for efficient, local coding agents, potentially influencing the broader developer tools ecosystem. Codex is available through ChatGPT's web app, the Codex CLI, a desktop app for Windows and macOS, and several IDE integrations. It is designed to handle tasks such as writing code, fixing bugs, and completing pull requests, with a focus on performance due to its Rust implementation.

github_trending · GitHub Trending · Aug 23, 01:32

**Background**: Codex is an AI coding agent developed by OpenAI, released in April 2025 as Codex CLI. It is a descendant of GPT-3, trained on both natural language and billions of lines of source code from public repositories. Terminal-based coding agents like Codex have direct access to the filesystem, shell, and dev tools, allowing them to autonomously edit files, run tests, and iterate on errors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://openai.com/codex/">Codex in ChatGPT | AI Coding Agents for Software ... - OpenAI</a></li>
<li><a href="https://openai.com/index/openai-codex/">OpenAI Codex</a></li>

</ul>
</details>

**Tags**: `#AI`, `#coding agent`, `#OpenAI`, `#developer tools`, `#Rust`

---

<a id="item-2"></a>
## [EnvHarness: Dynamic Environment Reshaping for Agent Learning](https://huggingface.co/papers/2608.19880) ⭐️ 8.0/10

EnvHarness introduces a programmable plugin layer that wraps static environments to dynamically reshape their behavior, and EnvRigger automatically synthesizes these plugins by observing the target policy's execution trajectories. This approach outperforms original environments and domain-specific pipelines across five benchmarks, achieving up to a 9.0-point improvement on held-out instances with 9.8% fewer execution steps. This framework addresses a critical limitation in reinforcement learning and LLM agent training: static environments that fail to adapt to an agent's evolving capabilities. By enabling continuous, targeted co-evolution of policy and environment, EnvHarness could significantly improve training efficiency and generalization across diverse domains. EnvHarness operates through standard interfaces, ensuring every reshaped environment retains its original verifier, thus avoiding expensive or unreliable verification. EnvRigger treats the target policy as a black box, diagnosing flaws and validating new components via fresh rollouts, making the approach general and domain-agnostic.

huggingface_papers · Hugging Face Papers · Aug 21, 00:00

**Background**: LLM agents learn by interacting with environments, but these environments are typically hand-built and static, becoming outdated as the agent improves. Recent environment generation methods require domain-specific pipelines and rely on expensive or unreliable verifiers, and still produce static environments. EnvHarness alleviates the engineering burden by providing a programmable layer that reshapes existing environments without modifying their underlying logic.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.19880">EnvHarness: Awakening Static Worlds for Agent Learning</a></li>
<li><a href="https://envharness.com/">EnvHarness: Awakening Static Worlds for Agent Learning</a></li>
<li><a href="https://huggingface.co/papers/2608.19880">Paper page - EnvHarness: Awakening Static Worlds for Agent Learning</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#LLM agents`, `#environment generation`, `#AI research`, `#co-evolution`

---

<a id="item-3"></a>
## [Zetta: Closed-Loop Harness for Self-Evolving Physical Intelligence](https://huggingface.co/papers/2608.16590) ⭐️ 8.0/10

Zetta introduces a closed-loop embodied harness that evolves code-based runtime critics and recovery skills online while keeping the base policy frozen, achieving state-of-the-art success rates of 90.8% on LIBERO-Pro and 93.6% on RoboCasa with an 11.1x inference speedup. This work addresses a critical limitation in current agentic systems by enabling closed-loop learning during physical execution, which is essential for reliable embodied AI. It demonstrates a scaling path for physical intelligence through self-exploration, potentially impacting robotics and autonomous systems. Zetta operates through three timescale-separated loops: action-frequency governance, rollout-level critic-recovery proposal, and validation-gated skill updates. It also introduces Z-Infra, a rollout infrastructure that decouples agent logic from heterogeneous execution resources, and learned skills transfer zero-shot with emergent robotic 'Aha Moments'.

huggingface_papers · Hugging Face Papers · Aug 20, 00:00

**Background**: Embodied agents often rely on end-to-end policy models, but agentic systems have struggled to achieve closed-loop learning during physical execution. Traditional harnesses are open-loop, following fixed skills and reflecting only after episodes, which cannot adapt to rapidly changing robot-environment states. Zetta addresses this by evolving runtime critics and recovery skills online, enabling real-time governance of physical actions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2608.16590">Zetta ζ: An Efficient Closed - Loop Embodied Harness for...</a></li>
<li><a href="https://huggingface.co/papers/2608.16590">Paper page - Zetta ζ: An Efficient Closed- Loop Embodied Harness for...</a></li>
<li><a href="https://www.alphaxiv.org/abs/2608.16590">Zetta $ζ$: An Efficient Closed- Loop Embodied Harness for... | alphaXiv</a></li>

</ul>
</details>

**Tags**: `#embodied AI`, `#robotics`, `#closed-loop learning`, `#agentic systems`, `#physical intelligence`

---

<a id="item-4"></a>
## [Simulation in AI: 10% Worse, 100x Cheaper, 10000x Faster](https://www.latent.space/p/ainews-10-worse-100x-cheaper-10000x) ⭐️ 8.0/10

The article highlights a growing trend where simulation is replacing real-world data collection in AI development, claiming it is only 10% worse in performance but 100x cheaper and 10000x faster. This approach is being applied across robotics, biology, and other fields, with examples like World Labs' Real-to-Sim-to-Real pipeline and CZ Biohub's virtual cell project. This shift could dramatically reduce the cost and time required for AI training and experimentation, making AI development more accessible and accelerating innovation. It also raises questions about the trade-offs between simulation fidelity and real-world performance, impacting industries that rely on physical data. The article cites specific examples: Poolside's 'reverse-execuhire' letter distinguishes intelligence-bound problems from experiment-bound ones, and CZ Biohub is imaging the Human Cell Atlas into a virtual cell, claiming in silico is roughly 1000x cheaper and faster than in vivo. World Labs' R2S2R pipeline enables faster and cheaper iteration for robot training.

rss · Latent Space · Aug 22, 07:36

**Background**: Simulation in AI involves creating virtual environments to train models, which can be cheaper and faster than collecting real-world data. Techniques like sim-to-real transfer aim to bridge the gap between simulated and real environments. The trend is driven by advances in generative AI and physics-based simulators, enabling more realistic and scalable simulations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.latent.space/p/ainews-10-worse-100x-cheaper-10000x">[AINews] 10% worse, 100x cheaper, 10000x faster: Why Simulation is taking over</a></li>
<li><a href="https://www.worldlabs.ai/blog/real-to-sim-to-real">Building Worlds That Train Robots | World Labs</a></li>
<li><a href="https://aws.amazon.com/blogs/physical-ai/sim-to-real-and-real-to-sim-the-engine-behind-capable-physical-ai/">Sim-to-Real and Real-to-Sim: The Engine Behind Capable Physical AI | AWS Physical AI Blog</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Simulation`, `#Machine Learning`, `#Cost Efficiency`, `#Trends`

---

<a id="item-5"></a>
## [Claude's Invisible Watermarking Explained in Video Walkthrough](https://magazine.sebastianraschka.com/p/claude-watermarking) ⭐️ 8.0/10

Sebastian Raschka published a 48-minute video walkthrough explaining how Anthropic's Claude models watermark AI-generated text, covering token sampling, watermark detection, and potential removal methods. The video follows Anthropic's recent announcement that they will watermark Claude's text outputs. This analysis is significant because AI watermarking is a critical tool for AI safety and provenance, helping to identify AI-generated content and align with regulations like the EU's transparency rules. The video provides technical depth that helps developers and researchers understand and potentially implement or counteract such watermarks. The video focuses on token sampling, which is the core mechanism where watermarks are embedded by subtly biasing the selection of tokens during generation. It also discusses detection methods and potential removal techniques, though the video format may limit the depth of coverage.

rss · Sebastian Raschka · Aug 22, 11:11

**Background**: Large language models (LLMs) generate text autoregressively by assigning probabilities to tokens and sampling the next token based on those probabilities. Watermarking techniques, such as those used by Claude, embed a statistical pattern using a secret key without altering the text's appearance or quality, enabling later detection of AI involvement. This approach aligns with growing demands for transparency in AI-generated content.

<details><summary>References</summary>
<ul>
<li><a href="https://magazine.sebastianraschka.com/p/claude-watermarking">How Claude Watermarks AI -Generated Text</a></li>
<li><a href="https://overcentral.com/en/claude-invisible-text-watermark/">Anthropic Reveals Claude 's Invisible Text Watermarking Technique</a></li>
<li><a href="https://smartcr.org/ai-technologies/generative-ai/understanding-claude-s-text-watermarking-technique-in-artificial-intelligence/">Understanding Claude ’s Text Watermarking Technique In... - SmartCR</a></li>

</ul>
</details>

**Tags**: `#AI watermarking`, `#Claude`, `#LLM`, `#AI safety`, `#token sampling`

---

<a id="item-6"></a>
## [DFlash 2 in llama.cpp: 2.26x Speedup on Real Coding Tasks](https://www.reddit.com/r/LocalLLaMA/comments/1vvncyh/i_benchmark_dflash_2_pr_build_in_llamacpp_on_qwen/) ⭐️ 8.0/10

A user benchmarked the DFlash 2 speculative decoding method in llama.cpp on Qwen 3.8 27B, reporting a 2.26x speedup on 100 real LiveCodeBench problems (67.97 to 153.91 tok/s) and up to 4.68x when combined with an n-gram drafter. The results show DFlash 2 outperforms DFlash 1 at matched draft width with half the VRAM cost. This benchmark provides independent validation of DFlash 2's effectiveness on real coding workloads, showing significant speedups that could reduce inference costs and latency for LLM serving. The findings also highlight the nuanced interaction between DFlash 2 and n-gram drafters, which is valuable for optimizing speculative decoding configurations. The benchmark used an RTX PRO 6000 GPU with concurrency 1, and DFlash 2 alone achieved 2.26x on LiveCodeBench, while adding one n-gram lookup table (ngram-map-k4v) gave 4.68x on an 18-turn coding session, but adding a second table made it slower (3.77x). The recommended --spec-draft-n-max 7 was past the peak; 5 gave ~11% more on 8K coding prompts, and --spec-draft-p-min does nothing on DFlash 2.

reddit · r/LocalLLaMA · /u/FantasticNature7590 · Aug 22, 20:41

**Background**: Speculative decoding is a technique that uses a small draft model to predict multiple future tokens, which the main model then verifies in parallel, speeding up inference without quality loss. DFlash 2 is a block diffusion model designed for speculative decoding, and llama.cpp is a popular open-source LLM inference engine. The benchmark compares DFlash 2 against plain decoding, MTP, and n-gram drafters, providing insights into when each method is most effective.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/">The next generation of speculative decoding: DFlash and Spec V2 - LMSYS Org</a></li>
<li><a href="https://github.com/z-lab/dflash">GitHub - z-lab/dflash: DFlash: Block Diffusion for Flash Speculative Decoding · GitHub</a></li>
<li><a href="https://www.mindstudio.ai/blog/dflash-2-speculative-decoding-qwen">DFlash 2: Run Qwen3.8-27B at 2x Speed with Speculative Decoding | MindStudio</a></li>

</ul>
</details>

**Tags**: `#speculative decoding`, `#llama.cpp`, `#benchmark`, `#LLM inference`, `#DFlash`

---

<a id="item-7"></a>
## [RTX 5090 Runs Qwen3.8-27B at 262K Context with 77 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1vvl7pc/single_rtx_5090_qwen3827b_nvfp4_at_a_real_262k/) ⭐️ 8.0/10

A Reddit user published a detailed guide and benchmark showing Qwen3.8-27B (NVFP4 quantized) running on a single RTX 5090 with a full 262,144-token context, achieving 77.2 tok/s decode speed for short contexts and 64.7 tok/s with 128K tokens resident. This demonstrates that a 27B-parameter model with a massive 262K context window can run on consumer hardware with usable performance, potentially enabling long-context applications like agentic workflows and document analysis on local machines. It also highlights the growing capability of consumer GPUs and efficient quantization techniques. The setup uses vLLM 0.27.1 with NVFP4 quantization, a hybrid model with 48 Gated DeltaNet layers and 16 full-attention layers, and retains the vision tower and MTP head. Prefix caching showed a 22.3x speedup for cached TTFT, but vLLM places the hybrid cache in experimental align mode, which may cause corrupted output; disabling prefix caching is the first troubleshooting step.

reddit · r/LocalLLaMA · /u/Fz1zz · Aug 22, 19:16

**Background**: NVFP4 is NVIDIA's 4-bit floating-point format for Blackwell GPUs, designed to reduce memory usage while maintaining accuracy. Gated DeltaNet is a linear-attention layer used in Qwen3-Next, offering efficient long-context handling. MTP (Multi-Token Prediction) heads allow the model to predict multiple future tokens, improving inference speed. These technologies enable running large models on consumer hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision Inference | NVIDIA Technical Blog</a></li>
<li><a href="https://arxiv.org/abs/2412.06464">[2412.06464] Gated Delta Networks: Improving Mamba2 with Delta Rule</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/mtp/">Multi-Token Prediction (MTP) | Sebastian Raschka, PhD</a></li>

</ul>
</details>

**Discussion**: Community comments express enthusiasm about the model's quality and performance, with one user noting it is 'not-dumb' on a MacBook Pro, another saying a 4-bit quant is indistinguishable from Gemini 3.7 flash in internal tests, and a third praising the control over model quality compared to cloud providers. Some users prefer higher precision quantizations for accuracy, while others highlight the practical benefits of running uncensored models locally.

**Tags**: `#LLM`, `#RTX 5090`, `#vLLM`, `#Qwen`, `#NVFP4`

---

<a id="item-8"></a>
## [Developer Trains 250M LLM from Scratch, Quantizes to 60 MB with Disk-Based Long Context](https://www.reddit.com/r/MachineLearning/comments/1vv2nkh/i_developed_my_own_quantized_llm_from_scratch/) ⭐️ 8.0/10

A developer trained a 250M parameter LLM from scratch on 30B tokens of fineweb, quantized it to under 2 bits per weight, resulting in a 60 MB deployment that runs at 400 tok/s on a laptop CPU. The model also features a novel disk-based long-context mechanism that compresses older tokens to 1 bit and supports retrieval from up to 100M tokens of history. This achievement demonstrates that highly compressed LLMs can be deployed on resource-constrained devices without GPUs, potentially enabling on-device AI applications. The disk-based long-context approach offers a scalable alternative to traditional KV cache memory, addressing a major bottleneck in handling very long sequences. The model uses a fixed 512-bit code for each of its 131k tokens, eliminating the need for a trained embedding table. The long-context mechanism keeps the most recent 2048 tokens in fp16, while older tokens are compressed to 1 bit and stored on disk at about 320 bytes per token, enabling 1M tokens of history in roughly 320 MB. The base model achieves a perplexity of 23.3 on held-out English web text, and the vocabulary table scores 0.619 Spearman correlation on WordSim-353, compared to 0.029 for random codes.

reddit · r/MachineLearning · /u/Final-Data-1410 · Aug 22, 04:39

**Background**: Quantization reduces the precision of model weights to lower bit widths, such as 8-bit or 4-bit, to decrease memory footprint and computational cost. Recent research shows that low-bit quantization (e.g., under 2 bits) tends to favor undertrained LLMs, which aligns with this model's training on a relatively small token budget. Traditional long-context handling relies on storing the KV cache in memory, which scales linearly with sequence length and becomes impractical for millions of tokens; disk-based approaches offload this data to storage, enabling much longer contexts at the cost of retrieval latency.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2411.17691v2">Low-Bit Quantization Favors Undertrained LLMs: Scaling Laws ...</a></li>
<li><a href="https://arxiv.org/html/2606.26105v1">Context Recycling for Long-Horizon LLM Inference A Hierarchical Memory Architecture for Managing Fixed Context Budgets Across Unbounded Sessions</a></li>
<li><a href="https://sampathkumaran.medium.com/llms-simplified-tokens-and-embeddings-f275e6ce016e">LLM’s Simplified — Tokens and Embeddings | by Sampath Kumaran Ganesan | Medium</a></li>

</ul>
</details>

**Discussion**: The community response has been overwhelmingly positive and curious, with the author expressing gratitude for the lack of roasting and noting the repo has reached 7 stars. Commenters are likely intrigued by the technical novelty, particularly the disk-based retrieval and fixed token codes, and may ask for more details on training and quantization methods.

**Tags**: `#LLM`, `#quantization`, `#efficient inference`, `#long context`, `#model compression`

---

<a id="item-9"></a>
## [Single Attention Head Ablation Makes Chess Transformer Miss Queen Sacrifice](https://www.reddit.com/r/MachineLearning/comments/1vvsf5b/ablating_1_of_a_chess_transformers_128_attention/) ⭐️ 8.0/10

Researchers found that ablating one of the 128 attention heads in the Maia-3 chess transformer causes the model to fail to find the famous queen sacrifice in a well-known game. This was discovered using the chessformer_lens interpretability library. This finding highlights that individual attention heads can encode highly specific strategic behaviors, advancing mechanistic interpretability of transformers. It could influence how we debug and understand complex models beyond chess, potentially improving model reliability and safety. The ablated head is one of 128 in the Maia-3 23M model, and the ablation was performed using the chessformer_lens library (DOI: 10.5281/zenodo.21986988). The specific head's role appears to be crucial for recognizing the queen sacrifice pattern, suggesting a high degree of specialization.

reddit · r/MachineLearning · /u/Weird-Asparagus4136 · Aug 23, 00:22

**Background**: Maia-3 is a family of transformer-based chess models designed to predict human moves across skill levels. The chessformer_lens library is a toolkit for mechanistic interpretability of such models, allowing researchers to inspect attention patterns and ablate components. Attention head ablation is a common technique to assess the importance of individual heads by setting their outputs to zero and measuring performance changes.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/CSSLab/maia3">GitHub - CSSLab/maia3: Maia-3 is the most accurate and efficient human chess move prediction engine. · GitHub</a></li>
<li><a href="https://github.com/chessformer-lens/chessformer_lens">GitHub - chessformer-lens/chessformer_lens: A toolkit ...</a></li>
<li><a href="https://huggingface.co/UofTCSSLab/Maia3-79M">UofTCSSLab/Maia3-79M · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#interpretability`, `#transformers`, `#chess`, `#mechanistic interpretability`, `#attention heads`

---

<a id="item-10"></a>
## [DelveRL: Open-Source Roguelike for Training Game-Playing Agents](https://www.reddit.com/r/MachineLearning/comments/1vvii1j/i_built_an_opensource_roguelike_specifically_for/) ⭐️ 8.0/10

The author released DelveRL, an open-source roguelike game designed specifically for training reinforcement learning agents, featuring a structured API, deterministic simulation, procedural levels, partial observability, and a recurrent PPO baseline that reaches a median floor of 18 and up to floor 33. This addresses a practical gap in RL research by providing a human-playable game environment that is easy to integrate with agent harnesses, potentially accelerating research in areas like exploration, partial observability, and long-horizon decision-making. It offers a standardized benchmark for comparing agent algorithms. The game is an endless turn-based roguelike where agents must explore, manage resources, fight enemies, and escape each floor. It includes batched renderer-free environments and a recurrent PPO trainer, with all code, checkpoints, documentation, and benchmarks open-sourced.

reddit · r/MachineLearning · /u/SnyderConsulting · Aug 22, 17:32

**Background**: Roguelikes are a genre of games characterized by procedural level generation and permadeath, offering rich challenges for AI agents. Reinforcement learning (RL) trains agents through trial and error, and environments like OpenAI Gym are commonly used, but many games are difficult to integrate with RL frameworks. DelveRL aims to bridge this gap by providing a purpose-built environment with features like partial observability, which is common in real-world scenarios.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Delver_(video_game)">Delver - Wikipedia</a></li>
<li><a href="https://stable-baselines.readthedocs.io/">Welcome to Stable Baselines docs! - RL Baselines Made Easy...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Partially_observable_system">Partially observable system - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#open-source`, `#game environment`, `#AI training`, `#procedural generation`

---

<a id="item-11"></a>
## [Evaluation Resolution Artifact Undermines Untrained CNN Brain-Likeness Claims](https://www.reddit.com/r/MachineLearning/comments/1vvdxwt/the_evaluation_resolution_has_been_shown_to_have/) ⭐️ 8.0/10

A new preprint demonstrates that the apparent superiority of untrained CNNs over trained ones in matching V1 brain activity is an artifact of evaluation resolution. The study shows the backpropagation vs. untrained V1 gap varies non-monotonically with image resolution, from -0.001±0.007 at 32px to +0.044±0.006 at 224px. This finding challenges a widely cited claim in computational neuroscience and highlights the critical role of evaluation methodology in model-brain comparisons. It could lead to more rigorous standards for such comparisons, affecting researchers in both machine learning and neuroscience. The study used a small CNN trained on a CIFAR-10 subset at 32px, five learning rules (random init, backprop, feedback alignment, predictive coding, STDP), and evaluated on THINGS-fMRI stimuli at six resolutions from 32px to 224px. They ruled out several potential confounds, including train/eval resolution mismatch and batch-norm issues, and found that the backprop > untrained effect at LOC persists across all resolutions.

reddit · r/MachineLearning · /u/ConfusionSpiritual19 · Aug 22, 14:30

**Background**: Model-brain comparison studies often use representational similarity analysis (RSA) to compare activations of artificial neural networks to brain activity. A common claim is that untrained CNNs can match or surpass trained CNNs at early visual cortex (V1), suggesting that learning rules like backpropagation may not be necessary for brain-like representations. This study investigates whether such conclusions are robust to evaluation resolution, a methodological factor often overlooked.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Spike-timing-dependent_plasticity">Spike-timing-dependent plasticity - Wikipedia</a></li>
<li><a href="https://towardsdatascience.com/feedback-alignment-methods-7e6c41446e36/">Feedback Alignment Methods - Towards Data Science</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is not provided, but the author's note invites feedback on the framing of receptive-field matching, indicating openness to critique. The community likely appreciates the methodological rigor and the correction of earlier preprints.

**Tags**: `#neuroscience`, `#CNN`, `#evaluation`, `#brain-comparison`, `#RSA`

---

<a id="item-12"></a>
## [UBS Projects $4.1T AI Infrastructure Spend by 2028, But Grid Queue Looms](https://www.reddit.com/r/artificial/comments/1vvfxyq/ubs_models_41t_in_ai_infrastructure_spending_by/) ⭐️ 8.0/10

UBS has modeled that AI infrastructure spending will reach $4.1 trillion by 2028, but the analysis highlights that grid interconnection queues, not chip supply, are becoming the harder bottleneck. Recent actions by the Tennessee Valley Authority, Denmark's grid operator, and PJM illustrate the growing strain on power interconnection. This matters because it shifts the focus from chip supply to power infrastructure as the critical constraint on AI expansion. If grid interconnection delays persist, they could slow AI data center deployments and affect the broader tech industry's growth plans. The Tennessee Valley Authority created a new rate class specifically for AI data centers, Denmark's grid operator began prioritizing other demand categories over new data center interconnection requests, and PJM's board overruled its own stakeholder vote on curtailment rules. These events indicate that the queue problem is worsening, and $4.1 trillion in spending assumes power will be available when needed.

reddit · r/artificial · /u/Servola-Journal · Aug 22, 15:51

**Background**: Grid interconnection is the process of connecting new power generation or load to the electric grid, which requires impact studies and can take years due to queue backlogs. Unlike chip shortages, which are supply problems that eventually resolve, interconnection is a queue problem where projects must wait in line, and paying more cannot expedite the process. The UBS forecast of $4.1 trillion in AI infrastructure spending by 2028 includes data centers, but the power supply assumptions may be optimistic given current grid constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://www.interconnection.fyi/">Latest Interconnection Queue Requests with daily data updates ...</a></li>
<li><a href="https://emp.lbl.gov/queues">Queued Up: Characteristics of Power Plants Seeking ...</a></li>
<li><a href="https://www.unite.ai/tva-board-creates-data-center-rate-to-shield-households-from-ai-power-costs/">TVA Board Creates Data Center Rate to Shield Households From AI ...</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely includes comments from users with utility or regulatory experience, debating whether interconnection is indeed the binding constraint compared to chips and cooling. Some may argue that the issue is overstated, while others may share firsthand experiences of queue delays.

**Tags**: `#AI infrastructure`, `#energy grid`, `#data centers`, `#bottlenecks`, `#policy`

---

<a id="item-13"></a>
## [NousResearch's Hermes Agent: Self-Improving AI Agent Goes Viral on GitHub](https://github.com/NousResearch/hermes-agent) ⭐️ 8.0/10

NousResearch's hermes-agent repository has gained 443 stars in a single day, reaching a total of 234,404 stars and 47,168 forks. The project is an open-source, self-hosted AI agent that features persistent memory, self-created skills, and multi-platform messaging integration. This rapid star growth indicates strong community interest in self-improving AI agents, a key trend in the AI/ML ecosystem. The project's open-source nature and multi-platform support could make it a foundational tool for developers building personalized AI assistants. Hermes Agent supports multiple LLM providers including OpenAI, Anthropic, Google, xAI, and Nous Portal, and integrates with 24 chat platforms such as Telegram, Discord, and Slack. It ships with over 80 pre-built skills and can run scheduled jobs via cron, operating from terminal, dashboard, GitHub workflows, and messaging channels.

github_trending · GitHub Trending · Aug 23, 01:32

**Background**: AI agents are software programs that autonomously perform tasks using large language models (LLMs). Hermes Agent is designed to 'grow with you' by maintaining persistent memory across sessions and creating new skills based on user interactions, distinguishing it from simple chatbots. The project is built by Nous Research, known for the Hermes model family, and is licensed under MIT.

<details><summary>References</summary>
<ul>
<li><a href="https://hermes-agent.nousresearch.com/">Hermes Agent — Open-Source AI Agent That... | Nous Research</a></li>
<li><a href="https://github.com/nousresearch/hermes-agent">GitHub - NousResearch / hermes - agent : The agent that grows with you</a></li>
<li><a href="https://hermesagents.net/">Hermes Agent : The AI That Grows With You</a></li>

</ul>
</details>

**Tags**: `#AI agent`, `#Python`, `#GitHub trending`, `#NousResearch`, `#open source`

---

<a id="item-14"></a>
## [ECC: Agent Harness Performance Optimization System Gains Traction](https://github.com/affaan-m/ECC) ⭐️ 8.0/10

The GitHub repository affaan-m/ECC, a JavaScript-based agent harness performance optimization system, has gained 411 stars today and 242,176 total stars, with 36,700 forks. It supports AI coding agents like Claude Code, Codex, Opencode, and Cursor. This system addresses the growing need for optimizing AI coding agent performance, which is critical as these agents become more integrated into development workflows. Its rapid popularity indicates a strong demand for tools that enhance agent efficiency, memory, and security across multiple platforms. ECC is described as a complete system including skills, instincts, memory optimization, continuous learning, security scanning, and research-first development. It is available via official channels such as the GitHub repository, npm packages (ecc-universal and ecc-agentshield), a GitHub App, and the project website ecc.tools.

github_trending · GitHub Trending · Aug 23, 01:32

**Background**: Agent harnesses are the frameworks that enable AI coding agents to interact with codebases, execute commands, and manage context. Optimizing these harnesses involves improving how agents learn from repository history, manage memory, and maintain security. ECC aims to turn a repository's actual working patterns into reusable guidance for AI agents, enhancing their performance and reliability.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/affaan-m/ECC">GitHub - affaan-m/ECC: The agent harness performance ...</a></li>
<li><a href="https://github.com/akashmehta10007/agent-harness-performance-optimization-system">akashmehta10007/agent-harness-performance-optimization-system</a></li>
<li><a href="https://arxiv.org/html/2602.22480v4">VeRO: A Harness for Agents to Optimize Agents - arXiv.org</a></li>

</ul>
</details>

**Tags**: `#AI`, `#developer-tools`, `#performance`, `#agent-harness`, `#JavaScript`

---

<a id="item-15"></a>
## [Tencent's AI-Infra-Guard: Full-Stack AI Red Teaming Platform](https://github.com/Tencent/AI-Infra-Guard) ⭐️ 8.0/10

Tencent has released AI-Infra-Guard, a comprehensive AI red teaming platform that scans and evaluates security across AI agents, skills, MCP, infrastructure, and LLM jailbreaks. The project has gained rapid traction, with 150 stars today and over 5,500 total stars. This platform addresses critical security gaps in the rapidly expanding AI ecosystem, offering a unified solution for diverse attack surfaces. Its broad coverage and high community interest suggest it could become a standard tool for AI security practitioners, influencing how organizations secure their AI deployments. The platform includes five scanning modules: Agent Scan, Skills Scan, MCP Scan, AI Infra Scan, and LLM jailbreak evaluation. It is written in Python and has 518 forks, indicating active community involvement.

github_trending · GitHub Trending · Aug 23, 01:32

**Background**: AI red teaming involves adversarially testing AI systems to uncover safety and security failures before deployment. As AI agents and MCP (Model Context Protocol) become more prevalent, new attack surfaces emerge, requiring specialized scanning tools. LLM jailbreak evaluation focuses on bypassing safety mechanisms through crafted prompts.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/cisco-ai-defense/mcp-scanner">GitHub - cisco-ai-defense/mcp-scanner: Scan MCP servers for potential threats & security findings. · GitHub</a></li>
<li><a href="https://jailbreakbench.github.io/">JailbreakBench: LLM robustness benchmark</a></li>
<li><a href="https://neuraltrust.ai/blog/best-ai-red-teaming-platforms">The 10 Best AI Red Teaming Platforms for Enterprise AI ... | NeuralTrust</a></li>

</ul>
</details>

**Tags**: `#AI Security`, `#Red Teaming`, `#LLM`, `#MCP`, `#DevOps`

---