---
layout: default
title: "Horizon Summary: 2026-06-25 (EN)"
date: 2026-06-25
lang: en
---

> From 152 items, 15 important content pieces were selected

---

1. [OpenAI unveils first custom AI inference chip Jalapeno](#item-1) ⭐️ 9.0/10
2. [Gemini 3.5 Flash Gains Built-in Computer Use](#item-2) ⭐️ 9.0/10
3. [Self-play RL agent achieves superhuman level in Generals.io](#item-3) ⭐️ 9.0/10
4. [iLLaDA: 8B Masked Diffusion Model Outperforms Autoregressive LLMs](#item-4) ⭐️ 9.0/10
5. [GitHub repo maps 817 cybersecurity skills for AI agents](#item-5) ⭐️ 8.0/10
6. [NousResearch Hermes Agent Surges with 1178 Stars in a Day](#item-6) ⭐️ 8.0/10
7. [Qwen-AgentWorld: Language World Models for General Agents](#item-7) ⭐️ 8.0/10
8. [NVIDIA's 45°C Cooling Slashes Data Center Water Use](#item-8) ⭐️ 8.0/10
9. [Nub: A Bun-like all-in-one toolkit for Node.js](#item-9) ⭐️ 8.0/10
10. [Rust crates.io seeks to reduce GitHub dependency](#item-10) ⭐️ 8.0/10
11. [Hobby OS Runs Windows Games via Wine](#item-11) ⭐️ 8.0/10
12. [PostHog engineer uses AI to rewrite SQL parser, 70x faster](#item-12) ⭐️ 8.0/10
13. [Databricks Leaders Argue for Open Agent Cloud Ecosystems](#item-13) ⭐️ 8.0/10
14. [Claude Tag: Multiplayer AI Agents in Slack](#item-14) ⭐️ 8.0/10
15. [Swiss Supreme Court Evaluates Abliterated Model Heretic](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI unveils first custom AI inference chip Jalapeno](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI and Broadcom unveiled Jalapeno, a custom AI inference chip designed specifically for large language models, manufactured by TSMC and developed in nine months with assistance from OpenAI's own models. This marks OpenAI's first entry into custom silicon, potentially reducing reliance on Nvidia GPUs and lowering inference costs, which could reshape the AI hardware landscape and improve efficiency for large-scale AI deployments. Jalapeno is optimized specifically for LLM inference, not general-purpose AI workloads, and its architecture focuses on compute, memory, networking, and serving requirements of modern models. The chip was co-designed with Broadcom and fabricated by TSMC.

hackernews · jamdesk · Jun 24, 17:47 · [Discussion](https://news.ycombinator.com/item?id=48663324)

**Background**: AI inference chips are specialized processors designed to run trained AI models efficiently, as opposed to training chips like Nvidia's H100. Many large AI companies, including Google with its TPUs and Amazon with Inferentia, have developed custom chips to reduce costs and improve performance. OpenAI's move follows this trend, aiming to optimize inference for its own models like GPT.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html">OpenAI and Broadcom reveal Jalapeno, first AI chip in partnership</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/openai-jalapeno-ai-inference-chip-broadcom">OpenAI unveils Jalapeño chip for large-scale inference workloads</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about OpenAI's claim that its models accelerated chip design, with some calling it vague marketing. Others speculated about architectural innovations like weight-in-ROM designs and compared the chip to competitors like Google's TPUs and Taalas's silicon-burned models.

**Tags**: `#AI hardware`, `#OpenAI`, `#custom chip`, `#inference`, `#Broadcom`

---

<a id="item-2"></a>
## [Gemini 3.5 Flash Gains Built-in Computer Use](https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/) ⭐️ 9.0/10

Google DeepMind has integrated computer use as a native tool in Gemini 3.5 Flash, allowing the AI to directly interact with computer interfaces such as screens, keyboards, and mice. This feature was previously only available as a standalone model in Gemini 2.5. This advancement enables AI agents to perform complex tasks like software testing, data entry, and workflow automation by directly controlling computer interfaces, significantly expanding the practical applications of AI in software engineering and enterprise automation. It represents a major step toward more autonomous and capable AI systems. Gemini 3.5 Flash supports a 1 million token context window, 65,000 max output tokens, and thinking capabilities, along with the same tool set as Gemini 3 Flash. Computer use is currently in preview and available via the Gemini API.

rss · Google DeepMind Blog · Jun 24, 16:30

**Background**: Computer use refers to an AI's ability to perceive and interact with graphical user interfaces (GUIs) just like a human, by interpreting screen content and performing actions such as clicking, typing, and scrolling. This capability is part of the broader field of AI agents, which aim to automate complex multi-step tasks in digital environments. Previous models required separate specialized systems for such interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/">Introducing computer use in Gemini 3 . 5 Flash</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3 . 5 Flash — Google DeepMind</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5">What's new in Gemini 3 . 5 Flash | Gemini Generate Content API...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Gemini`, `#computer use`, `#Google DeepMind`, `#machine learning`

---

<a id="item-3"></a>
## [Self-play RL agent achieves superhuman level in Generals.io](https://www.reddit.com/r/MachineLearning/comments/1uei2yg/i_made_a_superhuman_generalsio_agent_with/) ⭐️ 9.0/10

A self-play reinforcement learning agent using JAX and Vision Transformers has reached superhuman performance in the imperfect-information real-time strategy game Generals.io, ranking #1 on the human 1v1 leaderboard. The entire pipeline, including a fast JAX simulator, has been open-sourced. This work demonstrates that scaling with modern architectures like Vision Transformers and JAX can surpass human priors in complex strategy games, offering a blueprint for building superhuman AI in other imperfect-information domains. The open-source release provides a valuable resource for researchers and developers working on game AI and self-play RL. The agent was trained using self-play reinforcement learning with a Vision Transformer instead of a CNN, and the entire pipeline was reimplemented in JAX from NumPy/Torch for faster simulation. The open-source release includes a fast JAX simulator that can serve as an imperfect-information RTS environment for other projects.

reddit · r/MachineLearning · /u/shrekofspeed · Jun 24, 16:18

**Background**: Generals.io is a fast-paced multiplayer strategy game where players protect their general, capture territory, and eliminate opponents. Self-play reinforcement learning is a technique where agents improve by playing against themselves, famously used in AlphaGo and AlphaZero. Vision Transformers (ViTs) apply transformer architectures to image-like inputs, offering an alternative to CNNs for processing game boards.

<details><summary>References</summary>
<ul>
<li><a href="https://generals.io/">generals.io</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-play_(reinforcement_learning_technique)">Self-play (reinforcement learning technique)</a></li>
<li><a href="https://arxiv.org/abs/2408.13871">[2408.13871] AlphaViT: A flexible game-playing AI for multiple games and variable board sizes</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#self-play`, `#JAX`, `#game AI`, `#open source`

---

<a id="item-4"></a>
## [iLLaDA: 8B Masked Diffusion Model Outperforms Autoregressive LLMs](https://huggingface.co/papers/2606.25331) ⭐️ 9.0/10

Researchers introduced iLLaDA, an 8B masked diffusion language model with fully bidirectional attention, trained from scratch on 12T tokens and fine-tuned on a 25B-token instruction corpus. It outperforms autoregressive models on multiple benchmarks, including a 21.6-point improvement on BBH and 14.5-point improvement on MATH. This work challenges the dominant autoregressive paradigm in large language models by showing that masked diffusion models with bidirectional attention can scale and achieve superior performance. It opens a new competitive path for building strong language models without causal attention. iLLaDA uses grouped-query attention and tied input/output embeddings to reduce memory and parameters, and employs variable-length generation for efficiency and confidence-based scoring for multiple-choice evaluation. Despite non-autoregressive training, it remains competitive with Qwen2.5 7B on several benchmarks.

huggingface_papers · Hugging Face Papers · Jun 25, 00:00

**Background**: Most modern large language models, like GPT-4 and LLaMA, are trained with autoregressive factorization and causal attention, generating tokens left-to-right. Masked diffusion language models instead learn to reverse a noising process over token masks, allowing bidirectional context. iLLaDA builds on the LLaDA model and scales it up with improved training techniques.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.25331v1">Improved Large Language Diffusion Models - arXiv.org</a></li>
<li><a href="https://ml-gsai.github.io/LLaDA-demo/">LLaDA - Large Language Diffusion Models</a></li>
<li><a href="https://louiswang524.github.io/blog/diffusion-llm/">Diffusion Language Models : How They Work, How They Compare to...</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#language models`, `#bidirectional attention`, `#large-scale training`, `#NLP`

---

<a id="item-5"></a>
## [GitHub repo maps 817 cybersecurity skills for AI agents](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10

Mukul975/Anthropic-Cybersecurity-Skills, a GitHub repository mapping 817 structured cybersecurity skills to six frameworks (MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF, and MITRE F3), has gained over 1,000 stars in a day and now totals over 20,000 stars. This repository provides a comprehensive, standardized skill mapping that enables AI agents to operate across diverse security domains, potentially accelerating the adoption of AI in cybersecurity operations. The skills are formatted according to the agentskills.io standard, originally developed by Anthropic, and support over 20 platforms including Claude Code, GitHub Copilot, Codex CLI, Cursor, and Gemini CLI.

github_trending · GitHub Trending · Jun 25, 03:41

**Background**: MITRE ATT&CK is a widely used knowledge base of adversary tactics and techniques, while D3FEND catalogs defensive countermeasures. MITRE ATLAS focuses on threats to AI systems. The agentskills.io standard provides a common format for defining reusable AI agent skills, promoting interoperability across different agent platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/agentskills/agentskills">GitHub - agentskills/agentskills: Specification and ...</a></li>
<li><a href="https://atlas.mitre.org/">MITRE ATLAS™</a></li>
<li><a href="https://d3fend.mitre.org/">D3FEND Matrix | MITRE D3FEND™</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#AI agents`, `#MITRE ATT&CK`, `#NIST CSF`, `#GitHub trending`

---

<a id="item-6"></a>
## [NousResearch Hermes Agent Surges with 1178 Stars in a Day](https://github.com/NousResearch/hermes-agent) ⭐️ 8.0/10

NousResearch's open-source AI agent framework, hermes-agent, gained 1178 stars on GitHub in a single day, reaching over 202,000 total stars and 36,000 forks. This rapid growth signals strong community validation and interest in a Python-based AI agent framework, potentially offering novel features that could influence the broader AI agent ecosystem. The repository is written in Python and its tagline is "The agent that grows with you," suggesting a focus on adaptability or personalization. However, no detailed technical documentation is available in the provided content.

github_trending · GitHub Trending · Jun 25, 03:41

**Background**: AI agent frameworks are software libraries that help developers build autonomous AI agents capable of performing tasks, making decisions, and interacting with environments. Python is a popular language for AI development due to its extensive ecosystem. The high star count on GitHub often indicates community approval and project popularity.

**Tags**: `#AI`, `#agent`, `#Python`, `#open-source`, `#framework`

---

<a id="item-7"></a>
## [Qwen-AgentWorld: Language World Models for General Agents](https://huggingface.co/papers/2606.24597) ⭐️ 8.0/10

Alibaba's Qwen team released Qwen-AgentWorld-35B-A3B and Qwen-AgentWorld-397B-A17B, the first language world models capable of simulating agentic environments across 7 domains using long chain-of-thought reasoning. These models were trained on over 10 million interaction trajectories via a three-stage pipeline (CPT, SFT, RL) and significantly outperform existing frontier models on the new AgentWorldBench benchmark. This work introduces a new paradigm for training general AI agents by using language models as world simulators, enabling scalable and controllable environment simulation without real-world execution. It could accelerate agent training, evaluation, and synthetic data generation across diverse domains like software engineering, web navigation, and tool use. The models use a Mixture-of-Experts (MoE) architecture: the 35B model has only ~3B active parameters per token. The three-stage training includes continued pre-training (CPT) for general world modeling, supervised fine-tuning (SFT) for next-state prediction reasoning, and reinforcement learning (RL) with hybrid rubric-and-rule rewards to improve simulation fidelity.

huggingface_papers · Hugging Face Papers · Jun 24, 00:00

**Background**: A world model predicts how an environment changes in response to an agent's actions, enabling reasoning and planning. Traditional world models operate on pixel-level sensor inputs, while language world models use text to represent states and actions. This work extends the concept to agentic environments, where the model simulates tool calls, GUI interactions, and other digital actions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2201.11903">Chain-of-Thought Prompting Elicits Reasoning in Large ...</a></li>
<li><a href="https://arxiv.org/abs/2602.10090">[2602.10090] Agent World Model: Infinity Synthetic ... Magentic Marketplace - microsoft.github.io GitHub - tsinghua-fib-lab/AgentSociety: AgentSociety 2 is a ... Magentic Marketplace: An Open-Source Environment for Studying ... SAGE: Scalable Agentic 3D Scene Generation for Embodied AI</a></li>

</ul>
</details>

**Discussion**: The Reddit community highlighted the novelty of the model being a language world model rather than a standard chat or agent model, noting its potential for agent training, offline evaluation, and synthetic trajectory generation. The discussion focused on the practical applications of simulating environment responses without running real tools.

**Tags**: `#world models`, `#language models`, `#agentic AI`, `#environment simulation`, `#foundation models`

---

<a id="item-8"></a>
## [NVIDIA's 45°C Cooling Slashes Data Center Water Use](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.0/10

NVIDIA has introduced a 45°C liquid cooling design for its Rubin-generation AI servers, which uses direct-to-chip cooling with coolant temperatures significantly higher than traditional systems, enabling near-zero water consumption. This innovation dramatically reduces data center water usage and allows waste heat to be reused for district heating, potentially saving millions of dollars annually and improving the sustainability of AI infrastructure. The design operates at 45°C (113°F), hotter than typical hot tub water, and is part of NVIDIA's reference architecture for AI factories. It eliminates the need for chillers and evaporative cooling, cutting water use to near zero.

hackernews · nitin_flanker · Jun 24, 14:10 · [Discussion](https://news.ycombinator.com/item?id=48660178)

**Background**: Traditional data centers use air cooling or liquid cooling at lower temperatures (e.g., 20-30°C), which requires significant water for evaporative cooling or energy for chillers. Higher coolant temperatures enable more efficient heat rejection and waste heat reuse, but must stay within chip thermal limits. NVIDIA's 45°C approach balances cooling performance with energy and water savings.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techbuzz.ai/articles/nvidia-s-45-c-liquid-cooling-redefines-ai-data-center-energy">NVIDIA's 45°C Liquid Cooling Redefines AI Data Center ...</a></li>
<li><a href="https://www.guru3d.com/story/nvidia-unveils-liquid-cooling-design-for-ai-data-centers">NVIDIA Unveils 45°C Liquid Cooling Design for AI Data Centers</a></li>
<li><a href="https://www.weforum.org/stories/2025/06/sustainable-data-centre-heating/">These companies are using data centres to heat cities | World Economic Forum</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the potential for district heating synergy, noting that 45°C is workable for heating loops and could provide millions in annual value to communities. Some questioned what exactly is innovative, while others discussed favorable climates and referenced similar high-temperature cooling at NASA Ames.

**Tags**: `#data centers`, `#cooling`, `#sustainability`, `#AI infrastructure`, `#energy efficiency`

---

<a id="item-9"></a>
## [Nub: A Bun-like all-in-one toolkit for Node.js](https://github.com/nubjs/nub) ⭐️ 8.0/10

Colin McDonnell, creator of Zod and former Bun engineer, released Nub, an all-in-one toolkit that enhances Node.js with Bun-like developer experience via additive preload hooks, including oxc-powered transpilation, module resolution, and polyfills for APIs like Worker and Temporal. Nub improves Node.js developer experience without replacing the runtime, offering fast transpilation and modern API support, which could reduce the appeal of switching to Bun for many projects. Nub uses a --require preload hook to inject an oxc-based transpiler (packaged as a Node-API add-on), registers a module resolution hook, and adds polyfills for missing APIs, all purely additive so code runs on stock Node.js.

hackernews · colinmcd · Jun 24, 14:14 · [Discussion](https://news.ycombinator.com/item?id=48660267)

**Background**: Bun is an all-in-one JavaScript runtime that includes a transpiler, bundler, and package manager, offering a streamlined developer experience. Node.js traditionally requires separate tools for TypeScript transpilation and module resolution. Nub bridges this gap by adding these capabilities to Node.js via hooks, without modifying the runtime itself.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/oxc-project/oxc">GitHub - oxc-project/oxc: ⚓ A collection of high-performance JavaScript tools.</a></li>
<li><a href="https://nodejs.org/api/module.html">Modules: `node:module` API | Node.js v26.3.1 Documentation</a></li>

</ul>
</details>

**Discussion**: The community reacted positively, with one user migrating their entire monorepo to Nub with zero issues. Some discussed ESM support nuances and whether Node's native TypeScript support makes the transpiler redundant, but overall sentiment was favorable.

**Tags**: `#Node.js`, `#tooling`, `#TypeScript`, `#developer experience`, `#Bun`

---

<a id="item-10"></a>
## [Rust crates.io seeks to reduce GitHub dependency](https://infosec.exchange/@mttaggart/116806641273303255) ⭐️ 8.0/10

A recent RFC (pull/3963) has been merged to start decoupling crates.io from GitHub, with implementation work underway. The Rust project acknowledges the dependency as a known problem that requires significant volunteer effort to resolve. Reducing reliance on GitHub is critical for the resilience and decentralization of Rust's package ecosystem, ensuring that publishing crates does not depend on a single commercial platform. This change will benefit all Rust developers by making the registry more robust and independent. The decoupling effort is complex and slow because crates.io is largely volunteer-driven, with boring or uninteresting tasks depending on funding and reviewer availability. The official issue (crates.io#326) outlines a roadmap with specific tasks that need volunteer contributions.

hackernews · speckx · Jun 24, 19:40 · [Discussion](https://news.ycombinator.com/item?id=48664733)

**Background**: crates.io is the official Rust package registry, and Cargo (Rust's build tool) historically tied itself to GitHub for publishing. This dependency was established when GitHub was seen as an open-source utopia, but now it is deeply baked in, making it hard to roll back. The Rust project is not a company; most development is done by volunteers working on what they find interesting.

**Discussion**: Community comments express agreement that the dependency is a problem, but note that progress is slow due to volunteer-driven development and the complexity of the task. Some appreciate alternative approaches like Packagist, which forces packaging from a source repository to ensure consistency.

**Tags**: `#Rust`, `#crates.io`, `#GitHub`, `#open source`, `#package management`

---

<a id="item-11"></a>
## [Hobby OS Runs Windows Games via Wine](https://astral-os.org/posts/2026/04/03/wine-on-astral.html) ⭐️ 8.0/10

Astral OS, a hobby operating system, has successfully ported Wine to run Windows games, demonstrating a significant technical achievement in compatibility. This shows that a hobby OS can achieve daily-driver viability by leveraging Wine, potentially inspiring more hobby OS projects to aim for practical usability. The port runs natively without an X server or emulator, as confirmed by community discussion, and builds on earlier work that brought Minecraft to the OS.

hackernews · avaliosdev · Jun 24, 14:38 · [Discussion](https://news.ycombinator.com/item?id=48660671)

**Background**: Wine is a compatibility layer that allows Windows applications to run on Unix-like systems without emulation. Hobby operating systems are typically developed by individuals or small groups for learning or experimentation, often lacking broad application support.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wine_compatibility_layer">Wine compatibility layer</a></li>
<li><a href="https://www.winehq.org/">WineHQ - Run Windows applications on Linux, BSD, Solaris and macOS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hobbyist_operating_system">Hobbyist operating system - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed admiration for the technical feat, with some noting the challenge of implementing legacy interfaces. One commenter asked about the absence of an X server, and the author confirmed native rendering.

**Tags**: `#hobby OS`, `#Wine`, `#operating systems`, `#compatibility`, `#gaming`

---

<a id="item-12"></a>
## [PostHog engineer uses AI to rewrite SQL parser, 70x faster](https://posthog.com/blog/sql-parser) ⭐️ 8.0/10

A PostHog engineer rewrote their SQL parser using multiple parallel Claude Code sessions, achieving a ~70x speedup without deep knowledge of the original codebase. This demonstrates a novel workflow where AI can be used to rewrite performance-critical components with minimal human effort, sparking debate on the future of hand-rolled vs. generated parsers and AI's role in software engineering. The new parser consists of 16K lines of hand-rolled parser code, 5K lines of tooling, and additional tests, all generated by AI. The original parser used ANTLR, a parser generator, which the team found difficult to maintain.

hackernews · robbie-c · Jun 24, 18:05 · [Discussion](https://news.ycombinator.com/item?id=48663544)

**Background**: Parsers are programs that analyze code structure. Many teams use parser generators like ANTLR to avoid writing parsers by hand, but hand-rolled parsers can be faster and produce better error messages. PostHog's original SQL parser was built with ANTLR and was a performance bottleneck.

<details><summary>References</summary>
<ul>
<li><a href="https://posthog.com/blog/sql-parser">I wrote a 70x faster SQL parser while barely looking at the code</a></li>

</ul>
</details>

**Discussion**: Commenters debated the merits of hand-rolled parsers vs. parser generators, with some arguing hand-rolled parsers are easier to maintain than commonly believed. Others praised the AI-assisted approach but expressed concern that over-reliance on AI could hinder deep technical learning.

**Tags**: `#SQL`, `#parser`, `#AI-assisted development`, `#performance`, `#PostHog`

---

<a id="item-13"></a>
## [Databricks Leaders Argue for Open Agent Cloud Ecosystems](https://www.latent.space/p/databricks) ⭐️ 8.0/10

In a rare double-interview, Databricks co-founders Matei Zaharia and Reynold Xin argue that the frontier ecosystem must be open to enable every company to build their own Agent Clouds. This stance reinforces the open-source vs. proprietary debate in AI, potentially shaping how enterprises adopt AI agents and data platforms. If widely adopted, open ecosystems could lower barriers for companies to build custom AI solutions. The interview focuses on the concept of 'Agent Clouds'—a vision where every company can deploy autonomous AI agents on its own infrastructure. Databricks' own platform is built on open-source foundations like Apache Spark and MLflow.

rss · Latent Space · Jun 24, 18:53

**Background**: Agent Clouds refer to a conceptual framework where multiple AI agents collaborate within a cloud environment to perform complex tasks. Databricks is a leading data and AI platform that provides a unified environment for data engineering, analytics, and machine learning. The company has historically championed open-source technologies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.databricks.com/">Databricks : Leading Data and AI Platform for Enterprises</a></li>
<li><a href="https://medium.com/@philippeandrepage/ai-agent-clouds-c8cf588f7392">Autonomous Agent Clouds . A Conceptual Framework for... | Medium</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open source`, `#Databricks`, `#agent clouds`, `#ecosystem`

---

<a id="item-14"></a>
## [Claude Tag: Multiplayer AI Agents in Slack](https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive) ⭐️ 8.0/10

Anthropic launched Claude Tag on June 23, 2026, embedding a persistent, proactive AI agent into Slack that teams can tag and delegate tasks to, with channel memory and ambient monitoring. This transforms Claude from a reactive chatbot into a persistent team member that can work asynchronously, monitor channels, and proactively surface updates, significantly boosting team productivity and setting a new standard for enterprise AI assistants. Claude Tag is available in beta for Claude Enterprise and Team customers on Opus 4.8, and it can write up to 65% of its own code autonomously, with full audit trails for compliance.

rss · Latent Space · Jun 24, 07:14

**Background**: Traditional AI assistants in Slack are reactive—they only respond when directly invoked. Claude Tag introduces a proactive, persistent agent that stays in channels, learns from conversations over time, and can initiate actions without being prompted, making it a true teammate rather than a tool.

<details><summary>References</summary>
<ul>
<li><a href="https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive">[AINews] Claude Tag: Multiplayer, Proactive, Persistent ...</a></li>
<li><a href="https://www.techtimes.com/articles/318967/20260623/claude-tag-turns-slack-multiplayer-ai-anthropic-agent-writes-65-its-own-code.htm">Claude Tag Turns Slack Into Multiplayer AI: Anthropic Agent ...</a></li>
<li><a href="https://mer.vin/2026/06/claude-tag-explained-anthropics-multiplayer-ai-teammate-for-slack-beta/">Claude Tag Explained: Anthropic's Multiplayer AI Teammate for ...</a></li>

</ul>
</details>

**Discussion**: The community reaction has been highly positive, with Kevin Weil calling it 'such a good idea' and users noting it's one of the few agent features they would actually use daily in Slack.

**Tags**: `#AI`, `#Slack`, `#Claude`, `#agents`, `#productivity`

---

<a id="item-15"></a>
## [Swiss Supreme Court Evaluates Abliterated Model Heretic](https://www.reddit.com/r/LocalLLaMA/comments/1ueeund/the_swiss_federal_supreme_court_is_evaluating/) ⭐️ 8.0/10

The Swiss Federal Supreme Court is evaluating the abliterated model Heretic to address over-alignment in LLMs for legal applications, as detailed in a research paper that finds Heretic favorable for mitigating overly cautious refusals. This marks a real-world legal institution actively exploring abliteration to improve LLM utility, challenging the assumption that abliterated models are only for malicious use and highlighting the practical need to balance safety with legitimate functionality. The paper "Measuring & Mitigating Over-Alignment for LLMs in Multilingual Criminal Law Courts" evaluates Heretic in Section 5.2 with a favorable conclusion, and the court has been experiencing LLMs refusing legitimate requests, similar to common user complaints.

reddit · r/LocalLLaMA · /u/-p-e-w- · Jun 24, 14:19

**Background**: Abliteration is a technique that removes refusal directions from LLM weights using mechanistic interpretability, without retraining. Heretic is a specific abliterated model that allows users to decensor LLMs easily. Over-alignment occurs when LLMs become overly cautious and refuse legitimate requests, which can hinder practical applications like legal analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.bswen.com/blog/2026-03-10-heretic-vs-abliterated-models/">Heretic vs Abliterated LLM Models : Key Differences... | BSWEN</a></li>
<li><a href="https://arxiv.org/pdf/2509.08833">Position: The Pitfalls of Over - Alignment : Overly Caution...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Federal_Supreme_Court_of_Switzerland">Federal Supreme Court of Switzerland - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Reddit community reacted with initial concern that the court might ban abliterated models, but was relieved to learn the court is evaluating Heretic for its own use. Users noted the irony that abliterated models, often associated with malicious use, are being considered by a supreme court to improve LLM utility.

**Tags**: `#AI alignment`, `#abliteration`, `#LLM`, `#legal tech`, `#over-alignment`

---