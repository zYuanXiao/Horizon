---
layout: default
title: "Horizon Summary: 2026-07-19 (EN)"
date: 2026-07-19
lang: en
---

> From 123 items, 15 important content pieces were selected

---

1. [Ring-Zero Scales Zero RL to Trillion Parameters](#item-1) ⭐️ 9.0/10
2. [SigNoz Surges with 432 Daily Stars as Open-Source Observability Platform](#item-2) ⭐️ 8.0/10
3. [Open Interpreter Gains 383 Stars for Coding Agent with Kimi K3](#item-3) ⭐️ 8.0/10
4. [LongStraw: Million-Token RL Post-Training on Fixed GPU Budget](#item-4) ⭐️ 8.0/10
5. [Kimi K3: A Distillation Milestone from China](#item-5) ⭐️ 8.0/10
6. [The Computer at the Bottom of a Canal](#item-6) ⭐️ 8.0/10
7. [PHK Reflects on Bikeshedding and Reversible Decisions](#item-7) ⭐️ 8.0/10
8. [Qubes OS Security Paper Published with Public Evidence](#item-8) ⭐️ 8.0/10
9. [Controlling Reasoning Effort in LLMs](#item-9) ⭐️ 8.0/10
10. [Basalt Labs Accused of AI Model Fraud](#item-10) ⭐️ 8.0/10
11. [SooFi Team Releases Open-Source Hybrid Mamba-Transformer MoE Model](#item-11) ⭐️ 8.0/10
12. [Byte-Exact KV Cache Grafting Boosts Gemma 4 Accuracy](#item-12) ⭐️ 8.0/10
13. [Alleged AI Slop Wins $25K DeepMind Kaggle Prize](#item-13) ⭐️ 8.0/10
14. [Interactive t-SNE map of GPT-2 token embeddings](#item-14) ⭐️ 8.0/10
15. [White House to Dictate Access to Frontier AI Models](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Ring-Zero Scales Zero RL to Trillion Parameters](https://huggingface.co/papers/2607.12395) ⭐️ 9.0/10

A new paper presents a stable pipeline for scaling zero reinforcement learning (zero RL) to trillion-parameter models, achieving emergent reasoning capabilities and improved sample efficiency on mathematical benchmarks. This work validates the scaling benefits of zero RL at an unprecedented scale, demonstrating that trillion-parameter models spontaneously develop advanced reasoning behaviors, which could significantly advance AI reasoning without human annotation. The pipeline incorporates algorithmic and system optimizations such as clipped importance sampling, training-inference ratio correction, and mixed-precision control. The resulting model, Ring-2.5-1T-Zero, achieves competitive performance on seven mathematical benchmarks.

huggingface_papers · Hugging Face Papers · Jul 16, 00:00

**Background**: Zero reinforcement learning (zero RL) is a paradigm that applies RL with verifiable rewards directly to pretrained language models, bypassing the need for supervised fine-tuning. Prior work was limited to small models due to computational constraints, leaving the dynamics at large scale unexplored. This paper addresses that gap by scaling to 1 trillion parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.25528">[2510.25528] Zero Reinforcement Learning Towards General Domains</a></li>
<li><a href="https://swift.readthedocs.io/en/latest/Instruction/GRPO/AdvancedResearch/CISPO.html">Clipped Importance Sampling Policy Optimization (CISPO) — swift 4.5.0.dev0 documentation</a></li>
<li><a href="https://www.emergentmind.com/topics/training-inference-ratio-correction">Training-Inference Ratio Correction - emergentmind.com</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#large language models`, `#reasoning`, `#scaling`, `#AI research`

---

<a id="item-2"></a>
## [SigNoz Surges with 432 Daily Stars as Open-Source Observability Platform](https://github.com/SigNoz/signoz) ⭐️ 8.0/10

SigNoz, an open-source OpenTelemetry-native observability platform, gained 432 stars on GitHub in a single day, reaching over 30,000 total stars. The platform unifies logs, metrics, and traces with APM, distributed tracing, and AI agent support. This rapid star growth reflects strong community interest in open-source observability tools, especially those integrating AI agents. SigNoz's unified approach simplifies monitoring for DevOps teams and could challenge proprietary solutions like Datadog. SigNoz is built with TypeScript and supports OpenTelemetry natively, enabling seamless data ingestion. It also offers SigNoz MCP for custom queries and a native AI teammate in its cloud version.

github_trending · GitHub Trending · Jul 19, 02:48

**Background**: Observability platforms help engineers monitor and debug distributed systems by collecting logs, metrics, and traces. OpenTelemetry is a CNCF standard for instrumenting applications, and SigNoz leverages it to provide a unified, open-source alternative to proprietary tools.

<details><summary>References</summary>
<ul>
<li><a href="https://opentelemetry.io/">OpenTelemetry</a></li>
<li><a href="https://github.com/SigNoz/signoz-mcp-server">GitHub - SigNoz / signoz - mcp -server: MCP Server for SigNoz · GitHub</a></li>
<li><a href="https://signoz.io/tags/mcp/">mcp | SigNoz</a></li>

</ul>
</details>

**Tags**: `#observability`, `#open-source`, `#OpenTelemetry`, `#APM`, `#DevOps`

---

<a id="item-3"></a>
## [Open Interpreter Gains 383 Stars for Coding Agent with Kimi K3](https://github.com/openinterpreter/openinterpreter) ⭐️ 8.0/10

Open Interpreter, a coding agent for open models like Kimi K3, gained 383 stars on GitHub today, reaching over 66,000 total stars. The project is written in Rust and enables users to interact with code via natural language. This project makes advanced coding agents accessible to open-source models, lowering the barrier for developers to use AI-assisted coding. Its high star count reflects strong community interest in open-source AI tooling. Open Interpreter runs in the terminal, can read files, edit code, and execute commands, with safety checks before escalating actions. It supports the Kimi K3 model, which has 2.8 trillion parameters and a 1M token context window.

github_trending · GitHub Trending · Jul 19, 02:48

**Background**: Coding agents are AI tools that understand and generate code, often integrated with large language models (LLMs). Kimi K3 is a recent open-source LLM with 2.8 trillion parameters, built on a Mixture-of-Experts architecture, competing with proprietary models from OpenAI and Anthropic.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openinterpreter/openinterpreter">GitHub - openinterpreter/openinterpreter: A coding agent for open ...</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://artificialanalysis.ai/models/kimi-k3">Kimi K 3 - Intelligence, Performance & Price Analysis</a></li>

</ul>
</details>

**Tags**: `#AI`, `#coding agent`, `#open source`, `#Rust`, `#LLM`

---

<a id="item-4"></a>
## [LongStraw: Million-Token RL Post-Training on Fixed GPU Budget](https://huggingface.co/papers/2607.14952) ⭐️ 8.0/10

LongStraw is an architecture-aware execution stack that enables million-token RL post-training under a fixed GPU budget, instantiated with GRPO. It evaluates the shared prompt without autograd, retains only model-specific state, and replays short response branches one at a time to reduce memory. This bridges the growing gap between inference context lengths (approaching million tokens) and RL post-training (often ≤256K tokens), which is critical for AI agents with long trajectories. It enables practical long-context RL fine-tuning without requiring additional GPU resources. On eight H20 GPUs, LongStraw completes grouped Qwen scoring and response backward at 2.1M positions for groups of 2 and 8, with only 0.21 GB added peak memory per group size increase. A stress test reaches 4.46M positions, and on 32 H20 GPUs, it validates a 2.1M-token prompt across all 78 layers of GLM-5.2.

huggingface_papers · Hugging Face Papers · Jul 17, 00:00

**Background**: Long-context RL post-training is memory-intensive because standard methods like PPO require a critic model and retain gradients for the entire sequence. GRPO eliminates the critic by using group statistics as baselines, but still faces memory bottlenecks with long contexts. LongStraw optimizes memory by avoiding autograd on the shared prompt and replaying response branches sequentially, trading extra computation for reduced peak memory.

<details><summary>References</summary>
<ul>
<li><a href="https://cs360umass.org/grpo-demo.html">GRPO — Group Relative Policy Optimization</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/hybrid-attention/">Hybrid Attention | Sebastian Raschka, PhD</a></li>
<li><a href="https://datanorth.ai/blog/what-is-mixture-of-experts-moe-and-why-does-it-matter">What is mixture of experts (MoE) and why does it matter?</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#long-context`, `#GPU optimization`, `#AI agents`, `#GRPO`

---

<a id="item-5"></a>
## [Kimi K3: A Distillation Milestone from China](https://stephen.bochinski.dev/blog/2026/07/18/the-kimi-k3-moment/) ⭐️ 8.0/10

The Kimi K3 model from China may represent a major milestone in AI distillation, potentially achieving parity with frontier US models through distillation techniques. This challenges US frontier labs and raises questions about national security and open-weight access, potentially shifting the geopolitical landscape of AI development. Kimi K3 is available via subscription plans, with the 1M context model only accessible on the $79/month plan, and the K3 model not supported on the minimal $15/month plan.

hackernews · sbochins · Jul 18, 17:32 · [Discussion](https://news.ycombinator.com/item?id=48960218)

**Background**: AI distillation is a technique to create smaller, faster models from larger ones without sacrificing much accuracy. Open-weight access allows developers to run models locally, raising dual-use concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@As_Yu_like_it/the-power-and-promise-of-ai-distillation-26bca5e50461">The Power and Promise of AI Distillation | by Lawrence Yu | Medium</a></li>
<li><a href="https://www.linkedin.com/pulse/understanding-distillation-ai-how-models-can-extracted-pooni-vvaqc">Understanding " Distillation " in AI : How Models Can Be Extracted and...</a></li>
<li><a href="https://rdi.berkeley.edu/llm-agents/assets/percyliang.pdf">Open -source and Science in the Era of Foundation Models - Berkeley...</a></li>

</ul>
</details>

**Discussion**: Commenters note that distillation was inevitable and that the speed of progress is surprising. Some express concern about potential government restrictions on open-weight models, comparing it to the Napster era.

**Tags**: `#AI`, `#distillation`, `#open-source`, `#geopolitics`, `#machine learning`

---

<a id="item-6"></a>
## [The Computer at the Bottom of a Canal](https://negroniventurestudios.com/2026/07/18/the-computer-at-the-bottom-of-a-canal/) ⭐️ 8.0/10

A historical article details a unique capability-based computer discovered in a canal, exploring its innovative tagged architecture and the lessons for specialized hardware in a post-commodity era. This story highlights the trade-offs between specialized hardware and commodity computing, suggesting that as the commodity curve ends, custom hardware may become viable again, influencing future computer architecture design. The computer used a tagged architecture and capability-based addressing, concepts that were cutting-edge in the 1970s and 1980s but were eclipsed by commodity chips and Moore's Law.

hackernews · Kudos · Jul 18, 08:33 · [Discussion](https://news.ycombinator.com/item?id=48956231)

**Background**: Capability machines, like the Intel iAPX 432 and the CAP computer, were research systems that enforced fine-grained access control through hardware. Tagged architectures attach metadata to each memory word, enabling secure and efficient object-oriented programming. These ideas were largely abandoned due to the dominance of commodity CPUs, but modern projects like CHERI are reviving capability concepts for security.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Capability_Hardware_Enhanced_RISC_Instructions">Capability Hardware Enhanced RISC Instructions - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Capability-based_addressing">Capability-based addressing - Wikipedia</a></li>
<li><a href="https://homes.cs.washington.edu/~levy/capabook/Chapter1.pdf">Object- Based</a></li>

</ul>
</details>

**Discussion**: Commenters note that capability machines were once cutting-edge but were crushed by the commodity curve and Moore's Law. Some find the author's idea that the commodity curve is over intriguing, suggesting that with cheap hardware and AI, specialized hardware may become viable again.

**Tags**: `#computer architecture`, `#capability machines`, `#history of computing`, `#hardware design`, `#tagged architectures`

---

<a id="item-7"></a>
## [PHK Reflects on Bikeshedding and Reversible Decisions](https://queue.acm.org/detail.cfm?id=3818307) ⭐️ 8.0/10

Poul-Henning Kamp published an article in ACM Queue reflecting on the bikeshed effect in open source, advocating for reversible decisions to avoid over-analysis of trivial matters. This article provides valuable insights into open source governance and decision-making, helping teams reduce wasted time on trivial debates and focus on what truly matters. Kamp, who popularized the term 'bikeshedding' in the BSD community in 1999, now argues that reversible decisions should be made quickly and instinctively, without lengthy discussion.

hackernews · Ygg2 · Jul 18, 17:27 · [Discussion](https://news.ycombinator.com/item?id=48960155)

**Background**: The bikeshed effect, also known as Parkinson's law of triviality, describes how people disproportionately focus on trivial issues that are easy to understand, while neglecting complex but important ones. Kamp's original 1999 email popularized the term in software development. Reversible decisions are those that can be easily undone with low cost, and experts recommend making them quickly to avoid analysis paralysis.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bikeshed_effect">Bikeshed effect</a></li>
<li><a href="https://en.wikipedia.org/wiki/Law_of_triviality">Law of triviality - Wikipedia</a></li>
<li><a href="https://strategizeyourcareer.com/p/how-software-engineers-make-productive-decisions">How Software Engineers Make Productive Decisions (without slowing the team down)</a></li>

</ul>
</details>

**Discussion**: Commenters discussed the value of reversible decisions, with one noting that throwing money at trivial decisions can avoid bikeshedding. Another commenter highlighted Kamp's creation of the MD5crypt algorithm. Some criticized Kamp's view on LLMs as out of touch, while others praised the article after multiple reads.

**Tags**: `#open source`, `#software engineering`, `#bikeshedding`, `#governance`, `#decision making`

---

<a id="item-8"></a>
## [Qubes OS Security Paper Published with Public Evidence](https://arxiv.org/abs/2607.14587) ⭐️ 8.0/10

A new academic paper titled 'Qubes OS Security in the Public Record' has been published on arXiv, analyzing the security claims of Qubes OS using publicly available evidence. The author, Alfonso De Gregorio, participated in an AMA (Ask Me Anything) session in the community discussion. This paper provides a rigorous, evidence-based evaluation of Qubes OS's security, moving beyond marketing claims. It is significant for security-conscious users and researchers, as it offers transparency and accountability for a widely endorsed security-focused operating system. The paper focuses on Qubes OS's architecture, which uses virtualization to compartmentalize applications into isolated virtual machines called qubes. The analysis is based on public records, including source code, documentation, and community discussions.

hackernews · sciences44 · Jul 18, 08:50 · [Discussion](https://news.ycombinator.com/item?id=48956307)

**Background**: Qubes OS is a security-oriented desktop operating system that isolates applications in separate virtual machines to limit the impact of security breaches. It has been endorsed by notable figures like Edward Snowden. The paper's approach of using public evidence aligns with the open-source ethos of the project.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.14587">[2607.14587] Qubes OS Security in the Public Record</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qubes_OS">Qubes OS - Wikipedia</a></li>
<li><a href="https://www.qubes-os.org/">Qubes OS : A reasonably secure operating system | Qubes OS</a></li>

</ul>
</details>

**Discussion**: Community members expressed nostalgia and appreciation for Qubes OS, with one user noting its lean design and potential for broader use cases. Another highlighted Edward Snowden's endorsement. The author's AMA added credibility and engagement.

**Tags**: `#Qubes OS`, `#security`, `#academic paper`, `#operating systems`, `#privacy`

---

<a id="item-9"></a>
## [Controlling Reasoning Effort in LLMs](https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms) ⭐️ 8.0/10

A new article by Sebastian Raschka explores how LLMs can be trained to operate in low, medium, and high reasoning effort modes, allowing users to balance accuracy and computational cost. The approach uses system prompts to toggle reasoning effort, as seen in OpenAI's o3-mini and gpt-oss models. This technique enables more efficient deployment of LLMs by allowing users to choose the appropriate reasoning depth for each task, reducing latency and cost for simple queries while reserving high effort for complex problems. It addresses a key challenge in practical LLM deployment: controlling computational effort without sacrificing performance. High effort can improve accuracy by 10-30% on benchmarks but may increase cost by 10-74× compared to standard models. The reasoning effort is controlled via a system prompt parameter (e.g., "Reasoning effort: low/medium/high") prepended to each prompt.

rss · Sebastian Raschka · Jul 18, 11:16

**Background**: Large language models (LLMs) with chain-of-thought reasoning can solve complex problems but often use excessive computation for simple tasks. Reasoning effort modes allow the model to allocate just enough computation for the task at hand, similar to how humans adjust mental effort. This concept is implemented in models like OpenAI's o3-mini and the open-source gpt-oss series.

<details><summary>References</summary>
<ul>
<li><a href="https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms">Controlling Reasoning Effort in LLMs</a></li>
<li><a href="https://www.vellum.ai/llm-parameters/reasoning-effort">Reasoning effort - LLM Parameter Guide - Vellum</a></li>
<li><a href="https://cameronrwolfe.substack.com/p/demystifying-reasoning-models">Demystifying Reasoning Models - by Cameron R. Wolfe, Ph.D.</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#reasoning`, `#efficiency`, `#AI training`

---

<a id="item-10"></a>
## [Basalt Labs Accused of AI Model Fraud](https://www.reddit.com/r/LocalLLaMA/comments/1uztylz/basalt_labs_pulling_a_generationally_dumb_scam/) ⭐️ 8.0/10

Basalt Labs is accused of falsely claiming a 99.44% score on the HLE benchmark with tools, while the released model is based on Qwen2.5-7B-Instruct and the served model is actually DeepSeek. This scam undermines trust in AI benchmarks and model claims, potentially misleading investors and users. It highlights the need for transparency and verification in the AI community. The HLE benchmark is a difficult test for AI progress toward AGI, with top scores around 64.5% from leading models. Basalt Labs' claimed 99.44% is implausibly high, and the model swap suggests deliberate deception.

reddit · r/LocalLLaMA · /u/WithoutReason1729 · Jul 18, 11:58

**Background**: The HLE (Humanity's Last Exam) benchmark, released in January 2025, is designed to measure AI progress toward AGI. Qwen2.5-7B-Instruct is a 7-billion-parameter open-source model from Alibaba, while DeepSeek is a Chinese AI company known for cost-effective models. The discrepancy between the claimed and actual models indicates a bait-and-switch tactic.

<details><summary>References</summary>
<ul>
<li><a href="https://benchlm.ai/benchmarks/hle">HLE Leaderboard & Scores — July 2026 | BenchLM. ai</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen2.5-7B-Instruct">Qwen/ Qwen 2 . 5 - 7 B - Instruct · Hugging Face</a></li>

</ul>
</details>

**Discussion**: The Reddit community expressed outrage and mockery, calling the scam 'generationally dumb' and 'incredibly stupid.' Users pointed out the obvious discrepancy in benchmark scores and urged others to verify claims independently.

**Tags**: `#AI ethics`, `#scam`, `#LLM`, `#fraud`, `#community alert`

---

<a id="item-11"></a>
## [SooFi Team Releases Open-Source Hybrid Mamba-Transformer MoE Model](https://www.reddit.com/r/LocalLLaMA/comments/1v0cyix/german_soofi_team_launches_soofi_s_30ba3b_an/) ⭐️ 8.0/10

The German SooFi team has released Soofi S 30B-A3B, an open-source Mixture-of-Experts (MoE) model that combines Mamba and Transformer architectures, with 30 billion total parameters and 3 billion active parameters, optimized for German and English. This model represents a novel technical contribution by combining Mamba and Transformer in an MoE framework, offering efficient inference for German and English NLP tasks. Its open-source nature allows the community to study and build upon the hybrid architecture, potentially advancing multilingual AI. The model has 30 billion total parameters but only 3 billion are active per token, making it efficient for local deployment. It is a hybrid Mamba-Transformer model, leveraging the linear-time sequence modeling of Mamba and the attention mechanisms of Transformer.

reddit · r/LocalLLaMA · /u/epSos-DE · Jul 19, 01:14

**Background**: Mixture-of-Experts (MoE) is an architecture that activates only a subset of parameters per input, enabling larger models with lower computational cost. Mamba is a state space model that offers linear-time sequence modeling, while Transformer uses attention mechanisms. Hybrid Mamba-Transformer models aim to combine the strengths of both, achieving high accuracy and efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2312.00752">Mamba : Linear-Time Sequence Modeling with Selective State Spaces</a></li>
<li><a href="https://www.emergentmind.com/topics/hybrid-mamba-transformer-model">Hybrid Mamba - Transformer Model</a></li>
<li><a href="https://agentaibox.com/en/articles/moe-sparse-architecture-why-llms-going-sparse">MoE Architecture Explained: Why Every Major LLM Is Going Sparse</a></li>

</ul>
</details>

**Discussion**: The Reddit community discussion is active, with users praising the model's efficiency and open-source release. Some commenters discuss the technical details of the hybrid architecture and its potential for German NLP, while others compare it to existing models like Llama and Mistral.

**Tags**: `#Mixture-of-Experts`, `#Mamba`, `#Transformer`, `#German NLP`, `#open-source`

---

<a id="item-12"></a>
## [Byte-Exact KV Cache Grafting Boosts Gemma 4 Accuracy](https://www.reddit.com/r/LocalLLaMA/comments/1v07tib/byte_exact_kv_cache_grafting_on_frozen_gemma_4/) ⭐️ 8.0/10

Researchers published a method for byte-exact KV cache grafting on frozen Gemma 4 12B, improving routing accuracy on AIME 2025 from 76.7% to 90.0%. This technique enables storing and restoring verified knowledge as KV state without retraining, significantly boosting inference accuracy and efficiency for large language models. The method, called Taliesin, achieves byte-exact restoration of KV cache, and the verify-then-cache loop is named Galahad. It also extends usable context from 32,768 to 2,854,766 tokens with zero extra accelerator memory.

reddit · r/LocalLLaMA · /u/MindPsychological140 · Jul 18, 21:24

**Background**: KV cache stores key-value pairs from previous tokens to speed up transformer inference. Byte-exact grafting means the restored cache is identical to fresh computation, enabling reliable knowledge reuse.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/papers/2607.14431">Paper page - Smarter and Cheaper at Once: Byte - Exact KV - Cache ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=48942804">Show HN: KV - Cache Grafting – Boosting frozen... | Hacker News</a></li>

</ul>
</details>

**Tags**: `#KV cache`, `#LLM`, `#inference optimization`, `#Gemma`, `#knowledge storage`

---

<a id="item-13"></a>
## [Alleged AI Slop Wins $25K DeepMind Kaggle Prize](https://www.reddit.com/r/MachineLearning/comments/1uzyf66/did_blatant_ai_slop_just_win_a_25k_usd_deepmind/) ⭐️ 8.0/10

A Reddit user claims that a poorly constructed submission won the $25,000 grand prize in the Google DeepMind-sponsored Kaggle competition 'Measuring Progress Toward AGI - Cognitive Abilities', alleging the submission contains nonsensical code and unfounded claims. This controversy raises serious questions about the integrity of AI benchmarking and the review process in high-profile competitions, potentially undermining trust in how progress toward AGI is measured. The submission allegedly exceeded the requested format by 10 times, and the Reddit user provided two detailed posts analyzing the write-up, methodology, code, and data to support their claims.

reddit · r/MachineLearning · /u/TheWerkmeister · Jul 18, 15:10

**Background**: The competition, launched by Google DeepMind in March 2026, asked participants to design new cognitive-science-based AI benchmarks to evaluate frontier models beyond simple recall. The winning submission was awarded $25,000 and the grand prize stamp.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/">Measuring Progress Towards AGI : A Cognitive Framework</a></li>
<li><a href="https://ailearninghubhq.beehiiv.com/p/google-deepmind-wants-you-to-help-measure-agi">Google DeepMind Wants You to Help Measure AGI</a></li>
<li><a href="https://medium.com/@Micheal-Lanham/deepmind-just-told-you-how-to-evaluate-agi-and-why-agent-benchmarks-miss-7-of-10-cognitive-55e2eed37aed">DeepMind Just Told You How to Evaluate AGI , and Why... | Medium</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is highly critical, with many commenters expressing disbelief and demanding a more transparent review process. Some defend the organizers, arguing that judging is subjective, but the majority view is that the winning submission appears flawed.

**Tags**: `#Kaggle`, `#DeepMind`, `#AI benchmarking`, `#controversy`, `#research integrity`

---

<a id="item-14"></a>
## [Interactive t-SNE map of GPT-2 token embeddings](https://www.reddit.com/r/MachineLearning/comments/1v09muj/interactive_map_of_gpt2s_token_embedding_space/) ⭐️ 8.0/10

A Reddit user released an interactive t-SNE visualization of GPT-2-small's token embedding space, covering 32,070 alphabetic tokens with minimum spanning tree edges to show nearest-kin relationships. This tool makes GPT-2's token embeddings intuitively explorable, aiding researchers and students in understanding semantic relationships without running the model. It lowers the barrier to inspecting how LLMs represent language internally. The visualization uses t-SNE on a compressed representation of the embedding table and draws edges from a minimum spanning tree, so every line represents a genuine nearest-neighbor relationship. It works on mobile with pinch-to-zoom and includes a search box.

reddit · r/MachineLearning · /u/Limp-Contest-7309 · Jul 18, 22:42

**Background**: Token embeddings are dense vector representations of words or subwords learned by language models like GPT-2. t-SNE is a dimensionality reduction technique that maps high-dimensional vectors to 2D while preserving local structure. A minimum spanning tree connects all points with the smallest total edge weight, revealing the closest relationships in the embedding space.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding">t -distributed stochastic neighbor embedding - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Minimum_spanning_tree">Minimum spanning tree</a></li>
<li><a href="https://readmedium.com/line-by-line-lets-reproduce-gpt-2-section-1-b26684f98492">Line By Line, Let’s Reproduce GPT - 2 : Section 1</a></li>

</ul>
</details>

**Tags**: `#GPT-2`, `#token embeddings`, `#t-SNE`, `#visualization`, `#NLP`

---

<a id="item-15"></a>
## [White House to Dictate Access to Frontier AI Models](https://www.reddit.com/r/artificial/comments/1v010pk/the_white_house_is_dictating_access_to_frontier/) ⭐️ 8.0/10

The White House is reportedly planning to dictate access to frontier AI models, shifting power away from tech companies and toward the government. This represents a paradigm shift in AI governance, potentially giving the government control over the most advanced AI systems and affecting global AI development. Frontier AI models are the most advanced general-purpose AI models, trained with massive compute and data, and are considered to pose systemic risks such as misinformation and cyberattacks.

reddit · r/artificial · /u/PsychologicalBox5208 · Jul 18, 16:54

**Background**: Governments worldwide are increasingly regulating frontier AI due to potential risks. The EU AI Act, for example, focuses on models with high-impact capabilities, using a threshold of 10^25 FLOPs for training. The White House's move aligns with this trend, though it has previously distanced itself from tighter regulation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/beyond-hype-what-makes-frontier-ai-truly-hint-its-billions-tiwari-bgrff">Beyond the Hype: What Makes a ' Frontier AI ' Truly Frontier ?</a></li>
<li><a href="https://www.linkedin.com/posts/massimodonna_white-house-distances-itself-from-tighter-activity-7458410261708980224-wdZT">White House distances itself from tighter AI regulation</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#White House`, `#frontier AI`, `#tech giants`, `#governance`

---