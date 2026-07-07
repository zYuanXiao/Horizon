---
layout: default
title: "Horizon Summary: 2026-07-07 (EN)"
date: 2026-07-07
lang: en
---

> From 128 items, 15 important content pieces were selected

---

1. [Januscape: Critical KVM/x86 Guest-to-Host Escape](#item-1) ⭐️ 9.0/10
2. [Addy Osmani's Agent Skills: Production-Grade Skills for AI Coders](#item-2) ⭐️ 8.0/10
3. [Alibaba's Page-Agent: Natural Language GUI Control](#item-3) ⭐️ 8.0/10
4. [Monotonic Inference Policy Improvement for LLM RL](#item-4) ⭐️ 8.0/10
5. [Program-as-Weights: Compiling Fuzzy Functions into Neural Artifacts](#item-5) ⭐️ 8.0/10
6. [Kani: A Bit-Precise Model Checker for Rust](#item-6) ⭐️ 8.0/10
7. [Pulpie: 20x Cheaper Web Content Extraction Models](#item-7) ⭐️ 8.0/10
8. [Tencent Releases Hy3: 295B MoE Model with Apache 2.0](#item-8) ⭐️ 8.0/10
9. [Secret Claude tracker contradicts Anthropic's anti-surveillance stance](#item-9) ⭐️ 8.0/10
10. [Kyutai's Pocket TTS clones voice from 5s audio on CPU](#item-10) ⭐️ 8.0/10
11. [Sberbank Releases GigaChat3.5-432B-A28B MoE Model with Day-0 GGUF Support](#item-11) ⭐️ 8.0/10
12. [OpenComputer: Open-Source VM for Safe AI Agents](#item-12) ⭐️ 8.0/10
13. [Ascent GX10 Runs Pruned 162B DeepSeek Model at 262k Context](#item-13) ⭐️ 8.0/10
14. [Krea 2 Node Adds Multi-LoRA with Bounding Box Control](#item-14) ⭐️ 8.0/10
15. [LingBot-Vision: Masked Boundary Modeling for SSL](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Januscape: Critical KVM/x86 Guest-to-Host Escape](https://github.com/V4bel/Januscape) ⭐️ 9.0/10

A use-after-free vulnerability in KVM/x86's shadow MMU emulation, tracked as CVE-2026-53359, allows a guest VM to escape to the host on both Intel and AMD systems. A proof-of-concept (PoC) exploit has been published, and a full escape exploit exists but is withheld for now. This vulnerability poses a severe risk to multi-tenant VM providers and sandboxed environments, as an attacker could break out of a guest VM and gain host-level access. It is the first publicly demonstrated KVM/x86 guest-to-host escape, following a similar arm64 escape (ITScape) discovered earlier. The vulnerability has existed since 2008 and affects both Intel and AMD x86 hosts. Disabling nested virtualization in the host OS or BIOS makes the system immune to this specific bug.

hackernews · Imustaskforhelp · Jul 6, 17:35 · [Discussion](https://news.ycombinator.com/item?id=48807908)

**Background**: KVM (Kernel-based Virtual Machine) is a Linux kernel module that turns the host into a hypervisor, allowing multiple VMs to run. The shadow MMU is used for memory virtualization when hardware-assisted paging (e.g., Intel EPT, AMD NPT) is unavailable or disabled. Nested virtualization allows a VM to run its own hypervisor and further VMs inside it, increasing complexity and attack surface.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html">16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems</a></li>
<li><a href="https://lobste.rs/s/jea4xl/januscape_guest_host_escape_kvm_x86">Januscape: Guest-to-Host Escape in KVM/x86 | Lobsters</a></li>
<li><a href="https://lowendtalk.com/discussion/218905/januscape-guest-to-host-escape-in-kvm-x86-cve-2026-53359">Januscape: Guest-to-Host Escape in KVM/x86 (CVE-2026-53359) — LowEndTalk</a></li>

</ul>
</details>

**Discussion**: Commenters noted that nested virtualization adds significant complexity and historical flakiness, making it inadvisable for public VM hosts. Some questioned why /dev/kvm is world-writable on distributions like RHEL, enabling unprivileged local privilege escalation. Others confirmed that disabling nested virtualization mitigates the bug.

**Tags**: `#security`, `#virtualization`, `#KVM`, `#CVE`, `#x86`

---

<a id="item-2"></a>
## [Addy Osmani's Agent Skills: Production-Grade Skills for AI Coders](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

Addy Osmani released an open-source repository called agent-skills, a curated collection of 20 production-grade engineering skills designed to enhance AI coding agents' capabilities. The repository gained over 1,112 stars in a single day, reaching over 70,000 total stars. This repository addresses a critical need in AI-assisted software engineering by providing structured, best-practice workflows that guide AI coding agents to produce higher-quality code. It has the potential to significantly improve the reliability and effectiveness of AI coding tools, benefiting developers and teams adopting AI in their workflows. The skills cover areas such as core engineering, AI/ML/data, and professional tools, encoding workflows, quality gates, and best practices that senior engineers use. The repository is written in JavaScript and is available on GitHub under the MIT license.

github_trending · GitHub Trending · Jul 7, 03:30

**Background**: AI coding agents, such as Cursor and Zencoder, are tools that assist developers by generating, reviewing, and debugging code. However, without proper guidance, these agents may produce code that lacks production-grade quality. Agent Skills aims to fill this gap by providing a library of reusable, expert-level skills that agents can leverage to follow industry best practices.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/addyosmani/agent-skills">GitHub - addyosmani/agent- skills : Production - grade engineering ...</a></li>
<li><a href="https://www.everydev.ai/tools/addy-osmani-agent-skills">Addy Osmani Agent Skills - Skill Library by Addy Osmani | EveryDev.ai</a></li>

</ul>
</details>

**Tags**: `#AI`, `#coding agents`, `#software engineering`, `#GitHub trending`

---

<a id="item-3"></a>
## [Alibaba's Page-Agent: Natural Language GUI Control](https://github.com/alibaba/page-agent) ⭐️ 8.0/10

Alibaba has open-sourced Page-Agent, a TypeScript library that allows users to control web interfaces using natural language commands, gaining 892 stars on GitHub in a single day. This tool democratizes web automation by enabling non-technical users to interact with websites through plain language, potentially transforming how businesses build AI-native web applications. Page-Agent is an in-page GUI agent that can be integrated via a single script tag or npm package, supporting multi-page browsing and browser control through a Chrome extension.

github_trending · GitHub Trending · Jul 7, 03:31

**Background**: GUI automation traditionally requires scripting or programming knowledge. Page-Agent leverages AI to interpret natural language and perform actions like clicks, form fills, and navigation directly in the browser.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/alibaba/page-agent">GitHub - alibaba/page- agent : JavaScript in - page GUI agent .</a></li>
<li><a href="https://alibaba.github.io/page-agent/">PageAgent - The GUI Agent Living in Your Webpage</a></li>
<li><a href="https://emelia.io/hub/page-agent-alibaba">Page - Agent : Alibaba 's Open Source AI Web Copilot</a></li>

</ul>
</details>

**Tags**: `#GUI automation`, `#natural language`, `#TypeScript`, `#web agent`, `#open source`

---

<a id="item-4"></a>
## [Monotonic Inference Policy Improvement for LLM RL](https://huggingface.co/papers/2606.29526) ⭐️ 8.0/10

Researchers propose Monotonic Inference Policy Improvement (MIPI), a new objective for LLM reinforcement learning that ensures policy improvements during training translate to the inference phase, addressing training-inference mismatch. This work tackles a fundamental instability in LLM RL fine-tuning, which is critical for reliable deployment of reasoning models like those used in chat and code generation. The framework, Monotonic Inference Policy Update (MIPU), uses a two-step process: constructing sampler-referenced candidate updates and selectively accepting them based on an inference-side gap proxy. Experiments show improved reasoning performance and training stability under high mismatch conditions.

huggingface_papers · Hugging Face Papers · Jul 6, 00:00

**Background**: Reinforcement learning (RL) is used to fine-tune large language models (LLMs) for tasks like reasoning. However, LLMs often use separate engines for training and inference, leading to inconsistent probability distributions even with identical model parameters—a phenomenon called training-inference mismatch. This mismatch introduces off-policyness that can destabilize training.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/papers/2606.29526">Paper page - The Mirage of Optimizing Training Policies : Monotonic ...</a></li>
<li><a href="https://arxiv.org/pdf/2606.29526">The Mirage of Optimizing Training Policies : Monotonic Inference ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#reinforcement learning`, `#policy optimization`, `#training stability`

---

<a id="item-5"></a>
## [Program-as-Weights: Compiling Fuzzy Functions into Neural Artifacts](https://huggingface.co/papers/2607.02512) ⭐️ 8.0/10

Researchers propose fuzzy-function programming, instantiated as Program-as-Weights (PAW), where a 4B compiler trained on FuzzyBench generates parameter-efficient adapters for a frozen 0.6B interpreter, enabling local execution of natural-language-defined functions. PAW matches the performance of a 32B model while using 1/50th of the inference memory and running at 30 tokens/s on a MacBook M3, potentially enabling efficient, local AI deployment for tasks that previously required large API calls. The compiler is a 4B model that emits LoRA-like adapters for a frozen 0.6B Qwen3 interpreter, and the FuzzyBench dataset contains 10 million examples for training. The paradigm reframes foundation models as tool builders rather than per-input solvers.

huggingface_papers · Hugging Face Papers · Jul 3, 00:00

**Background**: Many programming tasks like log filtering or ranking are hard to specify with exact rules and are often outsourced to large language model APIs, which incurs latency, cost, and reproducibility issues. Fuzzy-function programming aims to compile natural language specifications into compact neural artifacts that run locally, combining the flexibility of LLMs with the efficiency of traditional programs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.02512">[2607.02512] Program-as-Weights: A Programming Paradigm for Fuzzy Functions</a></li>
<li><a href="https://huggingface.co/papers/2607.02512">Paper page - Program-as-Weights: A Programming Paradigm for Fuzzy Functions</a></li>

</ul>
</details>

**Tags**: `#programming paradigms`, `#neural compilation`, `#efficient inference`, `#NLP`, `#parameter-efficient fine-tuning`

---

<a id="item-6"></a>
## [Kani: A Bit-Precise Model Checker for Rust](https://arxiv.org/abs/2607.01504) ⭐️ 8.0/10

A new paper and tutorial have been released for Kani, an open-source bit-precise model checker for Rust programs. Kani helps Rust developers automatically verify safety and correctness properties, reducing undefined behavior and bugs in critical software. Kani uses CBMC as its backend and supports checking for panics, overflows, and other safety violations. The tutorial provides practical examples for getting started.

hackernews · Jimmc414 · Jul 6, 15:53 · [Discussion](https://news.ycombinator.com/item?id=48806410)

**Background**: Model checking is a formal verification technique that exhaustively explores program states to verify properties. Bit-precise model checking operates at the bit level, enabling precise reasoning about integer arithmetic and memory operations. Rust's safety guarantees make it a natural target for such verification tools.

<details><summary>References</summary>
<ul>
<li><a href="https://model-checking.github.io/kani/">Getting started - The Kani Rust Verifier</a></li>
<li><a href="https://github.com/model-checking/kani">GitHub - model - checking / kani : Kani Rust Verifier · GitHub</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the helpful tutorial and draw comparisons to similar tools like hypothesis-auto. References to prior work and related tools indicate active interest in Rust verification.

**Tags**: `#Rust`, `#model checking`, `#formal verification`, `#software engineering`

---

<a id="item-7"></a>
## [Pulpie: 20x Cheaper Web Content Extraction Models](https://usefeyn.com/blog/pulpie-pareto-optimal-models-for-cleaning-the-web/) ⭐️ 8.0/10

Feyn launched Pulpie, a family of Pareto-optimal encoder models that strip boilerplate from raw HTML, matching state-of-the-art extraction quality at 20x lower cost. Cleaning 1 billion webpages costs $7,900 with Pulpie versus $159,000 with Dripper. This makes high-quality web content extraction affordable for large-scale AI training and data pipelines, reducing a major cost barrier. The encoder architecture shift could influence future designs in web scraping and document understanding. Pulpie models are encoders that run one forward pass over the full input HTML and label each block as boilerplate or content, while decoders like Dripper generate output token by token, making them memory-bound. Pulpie is compute-bound, allowing cheaper GPUs with relatively more compute to run it efficiently.

hackernews · snyy · Jul 6, 16:04 · [Discussion](https://news.ycombinator.com/item?id=48806575)

**Background**: Web content extraction, or boilerplate removal, is the task of isolating the main content from web pages by removing ads, navigation, and other non-essential elements. Traditional approaches include rule-based libraries like Boilerpipe and newer decoder-based neural models. Encoder models process entire inputs in parallel, while decoder models generate outputs sequentially, often requiring more memory bandwidth.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pareto_efficiency">Pareto efficiency - Wikipedia</a></li>
<li><a href="https://mbottoni.github.io/2024/07/21/llm-archs.html">Encoder vs Decoder vs EncoderDecoder Architectures</a></li>
<li><a href="https://michaelmisiewicz.com/posts/scraping-webpages-2022/">How to scrape webpages in 2022 and best ways to remove boilerplate | Michael Misiewicz</a></li>

</ul>
</details>

**Discussion**: Commenters expressed interest in specific use cases like e-commerce product scraping and handling images, tables, and shadow DOMs. Some noted UI issues on the Hugging Face demo with Mozilla and dark theme, but overall sentiment was positive and curious about capabilities.

**Tags**: `#web scraping`, `#machine learning`, `#NLP`, `#cost efficiency`, `#open source`

---

<a id="item-8"></a>
## [Tencent Releases Hy3: 295B MoE Model with Apache 2.0](https://simonwillison.net/2026/Jul/6/hy3/#atom-everything) ⭐️ 8.0/10

Tencent has released Hy3, a 295-billion-parameter Mixture-of-Experts (MoE) model with 21 billion active parameters, under the permissive Apache 2.0 license. The model outperforms similar-sized models and rivals flagship open-source models with 2-5x more parameters. Hy3's strong performance and Apache 2.0 license make it a significant addition to the open-source AI ecosystem, potentially accelerating research and applications. Its free availability on OpenRouter until July 21st lowers the barrier for developers and researchers to experiment with a state-of-the-art model. The full-precision Hy3 model is 598GB on Hugging Face, while an FP8 quantized version is 300GB. It supports a context length of 256K tokens and includes 3.8 billion MTP (Multi-Token Prediction) layer parameters.

rss · Simon Willison · Jul 6, 23:57

**Background**: Mixture-of-Experts (MoE) is a neural network architecture that uses multiple specialized sub-networks (experts) and a gating mechanism to activate only a subset of experts for each input, enabling large model capacity with lower computational cost. Multi-Token Prediction (MTP) is a training technique where the model predicts multiple future tokens simultaneously, improving efficiency and performance. FP8 quantization reduces model size and memory usage by representing weights and activations in 8-bit floating-point format.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://deepwiki.com/deepseek-ai/DeepSeek-V3/4.4-multi-token-prediction-(mtp)">Multi-Token Prediction ( MTP ) | deepseek-ai/DeepSeek-V3 | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#LLM`, `#MoE`, `#Tencent`

---

<a id="item-9"></a>
## [Secret Claude tracker contradicts Anthropic's anti-surveillance stance](https://arstechnica.com/tech-policy/2026/07/anthropic-outed-for-claude-tracker-that-secretly-monitored-chinese-users/) ⭐️ 8.0/10

Anthropic is accused of secretly tracking Chinese users via a tracker embedded in Claude Code, which an engineer confirmed was an experiment that has since ended. This controversy undermines user trust in Anthropic and raises serious questions about the company's commitment to privacy and its stated opposition to mass surveillance. The tracker was added to Claude Code in March 2026 as an experiment, according to Anthropic engineer Thariq Shihipar, and was discovered by users who reported it on social media.

rss · Ars Technica AI · Jul 6, 16:44

**Background**: Anthropic has publicly opposed mass surveillance, including refusing a Pentagon demand to allow Claude for 'all lawful purposes' due to surveillance concerns. The company's CEO Dario Amodei has cited worries about mass domestic surveillance and fully autonomous weapons.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/07/anthropic-outed-for-claude-tracker-that-secretly-monitored-chinese-users/">Secret Claude tracker shocks users after... - Ars Technica</a></li>
<li><a href="https://www.asapdrew.com/p/anthropic-ai-mass-surveillance">Anthropic 's "AI Mass Surveillance " Stand Doesn't Survive Scr...</a></li>
<li><a href="https://washingtonmonthly.com/2026/04/02/the-pentagons-orwellian-case-against-anthropic/">The Pentagon’s “Orwellian” Case Against Anthropic</a></li>

</ul>
</details>

**Discussion**: Users expressed shock and betrayal on social media, with many accusing Anthropic of hypocrisy. Some defended the company, suggesting the tracker might have been a benign usage measurement tool.

**Tags**: `#privacy`, `#AI ethics`, `#surveillance`, `#Anthropic`, `#Claude`

---

<a id="item-10"></a>
## [Kyutai's Pocket TTS clones voice from 5s audio on CPU](https://www.reddit.com/r/LocalLLaMA/comments/1up07mk/kyutais_pocket_tts_clones_a_voice_from_5_seconds/) ⭐️ 8.0/10

Kyutai released Pocket TTS, a ~100M parameter streaming language model that generates audio tokens via the Mimi neural codec, enabling zero-shot voice cloning from just 5 seconds of reference audio on CPU, under MIT license. This is the first CPU-friendly TTS model capable of zero-shot voice cloning, filling a gap where other models like Kokoro and Supertonic only offer fixed voice sets, making it ideal for interactive and privacy-sensitive applications. Pocket TTS achieves a flat real-time factor (RTF) of 0.69–0.76 across text lengths, streams audio token-by-token, and scored a UTMOS of 4.10 in benchmarks, though it is slower than some alternatives.

reddit · r/LocalLLaMA · /u/gvij · Jul 6, 15:14

**Background**: Traditional TTS systems use an acoustic model plus a vocoder, while Pocket TTS employs an autoregressive language model over the Mimi neural codec, which combines semantic and acoustic information into tokens at 12.5 Hz. RTF (real-time factor) measures how many seconds of compute are needed to generate one second of audio; lower is better. UTMOS is an objective neural metric that predicts Mean Opinion Score for speech quality.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/kyutai/mimi">kyutai/ mimi · Hugging Face</a></li>
<li><a href="https://www.emergentmind.com/topics/utmos-score">UTMOS Score : Neural MOS Evaluation</a></li>
<li><a href="https://huggingface.co/datasets/Jarbas/ovos-tts-bench">Jarbas/ovos- tts -bench · Datasets at Hugging Face</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion highlights the novelty of Pocket TTS's architecture and its unique voice cloning capability on CPU, with users expressing interest in testing it on accented English and non-English voices. Some note its slower speed but agree it is the most interesting model in the field.

**Tags**: `#TTS`, `#voice cloning`, `#machine learning`, `#open source`, `#benchmark`

---

<a id="item-11"></a>
## [Sberbank Releases GigaChat3.5-432B-A28B MoE Model with Day-0 GGUF Support](https://www.reddit.com/r/LocalLLaMA/comments/1uotkm7/new_model_gigachat35432ba28b_with_day0_gguf/) ⭐️ 8.0/10

Sberbank has released GigaChat3.5-432B-A28B, a 432-billion-parameter Mixture-of-Experts (MoE) model, with immediate GGUF quantization support for local inference via llama.cpp. The GGUF versions are available on Hugging Face, and a pull request has been submitted to integrate support into the main llama.cpp branch. This release is significant for the local LLM community as it enables immediate experimentation with a large MoE model on consumer hardware through quantization. It demonstrates a growing trend of major organizations supporting open-source local inference ecosystems like llama.cpp. The model has 432 billion total parameters but only 28 billion active parameters per token due to the MoE architecture, making it more efficient than a dense model of similar size. The GGUF format supports various quantization levels (e.g., 2-bit to 8-bit) to fit different hardware constraints.

reddit · r/LocalLLaMA · /u/unbannedfornothing · Jul 6, 10:34

**Background**: Mixture-of-Experts (MoE) is a model architecture that divides the network into multiple 'experts' and uses a gating mechanism to activate only a subset of experts for each input, reducing computational cost. GGUF is a file format for storing quantized model weights, optimized for inference with llama.cpp, a popular open-source library for running LLMs locally on CPUs and GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@mne/explaining-the-mixture-of-experts-moe-architecture-in-simple-terms-85de9d19ea73">Explaining the Mixture-of-Experts ( MoE ) Architecture in... | Medium</a></li>
<li><a href="https://huggingface.co/docs/diffusers/quantization/gguf">GGUF · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#GGUF`, `#open-source`, `#MoE`, `#local-inference`

---

<a id="item-12"></a>
## [OpenComputer: Open-Source VM for Safe AI Agents](https://www.reddit.com/r/LocalLLaMA/comments/1up6swc/opencomputer_an_open_source_computer_built_for/) ⭐️ 8.0/10

The AnythingLLM team released OpenComputer, an open-source, isolated VM environment designed for safe AI agent execution, allowing full PC control without risking the host system. OpenComputer addresses a critical safety and UX gap in agent systems by providing a human-accessible interface alongside agent automation, making powerful agent capabilities practical for non-technical users. The base image is ~3GB Debian 13.5 with XFCE4, each agent uses ~100MB, and inference is agnostic to the VM, supporting local, cloud, or server backends. It avoids screenshot-based navigation, using accessibility trees and CLI instead.

reddit · r/LocalLLaMA · /u/tcarambat · Jul 6, 19:01

**Background**: AI agents often require full system access to install apps and manipulate UI, posing security risks. Existing solutions like Docker sandboxes or Microsoft MXC isolate agents but lack a human-friendly interface. OpenComputer provides a full desktop environment that both humans and agents can use collaboratively.

<details><summary>References</summary>
<ul>
<li><a href="https://anythingllm.com/">AnythingLLM | The all-in-one AI application for everyone</a></li>
<li><a href="https://lmstudio.ai/models/gemma-4">Gemma 4</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#open source`, `#VM isolation`, `#agent safety`, `#LLM`

---

<a id="item-13"></a>
## [Ascent GX10 Runs Pruned 162B DeepSeek Model at 262k Context](https://www.reddit.com/r/LocalLLaMA/comments/1up6t50/got_my_ascent_gx10_two_days_ago_ran_reappruned/) ⭐️ 8.0/10

A user successfully ran a REAP-pruned NVFP4 DeepSeek-V4-Flash model (162B active parameters) on a single Ascent GX10 Spark, achieving consistent throughput at up to 262k context length. This demonstrates that pruned MoE models can run efficiently on compact, desktop-class AI supercomputers, potentially enabling local deployment of large-scale LLMs for research and development. The model is a 162B-parameter variant of DeepSeek-V4-Flash, pruned using REAP (Router-Weighted Activation Pruning) and quantized to NVFP4 precision. The Ascent GX10 is an NVIDIA DGX Spark-based personal AI supercomputer with a GB10 Superchip and 128GB LPDDR5x memory.

reddit · r/LocalLLaMA · /u/Dry-Tough-8068 · Jul 6, 19:01

**Background**: REAP is a pruning technique that removes less important experts in Mixture-of-Experts (MoE) models based on router weights and activation patterns, reducing model size while preserving performance. NVFP4 is a 4-bit floating-point precision format that further shrinks model footprint. The Ascent GX10 is a desktop AI supercomputer designed for local inference and development.

<details><summary>References</summary>
<ul>
<li><a href="https://www.candede.com/articles/advanced-llm-compression-reap/">Advanced LLM Compression: A Deep Dive into REAP</a></li>
<li><a href="https://www.localainews.co/news/multimodal/nemotron-3-nano-omni-30b-a3b-reasoning-nvfp4-opens-local-multimodal-ai/">Nemotron-3-Nano-Omni-30B-A3B-Reasoning- NVFP 4 Opens Local...</a></li>
<li><a href="https://www.amazon.ca/Supercomputer-Superchip-Supports-OpenClaw-Stackable/dp/B0G1MQYHRD/ref=zg_bs_g_677250011_d_sccl_24/134-7740804-6287904?psc=1">ASUS Ascent GX 10 AI Supercomputer, DGX Spark , NVIDIA GB10...</a></li>

</ul>
</details>

**Discussion**: The Reddit community praised the benchmark results and the custom Grafana dashboard, with some users discussing the trade-offs of pruning vs. merging experts. Others expressed interest in reproducibility and the potential of the Ascent GX10 for local LLM work.

**Tags**: `#hardware`, `#LLM inference`, `#pruning`, `#benchmarking`, `#long context`

---

<a id="item-14"></a>
## [Krea 2 Node Adds Multi-LoRA with Bounding Box Control](https://www.reddit.com/r/StableDiffusion/comments/1uotykv/i_created_a_node_for_krea2_that_adds_multilora/) ⭐️ 8.0/10

A custom node for Krea 2, called ComfyUI-Krea2-Regional-MultiLoRA, enables multi-LoRA support with per-region bounding box control, preventing identity bleeding by spatially isolating LoRA effects via activation-delta injection. This solves a long-standing problem in multi-character image generation where LoRA identities bleed into each other, enabling precise composition control similar to Ideogram 4. It allows users to place multiple characters, objects, and backgrounds in a single image without identity mixing. The node uses hard spatial masking (activation-delta injection) rather than attention bias, ensuring LoRA effects are strictly confined to their bounding boxes. It supports unlimited regions, auto-syncs region rows with drawn boxes, and is fp8-safe, running at Krea 2's native CFG 1.

reddit · r/StableDiffusion · /u/tekprodfx16 · Jul 6, 10:55

**Background**: LoRA (Low-Rank Adaptation) is a technique to fine-tune large models for specific concepts like characters or styles. In multi-LoRA generation, identity bleeding occurs when LoRA effects overlap, causing merged faces or averaged features. Krea 2 is an open-source image generation model that supports bounding-box layout control via its Qwen3-VL text encoder. Ideogram 4 introduced similar per-element bounding box prompting for precise composition.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/CliffNodes/Krea2-Multi-Character-Lora-Node-w-bounding-box-By-Fedor">GitHub - CliffNodes/ Krea 2 -Multi-Character-Lora-Node...</a></li>
<li><a href="https://happyin.space/image-generation/lora-identity-disentanglement-in-flux2-klein-9b/">LoRA Identity Disentanglement in... - Happyin Knowledge Space</a></li>
<li><a href="https://news.creeta.com/en/ideogram-4-json-layout-bounding-box-2026/">Ideogram 4 .0 JSON Layout & Bounding Box Control 2026</a></li>

</ul>
</details>

**Tags**: `#Stable Diffusion`, `#LoRA`, `#Krea 2`, `#image generation`, `#AI art`

---

<a id="item-15"></a>
## [LingBot-Vision: Masked Boundary Modeling for SSL](https://www.reddit.com/r/MachineLearning/comments/1up4cjh/lingbotvision_masked_boundary_modeling_for/) ⭐️ 8.0/10

LingBot-Vision introduces masked boundary modeling, where a teacher network predicts a dense boundary field and forces the student to reconstruct those boundary regions, achieving 0.296 RMSE on NYUv2 linear-probe depth estimation at 1.1B parameters, outperforming DINOv3-7B's 0.309. This work demonstrates that explicitly guiding self-supervised learning to focus on boundary regions can yield state-of-the-art dense prediction performance with significantly fewer parameters and data, challenging the scaling assumptions of models like DINOv3. The method uses per-pixel categorical distributions for boundary fields to avoid collapse, and applies an a-contrario validation test to decoded segments before supervision. The distilled ViT-L (0.3B) achieves 0.310 RMSE on NYUv2, comparable to DINOv3-7B, but trails on ImageNet and ADE20K.

reddit · r/MachineLearning · /u/StillThese3747 · Jul 6, 17:37

**Background**: Self-supervised learning (SSL) for vision often uses masked image modeling, where a model learns to reconstruct masked patches. DINOv3 is a leading SSL method that uses self-distillation and centering/sharpening to prevent collapse. Linear probing evaluates representation quality by training a linear classifier on frozen features.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2602.22701v1">BRepMAE: Self - Supervised Masked BRep Autoencoders for...</a></li>
<li><a href="https://deepwiki.com/nianticlabs/wavelet-monodepth/4.2-nyuv2-training-and-evaluation">NYUv 2 Training and Evaluation | DeepWiki</a></li>
<li><a href="https://arxiv.org/html/2603.14482">V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised...</a></li>

</ul>
</details>

**Discussion**: The community discussion is substantive, with the author noting that the 0.013 RMSE delta is within probe hyperparameter variability and that no ablation against hard-masking baselines (e.g., AttMask) is provided. Commenters also question whether boundary forcing is complementary to Gram anchoring used in DINOv3.

**Tags**: `#self-supervised learning`, `#computer vision`, `#pretraining`, `#boundary detection`, `#transformer`

---