---
layout: default
title: "Horizon Summary: 2026-06-16 (EN)"
date: 2026-06-16
lang: en
---

> From 150 items, 15 important content pieces were selected

---

1. [Backdoor Hidden in Fake LinkedIn Job Offer via npm](#item-1) ⭐️ 9.0/10
2. [US orders Anthropic to block foreign nationals from Fable 5](#item-2) ⭐️ 9.0/10
3. [NVIDIA Releases SkillSpector: Security Scanner for AI Agent Skills](#item-3) ⭐️ 8.0/10
4. [Microsoft Launches Free AI Agents Course](#item-4) ⭐️ 8.0/10
5. [OmniDirector: Multi-Shot Camera Cloning Without Paired Data](#item-5) ⭐️ 8.0/10
6. [APPO: Fine-Grained Credit Assignment for LLM Agent RL](#item-6) ⭐️ 8.0/10
7. [Developers share local model setups for daily coding](#item-7) ⭐️ 8.0/10
8. [Peopleless Economy: Feasible but Disruptive](#item-8) ⭐️ 8.0/10
9. [Fox Reportedly Acquiring Roku Raises Neutrality Concerns](#item-9) ⭐️ 8.0/10
10. [Salesforce Acquires Fin (Intercom) for $3.6B](#item-10) ⭐️ 8.0/10
11. [TimescaleDB Hypercore Compression Deep Dive](#item-11) ⭐️ 8.0/10
12. [Rust vs C/C++ Memory Safety CVEs: A Nuanced Analysis](#item-12) ⭐️ 8.0/10
13. [CrankGPT: Hand-Cranked AI Assistant](#item-13) ⭐️ 8.0/10
14. [Reddit Post Urges Users to Stop Using Ollama](#item-14) ⭐️ 8.0/10
15. [Evalatro: Open Benchmark Where LLMs Play Balatro](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Backdoor Hidden in Fake LinkedIn Job Offer via npm](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 9.0/10

A detailed account reveals a backdoor hidden in a fake LinkedIn job offer's code review task, exploiting npm's prepare script to execute arbitrary code when a developer runs npm install. This novel social engineering attack combines fake job offers with an npm supply chain backdoor, posing a serious threat to developers and companies, as it exploits trust in recruitment processes and common development workflows. The backdoor is buried in commented-out test code within a public GitHub repository, and npm's prepare script runs automatically after npm install, so simply installing dependencies triggers the malicious code.

hackernews · lwhsiao · Jun 15, 20:00 · [Discussion](https://news.ycombinator.com/item?id=48546294)

**Background**: npm is a package manager for JavaScript, and its prepare script is a lifecycle hook that runs automatically after npm install in certain contexts. Supply chain attacks target the software supply chain by compromising dependencies or development tools. Social engineering attacks manipulate people into performing actions that compromise security.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v11/using-npm/scripts/">Scripts | npm Docs</a></li>
<li><a href="https://medium.com/works-on-my-machine/the-axios-npm-supply-chain-attack-what-happened-how-to-check-if-you-were-hit-and-what-to-do-now-2bcc10ba2460">The Axios npm Supply Chain Attack What Happened, How... | Medium</a></li>

</ul>
</details>

**Discussion**: Community comments express concern that this attack is uncomfortably close to normal interview tasks, with multiple users reporting similar experiences. Users criticize GitHub and LinkedIn for not removing the malicious repo and profile, and call for better reporting mechanisms for cybercrime.

**Tags**: `#supply chain attack`, `#social engineering`, `#npm security`, `#cybercrime`, `#job scam`

---

<a id="item-2"></a>
## [US orders Anthropic to block foreign nationals from Fable 5](https://www.reddit.com/r/artificial/comments/1u6lqp6/nobodys_talking_about_the_real_precedent_in_the/) ⭐️ 9.0/10

On June 12, the US Commerce Department ordered Anthropic to suspend access to its Fable 5 and Mythos 5 AI models for all foreign nationals, including non-citizens inside the US, citing national security concerns after Amazon reported a potential jailbreak. Unable to enforce nationality-based restrictions in real time, Anthropic disabled both models globally. This marks the first time US export controls have targeted an AI model itself rather than hardware, setting a precedent for nationality-based access rules that cannot be geographically enforced. It raises critical questions about identity infrastructure for AI access and the legal privilege of AI interactions. Anthropic received about 90 minutes' notice with no prior warning, and the trigger was reportedly a phone call from Amazon CEO Andy Jassy to Treasury Secretary Scott Bessent. The White House claims a trusted partner found a real jailbreak, while Anthropic argues the vulnerabilities were minor and already known in other public models like GPT-5.5.

reddit · r/artificial · /u/TheOnlyVibemaster · Jun 15, 16:36

**Background**: Export controls on AI have historically focused on hardware like chips, which are easier to track. This order extends controls to the model itself, treating frontier AI as a controlled national-security asset. A nationality-based rule that covers foreign nationals inside the US cannot be enforced via IP geoblocking, potentially requiring identity verification for AI access.

<details><summary>References</summary>
<ul>
<li><a href="https://thenextweb.com/news/anthropic-foreign-access-block-us-reversal">US order to block foreign access to Anthropic’s top models marks...</a></li>
<li><a href="https://cryptobriefing.com/anthropic-shuts-down-ai-models-us-ban/">Anthropic shuts down access to AI models after US government ban...</a></li>
<li><a href="https://particle.news/story/us-orders-anthropic-to-suspend-access-to-fable-5-and-mythos-5">Particle: U.S. Orders Anthropic to Suspend Access to Fable 5 and...</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion highlights the unprecedented nature of nationality-based AI access controls and the enforcement challenges. Commenters express concern that this sets a dangerous precedent for identity verification requirements and erodes privacy, with some noting that AI chats already lack legal privilege. There is debate over whether the jailbreak was genuine or a pretext.

**Tags**: `#AI regulation`, `#export controls`, `#national security`, `#Anthropic`, `#identity infrastructure`

---

<a id="item-3"></a>
## [NVIDIA Releases SkillSpector: Security Scanner for AI Agent Skills](https://github.com/NVIDIA/SkillSpector) ⭐️ 8.0/10

NVIDIA has open-sourced SkillSpector, a Python-based CLI security scanner that detects vulnerabilities and malicious patterns in AI agent skills before installation. As AI agents become more prevalent, the ability to vet third-party skills for security risks is critical; SkillSpector addresses a growing need for trust and safety in the AI ecosystem. SkillSpector accepts input from Git repositories, URLs, zip files, directories, and single files, and provides a pipeline for extending analysis capabilities.

github_trending · GitHub Trending · Jun 16, 04:20

**Background**: AI agent skills are modular components that extend agent capabilities, similar to plugins. However, they can introduce security risks such as prompt injection or data exfiltration. SkillSpector helps developers and users evaluate whether a skill is safe to install.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NVIDIA/SkillSpector">GitHub - NVIDIA / SkillSpector : Security scanner for AI agent skills .</a></li>
<li><a href="https://docs.nvidia.com/skills/scanning-agent-skills">Scan Agent Skills Before Installation | NVIDIA Skill Documentation</a></li>
<li><a href="https://www.everydev.ai/tools/skillspector">SkillSpector - AI Agent Skills Security Scanner | EveryDev.ai</a></li>

</ul>
</details>

**Tags**: `#AI Security`, `#Vulnerability Detection`, `#NVIDIA`, `#Python`, `#AI Agents`

---

<a id="item-4"></a>
## [Microsoft Launches Free AI Agents Course](https://github.com/microsoft/ai-agents-for-beginners) ⭐️ 8.0/10

Microsoft has released a free, 12-lesson course titled 'AI Agents for Beginners' on GitHub, designed to teach beginners how to build AI agents. The repository has gained over 67,000 stars and 22,000 forks, with 100 new stars today. This course provides a structured, accessible entry point into the rapidly growing field of AI agents, which are increasingly used for automation and task completion. Microsoft's backing and the high community engagement signal strong demand for practical AI education. The course is hosted on GitHub as a Jupyter Notebook-based repository, making it interactive and hands-on. It covers 12 lessons that guide learners from fundamentals to building functional AI agents.

github_trending · GitHub Trending · Jun 16, 04:20

**Background**: AI agents are software systems that use generative AI to pursue goals, use tools, and take actions autonomously within human-defined constraints. Jupyter Notebook is an open-source web-based interactive computing environment widely used for data science and education.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent</a></li>
<li><a href="https://en.wikipedia.org/wiki/Jupyter_Notebook">Jupyter Notebook</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Education`, `#Microsoft`, `#Jupyter Notebook`, `#GitHub Trending`

---

<a id="item-5"></a>
## [OmniDirector: Multi-Shot Camera Cloning Without Paired Data](https://huggingface.co/papers/2606.13432) ⭐️ 8.0/10

Researchers propose OmniDirector, a unified framework that uses grid motion videos to represent camera parameters and integrates multimodal diffusion transformers for multi-shot video generation without requiring cross-paired data. This work addresses the data scarcity and multi-shot generation limitations of existing camera motion cloning methods, enabling more precise and flexible control over video generation, which could benefit filmmakers and content creators. The camera grid representation encodes camera parameters as visual grid motion videos, supporting diverse trajectory integration for multi-shot generation. OmniDirector is trained on a million-scale camera grid-video pairs and includes a hierarchical prompt expansion agent for harmonizing control signals.

huggingface_papers · Hugging Face Papers · Jun 15, 00:00

**Background**: Camera motion cloning aims to transfer the camera movement from a reference video to a new scene. Existing methods often rely on parametric representations that struggle with multi-shot videos or require synthetic cross-paired data, which is scarce and limits performance. Multimodal diffusion transformers are a recent advancement that jointly model multiple modalities (e.g., text, image, video) for generative tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.13432">[2606.13432] OmniDirector: General Multi - Shot Camera Cloning ...</a></li>
<li><a href="https://huggingface.co/papers/2606.13432">Paper page - OmniDirector: General Multi - Shot Camera Cloning ...</a></li>
<li><a href="https://hyper.ai/en/papers/2606.13432">OmniDirector: General Multi - Shot Camera Cloning without... | HyperAI</a></li>

</ul>
</details>

**Tags**: `#video generation`, `#camera motion cloning`, `#diffusion transformers`, `#computer vision`, `#AI`

---

<a id="item-6"></a>
## [APPO: Fine-Grained Credit Assignment for LLM Agent RL](https://huggingface.co/papers/2606.12384) ⭐️ 8.0/10

Researchers propose Agentic Procedural Policy Optimization (APPO), a novel reinforcement learning method that improves multi-turn tool-use in LLM agents by refining credit assignment and branching decisions at fine-grained decision points rather than coarse interaction units. APPO addresses the credit assignment problem in agentic RL, enabling more efficient training of LLM agents for complex multi-turn tasks, which is crucial for advancing autonomous AI systems that can use tools and interact over multiple steps. APPO uses a Branching Score combining token uncertainty with policy-induced likelihood gains to select branching locations, and introduces procedure-level advantage scaling to better distribute credit across branched rollouts. Experiments on 13 benchmarks show consistent improvements of nearly 4 points over strong baselines.

huggingface_papers · Hugging Face Papers · Jun 15, 00:00

**Background**: Reinforcement learning (RL) trains agents to maximize rewards through interaction. In LLM agents, the credit assignment problem refers to determining which actions in a sequence of tool calls and decisions lead to successful outcomes. Existing methods often assign credit over coarse units like tool-call boundaries, missing fine-grained influences.

<details><summary>References</summary>
<ul>
<li><a href="https://nick-baliesnyi.medium.com/self-attentional-credit-assignment-in-reinforcement-learning-1080c97535f6">Self-Attentional Credit Assignment in Reinforcement Learning</a></li>
<li><a href="https://ai.stackexchange.com/questions/12908/what-is-the-credit-assignment-problem">reinforcement learning - What is the credit assignment problem?</a></li>
<li><a href="https://inclusionai.github.io/AReaL/tutorial/agentic_rl.html">Agentic Reinforcement Learning — AReaL Documentation</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#LLM agents`, `#credit assignment`, `#tool-use`

---

<a id="item-7"></a>
## [Developers share local model setups for daily coding](https://news.ycombinator.com/item?id=48542100) ⭐️ 8.0/10

Developers on Hacker News are sharing their experiences and setups for replacing cloud-based coding assistants like Claude and GPT with local models such as Qwen and Gemma for daily coding tasks. This shift could reduce reliance on paid subscriptions and improve data privacy, making powerful coding assistance more accessible and secure for individual developers. Users report using models like Qwen3.6 35B and Gemma 4 26B with setups like the Pi coding harness and unsloth studio, achieving speeds around 150 tokens per second on dual RTX 3090s.

hackernews · cloudking · Jun 15, 14:46

**Background**: Local large language models (LLMs) run on a user's own hardware instead of cloud servers, offering privacy and offline use. Qwen is an open-source LLM family by Alibaba Cloud, while Gemma is Google's lightweight open model series. Tokens per second (tok/s) measures inference speed.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://deepmind.google/models/gemma/">Gemma — Google DeepMind</a></li>

</ul>
</details>

**Discussion**: The community is divided: some users successfully replaced Claude/GPT and praise the privacy and cost benefits, while others argue that frontier models still outperform local ones significantly, making the switch not worth the effort for now.

**Tags**: `#local LLMs`, `#coding assistant`, `#privacy`, `#open source models`, `#developer tools`

---

<a id="item-8"></a>
## [Peopleless Economy: Feasible but Disruptive](https://gmalandrakis.com/writings/ad-economicum.html) ⭐️ 8.0/10

An article explores the technical feasibility of a peopleless economy driven by AI and automation, questioning whether human labor will become obsolete and how society might adapt. This discussion challenges fundamental assumptions about work, value, and distribution, potentially reshaping economic policy and societal structures as AI advances. The article argues that a peopleless economy is not technically impossible, but it would require rethinking concepts like consumer demand, income distribution, and governance.

hackernews · l0new0lf-G · Jun 15, 21:10 · [Discussion](https://news.ycombinator.com/item?id=48547062)

**Background**: The concept of a peopleless economy imagines a future where AI and robots perform all productive work, eliminating the need for human labor. This raises questions about how people would earn income and what role consumption would play in such a system.

**Discussion**: Commenters debate whether AI will concentrate wealth like previous capital, with some arguing it will lead to extreme inequality and others questioning the assumption that governments will not intervene. Some note that labor becoming less valuable and capital more valuable is a likely outcome.

**Tags**: `#AI`, `#economics`, `#automation`, `#future of work`, `#technology impact`

---

<a id="item-9"></a>
## [Fox Reportedly Acquiring Roku Raises Neutrality Concerns](https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9) ⭐️ 8.0/10

Fox is reportedly in talks to acquire Roku, the leading streaming hardware platform in the US, according to the Wall Street Journal. This deal would give a major content provider direct control over a TV operating system used in millions of households. If completed, the acquisition could undermine Roku's platform neutrality, potentially allowing Fox to prioritize its own content and ads over competitors. This raises antitrust concerns and could reshape the streaming hardware landscape, affecting consumers and rival services. Roku has historically maintained a service-agnostic architecture, but recent moves like in-platform ads and content partnerships have already drawn criticism. The deal's financial terms have not been disclosed, and it may face regulatory scrutiny given Roku's market share of 30-50% of US households.

hackernews · thm · Jun 15, 12:50 · [Discussion](https://news.ycombinator.com/item?id=48540499)

**Background**: Roku is a streaming device and platform company that powers the connected TV advertising ecosystem. Its business model relies on selling hardware at low margins while generating profit through platform fees, ads, and licensing. Platform neutrality—treating all streaming services equally—has been a key selling point for Roku, making it attractive to both consumers and content providers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.enveu.com/compare/roku-vs-fire-tv">Roku vs Fire TV for OTT: Key Differences Explained</a></li>
<li><a href="https://fasterthannormal.co/businesses/roku">Roku — Business Strategy Analysis | Faster Than Normal</a></li>
<li><a href="https://pratsdigital.in/roku-business-model-platform-strategy/">Roku Business Model: Trojan Horse of Streaming... - PratsDigital</a></li>

</ul>
</details>

**Discussion**: Community sentiment is overwhelmingly negative, with users expressing pessimism about Fox gaining direct access to Roku's user base. Commenters worry about loss of neutrality, increased ads, and potential for a 'Fox News button' on remotes. Some users have already started migrating to alternatives like Nvidia Shield to avoid platform bias.

**Tags**: `#acquisition`, `#streaming`, `#antitrust`, `#TV hardware`, `#media`

---

<a id="item-10"></a>
## [Salesforce Acquires Fin (Intercom) for $3.6B](https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/?bc=HL) ⭐️ 8.0/10

Salesforce has signed a definitive agreement to acquire Fin, formerly known as Intercom, for approximately $3.6 billion, aiming to strengthen its AI-powered customer service offerings. This acquisition signals major consolidation in the AI customer service space, as Salesforce competes with rising startups like Sierra and Decagon. It also marks a strategic move by CEO Marc Benioff to counter his former co-CEO Bret Taylor's company Sierra. Fin's AI platform boasts a 67% average resolution rate for complex customer queries, with some customers achieving 85%+. The deal comes just a month after Intercom rebranded to Fin, highlighting the fast-moving competitive landscape.

hackernews · colesantiago · Jun 15, 12:08 · [Discussion](https://news.ycombinator.com/item?id=48540126)

**Background**: Fin (formerly Intercom) is a customer support platform that uses AI agents to handle complex queries across multiple channels. Salesforce, a leading CRM provider, has been expanding its AI capabilities through acquisitions to compete with specialized AI customer service startups.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/sectors/technology/articles/salesforce-acquires-fin-formerly-intercom-134006281.html">Salesforce acquires Fin, formerly Intercom, for $3.6 billion</a></li>
<li><a href="https://fin.ai/capabilities">Fin capabilities: resolve complex customer queries | Fin</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: some praise AI customer service when executed well, while others are skeptical of Salesforce's ability to integrate Fin without degrading the product. Several commenters note the increasing competition from Sierra and Decagon, and question the long-term viability of standalone helpdesk companies.

**Tags**: `#acquisition`, `#AI`, `#customer support`, `#Salesforce`, `#SaaS`

---

<a id="item-11"></a>
## [TimescaleDB Hypercore Compression Deep Dive](https://roszigit.com/en/blog/timescaledb-compression-hypercore) ⭐️ 8.0/10

TimescaleDB's new hypercore compression engine achieves up to 98% compression for time-series data using columnar storage and type-aware techniques. This breakthrough significantly reduces storage costs and improves analytical query performance for time-series workloads, benefiting IoT, finance, and monitoring applications. Hypercore is a hybrid row-columnar engine that automatically converts older row-based chunks to compressed columnar format, using delta encoding, delta-of-delta, simple-8b, and run-length encoding for integer-like types.

hackernews · lkanwoqwp · Jun 15, 17:29 · [Discussion](https://news.ycombinator.com/item?id=48544451)

**Background**: Time-series data often grows rapidly, making storage efficiency critical. Traditional row-based storage is inefficient for analytical queries that scan many rows but few columns. Columnar storage organizes data by column, enabling better compression and faster scans. TimescaleDB is a PostgreSQL extension that adds time-series capabilities, and hypercore is its latest compression engine.

<details><summary>References</summary>
<ul>
<li><a href="https://roszigit.com/en/blog/timescaledb-compression-hypercore">TimescaleDB Compression: Hypercore and Columnar Storage with up to 98% Ratio in PostgreSQL</a></li>
<li><a href="https://www.tigerdata.com/docs/build/how-to/basic-compression">Basic compression with hypercore | Tiger Data Docs</a></li>
<li><a href="https://www.tigerdata.com/docs/learn/columnar-storage/compression-methods">Compression methods in hypercore | Tiger Data Docs</a></li>

</ul>
</details>

**Discussion**: Community comments highlight trade-offs between compression and query performance, with comparisons to alternatives like DeltaX and Gorilla compression. Some users question the 'up to 98%' claim, while others discuss lossy compression methods like swinging-door for IoT.

**Tags**: `#TimescaleDB`, `#compression`, `#time-series`, `#PostgreSQL`, `#database`

---

<a id="item-12"></a>
## [Rust vs C/C++ Memory Safety CVEs: A Nuanced Analysis](https://kobzol.github.io/rust/2026/06/15/how-memory-safety-cves-differ-between-rust-and-c-cpp.html) ⭐️ 8.0/10

A new blog post by Kobzol examines how memory safety CVEs differ between Rust and C/C++, arguing that simplistic CVE count comparisons are misleading and that Rust's soundness holes in safe APIs can lead to CVEs even without real-world exploits. This analysis challenges the common narrative that Rust eliminates memory safety vulnerabilities, highlighting the need for nuanced vulnerability metrics and deeper understanding of language-level safety guarantees in software security discussions. The article points out that Rust CVEs can arise from unsound safe APIs (soundness holes) where memory safety can be violated without unsafe code, whereas C/C++ CVEs typically stem from direct misuse of unsafe operations like null pointers or buffer overflows.

hackernews · nicoburns · Jun 15, 16:11 · [Discussion](https://news.ycombinator.com/item?id=48543392)

**Background**: Memory safety vulnerabilities, such as buffer overflows and use-after-free, have been a leading cause of security flaws in C and C++ for decades. Rust was designed to prevent these issues through its ownership system and borrow checker, but it still allows unsafe code blocks and can have soundness holes in safe APIs. Comparing CVE counts between languages is complicated by differences in disclosure practices, codebase size, and the definition of what constitutes a vulnerability.

<details><summary>References</summary>
<ul>
<li><a href="https://kobzol.github.io/rust/2026/06/15/how-memory-safety-cves-differ-between-rust-and-c-cpp.html">How memory safety CVEs differ between Rust and C/C++ | Kobzol’s blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Memory_safety">Memory safety - Wikipedia</a></li>
<li><a href="https://aquilax.ai/blog/memory-safety-vulnerabilities-cpp-rust">Memory Safety Vulnerabilities in C/C++: Why Rust Is Not Hype | AquilaX</a></li>

</ul>
</details>

**Discussion**: Commenters debate the usefulness of CVE counts as a metric, with some arguing it's a poor indicator of security. Others discuss specific examples like curl_getenv() and the implications of Rust's Option<T> handling, while one commenter warns that any type safety glitch in Rust could be considered a vulnerability, posing challenges for developers.

**Tags**: `#memory safety`, `#Rust`, `#C/C++`, `#CVEs`, `#software security`

---

<a id="item-13"></a>
## [CrankGPT: Hand-Cranked AI Assistant](https://crankgpt.com/) ⭐️ 8.0/10

CrankGPT is a hand-crank-powered AI assistant that uses a Raspberry Pi 5 to run small language models locally, highlighting the energy cost of AI inference. This project creatively demonstrates the real energy cost of AI, sparking discussion on sustainability and green computing in the AI industry. The system uses a hand-crank generator to power a Raspberry Pi 5, which runs models like Llama 3.1 8B at acceptable speeds. Technical documentation is available at squeezlabs.github.io/handcrank.

hackernews · rishikeshs · Jun 15, 13:20 · [Discussion](https://news.ycombinator.com/item?id=48540854)

**Background**: AI inference consumes significant energy, with data centers often relying on fossil fuels. Hand-crank generators convert mechanical energy to electricity, offering a low-carbon but labor-intensive power source. This project juxtaposes the two to provoke thought.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Environmental_impact_of_artificial_intelligence">Environmental impact of artificial intelligence - Wikipedia</a></li>
<li><a href="https://www.powerhome.com/portable-hand-crank-electric-generator">Portable Hand Crank Electric Generator , 20W | Power Home</a></li>

</ul>
</details>

**Discussion**: Comments range from praise for the concept to critiques of the web design. Some users humorously compare human energy efficiency (e.g., eggs vs. data centers) while others question the practicality and satire vs. seriousness of the project.

**Tags**: `#AI`, `#sustainability`, `#energy`, `#hardware`, `#green computing`

---

<a id="item-14"></a>
## [Reddit Post Urges Users to Stop Using Ollama](https://www.reddit.com/r/LocalLLaMA/comments/1u6s6pm/stop_using_ollama/) ⭐️ 8.0/10

A Reddit post titled 'Stop using Ollama' has sparked debate in the local LLM community, arguing against the use of Ollama for local model deployment due to performance or architectural concerns. Ollama is a widely-used tool for running LLMs locally, so a high-profile critique could influence user adoption and prompt developers to address underlying issues, affecting the broader local AI ecosystem. The post's specific criticisms are not detailed in the provided content, but common Ollama issues include slow performance, GPU detection problems with certain driver versions, and the need for optimization.

reddit · r/LocalLLaMA · /u/zxyzyxz · Jun 15, 20:22

**Background**: Ollama is a tool that simplifies running large language models (LLMs) locally on personal computers, offering features like parameter adjustment and fine-tuning. It is popular among developers and researchers for offline AI tasks, but performance can vary based on hardware and configuration.

<details><summary>References</summary>
<ul>
<li><a href="https://journal.hexmos.com/ollama-performance-debug-guide/">Diagnose & Fix Painfully Slow Ollama : 4 Essential Debugging...</a></li>
<li><a href="https://insiderllm.com/guides/ollama-troubleshooting-guide/">Ollama Troubleshooting Guide: Every Common Problem... | InsiderLLM</a></li>
<li><a href="https://anakin.ai/blog/how-to-make-ollama-faster/">How to Make Ollama Faster: Optimizing Performance for Local...</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is expected to include diverse viewpoints, with some users defending Ollama's ease of use and others agreeing with performance criticisms or suggesting alternatives like llama.cpp.

**Tags**: `#Ollama`, `#local LLM`, `#model deployment`, `#Reddit discussion`

---

<a id="item-15"></a>
## [Evalatro: Open Benchmark Where LLMs Play Balatro](https://www.reddit.com/r/LocalLLaMA/comments/1u6qso1/evalatro_an_open_benchmark_where_llms_play_the/) ⭐️ 8.0/10

Evalatro is an open-source benchmark that lets LLMs play the real Balatro game via text state representation and fixed seeds for reproducibility. The benchmark aims to clear Ante 12, but so far the best model (mimo-v2.5-pro) only reached Ante 5. This benchmark provides a novel, reproducible environment for evaluating LLM reasoning in a complex, strategic game, moving beyond static QA benchmarks. It could drive progress in LLM planning and decision-making under uncertainty. The benchmark uses the real Balatro game with Steamodded and balatrobot mods, providing a JSON-RPC API for LLM interaction. Scores are computed server-side to prevent cheating, and all runs are publicly viewable on a dashboard.

reddit · r/LocalLLaMA · /u/awfulalexey · Jun 15, 19:32

**Background**: Balatro is a 2024 poker-themed roguelike deck-building game where players score points by playing poker hands. Steamodded is a modding framework for Balatro, and balatrobot provides an HTTP API for external control of the game. Evalatro combines these to create a standardized LLM evaluation environment.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Steamodded/smods">GitHub - Steamodded/smods: A Balatro Modding Framework · GitHub</a></li>
<li><a href="https://github.com/coder/balatrobot">GitHub - coder/balatrobot: API for developing Balatro bots 🃏</a></li>

</ul>
</details>

**Discussion**: The Reddit community is actively discussing the benchmark, with many praising its open-source nature and reproducibility. Some question whether Ante 12 is too difficult as a goal, while others suggest additional metrics like score efficiency or decision speed.

**Tags**: `#LLM`, `#benchmark`, `#game AI`, `#open-source`, `#reasoning`

---