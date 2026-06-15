---
layout: default
title: "Horizon Summary: 2026-06-15 (ZH)"
date: 2026-06-15
lang: zh
---

> 从 138 条内容中筛选出 15 条重要资讯。

---

1. [NVIDIA SkillSpector：AI 代理技能安全扫描器](#item-1) ⭐️ 8.0/10
2. [LMCache：最快的 LLM 推理 KV 缓存层](#item-2) ⭐️ 8.0/10
3. [EvoArena 与 EvoMem：面向动态环境的 LLM 智能体基准与记忆范式](#item-3) ⭐️ 8.0/10
4. [MiniMax 稀疏注意力提升长上下文 LLM 效率](#item-4) ⭐️ 8.0/10
5. [Yserver：用 Rust 编写的现代 X11 服务器](#item-5) ⭐️ 8.0/10
6. [大西洋冷斑暗示 AMOC 崩溃风险](#item-6) ⭐️ 8.0/10
7. [不要轻信大上下文窗口](#item-7) ⭐️ 8.0/10
8. [为什么 AI 还没有取代软件工程师，而且不会](#item-8) ⭐️ 8.0/10
9. [进入 AI 治理的 AGI 时代](#item-9) ⭐️ 8.0/10
10. [OpenAI 推出合作伙伴网络，投资 1.5 亿美元](#item-10) ⭐️ 8.0/10
11. [小米 MiMo V2.5 借助 DFlash 和持久化内核实现 1000-3000 tps](#item-11) ⭐️ 8.0/10
12. [EAGLE 推测解码已合并到 llama.cpp](#item-12) ⭐️ 8.0/10
13. [基于 Qwen3.5-397B 的实时本地语音聊天机器人](#item-13) ⭐️ 8.0/10
14. [在 M3 Max Mac 上通过 SSD 流式运行 DeepSeek V4 Flash](#item-14) ⭐️ 8.0/10
15. [双 DGX Spark 运行 DeepSeek V4 Flash 达到 350 tk/s](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [NVIDIA SkillSpector：AI 代理技能安全扫描器](https://github.com/NVIDIA/SkillSpector) ⭐️ 8.0/10

NVIDIA 发布了 SkillSpector，这是一个用于 AI 代理技能的开源安全扫描器，能够检测漏洞、恶意模式和安全风险。该工具现已在 GitHub 上可用，并在一天内获得了超过 964 颗星。 随着 AI 代理变得越来越自主，保护其技能对于防止提示注入和数据泄露等攻击至关重要。SkillSpector 填补了 AI 安全生态中的关键空白，尤其是在 NVIDIA 的支持下，并集成到其验证技能流程中。 SkillSpector 使用 Python 编写，对代理技能定义进行静态分析，检测超过 25 种威胁类型，包括命令注入、凭证盗窃和供应链风险。NVIDIA 将其作为发布验证流程的一部分，在技能进入 NVIDIA Skills 目录之前使用。

github_trending · GitHub Trending · 6月15日 01:01

**背景**: AI 代理技能是扩展代理功能的模块化能力，通常定义为提示或脚本。然而，这些技能可能包含恶意代码或漏洞，从而危及代理的安全。SkillSpector 通过在安装前扫描技能来解决这一问题，类似于杀毒软件扫描文件的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/nvidia/skillspector">GitHub - NVIDIA/SkillSpector: Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, and security risks. · GitHub</a></li>
<li><a href="https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/">NVIDIA-Verified Agent Skills Provide Capability Governance for AI Agents | NVIDIA Technical Blog</a></li>
<li><a href="https://docs.nvidia.com/skills/scanning-agent-skills">Scan Agent Skills Before Installation | NVIDIA Skill Documentation</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Vulnerability Detection`, `#Python`, `#AI Agents`, `#NVIDIA`

---

<a id="item-2"></a>
## [LMCache：最快的 LLM 推理 KV 缓存层](https://github.com/LMCache/LMCache) ⭐️ 8.0/10

LMCache，一个用于 LLM 的高性能 KV 缓存层，今日在 GitHub 上获得 248 颗星，总星数达到 9048 颗，凸显了其通过减少内存开销来加速 LLM 推理的日益受欢迎。 KV 缓存是 LLM 推理中的关键瓶颈，LMCache 的优化缓存层可以显著降低延迟和内存使用，从而在生产环境中实现更快、更具成本效益的大语言模型部署。 LMCache 使用 Python 编写，支持与流行的 LLM 框架集成；它通过高效存储和重用键值计算来减少推理期间的内存开销。

github_trending · GitHub Trending · 6月15日 01:02

**背景**: 在 LLM 推理中，键值（KV）缓存存储中间注意力计算以避免冗余计算，这对于高效的自回归生成至关重要。然而，KV 缓存可能会变得很大，消耗大量 GPU 内存。LMCache 通过提供一个快速、内存高效的缓存层来解决这个问题，该层可以插入到现有的 LLM 服务系统中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/lmcache/lmcache">GitHub - LMCache/LMCache: LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub</a></li>
<li><a href="https://lmcache.ai/">LMCache</a></li>

</ul>
</details>

**标签**: `#LLM`, `#KV Cache`, `#Inference Optimization`, `#Python`, `#Machine Learning`

---

<a id="item-3"></a>
## [EvoArena 与 EvoMem：面向动态环境的 LLM 智能体基准与记忆范式](https://huggingface.co/papers/2606.13681) ⭐️ 8.0/10

研究人员提出了 EvoArena 基准测试套件，该套件模拟终端、软件和社交领域的渐进式环境变化，并提出了 EvoMem，一种基于补丁的记忆范式，通过记录结构化的更新历史帮助 LLM 智能体推理环境演变。 当前 LLM 智能体在动态环境中表现不佳，在 EvoArena 上平均准确率仅为 39.6%；EvoMem 在 EvoArena 上提升了 1.5%的性能，并在 GAIA 和 LoCoMo 等标准基准上分别提升了 6.1%和 4.8%，凸显了评估和记忆中对演变的关注。 EvoMem 是一种基于补丁的记忆范式，将记忆存储为结构化的更新历史，使智能体能够通过记忆演变推理环境变化。在 EvoArena 上，它还将链级准确率提升了 3.7%，链级任务要求完成一系列连续相关的子任务。

huggingface_papers · Hugging Face Papers · 6月12日 00:00

**背景**: 大多数 LLM 智能体基准测试假设环境是静态的，但实际部署是动态的，要求智能体适应不断变化的条件。EvoArena 通过跨领域建模渐进式更新填补了这一空白。EvoMem 引入了一种结构化记忆方法，跟踪环境如何演变，不同于传统的扁平记忆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/papers/2606.13681">EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic ...</a></li>
<li><a href="https://arxiv.org/html/2606.13681">EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic ...</a></li>
<li><a href="https://arxiv.org/pdf/2606.13681">EvoArena: Tracking Memory Evolution for Robust LLM Agents in...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#benchmark`, `#memory evolution`, `#dynamic environments`, `#AI research`

---

<a id="item-4"></a>
## [MiniMax 稀疏注意力提升长上下文 LLM 效率](https://huggingface.co/papers/2606.13392) ⭐️ 8.0/10

MiniMax 发布了一种名为 MiniMax 稀疏注意力（MSA）的新型稀疏注意力机制，它利用块级稀疏性和优化的 GPU 内核，在 H800 GPU 上为 109B 参数的多模态模型在 1M 上下文长度下实现了 14.2 倍的预填充和 7.6 倍的解码加速。 超长上下文能力对于智能体工作流和代码推理至关重要，但二次注意力成本限制了部署。MSA 提供了一种实用的、与硬件对齐的解决方案，在保持模型质量的同时显著减少计算量，从而实现更高效的长上下文 LLM 推理。 MSA 基于分组查询注意力（GQA）构建，包含一个轻量级索引分支，为每组选择 Top-k 键值块，以及一个主分支执行精确的块稀疏注意力。协同设计的 GPU 内核使用无指数 Top-k 选择和 KV 外稀疏注意力来提高张量核心利用率。

huggingface_papers · Hugging Face Papers · 6月12日 00:00

**背景**: 标准 softmax 注意力在序列长度上具有二次复杂度，使得它对于非常长的上下文不可行。稀疏注意力方法通过仅关注一部分 token 来降低这一成本。分组查询注意力（GQA）将查询头分组以减少内存和计算，而块级稀疏注意力通过对 token 块进行操作进一步提高效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.13392">[2606.13392] MiniMax Sparse Attention</a></li>
<li><a href="https://friendli.ai/blog/gqa-vs-mha">Grouped Query Attention ( GQA ) vs. Multi Head Attention ...</a></li>
<li><a href="https://www.emergentmind.com/topics/blockwise-sparse-attention-mechanisms">Blockwise Sparse Attention Mechanisms</a></li>

</ul>
</details>

**标签**: `#attention mechanism`, `#LLM`, `#efficiency`, `#sparse attention`, `#long context`

---

<a id="item-5"></a>
## [Yserver：用 Rust 编写的现代 X11 服务器](https://github.com/joske/yserver) ⭐️ 8.0/10

Yserver 是一个用 Rust 编写的新型 X11 服务器，已经能够运行像 XFCE4 这样的真实窗口管理器，但缺少多屏幕支持和合成器兼容性。 该项目表明，构建一个现代、内存安全的 X11 服务器是可行的，有望提升 Linux 桌面的安全性和性能。它也重新激发了人们对 Wayland 之外的 X11 替代方案的兴趣。 Yserver 放弃了多屏幕等遗留负担，一些用户批评这对多显示器设置至关重要。目前它在禁用合成时能与 XFCE4 配合使用，但无法与 LightDM 正常工作。

hackernews · Venn1 · 6月14日 19:10 · [社区讨论](https://news.ycombinator.com/item?id=48531394)

**背景**: X Window System (X11) 是类 Unix 操作系统的窗口系统，最初于 1984 年发布。参考实现 X.Org Server 用 C 语言编写，积累了数十年的遗留代码。Rust 是一种现代系统编程语言，强调内存安全和并发性，无需垃圾回收器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/X11_server">X11 server</a></li>
<li><a href="https://en.wikipedia.org/wiki/X_Window_System">X Window System - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust ( programming language ) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Yserver 能运行真实窗口管理器印象深刻，但许多人对其缺乏多屏幕支持表示担忧，认为这是必需的。一些人提到了历史上的 Y Window System，并指出 Yserver 的时机具有讽刺意味，因为它在 Wayland 已经占据主导地位后才出现。

**标签**: `#Rust`, `#X11`, `#Linux Desktop`, `#Window System`

---

<a id="item-6"></a>
## [大西洋冷斑暗示 AMOC 崩溃风险](https://www.cnn.com/2026/06/12/climate/cold-blob-atlantic-amoc-ocean-circulation) ⭐️ 8.0/10

研究人员在格陵兰岛和冰岛以南的北大西洋发现了一个持续的冷斑，他们认为这是由于大西洋经向翻转环流（AMOC）减弱所致。这一发现表明 AMOC 可能正接近一个关键的临界点。 AMOC 崩溃将引发严重的气候影响，包括欧洲大幅降温、亚马逊雨林降雨模式紊乱以及全球变暖加速。这凸显了应对气候变化以避免跨越不可逆临界点的紧迫性。 冷斑是由格陵兰冰盖融化的淡水干扰了驱动 AMOC 的稠密咸水下沉所致。2024 年《科学进展》的一项研究发现，AMOC 崩溃可能导致亚马逊的旱季和雨季发生逆转。

hackernews · tambourine_man · 6月14日 14:40 · [社区讨论](https://news.ycombinator.com/item?id=48527658)

**背景**: 大西洋经向翻转环流（AMOC）是一个主要的洋流系统，它将温暖的海水向北输送，将寒冷的海水向南输送，在调节全球气候中起着关键作用。临界点是一个关键阈值，超过该阈值系统会发生大规模、通常不可逆的变化。过去 AMOC 的关闭曾发生在末次冰期，原因是冰盖融化导致淡水涌入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Atlantic_meridional_overturning_circulation">Atlantic meridional overturning circulation - Wikipedia</a></li>
<li><a href="https://interactive.carbonbrief.org/amoc-explainer/index.html">AMOC: Is global warming tipping key Atlantic ocean currents towards ‘collapse’?</a></li>
<li><a href="https://climate.mit.edu/ask-mit/what-would-happen-if-atlantic-meridional-overturning-circulation-amoc-collapses-how-likely">What would happen if the Atlantic Meridional Overturning Circulation (AMOC) collapses? How likely is it? | MIT Climate Portal</a></li>

</ul>
</details>

**社区讨论**: 评论者对气候变化的缓慢应对表示担忧，有些人将其与科幻小说中的情景相提并论。其他人指出，冷斑的位置与早期关于 AMOC 减弱的预测相符，并就阻止最坏结果是否为时已晚展开了辩论。

**标签**: `#climate change`, `#AMOC`, `#ocean circulation`, `#global warming`, `#tipping point`

---

<a id="item-7"></a>
## [不要轻信大上下文窗口](https://garrit.xyz/posts/2026-05-06-dont-trust-large-context-windows) ⭐️ 8.0/10

一篇博客文章指出，LLM 的大上下文窗口会降低性能和可靠性，并呼吁不要轻信供应商的宣传。 这很重要，因为许多用户依赖大上下文窗口处理复杂任务，而性能下降可能导致不可靠的输出，影响生产力和对 AI 系统的信任。 作者报告称，超过 10 万 token 后性能显著下降，模型会失去焦点并出错。一些评论者指出 Opus 能很好地处理高达 50 万 token，但其他人同意无关上下文会损害性能。

hackernews · computersuck · 6月14日 06:07 · [社区讨论](https://news.ycombinator.com/item?id=48524620)

**背景**: 大上下文窗口允许 LLM 一次处理更多输入，但研究表明，随着上下文增长，模型难以保持准确性，常出现“中间丢失”效应。尽管有营销宣传，这是一个已知的局限性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://demiliani.com/2025/11/02/understanding-llm-performance-degradation-a-deep-dive-into-context-window-limits/">Understanding LLM performance degradation: a deep dive into Context Window limits – Stefano Demiliani</a></li>
<li><a href="https://eval.16x.engineer/blog/llm-context-management-guide">LLM Context Management: How to Improve Performance and Lower Costs</a></li>
<li><a href="https://towardsdatascience.com/your-1m-context-window-llm-is-less-powerful-than-you-think/">Your 1M+ Context Window LLM Is Less Powerful Than You Think | Towards Data Science</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了不同的经验：一些人通过递归代理循环等变通方法避免上下文膨胀，而另一些人报告 Opus 在高达 80 万 token 时效果良好。大家一致认为无关上下文会损害性能，记忆系统往往适得其反。

**标签**: `#LLMs`, `#context windows`, `#AI reliability`, `#practical AI`

---

<a id="item-8"></a>
## [为什么 AI 还没有取代软件工程师，而且不会](https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/#atom-everything) ⭐️ 8.0/10

Arvind Narayanan 和 Sayash Kapoor 发表了一篇文章，认为证据不支持 AI 将导致软件工程大规模裁员的说法，并引用纽约 WARN 法案数据，显示第一年没有一例与 AI 相关的裁员。 这篇文章用数据和定性分析挑战了流行的 AI 取代就业的说法，表明即使在一个特别适合 AI 颠覆的领域，核心瓶颈——决定构建什么、验证输出以及深度人类理解——仍然难以自动化。 作者指出了软件工程的三个真正瓶颈：决定和指定要构建什么、验证并对交付的内容负责，以及对代码库、业务和环境的深度人类理解。他们指出 AI 加快了输入代码的速度，但并未加速这些更高级的任务。

rss · Simon Willison · 6月14日 23:54

**背景**: 《工人调整和再培训通知法案》（WARN 法案）要求拥有 100 名或以上员工的雇主在大规模裁员前提前 60 天通知。2025 年 3 月，纽约在 WARN 申报中增加了 AI 披露复选框；在第一个完整年度，没有一家公司勾选该框。Arvind Narayanan 和 Sayash Kapoor 是《AI 蛇油》一书的作者，该书批评了夸大的人工智能承诺。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_Snake_Oil">AI Snake Oil - Wikipedia</a></li>
<li><a href="https://engineering.princeton.edu/news/2025/01/13/ai-snake-oil-conversation-princeton-ai-experts-arvind-narayanan-and-sayash-kapoor">‘AI Snake Oil’: A conversation with Princeton AI experts Arvind Narayanan and Sayash Kapoor - Princeton Engineering</a></li>

</ul>
</details>

**标签**: `#AI`, `#software engineering`, `#job displacement`, `#labor economics`

---

<a id="item-9"></a>
## [进入 AI 治理的 AGI 时代](https://www.interconnects.ai/p/welcome-to-the-agi-era-of-ai-governance) ⭐️ 8.0/10

文章认为，我们已经进入 AI 治理的 AGI 时代，其特点是做出了我们尚未准备好的不可逆转的决策。 这一转变意味着当前的 AI 治理决策具有长期影响，需要政策制定者和公众紧急且审慎地考虑。 作者将这种情况描述为“单向门”，强调一旦做出决定，就无法轻易逆转。文章指出，我们尚未为这个新时代做好准备。

rss · Interconnects · 6月14日 17:43

**背景**: AGI（通用人工智能）指的是能够执行人类任何智力任务的人工智能系统。AI 治理涉及制定政策框架来管理 AI 技术的开发和部署。文章认为，AI 的最新进展已将我们推入一个治理决策具有前所未有重要性的时代。

**标签**: `#AI governance`, `#AGI`, `#AI policy`, `#technology ethics`

---

<a id="item-10"></a>
## [OpenAI 推出合作伙伴网络，投资 1.5 亿美元](https://openai.com/index/introducing-openai-partner-network) ⭐️ 8.0/10

OpenAI 宣布推出 OpenAI 合作伙伴网络，这是一个由 1.5 亿美元投资支持的新计划，旨在帮助全球合作伙伴加速企业 AI 的采用、部署和转型。 这一举措标志着 OpenAI 深化企业布局的战略转变，可能加速 AI 在各行业的整合，并构建一个强大的服务提供商生态系统。 1.5 亿美元的投资将用于为合作伙伴提供资源、培训和上市策略支持。该网络旨在简化 OpenAI 技术在企业环境中的部署。

rss · OpenAI Blog · 6月14日 17:00

**背景**: 企业 AI 的采用通常需要专业知识和集成支持。通过建立正式的合作伙伴网络，OpenAI 遵循了企业软件领域（如 Salesforce、AWS）常见的模式，通过第三方顾问、系统集成商和经销商来扩大采用。

**标签**: `#OpenAI`, `#Enterprise AI`, `#AI Adoption`, `#Partnerships`, `#Investment`

---

<a id="item-11"></a>
## [小米 MiMo V2.5 借助 DFlash 和持久化内核实现 1000-3000 tps](https://www.reddit.com/r/LocalLLaMA/comments/1u5jtr8/xiaomi_is_now_serving_mimo_v25_at_10003000tps/) ⭐️ 8.0/10

小米宣布其 MiMo V2.5 模型现在使用 DFlash 和持久化内核实现每秒 1000-3000 tokens 的推理速度，DFlash 模型已发布，并承诺即将开源。 这一性能声称意义重大，因为它表明 LLM 推理速度实现了重大飞跃，可能实现实时应用并降低服务成本，从而影响更广泛的 AI 服务生态系统。 DFlash 模型已在 Hugging Face 上发布，持久化内核技术将整个 LLM 推理编译成一个融合的 GPU 内核，消除了内核启动开销。开源版本已承诺但尚未发布。

reddit · r/LocalLLaMA · /u/Dany0 · 6月14日 12:26

**背景**: DFlash 是一种推理加速方法，利用目标模型的隐藏状态作为输入特征，在自回归解码的质量与扩散 LLM 的速度之间取得平衡，实现高达 3 倍的推理加速。持久化内核（如 Mirage Persistent Kernel）将 LLM 推理编译成一个单一的大内核，通过消除逐算子内核启动并重叠计算与数据移动来降低延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.5">XiaomiMiMo/MiMo-V2.5 - Hugging Face</a></li>
<li><a href="https://docs.vllm.ai/projects/speculators/en/latest/user_guide/algorithms/dflash/">Dflash - Speculators Docs</a></li>
<li><a href="https://github.com/mirage-project/mirage">GitHub - mirage-project/mirage: Mirage Persistent Kernel : Compiling...</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#open-source`, `#performance optimization`, `#Xiaomi`, `#AI serving`

---

<a id="item-12"></a>
## [EAGLE 推测解码已合并到 llama.cpp](https://www.reddit.com/r/LocalLLaMA/comments/1u5z4j0/eagle_support_merged_into_llamacpp/) ⭐️ 8.0/10

EAGLE（Extrapolation Algorithm for Greater Language-model Efficiency）推测解码支持已合并到 llama.cpp 仓库中，从而在本地硬件上实现更快的 LLM 推理。 这一集成显著提升了通过 llama.cpp 在本地运行 LLM 的推理速度，使先进的推测解码技术在不牺牲输出质量的前提下惠及广大社区。 EAGLE 使用一个在目标模型隐藏状态上训练的小型草稿头来预测多个未来 token，相比标准自回归解码可实现 2-3 倍的加速。

reddit · r/LocalLLaMA · /u/Diablo-D3 · 6月14日 22:45

**背景**: 推测解码是一种推理时优化技术，通过使用较小的草稿模型提出 token，再由目标模型验证，从而加速 LLM 的 token 生成。EAGLE 是一种特定的推测解码框架，它利用目标模型自身的隐藏状态，无需单独的草稿模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/EAGLE_speculative_decoding">EAGLE (speculative decoding)</a></li>
<li><a href="https://arxiv.org/abs/2401.15077">EAGLE : Speculative Sampling Requires Rethinking Feature Uncertainty</a></li>
<li><a href="https://bentoml.com/llm/inference-optimization/speculative-decoding">Speculative decoding | LLM Inference Handbook</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对这一合并表示热情，认为 EAGLE 集成到 llama.cpp 将使推测解码在日常本地 LLM 使用中更加实用。一些用户讨论了潜在的内存开销以及与不同模型架构的兼容性问题。

**标签**: `#llama.cpp`, `#speculative decoding`, `#EAGLE`, `#LLM inference`, `#open source`

---

<a id="item-13"></a>
## [基于 Qwen3.5-397B 的实时本地语音聊天机器人](https://www.reddit.com/r/LocalLLaMA/comments/1u5uqsc/voicetovoice_chatbot_update/) ⭐️ 8.0/10

这表明大型 MoE 模型可以在消费级硬件上实现实时语音交互，有望实现无需云端的隐私保护、低延迟语音助手。 该系统使用 Unsloth 的 UD-Q3_K_XL 量化版 Qwen3.5-397B、Whisper-small 进行语音识别，以及基于 ONNX 的自定义 SNAC 解码器的 Orpheus TTS，VRAM 占用 21.3GB，上下文长度 131,072 token。

reddit · r/LocalLLaMA · /u/Responsible_Fig_1271 · 6月14日 19:45

**背景**: Qwen3.5-397B 是一个混合专家模型，总参数量 3970 亿，但每个 token 仅激活 170 亿参数，从而实现高效推理。Orpheus TTS 是一个开源文本转语音模型，能生成自然语音。Whisper-small 是一个轻量级语音识别模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/02/16/alibaba-qwen-team-releases-qwen3-5-397b-moe-model-with-17b-active-parameters-and-1m-token-context-for-ai-agents/">Alibaba Qwen Team Releases Qwen 3 . 5 - 397 B MoE ... - MarkTechPost</a></li>
<li><a href="https://andrew.ooo/posts/flash-moe-397b-model-macbook-local-inference/">Flash- MoE : Running a 397 B Parameter Model on... — andrew.ooo</a></li>
<li><a href="https://unsloth.ai/docs/models/qwen3.5/gguf-benchmarks">Qwen3.5 GGUF Benchmarks | Unsloth Documentation</a></li>

</ul>
</details>

**标签**: `#voice-to-voice`, `#local LLM`, `#real-time`, `#Qwen3.5`, `#chatbot`

---

<a id="item-14"></a>
## [在 M3 Max Mac 上通过 SSD 流式运行 DeepSeek V4 Flash](https://www.reddit.com/r/LocalLLaMA/comments/1u5mfaq/you_can_run_deepseek_4_flash_on_mac_m3_max_96gb/) ⭐️ 8.0/10

一位用户使用 antirez 的 ds4 引擎配合 SSD 流式传输，在 96GB 内存的 M3 Max Mac 上成功运行 DeepSeek V4 Flash，达到约 12 tokens/s 的速度。该方法需要传递--ssd-streaming 参数并调整 Metal 内存限制。 这展示了像 DeepSeek V4 Flash 这样的大型混合专家模型可以通过 SSD 流式传输在消费级 Mac 硬件上运行，无需海量内存。这降低了本地 LLM 部署的门槛，使强大模型能在笔记本上运行。 该设置使用 antirez 的 ds4 引擎配合自定义 GGUF 文件和--ssd-streaming 标志，并通过 iogpu.wired_limit_mb=86016 提高 Metal 分配。36k token 的预填充耗时约 2.5 分钟，但后续生成保持约 12 t/s。

reddit · r/LocalLLaMA · /u/Zeeplankton · 6月14日 14:20

**背景**: DeepSeek V4 Flash 是一个混合专家模型，参数量巨大，通常需要大内存。SSD 流式传输按需从磁盘加载必要的专家权重，使得运行比内存更大的模型成为可能。ds4 引擎是专为 DeepSeek 模型设计的推理引擎，支持 Metal、CUDA 和 ROCm。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez/ds4: DeepSeek 4 Flash and PRO local inference engine for Metal, CUDA and ROCm · GitHub</a></li>
<li><a href="https://github.com/quantumnic/ssd-llm">GitHub - quantumnic/ssd-llm: Run 70B+ LLMs on Apple Silicon by using SSD as extended memory — intelligent layer streaming and caching for Mac</a></li>
<li><a href="https://simonwillison.net/2026/Mar/24/streaming-experts/">Streaming experts</a></li>

</ul>
</details>

**社区讨论**: 社区对此印象深刻并验证了可行性，一些用户分享了类似经验。大家讨论了缓存安全补丁等优化，并表示有兴趣尝试其他 MoE 模型。

**标签**: `#DeepSeek`, `#Local LLM`, `#Mac`, `#GGUF`, `#SSD streaming`

---

<a id="item-15"></a>
## [双 DGX Spark 运行 DeepSeek V4 Flash 达到 350 tk/s](https://www.reddit.com/r/LocalLLaMA/comments/1u5g9pr/dual_dgx_sparks_40tks_single_1m_350_tks_agg/) ⭐️ 8.0/10

一份实用指南对双 DGX Spark（通过一根 180 美元的 ConnectX-7 线缆连接）运行 DeepSeek V4 Flash 进行了基准测试，实现了约 40 tk/s 的单流速度和约 350 tk/s 的聚合吞吐量（使用 FP8 量化）。 这表明前沿的 MoE 模型可以在本地以可用速度运行，适用于代理工作流，可能减少对云端 API 进行高吞吐量推理的依赖。 该设置使用两台 DGX Spark，搭配 vLLM 和 FP8 量化，在 32 个并发请求（每个上下文 256k）下实现了约 350 tk/s 的聚合速度，优于单块 RTX Pro 6000（46.9 tk/s）和 Mac M2 Ultra（29.7 tk/s）。

reddit · r/LocalLLaMA · /u/elsung · 6月14日 09:07

**背景**: DeepSeek V4 Flash 是一个 284B 参数的 MoE 模型，激活参数为 13B，支持 100 万 token 的上下文窗口。DGX Spark 是 NVIDIA 的紧凑型桌面 AI 超级计算机，ConnectX-7 是一种 200 Gbps 的互连线缆，可实现低延迟的多节点推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>
<li><a href="https://www.lenovo.com/us/en/p/accessories-and-software/cables-and-adapters/cables/4x91u42988">PGX ConnectX-7 cable | 4X91U42988 | Lenovo US</a></li>
<li><a href="https://sebastianraschka.com/blog/2025/dgx-impressions.html">Local PyTorch and LLM Dev: DGX Spark ... | Sebastian Raschka, PhD</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区称赞该基准测试具有高价值和实用性，讨论集中在 180 美元线缆相对于云替代方案的成本效益上。一些用户指出需要两台 DGX Spark 是一个限制。

**标签**: `#DeepSeek`, `#DGX Spark`, `#MoE`, `#benchmark`, `#local LLM`

---