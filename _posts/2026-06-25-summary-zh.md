---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 152 条内容中筛选出 15 条重要资讯。

---

1. [OpenAI 发布首款定制 AI 推理芯片 Jalapeno](#item-1) ⭐️ 9.0/10
2. [Gemini 3.5 Flash 内置计算机使用功能](#item-2) ⭐️ 9.0/10
3. [自对弈强化学习智能体在 Generals.io 达到超人类水平](#item-3) ⭐️ 9.0/10
4. [iLLaDA：8B 掩码扩散模型超越自回归大语言模型](#item-4) ⭐️ 9.0/10
5. [GitHub 仓库为 AI 代理映射 817 项网络安全技能](#item-5) ⭐️ 8.0/10
6. [NousResearch Hermes Agent 单日获 1178 星](#item-6) ⭐️ 8.0/10
7. [Qwen-AgentWorld：面向通用智能体的语言世界模型](#item-7) ⭐️ 8.0/10
8. [NVIDIA 45°C 冷却方案大幅降低数据中心用水](#item-8) ⭐️ 8.0/10
9. [Nub：一个类似 Bun 的 Node.js 一体化工具包](#item-9) ⭐️ 8.0/10
10. [Rust crates.io 寻求减少对 GitHub 的依赖](#item-10) ⭐️ 8.0/10
11. [业余操作系统通过 Wine 运行 Windows 游戏](#item-11) ⭐️ 8.0/10
12. [PostHog 工程师用 AI 重写 SQL 解析器，速度提升 70 倍](#item-12) ⭐️ 8.0/10
13. [Databricks 领导者呼吁开放 Agent Cloud 生态系统](#item-13) ⭐️ 8.0/10
14. [Claude Tag：Slack 中的多人 AI 代理](#item-14) ⭐️ 8.0/10
15. [瑞士最高法院评估去审查模型 Heretic](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布首款定制 AI 推理芯片 Jalapeno](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 与 Broadcom 联合发布了 Jalapeno，这是一款专为大语言模型设计的定制 AI 推理芯片，由台积电制造，并在 OpenAI 自身模型的辅助下于九个月内完成开发。 这标志着 OpenAI 首次进入定制芯片领域，可能减少对英伟达 GPU 的依赖并降低推理成本，有望重塑 AI 硬件格局，提升大规模 AI 部署的效率。 Jalapeno 专门针对 LLM 推理优化，而非通用 AI 工作负载，其架构聚焦于现代模型的计算、内存、网络和服务需求。该芯片由 Broadcom 共同设计，并由台积电制造。

hackernews · jamdesk · 6月24日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 推理芯片是专门用于高效运行已训练 AI 模型的处理器，与英伟达 H100 等训练芯片不同。许多大型 AI 公司，如谷歌（TPU）和亚马逊（Inferentia），都已开发定制芯片以降低成本并提升性能。OpenAI 此举顺应了这一趋势，旨在为其 GPT 等模型优化推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html">OpenAI and Broadcom reveal Jalapeno, first AI chip in partnership</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/openai-jalapeno-ai-inference-chip-broadcom">OpenAI unveils Jalapeño chip for large-scale inference workloads</a></li>

</ul>
</details>

**社区讨论**: 评论者对 OpenAI 声称其模型加速了芯片设计表示怀疑，有人称这是模糊的营销话术。其他人则猜测架构创新，如权重固化在 ROM 中的设计，并将该芯片与谷歌 TPU 和 Taalas 的硅内嵌模型等竞品进行比较。

**标签**: `#AI hardware`, `#OpenAI`, `#custom chip`, `#inference`, `#Broadcom`

---

<a id="item-2"></a>
## [Gemini 3.5 Flash 内置计算机使用功能](https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/) ⭐️ 9.0/10

Google DeepMind 已将计算机使用功能作为原生工具集成到 Gemini 3.5 Flash 中，使 AI 能够直接与屏幕、键盘和鼠标等计算机界面交互。此前该功能仅在 Gemini 2.5 中作为独立模型提供。 这一进步使 AI 代理能够通过直接控制计算机界面来执行软件测试、数据录入和工作流自动化等复杂任务，极大地扩展了 AI 在软件工程和企业自动化中的实际应用。这标志着向更自主、更强大的 AI 系统迈出了重要一步。 Gemini 3.5 Flash 支持 100 万 token 的上下文窗口、6.5 万最大输出 token 以及思考能力，并拥有与 Gemini 3 Flash 相同的工具集。计算机使用功能目前处于预览阶段，可通过 Gemini API 使用。

rss · Google DeepMind Blog · 6月24日 16:30

**背景**: 计算机使用是指 AI 像人类一样感知图形用户界面（GUI）并与之交互的能力，通过理解屏幕内容并执行点击、打字和滚动等操作。这一能力属于更广泛的 AI 代理领域，旨在自动化数字环境中的复杂多步骤任务。之前的模型需要独立的专用系统来实现此类交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/">Introducing computer use in Gemini 3 . 5 Flash</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3 . 5 Flash — Google DeepMind</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5">What's new in Gemini 3 . 5 Flash | Gemini Generate Content API...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Gemini`, `#computer use`, `#Google DeepMind`, `#machine learning`

---

<a id="item-3"></a>
## [自对弈强化学习智能体在 Generals.io 达到超人类水平](https://www.reddit.com/r/MachineLearning/comments/1uei2yg/i_made_a_superhuman_generalsio_agent_with/) ⭐️ 9.0/10

一个使用 JAX 和 Vision Transformer 的自对弈强化学习智能体在不完全信息实时策略游戏 Generals.io 中达到了超人类水平，在人类 1v1 排行榜上排名第一。整个流程，包括一个快速的 JAX 模拟器，均已开源。 这项工作表明，使用 Vision Transformer 和 JAX 等现代架构进行扩展可以在复杂策略游戏中超越人类先验知识，为在其他不完全信息领域构建超人类 AI 提供了蓝图。开源发布为从事游戏 AI 和自对弈 RL 的研究人员和开发者提供了宝贵资源。 该智能体使用自对弈强化学习训练，采用 Vision Transformer 替代 CNN，并将整个流程从 NumPy/Torch 重新实现为 JAX 以加速模拟。开源发布包括一个快速的 JAX 模拟器，可作为其他项目的不完全信息 RTS 环境。

reddit · r/MachineLearning · /u/shrekofspeed · 6月24日 16:18

**背景**: Generals.io 是一款快节奏的多人在线策略游戏，玩家需要保护自己的将军、占领领土并消灭对手。自对弈强化学习是一种智能体通过与自己对抗来提升性能的技术，在 AlphaGo 和 AlphaZero 中曾取得显著成功。Vision Transformer（ViT）将 Transformer 架构应用于类似图像的输入，为处理游戏棋盘提供了 CNN 之外的另一种选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://generals.io/">generals.io</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-play_(reinforcement_learning_technique)">Self-play (reinforcement learning technique)</a></li>
<li><a href="https://arxiv.org/abs/2408.13871">[2408.13871] AlphaViT: A flexible game-playing AI for multiple games and variable board sizes</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#self-play`, `#JAX`, `#game AI`, `#open source`

---

<a id="item-4"></a>
## [iLLaDA：8B 掩码扩散模型超越自回归大语言模型](https://huggingface.co/papers/2606.25331) ⭐️ 9.0/10

研究人员推出了 iLLaDA，一个 8B 参数的掩码扩散语言模型，采用完全双向注意力机制，从零开始在 12T token 上预训练，并在 25B token 的指令语料上微调。它在多个基准测试上超越自回归模型，包括在 BBH 上提升 21.6 分，在 MATH 上提升 14.5 分。 这项工作挑战了大语言模型中占主导地位的自回归范式，证明了具有双向注意力的掩码扩散模型可以规模化并取得更优性能。它为构建无需因果注意力的强大语言模型开辟了一条新的竞争路径。 iLLaDA 使用分组查询注意力和绑定输入/输出嵌入以减少内存和参数量，并采用变长生成提高效率，以及基于置信度的评分用于多项选择评估。尽管是非自回归训练，它在多个基准测试上与 Qwen2.5 7B 保持竞争力。

huggingface_papers · Hugging Face Papers · 6月25日 00:00

**背景**: 大多数现代大语言模型（如 GPT-4 和 LLaMA）采用自回归分解和因果注意力训练，从左到右生成 token。掩码扩散语言模型则学习逆转 token 掩码上的加噪过程，从而利用双向上下文。iLLaDA 基于 LLaDA 模型，并通过改进的训练技术进行了规模化扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.25331v1">Improved Large Language Diffusion Models - arXiv.org</a></li>
<li><a href="https://ml-gsai.github.io/LLaDA-demo/">LLaDA - Large Language Diffusion Models</a></li>
<li><a href="https://louiswang524.github.io/blog/diffusion-llm/">Diffusion Language Models : How They Work, How They Compare to...</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#language models`, `#bidirectional attention`, `#large-scale training`, `#NLP`

---

<a id="item-5"></a>
## [GitHub 仓库为 AI 代理映射 817 项网络安全技能](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10

Mukul975/Anthropic-Cybersecurity-Skills 是一个 GitHub 仓库，将 817 项结构化网络安全技能映射到六个框架（MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF 和 MITRE F3），一天内获得超过 1000 颗星，总星数已超过 20000。 该仓库提供了全面的标准化技能映射，使 AI 代理能够在不同安全领域运行，可能加速 AI 在网络安全运营中的应用。 这些技能按照 Anthropic 最初开发的 agentskills.io 标准格式化，支持超过 20 个平台，包括 Claude Code、GitHub Copilot、Codex CLI、Cursor 和 Gemini CLI。

github_trending · GitHub Trending · 6月25日 03:41

**背景**: MITRE ATT&CK 是一个广泛使用的对手战术和技术知识库，而 D3FEND 则收录了防御性对策。MITRE ATLAS 专注于 AI 系统的威胁。agentskills.io 标准为定义可复用的 AI 代理技能提供了通用格式，促进了不同代理平台之间的互操作性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/agentskills/agentskills">GitHub - agentskills/agentskills: Specification and ...</a></li>
<li><a href="https://atlas.mitre.org/">MITRE ATLAS™</a></li>
<li><a href="https://d3fend.mitre.org/">D3FEND Matrix | MITRE D3FEND™</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI agents`, `#MITRE ATT&CK`, `#NIST CSF`, `#GitHub trending`

---

<a id="item-6"></a>
## [NousResearch Hermes Agent 单日获 1178 星](https://github.com/NousResearch/hermes-agent) ⭐️ 8.0/10

NousResearch 的开源 AI 智能体框架 hermes-agent 在 GitHub 上单日获得 1178 颗星，总星数超过 20.2 万，复刻数达 3.6 万。 这种快速增长表明社区对基于 Python 的 AI 智能体框架的强烈认可和兴趣，该框架可能提供新颖功能，从而影响更广泛的 AI 智能体生态系统。 该仓库使用 Python 编写，标语为“与你一同成长的智能体”，暗示其注重适应性或个性化。但提供的内容中没有详细的技术文档。

github_trending · GitHub Trending · 6月25日 03:41

**背景**: AI 智能体框架是帮助开发者构建自主 AI 智能体的软件库，这些智能体能够执行任务、做出决策并与环境交互。Python 因其丰富的生态系统而成为 AI 开发的热门语言。GitHub 上的高星数通常表明社区认可和项目受欢迎程度。

**标签**: `#AI`, `#agent`, `#Python`, `#open-source`, `#framework`

---

<a id="item-7"></a>
## [Qwen-AgentWorld：面向通用智能体的语言世界模型](https://huggingface.co/papers/2606.24597) ⭐️ 8.0/10

阿里巴巴 Qwen 团队发布了 Qwen-AgentWorld-35B-A3B 和 Qwen-AgentWorld-397B-A17B，这是首批能够通过长链思维推理模拟 7 个领域智能体环境的语言世界模型。这些模型基于超过 1000 万条交互轨迹，通过三阶段训练流程（CPT、SFT、RL）训练而成，并在新基准 AgentWorldBench 上显著优于现有前沿模型。 这项工作引入了一种新的通用 AI 智能体训练范式，即使用语言模型作为世界模拟器，无需真实环境执行即可实现可扩展且可控的环境模拟。它可能加速软件工程、网页导航和工具使用等多个领域的智能体训练、评估和合成数据生成。 这些模型采用混合专家（MoE）架构：35B 模型每个 token 仅激活约 30 亿参数。三阶段训练包括：持续预训练（CPT）用于通用世界建模、监督微调（SFT）用于下一状态预测推理，以及使用混合评分与规则奖励的强化学习（RL）来提高模拟保真度。

huggingface_papers · Hugging Face Papers · 6月24日 00:00

**背景**: 世界模型预测环境如何响应智能体的动作而变化，从而实现推理和规划。传统世界模型处理像素级传感器输入，而语言世界模型使用文本表示状态和动作。这项工作将概念扩展到智能体环境，模型模拟工具调用、GUI 交互和其他数字动作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2201.11903">Chain-of-Thought Prompting Elicits Reasoning in Large ...</a></li>
<li><a href="https://arxiv.org/abs/2602.10090">[2602.10090] Agent World Model: Infinity Synthetic ... Magentic Marketplace - microsoft.github.io GitHub - tsinghua-fib-lab/AgentSociety: AgentSociety 2 is a ... Magentic Marketplace: An Open-Source Environment for Studying ... SAGE: Scalable Agentic 3D Scene Generation for Embodied AI</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区强调该模型是语言世界模型而非标准聊天或智能体模型的新颖性，指出其在智能体训练、离线评估和合成轨迹生成方面的潜力。讨论集中在无需运行真实工具即可模拟环境响应的实际应用上。

**标签**: `#world models`, `#language models`, `#agentic AI`, `#environment simulation`, `#foundation models`

---

<a id="item-8"></a>
## [NVIDIA 45°C 冷却方案大幅降低数据中心用水](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.0/10

NVIDIA 为其 Rubin 代 AI 服务器推出了 45°C 液冷设计，采用直接芯片级冷却，冷却液温度远高于传统系统，从而实现近乎零耗水。 这一创新大幅降低了数据中心的用水量，并使废热可用于区域供暖，每年可节省数百万美元，并提升 AI 基础设施的可持续性。 该设计运行温度为 45°C（113°F），比典型热水浴缸的水温还高，是 NVIDIA AI 工厂参考架构的一部分。它消除了对冷水机和蒸发冷却的需求，将用水量降至接近零。

hackernews · nitin_flanker · 6月24日 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48660178)

**背景**: 传统数据中心使用空气冷却或低温（如 20-30°C）液冷，需要大量水进行蒸发冷却或消耗能源驱动冷水机。更高的冷却液温度可实现更高效的热排放和废热再利用，但必须保持在芯片热限值内。NVIDIA 的 45°C 方法在冷却性能与节能节水之间取得了平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techbuzz.ai/articles/nvidia-s-45-c-liquid-cooling-redefines-ai-data-center-energy">NVIDIA's 45°C Liquid Cooling Redefines AI Data Center ...</a></li>
<li><a href="https://www.guru3d.com/story/nvidia-unveils-liquid-cooling-design-for-ai-data-centers">NVIDIA Unveils 45°C Liquid Cooling Design for AI Data Centers</a></li>
<li><a href="https://www.weforum.org/stories/2025/06/sustainable-data-centre-heating/">These companies are using data centres to heat cities | World Economic Forum</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了与区域供暖协同的潜力，指出 45°C 可用于供暖回路，每年可为社区带来数百万美元的价值。有人质疑创新点具体何在，另一些人则讨论了有利气候条件，并提及 NASA Ames 类似的高温冷却方案。

**标签**: `#data centers`, `#cooling`, `#sustainability`, `#AI infrastructure`, `#energy efficiency`

---

<a id="item-9"></a>
## [Nub：一个类似 Bun 的 Node.js 一体化工具包](https://github.com/nubjs/nub) ⭐️ 8.0/10

Zod 的创建者、前 Bun 工程师 Colin McDonnell 发布了 Nub，这是一个一体化工具包，通过附加的预加载钩子为 Node.js 添加了类似 Bun 的开发体验，包括基于 oxc 的转译、模块解析以及 Worker 和 Temporal 等 API 的 polyfill。 Nub 在不替换运行时的情况下改善了 Node.js 的开发体验，提供了快速的转译和现代 API 支持，这可能会降低许多项目转向 Bun 的吸引力。 Nub 使用 --require 预加载钩子注入基于 oxc 的转译器（打包为 Node-API 插件），注册模块解析钩子，并为缺失的 API 添加 polyfill，所有操作都是纯附加的，因此代码在原生 Node.js 上运行。

hackernews · colinmcd · 6月24日 14:14 · [社区讨论](https://news.ycombinator.com/item?id=48660267)

**背景**: Bun 是一个一体化的 JavaScript 运行时，包含转译器、打包器和包管理器，提供简化的开发体验。Node.js 传统上需要单独的工具进行 TypeScript 转译和模块解析。Nub 通过钩子将这些能力添加到 Node.js 中，而无需修改运行时本身，从而弥合了这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/oxc-project/oxc">GitHub - oxc-project/oxc: ⚓ A collection of high-performance JavaScript tools.</a></li>
<li><a href="https://nodejs.org/api/module.html">Modules: `node:module` API | Node.js v26.3.1 Documentation</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，有用户将整个 monorepo 迁移到 Nub 且没有遇到任何问题。一些人讨论了 ESM 支持的细微差别以及 Node 的原生 TypeScript 支持是否使转译器变得多余，但总体情绪是积极的。

**标签**: `#Node.js`, `#tooling`, `#TypeScript`, `#developer experience`, `#Bun`

---

<a id="item-10"></a>
## [Rust crates.io 寻求减少对 GitHub 的依赖](https://infosec.exchange/@mttaggart/116806641273303255) ⭐️ 8.0/10

最近合并的 RFC（pull/3963）已开始着手将 crates.io 与 GitHub 解耦，实现工作正在进行中。Rust 项目承认这一依赖是已知问题，需要大量志愿者努力才能解决。 减少对 GitHub 的依赖对于 Rust 包生态系统的韧性和去中心化至关重要，确保发布 crate 不依赖于单一商业平台。这一变化将使注册表更加健壮和独立，惠及所有 Rust 开发者。 解耦工作复杂且进展缓慢，因为 crates.io 主要由志愿者驱动，枯燥或无趣的任务依赖于资金和审查者的可用性。官方 issue（crates.io#326）列出了包含具体任务的路线图，需要志愿者贡献。

hackernews · speckx · 6月24日 19:40 · [社区讨论](https://news.ycombinator.com/item?id=48664733)

**背景**: crates.io 是 Rust 的官方包注册表，而 Cargo（Rust 的构建工具）历史上与 GitHub 绑定用于发布。这种依赖关系是在 GitHub 被视为开源乌托邦时建立的，但现在已深深嵌入，难以回退。Rust 项目并非公司；大部分开发由志愿者完成，他们只做自己感兴趣的工作。

**社区讨论**: 社区评论一致认为这一依赖是个问题，但指出由于志愿者驱动开发和任务复杂性，进展缓慢。有人赞赏像 Packagist 这样的替代方案，它强制从源代码仓库打包以确保一致性。

**标签**: `#Rust`, `#crates.io`, `#GitHub`, `#open source`, `#package management`

---

<a id="item-11"></a>
## [业余操作系统通过 Wine 运行 Windows 游戏](https://astral-os.org/posts/2026/04/03/wine-on-astral.html) ⭐️ 8.0/10

Astral OS 是一个业余操作系统，它成功移植了 Wine 以运行 Windows 游戏，展示了兼容性方面的重大技术成就。 这表明业余操作系统可以通过利用 Wine 实现日常使用的可行性，可能激励更多业余操作系统项目追求实用性。 社区讨论证实，该移植无需 X 服务器或模拟器即可原生运行，并且建立在之前将 Minecraft 引入该操作系统的工作基础之上。

hackernews · avaliosdev · 6月24日 14:38 · [社区讨论](https://news.ycombinator.com/item?id=48660671)

**背景**: Wine 是一个兼容层，允许 Windows 应用程序在类 Unix 系统上运行而无需模拟。业余操作系统通常由个人或小团体为学习或实验而开发，往往缺乏广泛的应用支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wine_compatibility_layer">Wine compatibility layer</a></li>
<li><a href="https://www.winehq.org/">WineHQ - Run Windows applications on Linux, BSD, Solaris and macOS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hobbyist_operating_system">Hobbyist operating system - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一技术成就表示赞赏，有人指出实现遗留接口的挑战。一位评论者询问了缺少 X 服务器的情况，作者确认是原生渲染。

**标签**: `#hobby OS`, `#Wine`, `#operating systems`, `#compatibility`, `#gaming`

---

<a id="item-12"></a>
## [PostHog 工程师用 AI 重写 SQL 解析器，速度提升 70 倍](https://posthog.com/blog/sql-parser) ⭐️ 8.0/10

一位 PostHog 工程师使用多个并发的 Claude Code 会话重写了他们的 SQL 解析器，在几乎不了解原始代码的情况下实现了约 70 倍的性能提升。 这展示了一种新颖的工作流程，即利用 AI 以最少的人力重写性能关键组件，引发了关于手写解析器与生成解析器未来以及 AI 在软件工程中角色的讨论。 新解析器包含 16K 行手写解析器代码、5K 行工具代码以及额外的测试，全部由 AI 生成。原始解析器使用 ANTLR 解析器生成器，团队认为其难以维护。

hackernews · robbie-c · 6月24日 18:05 · [社区讨论](https://news.ycombinator.com/item?id=48663544)

**背景**: 解析器是分析代码结构的程序。许多团队使用 ANTLR 等解析器生成器来避免手写解析器，但手写解析器可能更快且能生成更好的错误信息。PostHog 原始的 SQL 解析器基于 ANTLR 构建，成为性能瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://posthog.com/blog/sql-parser">I wrote a 70x faster SQL parser while barely looking at the code</a></li>

</ul>
</details>

**社区讨论**: 评论者就手写解析器与解析器生成器的优劣展开了辩论，有人认为手写解析器比通常认为的更容易维护。其他人则称赞 AI 辅助方法，但担心过度依赖 AI 会阻碍深层技术学习。

**标签**: `#SQL`, `#parser`, `#AI-assisted development`, `#performance`, `#PostHog`

---

<a id="item-13"></a>
## [Databricks 领导者呼吁开放 Agent Cloud 生态系统](https://www.latent.space/p/databricks) ⭐️ 8.0/10

在一次罕见的联合采访中，Databricks 联合创始人 Matei Zaharia 和 Reynold Xin 主张前沿生态系统必须开放，以使每家公司都能构建自己的 Agent Cloud。 这一立场强化了 AI 领域的开源与专有之争，可能影响企业采用 AI 代理和数据平台的方式。如果被广泛采纳，开放生态系统可以降低公司构建定制 AI 解决方案的门槛。 采访聚焦于“Agent Cloud”概念——即每家公司都可以在自己的基础设施上部署自主 AI 代理的愿景。Databricks 自身的平台建立在 Apache Spark 和 MLflow 等开源基础之上。

rss · Latent Space · 6月24日 18:53

**背景**: Agent Cloud 是一个概念框架，其中多个 AI 代理在云环境中协作以执行复杂任务。Databricks 是一个领先的数据和 AI 平台，为数据工程、分析和机器学习提供统一环境。该公司历来倡导开源技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.databricks.com/">Databricks : Leading Data and AI Platform for Enterprises</a></li>
<li><a href="https://medium.com/@philippeandrepage/ai-agent-clouds-c8cf588f7392">Autonomous Agent Clouds . A Conceptual Framework for... | Medium</a></li>

</ul>
</details>

**标签**: `#AI`, `#open source`, `#Databricks`, `#agent clouds`, `#ecosystem`

---

<a id="item-14"></a>
## [Claude Tag：Slack 中的多人 AI 代理](https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive) ⭐️ 8.0/10

Anthropic 于 2026 年 6 月 23 日推出了 Claude Tag，将持久化、主动式的 AI 代理嵌入 Slack，团队可以@提及并委派任务，具备频道记忆和环境监控能力。 这使 Claude 从被动聊天机器人转变为持久的团队成员，能够异步工作、监控频道并主动推送更新，显著提升团队生产力，为企业 AI 助手树立了新标准。 Claude Tag 以 Beta 版形式提供给使用 Opus 4.8 的 Claude Enterprise 和 Team 客户，它能够自主编写高达 65%的代码，并提供完整的审计追踪以满足合规要求。

rss · Latent Space · 6月24日 07:14

**背景**: 传统的 Slack AI 助手是被动的——仅在直接调用时响应。Claude Tag 引入了主动式、持久化的代理，它常驻频道，随时间从对话中学习，并能在未被提示时主动发起行动，使其成为真正的队友而非工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive">[AINews] Claude Tag: Multiplayer, Proactive, Persistent ...</a></li>
<li><a href="https://www.techtimes.com/articles/318967/20260623/claude-tag-turns-slack-multiplayer-ai-anthropic-agent-writes-65-its-own-code.htm">Claude Tag Turns Slack Into Multiplayer AI: Anthropic Agent ...</a></li>
<li><a href="https://mer.vin/2026/06/claude-tag-explained-anthropics-multiplayer-ai-teammate-for-slack-beta/">Claude Tag Explained: Anthropic's Multiplayer AI Teammate for ...</a></li>

</ul>
</details>

**社区讨论**: 社区反响非常积极，Kevin Weil 称其为“绝妙的主意”，用户也表示这是他们为数不多愿意每天在 Slack 中使用的代理功能。

**标签**: `#AI`, `#Slack`, `#Claude`, `#agents`, `#productivity`

---

<a id="item-15"></a>
## [瑞士最高法院评估去审查模型 Heretic](https://www.reddit.com/r/LocalLLaMA/comments/1ueeund/the_swiss_federal_supreme_court_is_evaluating/) ⭐️ 8.0/10

瑞士联邦最高法院正在评估去审查模型 Heretic，以解决法律应用中 LLM 的过度对齐问题，一篇研究论文认为 Heretic 在缓解过度谨慎的拒绝方面效果良好。 这标志着一个真实的法律机构正在积极探索去审查技术以提升 LLM 的实用性，挑战了去审查模型仅用于恶意用途的假设，并凸显了在安全与合法功能之间取得平衡的实际需求。 论文《在多语言刑事法院中测量和缓解 LLM 的过度对齐》在第 5.2 节评估了 Heretic 并得出有利结论，而法院也遇到了 LLM 拒绝合法请求的问题，这与普通用户的抱怨类似。

reddit · r/LocalLLaMA · /u/-p-e-w- · 6月24日 14:19

**背景**: 去审查（Abliteration）是一种利用机械可解释性从 LLM 权重中移除拒绝方向的技术，无需重新训练。Heretic 是一个具体的去审查模型，允许用户轻松去除 LLM 的审查。过度对齐是指 LLM 变得过度谨慎并拒绝合法请求，这会阻碍法律分析等实际应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.bswen.com/blog/2026-03-10-heretic-vs-abliterated-models/">Heretic vs Abliterated LLM Models : Key Differences... | BSWEN</a></li>
<li><a href="https://arxiv.org/pdf/2509.08833">Position: The Pitfalls of Over - Alignment : Overly Caution...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Federal_Supreme_Court_of_Switzerland">Federal Supreme Court of Switzerland - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区最初担心法院可能会禁止去审查模型，但得知法院正在评估 Heretic 供自己使用后松了一口气。用户指出，去审查模型通常与恶意用途相关，而现在最高法院却在考虑用它来提升 LLM 的实用性，这颇具讽刺意味。

**标签**: `#AI alignment`, `#abliteration`, `#LLM`, `#legal tech`, `#over-alignment`

---