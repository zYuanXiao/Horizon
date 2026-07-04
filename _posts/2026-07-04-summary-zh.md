---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> 从 158 条内容中筛选出 15 条重要资讯。

---

1. [欧盟议会间谍调查成员遭飞马间谍软件攻击](#item-1) ⭐️ 9.0/10
2. [Mistral 发布 Leanstral-1.5，一款 6B 活跃参数的形式化验证模型](#item-2) ⭐️ 9.0/10
3. [Superpowers：热门智能体技能框架](#item-3) ⭐️ 8.0/10
4. [Anthropic 的 Claude Code 在 GitHub 上星数激增](#item-4) ⭐️ 8.0/10
5. [程序即权重：将自然语言规范编译为紧凑神经制品](#item-5) ⭐️ 8.0/10
6. [面向长周期 LLM 智能体的有界记忆测试平台](#item-6) ⭐️ 8.0/10
7. [Current AI 发布开源 AI 差距地图](#item-7) ⭐️ 8.0/10
8. [课程创作者报告销售额因 AI 下降超过 50%](#item-8) ⭐️ 8.0/10
9. [HAT-4D：单目视频生成 4D 交互场景](#item-9) ⭐️ 8.0/10
10. [LongCat 2 模型权重发布在 Hugging Face 上](#item-10) ⭐️ 8.0/10
11. [ComfyUI 工作流无需 LoRA 即可根据故事生成漫画](#item-11) ⭐️ 8.0/10
12. [CDD 仅从 logits 恢复微调逐字数据](#item-12) ⭐️ 8.0/10
13. [简单提示注入可提取 60-70% AI 助手的系统提示](#item-13) ⭐️ 8.0/10
14. [Elixir 1.2 发布渐进式集合论类型系统](#item-14) ⭐️ 8.0/10
15. [阿里巴巴 Page-Agent：用自然语言控制网页](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [欧盟议会间谍调查成员遭飞马间谍软件攻击](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 9.0/10

公民实验室披露，欧洲议会议员斯特利奥斯·库洛格卢（Stelios Kouloglou）曾参与调查间谍软件滥用问题的委员会，其设备在 2022 年和 2023 年至少三次被成功感染飞马间谍软件。 这一事件表明，国家支持的间谍软件正被用于对付负责调查其滥用行为的官员，这破坏了民主监督，并对欧盟机构构成直接威胁。 2022 年 10 月的首次感染与已知的针对俄罗斯和白俄罗斯流亡记者的飞马间谍软件活动重叠，表明一个拥有跨欧洲授权的飞马客户应对此负责。

hackernews · ledoge · 7月3日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马间谍软件是由以色列 NSO 集团开发的一款强大间谍软件，能够远程入侵移动设备并提取数据、信息和录音。公民实验室是多伦多大学的一个研究小组，专门调查数字威胁，并已揭露全球多起飞马间谍软件滥用事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，包括希腊、波兰和意大利在内的多个欧盟成员国与飞马间谍软件滥用有关，有人认为此次攻击可能是由希腊政府而非外部行为者策划的。其他人质疑为何欧盟议员使用个人设备处理敏感工作，从而面临机密信息泄露的风险。

**标签**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#European Parliament`, `#surveillance`

---

<a id="item-2"></a>
## [Mistral 发布 Leanstral-1.5，一款 6B 活跃参数的形式化验证模型](https://www.reddit.com/r/LocalLLaMA/comments/1umgdhx/mistral_released_leanstral15119ba6b/) ⭐️ 9.0/10

Mistral AI 发布了 Leanstral-1.5-119B-A6B，这是一款混合专家模型，拥有 60 亿活跃参数，在形式化验证中取得了最先进的结果，包括在 miniF2F 基准测试上达到饱和，并在开源仓库中发现了 5 个真实漏洞。 此次发布标志着自动定理证明和代码验证领域的重大进步，使开发者能够正式验证软件正确性，并捕获传统测试和模糊测试可能遗漏的边界情况漏洞。 该模型通过中期训练、监督微调和基于 CISPO（裁剪重要性采样策略优化）的强化学习进行训练。它在 FATE-H 上达到 87%，在 FATE-X 上达到 34%，并解决了 672 个 PutnamBench 问题中的 587 个。

reddit · r/LocalLLaMA · /u/Tall-Ad-7742 · 7月3日 14:44

**背景**: Leanstral-1.5 是一款混合专家（MoE）模型，针对使用 Lean 4 定理证明器的形式化验证进行了优化。形式化验证利用数学证明来确保软件正确性，补充了传统的测试方法。miniF2F 基准测试包含形式化的奥林匹克级别数学问题，用于评估定理证明能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://emelia.io/hub/leanstral-mistral-ai-formal-verification">Leanstral by Mistral AI: The AI That Proves Your Code Is Correct</a></li>
<li><a href="https://arxiv.org/abs/2109.00110">[2109.00110] MiniF2F: a cross-system benchmark for formal ...</a></li>

</ul>
</details>

**社区讨论**: 一些评论者对“该漏洞会被测试遗漏”的说法提出质疑，指出这是一个经典的边界条件。其他人则指出，该模型仅与半年前的旧模型进行了比较，并对选择 Lean 4 而非 Isabelle/HOL 或 TLA+ 等其他形式化验证工具表示好奇。

**标签**: `#AI`, `#formal verification`, `#Mistral`, `#theorem proving`, `#open-source`

---

<a id="item-3"></a>
## [Superpowers：热门智能体技能框架](https://github.com/obra/superpowers) ⭐️ 8.0/10

GitHub 仓库 obra/superpowers 单日获得超过 1209 颗星，总星数达 245,604，成为热门项目，为 AI 编码智能体提供开源智能体技能框架和软件开发方法论。 该框架提供了一种可组合、零依赖的方法论，能将 AI 编码助手转变为更高效的智能体，满足了快速发展的 AI 辅助软件开发领域的关键需求。 Superpowers 支持多种 AI 编码工具，包括 Claude Code、Cursor、Codex、OpenCode 和 Gemini CLI，基于可组合技能构建，并附带初始指令以确保正确使用。

github_trending · GitHub Trending · 7月4日 03:27

**背景**: 智能体技能框架旨在通过提供结构化、可复用的指令和脚本来扩展 AI 编码智能体的能力。该项目由 Prime Radiant 的 Jesse Vincent 创建，提供了一套完整的软件开发方法论，帮助智能体按需发现和加载技能，类似于 Microsoft 的 Agent Skills。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/obra/superpowers">GitHub - obra / superpowers : An agentic skills framework & software...</a></li>
<li><a href="https://grokipedia.com/page/Superpowers_agentic_skills_framework">Superpowers (agentic skills framework)</a></li>
<li><a href="https://ai-trove.com/en/superpowers">Superpowers — agentic skills framework & software</a></li>

</ul>
</details>

**标签**: `#agentic-framework`, `#software-development`, `#methodology`, `#github-trending`

---

<a id="item-4"></a>
## [Anthropic 的 Claude Code 在 GitHub 上星数激增](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic 的 Claude Code 是一款基于终端的智能编码工具，今日在 GitHub 上获得 221 颗星，总星数超过 135,000 颗。 这一激增反映了开发者对能够理解整个代码库并自动化复杂工作流的 AI 编码助手的浓厚兴趣，可能提升软件工程生产力。 Claude Code 直接在终端中运行，使用自然语言执行任务、解释代码和管理 git 工作流，由 Anthropic 用 Python 构建。

github_trending · GitHub Trending · 7月4日 03:27

**背景**: 智能编码工具是能够以最少人工干预执行多步开发任务的 AI 系统。Claude Code 就是这样一个驻留在终端中的工具，可以读取和编辑代码、运行命令，帮助开发者更快地交付产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal , IDE</a></li>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/overview">Claude Code overview - Anthropic</a></li>

</ul>
</details>

**标签**: `#AI coding assistant`, `#developer tools`, `#Anthropic`, `#terminal`, `#agentic`

---

<a id="item-5"></a>
## [程序即权重：将自然语言规范编译为紧凑神经制品](https://huggingface.co/papers/2607.02512) ⭐️ 8.0/10

研究人员提出了模糊函数编程，并通过程序即权重（PAW）实现：一个在 FuzzyBench（1000 万示例）上训练的 4B 编译器，为冻结的 0.6B 解释器生成参数高效适配器，其性能与 32B 模型相当，但推理内存仅需 1/50。 该范式将基础模型从逐个输入的问题解决者转变为工具构建者，使得日志告警或 JSON 修复等模糊函数能够廉价、本地执行，无需依赖大型 API 调用。这可能使日常编程任务中的高质量 AI 更加普及。 PAW 编译器是一个 4B 模型，在 FuzzyBench（一个包含 1000 万自然语言到适配器示例的新数据集）上训练。解释器是冻结的 0.6B Qwen3 模型，在 MacBook M3 上以 30 tokens/s 运行，通过直接提示达到与 Qwen3-32B 相当的性能。

huggingface_papers · Hugging Face Papers · 7月3日 00:00

**背景**: 许多编程任务（如日志行告警、修复格式错误的 JSON）难以用规则指定，通常外包给大型语言模型 API，这带来了成本、延迟和可重复性问题。模糊函数编程旨在将自然语言规范编译为紧凑、可本地执行的神经制品，结合了 LLM 的灵活性和传统程序的效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.02512">Program -as-Weights: A Programming Paradigm for Fuzzy Functions</a></li>
<li><a href="https://huggingface.co/papers/2607.02512">Paper page - Program -as-Weights: A Programming Paradigm for...</a></li>

</ul>
</details>

**标签**: `#programming paradigms`, `#neural compilation`, `#fuzzy functions`, `#parameter-efficient adapters`, `#natural language specification`

---

<a id="item-6"></a>
## [面向长周期 LLM 智能体的有界记忆测试平台](https://huggingface.co/papers/2607.02255) ⭐️ 8.0/10

研究人员提出了 AgenticSTS，这是一个面向长周期 LLM 智能体的有界记忆测试平台，通过类型化检索组装全新提示，从而实现对记忆组件的隔离分析。在《Slay the Spire 2》中，固定 A0 消融实验显示，添加战略技能后胜率从 3/10 提升至 6/10。 这项工作通过引入有界记忆契约，使提示大小与运行长度无关，从而实现了可重复的消融研究，解决了长周期智能体设计中的关键挑战。它为研究显式记忆层如何影响智能体决策提供了经过验证的方法论，对复杂决策任务具有重要意义。 有界契约确保每个决策都通过类型化检索组装的全新提示做出，不附加任何跨决策原始记录。该测试平台包含 298 条带有条件标签的完整轨迹、冻结的记忆/技能快照以及分析脚本，均已公开发布。

huggingface_papers · Hugging Face Papers · 7月3日 00:00

**背景**: 长周期 LLM 智能体需要记忆来在多次交互中持久化和回忆信息，但传统方法将所有历史上下文附加到每个提示中，导致提示无限增长且难以隔离单个记忆组件的影响。有界契约将记忆视为关于每个未来决策允许看到什么的契约，通过 top-k 检索限制提示大小。《Slay the Spire 2》是一款复杂的卡牌构筑游戏，需要数百个战术和战略决策，为测试提供了具有挑战性的环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/papers/2607.02255">Paper page - AgenticSTS: A Bounded - Memory Testbed for...</a></li>
<li><a href="https://arxiv.org/pdf/2607.02255">AgenticSTS: A Bounded - Memory Testbed for Long-Horizon LLM ...</a></li>
<li><a href="https://github.com/AlayaLab/AgenticSTS">AlayaLab/AgenticSTS: Bounded , typed, ablatable memory contract ...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#memory`, `#decision-making`, `#testbed`, `#Slay the Spire`

---

<a id="item-7"></a>
## [Current AI 发布开源 AI 差距地图](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI 是一家在 2025 年 2 月巴黎人工智能行动峰会上成立的非营利组织，已获得 4 亿美元承诺资金。它发布了开源 AI 差距地图 v0.1，索引了开源 AI 栈中的 421 个产品，包括来自 228 个组织的 266 个软件工具、85 个模型、50 个数据集和 20 个硬件项目。 该地图提供了开源 AI 生态系统的结构化、数据驱动概览，帮助开发者、研究人员和政策制定者识别差距和机遇。底层数据以 MIT 许可证发布，支持进一步分析和社区贡献。 该地图将产品组织到栈的 3 个层（模型组件、产品/用户体验和基础设施）的 14 个类别中，并跟踪了长尾中的 24,400 个额外工件。数据以 1,184 个 YAML 文件和包含 16,185 个 GitHub 仓库的 CSV 文件形式在 GitHub 上提供，并可通过 Datasette Lite 进行探索。

rss · Simon Willison · 7月3日 22:04

**背景**: Current AI 是一个全球性的非营利合作伙伴关系，旨在构建 AI 的公共选项，获得了多方大量资金支持。2025 年 2 月在巴黎举行的人工智能行动峰会是一个重要的国际活动，聚焦于 AI 治理和公共利益 AI。差距地图旨在系统性地编录开源 AI 领域，该领域虽发展迅速但缺乏全面的地图。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.currentai.org/">Current AI | Building Public Interest AI Technology Together</a></li>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1</a></li>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map - simonwillison.net</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI`, `#ecosystem`, `#mapping`

---

<a id="item-8"></a>
## [课程创作者报告销售额因 AI 下降超过 50%](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) ⭐️ 8.0/10

知名课程创作者 Josh W. Comeau 报告称，其最新课程销量预计仅为通常水平的三分之一，现有课程销售额同比下滑超过 50%，他将此归因于 AI 引发的开发者就业不确定性以及 LLM 取代付费教育内容。 来自多位课程创作者的第一手数据表明，开发者教育市场正在发生结构性转变：AI 一方面因就业担忧降低了学习需求，另一方面用免费的 LLM 辅导替代付费内容，威胁独立教育工作者的生计。 Comeau 的第三门课程“Whimsical Animations”销量约为通常水平的三分之一，他与其他创作者交流后发现，所有人收入均下降 50%以上，参与度降低，许多人转向 LLM，而 LLM 未经同意或补偿即复制其作品。

rss · Simon Willison · 7月3日 21:25

**背景**: 长期以来，在线课程创作者依靠向寻求技能提升的开发者销售优质教育内容为生。然而，GPT-4 等大型语言模型（LLM）的快速发展使得个性化辅导成本降低，削弱了付费课程的感知价值。与此同时，AI 驱动的自动化担忧广泛蔓延，开发者因不确定未来就业前景而犹豫是否投入时间和金钱学习新技能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://economy.ac/review/2026/01/202601287061">When the Children Replace the Parent: How LLMs Replace ...</a></li>
<li><a href="https://arxiv.org/html/2409.11917">LLMs in Education: Novel Perspectives, Challenges, and ...</a></li>
<li><a href="https://files.eric.ed.gov/fulltext/EJ1487508.pdf">Assessing the Potential Challenges of Paid LLMs and ...</a></li>

</ul>
</details>

**标签**: `#AI impact`, `#developer education`, `#online courses`, `#job market`, `#LLMs`

---

<a id="item-9"></a>
## [HAT-4D：单目视频生成 4D 交互场景](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247901356&idx=3&sn=54ee94026f76691a380cd3ea214e0def) ⭐️ 8.0/10

上海交通大学等机构提出 HAT-4D，这是首个从单目视频中重建多物体 3D 几何、时间动态和物理交互的智能体框架。 这一突破消除了对昂贵多摄像头动作捕捉棚的需求，使任何拥有单摄像头的人都能进行 4D 交互场景重建，可能彻底改变电影制作、游戏和机器人等领域。 HAT-4D 在 arXiv 论文（2606.28215）中详细描述，旨在从单段视频输入中处理多个物体及其物理交互，例如用刀切香蕉。

rss · 量子位 · 7月3日 03:43

**背景**: 传统的 4D 重建（3D+时间）通常需要多视角设置或昂贵的动作捕捉系统。近期如 CAT4D 和 Vivid4D 等工作也致力于将单目视频提升到 4D，但 HAT-4D 特别关注多物体物理交互，这是一个更具挑战性的任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.28215">[2606.28215] HAT-4D: Lifting Monocular Video for 4D Multi ...</a></li>
<li><a href="https://arxiv.org/html/2606.28215v1">HAT-4D: Lifting Monocular Video for 4D Multi-Object ...</a></li>

</ul>
</details>

**标签**: `#computer vision`, `#4D reconstruction`, `#AI`, `#motion capture`, `#monocular video`

---

<a id="item-10"></a>
## [LongCat 2 模型权重发布在 Hugging Face 上](https://www.reddit.com/r/LocalLLaMA/comments/1umo8zu/longcat_2_model_weights_have_been_published/) ⭐️ 8.0/10

美团在 Hugging Face 上发布了 LongCat 2.0 模型的 INT8 和 FP8 量化权重，使得长上下文 LLM 推理能够在降低内存占用的情况下进行。 此次发布使得长上下文 LLM 更易于本地部署，因为量化权重在保持性能的同时大幅降低了内存需求，惠及开源 AI 社区。 INT8 量化使用 8 位整数表示权重，而 FP8 使用 8 位浮点格式；两者均受现代硬件支持，可在消费级 GPU 上实现高效推理。

reddit · r/LocalLLaMA · /u/RhubarbSimilar1683 · 7月3日 19:49

**背景**: 量化将模型权重从 32 位浮点数降低到 8 位精度，内存使用减少约 75%，而精度损失极小。长上下文 LLM 可以一次性处理数千个 token，适用于文档分析、长文推理等任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mathworks.com/company/technical-articles/what-is-int8-quantization-and-why-is-it-popular-for-deep-neural-networks.html">What Is int8 Quantization and Why Is It Popular for Deep ...</a></li>
<li><a href="https://rcrtech.com/semiconductor-news/llms-quantization-fp8-fp4-int8/">LLMs and quantization: FP8, FP4, and INT8 explained</a></li>
<li><a href="https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/">Mastering LLM Techniques: Inference Optimization | NVIDIA Technical...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-source`, `#quantization`, `#long-context`, `#Hugging Face`

---

<a id="item-11"></a>
## [ComfyUI 工作流无需 LoRA 即可根据故事生成漫画](https://www.reddit.com/r/StableDiffusion/comments/1umhul8/comfyui_instant_storytocomic_generator_no_loras/) ⭐️ 8.0/10

一个 ComfyUI 工作流被发布，它可以直接根据书面故事生成一致的漫画页面，仅使用基于语言的世界描述，无需 LoRA、参考图像或 ControlNet。 这种方法展示了 AI 辅助叙事中的范式转变，通过语言而非视觉参考实现一致性，可能简化漫画创作并使叙事生成更加普及。 该工作流使用标准 ComfyUI 节点和一个小的 Python 脚本将生成的脚本分割成页面，依靠重复的规范语义描述来保持独立生成图像之间的一致性。

reddit · r/StableDiffusion · /u/aurelm · 7月3日 15:41

**背景**: ComfyUI 是一个基于节点的 Stable Diffusion 界面，允许用户创建自定义图像生成工作流。传统的人物一致性方法通常需要 LoRA 训练、ControlNet 或参考图像，这可能耗时且资源密集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://comfy.org/workflows/">ComfyUI Workflows - Free AI Generation Workflows</a></li>
<li><a href="https://docs.comfy.org/development/core-concepts/workflow">Workflow - ComfyUI</a></li>
<li><a href="https://civitai.com/articles/27654/character-consistency-without-loras-free-360-viewers-with-ltx-video-23-in-comfyui">Character Consistency Without LoRAs : Free 360° Viewers... | Civitai</a></li>

</ul>
</details>

**社区讨论**: 社区讨论活跃且富有洞察力，用户探讨了仅语言一致性方法的影响和局限性，指出其可能使漫画创作民主化，同时质疑其在复杂叙事中的稳健性。

**标签**: `#Stable Diffusion`, `#ComfyUI`, `#AI comic generation`, `#character consistency`, `#workflow`

---

<a id="item-12"></a>
## [CDD 仅从 logits 恢复微调逐字数据](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

研究人员提出了对比解码差异分析（CDD），这是一种灰盒方法，通过对比基础模型和微调模型的 logits 来恢复 LLM 中的逐字微调数据，在四个模型家族（1B-32B 参数）的 19/20 个模型对上实现了 4+/5 的恢复分数，且无需访问权重。 CDD 仅通过 logits 访问即可实现逐字内容恢复，性能优于 Activation Difference Lens (ADL)等白盒方法，显著推动了模型可解释性和安全性。这有助于检测 LLM 中的未经授权微调、数据泄露或隐藏后门。 CDD 使用单一默认配置，无需逐模型校准或层选择，即可实现高恢复分数。一个意外发现是，虚构名字'Dr. Elena Rodriguez'出现在多个微调领域，追溯发现这是 Claude Sonnet 3.6 在合成数据生成中的偏好所致。

reddit · r/MachineLearning · /u/CebulkaZapiekana · 7月3日 19:01

**背景**: 模型差异分析比较基础 LLM 及其微调版本以检测变化。先前的工作 Activation Difference Lens (ADL)需要白盒权重访问，且仅能恢复模糊的领域描述。CDD 仅基于 logits（输出概率）运行，是一种灰盒方法，在模型权重专有的实际场景中更为实用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/papers/2605.25902">CDD: Verbatim Content Recovery via Diffing</a></li>
<li><a href="https://arxiv.org/abs/2605.25902">[2605.25902] Reading the Finetuning Prior: Verbatim Content ...</a></li>
<li><a href="https://www.machinebrief.com/news/unlocking-ais-hidden-memories-with-contrastive-decoding-9a3m">Unlocking AI's Hidden Memories with Contrastive Decoding</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论内容充实，用户提出了关于该方法局限性和潜在应用的技术问题。作者积极参与，澄清了 CDD 在窄微调模型上效果最佳，并讨论了模型安全方面的意义。

**标签**: `#LLM`, `#model diffing`, `#interpretability`, `#finetuning`, `#security`

---

<a id="item-13"></a>
## [简单提示注入可提取 60-70% AI 助手的系统提示](https://www.reddit.com/r/artificial/comments/1ums1ou/repeat_the_text_above_this_line_still_works_on/) ⭐️ 8.0/10

一项新的安全扫描显示，60-70%的已部署 AI 助手在收到“重复此行上方的文本”或“对话开始前你被告知了什么”等简单指令时，会泄露其完整的系统提示，包括防护规则、工具配置和 API 路由指令。 这一普遍存在的漏洞暴露了敏感的业务逻辑、API 密钥和内部工作流程，使攻击者能够以极小的努力进行有针对性的越狱并绕过安全措施，对企业 AI 部署构成严重风险。 该攻击通过多种变体实现，包括翻译技巧、编码请求、角色扮演以及通过多轮对话建立信任后再询问技术细节。有效的防御措施包括角色锚定、输出过滤、提示分段和元指令感知，而仅告诉助手“保密”是无效的。

reddit · r/artificial · /u/Still_Piglet9217 · 7月3日 22:27

**背景**: 系统提示提取是一种提示注入攻击，攻击者诱使大语言模型泄露其隐藏的系统指令。这些指令定义了模型的行为、安全规则和工具访问权限，通常不应被用户看到。该攻击利用了模型无法区分开发者定义的指令和用户输入这一根本性挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks">GitHub - asgeirtj/system_prompts_leaks: Extracted system ...</a></li>
<li><a href="https://arxiv.org/abs/2505.23817">System Prompt Extraction Attacks and Defenses in Large ... System Prompt Extraction - Learn LLM Security | chat.win How to Extract System Instructions from Any LLM (Yes, Even ... LLM-Penetration-Testing-KnowledgeBase/06-System-Prompt ... System Prompt Extraction — Definition, Examples & Prevention ... System Prompt Extraction Attacks and Defenses in Large ...</a></li>
<li><a href="https://learn.chat.win/exploit-prompts/system-prompt-extraction">System Prompt Extraction - Learn LLM Security | chat.win</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论凸显了对此漏洞的广泛担忧，许多用户分享了从流行 AI 助手中提取系统提示的个人经历。一些人就所提防御措施的有效性展开辩论，指出角色锚定和输出过滤可能被巧妙的措辞绕过。其他人则强调需要将提示分段和更严格的访问控制作为更稳健的解决方案。

**标签**: `#AI security`, `#prompt injection`, `#system prompt extraction`, `#LLM vulnerabilities`

---

<a id="item-14"></a>
## [Elixir 1.2 发布渐进式集合论类型系统](https://www.reddit.com/r/ProgrammingLanguages/comments/1umai41/what_does_it_take_to_add_settheoretic_types_to_a/) ⭐️ 8.0/10

Elixir 1.2 正在发布一个基于 Guillaume Dubois 博士工作的渐进式集合论类型系统，同时 Annette Bieniusa 也在为 Erlang 进行平行开发。该系统从一开始就将动态类型结构性地嵌入类型格中，并采用“先警告后拒绝”的设计。 这标志着在拥有数十年生产代码的动态语言上改造表达性类型系统的重大进展，有望提升 Elixir 和 Erlang 生态系统的可靠性和开发者体验。其设计选择，如动态类型的结构性嵌入和先警告后拒绝，为大型代码库的渐进式类型化提供了一条务实路径。 该类型系统基于集合论类型和渐进式类型化，将 dynamic() 视为一个范围类型的渐进类型。跨进程的消息类型化目前明确不在范围内，当前里程碑专注于类型推断，无需用户提供类型签名。

reddit · r/ProgrammingLanguages · /u/rtrusca · 7月3日 10:14

**背景**: 自 1995 年以来，Erlang 一直抵制静态类型化，Philip Wadler 的早期尝试也未能成功。集合论类型将类型视为值的集合，支持并集、交集和否定操作。渐进式类型化允许开发者在同一代码库中混合静态和动态类型。BEAM 虚拟机同时运行 Elixir 和 Erlang。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://elixir.hexdocs.pm/main/gradual-set-theoretic-types.html">Gradual set-theoretic types — Elixir v1.21.0-dev - HexDocs</a></li>
<li><a href="https://github.com/elixir-lang/elixir/blob/main/lib/elixir/pages/references/gradual-set-theoretic-types.md">elixir/lib/elixir/pages/references/gradual-set-theoretic ...</a></li>
<li><a href="https://src.acm.org/binaries/content/assets/src/2016/victorlanvin.pdf">Gradual Set-Theoretic Types</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论强调了为 Erlang 添加静态类型的历史困难，并赞扬了务实的设计选择。一些评论者将此方法与 TypeScript 等其他渐进式类型系统进行比较，指出了表达力和复杂性之间的权衡。

**标签**: `#type systems`, `#Elixir`, `#Erlang`, `#programming languages`, `#gradual typing`

---

<a id="item-15"></a>
## [阿里巴巴 Page-Agent：用自然语言控制网页](https://github.com/alibaba/page-agent) ⭐️ 8.0/10

阿里巴巴发布了 Page-Agent，这是一个开源的 TypeScript 库，作为页面内 GUI 代理，允许用户通过自然语言命令控制网页界面。 该项目通过自然语言与网页交互，简化了网页自动化，使非技术用户也能轻松操作，可能改变人们使用和自动化网页应用的方式。 Page-Agent 使用 TypeScript 编写，在 GitHub 上已获得超过 22,000 颗星，可通过单个脚本集成到任何网页中，并为外部代理提供函数调用接口。

ossinsight · GitHub Trending · 7月4日 03:27

**背景**: GUI 代理是能够像人类一样与图形用户界面交互的 AI 工具。Page-Agent 直接在浏览器中运行，无需修改服务器端即可轻松为现有网页应用添加智能自动化功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/alibaba/page-agent">GitHub - alibaba/page-agent: JavaScript in-page GUI agent ...</a></li>
<li><a href="https://alibaba.github.io/page-agent/">PageAgent - The GUI Agent Living in Your Webpage</a></li>
<li><a href="https://www.scriptbyai.com/web-page-agent/">Page Agent : Free & Open-source In - Page AI Browser Control</a></li>

</ul>
</details>

**标签**: `#GUI agent`, `#natural language`, `#web automation`, `#TypeScript`, `#open source`

---