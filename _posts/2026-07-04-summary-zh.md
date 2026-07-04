---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> 从 158 条内容中筛选出 15 条重要资讯。

---

1. [欧盟议会间谍软件调查员遭飞马间谍软件攻击](#item-1) ⭐️ 9.0/10
2. [Mistral 发布 Leanstral-1.5 用于形式验证](#item-2) ⭐️ 9.0/10
3. [Superpowers GitHub 仓库因智能体技能框架走红](#item-3) ⭐️ 8.0/10
4. [Agency-Agents：专业化 AI 智能体框架](#item-4) ⭐️ 8.0/10
5. [程序即权重：将自然语言编译为紧凑神经工件](#item-5) ⭐️ 8.0/10
6. [AgenticSTS：面向长周期 LLM 智能体的有界内存测试平台](#item-6) ⭐️ 8.0/10
7. [Wordgard：ProseMirror 创建者推出的新富文本编辑器](#item-7) ⭐️ 8.0/10
8. [PostgreSQL 与 OOM 杀手：为何严格内存过量使用至关重要](#item-8) ⭐️ 8.0/10
9. [开源 AI 差距图发布](#item-9) ⭐️ 8.0/10
10. [HAT-4D：单目视频生成 4D 交互场景](#item-10) ⭐️ 8.0/10
11. [DeepSeek V4 Flash MoE 在 RTX 5090 上运行，使用自定义 llama.cpp 分支](#item-11) ⭐️ 8.0/10
12. [CDD 无需权重访问即可从 LLM 对数中恢复微调数据](#item-12) ⭐️ 8.0/10
13. [系统提示提取攻击对 60-70%的 AI 智能体有效](#item-13) ⭐️ 8.0/10
14. [Elixir 1.2 引入渐进集合论类型系统](#item-14) ⭐️ 8.0/10
15. [OmniRoute：免费 AI 网关，支持 230 多家提供商](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [欧盟议会间谍软件调查员遭飞马间谍软件攻击](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 9.0/10

公民实验室发现，一名参与调查间谍软件的欧洲议会委员会成员在 2022 年 10 月和 2023 年 3 月两次被飞马间谍软件感染。 这表明一个拥有跨欧洲授权的国家行为者正在针对欧盟机构，破坏民主监督并引发严重的安全担忧。 这些感染与针对欧洲俄语和白俄罗斯语流亡记者的飞马间谍活动重叠，表明存在一个拥有多国间谍授权的单一客户。

hackernews · ledoge · 7月3日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马间谍软件由以色列 NSO 集团开发，仅出售给政府，能够零点击远程感染并完全控制设备。公民实验室是多伦多大学的一个研究小组，专门调查对人权的数字威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lzX2FQQ0VSR2FLSUx4NTNxVDB5Z0FQAQ?hl=en-GB&gl=GB&ceid=GB:en">Google News - News about spyware • EU • surveillance - Overview</a></li>

</ul>
</details>

**社区讨论**: 评论者指出调查员被监视的讽刺性，并提到希腊、波兰和意大利过去的飞马间谍软件滥用事件。有人质疑为什么欧盟议会不强制执行工作与个人设备分离的政策。

**标签**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#European Parliament`, `#surveillance`

---

<a id="item-2"></a>
## [Mistral 发布 Leanstral-1.5 用于形式验证](https://www.reddit.com/r/LocalLLaMA/comments/1umgdhx/mistral_released_leanstral15119ba6b/) ⭐️ 9.0/10

Mistral 发布了 Leanstral-1.5，这是一个拥有 6B 活跃参数的模型，采用 Apache-2.0 许可证，在 miniF2F、PutnamBench、FATE-H 和 FATE-X 等形式验证基准上取得了最先进的结果，并在 57 个代码仓库中发现了 5 个真实漏洞。 此次发布标志着自动定理证明和形式验证领域的重大进步，使开发者更容易验证软件正确性并捕捉传统测试可能遗漏的细微漏洞，开源许可证鼓励广泛采用。 该模型通过中期训练、监督微调和基于 CISPO（裁剪重要性采样策略优化）的强化学习进行训练，在 miniF2F 基准上达到饱和，解决了 672 个 PutnamBench 问题中的 587 个，并在 FATE-H 上达到 87%，在 FATE-X 上达到 34%。

reddit · r/LocalLLaMA · /u/Tall-Ad-7742 · 7月3日 14:44

**背景**: 形式验证使用数学证明来确保软件正确性，而自动定理证明旨在自动生成这些证明。miniF2F 和 PutnamBench 等基准测试评估模型在 Lean 4 等系统中形式化的竞赛级数学问题上的表现。CISPO 是一种强化学习算法，通过裁剪重要性采样权重来提高稳定性和样本效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/miniF2F">GitHub - openai/miniF2F: Formal to Formal Mathematics Benchmark</a></li>
<li><a href="https://github.com/trishullab/PutnamBench">GitHub - trishullab/PutnamBench: An evaluation benchmark for undergraduate competition math in Lean4, Isabelle, Coq, and natural language. · GitHub</a></li>
<li><a href="https://www.emergentmind.com/topics/cispo-algorithm">CISPO: Clipped Importance Sampling RL - emergentmind.com</a></li>

</ul>
</details>

**社区讨论**: 一些评论者对声称该漏洞会被测试遗漏表示质疑，指出那只是一个简单的溢出边界情况。其他人指出该模型与半年前的旧模型进行比较，觉得这很有趣。还有人对为什么选择 Lean 4 而非 Isabelle/HOL 等其他形式验证工具表示好奇。

**标签**: `#AI`, `#formal verification`, `#Mistral`, `#theorem proving`, `#open-source`

---

<a id="item-3"></a>
## [Superpowers GitHub 仓库因智能体技能框架走红](https://github.com/obra/superpowers) ⭐️ 8.0/10

GitHub 仓库 obra/superpowers 单日获得超过 1200 颗星，总星数接近 246,000，该仓库为编码智能体引入了一个智能体技能框架和软件开发方法论。 该方法论将 AI 编码助手从简单的代码编写工具转变为纪律严明的工程伙伴，有望提升整个行业的软件开发效率和质量。 Superpowers 是一个零依赖插件，提供可组合的技能和初始指令来指导编码智能体，由 Prime Radiant 的 Jesse Vincent（@obra）构建。

github_trending · GitHub Trending · 7月4日 03:16

**背景**: 智能体技能框架允许 AI 智能体按需发现和加载可移植的指令、脚本和资源包。该仓库将此概念应用于软件开发，为编码智能体提供了一套完整的方法论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/obra/superpowers">GitHub - obra / superpowers : An agentic skills framework & software ...</a></li>
<li><a href="https://zread.ai/obra/superpowers">Overview | obra / superpowers | Zread</a></li>
<li><a href="https://ai-trove.com/en/superpowers">Superpowers — agentic skills framework & software</a></li>

</ul>
</details>

**标签**: `#software-development`, `#methodology`, `#github-trending`, `#shell`

---

<a id="item-4"></a>
## [Agency-Agents：专业化 AI 智能体框架](https://github.com/msitarzewski/agency-agents) ⭐️ 8.0/10

GitHub 仓库 msitarzewski/agency-agents 单日获得超过 1208 颗星，总星数达 126,558，该框架用于创建具有不同角色和交付成果的专业化 AI 智能体。 该框架使开发者能够构建模块化的 AI 智能体系统，每个智能体拥有独特的个性和流程，可能简化复杂的多智能体工作流，并吸引了社区的强烈关注。 该仓库使用 Shell 编写，拥有 20,539 个分支；它将智能体描述为“前端巫师”、“Reddit 社区忍者”和“奇思妙想注入者”，强调专业化能力。

github_trending · GitHub Trending · 7月4日 03:16

**背景**: AI 智能体框架为开发和自主管理 AI 智能体提供了基础组件。多智能体系统为智能体分配不同角色，模拟人类团队结构以协作处理复杂任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/agent-framework/overview/">Microsoft Agent Framework Overview | Microsoft Learn</a></li>
<li><a href="https://www.ibm.com/think/insights/top-ai-agent-frameworks">AI Agent Frameworks: Choosing the Right Foundation for Your Business | IBM</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#framework`, `#Shell`, `#open source`, `#tooling`

---

<a id="item-5"></a>
## [程序即权重：将自然语言编译为紧凑神经工件](https://huggingface.co/papers/2607.02512) ⭐️ 8.0/10

研究人员提出“程序即权重”（PAW）范式，使用 4B 编译器将自然语言规范编译为紧凑神经工件，并由 0.6B 解释器执行，性能媲美 32B 模型，但推理内存仅为其 1/50，在 MacBook M3 上可达 30 tokens/s。 该工作将大型基础模型从每次输入的问题求解器重新定位为工具构建者，使得模糊函数（如日志告警、JSON 修复）能够高效本地执行，无需昂贵的 API 调用。它大幅降低了资源需求，使先进 NLP 能力可在边缘设备上使用。 PAW 编译器在作者发布的包含 1000 万样本的新数据集 FuzzyBench 上训练。解释器是冻结的 0.6B Qwen3 模型，执行编译器生成的参数高效适配器，性能与直接提示 Qwen3-32B 相当。

huggingface_papers · Hugging Face Papers · 7月3日 00:00

**背景**: 许多编程任务（如日志行告警或搜索结果排序）难以用显式规则实现，常被外包给大型语言模型 API，这会引入延迟、成本和可重复性问题。参数高效适配器（如 LoRA）允许在不修改基础模型的情况下，针对特定任务微调少量模型参数。PAW 结合了这些思想，使用编译器从自然语言生成适配器，从而实现高效的本地执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://weightagnostic.github.io/">Weight Agnostic Neural Networks</a></li>
<li><a href="https://arxiv.org/abs/1902.00751">[1902.00751] Parameter-Efficient Transfer Learning for NLP GitHub - adapter-hub/adapters: A Unified Library for ... Awesome Adapter Resources - Clifton Poth LoRA & PEFT Fine-Tuning: Production Guide for 2026 - TheCodeForge ELP-Adapters: Parameter Efficient Adapter Tuning for Various ...</a></li>

</ul>
</details>

**标签**: `#programming paradigms`, `#neural networks`, `#natural language processing`, `#efficient inference`, `#fuzzy functions`

---

<a id="item-6"></a>
## [AgenticSTS：面向长周期 LLM 智能体的有界内存测试平台](https://huggingface.co/papers/2607.02255) ⭐️ 8.0/10

研究人员提出了 AgenticSTS，这是一个面向长周期 LLM 智能体的有界内存测试平台，通过类型化检索组装全新提示，实现对内存组件的独立消融。在《杀戮尖塔 2》中，该设计取得了胜利，而基于公开转录的智能体得分为零。 这项工作解决了长周期智能体系统中的关键挑战：隔离单个内存组件的影响。有界契约方法有望为复杂决策任务带来更可解释、更高效的 LLM 智能体。 有界契约确保每个决策都使用通过类型化检索组装的新提示，不附加原始跨决策记录。在《杀戮尖塔 2》中，添加战略技能层将胜率从 3/10 提升至 6/10，但该比较仅为方向性（Fisher 精确检验 p≈0.37）。

huggingface_papers · Hugging Face Papers · 7月3日 00:00

**背景**: 长周期 LLM 智能体需要内存来跨多个决策持久化信息。最简单的方法是将所有历史附加到每个提示中，但这会创建混乱的上下文，使得难以研究单个内存组件。AgenticSTS 引入了一种有界契约，每个决策仅看到通过类型化检索组装的新提示，保持提示大小恒定，并支持干净的消融研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.02255">[2607.02255] AgenticSTS: A Bounded-Memory Testbed for Long ...</a></li>
<li><a href="https://github.com/AlayaLab/AgenticSTS">GitHub - AlayaLab/AgenticSTS: Bounded, typed, ablatable ...</a></li>
<li><a href="https://huggingface.co/papers/2607.02255">Paper page - AgenticSTS: A Bounded-Memory Testbed for Long ...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#memory`, `#long-horizon`, `#testbed`, `#decision-making`

---

<a id="item-7"></a>
## [Wordgard：ProseMirror 创建者推出的新富文本编辑器](https://wordgard.net/) ⭐️ 8.0/10

ProseMirror 的创建者发布了 Wordgard 0.1.0，这是一款新的浏览器内富文本编辑器。它与 ProseMirror 共享许多概念，但并非直接升级路径。 此次发布意义重大，因为它来自富文本编辑领域备受尊敬的创建者，社区反响热烈，获得了 273 个点赞和 90 条评论。它可能会影响基于 Web 的所见即所得编辑器的未来。 Wordgard 并非 ProseMirror 的直接升级版本；迁移需要大量工作。该编辑器设计轻量且易于使用，注重简洁性。

hackernews · indy · 7月3日 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48772573)

**背景**: ProseMirror 是一个流行的开源工具包，用于在浏览器中构建富文本编辑器，广泛应用于 TipTap 等应用中。Wordgard 是同一领域的新系统，旨在以全新方法简化内容编辑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://discuss.prosemirror.net/t/wordgard-0-1-0/9035">Wordgard 0.1.0 - Announce - discuss.ProseMirror</a></li>
<li><a href="https://digitechbytes.com/digital-lifestyle-productivity/wordgard-in-browser-rich-text-editor-from-the-creator-of-prosemirror/">Wordgard: In-browser Rich-text Editor From The Creator Of ...</a></li>

</ul>
</details>

**社区讨论**: 社区对 Wordgard 背后的“原因”感到好奇，并指出从 ProseMirror 没有升级路径。一些用户看到与自己工作的相似之处感到被认可，而另一些用户则强调 ProseMirror 缺乏静态类型模式是一个痛点。

**标签**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#open source`, `#WYSIWYG`

---

<a id="item-8"></a>
## [PostgreSQL 与 OOM 杀手：为何严格内存过量使用至关重要](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.0/10

Ubicloud 发布了一篇博客文章，解释了他们为何对 PostgreSQL 使用严格内存过量使用（vm.overcommit_memory=2）以防止 Linux OOM 杀手终止数据库进程，并分享了他们因内核 bug 而暂时禁用该设置的经验。 这很重要，因为 PostgreSQL 对内存压力敏感，而 Linux 默认的过量使用行为可能导致灾难性的 OOM 杀死，使数据库崩溃。该文章为寻求更可预测和稳定生产部署的数据库管理员提供了实用指导。 严格过量使用（模式 2）完全禁用内存过量使用，因此如果内存不可用，malloc() 返回 NULL，从而阻止 OOM 杀手激活。然而，如果过量使用比例配置不当，模式 2 可能导致 fork() 失败，文章还提到一个三个字符的内核 bug 迫使他们暂时恢复默认设置。

hackernews · furkansahin · 7月3日 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48774509)

**背景**: Linux 默认使用内存过量使用（模式 0 - 启发式），允许进程分配比物理 RAM + 交换空间更多的虚拟内存，假设并非所有内存会同时使用。当系统内存耗尽时，OOM 杀手会选择并终止一个进程以释放内存，这可能会杀死关键的 PostgreSQL 进程。严格过量使用（模式 2）确保仅在内存实际可用时分配成功，避免 OOM 杀死，但存在分配失败的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit">PostgreSQL and the OOM Killer: Why We Use Strict Memory ...</a></li>
<li><a href="https://www.kernel.org/doc/Documentation/vm/overcommit-accounting">The Linux kernel supports the following overcommit handling modes</a></li>
<li><a href="https://www.cybertec-postgresql.com/en/what-you-should-know-about-linux-memory-overcommit-in-postgresql/">Memory overcommit and PostgreSQL - CYBERTEC</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了权衡：一些人指出 Linux 默认设置在内存压力下存在问题，而另一些人则警告模式 2 可能破坏依赖 fork() 或分配大量虚拟内存（例如 Go 程序）的应用程序。来自 Ubicloud 的一位评论者承认文章语气强烈，并强调严格过量使用在许多场景下可能产生未预料的副作用。

**标签**: `#PostgreSQL`, `#Linux`, `#memory management`, `#OOM killer`, `#database administration`

---

<a id="item-9"></a>
## [开源 AI 差距图发布](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI（一家于 2025 年 2 月成立的非营利组织）发布了开源 AI 差距图 v0.1，索引了 AI 堆栈中的 421 个产品，以识别差距和机会。 该图提供了开源 AI 生态系统的结构化概览，帮助开发者、投资者和政策制定者了解应聚焦于何处以及如何投入资金。 该图涵盖了来自 228 个组织的 266 个软件工具、85 个模型、50 个数据集和 20 个硬件项目，底层数据以 MIT 许可证发布在 GitHub 上。

rss · Simon Willison · 7月3日 22:04

**背景**: Current AI 是一个致力于构建 AI 公共选项的全球合作伙伴关系，已获得 4 亿美元承诺资金。差距图基于哥伦比亚会议、MOF、Hugging Face 等机构的工作，绘制开源 AI 堆栈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map - simonwillison.net</a></li>
<li><a href="https://map.currentai.org/">Current AI – Open Source AI Gap Map</a></li>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1 - currentai.org</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI`, `#ecosystem`, `#mapping`, `#non-profit`

---

<a id="item-10"></a>
## [HAT-4D：单目视频生成 4D 交互场景](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247901356&idx=3&sn=54ee94026f76691a380cd3ea214e0def) ⭐️ 8.0/10

上海交通大学等机构提出 HAT-4D 方法，能够直接从单目视频生成 4D 交互场景，无需昂贵的多摄像头动捕系统。 这一突破可能通过用单台消费级摄像头取代百万级动捕棚，为 VR/AR、游戏和电影制作中的 4D 内容创作带来民主化，大幅降低成本和准入门槛。 HAT-4D 从单目视频重建具有时间一致性的动态 3D 场景，支持交互式视角控制和场景编辑。该方法可能基于高斯泼溅或神经辐射场等 4D 重建领域的最新进展。

rss · 量子位 · 7月3日 03:43

**背景**: 传统的 4D（动态 3D）场景捕捉需要多摄像头阵列或昂贵的动捕服，成本高达数百万。近期如 CAT4D 和 Vivid4D 等研究已探索了从单目视频到 4D 重建，但 HAT-4D 专门针对交互式场景理解和操控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2504.11092">Vivid4D: Improving 4D Reconstruction from Monocular Video by ...</a></li>
<li><a href="https://arxiv.org/abs/2601.18993">[2601.18993] FreeOrbit4D: Training-Free Arbitrary Camera ... 4D-Fly: Fast 4D Reconstruction from a Single Monocular Video CAT4D: Create Anything in 4D with Multi-View Video Diffusion ... Vivid4D: Improving 4D Reconstruction from Monocular Video by ... GitHub - VVeiCao/FreeOrbit4D: [SIGGRAPH 2026 Conference ...</a></li>

</ul>
</details>

**标签**: `#4D reconstruction`, `#computer vision`, `#AI`, `#motion capture`, `#scene understanding`

---

<a id="item-11"></a>
## [DeepSeek V4 Flash MoE 在 RTX 5090 上运行，使用自定义 llama.cpp 分支](https://www.reddit.com/r/LocalLLaMA/comments/1umsik8/deepseek_v4_flash_running_on_rtx_5090_moe/) ⭐️ 8.0/10

一位 Reddit 用户使用自定义的 llama.cpp 分支，在 RTX 5090 上成功运行了 284B 参数的 MoE 模型 DeepSeek V4 Flash，实现了 21.3 TG T/s 和 927 PP T/s 的性能，并支持高达 100 万 token 的上下文。 这表明像 DeepSeek V4 Flash 这样的大型 MoE 模型可以在消费级硬件上本地运行，实现快速、私密的 AI 推理，无需云 API，凸显了本地 LLM 部署能力的提升。 该设置使用了 Q2_K 量化的 GGUF 模型、支持 CUDA 的自定义 llama.cpp 分支，以及 --n-cpu-moe 37 参数将专家层卸载到 CPU，从而在 512 ub 下适配了 100 万上下文。构建目标为 CUDA 架构 120（Blackwell）。

reddit · r/LocalLLaMA · /u/H_DANILO · 7月3日 22:48

**背景**: DeepSeek V4 Flash 是一个 284B 参数的混合专家（MoE）模型，激活参数为 13B，支持 100 万 token 上下文窗口，针对快速编码和智能体任务进行了优化。RTX 5090 是 NVIDIA 基于 Blackwell 架构的最新消费级 GPU。llama.cpp 是一个用于本地运行 LLM 的开源 C++ 实现，而自定义分支增加了对 DeepSeek V4 架构的支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://build.nvidia.com/deepseek-ai/deepseek-v4-flash">deepseek - v 4 - flash Model by Deepseek -ai | NVIDIA NIM</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V 4 Flash - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 社区称赞了这一成就，后续基准测试显示，DeepSeek V4 Flash 在 vLLM 上达到了 Sonnet 级别的质量，并且实际运行时间比基于 API 的模型更快。用户指出，本地模型现在具有竞争力，尤其是在避免密集注意力时，而 Opus 和 Fable 在质量上仍然领先。

**标签**: `#DeepSeek`, `#RTX 5090`, `#MoE`, `#llama.cpp`, `#benchmark`

---

<a id="item-12"></a>
## [CDD 无需权重访问即可从 LLM 对数中恢复微调数据](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

研究人员提出了对比解码差分（CDD），这是一种灰盒方法，通过对比基模型和微调模型的对数来从大语言模型中逐字恢复微调数据，无需权重访问即可获得高恢复分数。 CDD 解决了大语言模型中的一个关键隐私和安全问题，它表明仅通过对数访问（比权重更容易获取）就能提取微调数据，可能暴露微调中使用的敏感信息。 在 SDF 基准测试中，CDD 在四个模型家族（1B 到 32B 参数）的 20 个生物-模型对中的 19 个上实现了 4+/5 的逐字恢复分数，优于白盒方法 Activation Difference Lens (ADL)，后者从未超过 3/5。

reddit · r/MachineLearning · /u/CebulkaZapiekana · 7月3日 19:01

**背景**: 模型差分旨在识别基模型与其微调版本之间的差异。先前的工作 Activation Difference Lens (ADL) 需要完全权重访问，且只能恢复模糊的领域级描述。CDD 在输出层操作，仅使用对数分布，使其成为一种更实用的灰盒方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/papers/2605.25902">CDD: Verbatim Content Recovery via Diffing</a></li>
<li><a href="https://www.machinebrief.com/news/unlocking-ais-hidden-memories-with-contrastive-decoding-9a3m">Unlocking AI's Hidden Memories with Contrastive Decoding</a></li>
<li><a href="https://arxiv.org/html/2510.13900">Narrow Finetuning Leaves Clearly Readable Traces in Activation ...</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论强调了该方法的创新性和隐私影响，一些评论者注意到一个令人惊讶的发现：一个虚构人物“Dr. Elena Rodriguez”在无关的微调领域中反复出现，表明合成数据生成中存在偏差。其他人则讨论了实际威胁程度和潜在的防御措施。

**标签**: `#LLM`, `#model diffing`, `#privacy`, `#finetuning`, `#security`

---

<a id="item-13"></a>
## [系统提示提取攻击对 60-70%的 AI 智能体有效](https://www.reddit.com/r/artificial/comments/1ums1ou/repeat_the_text_above_this_line_still_works_on/) ⭐️ 8.0/10

一种简单的提示注入攻击，例如要求“重复此行上方的文本”，可以从 60-70%已部署的 AI 智能体中提取完整的系统提示，暴露防护措施、工具配置和 API 密钥。 这一漏洞构成严重安全风险，因为泄露的系统提示为攻击者提供了绕过防护、访问内部工具和利用业务逻辑的路线图，影响无数生产环境中的 AI 系统。 该攻击通过直接命令、翻译技巧、编码请求、角色扮演和多轮对话等方式生效；有效的防御措施包括角色锚定、输出过滤、提示分段和元指令感知。

reddit · r/artificial · /u/Still_Piglet9217 · 7月3日 22:27

**背景**: 系统提示提取是一种提示注入攻击，攻击者诱使 LLM 泄露其隐藏的系统指令。这些指令定义了模型的行为、工具访问权限和安全规则。该攻击利用了模型无法区分开发者定义的提示和用户输入这一根本性挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2505.23817">System Prompt Extraction Attacks and Defenses in Large Language...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://wraith.sh/learn/system-prompt-extraction-guide">System Prompt Extraction : Techniques and Defenses | Wraith</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论基本验证了这些发现，许多用户分享了类似经历，并强调需要更好的防御措施。一些评论者指出，该攻击执行起来非常简单，尽管已知风险，许多生产环境中的智能体仍然脆弱。

**标签**: `#AI security`, `#prompt injection`, `#system prompt extraction`, `#LLM vulnerabilities`, `#red teaming`

---

<a id="item-14"></a>
## [Elixir 1.2 引入渐进集合论类型系统](https://www.reddit.com/r/ProgrammingLanguages/comments/1umai41/what_does_it_take_to_add_settheoretic_types_to_a/) ⭐️ 8.0/10

Elixir 1.2 发布了一个基于 Guillaume Dubois 在巴黎 IRIF 的博士工作的渐进集合论类型系统，同时德国 RPTU 的 Annette Bieniusa 正在基于相同基础为 Erlang 构建一个并行类型检查器。 这标志着一项重大技术成就：在拥有 30 年生产代码的动态语言上改造出一个富有表现力的类型系统，此前数十年间包括 Philip Wadler 在 1995 年的尝试均以失败告终。 动态类型从一开始就被结构性地嵌入集合论格中，系统在拒绝代码之前会发出警告；跨进程的消息类型化目前明确不在范围内。

reddit · r/ProgrammingLanguages · /u/rtrusca · 7月3日 10:14

**背景**: 渐进类型允许在同一语言中混合静态和动态类型。集合论类型使用集合运算（并集、交集、否定）来描述类型，从而能够精确建模动态模式。Elixir 运行在 Erlang 虚拟机（BEAM）上，该虚拟机历来抵制静态类型化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gradual_typing">Gradual typing</a></li>
<li><a href="https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/">Elixir v1.20 released: now a gradually typed language</a></li>
<li><a href="https://www.reddit.com/r/programming/comments/1twg7mu/elixir_v120_released_now_a_gradually_typed/">Elixir v1.20 released: now a gradually typed language : r/programming - Reddit</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论强调了在动态语言上改造类型系统的难度，并将 Elixir 的方法与 TypeScript 和 Hack 等其他渐进类型化努力进行了比较。一些评论者对集合论类型在大型代码库中的实用性表示怀疑。

**标签**: `#type systems`, `#Elixir`, `#Erlang`, `#gradual typing`, `#programming languages`

---

<a id="item-15"></a>
## [OmniRoute：免费 AI 网关，支持 230 多家提供商](https://github.com/diegosouzapw/OmniRoute) ⭐️ 8.0/10

OmniRoute 是一个用 TypeScript 编写的免费开源 AI 网关，现在提供单一端点，可访问超过 230 家 AI 提供商（包括 50 多个免费层），并具备令牌压缩和智能自动回退功能。 该项目通过将众多提供商统一到一个 API 后面，简化了 AI 集成，通过令牌压缩降低成本，并通过自动回退确保可靠性，这对构建 AI 驱动应用的开发者非常有价值。 OmniRoute 使用 RTK（Rust Token Killer）和 Caveman 堆叠压缩，可节省 15-95%的令牌，支持 MCP 和 A2A 协议、多模态 API，并可作为桌面应用或 PWA 使用。

ossinsight · GitHub Trending · 7月4日 03:16

**背景**: AI 网关是位于应用程序和 AI 服务提供商之间的中间件，管理 API 调用、路由、安全和监控。像 RTK 和 Caveman 这样的令牌压缩技术减少了发送给 LLM 的令牌数量，从而降低成本。MCP（模型上下文协议）和 A2A（代理间协议）是用于代理互操作性的新兴协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/sonim1/token-saving-and-caveman-e1f">Token Saving, and Caveman - DEV Community</a></li>
<li><a href="https://a2a-protocol.org/latest/">A 2 A Protocol</a></li>
<li><a href="https://vercel.com/ai-gateway">AI Gateway – Vercel</a></li>

</ul>
</details>

**标签**: `#AI Gateway`, `#TypeScript`, `#Open Source`, `#API`, `#Token Compression`

---