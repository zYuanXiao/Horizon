---
layout: default
title: "Horizon Summary: 2026-07-17 (ZH)"
date: 2026-07-17
lang: zh
---

> 从 151 条内容中筛选出 15 条重要资讯。

---

1. [Firefox 被编译为 WebAssembly 在浏览器内运行](#item-1) ⭐️ 9.0/10
2. [Thinking Machines Lab 发布 975B 开放权重模型 Inkling](#item-2) ⭐️ 9.0/10
3. [Kimi K3：最大开源模型，性能媲美 Opus 4.8](#item-3) ⭐️ 9.0/10
4. [Ring-Zero 将零强化学习扩展到万亿参数](#item-4) ⭐️ 9.0/10
5. [Open Interpreter 每日获 661 星，成为开放模型编码代理](#item-5) ⭐️ 8.0/10
6. [Hermes Agent：开源 AI 代理，与你一同成长](#item-6) ⭐️ 8.0/10
7. [Boogu-Image-0.1：开源多模态模型家族](#item-7) ⭐️ 8.0/10
8. [GPT-5.6 Codex 漏洞可删除用户文件](#item-8) ⭐️ 8.0/10
9. [Linus Torvalds 声明 Linux 不反 AI](#item-9) ⭐️ 8.0/10
10. [Lila Sciences：未来实验室即数据中心](#item-10) ⭐️ 8.0/10
11. [欧盟强制谷歌共享搜索数据并开放安卓 AI](#item-11) ⭐️ 8.0/10
12. [现代工人因仿人机器人部署计划罢工](#item-12) ⭐️ 8.0/10
13. [DFlash 使 Qwen3.6-27B 推理速度提升 2.2 倍且质量无损](#item-13) ⭐️ 8.0/10
14. [QLoRA 默认学习率 2e-4 在小数据集上导致过拟合](#item-14) ⭐️ 8.0/10
15. [ExTernD：扩展秩三元分解用于大语言模型量化](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Firefox 被编译为 WebAssembly 在浏览器内运行](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter 将完整的 Firefox 浏览器（Gecko 引擎）编译为 WebAssembly，使其能够在另一个浏览器标签页内运行。该项目使用了价值约 25,000 美元的 AI 代币（Claude Opus 和 Fable），并已在 GitHub 上开源。 这一突破表明，即使是像完整网页浏览器这样复杂的原生应用也可以移植到 WebAssembly，为在浏览器中运行遗留或沙盒软件开辟了新的可能性。它也展示了 AI 辅助编程在处理大规模移植工作方面的强大能力。 所有网络流量都通过基于 WebSocket 的 Wisp 协议经由 Puter 的服务器转发，因为 WebAssembly 代码无法打开任意网络连接。该演示支持 HTTPS 流量的端到端加密，团队不得不扩展服务器以应对 Hacker News 带来的流量。

rss · Simon Willison · 7月16日 23:34

**背景**: WebAssembly (Wasm) 是一种低级二进制指令格式，能在现代浏览器中以接近原生的速度运行。传统上，浏览器运行 JavaScript，但 Wasm 允许在浏览器中运行从 C++ 等语言编译而来的代码。Wisp 协议是一种低开销协议，用于通过单个 WebSocket 连接代理多个 TCP 和 UDP 套接字，从而为 Wasm 模块提供网络访问能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.puter.com/labs/firefox-wasm/">Firefox in WebAssembly - developer.puter.com</a></li>
<li><a href="https://github.com/HeyPuter/firefox-wasm">HeyPuter/firefox-wasm: Firefox in WebAssembly - GitHub</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/ wisp - protocol : Wisp is a low-overhead...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论非常积极，许多评论者对这一技术成就以及使用 AI 辅助移植印象深刻。一些人担心代理流量的成本和对 Puter 服务器的依赖，但团队回应称他们因需求激增而不得不扩展服务器。

**标签**: `#WebAssembly`, `#Firefox`, `#browser`, `#compilation`, `#Wisp`

---

<a id="item-2"></a>
## [Thinking Machines Lab 发布 975B 开放权重模型 Inkling](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 9.0/10

由 Mira Murati 领导的 Thinking Machines Lab 发布了 Inkling，这是一个开放权重的多模态混合专家模型，总参数量 975B，激活参数量 41B，采用 Apache-2.0 许可证。该模型在 45 万亿个文本、图像、音频和视频 token 上进行了训练。 此次发布标志着美国开放权重 AI 生态系统的重要补充，为中国模型及 NVIDIA Nemotron、Gemma 4 等其他开放权重竞争者提供了有力替代。其 Apache-2.0 许可证和多模态能力使其成为微调和定制的强大基础。 模型卡片明显简略，训练数据文档极少，Thinking Machines Lab 承认 Inkling 并非前沿模型，而是通过其 Tinker 平台进行微调的强大基础模型。较小的变体 Inkling-Small（总参数量 276B，激活参数量 12B）已承诺但尚未发布。

rss · Simon Willison · 7月16日 15:35

**背景**: 混合专家模型（MoE）是一种神经网络架构，将模型划分为多个专门的“专家”子网络，每个输入仅激活其中一部分，从而降低计算成本。开放权重模型公开发布训练后的参数，允许任何人下载、修改和使用，但可能不包含完整的训练数据或代码。Apache-2.0 许可证是一种宽松的开源许可证，允许无版税地使用、修改和分发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-weights`, `#multimodal`, `#Mixture-of-Experts`, `#Mira Murati`

---

<a id="item-3"></a>
## [Kimi K3：最大开源模型，性能媲美 Opus 4.8](https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest) ⭐️ 9.0/10

Moonshot AI 发布了 Kimi K3，这是一个拥有 2.8 万亿参数、50B 激活参数的开源权重模型，性能媲美 Anthropic 的 Opus 4.8，但定价与 Sonnet 5 相当（每百万 token 输入 3 美元、输出 15 美元）。 作为有史以来最大的开源模型，Kimi K3 大幅降低了前沿 AI 的成本，可能加速智能的 commoditization，并对专有模型定价形成压力。 Kimi K3 采用 MoE 架构，总参数 2.8T，每个 token 激活 50B 参数，支持 100 万 token 上下文窗口，在编程、智能体任务、长程推理和视觉理解方面表现优异。

rss · Latent Space · 7月17日 01:46

**背景**: 像 Kimi K3 这样的开源权重模型允许开发者下载和微调，而封闭 API 则不能。该模型使用 Kimi Delta Attention 和 Attention Residuals 提高效率。Opus 4.8 是 Anthropic 的顶级模型，而 Sonnet 5 则提供更具性价比的选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://www.marktechpost.com/2026/07/16/moonshot-ai-releases-kimi-k3-a-2-8-trillion-parameter-open-moe-model-with-kimi-delta-attention-and-1m-context/">Moonshot AI Releases Kimi K 3 : A 2 . 8 Trillion... - MarkTechPost</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-8">Introducing Claude Opus 4.8 \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，该模型作为中国开源权重模型定价较高（每百万 token 输入 3 美元、输出 15 美元），但承认其性能具有竞争力。一些人猜测中国实验室正在将智能 commoditize 以推动硬件销售，而另一些人则指出所需的大量投资。

**标签**: `#AI`, `#open-source`, `#large language model`, `#Kimi K3`, `#breakthrough`

---

<a id="item-4"></a>
## [Ring-Zero 将零强化学习扩展到万亿参数](https://huggingface.co/papers/2607.12395) ⭐️ 9.0/10

研究人员提出了 Ring-Zero，这是一个稳定的训练流程，可将零强化学习扩展到 1 万亿参数模型，并展示了自我验证、并行推理等涌现推理行为。 这一突破在空前规模上验证了零强化学习的扩展定律，表明万亿参数模型无需人工标注数据即可发展出高级推理能力，可能改变 AI 推理能力的发展路径。 该流程包括裁剪重要性采样、训练-推理比率校正和混合精度控制等算法优化。最终模型 Ring-2.5-1T-Zero 在七个数学基准上取得了有竞争力的性能。

huggingface_papers · Hugging Face Papers · 7月16日 00:00

**背景**: 零强化学习（zero RL）使用可验证奖励训练模型，无需人工标注数据，从而涌现出思维链推理。由于计算限制，先前的工作仅限于小模型，扩展行为尚未被探索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2510.25528">Zero Reinforcement Learning Towards General Domains</a></li>
<li><a href="https://arxiv.org/abs/2503.18892">SimpleRL-Zoo: Investigating and Taming Zero Reinforcement Learning for ...</a></li>
<li><a href="https://arxiv.org/abs/1905.02363">[1905.02363] Dimension-Wise Importance Sampling Weight Clipping for Sample-Efficient Reinforcement Learning</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#scaling laws`, `#reasoning`, `#large language models`, `#AI research`

---

<a id="item-5"></a>
## [Open Interpreter 每日获 661 星，成为开放模型编码代理](https://github.com/openinterpreter/openinterpreter) ⭐️ 8.0/10

Open Interpreter 是一个面向 Kimi K3 等开放模型的编码代理，单日获得 661 颗星，GitHub 总星数超过 66,000。该项目使用 Rust 编写，专注于实现自然语言代码执行。 这一增长表明社区对与开放模型配合使用的 AI 辅助开发工具兴趣浓厚，可能降低开发者利用大语言模型完成编码任务的门槛。使用 Rust 表明其注重性能和安全性。 Open Interpreter 是 OpenAI Codex 的一个分支，针对低成本模型进行了优化，可在终端本地运行。它能读取文件、编辑代码、运行命令，并且仅在用户批准后才执行沙箱外的操作。

github_trending · GitHub Trending · 7月17日 02:43

**背景**: Kimi K3 是 Kimi 发布的拥有 2.8 万亿参数的开源模型，是目前最大的开源模型之一。Open Interpreter 提供类似 ChatGPT 的界面，支持多种编程语言的代码执行，充当连接自然语言与代码的编码代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openinterpreter/openinterpreter">GitHub - openinterpreter/openinterpreter: A coding agent for low-cost models · GitHub</a></li>
<li><a href="https://www.openinterpreter.com/">Open Interpreter CLI: open source AI coding agent</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**标签**: `#coding agent`, `#open models`, `#Rust`, `#AI-assisted development`, `#GitHub trending`

---

<a id="item-6"></a>
## [Hermes Agent：开源 AI 代理，与你一同成长](https://github.com/NousResearch/hermes-agent) ⭐️ 8.0/10

NousResearch 发布了 Hermes Agent，这是一个开源的 Python AI 代理，在 GitHub 上一天内获得 588 颗星，其内置学习循环能从经验中创建技能并跨会话记忆。 该项目代表了向自主、自我改进的 AI 代理的转变，这些代理可在多个平台（CLI、消息应用、语音）上运行，可能减少对单一供应商解决方案的锁定，并支持长期运行、个性化的 AI 助手。 Hermes Agent 支持从单个网关连接 Telegram、Discord、Slack、WhatsApp、Signal 和 CLI，包括语音备忘录转录、跨平台对话连续性以及带有定期提示的代理策划记忆。

github_trending · GitHub Trending · 7月17日 02:43

**背景**: Hermes Agent 由 Nous Research 构建，该实验室是 Hermes、Nomos 和 Psyche 模型系列的幕后团队。与绑定到 IDE 的编码副手或围绕单个 API 的聊天机器人包装器不同，该代理设计为驻留在你的服务器上，记住所学内容，并随时间变得更强大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/nousresearch/hermes-agent">GitHub - NousResearch/hermes-agent: The agent that grows with you · GitHub</a></li>
<li><a href="https://hermes-agent.nousresearch.com/">Hermes Agent — The Agent That Grows With You</a></li>
<li><a href="https://hermes-agent.nousresearch.com/docs/">Hermes Agent Documentation | Hermes Agent</a></li>

</ul>
</details>

**标签**: `#AI`, `#agent`, `#Python`, `#open-source`

---

<a id="item-7"></a>
## [Boogu-Image-0.1：开源多模态模型家族](https://huggingface.co/papers/2607.13125) ⭐️ 8.0/10

Boogu-Image-0.1 是一个开源统一多模态模型家族，在文本到图像生成、基于指令的编辑和双语文本渲染方面取得了有竞争力的性能，包含 Base、Turbo、Edit 和 Edit-Turbo 等变体。 这项工作表明，即使在有限的计算预算下，通过针对性的数据质量和训练流程改进以及智能推理时扩展，也能显著提升性能，从而推动开源多模态理解与生成的发展。 基础模型仅使用 2.0862 亿张独特图像进行训练，理论训练成本约为 40 万美元，但其性能匹配或超越其他开源模型，并接近领先的闭源系统（如 Nano-Banana-Pro 和 GPT-Image-2）。

huggingface_papers · Hugging Face Papers · 7月16日 00:00

**背景**: 统一多模态理解与生成模型旨在单个框架中同时处理图像理解和创建。闭源系统通常通过未公开的系统级集成取得强劲结果，而开源替代方案通常落后。Boogu-Image-0.1 通过以 Apache 2.0 许可证发布权重、代码和配方来弥补这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2604.16529">Scaling Test-Time Compute for Agentic Coding</a></li>
<li><a href="https://arxiv.org/abs/2604.16529">[2604.16529] Scaling Test-Time Compute for Agentic Coding</a></li>
<li><a href="https://arxiv.org/html/2602.12276">Agentic Test-Time Scaling for WebAgents</a></li>

</ul>
</details>

**标签**: `#multimodal`, `#text-to-image`, `#open-source`, `#image generation`, `#AI`

---

<a id="item-8"></a>
## [GPT-5.6 Codex 漏洞可删除用户文件](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

Thibault Sottiaux 报告称，GPT-5.6 的 Codex 存在一个漏洞：在启用完全访问模式且未使用沙箱保护时，由于覆盖 $HOME 环境变量时出错，可能导致删除用户文件。 该漏洞凸显了 AI 编程代理中的重大安全风险，尤其是对于授予完全文件系统访问权限而未使用沙箱的开发者，可能导致数据丢失或系统损坏。 该漏洞发生在 Codex 尝试覆盖 $HOME 以设置临时目录时，却错误地删除了 $HOME。当启用完全访问模式且未启用沙箱或自动审查时，此问题最为常见。

rss · Simon Willison · 7月16日 17:45

**背景**: Codex 是 OpenAI 开发的开源编程代理，用 Rust 编写，在终端中运行。完全访问模式赋予代理不受限制的文件系统权限，在没有沙箱的情况下可能很危险。$HOME 环境变量指向用户的主目录；错误地覆盖它可能导致意外删除。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepnoodle.ai/blog/sandboxing-ai-coding-agents">The Deep Noodle Blog | Sandboxing AI Coding Agents</a></li>
<li><a href="https://www.theunwindai.com/p/sandboxing-ai-agents-100x-faster">Sandboxing AI Agents, 100 x Faster</a></li>
<li><a href="https://openai.com/index/introducing-the-codex-app/">Introducing the Codex app | OpenAI</a></li>

</ul>
</details>

**标签**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`, `#bug`

---

<a id="item-9"></a>
## [Linus Torvalds 声明 Linux 不反 AI](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linux 创始人兼顶级维护者 Linus Torvalds 公开表示 Linux 不是一个反 AI 的项目，并认为 AI 是一个明显有用的工具，他邀请持不同意见者分叉或离开。 来自 Linux 顶级维护者的权威背书可能影响开源社区对 AI 工具的态度，从而加速 AI 在 Linux 开发及相关项目中的应用。 Torvalds 在 Linux Media 邮件列表中发表此声明，强调 AI 的有用性已毋庸置疑，尽管其经济影响等其他问题仍有待探讨。

rss · Simon Willison · 7月16日 13:26

**背景**: Linus Torvalds 是 Linux 内核（Linux 操作系统的核心）的创建者和长期维护者。开源社区一直就 AI 工具的使用存在争议，部分人出于伦理、版权或环境影响等担忧主张禁止使用。

**标签**: `#Linux`, `#AI`, `#Open Source`, `#Linus Torvalds`

---

<a id="item-10"></a>
## [Lila Sciences：未来实验室即数据中心](https://www.latent.space/p/the-lab-of-the-future-should-feel) ⭐️ 8.0/10

Lila Sciences 提出将科学实验室转变为数据中心，利用机器人和 AI 从实验中生成大量训练数据。该方法将科学视为 AI 模型尚未开发的高质量训练数据来源。 这种范式转变可能通过自动化数据生成并使 AI 直接从实验中学习，从而大幅加速科学发现。它可能减少对互联网数据的依赖（这些数据通常嘈杂且有限），并在化学和材料科学等领域实现新的突破。 Lila Sciences 正在构建一个自主实验室平台，集成机器人和 AI 以大规模进行实验并收集数据。该公司旨在创建一种“科学超级智能”，能够无需人工干预地生成假设、运行实验并分析结果。

rss · Latent Space · 7月16日 13:30

**背景**: 传统的 AI 训练严重依赖从互联网抓取的数据，这些数据可能嘈杂且有偏差。相比之下，科学实验产生结构化、高质量的数据，非常适合训练 AI 模型。Lila Sciences 设想未来实验室像自动化工厂一样运行，持续生成实验数据以供给 AI 系统，类似于数据中心支撑云计算的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lila.ai/">LILA | Scientific Superintelligence</a></li>
<li><a href="https://www.linkedin.com/company/lila-sciences">Lila Sciences | LinkedIn</a></li>
<li><a href="https://www.science.org/doi/10.1126/scirobotics.adm6991">Transforming science labs into automated factories of discovery | Science Robotics</a></li>

</ul>
</details>

**标签**: `#AI`, `#scientific discovery`, `#robotics`, `#data generation`, `#lab automation`

---

<a id="item-11"></a>
## [欧盟强制谷歌共享搜索数据并开放安卓 AI](https://arstechnica.com/gadgets/2026/07/its-official-eu-will-force-google-to-share-search-data-and-open-up-ai-on-android/) ⭐️ 8.0/10

欧盟根据《数字市场法案》正式要求谷歌与竞争对手共享搜索数据，并开放安卓系统上的 AI 功能，理由是出于竞争担忧。 这项里程碑式的法规可能通过增加竞争重塑数字市场，有望带来更多创新和消费者选择，而谷歌警告称这可能损害用户隐私和安全。 该指令要求谷歌向第三方搜索引擎提供其搜索数据，并允许在安卓设备上使用替代 AI 服务，不遵守规定可能面临高达全球营业额 10%的罚款。

rss · Ars Technica AI · 7月16日 20:41

**背景**: 《数字市场法案》（DMA）是欧盟的一项法规，针对被指定为“守门人”的大型数字平台，以确保公平竞争。该法案于 2022 年 11 月生效，2023 年 5 月开始适用，义务包括数据共享和互操作性。谷歌作为守门人，必须遵守这些规则以防止反竞争行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/EU_Digital_Markets_Act">EU Digital Markets Act</a></li>
<li><a href="https://www.nytimes.com/2025/09/02/technology/google-search-antitrust-decision.html">Google Must Share Search Data With Rivals, Judge Rules in Antitrust...</a></li>
<li><a href="https://ppc.land/google-ordered-to-share-glue-data-system-in-landmark-antitrust-ruling/">Google ordered to share Glue data system in landmark antitrust ruling</a></li>

</ul>
</details>

**标签**: `#EU regulation`, `#Google`, `#Android`, `#AI`, `#privacy`

---

<a id="item-12"></a>
## [现代工人因仿人机器人部署计划罢工](https://arstechnica.com/ai/2026/07/fear-of-humanoid-robots-spurs-human-workers-to-strike-at-hyundai-auto-factory/) ⭐️ 8.0/10

现代汽车计划到 2028 年在美国工厂部署 25,000 台波士顿动力的 Atlas 仿人机器人，此举引发了担心失业的人类工人罢工。 此次罢工凸显了自动化与劳动力之间日益紧张的关系，可能为全球制造业如何协商仿人机器人的采用开创先例。 Atlas 机器人由现代汽车子公司波士顿动力开发，专为物料搬运和零件排序等工业任务设计，计划于 2028 年在美国工厂开始部署。

rss · Ars Technica AI · 7月16日 20:09

**背景**: 像 Atlas 这样的仿人机器人是设计用于在人类环境中工作的双足机器。现代汽车于 2020 年收购了波士顿动力，并一直在将 Atlas 整合到其制造计划中。此次罢工反映了汽车行业对自动化取代工人的广泛担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Atlas_(robot)">Atlas ( robot ) - Wikipedia</a></li>
<li><a href="https://bostondynamics.com/products/atlas/">Atlas Humanoid Robot | Boston Dynamics</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lRd3VXa0VCR2JqdllkNnJHOXVTZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en">Google News - Hyundai Atlas robot at CES 2026 - Overview</a></li>

</ul>
</details>

**标签**: `#humanoid robots`, `#labor relations`, `#automation`, `#Hyundai`, `#AI in manufacturing`

---

<a id="item-13"></a>
## [DFlash 使 Qwen3.6-27B 推理速度提升 2.2 倍且质量无损](https://www.reddit.com/r/LocalLLaMA/comments/1uyay0w/dflash_makes_qwen36_27b_22x_faster_with_no/) ⭐️ 8.0/10

一种名为 DFlash 的新型推测解码技术，在 Qwen3.6-27B 上针对编码和 JSON 生成等结构化任务实现了 2.2 倍的推理加速，同时保持与基线相同的输出质量。 这一突破显著降低了结构化任务的推理延迟，使本地 LLM 部署在编码和数据处理方面更加实用，并为不同使用场景提供了与多令牌预测（MTP）的清晰权衡分析。 DFlash 使用轻量级块扩散模型并行草拟 15 个令牌，在 JSON 任务上达到 152 tok/s（3.4 倍），但由于接受率低，在创意文本上可能低于基线（42 vs 44 tok/s）。

reddit · r/LocalLLaMA · /u/ElmBark · 7月16日 18:22

**背景**: 推测解码通过使用小型草稿模型提出多个令牌，再由大型目标模型并行验证，从而加速 LLM 推理。DFlash 是一种采用块扩散模型进行草拟的新型框架，而 MTP（多令牌预测）则使用同一模型同时预测多个令牌。这两种技术都旨在不牺牲输出质量的前提下降低延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2602.06036">[2602.06036] DFlash: Block Diffusion for Flash Speculative Decoding</a></li>
<li><a href="https://github.com/z-lab/dflash">GitHub - z-lab/dflash: DFlash: Block Diffusion for Flash Speculative Decoding · GitHub</a></li>
<li><a href="https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/">The next generation of speculative decoding: DFlash and Spec V2 - LMSYS Org</a></li>

</ul>
</details>

**标签**: `#speculative decoding`, `#inference optimization`, `#LLM inference`, `#Qwen`, `#local LLM`

---

<a id="item-14"></a>
## [QLoRA 默认学习率 2e-4 在小数据集上导致过拟合](https://www.reddit.com/r/MachineLearning/comments/1uy1z8b/the_qlora_2e4_default_is_wrong_under_10k_samples/) ⭐️ 8.0/10

一位 Reddit 用户发现，广泛推荐的 QLoRA 学习率 2e-4 在样本数少于 10,000 的数据集上会导致过拟合，而将学习率降至 1e-4 并增加训练轮数能显著提升评估性能。 这一发现挑战了无数 QLoRA 微调教程和工具中使用的默认设置，可能为从业者节省在小数据集上浪费的数周时间，并提升模型质量。 用户报告称，使用 2e-4 时模型在第一个 epoch 内就过拟合，而将学习率降至 1e-4 并将训练轮数从 3 增加到 5，在小于 10k 样本的数据集上取得了最佳效果。他们建议根据数据集大小调整学习率：样本数超过 30k 时 2e-4 可能没问题；小于 10k 时从 1e-4 或更低开始。

reddit · r/MachineLearning · /u/Pretty-Ad774 · 7月16日 12:50

**背景**: QLoRA 是一种参数高效的微调方法，结合了量化和低秩适配（LoRA），可在消费级硬件上微调大型语言模型。默认学习率 2e-4 源自 Alpaca 数据集（52k 样本），并被广泛复制到教程和代码示例中，未针对更小的数据集进行调整。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lightning.ai/pages/community/lora-insights/">Finetuning LLMs with LoRA and QLoRA : Insights from... - Lightning AI</a></li>
<li><a href="https://github.com/artidoro/qlora">GitHub - artidoro/qlora: QLoRA: Efficient Finetuning of Quantized LLMs · GitHub</a></li>
<li><a href="https://arxiv.org/pdf/2305.14314">QLORA: Efficient Finetuning of Quantized LLMs Tim Dettmers∗ Artidoro Pagnoni∗</a></li>

</ul>
</details>

**社区讨论**: 该帖子获得了社区的高度认可，点赞数高且讨论深入。许多用户分享了类似的使用 2e-4 在小数据集上过拟合的经历，而其他人指出学习率调度器或预热步骤可以缓解该问题。部分用户就最佳学习率范围进行了辩论，建议对非常小的数据集使用 1e-5 到 5e-5。

**标签**: `#QLoRA`, `#fine-tuning`, `#learning rate`, `#overfitting`, `#LLM`

---

<a id="item-15"></a>
## [ExTernD：扩展秩三元分解用于大语言模型量化](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 8.0/10

ExTernD 提出了一种训练后量化方法，将权重矩阵分解为两个三元矩阵和一个对角缩放矩阵，使得内部秩可以任意大，从而克服固定大小三元量化的精度限制。 该方法使大语言模型的三元量化能够达到接近高位量化的精度，同时仅比现有方法略多占用 VRAM，有望让大型模型在消费级硬件上更易部署。 该方法在 arXiv 论文（2607.13511）中得到验证，并声称扩展秩无需很大即可达到高精度，且相比标准量化仅适度增加 VRAM。

reddit · r/MachineLearning · /u/LMTLS5 · 7月16日 13:31

**背景**: 训练后量化（PTQ）通过将权重转换为较低精度来减小模型大小并加速推理，无需重新训练。三元量化将权重映射到 {-α, 0, +α} 中的值，通常每个权重使用 2 比特，但固定大小的三元矩阵常面临精度损失。ExTernD 通过分解矩阵来增加表示能力，从而解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1612.01064">[1612.01064] Trained Ternary Quantization</a></li>
<li><a href="https://www.emergentmind.com/topics/ternary-quantization">Ternary Quantization in Neural Networks</a></li>
<li><a href="https://apxml.com/courses/practical-llm-quantization/chapter-2-post-training-quantization-ptq">Post - Training Quantization (PTQ) for LLMs</a></li>

</ul>
</details>

**标签**: `#LLM`, `#quantization`, `#ternary`, `#model compression`, `#PTQ`

---