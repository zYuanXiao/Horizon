---
layout: default
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 158 items, 15 important content pieces were selected

---

1. [EU Parliament Spyware Investigator Hacked with Pegasus](#item-1) ⭐️ 9.0/10
2. [Mistral Releases Leanstral-1.5 for Formal Verification](#item-2) ⭐️ 9.0/10
3. [Superpowers GitHub repo trends with agentic skills framework](#item-3) ⭐️ 8.0/10
4. [Agency-Agents: A Framework for Specialized AI Agents](#item-4) ⭐️ 8.0/10
5. [Program-as-Weights: Compiling NL into Compact Neural Artifacts](#item-5) ⭐️ 8.0/10
6. [AgenticSTS: Bounded-Memory Testbed for Long-Horizon LLM Agents](#item-6) ⭐️ 8.0/10
7. [Wordgard: New Rich-Text Editor from ProseMirror Creator](#item-7) ⭐️ 8.0/10
8. [PostgreSQL OOM Killer: Why Strict Memory Overcommit Matters](#item-8) ⭐️ 8.0/10
9. [Open Source AI Gap Map Launched](#item-9) ⭐️ 8.0/10
10. [HAT-4D: 4D Interactive Scenes from Monocular Video](#item-10) ⭐️ 8.0/10
11. [DeepSeek V4 Flash MoE Runs on RTX 5090 with Custom llama.cpp Fork](#item-11) ⭐️ 8.0/10
12. [CDD recovers finetuning data from LLM logits without weight access](#item-12) ⭐️ 8.0/10
13. [System Prompt Extraction Attack Works on 60-70% of AI Agents](#item-13) ⭐️ 8.0/10
14. [Elixir 1.2 Adds Gradual Set-Theoretic Types](#item-14) ⭐️ 8.0/10
15. [OmniRoute: Free AI Gateway with 230+ Providers](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [EU Parliament Spyware Investigator Hacked with Pegasus](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 9.0/10

Citizen Lab discovered that a member of the European Parliament's committee investigating spyware was infected with Pegasus spyware in October 2022 and again in March 2023. This indicates a state actor with cross-European authorization is targeting EU institutions, undermining democratic oversight and raising serious security concerns. The infections overlapped with a Pegasus campaign targeting Russian and Belarusian-speaking exiled journalists in Europe, suggesting a single customer with multi-country spying authorization.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is spyware developed by Israeli firm NSO Group, sold only to governments, capable of zero-click remote infection and full device takeover. Citizen Lab is a University of Toronto research group that investigates digital threats to human rights.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lzX2FQQ0VSR2FLSUx4NTNxVDB5Z0FQAQ?hl=en-GB&gl=GB&ceid=GB:en">Google News - News about spyware • EU • surveillance - Overview</a></li>

</ul>
</details>

**Discussion**: Commenters noted the irony of an investigator being spied on, and pointed to past Pegasus abuses in Greece, Poland, and Italy. Some questioned why the EU Parliament does not enforce separation of work and personal devices.

**Tags**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#European Parliament`, `#surveillance`

---

<a id="item-2"></a>
## [Mistral Releases Leanstral-1.5 for Formal Verification](https://www.reddit.com/r/LocalLLaMA/comments/1umgdhx/mistral_released_leanstral15119ba6b/) ⭐️ 9.0/10

Mistral has released Leanstral-1.5, a 6B active parameter model under Apache-2.0 license, achieving state-of-the-art results on formal verification benchmarks including miniF2F, PutnamBench, FATE-H, and FATE-X, and uncovering 5 real bugs across 57 repositories. This release marks a significant advancement in automated theorem proving and formal verification, making it easier for developers to verify software correctness and catch subtle bugs that traditional testing might miss, with an open-source license encouraging broad adoption. The model was trained using mid-training, supervised fine-tuning, and reinforcement learning with CISPO (Clipped Importance Sampling Policy Optimization), and it saturates the miniF2F benchmark, solves 587 out of 672 PutnamBench problems, and achieves 87% on FATE-H and 34% on FATE-X.

reddit · r/LocalLLaMA · /u/Tall-Ad-7742 · Jul 3, 14:44

**Background**: Formal verification uses mathematical proofs to ensure software correctness, and automated theorem proving aims to generate these proofs automatically. Benchmarks like miniF2F and PutnamBench evaluate models on competition-level math problems formalized in systems like Lean 4. CISPO is a reinforcement learning algorithm that clips importance sampling weights to improve stability and sample efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/miniF2F">GitHub - openai/miniF2F: Formal to Formal Mathematics Benchmark</a></li>
<li><a href="https://github.com/trishullab/PutnamBench">GitHub - trishullab/PutnamBench: An evaluation benchmark for undergraduate competition math in Lean4, Isabelle, Coq, and natural language. · GitHub</a></li>
<li><a href="https://www.emergentmind.com/topics/cispo-algorithm">CISPO: Clipped Importance Sampling RL - emergentmind.com</a></li>

</ul>
</details>

**Discussion**: Some commenters questioned the claim that the discovered bug would be missed by testing, noting it was a simple overflow edge case. Others pointed out that the model was compared to older models from half a year ago, which they found amusing. There was also curiosity about why Lean 4 was chosen over other formal verification tools like Isabelle/HOL.

**Tags**: `#AI`, `#formal verification`, `#Mistral`, `#theorem proving`, `#open-source`

---

<a id="item-3"></a>
## [Superpowers GitHub repo trends with agentic skills framework](https://github.com/obra/superpowers) ⭐️ 8.0/10

The GitHub repository obra/superpowers has gained over 1,200 stars in a single day, reaching nearly 246,000 total stars, as it introduces an agentic skills framework and software development methodology for coding agents. This methodology transforms AI coding assistants from simple code-writing tools into disciplined engineering partners, potentially improving software development efficiency and quality across the industry. Superpowers is a zero-dependency plugin that provides composable skills and initial instructions to guide coding agents, built by Jesse Vincent (@obra) at Prime Radiant.

github_trending · GitHub Trending · Jul 4, 03:16

**Background**: An agentic skills framework allows AI agents to discover and load portable packages of instructions, scripts, and resources on demand. This repository applies that concept to software development, offering a complete methodology for coding agents.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/obra/superpowers">GitHub - obra / superpowers : An agentic skills framework & software ...</a></li>
<li><a href="https://zread.ai/obra/superpowers">Overview | obra / superpowers | Zread</a></li>
<li><a href="https://ai-trove.com/en/superpowers">Superpowers — agentic skills framework & software</a></li>

</ul>
</details>

**Tags**: `#software-development`, `#methodology`, `#github-trending`, `#shell`

---

<a id="item-4"></a>
## [Agency-Agents: A Framework for Specialized AI Agents](https://github.com/msitarzewski/agency-agents) ⭐️ 8.0/10

The GitHub repository msitarzewski/agency-agents has gained over 1208 stars in a single day, reaching 126,558 total stars, offering a framework for creating specialized AI agents with distinct roles and deliverables. This framework enables developers to build modular AI agent systems where each agent has a unique personality and process, potentially streamlining complex multi-agent workflows and attracting strong community interest. The repository is written in Shell and has 20,539 forks; it describes agents as 'frontend wizards,' 'Reddit community ninjas,' and 'whimsy injectors,' emphasizing specialized expertise.

github_trending · GitHub Trending · Jul 4, 03:16

**Background**: AI agent frameworks provide building blocks for developing and managing autonomous AI agents. Multi-agent systems assign distinct roles to agents, mirroring human team structures to handle complex tasks collaboratively.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/agent-framework/overview/">Microsoft Agent Framework Overview | Microsoft Learn</a></li>
<li><a href="https://www.ibm.com/think/insights/top-ai-agent-frameworks">AI Agent Frameworks: Choosing the Right Foundation for Your Business | IBM</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#framework`, `#Shell`, `#open source`, `#tooling`

---

<a id="item-5"></a>
## [Program-as-Weights: Compiling NL into Compact Neural Artifacts](https://huggingface.co/papers/2607.02512) ⭐️ 8.0/10

Researchers propose Program-as-Weights (PAW), a paradigm that compiles natural-language specifications into compact neural artifacts using a 4B compiler and a 0.6B interpreter, matching the performance of a 32B model while using 1/50th of the inference memory and running at 30 tokens/s on a MacBook M3. This work reframes large foundation models from per-input problem solvers into tool builders, enabling efficient local execution of fuzzy functions (e.g., log alerting, JSON repair) without costly API calls. It significantly reduces resource requirements, making advanced NLP capabilities accessible on edge devices. The PAW compiler is trained on FuzzyBench, a new 10M-example dataset released by the authors. The interpreter is a frozen 0.6B Qwen3 model that executes parameter-efficient adapters emitted by the compiler, achieving performance comparable to direct prompting of Qwen3-32B.

huggingface_papers · Hugging Face Papers · Jul 3, 00:00

**Background**: Many programming tasks, such as alerting on log lines or ranking search results, are difficult to implement with explicit rules and are often outsourced to large language model APIs, which introduces latency, cost, and reproducibility issues. Parameter-efficient adapters (e.g., LoRA) allow fine-tuning a small subset of model parameters for specific tasks without modifying the base model. PAW combines these ideas by using a compiler to generate adapters from natural language, enabling efficient local execution.

<details><summary>References</summary>
<ul>
<li><a href="https://weightagnostic.github.io/">Weight Agnostic Neural Networks</a></li>
<li><a href="https://arxiv.org/abs/1902.00751">[1902.00751] Parameter-Efficient Transfer Learning for NLP GitHub - adapter-hub/adapters: A Unified Library for ... Awesome Adapter Resources - Clifton Poth LoRA & PEFT Fine-Tuning: Production Guide for 2026 - TheCodeForge ELP-Adapters: Parameter Efficient Adapter Tuning for Various ...</a></li>

</ul>
</details>

**Tags**: `#programming paradigms`, `#neural networks`, `#natural language processing`, `#efficient inference`, `#fuzzy functions`

---

<a id="item-6"></a>
## [AgenticSTS: Bounded-Memory Testbed for Long-Horizon LLM Agents](https://huggingface.co/papers/2607.02255) ⭐️ 8.0/10

Researchers propose AgenticSTS, a bounded-memory testbed for long-horizon LLM agents that uses typed retrieval to assemble fresh prompts, enabling isolated ablation of memory components. In Slay the Spire 2, this design achieved wins where public transcript-based agents scored zero. This work addresses a critical challenge in long-horizon agentic systems: isolating the effect of individual memory components. The bounded contract approach could lead to more interpretable and efficient LLM agents for complex decision-making tasks. The bounded contract ensures each decision uses a fresh prompt assembled via typed retrieval, with no raw cross-decision transcript appended. In Slay the Spire 2, adding a strategic skill layer improved win rate from 3/10 to 6/10, though the comparison is directional (Fisher exact p≈0.37).

huggingface_papers · Hugging Face Papers · Jul 3, 00:00

**Background**: Long-horizon LLM agents need memory to persist information across many decisions. The simplest approach appends all history to each prompt, but this creates a jumbled context that makes it hard to study individual memory components. AgenticSTS introduces a bounded contract where each decision sees only a fresh prompt assembled from typed retrievals, keeping the prompt size constant and enabling clean ablation studies.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.02255">[2607.02255] AgenticSTS: A Bounded-Memory Testbed for Long ...</a></li>
<li><a href="https://github.com/AlayaLab/AgenticSTS">GitHub - AlayaLab/AgenticSTS: Bounded, typed, ablatable ...</a></li>
<li><a href="https://huggingface.co/papers/2607.02255">Paper page - AgenticSTS: A Bounded-Memory Testbed for Long ...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#memory`, `#long-horizon`, `#testbed`, `#decision-making`

---

<a id="item-7"></a>
## [Wordgard: New Rich-Text Editor from ProseMirror Creator](https://wordgard.net/) ⭐️ 8.0/10

Wordgard 0.1.0, a new in-browser rich-text editor, has been released by the creator of ProseMirror. It shares many concepts with ProseMirror but is not a direct upgrade path. This release is significant because it comes from a highly respected creator in the rich-text editing space, and the community has shown strong interest with 273 points and 90 comments. It could influence the future of web-based WYSIWYG editors. Wordgard is not a direct upgrade from ProseMirror; switching requires significant work. The editor is designed to be lightweight and accessible, with a focus on simplicity.

hackernews · indy · Jul 3, 08:50 · [Discussion](https://news.ycombinator.com/item?id=48772573)

**Background**: ProseMirror is a popular open-source toolkit for building rich-text editors in the browser, widely used in applications like TipTap. Wordgard is a new system in the same space, aiming to simplify content editing with a fresh approach.

<details><summary>References</summary>
<ul>
<li><a href="https://discuss.prosemirror.net/t/wordgard-0-1-0/9035">Wordgard 0.1.0 - Announce - discuss.ProseMirror</a></li>
<li><a href="https://digitechbytes.com/digital-lifestyle-productivity/wordgard-in-browser-rich-text-editor-from-the-creator-of-prosemirror/">Wordgard: In-browser Rich-text Editor From The Creator Of ...</a></li>

</ul>
</details>

**Discussion**: The community is curious about the 'why' behind Wordgard and notes that there is no upgrade path from ProseMirror. Some users express validation seeing similarities with their own work, while others highlight the lack of a statically-typed schema as a pain point in ProseMirror.

**Tags**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#open source`, `#WYSIWYG`

---

<a id="item-8"></a>
## [PostgreSQL OOM Killer: Why Strict Memory Overcommit Matters](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.0/10

Ubicloud published a blog post explaining why they use strict memory overcommit (vm.overcommit_memory=2) for PostgreSQL to prevent the Linux OOM killer from terminating database processes, and shared their experience with a kernel bug that temporarily forced them to disable the setting. This matters because PostgreSQL is sensitive to memory pressure, and the default Linux overcommit behavior can lead to catastrophic OOM kills that crash the database. The article provides practical guidance for database administrators seeking more predictable and stable production deployments. Strict overcommit (mode 2) disables memory overcommit entirely, so malloc() returns NULL if memory is unavailable, preventing the OOM killer from activating. However, mode 2 can cause fork() failures if the overcommit ratio is misconfigured, and the article notes a three-character kernel bug that forced them to temporarily revert to defaults.

hackernews · furkansahin · Jul 3, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48774509)

**Background**: Linux uses memory overcommit by default (mode 0 - heuristic), allowing processes to allocate more virtual memory than physical RAM + swap, assuming not all memory will be used simultaneously. When the system runs out of memory, the OOM killer selects and terminates a process to free memory, which can kill critical PostgreSQL processes. Strict overcommit (mode 2) ensures allocations only succeed if memory is actually available, avoiding OOM kills but risking allocation failures.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit">PostgreSQL and the OOM Killer: Why We Use Strict Memory ...</a></li>
<li><a href="https://www.kernel.org/doc/Documentation/vm/overcommit-accounting">The Linux kernel supports the following overcommit handling modes</a></li>
<li><a href="https://www.cybertec-postgresql.com/en/what-you-should-know-about-linux-memory-overcommit-in-postgresql/">Memory overcommit and PostgreSQL - CYBERTEC</a></li>

</ul>
</details>

**Discussion**: Commenters debated the trade-offs: some noted that Linux defaults are problematic under memory pressure, while others cautioned that mode 2 can break applications that rely on fork() or allocate large virtual memory (e.g., Go programs). One commenter from Ubicloud acknowledged the article's strong tone and emphasized that strict overcommit may have unanticipated side-effects in many scenarios.

**Tags**: `#PostgreSQL`, `#Linux`, `#memory management`, `#OOM killer`, `#database administration`

---

<a id="item-9"></a>
## [Open Source AI Gap Map Launched](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a non-profit founded in February 2025, launched the Open Source AI Gap Map v0.1, indexing 421 products across the AI stack to identify gaps and opportunities. This map provides a structured overview of the open source AI ecosystem, helping developers, investors, and policymakers understand where to focus efforts and funding. The map covers 266 software tools, 85 models, 50 datasets, and 20 hardware projects from 228 organizations, with underlying data released under an MIT license on GitHub.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI is a global partnership building a public option for AI, backed by $400 million in committed capital. The Gap Map builds on work from Columbia Convening, MOF, Hugging Face, and others to map the open source AI stack.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map - simonwillison.net</a></li>
<li><a href="https://map.currentai.org/">Current AI – Open Source AI Gap Map</a></li>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1 - currentai.org</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#ecosystem`, `#mapping`, `#non-profit`

---

<a id="item-10"></a>
## [HAT-4D: 4D Interactive Scenes from Monocular Video](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247901356&idx=3&sn=54ee94026f76691a380cd3ea214e0def) ⭐️ 8.0/10

Shanghai Jiao Tong University and collaborators propose HAT-4D, a method that generates 4D interactive scenes directly from a single monocular video, eliminating the need for expensive multi-camera motion capture systems. This breakthrough could democratize 4D content creation for VR/AR, gaming, and film production by replacing million-dollar motion capture studios with a single consumer camera, significantly lowering cost and barrier to entry. HAT-4D reconstructs dynamic 3D scenes with temporal consistency from monocular video, enabling interactive viewpoint control and scene editing. The method likely builds on recent advances in 4D reconstruction using Gaussian splatting or neural radiance fields.

rss · 量子位 · Jul 3, 03:43

**Background**: Traditional 4D (dynamic 3D) scene capture requires multi-camera arrays or expensive motion capture suits, costing millions. Recent research like CAT4D and Vivid4D has explored monocular video to 4D reconstruction, but HAT-4D specifically targets interactive scene understanding and manipulation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2504.11092">Vivid4D: Improving 4D Reconstruction from Monocular Video by ...</a></li>
<li><a href="https://arxiv.org/abs/2601.18993">[2601.18993] FreeOrbit4D: Training-Free Arbitrary Camera ... 4D-Fly: Fast 4D Reconstruction from a Single Monocular Video CAT4D: Create Anything in 4D with Multi-View Video Diffusion ... Vivid4D: Improving 4D Reconstruction from Monocular Video by ... GitHub - VVeiCao/FreeOrbit4D: [SIGGRAPH 2026 Conference ...</a></li>

</ul>
</details>

**Tags**: `#4D reconstruction`, `#computer vision`, `#AI`, `#motion capture`, `#scene understanding`

---

<a id="item-11"></a>
## [DeepSeek V4 Flash MoE Runs on RTX 5090 with Custom llama.cpp Fork](https://www.reddit.com/r/LocalLLaMA/comments/1umsik8/deepseek_v4_flash_running_on_rtx_5090_moe/) ⭐️ 8.0/10

A Reddit user successfully ran DeepSeek V4 Flash, a 284B MoE model, on an RTX 5090 using a custom llama.cpp fork, achieving 21.3 TG T/s and 927 PP T/s with up to 1 million token context. This demonstrates that large MoE models like DeepSeek V4 Flash can be run locally on consumer hardware, enabling fast, private AI inference without cloud APIs, and highlights the growing capability of local LLM deployment. The setup uses a Q2_K quantized GGUF model, a custom llama.cpp fork with CUDA support, and the --n-cpu-moe 37 parameter to offload expert layers to CPU, fitting a 1M context with 512 ub. The build targets CUDA architecture 120 (Blackwell).

reddit · r/LocalLLaMA · /u/H_DANILO · Jul 3, 22:48

**Background**: DeepSeek V4 Flash is a 284B-parameter Mixture-of-Experts (MoE) model with 13B activated parameters and a 1M-token context window, optimized for fast coding and agent tasks. The RTX 5090 is NVIDIA's latest consumer GPU based on the Blackwell architecture. llama.cpp is an open-source C++ implementation for running LLMs locally, and the custom fork adds support for DeepSeek V4's architecture.

<details><summary>References</summary>
<ul>
<li><a href="https://build.nvidia.com/deepseek-ai/deepseek-v4-flash">deepseek - v 4 - flash Model by Deepseek -ai | NVIDIA NIM</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V 4 Flash - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**Discussion**: The community praised the achievement, with follow-up benchmarks showing DeepSeek V4 Flash on vLLM achieving Sonnet-level quality and faster wall-clock time than API-based models. Users noted that local models are now competitive, especially when avoiding dense attention, and that Opus and Fable still lead in quality.

**Tags**: `#DeepSeek`, `#RTX 5090`, `#MoE`, `#llama.cpp`, `#benchmark`

---

<a id="item-12"></a>
## [CDD recovers finetuning data from LLM logits without weight access](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

Researchers introduce Contrastive Decoding Diffing (CDD), a grey-box method that recovers verbatim finetuning data from large language models by contrasting logits of the base and finetuned models, achieving high recovery scores without needing weight access. CDD addresses a critical privacy and security concern in LLMs by demonstrating that finetuning data can be extracted with only logit access, which is much easier to obtain than weights, potentially exposing sensitive information used in fine-tuning. CDD achieves a verbatim recovery score of 4+/5 on 19 out of 20 organism-model pairs across four model families (1B to 32B parameters) on the SDF benchmark, outperforming the white-box Activation Difference Lens (ADL) which never exceeds 3/5.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jul 3, 19:01

**Background**: Model diffing aims to identify differences between a base model and its finetuned version. Previous work, Activation Difference Lens (ADL), required full weight access and could only recover vague domain-level descriptions. CDD operates at the output level, using only logit distributions, making it a grey-box method that is more practical for real-world scenarios.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/papers/2605.25902">CDD: Verbatim Content Recovery via Diffing</a></li>
<li><a href="https://www.machinebrief.com/news/unlocking-ais-hidden-memories-with-contrastive-decoding-9a3m">Unlocking AI's Hidden Memories with Contrastive Decoding</a></li>
<li><a href="https://arxiv.org/html/2510.13900">Narrow Finetuning Leaves Clearly Readable Traces in Activation ...</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion highlights the method's novelty and privacy implications, with some commenters noting the surprising finding that a fictional persona 'Dr. Elena Rodriguez' consistently appeared across unrelated finetuning domains, indicating a bias in synthetic data generation. Others debate the practical threat level and potential defenses.

**Tags**: `#LLM`, `#model diffing`, `#privacy`, `#finetuning`, `#security`

---

<a id="item-13"></a>
## [System Prompt Extraction Attack Works on 60-70% of AI Agents](https://www.reddit.com/r/artificial/comments/1ums1ou/repeat_the_text_above_this_line_still_works_on/) ⭐️ 8.0/10

A simple prompt injection attack, such as asking 'repeat the text above this line,' can extract the full system prompt from 60-70% of deployed AI agents, revealing guardrails, tool configurations, and API keys. This vulnerability poses a serious security risk because leaked system prompts provide attackers with a roadmap to bypass guardrails, access internal tools, and exploit business logic, affecting countless production AI systems. The attack works through direct commands, translation tricks, encoding requests, roleplay, and multi-turn conversations; effective defenses include role anchoring, output filtering, prompt segmentation, and meta-instruction awareness.

reddit · r/artificial · /u/Still_Piglet9217 · Jul 3, 22:27

**Background**: System prompt extraction is a type of prompt injection attack where an attacker tricks an LLM into revealing its hidden system instructions. These instructions define the model's behavior, tool access, and safety rules. The attack exploits the model's inability to distinguish between developer-defined prompts and user inputs, a fundamental challenge in LLM security.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2505.23817">System Prompt Extraction Attacks and Defenses in Large Language...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://wraith.sh/learn/system-prompt-extraction-guide">System Prompt Extraction : Techniques and Defenses | Wraith</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion largely validates the findings, with many users sharing similar experiences and emphasizing the need for better defenses. Some commenters note that the attack is trivial to execute and that many production agents remain vulnerable despite known risks.

**Tags**: `#AI security`, `#prompt injection`, `#system prompt extraction`, `#LLM vulnerabilities`, `#red teaming`

---

<a id="item-14"></a>
## [Elixir 1.2 Adds Gradual Set-Theoretic Types](https://www.reddit.com/r/ProgrammingLanguages/comments/1umai41/what_does_it_take_to_add_settheoretic_types_to_a/) ⭐️ 8.0/10

Elixir 1.2 ships a gradual set-theoretic type system based on Guillaume Dubois's PhD work at IRIF Paris, with a parallel etalizer for Erlang being built by Annette Bieniusa at RPTU Germany on the same foundation. This marks a significant technical achievement: retrofitting an expressive type system onto a dynamic language with 30 years of production code, after decades of resistance including Philip Wadler's failed attempt in 1995. The dynamic type is structurally embedded into the set-theoretic lattice from the start, and the system warns before rejecting code; message typing across processes is explicitly out of scope for now.

reddit · r/ProgrammingLanguages · /u/rtrusca · Jul 3, 10:14

**Background**: Gradual typing allows mixing static and dynamic types in the same language. Set-theoretic types use set operations (union, intersection, negation) to describe types, enabling precise modeling of dynamic patterns. Elixir runs on the Erlang VM (BEAM), which has historically resisted static typing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gradual_typing">Gradual typing</a></li>
<li><a href="https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/">Elixir v1.20 released: now a gradually typed language</a></li>
<li><a href="https://www.reddit.com/r/programming/comments/1twg7mu/elixir_v120_released_now_a_gradually_typed/">Elixir v1.20 released: now a gradually typed language : r/programming - Reddit</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion highlights the difficulty of retrofitting types onto dynamic languages and compares Elixir's approach to other gradual typing efforts like TypeScript and Hack. Some commenters express skepticism about the practicality of set-theoretic types in large codebases.

**Tags**: `#type systems`, `#Elixir`, `#Erlang`, `#gradual typing`, `#programming languages`

---

<a id="item-15"></a>
## [OmniRoute: Free AI Gateway with 230+ Providers](https://github.com/diegosouzapw/OmniRoute) ⭐️ 8.0/10

OmniRoute, a free and open-source AI gateway written in TypeScript, now provides a single endpoint to access over 230 AI providers, including 50+ free tiers, with token compression and smart auto-fallback. This project simplifies AI integration by unifying many providers behind one API, reducing costs through token compression and ensuring reliability with automatic fallback, which is valuable for developers building AI-powered applications. OmniRoute uses RTK (Rust Token Killer) and Caveman stacked compression to save 15-95% tokens, supports MCP and A2A protocols, multimodal APIs, and can be used as a Desktop app or PWA.

ossinsight · GitHub Trending · Jul 4, 03:16

**Background**: An AI gateway is middleware that sits between applications and AI service providers, managing API calls, routing, security, and monitoring. Token compression techniques like RTK and Caveman reduce the number of tokens sent to LLMs, lowering costs. MCP (Model Context Protocol) and A2A (Agent-to-Agent) are emerging protocols for agent interoperability.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/sonim1/token-saving-and-caveman-e1f">Token Saving, and Caveman - DEV Community</a></li>
<li><a href="https://a2a-protocol.org/latest/">A 2 A Protocol</a></li>
<li><a href="https://vercel.com/ai-gateway">AI Gateway – Vercel</a></li>

</ul>
</details>

**Tags**: `#AI Gateway`, `#TypeScript`, `#Open Source`, `#API`, `#Token Compression`

---