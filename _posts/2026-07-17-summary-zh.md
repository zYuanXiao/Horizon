---
layout: default
title: "Horizon Summary: 2026-07-17 (ZH)"
date: 2026-07-17
lang: zh
---

> 从 151 条内容中筛选出 15 条重要资讯。

---

1. [Firefox 被编译为 WebAssembly 在 Chrome 中运行](#item-1) ⭐️ 9.0/10
2. [Linus Torvalds 力挺 AI 用于 Linux 内核开发](#item-2) ⭐️ 9.0/10
3. [Kimi K3 2.8T-A50B：最大开源模型，Opus 4.8 级别性能，Sonnet 5 价格](#item-3) ⭐️ 9.0/10
4. [OpenAI Codex：终端中的轻量级编码代理](#item-4) ⭐️ 9.0/10
5. [Ring-Zero 将零强化学习扩展到万亿参数实现涌现推理](#item-5) ⭐️ 9.0/10
6. [Open Interpreter 作为开放模型编程代理迅速崛起](#item-6) ⭐️ 8.0/10
7. [Boogu-Image-0.1：开源多模态模型家族](#item-7) ⭐️ 8.0/10
8. [汽车 OTA 更新导致 Android Auto 故障，引发软件质量讨论](#item-8) ⭐️ 8.0/10
9. [索尼删除用户已购买的电影](#item-9) ⭐️ 8.0/10
10. [Schema Harness 在 ARC-AGI-3 公开集上达到约 99%](#item-10) ⭐️ 8.0/10
11. [GPT-5.6 Codex 漏洞在完全访问模式下删除文件](#item-11) ⭐️ 8.0/10
12. [Thinking Machines Lab 发布开源权重模型 Inkling](#item-12) ⭐️ 8.0/10
13. [Lila Sciences：未来实验室即数据中心](#item-13) ⭐️ 8.0/10
14. [DeepMind 与 Isomorphic Labs 发布生物韧性 AI 方案](#item-14) ⭐️ 8.0/10
15. [欧盟强制谷歌共享搜索数据并开放安卓 AI](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Firefox 被编译为 WebAssembly 在 Chrome 中运行](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter 已将完整的 Firefox 浏览器（Gecko 引擎）编译为 WebAssembly，使其能够完全在另一个浏览器内运行，演示中在 Chrome 里的 Firefox 中加载了一个博客。 这一突破性成就展示了浏览器内执行浏览器的新范式，可能实现安全沙箱、遗留应用兼容性以及新颖的 Web 平台能力。 该项目使用了估计价值 25,000 美元的 AI token（Claude Opus 和 Fable），但由于订阅计划实际花费少得多；所有网络流量通过 Wisp 协议经 WebSocket 代理到 Puter 的服务器。

rss · Simon Willison · 7月16日 23:34

**背景**: WebAssembly (Wasm) 是一种低级二进制指令格式，能在现代浏览器中以接近原生的速度运行。将 Firefox 这样的完整浏览器编译为 Wasm 极具挑战性，因为其体积和复杂性；生成的 gecko.wasm 二进制文件达 233 MB。该项目选择 Firefox 是因为 Gecko 具有强大的单进程支持，简化了 Wasm 移植。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.puter.com/labs/firefox-wasm/">Firefox in WebAssembly</a></li>
<li><a href="https://news.ycombinator.com/item?id=48926939">Show HN: Firefox in WebAssembly | Hacker News</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/ wisp - protocol : Wisp is a low-overhead...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论非常积极，许多人对这一技术壮举印象深刻。一些人担心代理流量的成本以及在 Wasm 中运行完整浏览器的实用性，但团队表示他们不得不扩展服务器以应对流量激增。

**标签**: `#WebAssembly`, `#Firefox`, `#Browser`, `#Wasm`, `#Virtualization`

---

<a id="item-2"></a>
## [Linus Torvalds 力挺 AI 用于 Linux 内核开发](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 9.0/10

Linux 创始人 Linus Torvalds 公开声明 Linux 不是反 AI 项目，并称 AI 是内核开发的明确有用工具，警告不同意者可以分叉项目或离开。 作为顶级维护者的明确表态，标志着 Linux 内核社区可能发生政策转变，有望加速 AI 工具在开源开发中的应用，并影响其他项目。 Torvalds 在 Linux 媒体邮件列表中表示，他愿意在这个问题上“绝对坚持立场”，强调 AI 的有用性已毋庸置疑，尽管其他经济问题仍待解决。

rss · Simon Willison · 7月16日 13:26

**背景**: Linux 内核是 Linux 操作系统的核心，由 Linus Torvalds 领导的大型开源社区维护。AI 工具（如大型语言模型 LLMs）越来越多地被用于代码生成和调试，但一些开发者对其在开源项目中的使用提出了伦理和实际方面的担忧。

**标签**: `#Linux`, `#AI`, `#Open Source`, `#Kernel Development`, `#Linus Torvalds`

---

<a id="item-3"></a>
## [Kimi K3 2.8T-A50B：最大开源模型，Opus 4.8 级别性能，Sonnet 5 价格](https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest) ⭐️ 9.0/10

Moonshot AI 发布了 Kimi K3，这是一个拥有 2.8 万亿参数的开源混合专家模型，支持 100 万 token 上下文窗口，声称性能媲美 Anthropic 的 Opus 4.8，而定价与 Sonnet 5 相当。 作为有史以来最大的开源模型，Kimi K3 推动了开源 AI 的前沿，可能使接近前沿的智能更加普及，并加剧 AI 实验室之间的竞争。 Kimi K3 采用 MoE 架构，总参数 2.8T，每个 token 激活 50B 参数，并采用 Kimi Delta Attention 实现高效长上下文处理。其 API 定价为每百万 token 输入 $3、输出 $15，与 Anthropic 的 Sonnet 5 定价一致。

rss · Latent Space · 7月17日 01:46

**背景**: 开源模型传统上在性能上落后于专有前沿模型。Kimi K3 旨在缩小这一差距，提供与 Anthropic 最强大的专有模型之一 Opus 4.8 相媲美的模型，同时保持开源并以与 Sonnet 5 竞争性的价格提供。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kie.ai/blog/what-is-kimi-k3">What Is Kimi K3? Moonshot's 2.8T, 1M-Context Flagship</a></li>
<li><a href="https://www.marktechpost.com/2026/07/16/moonshot-ai-releases-kimi-k3-a-2-8-trillion-parameter-open-moe-model-with-kimi-delta-attention-and-1m-context/">Moonshot AI Releases Kimi K3: A 2.8 Trillion Parameter Open MoE Model With Kimi Delta Attention and 1M Context - MarkTechPost</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，对于中国开源权重模型而言，该模型定价较高，但如果确实能与前沿模型竞争，则定价合理。一些人认为中国实验室正在推动 AI 智能的商品化，而另一些人则质疑所需的大量投资。

**标签**: `#open models`, `#AI`, `#large language models`, `#Kimi K3`, `#machine learning`

---

<a id="item-4"></a>
## [OpenAI Codex：终端中的轻量级编码代理](https://github.com/openai/codex) ⭐️ 9.0/10

OpenAI Codex 是一个用 Rust 编写的轻量级编码代理，今日在 GitHub 上获得 381 颗星，总星数达到 98,900。它能在终端中直接将自然语言翻译成代码。 该工具通过实现自然语言到代码的翻译，代表了开发者工具领域的范式转变，可能为数百万开发者提升生产力。其庞大的社区采用率（98.9k 星）表明对 AI 驱动的编码助手有强烈需求。 Codex 使用 Rust 构建，强调性能与安全性，并作为基于终端的代理运行。它是 OpenAI 旨在自动化软件工程任务的 AI 驱动编码代理套件的一部分。

github_trending · GitHub Trending · 7月17日 02:55

**背景**: 编码代理是一种自主执行编码任务的 AI 系统，例如编写、审查和重构代码。OpenAI Codex 是几个流行的 AI 编码代理之一，其他工具包括 Cursor、Claude Code 和 GitHub Copilot，它们在速度、控制性和自主性之间各有侧重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Codex">OpenAI Codex</a></li>
<li><a href="https://grokipedia.com/page/Coding_agent">Coding agent</a></li>
<li><a href="https://www.faros.ai/blog/best-ai-coding-agents-2026">Best AI Coding Agents for 2026: Real-World Developer Reviews</a></li>

</ul>
</details>

**标签**: `#AI`, `#coding agent`, `#developer tools`, `#natural language processing`, `#Rust`

---

<a id="item-5"></a>
## [Ring-Zero 将零强化学习扩展到万亿参数实现涌现推理](https://huggingface.co/papers/2607.12395) ⭐️ 9.0/10

研究人员提出了 Ring-Zero，这是一个稳定高效的流水线，可将基于可验证奖励的强化学习（零强化学习）扩展到万亿参数模型，在七个数学基准上取得了有竞争力的性能。 这项工作表明，将零强化学习扩展到万亿参数模型显著提升了样本效率和性能上限，并揭示了自我验证、并行推理等涌现推理行为，可能减少 AI 系统中手工启发式方法的需求。 该流水线包含算法和系统优化，包括裁剪重要性采样、训练-推理比率校正和混合精度控制。训练过程依次经历初始发现阶段和锐化阶段。

huggingface_papers · Hugging Face Papers · 7月16日 00:00

**背景**: 基于可验证奖励的强化学习（零强化学习）是一种无需人工标注数据即可增强大型语言模型推理能力的范式。由于计算限制，先前的工作仅限于小模型，缩放行为尚未被探索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.12395">Ring- Zero : Scaling Zero RL to a Trillion Parameters for Emergent...</a></li>
<li><a href="https://arxiv.org/abs/1905.02363">[1905.02363] Dimension-Wise Importance Sampling Weight Clipping for Sample-Efficient Reinforcement Learning</a></li>
<li><a href="https://arxiv.org/html/2602.01826">Beyond Precision: Training-Inference Mismatch is an Optimization Problem and Simple LR Scheduling Fixes It</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#large language models`, `#reasoning`, `#scaling`, `#zero RL`

---

<a id="item-6"></a>
## [Open Interpreter 作为开放模型编程代理迅速崛起](https://github.com/openinterpreter/openinterpreter) ⭐️ 8.0/10

Open Interpreter 是一个针对 Kimi K3 等开放模型的编程代理，单日在 GitHub 上获得 661 颗星，总星数超过 66,000。该项目使用 Rust 编写，专注于低成本模型的性能。 这种快速增长表明社区对使用开放模型进行 AI 辅助编程有浓厚兴趣，可能将编程代理从专有解决方案扩展到更广泛的开发者群体，降低将 AI 集成到工作流程中的门槛。 Open Interpreter 是 OpenAI Codex 的一个分支，设计在终端中运行并跨多种语言执行代码。它使用沙箱确保安全，并支持 Kimi K3 等模型，该模型拥有 2.8 万亿参数和 100 万 token 的上下文窗口。

github_trending · GitHub Trending · 7月17日 02:55

**背景**: Open Interpreter 是一个本地代码执行环境，允许大型语言模型通过类似 ChatGPT 的终端界面运行代码。它强调使用低成本模型的性能，并用 Rust 编写以提高速度。Kimi K3 是最近发布的开放模型，拥有 2.8 万亿参数，是最大的开放模型之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openinterpreter/openinterpreter">GitHub - openinterpreter/openinterpreter: A coding agent for low-cost models · GitHub</a></li>
<li><a href="https://www.openinterpreter.com/">Open Interpreter CLI: open source AI coding agent</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**标签**: `#AI`, `#coding agent`, `#open models`, `#Rust`, `#developer tools`

---

<a id="item-7"></a>
## [Boogu-Image-0.1：开源多模态模型家族](https://huggingface.co/papers/2607.13125) ⭐️ 8.0/10

Boogu-Image-0.1 是一个开源统一多模态理解与生成模型家族，包含 Base、Turbo、Edit 和 Edit-Turbo 变体，在文本到图像生成、快速推理和双语文本渲染方面表现出色。 这项工作表明，在有限的计算预算下，通过针对性地改进数据质量、训练流程和智能推理时扩展，可以显著提升生成性能，达到或超越其他开源模型，并接近闭源系统。 基础模型仅使用 2.0862 亿张独特图像进行训练，理论训练成本约为 40 万美元。模型家族包括用于快速推理的 Turbo 变体和基于指令编辑的 Edit 变体。

huggingface_papers · Hugging Face Papers · 7月16日 00:00

**背景**: 统一多模态理解与生成模型旨在单一框架内同时处理图像理解和创建。像 Nano-Banana-Pro 和 GPT-Image-2 这样的闭源系统通过系统级集成实现了强大性能，但其内部实践未公开。Boogu-Image-0.1 以 Apache 2.0 许可证发布，提供权重、代码和配方，以推动开源进展。

**标签**: `#multimodal`, `#text-to-image`, `#open-source`, `#image generation`, `#AI model`

---

<a id="item-8"></a>
## [汽车 OTA 更新导致 Android Auto 故障，引发软件质量讨论](https://imdanielkendall.com/the-great-software-regress-how-move-fast-and-break-things-broke-our-lives/) ⭐️ 8.0/10

一位车主报告称，MINI 的一次 OTA 更新导致 Android Auto 功能失效，需要致电制造商要求修复。这一事件凸显了软件更新可能降低用户体验且缺乏问责制的问题。 这很重要，因为随着汽车越来越软件化，OTA 更新可能引入回归问题，影响 Android Auto 等核心功能，从而削弱信任并可能影响汽车销量。这一讨论反映了对敏捷开发实践中软件质量的广泛担忧。 作者的 MINI OTA 更新导致 Android Auto 故障，类似问题在起亚 EV9 更新中也有报道，导致屏幕空白。文章批评了“快速行动，打破常规”的文化以及敏捷开发中缺乏客户反馈循环的问题。

hackernews · Expletive4138 · 7月16日 22:29 · [社区讨论](https://news.ycombinator.com/item?id=48941129)

**背景**: OTA 更新允许汽车制造商无线更新车辆软件，类似于智能手机更新。Android Auto 是一个将手机应用镜像到汽车显示屏的系统。随着汽车越来越互联，软件质量问题可能直接影响用户体验和安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.racv.com.au/royalauto/transport/cars/what-are-ota-updates-in-cars-how-they-work.html">What are over -the- air ( OTA ) updates and how they work in cars | RACV</a></li>
<li><a href="https://www.vw.com/en/owners-and-services/apps-and-connected-services/vehicle-software-updates.html">Vehicle Software Updates | Volkswagen</a></li>
<li><a href="https://www.makeuseof.com/what-are-tesla-over-the-air-updates/">Tesla's over -the- air updates can be frustrating, but they're important...</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了类似经历，有人指出起亚 EV9 更新导致 CarPlay 故障。另有人认为，发布有缺陷软件的成本已从制造商转移到用户身上，客户不情愿地充当了 QA 角色。大家一致认为糟糕的软件体验会损害品牌声誉和销量。

**标签**: `#software quality`, `#agile development`, `#automotive software`, `#OTA updates`, `#user experience`

---

<a id="item-9"></a>
## [索尼删除用户已购买的电影](https://www.techdirt.com/2026/07/15/sony-deletes-a-bunch-more-movies-from-the-accounts-of-people-who-bought-them/) ⭐️ 8.0/10

索尼从用户账户中删除了多部电影，这些用户原本以为自己已经购买了这些电影，此举再次引发了关于数字所有权和消费者权利的讨论。 这一事件凸显了数字所有权的脆弱性，消费者可能在没有补偿的情况下失去对已付费内容的访问权限，这可能削弱对数字商店的信任，并促使用户转向实体媒体或盗版。 删除操作涉及通过 PlayStation 商店购买的电影，用户报告未收到退款或事先通知。这并非索尼首次删除已购买内容；类似事件在 2024 年和 2025 年也曾发生。

hackernews · nekusar · 7月16日 12:13 · [社区讨论](https://news.ycombinator.com/item?id=48933419)

**背景**: 数字所有权通常意味着购买访问内容的许可，而非拥有内容本身。像索尼这样的公司可以根据服务条款撤销这些许可，消费者几乎没有法律追索权。数字商店中的“购买”一词往往具有误导性，因为它暗示了永久所有权。

**社区讨论**: 评论者意见不一：一些人认为撤销许可应伴随全额退款以平衡经济影响，而另一些人则坚持认为客户应获得实际视频文件，而非依赖服务。还有关于“购买”按钮是否合法地伪装成“租赁”按钮的讨论。

**标签**: `#digital rights`, `#consumer protection`, `#Sony`, `#digital ownership`, `#media`

---

<a id="item-10"></a>
## [Schema Harness 在 ARC-AGI-3 公开集上达到约 99%](https://schema-harness.github.io/) ⭐️ 8.0/10

Impossible Research 的 Schema harness 使用 Opus 4.8 和 Fable 5 等前沿模型，在 ARC-AGI-3 公开集上达到了约 99% 的准确率，而未经该 harness 的基线仅为 13% 左右。 这一结果凸显了 harness 工程在 AI 中日益增长的重要性，表明系统级脚手架可以大幅提升基准性能，可能重塑我们评估和开发通用智能的方式。 该 harness 的工作原理是使用前沿模型为任务编写模拟器，然后在模拟器中求解，这与直接求解原始 ARC-AGI 谜题的方法不同。在保留集上的表现尚未得到确认。

hackernews · jasondavies · 7月16日 15:29 · [社区讨论](https://news.ycombinator.com/item?id=48935905)

**背景**: ARC-AGI 是一个对人类容易但对 AI 困难的基准测试，用于测试视觉网格谜题上的泛化和推理能力。Harness 工程指的是围绕 AI 模型的基础设施、编排和脚手架，可以显著增强其能力，超越原始模型性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://schema-harness.github.io/">Frontier Models with Our Harness Achieve ~99% on ARC-AGI-3 Public — Schema</a></li>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - The only AI benchmark that measures AGI progress.</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些人认为如果在保留集上也能成立，这将是一件大事；而另一些人则认为它衡量的是与预期泛化不同的东西，因为该 harness 本质上是让模型先编写模拟器。由于缺乏开源和保留集验证，怀疑情绪依然存在。

**标签**: `#ARC-AGI`, `#AI benchmarks`, `#harness engineering`, `#frontier models`, `#generalization`

---

<a id="item-11"></a>
## [GPT-5.6 Codex 漏洞在完全访问模式下删除文件](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

GPT-5.6 的 Codex 存在一个漏洞：当启用完全访问模式且未开启沙箱保护时，模型会错误地删除 $HOME 目录而非临时目录，导致用户文件被意外删除。 该漏洞凸显了 AI 编程代理中的关键安全风险，授予文件系统访问权限的用户可能遭受数据丢失。这强调了在部署此类代理之前需要强大的沙箱和审查机制。 该漏洞发生在启用完全访问模式、关闭沙箱保护且关闭自动审查的情况下。模型试图覆盖 $HOME 环境变量以定义临时目录，但错误地删除了 $HOME 目录。

rss · Simon Willison · 7月16日 17:45

**背景**: Codex 是一个 AI 编程代理，可以在用户系统上执行命令。沙箱技术将代理隔离以防止有害操作，而完全访问模式则移除了这些限制。$HOME 环境变量指向用户的主目录，其中包含个人文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/320198/20260712/chatgpt-work-launch-went-wrong-gpt-56-sol-deleted-user-files-without-permission.htm">ChatGPT Work Launch Went Wrong: GPT - 5 . 6 Sol Deleted User Files ...</a></li>
<li><a href="https://techcrunch.com/2026/07/14/openais-new-flagship-model-deletes-files-on-its-own-people-keep-warning/">OpenAI's new flagship model deletes files on its own... | TechCrunch</a></li>
<li><a href="https://explainx.ai/blog/chatgpt-codex-5-hour-limit-removed-weekly-reset-july-2026">ChatGPT 5-Hour Limit Removed — July 2026 | explainx.ai... | explainx.ai</a></li>

</ul>
</details>

**社区讨论**: 社区表达了震惊和沮丧，许多用户报告数据丢失。一些人批评 OpenAI 没有默认强制启用沙箱，另一些人则呼吁在部署如此强大的代理之前采取更好的保护措施。

**标签**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`, `#bug`

---

<a id="item-12"></a>
## [Thinking Machines Lab 发布开源权重模型 Inkling](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

由 Mira Murati 领导的 Thinking Machines Lab 发布了 Inkling，这是一个开源权重的多模态混合专家 Transformer 模型，总参数量 975B（活跃参数 41B），采用 Apache-2.0 许可，在 45 万亿 token 的文本、图像、音频和视频数据上训练。 Inkling 增强了美国开源权重生态系统，为中国开源模型提供了有竞争力的替代方案，并通过 Tinker 平台支持微调，可能使大型多模态 AI 的访问更加民主化。 Inkling 支持高达 100 万 token 的上下文窗口，并非前沿模型，而是适合定制的强大基础模型；较小的变体 Inkling-Small（总参数量 276B，活跃参数 12B）即将推出。模型卡和训练数据文档明显简略。

rss · Simon Willison · 7月16日 15:35

**背景**: 混合专家（MoE）架构每次输入仅激活部分参数，从而在高效推理的同时实现巨大的总参数量。开源权重模型允许开发者自由下载、微调和部署模型，促进创新和透明度。Thinking Machines Lab 是由前 OpenAI CTO Mira Murati 创立的新 AI 公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our open-weights model - Thinking Machines Lab</a></li>
<li><a href="https://thinkingmachines.ai/inkling/">An efficient open - weights model that reasons over text, image, and...</a></li>
<li><a href="https://artificialanalysis.ai/models/inkling">Inkling - Intelligence, Performance & Price Analysis</a></li>

</ul>
</details>

**标签**: `#open-weights`, `#multimodal`, `#Mixture-of-Experts`, `#AI model release`, `#Thinking Machines Lab`

---

<a id="item-13"></a>
## [Lila Sciences：未来实验室即数据中心](https://www.latent.space/p/the-lab-of-the-future-should-feel) ⭐️ 8.0/10

Lila Sciences 将未来实验室设想为一个数据中心，AI 和机器人在这里生成并利用科学数据，作为训练模型的新前沿。 这种范式转变通过将实验数据视为 AI 的可扩展资源，可能极大地加速科学发现，从而变革制药和材料科学等行业。 文章引用了 Andy Beam 和 Rafa Gómez-Bombarelli 的观点，Lila Sciences 正在构建一个用于生命、化学和材料科学的自主实验室平台。

rss · Latent Space · 7月16日 13:30

**背景**: 传统科学研究依赖手动实验和假设检验，速度慢且规模有限。AI 驱动的科学实验将 AI 与自动化工作流相结合，以生成假设、规划实验并持续优化模型。Lila Sciences 旨在创建一个“科学超级智能”平台，将实验室视为数据中心，由机器人运行实验，AI 从产生的数据中学习。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lila.ai/">LILA | Scientific Superintelligence</a></li>
<li><a href="https://www.linkedin.com/company/lila-sciences">Lila Sciences | LinkedIn</a></li>
<li><a href="https://www.emergentmind.com/topics/ai-driven-scientific-experimentation">AI - Driven Scientific Experimentation</a></li>

</ul>
</details>

**标签**: `#AI`, `#scientific research`, `#robotics`, `#data center`, `#Lila Sciences`

---

<a id="item-14"></a>
## [DeepMind 与 Isomorphic Labs 发布生物韧性 AI 方案](https://deepmind.google/blog/our-approach-to-bioresilience/) ⭐️ 8.0/10

Google DeepMind 与 Isomorphic Labs 联合宣布了他们在生物韧性方面的研究方案，利用 AI 模型增强生物系统适应变化和抵御威胁的能力。 这一举措标志着将 AI 应用于全球生物挑战的重要一步，可能提升大流行防范、药物发现和生态韧性。同时，它为 AI 在生物学中的负责任使用树立了先例。 该公告为高层级声明，技术细节较少，但基于 DeepMind 的 AlphaFold 技术和 Isomorphic Labs 的药物发现专长。重点在于防止 AI 滥用，同时协助疫情应对。

rss · Google DeepMind Blog · 7月16日 09:30

**背景**: 生物韧性指物种或个体适应环境变化的能力。DeepMind 的 AlphaFold 能高精度预测蛋白质结构，Isomorphic Labs 则将 AI 应用于药物发现。此次合作旨在结合这些优势，实现更广泛的生物韧性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bioresilience">Bioresilience - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isomorphic_Labs">Isomorphic Labs</a></li>
<li><a href="https://www.artificialintelligence-news.com/news/examining-google-deepmind-ai-bioresilience-push/">Examining Google DeepMind 's AI bioresilience push</a></li>

</ul>
</details>

**标签**: `#AI`, `#bioresilience`, `#DeepMind`, `#Isomorphic Labs`, `#biology`

---

<a id="item-15"></a>
## [欧盟强制谷歌共享搜索数据并开放安卓 AI](https://arstechnica.com/gadgets/2026/07/its-official-eu-will-force-google-to-share-search-data-and-open-up-ai-on-android/) ⭐️ 8.0/10

欧盟正式根据《数字市场法案》（DMA）强制要求谷歌向第三方共享其搜索数据，并开放安卓上的 AI 功能，理由是竞争担忧。 这项里程碑式的法规可能重塑欧洲的安卓生态系统和 AI 市场，有望增加竞争和用户选择，而谷歌则警告存在隐私和安全风险。 DMA 要求谷歌等守门人确保互操作性和数据访问；不遵守可能导致高达全球营业额 10%的罚款。

rss · Ars Technica AI · 7月16日 20:41

**背景**: 欧盟《数字市场法案》（DMA）于 2022 年 11 月生效，2023 年 5 月适用，针对谷歌、苹果、Meta 等大型平台。它旨在防止这些守门人滥用市场力量，包括强制它们向竞争对手开放服务和数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/EU_Digital_Markets_Act">EU Digital Markets Act</a></li>
<li><a href="https://en.cryptonomist.ch/2026/04/28/android-ai-openness-eu/">EU pressures Google to open Android AI under DMA rules</a></li>

</ul>
</details>

**标签**: `#EU regulation`, `#Google`, `#Android`, `#AI`, `#privacy`

---