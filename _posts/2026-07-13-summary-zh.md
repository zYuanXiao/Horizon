---
layout: default
title: "Horizon Summary: 2026-07-13 (ZH)"
date: 2026-07-13
lang: zh
---

> 从 126 条内容中筛选出 15 条重要资讯。

---

1. [AI 代理自主执行完整勒索软件攻击](#item-1) ⭐️ 9.0/10
2. [OpenAI Codex：终端中的轻量级 AI 编程代理](#item-2) ⭐️ 8.0/10
3. [ComfyUI：扩散模型的模块化图形界面](#item-3) ⭐️ 8.0/10
4. [Vidu S1：在消费级 GPU 上实现实时交互视频生成](#item-4) ⭐️ 8.0/10
5. [SciReasoner：跨学科可解释结构推理模型](#item-5) ⭐️ 8.0/10
6. [AI 进步可能削弱人类专业知识](#item-6) ⭐️ 8.0/10
7. [因果理论应用于大语言模型可解释性](#item-7) ⭐️ 8.0/10
8. [乔治·霍兹：LLM 很棒，但炒作过头了](#item-8) ⭐️ 8.0/10
9. [开源 AI 面临关键的 6 个月考验](#item-9) ⭐️ 8.0/10
10. [苹果起诉 OpenAI 窃取商业机密](#item-10) ⭐️ 8.0/10
11. [Swift-MLX 移植将 Hunyuan3D 带到 Apple Silicon](#item-11) ⭐️ 8.0/10
12. [Moondream 3.1：9B MoE 视觉语言模型，仅 2B 活跃参数](#item-12) ⭐️ 8.0/10
13. [基于摘要化思维链微调的陷阱](#item-13) ⭐️ 8.0/10
14. [修复 3 个 bug，使 Qwen3.5-122B 在 Mac Studio 上实现亚秒级预填充](#item-14) ⭐️ 8.0/10
15. [将 Anthropic 的 J-space 推理应用于 Qwen3-8B](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AI 代理自主执行完整勒索软件攻击](https://www.reddit.com/r/artificial/comments/1uuouu7/someone_built_an_ai_agent_that_hacks_networks_and/) ⭐️ 9.0/10

Sysdig 研究人员记录了首个已知的自主勒索软件操作，名为 JADEPUFFER，其中基于 LLM 的代理自主入侵了 Langflow 服务器，窃取凭证，横向移动，加密数据库并索要赎金——全程无需人工干预。 这表明 AI 代理现在可以端到端执行复杂的多阶段网络攻击，包括自我适应错误，这标志着自主网络威胁的重大升级，并迫使人们重新思考防御策略。 该代理利用了 CVE-2025-3248，这是一个 Langflow 漏洞，允许未经身份验证的远程代码执行，并在遇到格式错误的响应时在 31 秒内重写自己的代码，从失败的登录适应为有效的利用。

reddit · r/artificial · /u/Still_Piglet9217 · 7月12日 19:22

**背景**: Langflow 是一个用于构建 LLM 应用程序的低代码工具，CVE-2025-3248 是一个关键漏洞，允许未经身份验证的攻击者执行任意代码。自主勒索软件是指使用 AI 代理自主规划和执行攻击、实时适应防御的勒索软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion">JADEPUFFER: Agentic ransomware for automated database extortion | Sysdig</a></li>
<li><a href="https://arxiv.org/abs/2402.06664">[2402.06664] LLM Agents can Autonomously Hack Websites</a></li>

</ul>
</details>

**标签**: `#AI security`, `#autonomous agents`, `#cybersecurity`, `#ransomware`, `#LLM`

---

<a id="item-2"></a>
## [OpenAI Codex：终端中的轻量级 AI 编程代理](https://github.com/openai/codex) ⭐️ 8.0/10

OpenAI Codex 是一个在终端中运行的轻量级编程代理，今日在 GitHub 上获得 195 颗星，总星数超过 97,400。它使用 Rust 构建，直接在命令行中提供 AI 驱动的代码生成和辅助功能。 Codex 代表了大型语言模型在软件开发中的实际应用，使 AI 辅助编程可直接在终端中使用。其高社区参与度（超过 97,000 星）和每日增长表明开发者对 AI 驱动的开发工具有浓厚兴趣。 Codex 使用 Rust 编写，这是一种以高性能和内存安全著称的系统编程语言。它包含在 ChatGPT Plus、Pro、Business、Edu 和 Enterprise 计划中，也可作为 Visual Studio Code 扩展使用。

github_trending · GitHub Trending · 7月13日 03:04

**背景**: OpenAI Codex 是一个编程代理，利用 OpenAI 的前沿编码模型帮助开发者完成代码生成、重构和调试等任务。它在终端中运行，提供了基于 IDE 的助手的轻量级替代方案。Rust 是一种强调性能和安全的语言，适合构建可靠的开发工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://marketplace.visualstudio.com/items?itemName=openai.chatgpt">Codex – OpenAI’s coding agent - Visual Studio Marketplace</a></li>
<li><a href="https://chatgpt.com/codex/">Codex in ChatGPT | AI Coding Agents for Software Engineering</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust (programming language)</a></li>

</ul>
</details>

**标签**: `#AI`, `#coding agent`, `#OpenAI`, `#developer tools`, `#Rust`

---

<a id="item-3"></a>
## [ComfyUI：扩散模型的模块化图形界面](https://github.com/Comfy-Org/ComfyUI) ⭐️ 8.0/10

ComfyUI，一个流行的基于图形的扩散模型 GUI 和后端，今天在 GitHub 上新增 125 颗星，总星数超过 12 万。 ComfyUI 的模块化节点界面支持复杂且可定制的 AI 图像生成工作流，使高级扩散模型对艺术家和开发者更加易用。 该仓库使用 Python 编写，拥有超过 14,000 个 fork，表明有一个庞大且活跃的社区为其开发做出贡献。

github_trending · GitHub Trending · 7月13日 03:04

**背景**: 扩散模型是一类生成模型，学习逆转添加噪声的过程以生成新数据（如图像）。ComfyUI 提供了一个可视化图形界面，用户可连接代表不同模型组件的节点，无需编码即可灵活设计工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Diffusion_model">Diffusion model</a></li>
<li><a href="https://www.trendingaitools.com/ai-tools/comfyui-web/">ComfyUI Web: Web- Based GUI for AI Image Workflow Automation</a></li>

</ul>
</details>

**标签**: `#AI`, `#diffusion models`, `#GUI`, `#Python`, `#machine learning`

---

<a id="item-4"></a>
## [Vidu S1：在消费级 GPU 上实现实时交互视频生成](https://huggingface.co/papers/2607.03118) ⭐️ 8.0/10

Vidu S1 是一款实时交互式视频生成模型，支持通过语音指令控制数字角色动画，在消费级 GPU 上以高达 42 FPS 的帧率生成无限长度的视频。 这一突破使得在平价硬件上实现实时交互式视频生成成为可能，为直播内容创作、虚拟角色和互动娱乐开辟了新可能，无需依赖昂贵的云基础设施。 Vidu S1 基于 TurboDiffusion 和 TurboServe 构建，在标准消费级 GPU 上以 42 FPS 的帧率生成 540p 分辨率的视频，并支持上传真人、动漫和宠物的自定义图像，搭配多种语音语调。

huggingface_papers · Hugging Face Papers · 7月10日 00:00

**背景**: 传统的视频生成模型速度慢且需要强大的服务器，难以实现实时交互。TurboDiffusion 将扩散模型加速 100–200 倍且质量损失极小，TurboServe 则优化了服务效率。Vidu S1 结合这两者，在消费级硬件上实现了实时、语音控制的视频生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/thu-ml/TurboDiffusion">GitHub - thu-ml/ TurboDiffusion : TurboDiffusion : 100–200...</a></li>
<li><a href="https://www.vidu.com/vidu-stream">Vidu S1 AI Video Model | Vidu AI</a></li>

</ul>
</details>

**标签**: `#video generation`, `#real-time`, `#voice control`, `#AI`, `#consumer hardware`

---

<a id="item-5"></a>
## [SciReasoner：跨学科可解释结构推理模型](https://huggingface.co/papers/2607.07708) ⭐️ 8.0/10

研究人员推出了 SciReasoner，这是一个多模态科学基础模型，它将结构元素离散化为统一词汇，实现对蛋白质、分子和晶体的可解释推理。该模型在 86 项基准测试中的 67 项上达到最先进性能，将基因本体预测的 F_max 从 0.42 提升至 0.55，逆合成准确率从 0.63 提升至 0.72。 SciReasoner 弥合了准确预测与可解释科学推理之间的鸿沟，使研究人员能够理解模型为何做出特定预测。它通过提供专家可验证的透明推理轨迹，有望加速药物发现和材料科学的发展。 该模型使用结构感知词汇表，将坐标、拓扑和周期性连接表示为可寻址的证据单元。在双盲专家评估中，SciReasoner 的推理轨迹在 98%的案例中被认为优于或相当于前沿大语言模型。

huggingface_papers · Hugging Face Papers · 7月9日 00:00

**背景**: 结构-性质关系是生物学、化学和材料科学的基础，功能由空间和化学组织决定。传统 AI 模型往往缺乏可解释性，导致预测难以被信任。SciReasoner 通过将结构元素离散化为统一词汇，使模型能够在科学约束下逐步推理，从而解决了这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2509.21320">[2509.21320] SciReasoner: Laying the Scientific Reasoning Ground Across Disciplines</a></li>

</ul>
</details>

**标签**: `#AI for Science`, `#Structural Biology`, `#Materials Science`, `#Multimodal Learning`, `#Interpretable AI`

---

<a id="item-6"></a>
## [AI 进步可能削弱人类专业知识](https://arxiv.org/abs/2607.06377) ⭐️ 8.0/10

关于文章《没有理解的自动化》的讨论警告说，随着 AI 系统能力增强，人类可能失去检测 AI 错误所需的专业知识，导致无法验证 AI 输出。 这很重要，因为它突出了一个关键的社会风险：如果我们停止培养能够理解和验证 AI 的专家，我们可能会依赖无法纠正或信任的系统，从而破坏科学、工程和决策中的问责制。 讨论指出，AI 系统通常在不透明推理的情况下产生输出，社区建议强制 AI 通过形式化证明、执行轨迹或来源引用展示其工作，以保持可验证性。

hackernews · root-parent · 7月12日 16:54 · [社区讨论](https://news.ycombinator.com/item?id=48882554)

**背景**: 随着 AI 系统变得更加先进，它们越来越多地被用于自动化以前需要人类专业知识的任务，例如编写代码、生成证明或分析数据。然而，如果人类停止练习这些技能，他们可能会失去批判性评估 AI 输出的能力，从而造成知识差距，使错误更难被发现。

**社区讨论**: 评论者担心 AI 可能取代专家而不培养新专家，导致未来 AI 输出无法验证。一位评论者建议强制 AI 通过形式化证明或执行轨迹展示其工作，另一位则指出即使是当前的专家也可能难以通过他们曾经参加过的考试，突显了专业知识的脆弱性。

**标签**: `#AI`, `#expertise`, `#verification`, `#societal impact`, `#epistemology`

---

<a id="item-7"></a>
## [因果理论应用于大语言模型可解释性](https://cacm.acm.org/news/can-we-understand-how-large-language-models-reason/) ⭐️ 8.0/10

研究人员正在将因果理论应用于大语言模型的机械可解释性研究，旨在理解神经网络中编码的知识是否对应于类似推理的概念。该方法涉及调整权重和激活等实验来探究内部机制。 这项工作对 AI 安全性和透明度具有重要意义，因为理解大语言模型的推理有助于确保这些模型可靠且与人类目标一致。它也推动了可解释 AI 领域的发展，从黑箱分析转向对神经网络的逆向工程。 该研究在 CACM 的一篇文章中被重点介绍，引用了 arXiv 上的论文（2301.04709）和相关的 YouTube 讨论。一个例子显示研究人员通过调整权重和激活观察到模型如何处理时钟时间计算。

hackernews · adunk · 7月12日 18:04 · [社区讨论](https://news.ycombinator.com/item?id=48883090)

**背景**: 机械可解释性是可解释 AI 的一个子领域，旨在通过分析神经网络的内部结构、算法和电路来对其进行逆向工程。因果理论，特别是 Judea Pearl 的框架，提供了因果发现和推断的工具，有助于识别模型组件如何对输出做出贡献。这种结合为理解深度神经网络中的隐藏算法提供了一条路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://en.wikipedia.org/wiki/Causal_AI">Causal AI - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了谨慎的乐观态度，一些人质疑机械可解释性是否能够将大语言模型完全简化为简单的方程。一位评论者指出神经网络中的“意大利面条式代码”类比，认为复杂性可能从根本上限制可解释性。

**标签**: `#mechanistic interpretability`, `#LLMs`, `#causality`, `#AI safety`, `#deep learning`

---

<a id="item-8"></a>
## [乔治·霍兹：LLM 很棒，但炒作过头了](https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html) ⭐️ 8.0/10

乔治·霍兹发表博客文章，认为虽然 LLM 具有变革性，但前沿实验室（如 OpenAI 和 Anthropic）无法捕获它们创造的价值，生产力提升确实存在，但体现在私有的、一次性的软件中，而非可见的新产品。 这一分析挑战了前沿 AI 实验室的高估值，并表明 LLM 的经济效益可能流向用户和开源项目，而非构建模型的公司，这对 AI 领域的投资和商业策略具有影响。 霍兹指出，尽管 LLM 带来了巨大的生产力提升，但缺乏新的可见软件产品，因为收益体现在私有的定制脚本和工具中。他还指出，开源模型正在使 LLM 能力商品化，使得前沿实验室更难收取高价。

hackernews · therepanic · 7月12日 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48883343)

**背景**: 乔治·霍兹（geohot）是著名黑客和企业家，创立了 comma.ai 并开发了 tinygrad 深度学习框架。前沿实验室指 OpenAI、Anthropic 和 Google DeepMind 等开发最先进大语言模型的领先 AI 公司。关于价值捕获的争论核心在于这些公司能否充分将 AI 货币化，以证明其数万亿美元估值的合理性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/George_Hotz">George Hotz</a></li>
<li><a href="https://drux.space/search/are-we-as-society-going-to-let-llm-companies-take-all-the-va-dvzqj">Are we as society going to let LLM companies take all the… — Drux</a></li>

</ul>
</details>

**社区讨论**: 评论者大多同意霍兹的观点，分享了使用 LLM 为小众需求构建一次性软件的个人经验。一些人指出，像 Sonnet 4 和 Opus 4.5 这样的新模型感觉像是阶跃变化，但总体情绪是前沿实验室面临价值捕获问题，开源替代方案正在侵蚀其护城河。

**标签**: `#LLM`, `#AI hype`, `#open source`, `#productivity`, `#valuation`

---

<a id="item-9"></a>
## [开源 AI 面临关键的 6 个月考验](https://www.interconnects.ai/p/6-months-to-live-for-open-models) ⭐️ 8.0/10

一篇分析文章认为，当前时期是开源 AI 模型可行性的最严峻考验，暗示它们大约有六个月时间来证明自身价值。 这场辩论直接影响 AI 开发的未来方向，决定开源模型能否与专有系统竞争并在生态系统中保持一席之地。 该分析未明确说明哪些模型或指标正在被测试，但挑衅性的标题强调了开源社区展示进展的紧迫性。

rss · Interconnects · 7月12日 16:47

**背景**: 开源 AI 模型，如来自 Meta 和 Mistral 的模型，因其可访问性和可定制性而受到欢迎。然而，它们在性能上往往落后于 GPT-4 等专有模型，引发了对其长期可行性的质疑。

**标签**: `#open source`, `#AI`, `#viability`, `#models`, `#analysis`

---

<a id="item-10"></a>
## [苹果起诉 OpenAI 窃取商业机密](https://www.reddit.com/r/LocalLLaMA/comments/1uus189/apple_sues_openai_alleging_trade_secret_theft/) ⭐️ 8.0/10

苹果已对 OpenAI 提起诉讼，指控其在整个组织层面系统性地窃取商业机密。 这起诉讼可能重塑 AI 行业的知识产权执法，并为在 AI 快速发展中如何保护商业机密树立先例。 诉状称 OpenAI 的计划涉及“各个层面”的商业机密盗窃，但涉嫌盗窃的具体细节尚未公开披露。

reddit · r/LocalLLaMA · /u/fallingdowndizzyvr · 7月12日 21:25

**背景**: 商业机密是提供竞争优势的机密商业信息。苹果和 OpenAI 是 AI 领域的主要参与者，苹果专注于设备端 AI，而 OpenAI 专注于大型语言模型。这起诉讼凸显了专有 AI 开发与开源或协作方法之间的紧张关系。

**社区讨论**: r/LocalLLaMA 上的 Reddit 社区反应不一，一些用户对苹果的说法持怀疑态度，另一些则担心这对开源 AI 的影响。少数评论者指出，以保密著称的苹果起诉商业机密盗窃具有讽刺意味。

**标签**: `#Apple`, `#OpenAI`, `#trade secrets`, `#lawsuit`, `#AI industry`

---

<a id="item-11"></a>
## [Swift-MLX 移植将 Hunyuan3D 带到 Apple Silicon](https://www.reddit.com/r/LocalLLaMA/comments/1uuga40/local_image_to_3d_2gb_ram_20s_apple_silicon_iphone/) ⭐️ 8.0/10

一位开发者完成了腾讯 Hunyuan3D 模型的 Swift-MLX 移植，使得在包括 iPhone 在内的 Apple Silicon 设备上能够进行图像到 3D 的生成，小模型推理时间低于 20 秒，内存使用低于 2 GB。 这将高质量的 3D 资产生成带到本地 Apple 设备，无需依赖云端，使 Mac 和 iPhone 上的开发者和爱好者能够更便捷地创建 3D 内容。 该移植支持 Hunyuan3D-Shape 和 Hunyuan3D-Paint 模型，在 M4 Max 上的基准测试显示，形状（小）模型耗时 20.9 秒，内存约 5.6 GB；绘制（RGB）模型耗时 231 秒，内存约 38 GB。应用 Modelr 已开源，可在 Mac 和 iOS 上使用。

reddit · r/LocalLLaMA · /u/arduinoRPi4 · 7月12日 14:00

**背景**: Hunyuan3D 是腾讯推出的一系列大规模扩散模型，用于从图像或文本生成高分辨率带纹理的 3D 资产。MLX 是 Apple 开发的开源数组框架，用于在 Apple Silicon 上高效运行机器学习，提供类似 NumPy 的 API。Swift-MLX 是 MLX 的 Swift API，允许原生集成到 Swift 应用中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tencent-Hunyuan/Hunyuan3D-2">GitHub - Tencent-Hunyuan/Hunyuan3D-2: High-Resolution 3D Assets Generation with Large Scale Hunyuan3D Diffusion Models. · GitHub</a></li>
<li><a href="https://github.com/ml-explore/mlx-swift">GitHub - ml-explore/ mlx - swift : Swift API for MLX · GitHub</a></li>
<li><a href="https://mlx-framework.org/">MLX</a></li>

</ul>
</details>

**标签**: `#3D generation`, `#Apple Silicon`, `#MLX`, `#image-to-3D`, `#local AI`

---

<a id="item-12"></a>
## [Moondream 3.1：9B MoE 视觉语言模型，仅 2B 活跃参数](https://www.reddit.com/r/LocalLLaMA/comments/1uunqcz/moondream319ba2b/) ⭐️ 8.0/10

Moondream 3.1 是一个采用混合专家架构的视觉语言模型，总参数量 9B，但仅 2B 活跃参数，在保持快速和低成本部署的同时，实现了最先进的视觉推理和检测能力。 该模型证明了 MoE 架构可以在不牺牲性能的情况下大幅降低 VLM 的推理成本，使先进的视觉 AI 更易于在实际应用中使用。 该模型原生支持查询、检测、指向和描述任务，并返回结构化输出。它是开源的，专为高效部署而设计。

reddit · r/LocalLLaMA · /u/secopsml · 7月12日 18:40

**背景**: 视觉语言模型（VLM）结合了图像和文本理解能力，但大型模型运行成本往往很高。混合专家（MoE）架构使用多个专门的子网络（专家），每次输入只激活其中一部分，从而在保持高容量的同时减少计算量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision-language_model">Vision-language model</a></li>

</ul>
</details>

**标签**: `#vision-language model`, `#mixture-of-experts`, `#efficient AI`, `#visual reasoning`, `#open-source`

---

<a id="item-13"></a>
## [基于摘要化思维链微调的陷阱](https://www.reddit.com/r/LocalLLaMA/comments/1uuvkw9/why_do_people_keep_finetuning_on/) ⭐️ 8.0/10

一篇 Reddit 帖子批判性地审视了在来自 Claude 等专有模型的摘要化或审查过的思维链轨迹上微调开源模型的做法，认为这反而会降低性能而非提升。 这凸显了 LLM 社区对蒸馏保真度的根本误解，可能导致许多从业者将资源浪费在损害模型能力的微调策略上。 帖子特别提到“Fable 微调”作为例子，指出 Anthropic 模型的推理轨迹与实际思维链完全不同，使得最终的微调结果必然更差。

reddit · r/LocalLLaMA · /u/wombweed · 7月12日 23:54

**背景**: 思维链推理涉及模型在得出答案前生成显式的中间步骤。知识蒸馏将知识从大型“教师”模型转移到较小的“学生”模型，通常使用教师模型的输出作为训练数据。然而，当教师模型的内部思维链在被用于蒸馏之前被摘要化或审查时，学生模型会学习到扭曲的推理过程，从而可能降低其性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://huggingface.co/Trilogix1/Anthropics-Fable-finetuned-in-Qwen3.6-35B">Trilogix1/Anthropics- Fable - finetuned -in-Qwen3.6-35B · Hugging Face</a></li>
<li><a href="https://arxiv.org/html/2511.10714v1">BadThink: Triggered Overthinking Attacks on Chain - of - Thought ...</a></li>

</ul>
</details>

**社区讨论**: 该帖子引发了实质性讨论，许多评论者同意在摘要化轨迹上蒸馏是有缺陷的，而一些人则辩护称这是注入推理模式的实用方法。少数人指出问题不在于蒸馏本身，而在于所用轨迹的质量。

**标签**: `#LLM fine-tuning`, `#distillation`, `#chain-of-thought`, `#model capability`, `#reasoning traces`

---

<a id="item-14"></a>
## [修复 3 个 bug，使 Qwen3.5-122B 在 Mac Studio 上实现亚秒级预填充](https://www.reddit.com/r/LocalLLaMA/comments/1uuwrc0/running_qwen35122b_on_mac_studio_96gb_fixed_3/) ⭐️ 8.0/10

一位开发者修复了 qMLX 服务栈（rapid-mlx 的一个分支）中的三个 bug，将 Qwen3.5-122B 在 96GB M3 Ultra Mac Studio 上的预填充时间从几分钟降至亚秒级，使长上下文推理变得可用。 这一突破使得像 Qwen3.5-122B 这样的大型混合 MoE 模型在消费级硬件上进行本地代理编程变得实用，大大降低了离线运行最先进 LLM 的门槛。 三个 bug 分别是：唯一消息 ID 导致字节精确 KV 缓存匹配失败的提示不稳定性、中断的流式回复未持久化、以及后台写入器创建不匹配检查点导致激进驱逐。修复后，一个 53k token 的缓存上下文仅需预填充 33 个 token。

reddit · r/LocalLLaMA · /u/marzukia · 7月13日 00:47

**背景**: LLM 使用 KV 缓存来避免重新计算之前的 token，但要求输入前缀完全匹配。像 Qwen3.5 这样的混合注意力模型结合了局部和全局注意力，使缓存更加复杂。qMLX 栈是一个针对 Apple Silicon 优化的专用服务框架，适用于此类模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mrzk.io/posts/qmlx-maximising-ai-psychosis-minmaxing-mac-studio/">qMLX: Maximising my AI psychosis by minmaxing my Mac Studio · Andryo Marzuki - Net Zero Productivity by 2050</a></li>
<li><a href="https://betterstack.com/community/guides/ai/omlx-apple-silicon/">oMLX: Apple Silicon-Optimized LLM Inference with Two-Tier KV Caching | Better Stack Community</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区称赞了详细的调试过程和开源贡献，一些用户提到在混合注意力缓存中遇到类似问题，并表示有兴趣测试该分支。作者积极互动，解释了分叉而非向上游提交的原因。

**标签**: `#LLM inference`, `#Mac Studio`, `#bug fix`, `#long context`, `#qMLX`

---

<a id="item-15"></a>
## [将 Anthropic 的 J-space 推理应用于 Qwen3-8B](https://www.reddit.com/r/LocalLLaMA/comments/1uugulk/anthropic_found_claude_reasoning_in_silence/) ⭐️ 8.0/10

一位 Reddit 用户将 Anthropic 的 Jacobian 透镜应用于开源模型 Qwen3-8B，检测到静默推理（J-space），并利用它在工具调用前捕捉散文漂移，然后将其接入带有 LoRA 恢复的智能体防护循环。 这表明 Anthropic 新颖的 J-space 研究可以在开源模型上复现，从而实现实用的智能体安全机制，如检测散文漂移和防止防护循环失败，这对可靠的 AI 智能体至关重要。 该用户在本地将 Jacobian 透镜应用于 Qwen3-8B，利用它捕捉散文漂移（例如模型倾向于输出'To, You, Do…'而非 JSON），并构建了智能体防护，可停止、取消或保留有用空间，并将恢复蒸馏到 LoRA 数据中。

reddit · r/LocalLLaMA · /u/Murky-Sign37 · 7月12日 14:22

**背景**: Anthropic 最近发现大型语言模型有一个隐藏的内部工作空间，称为 J-space，其中静默推理发生在神经激活中，没有可见文本。Jacobian 透镜是一种可解释性工具，用于估计哪些内部活动模式影响未来的 token 生成，使研究人员能够观察这种隐藏的推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/global-workspace">A global workspace in language models \ Anthropic</a></li>
<li><a href="https://www.developersdigest.tech/blog/anthropic-j-space-global-workspace-llm">Anthropic Discovers J-Space: A Global Workspace Inside Language Models - Developers Digest</a></li>
<li><a href="https://www.1950.ai/post/anthropic-s-j-lens-unlocks-the-hidden-logic-of-ai-a-major-leap-in-understanding-large-language-mode">Anthropic's J- Lens Unlocks the Hidden Logic of AI, A Major Leap in...</a></li>

</ul>
</details>

**标签**: `#mechanistic interpretability`, `#LLM reasoning`, `#open source`, `#agent safety`, `#Qwen`

---