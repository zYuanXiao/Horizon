---
layout: default
title: "Horizon Summary: 2026-08-06 (EN)"
date: 2026-08-06
lang: en
---

> From 144 items, 15 important content pieces were selected

---

1. [Google DeepMind Leadership Shakeup: Hassabis to Chair, Dean Departs](#item-1) ⭐️ 9.0/10
2. [TencentDB Agent Memory: Team-Level Memory Hub for AI Agents](#item-2) ⭐️ 8.0/10
3. [Superpowers: Agentic Skills Framework Surges on GitHub](#item-3) ⭐️ 8.0/10
4. [MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce](#item-4) ⭐️ 8.0/10
5. [JoyAI-Video-Edit: Real-Time 720p Video Editing at 30 FPS](#item-5) ⭐️ 8.0/10
6. [NVIDIA Vera Whitepaper Under Fire for Benchmark and Security Claims](#item-6) ⭐️ 8.0/10
7. [Cloudflare OS: Open Platform for Agents and Apps](#item-7) ⭐️ 8.0/10
8. [Deno's Celld: Self-Hosted Durable Objects with SQLite and S3](#item-8) ⭐️ 8.0/10
9. [Position Paper: LLMs Can't Jump in Scientific Discovery](#item-9) ⭐️ 8.0/10
10. [Webhook Limitations and a Streaming GET Proposal](#item-10) ⭐️ 8.0/10
11. [Rubin Observatory Releases First LSST Camera Data: 500k Galaxies in COSMOS Field](#item-11) ⭐️ 8.0/10
12. [AI Cracks Legendary Erdős Problems, Shifting Math Research](#item-12) ⭐️ 8.0/10
13. [Painting with Gaussians: A New Image Stylization Technique](#item-13) ⭐️ 8.0/10
14. [Meta Ran Ads Containing AI-Generated Child Sexual Abuse Imagery](#item-14) ⭐️ 8.0/10
15. [build2 Claims Faster Than Ninja in Detailed Performance Analysis](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google DeepMind Leadership Shakeup: Hassabis to Chair, Dean Departs](https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/) ⭐️ 9.0/10

Demis Hassabis is stepping down as CEO of Google DeepMind to become its chair and Alphabet's chief scientist, while Jeff Dean and Sanjay Ghemawat are leaving Google to co-found a new AI startup called Discovery Loop. This marks a major shift in Google's AI leadership, potentially impacting its competitive position against rivals like OpenAI and Anthropic. The departure of long-time leaders like Jeff Dean could signal a talent exodus and raise concerns about Google's ability to retain top AI researchers. Jeff Dean and Sanjay Ghemawat are launching Discovery Loop, an independent public benefit corporation focused on using AI to accelerate discoveries in ML, science, and engineering. Hassabis's new role as Alphabet chief scientist positions him to oversee broader research across the company.

hackernews · colesantiago · Aug 5, 16:05 · [Discussion](https://news.ycombinator.com/item?id=49184755)

**Background**: Google DeepMind is a leading AI research lab known for breakthroughs like AlphaGo and AlphaFold. Jeff Dean has been a key figure at Google for 27 years, contributing to foundational systems like MapReduce and TensorFlow. The reshuffle reflects ongoing changes in AI leadership as companies compete for top talent.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/aug/05/big-shake-up-in-googles-ai-team-as-deepmind-chief-executive-steps-down">Big shake-up in Google’s AI team as DeepMind chief executive steps down | AI (artificial intelligence) | The Guardian</a></li>
<li><a href="https://www.businessinsider.com/google-ai-leadership-demis-hassabis-steps-down-deepmind-ceo-2026-8">Google shakes up AI leadership. Demis Hassabis takes on broader research role, and Jeff Dean leaves.</a></li>
<li><a href="https://www.theverge.com/tech/975677/google-deepmind-ai-demis-hassabis-shakeup">Google just announced a major shakeup of its top AI leadership | The Verge</a></li>
<li><a href="https://www.nytimes.com/2026/08/05/technology/google-researchers-ai-startup.html">Four Top Google A.I. Researchers Form New Start-Up - The New York Times</a></li>
<li><a href="https://techcrunch.com/2026/08/05/jeff-dean-and-other-top-ai-researchers-are-leaving-google-to-launch-their-own-startup/">Jeff Dean and other top AI researchers are leaving Google to launch their own startup | TechCrunch</a></li>

</ul>
</details>

**Discussion**: The community expressed concern over the loss of prominent researchers, with one commenter listing many recent departures and noting no major hires. Others highlighted that Jeff Dean's departure is the bigger news, and some saw Google's investment in his new company as a positive move to retain ties.

**Tags**: `#Google DeepMind`, `#AI leadership`, `#Jeff Dean`, `#Demis Hassabis`, `#AI research`

---

<a id="item-2"></a>
## [TencentDB Agent Memory: Team-Level Memory Hub for AI Agents](https://github.com/TencentCloud/TencentDB-Agent-Memory) ⭐️ 8.0/10

TencentCloud has open-sourced TencentDB Agent Memory, a team-level memory hub for AI agents that converts conversations, docs, and code into four reusable memory assets: Chat Memory, Skill, LLM-Wiki, and Code-Graph. The repository gained 1892 stars today, reaching a total of 15170 stars. This addresses a critical need for shared, governed memory in multi-agent systems, enabling agents to reuse experience and knowledge across sessions and frameworks. It could significantly improve agent efficiency and reduce token consumption, as evidenced by reported savings of up to 61.38% tokens and a 51.52% relative improvement in task completion rate. The project is written in TypeScript and is available on GitHub and npm. It supports OpenClaw and Hermes Gateway out of the box, and is licensed under the MIT license. The memory system is designed as a layered architecture, rejecting both brute-force history accumulation and irreversible lossy summarization.

github_trending · GitHub Trending · Aug 6, 02:37

**Background**: AI agents often struggle with retaining context across sessions and sharing knowledge among team members. Traditional approaches either accumulate all history (costly) or summarize lossily (losing detail). TencentDB Agent Memory introduces a structured memory layer that categorizes information into four asset types, allowing agents to learn workflows, retain task context, and reuse past experience efficiently.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/TencentCloud/tencentdb-agent-memory">GitHub - TencentCloud/TencentDB-Agent-Memory: TencentDB Agent Memory is ...</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2668579">TencentDB Agent Memory 正式开源：让 Agent 沉淀经验，让人专注创造</a></li>
<li><a href="https://www.npmjs.com/package/@tencentdb-agent-memory/memory-tencentdb">@tencentdb-agent-memory/memory-tencentdb - npm</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Memory Management`, `#LLM`, `#Developer Tools`, `#TencentCloud`

---

<a id="item-3"></a>
## [Superpowers: Agentic Skills Framework Surges on GitHub](https://github.com/obra/superpowers) ⭐️ 8.0/10

The GitHub repository obra/superpowers has gained significant traction, with 931 stars today and a total of 267,352 stars, positioning it as a trending project. It presents an agentic skills framework and software development methodology designed for AI coding agents. This repository reflects a growing trend in AI-assisted software development, offering a structured methodology that could improve how coding agents work. Its popularity indicates strong community interest in standardizing agentic workflows, potentially influencing future development tools and practices. The framework is built on composable skills and initial instructions, targeting agents like Claude Code, Cursor, Codex, OpenCode, and Gemini CLI. It is written in Shell and has 23,890 forks, indicating active community engagement.

github_trending · GitHub Trending · Aug 6, 02:37

**Background**: Agent skills are a format originally developed by Anthropic and released as an open standard, adopted by various agent products. A software development methodology prescribes a process for developing software, often dividing the effort into smaller steps to ensure high-quality results. Superpowers combines these concepts, providing a complete methodology for coding agents.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/obra/superpowers">GitHub - obra/superpowers: An agentic skills framework ...</a></li>
<li><a href="https://grokipedia.com/page/Superpowers_agentic_skills_framework">Superpowers (agentic skills framework)</a></li>
<li><a href="https://agentskills.io/home">Agent Skills Overview - Agent Skills</a></li>

</ul>
</details>

**Tags**: `#agentic AI`, `#software development`, `#framework`, `#GitHub trending`

---

<a id="item-4"></a>
## [MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce](https://huggingface.co/papers/2607.28956) ⭐️ 8.0/10

MerchantBench introduces a 365-day order-level simulation benchmark for evaluating LLM agents' long-term coherence in e-commerce operations, grounded in 98,843 real product records and equipped with 26 tools. The benchmark evaluates eight LLMs under two agent frameworks across 48 runs, revealing that the best LLM achieves only 27.3% of the mean final net assets of human participants. This benchmark addresses a critical gap in LLM agent evaluation by focusing on long-term coherence, which is essential for real-world deployments where actions have delayed consequences and require adaptive decision-making. It provides a realistic and challenging testbed that could drive improvements in LLM agents for complex, persistent environments, impacting both AI research and practical e-commerce operations. The simulation includes product sourcing, listing and pricing control, cash-flow management, and mixed-latency feedback adaptation, with actions constraining future choices and feedback arriving at heterogeneous delays. The benchmark uses 98,843 real e-commerce product records and 26 tools, and evaluates eight LLMs under two agent frameworks in 48 runs, each spanning 365 simulated days.

huggingface_papers · Hugging Face Papers · Aug 5, 00:00

**Background**: LLM agents are increasingly used as autonomous tool users, but most benchmarks evaluate bounded tasks with immediate success criteria. Long-term coherence, the ability to maintain purposeful behavior over extended horizons while adapting to accumulated evidence, is crucial for real-world applications like e-commerce, where decisions are interdependent and feedback is delayed. MerchantBench provides a persistent simulation environment to measure this capability, comparing LLM agents against human performance.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.28956">[2607.28956] MerchantBench: Benchmarking LLM Agents for Long-Term ...</a></li>
<li><a href="https://huggingface.co/papers/2607.28956">Paper page - MerchantBench: Benchmarking LLM Agents for Long-Term ...</a></li>
<li><a href="https://arxiv.org/html/2607.28956">MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E ...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#benchmark`, `#e-commerce`, `#long-term coherence`, `#AI evaluation`

---

<a id="item-5"></a>
## [JoyAI-Video-Edit: Real-Time 720p Video Editing at 30 FPS](https://huggingface.co/papers/2608.03974) ⭐️ 8.0/10

JoyAI-Video-Edit, a 16B-parameter autoregressive diffusion model, achieves real-time open-ended video editing at 720p resolution with approximately 30 FPS on a single Nvidia B200 GPU. The framework introduces chunk-wise autoregressive adaptation, Source-Anchored Distribution Matching Distillation (SA-DMD), and Long-Horizon Autoregressive Distillation to enable low-latency causal generation without future frames. This work significantly advances real-time video editing by achieving high-quality results on a single GPU, making it accessible for practical applications. It addresses key challenges like temporal consistency and source fidelity, potentially enabling interactive video editing tools and real-time content creation. The model uses a two-step generation process via SA-DMD to preserve source fidelity, and Long-Horizon Autoregressive Distillation mitigates accumulated temporal drift. The code is open-sourced on GitHub, and the system outperforms existing streaming editors while remaining competitive with offline systems on both short and long videos.

huggingface_papers · Hugging Face Papers · Aug 5, 00:00

**Background**: Autoregressive diffusion models combine autoregressive factorization with diffusion-based denoising to generate sequences efficiently. Distribution Matching Distillation (DMD) is a technique that distills multi-step diffusion models into few-step variants for faster inference. Real-time video editing requires low-latency causal generation with bounded computational resources while preserving source fidelity and long-term temporal consistency.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2511.13649">[2511.13649] Distribution Matching Distillation Meets ... [2602.03139] Diversity-Preserved Distribution Matching ... Images GitHub - tianweiy/DMD2: (NeurIPS 2024 Oral ) Improved ... One-step Diffusion with Distribution Matching Distillation arXiv:2311.18828v3 [cs.CV] 5 Dec 2023 - GitHub Pages CVPR 2026 Open Access Repository</a></li>
<li><a href="https://arxiv.org/abs/2602.03139">[2602.03139] Diversity-Preserved Distribution Matching ... Images GitHub - tianweiy/DMD2: (NeurIPS 2024 Oral ) Improved ... One-step Diffusion with Distribution Matching Distillation arXiv:2311.18828v3 [cs.CV] 5 Dec 2023 - GitHub Pages CVPR 2026 Open Access Repository</a></li>
<li><a href="https://arxiv.org/abs/2605.11596">[2605.11596] HorizonDrive: Self-Corrective Autoregressive ...</a></li>

</ul>
</details>

**Tags**: `#video editing`, `#diffusion models`, `#real-time`, `#autoregressive`, `#AI/ML`

---

<a id="item-6"></a>
## [NVIDIA Vera Whitepaper Under Fire for Benchmark and Security Claims](https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread) ⭐️ 8.0/10

Chips and Cheese published a critical analysis of NVIDIA's Vera whitepaper, questioning the validity of its 'agentic benchmarks' and highlighting potential security concerns related to speculative execution. The article argues that the benchmarks are misleading and that the CPU's design prioritizes performance over security. This analysis matters because NVIDIA's Vera CPU is a major product for the AI data center market, and its benchmark claims influence purchasing decisions. The criticism could affect NVIDIA's reputation and prompt a broader discussion about the transparency and security of next-generation AI hardware. The whitepaper labels SPEC CPU 2026 results as 'agentic benchmarks,' but the analysis argues this is misleading because they only approximate a subset of agentic workloads. Additionally, the Vera CPU's reliance on speculative execution raises security concerns, as noted by community members, especially in the context of agentic AI systems.

hackernews · pella · Aug 5, 21:24 · [Discussion](https://news.ycombinator.com/item?id=49189234)

**Background**: NVIDIA's Vera CPU is part of the Vera Rubin platform, designed for agentic AI workloads in data centers. The whitepaper claims significant IPC gains over previous generations, but the benchmarks were run on reference hardware that was not generally available. Speculative execution is a common CPU optimization technique but has been a source of security vulnerabilities, such as Spectre and Meltdown.

<details><summary>References</summary>
<ul>
<li><a href="https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread">NVIDIA’s Vera Whitepaper Has a Thread Loose</a></li>
<li><a href="https://www.tomshardware.com/pc-components/cpus/nvidia-spills-the-beans-on-vera-cpu-spec-benchmarks-revealed-olympus-architecture-detailed-and-more">Nvidia deep dives Vera CPU for AI data centers — SPEC CPU 2026 benchmarks revealed, Olympus architecture specifics, and more | Tom's Hardware</a></li>
<li><a href="https://www.servethehome.com/diving-deeper-on-nvidias-vera-cpu-new-architectural-details-and-spec-cpu-2026-benchmarks/">Diving Deeper on NVIDIA's Vera CPU: New Architectural Details and SPEC CPU 2026 Benchmarks - ServeTheHome</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some defend NVIDIA's benchmark choices as practical, while others criticize the company's marketing history and security trade-offs. One commenter appreciates the technical depth, while another expresses skepticism about NVIDIA's claims, citing past controversies.

**Tags**: `#NVIDIA`, `#hardware`, `#benchmarks`, `#security`, `#speculation`

---

<a id="item-7"></a>
## [Cloudflare OS: Open Platform for Agents and Apps](https://blog.cloudflare.com/cloudflare-os/) ⭐️ 8.0/10

Cloudflare announced Cloudflare OS, an open-source platform built on Workers that combines an agent workspace, a security and governance framework, and a platform for personal, modifiable apps. It is positioned as an AI operating system for companies, enabling employees to build apps and automate work. This marks a significant move by Cloudflare to integrate AI deeply into its platform, potentially reshaping how companies build and deploy internal tools. It also revives the vision of Sandstorm, an earlier open platform, but with modern AI capabilities, which could influence the broader trend of AI-driven work platforms. Cloudflare OS consists of three parts: an agent workspace with an isolated runtime for code execution, a security and governance framework for safe access to internal data, and a platform for building and sharing modifiable apps. It is open-source and leverages Cloudflare Workers, with a public site at os.cloudflare.app.

hackernews · speckx · Aug 5, 13:58 · [Discussion](https://news.ycombinator.com/item?id=49182996)

**Background**: Cloudflare Workers is a serverless execution environment that allows developers to run code at the edge. Sandstorm, created by Cloudflare's Kenton Varda, was an earlier open-source platform for running web apps on personal servers, but it was discontinued. Cloudflare OS appears to be a modern reinterpretation of Sandstorm, built on Workers and enhanced with AI capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/cloudflare-os/">Cloudflare OS: an open platform for agents, apps, and work | The Cloudflare Blog</a></li>
<li><a href="https://www.phoronix.com/news/Cloudflare-OS">Cloudflare Announces Open-Source Cloudflare OS As AI "Operating System" - Phoronix</a></li>
<li><a href="https://os.cloudflare.app/">Cloudflare OS</a></li>

</ul>
</details>

**Discussion**: Community comments show a mix of excitement and skepticism. Some users praised the concept, drawing parallels to Sandstorm, while others expressed concerns about vendor lock-in and the vague use of the term 'OS'. There were also technical questions about data sharing and updates in a decentralized app model.

**Tags**: `#Cloudflare`, `#AI`, `#platform`, `#agents`, `#open source`

---

<a id="item-8"></a>
## [Deno's Celld: Self-Hosted Durable Objects with SQLite and S3](https://github.com/denoland/celld) ⭐️ 8.0/10

Deno has released Celld, an open-source daemon that runs Cloudflare Workers and Durable Objects on your own machines. Each object is its own SQLite database, addressed by name and replicated to an S3-compatible bucket you own. Celld provides a portable, self-hosted alternative to Cloudflare's Durable Objects, addressing the need for multi-provider portability and data ownership. This could significantly impact developers who want to avoid vendor lock-in while using the durable object abstraction. Celld is a 58 MB static executable that can be installed via curl or Docker. It supports running Workers and Durable Objects code unchanged, with data stored in SQLite and replicated to S3-compatible storage.

hackernews · calvinfo · Aug 5, 16:50 · [Discussion](https://news.ycombinator.com/item?id=49185430)

**Background**: Durable Objects are a Cloudflare Workers feature that provides strongly consistent, single-threaded coordination and storage for distributed applications. Celld extends this concept by allowing self-hosting, using SQLite for local storage and S3 for replication, making it a portable alternative to Cloudflare's managed service.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/denoland/celld">GitHub - denoland/celld: self-hosted, distributed Durable Objects · GitHub</a></li>
<li><a href="https://celld.dev/">celld: self-hosted, distributed Durable Objects</a></li>
<li><a href="https://github.com/denoland/celld/blob/main/README.md">celld/README.md at main · denoland/celld</a></li>

</ul>
</details>

**Discussion**: The community is excited about Celld, with users praising the abstraction and the ability to run durable objects outside of a single provider. Some are curious about the differences between Celld and Cloudflare's open-source workerd, while others note the practical benefits for self-hosting and cost savings.

**Tags**: `#distributed-systems`, `#durable-objects`, `#self-hosted`, `#sqlite`, `#deno`

---

<a id="item-9"></a>
## [Position Paper: LLMs Can't Jump in Scientific Discovery](https://openreview.net/challenge?redirect=%2Fforum%3Fid%3DklU4737opt) ⭐️ 8.0/10

DeepMind researcher Tom Zahavy published a position paper titled 'LLMs Can't Jump' arguing that large language models have fundamental limitations in scientific discovery, sparking a rich community debate on the role of language in human experience and scientific reasoning. This paper challenges the prevailing optimism about AI for science, prompting researchers to reconsider the true capabilities and limitations of LLMs in driving scientific breakthroughs. The high engagement (247 points, 170 comments) indicates significant interest and potential impact on future research directions in AI and scientific discovery. The paper argues that language is a lossy encoding of human experience, and that scientific discovery often relies on non-linguistic intuition and leaps of insight that LLMs cannot replicate. The author, Tom Zahavy, clarified on Twitter that the paper does not claim LLMs can never make real scientific discoveries, but rather highlights their limitations.

hackernews · theanonymousone · Aug 5, 11:01 · [Discussion](https://news.ycombinator.com/item?id=49181083)

**Background**: Large language models (LLMs) like GPT-4 have shown impressive capabilities in various tasks, including scientific text analysis and hypothesis generation. However, their ability to perform genuine scientific discovery, which often requires creative leaps and non-verbal reasoning, remains debated. This position paper contributes to that debate by arguing that LLMs are fundamentally limited in this regard.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s44387-025-00019-5">Exploring the role of large language models in the scientific ...</a></li>
<li><a href="https://arxiv.org/pdf/2507.02694">Can LLMs Identify Critical Limitations within Scientific ...</a></li>
<li><a href="https://aclanthology.org/2025.acl-long.1009/">Can LLMs Identify Critical Limitations within Scientific ...</a></li>

</ul>
</details>

**Discussion**: Community comments reflect a mix of agreement and skepticism. Some users support the idea that language is lossy and LLMs lack intuitive leaps, while others criticize the paper for lacking quantitative evidence and being one person's opinion. The author's clarification that the paper is not anti-LLM but highlights limitations was also noted.

**Tags**: `#LLM`, `#AI for Science`, `#Position Paper`, `#DeepMind`, `#Scientific Discovery`

---

<a id="item-10"></a>
## [Webhook Limitations and a Streaming GET Proposal](https://weli.dev/blog/the-valley-of-webhooks/) ⭐️ 8.0/10

The article 'The Valley of Webhooks' analyzes the problems of using webhooks for state synchronization and proposes a streaming GET-based protocol similar to an IETF draft called SCROLL. The proposal suggests using a GET request with a 'Prefer: stream' header to establish a persistent connection for continuous updates. This matters because webhooks are widely used but have inherent issues like reliability, ordering, and state consistency. A standardized streaming GET approach could offer a more robust alternative, potentially influencing API design and real-time data synchronization across the industry. The proposed SCROLL protocol is remarkably similar to the actual IETF draft 'Braid-HTTP Subscriptions' being presented at IETF 127. Both drafts use a GET request with a header to request a subscription, enabling a stream of updates over a single connection.

hackernews · weli · Aug 5, 15:22 · [Discussion](https://news.ycombinator.com/item?id=49184216)

**Background**: Webhooks are HTTP callbacks that notify clients of events, but they suffer from issues like lack of ordering, duplicate delivery, and difficulty in maintaining consistent state. Streaming GET protocols, such as those being standardized by the IETF, aim to provide a more reliable and efficient way to synchronize state over HTTP by maintaining a persistent connection and pushing updates.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49187511">This is a nice writeup of the problems in using Webhooks for State ...</a></li>
<li><a href="https://signalwire.com/c/twilio-migration-guide">Stop Reconstructing Call State From Webhooks . | SignalWire</a></li>
<li><a href="https://github.com/arabcoders/watchstate/discussions/697">Webhook state not updating local metadata · arabcoders watchstate...</a></li>

</ul>
</details>

**Discussion**: Community comments highlight real-world webhook issues, such as QuickBooks returning errors while still creating entities, and concerns about the efficiency of persistent connections for low-frequency events. Some prefer cursor-paginated APIs or suggest using webhooks as a 'poke' to supplement polling, while others note the need for IETF standardization to gain adoption.

**Tags**: `#webhooks`, `#API design`, `#state synchronization`, `#protocols`, `#real-time`

---

<a id="item-11"></a>
## [Rubin Observatory Releases First LSST Camera Data: 500k Galaxies in COSMOS Field](https://rubinobservatory.org/news/rubin-new-window-cosmos-field) ⭐️ 8.0/10

The Vera C. Rubin Observatory has released its first dataset from the LSST Camera, capturing approximately 500,000 galaxies in the COSMOS field. This marks the first public data release from the camera, which is designed to survey the entire sky repeatedly over a decade. This release demonstrates the LSST Camera's unprecedented wide-field imaging capability, which will enable transformative studies in dark energy, dark matter, and galactic evolution. It provides the scientific community with a massive, high-quality dataset that will drive discoveries for years to come. The LSST Camera has a 64 cm diameter focal plane with 0.2 arcsecond sampling and covers wavelengths from 400nm to 1060nm in five or more bands. The COSMOS field is a 2 square degree region in the constellation Sextans, previously studied by the Hubble Space Telescope.

hackernews · MarcoDewey · Aug 5, 14:04 · [Discussion](https://news.ycombinator.com/item?id=49183079)

**Background**: The Vera C. Rubin Observatory, formerly known as the Large Synoptic Survey Telescope (LSST), is an astronomical observatory under construction in Chile, funded by the NSF and DOE. Its primary instrument, the LSST Camera, is the largest digital camera ever built for astronomy, designed to capture the entire visible sky every few nights. The COSMOS field is a well-studied patch of sky used for deep extragalactic surveys, providing a benchmark for testing new instruments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vera_C._Rubin_Observatory">Vera C. Rubin Observatory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/COSMOS_field">COSMOS field</a></li>
<li><a href="https://www.lsst.org/gallery/camera">LSST Camera</a></li>

</ul>
</details>

**Discussion**: Community members expressed excitement about the data, with one user noting the camera's ability to capture the entire sky in a time-lapse manner over 10 years. Another user identified potential processing artifacts in the images, such as a bright blue segment and blue filter artifacts on starbursts, and shared labeled screenshots for discussion. A third user provided a link to view the data using the Aladin Sky Atlas viewer.

**Tags**: `#astronomy`, `#LSST`, `#Rubin Observatory`, `#data release`, `#scientific imaging`

---

<a id="item-12"></a>
## [AI Cracks Legendary Erdős Problems, Shifting Math Research](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/) ⭐️ 8.0/10

AI systems are increasingly solving long-standing Erdős problems, a collection of over a thousand mathematical conjectures proposed by Paul Erdős. This marks a notable shift in mathematical research capabilities, as AI demonstrates the ability to tackle problems that have stumped human mathematicians for decades. This trend could revolutionize mathematical research by accelerating problem-solving and potentially uncovering new insights. It raises important questions about the role of human mathematicians, the nature of mathematical understanding, and how AI-generated proofs can be verified and utilized. The article highlights that AI's success stems from a combination of broad mathematical familiarity and stamina in working through details. An obvious area for improvement is automated generation of new conjectures and attempts to prove or disprove them, with discovered arguments then being used to further advance the field.

hackernews · pseudolus · Aug 5, 11:49 · [Discussion](https://news.ycombinator.com/item?id=49181519)

**Background**: Paul Erdős was a prolific Hungarian mathematician known for his vast output of conjectures and collaborations. The Erdős problems are a collection of open problems he posed across various fields of mathematics, many of which remain unsolved. AI's recent successes in solving these problems represent a significant milestone in the intersection of artificial intelligence and mathematics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Erdős_problems">Erdős problems</a></li>
<li><a href="https://teorth.github.io/erdosproblems/?status=solved">Erdős Problems Database - Interactive Table</a></li>
<li><a href="https://www.forbes.com/sites/anishasircar/2026/04/17/ai-solved-a-mathematical-problem-that-had-stumped-the-worlds-best-minds-for-decades/">AI Solved A Mathematical Problem That Had Stumped ... - Forbes</a></li>

</ul>
</details>

**Discussion**: Community comments express both fascination and concern. Some worry that AI-generated proofs may be too complex for humans to understand, questioning their practical utility. Others note that AI's success extends beyond Erdős problems and speculate about the impact on other scientific fields, while some find the human story of Erdős himself intriguing.

**Tags**: `#AI`, `#mathematics`, `#research`, `#machine learning`, `#Erdős problems`

---

<a id="item-13"></a>
## [Painting with Gaussians: A New Image Stylization Technique](https://yogthos.net/posts/2026-08-03-splat-painter.html) ⭐️ 8.0/10

A blog post demonstrates a novel technique for converting photos into painterly images using Gaussian splatting, a method typically used for 3D scene rendering. The post shows results that impress commenters, with some noting it looks better than traditional painting effects in image editors. This technique offers a fresh approach to image stylization, potentially providing more realistic and aesthetically pleasing results than existing methods. It highlights the versatility of Gaussian splatting beyond 3D rendering, opening up new creative possibilities for artists and developers. The technique uses Gaussian splatting to encode brush strokes, with some commenters noting that it exaggerates depth of field in backgrounds, leading to a posterized look. One commenter suggests using images without heavy bokeh for better results, while another proposes using the technique to generate training pairs for image generation models.

hackernews · yogthos · Aug 5, 13:34 · [Discussion](https://news.ycombinator.com/item?id=49182695)

**Background**: Gaussian splatting is a rasterization technique introduced in the early 1990s and revitalized in 2023 by a research group from Inria, offering real-time rendering of photorealistic scenes. It is an alternative to NeRF-like models for 3D scene representation. Painterly image stylization has been explored through stroke-based rendering algorithms, but this post applies Gaussian splatting in a novel way.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_splatting">Gaussian splatting - Wikipedia</a></li>
<li><a href="https://towardsdatascience.com/a-comprehensive-overview-of-gaussian-splatting-e7d570081362/">A Comprehensive Overview of Gaussian Splatting | Towards Data Science</a></li>
<li><a href="https://huggingface.co/blog/gaussian-splatting">Introduction to 3D Gaussian Splatting</a></li>

</ul>
</details>

**Discussion**: Commenters are generally positive, with one saying results look 'way better than I was expecting.' However, some critique the technique's handling of depth of field, noting it can exaggerate bokeh and create a posterized effect. A commenter suggests using images without heavy bokeh, while another proposes using the technique to generate training data for image generation models.

**Tags**: `#Gaussian splatting`, `#image stylization`, `#computer graphics`, `#machine learning`, `#creative coding`

---

<a id="item-14"></a>
## [Meta Ran Ads Containing AI-Generated Child Sexual Abuse Imagery](https://www.wired.com/story/meta-ran-ads-that-contained-ai-generated-child-sexual-abuse-imagery/) ⭐️ 8.0/10

Meta reportedly ran advertisements that contained AI-generated child sexual abuse imagery, as revealed by a Wired investigation. This raises serious concerns about the platform's content moderation systems and their ability to detect AI-generated harmful content. This incident highlights systemic failures in Meta's content moderation, especially regarding AI-generated CSAM, which is a growing problem across platforms. It underscores the need for stronger enforcement and accountability, as such content can cause severe harm and legal consequences. The ads reportedly slipped past Meta's automated moderation systems, which rely on AI tools like computer vision and natural language processing. The investigation suggests that these systems may not be adequately trained to detect AI-generated CSAM, and that human oversight may be insufficient.

hackernews · malshe · Aug 5, 19:47 · [Discussion](https://news.ycombinator.com/item?id=49187977)

**Background**: AI-generated child sexual abuse material (AI CSAM) is a rapidly growing concern, with organizations like the Internet Watch Foundation reporting thousands of realistic AI-generated images and videos. Meta uses AI-based content moderation tools to scan for such content, but this incident shows that gaps remain. The company has faced criticism for prioritizing profit over safety, and this case adds to that narrative.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2510.02978v1">AI Generated Child Sexual Abuse Material—What’s the Harm?</a></li>
<li><a href="https://www.iwf.org.uk/about-us/why-we-exist/our-research/how-ai-is-being-abused-to-create-child-sexual-abuse-imagery/">AI-Generated Child Sexual Abuse: 2026 Report on Trends, Data ...</a></li>
<li><a href="https://blog.com.bot/meta-ai-content-moderation/">Meta AI : Role, Tools, and Limitations in Content Moderation</a></li>

</ul>
</details>

**Discussion**: Community comments express frustration and skepticism about Meta's moderation efforts, with users noting that similar issues occur on other platforms like YouTube. Some commenters argue that fines are merely a cost of doing business for Meta, and that stronger punishments are needed to force change. Others highlight broader problems, such as ads promoting violence or scams, indicating a systemic failure in ad moderation.

**Tags**: `#AI safety`, `#content moderation`, `#Meta`, `#ethics`, `#online safety`

---

<a id="item-15"></a>
## [build2 Claims Faster Than Ninja in Detailed Performance Analysis](https://build2.org/blog/faster-than-ninja.xhtml) ⭐️ 8.0/10

The build2 project published a blog post titled 'Faster Than Ninja' presenting a detailed performance analysis claiming build2 outperforms Ninja in certain build scenarios. The post includes methodology and benchmarks, sparking discussion among build system developers. This comparison is significant because Ninja is widely regarded as the de facto standard for fast builds, especially in large projects like Chromium. If build2 can genuinely surpass Ninja's performance, it could influence build system choices and drive further optimization in the ecosystem. The post details how build2 achieves speed by leveraging its own file cache with optional compression, and it compares against Ninja's approach of avoiding work by limiting scope. The author acknowledges that Ninja's speed comes partly from 'cheating' by not handling certain tasks, making it a challenging target to race.

hackernews · elasticdog · Aug 5, 13:33 · [Discussion](https://news.ycombinator.com/item?id=49182685)

**Background**: Ninja is a build system designed for speed, often used with higher-level generators like CMake or Meson. It focuses on fast incremental builds by minimizing work. build2 is a newer build system that aims to be a complete solution, including dependency management and more features, which may add overhead but also opportunities for optimization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ninja_(build_system)">Ninja (build system) - Wikipedia</a></li>
<li><a href="https://ninja-build.org/">Ninja, a small build system with a focus on speed</a></li>
<li><a href="https://ninja-build.org/manual.html">The Ninja build system</a></li>

</ul>
</details>

**Discussion**: Comments from the Ninja author (evmar) appreciate the deep dive and note that Ninja's speed comes from avoiding work, making it a good benchmark target. Other users question the fairness of comparisons, such as CMake's generation time, and wonder how build2 compares to Tup. Some also discuss technical details like compression algorithms and the lack of --help in modern build systems.

**Tags**: `#build systems`, `#performance`, `#C++`, `#Ninja`, `#build2`

---