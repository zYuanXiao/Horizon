---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 151 条内容中筛选出 15 条重要资讯。

---

1. [OpenAI 发布首款定制 AI 推理芯片 Jalapeño](#item-1) ⭐️ 9.0/10
2. [通过自对弈强化学习实现超人类 Generals.io 智能体](#item-2) ⭐️ 9.0/10
3. [GitHub 仓库为 AI 智能体映射 817 项网络安全技能](#item-3) ⭐️ 8.0/10
4. [NousResearch/hermes-agent 单日获 1178 星](#item-4) ⭐️ 8.0/10
5. [NatureBench 测试 AI 智能体的真实科学发现能力](#item-5) ⭐️ 8.0/10
6. [MobileForge：移动 GUI 代理的无标注自适应系统](#item-6) ⭐️ 8.0/10
7. [卡马克反思在 id Software 早期对团队施压过重](#item-7) ⭐️ 8.0/10
8. [Rust 社区讨论 crates.io 对 GitHub 的依赖问题](#item-8) ⭐️ 8.0/10
9. [业余操作系统通过移植 Wine 运行 Windows 游戏](#item-9) ⭐️ 8.0/10
10. [PostHog SQL 解析器借助 AI 重写，速度提升 70 倍](#item-10) ⭐️ 8.0/10
11. [LLM 生成的求职申请侵蚀真实性](#item-11) ⭐️ 8.0/10
12. [TRM 思考奖励模型量化大模型推理质量](#item-12) ⭐️ 8.0/10
13. [Databricks 领导者倡导开放前沿生态系统](#item-13) ⭐️ 8.0/10
14. [Claude Tag：Slack 中的多人、主动、持久化 AI 代理](#item-14) ⭐️ 8.0/10
15. [上下文窗口不等于记忆：AI Agent 开发者的关键认知](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布首款定制 AI 推理芯片 Jalapeño](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 发布了其首款定制 AI 推理芯片，名为 Jalapeño，由 Broadcom 合作开发、台积电制造。该芯片从零开始设计，并声称在 OpenAI 自身 AI 模型的加速下，从设计到生产仅用了九个月。 这标志着 OpenAI 减少对 NVIDIA GPU 依赖、优化大规模推理成本和性能的重大战略举措。随着推理成为主导的 AI 工作负载，像 Jalapeño 这样的定制芯片可能重塑 AI 硬件格局，并降低部署大型语言模型的成本。 Jalapeño 是一款针对 LLM 工作负载优化的推理专用 ASIC，基于 Broadcom 的 XPU 平台构建，由台积电制造。OpenAI 声称该芯片的开发由其自身 AI 模型加速，但部分社区成员质疑这一说法的意义。

hackernews · jamdesk · 6月24日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 推理是运行已训练模型以生成预测的过程，与需要大量算力的训练不同。推理芯片专门优化每 token 成本、延迟和能效，随着 AI 模型大规模部署而日益重要。Broadcom 有为 Google（TPU）和 Meta 等超大规模企业设计定制 AI 芯片的历史。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip</a></li>
<li><a href="https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/">OpenAI unveils its first custom chip, built by Broadcom</a></li>
<li><a href="https://investors.broadcom.com/news-releases/news-release-details/openai-and-broadcom-unveil-llm-optimized-intelligence-processor">OpenAI and Broadcom Unveil LLM-Optimized Intelligence ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 AI 加速设计的说法表示好奇，部分人怀疑这可能是营销噱头。其他人指出该芯片由台积电制造，并讨论了推理专用芯片的潜力，将其与 Google 的 TPU 以及像 Taalas 这样将模型烧录到硅片中的初创公司进行比较。

**标签**: `#AI hardware`, `#OpenAI`, `#custom chip`, `#inference`, `#Broadcom`

---

<a id="item-2"></a>
## [通过自对弈强化学习实现超人类 Generals.io 智能体](https://www.reddit.com/r/MachineLearning/comments/1uei2yg/i_made_a_superhuman_generalsio_agent_with/) ⭐️ 9.0/10

一个使用 JAX 和 Vision Transformer 的自对弈强化学习智能体在 Generals.io 1v1 人类排行榜上取得第一名，超越了顶尖人类玩家。该项目完全开源，包括一个快速的 JAX 模拟器和详细指南。 这项工作表明，通过 JAX 和 ViT 扩展计算和模型容量，可以在复杂的实时策略游戏中超越手工特征和人类先验。它为使用现代工具构建超人类游戏 AI 提供了可复现的蓝图。 该智能体最初通过行为克隆和 RL 微调训练，但仅在将整个流程重写为 JAX 并用 Vision Transformer 替换 CNN 后才达到超人类水平。开源代码包括一个快速的基于 JAX 的游戏模拟器，可作为不完美信息 RTS 环境使用。

reddit · r/MachineLearning · /u/shrekofspeed · 6月24日 16:18

**背景**: Generals.io 是一款快节奏的多人在线实时策略游戏，玩家需要占领领土并消灭对手的将军。自对弈强化学习已在围棋、国际象棋等游戏中取得超人类表现，但应用于不完美信息 RTS 游戏仍具挑战。JAX 是一个高性能数值计算库，可实现高效的 GPU/TPU 加速；Vision Transformer（ViT）最近被探索作为 CNN 的替代方案用于游戏 AI。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.generals.io/">generals.io</a></li>
<li><a href="https://arxiv.org/abs/2408.13871">[2408.13871] AlphaViT: A flexible game-playing AI for multiple games and variable board sizes</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对该工作的技术深度和开源贡献表示赞赏，许多人询问具体的训练细节和 ViT 的作用。部分用户讨论了将自对弈 RL 应用于不完美信息游戏的难度，以及 JAX 重写对性能提升的重要性。

**标签**: `#reinforcement learning`, `#self-play`, `#JAX`, `#game AI`, `#vision transformer`

---

<a id="item-3"></a>
## [GitHub 仓库为 AI 智能体映射 817 项网络安全技能](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10

一个名为 mukul975/Anthropic-Cybersecurity-Skills 的 GitHub 仓库已发布，提供了 817 项结构化的网络安全技能，映射到包括 MITRE ATT&CK 和 NIST CSF 2.0 在内的六个框架，并兼容 20 多个平台。 该仓库弥合了网络安全框架与 AI 智能体能力之间的鸿沟，支持跨多个平台和框架的自动化安全操作，可能显著加速企业环境中的威胁检测与响应。 这些技能按照最初由 Anthropic 开发的 agentskills.io 标准格式化，涵盖 29 个安全领域，采用 Apache 2.0 许可证。该仓库已获得超过 20,000 颗星和 2,300 个分支，表明社区高度认可。

github_trending · GitHub Trending · 6月25日 03:52

**背景**: AI 智能体是能够自主执行任务的软件程序，而 MITRE ATT&CK 等网络安全框架提供了对手策略和技术的标准化分类法。agentskills.io 标准定义了描述可复用智能体技能的规范，促进了不同 AI 智能体平台之间的互操作性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/agentskills/agentskills">GitHub - agentskills/agentskills: Specification and ...</a></li>
<li><a href="https://agentskills.io/home">Agent Skills Overview - Agent Skills</a></li>
<li><a href="https://atlas.mitre.org/">MITRE ATLAS™</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI agents`, `#MITRE ATT&CK`, `#NIST CSF`, `#open source`

---

<a id="item-4"></a>
## [NousResearch/hermes-agent 单日获 1178 星](https://github.com/NousResearch/hermes-agent) ⭐️ 8.0/10

NousResearch/hermes-agent，一个基于 Python 的 AI 智能体框架，单日获得 1178 个 GitHub 星标，总星标数超过 20.2 万。该项目被描述为一个具有内置学习循环的自我改进智能体，能从经验中创造技能。 这种快速增长表明社区对具有持久记忆和自我改进能力的自主 AI 智能体有浓厚兴趣。它反映了开源 AI 智能体能够跨会话学习和适应的更广泛趋势。 Hermes Agent 可作为 macOS、Windows 和 Linux 的原生应用使用，并与 Telegram、Discord、Slack、WhatsApp 和 Signal 等消息平台集成。其内置学习循环使其能够从经验中创造和改进技能。

github_trending · GitHub Trending · 6月25日 03:52

**背景**: AI 智能体是能够自主执行任务的软件程序，通常使用大型语言模型。Hermes Agent 的独特之处在于具有持久记忆和学习循环，使其能够随时间建立用户模型。这是不断增长的开源 AI 智能体生态系统的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/nousresearch/hermes-agent">NousResearch/hermes-agent: The agent that grows with you - GitHub</a></li>
<li><a href="https://hermes-agent.nousresearch.com/">Hermes Agent | Nous Research</a></li>
<li><a href="https://hermes-agent.nousresearch.com/docs/">Hermes Agent Documentation | Hermes Agent</a></li>

</ul>
</details>

**标签**: `#AI`, `#agent`, `#Python`, `#open-source`

---

<a id="item-5"></a>
## [NatureBench 测试 AI 智能体的真实科学发现能力](https://huggingface.co/papers/2606.24530) ⭐️ 8.0/10

研究人员推出了 NatureBench，这是一个包含 90 个来自 Nature 系列论文任务的基准测试，发现当前 AI 编码智能体仅在 17.8%的任务上超越已发表的最优结果，且主要依赖方法翻译而非真正创新。 该基准测试为 AI 编码智能体在科学发现中提供了可信的跨学科评估，凸显了复现与真正创新之间的关键差距，这是 AI 推动科学进步必须解决的问题。 NatureBench 使用 NatureGym 自动管道为每个任务创建标准化的容器化环境，解决了环境碎片化问题。评估在严格的禁用网络搜索协议下进行，使用了十种前沿智能体配置。

huggingface_papers · Hugging Face Papers · 6月24日 00:00

**背景**: AI 编码智能体是能够编写和执行代码以解决问题的系统。以往的基准测试常受环境碎片化困扰，即不同任务需要不同设置，难以公平比较。NatureBench 通过将每个任务容器化来解决此问题。该基准测试涵盖六个科学领域，重点关注智能体能否实现超越简单复现的发现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.24530">NatureBench : Can Coding Agents Match the Published SOTA of...</a></li>
<li><a href="https://huggingface.co/papers/2606.24530">Paper page - NatureBench : Can Coding Agents Match the Published...</a></li>
<li><a href="https://github.com/FrontisAI/NatureBench">GitHub - FrontisAI/ NatureBench : NatureBench : Can Coding Agents...</a></li>

</ul>
</details>

**标签**: `#AI for Science`, `#Benchmark`, `#Coding Agents`, `#Scientific Discovery`, `#Nature`

---

<a id="item-6"></a>
## [MobileForge：移动 GUI 代理的无标注自适应系统](https://huggingface.co/papers/2606.19930) ⭐️ 8.0/10

MobileForge 提出了一种无需标注的移动 GUI 代理自适应系统，结合了 MobileGym（真实应用交互基础）和分层反馈引导策略优化（HiFPO）进行步骤级策略更新。适配后的 Qwen3-VL-8B 在 AndroidWorld 上达到 67.2%的 Pass@3，而 ForgeOwl-8B 达到 77.6%的 Pass@3，在开放数据移动 GUI 代理中创下新纪录。 这项工作通过消除人工标注需求，大幅降低了将 GUI 代理适配到真实移动应用的成本，考虑到移动应用数量庞大且更新频繁，这一点至关重要。在域内和域外基准测试上的强劲表现证明了无标注自适应在移动自动化中的实际可行性。 MobileForge 使用 MobileGym 在真实应用环境中自动生成任务并评估轨迹，HiFPO 将轨迹结果、步骤级过程反馈和纠正提示转化为提示上下文化的步骤级 GRPO 更新。该系统仅使用自动生成的无标注数据，在 AndroidWorld 上达到 77.6%的 Pass@3，在域外 MobileWorld GUI-only 分割上达到 41.0%的成功率。

huggingface_papers · Hugging Face Papers · 6月24日 00:00

**背景**: 基于多模态大语言模型（MLLM）的移动 GUI 代理能够理解 UI 屏幕并执行操作，但将它们适配到新应用通常需要昂贵的人工编写任务、演示或奖励标签。无标注学习旨在减少这种人工投入，但现有方法缺乏统一的框架来连接探索、课程挖掘、轨迹执行和反馈，且往往依赖粗粒度的奖励。MobileForge 通过将学习扎根于真实应用交互并使用分层反馈进行细粒度策略优化来解决这些问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.19930">[2606.19930] MobileForge: Annotation - Free Adaptation for Mobile...</a></li>
<li><a href="https://huggingface.co/papers/2606.19930">Paper page - MobileForge: Annotation-Free Adaptation for ...</a></li>
<li><a href="https://arxiv.org/abs/2602.22817">Hierarchy-of-Groups Policy Optimization for Long-Horizon ... MobileForge: Annotation-Free Adaptation for Mobile GUI Agents ... AI Native Daily Paper Digest – 20260624 - AI Native Foundation ICML 2026 Papers</a></li>

</ul>
</details>

**标签**: `#mobile GUI agents`, `#annotation-free learning`, `#policy optimization`, `#MLLM`, `#UI automation`

---

<a id="item-7"></a>
## [卡马克反思在 id Software 早期对团队施压过重](https://twitter.com/ID_AA_Carmack/status/2069799283369345247) ⭐️ 8.0/10

约翰·卡马克公开反思在 id Software 早期对团队施压过重，承认创业公司的强度对成熟公司来说不可持续。 这一反思为科技和游戏开发行业提供了宝贵的领导力教训，强调了加班文化的长期代价以及可持续工作实践的重要性。 卡马克特别提到，他没有意识到成熟的公司需要更多的宽松度，而持续以创业强度要求员工会让他们精疲力竭。这条推文提到了《雷神之锤》的开发，他认为这款游戏耗尽了 id Software 的精力，但鉴于其影响力，这是值得的。

hackernews · shadowtree · 6月24日 15:56 · [社区讨论](https://news.ycombinator.com/item?id=48661825)

**背景**: 约翰·卡马克是传奇游戏程序员和 id Software 的联合创始人，以创作《毁灭战士》和《雷神之锤》等标志性游戏而闻名。id Software 早期以高强度加班文化为特征，团队长时间工作以推动技术边界。这条推文是游戏行业关于此类做法可持续性更广泛讨论的一部分。

**社区讨论**: 评论者普遍认同卡马克的反思，有人指出《雷神之锤》的成功是以团队的高昂代价换来的。其他人则争论结果是否证明手段合理，一位评论者表示游戏比游戏公司更重要。还有关于 Sandy Petersen 对 id Software 加班文化看法的讨论。

**标签**: `#game development`, `#leadership`, `#startup culture`, `#John Carmack`, `#id Software`

---

<a id="item-8"></a>
## [Rust 社区讨论 crates.io 对 GitHub 的依赖问题](https://infosec.exchange/@mttaggart/116806641273303255) ⭐️ 8.0/10

最近在 Infosec Exchange 上的一场讨论批评了当前在 crates.io 上发布 Rust 包需要 GitHub 账户的问题，强调了社区正在努力解耦这一长期依赖。 这种依赖为 Rust 包生态系统带来了单点故障和供应商锁定问题，影响所有发布或使用 crate 的 Rust 开发者。解耦将提高系统的韧性，并符合开源原则。 最近合并了一个 RFC（pull/3963）以推动解耦工作，实现已经开始。然而，由于 Rust 开发主要由志愿者驱动，且该任务被认为缺乏趣味且资金不足，进展缓慢。

hackernews · speckx · 6月24日 19:40 · [社区讨论](https://news.ycombinator.com/item?id=48664733)

**背景**: crates.io 是 Rust 的官方包注册中心，开发者在此发布和分享库（crate）。目前，发布 crate 需要通过 GitHub 账户进行身份验证，这一集成在早期 GitHub 被视为开源乌托邦时建立，现已深深嵌入系统，难以移除。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/rust-lang/crates.io">GitHub - rust-lang/crates.io: The Rust package registry GitHub Dependency for Rust Crates.io Publishing Criticized The crates.io package index GitHub - BarbossHack/crates-io: crates-io is an extension ... Specifying Dependencies - The Cargo Book - Learn Rust Overriding Dependencies - The Cargo Book - Learn Rust</a></li>

</ul>
</details>

**社区讨论**: 社区成员普遍同意应该移除这种依赖，但承认由于志愿者驱动开发和缺乏资金，难度很大。一些人赞赏像 Packagist 那样基于源码打包的替代方案，另一些人则指出了现有的路线图并欢迎志愿者贡献。

**标签**: `#rust`, `#crates.io`, `#github`, `#open-source`, `#package management`

---

<a id="item-9"></a>
## [业余操作系统通过移植 Wine 运行 Windows 游戏](https://astral-os.org/posts/2026/04/03/wine-on-astral.html) ⭐️ 8.0/10

业余操作系统 Astral OS 的开发者成功地将 Wine 移植到该系统上，使其能够直接运行 Windows 游戏，这是一项重大的技术成就。 这表明业余操作系统可以通过利用 Wine 等兼容层来充当日常使用的系统，从而弥合实验系统与实用之间的差距。 该移植无需 X 服务器或模拟器即可原生运行，依赖于 Wine 的直接渲染和窗口支持。开发者此前还移植了 Minecraft，表明其具备支持流行应用程序的能力。

hackernews · avaliosdev · 6月24日 14:38 · [社区讨论](https://news.ycombinator.com/item?id=48660671)

**背景**: Wine 是一个免费开源兼容层，通过将 Windows API 调用转换为 POSIX 调用，使 Windows 应用程序能在类 Unix 操作系统上运行。业余操作系统通常由个人或小团队出于学习或实验目的开发，通常缺乏主流系统的应用生态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wine_compatibility_layer">Wine compatibility layer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hobbyist_operating_system">Hobbyist operating system - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一技术成就表示赞赏，有人指出业余操作系统为了实用而需要实现旧接口的讽刺之处。其他人则分享了自己的业余操作系统开发经验，强调了简单性与兼容性之间的权衡。

**标签**: `#hobby OS`, `#Wine`, `#operating systems`, `#compatibility`, `#gaming`

---

<a id="item-10"></a>
## [PostHog SQL 解析器借助 AI 重写，速度提升 70 倍](https://posthog.com/blog/sql-parser) ⭐️ 8.0/10

PostHog 使用多个并行的 Claude Code 会话重写了其 SQL 解析器，生成了 1.6 万行手写风格的解析器代码和 5 千行工具代码，实现了约 70 倍的性能提升。 这展示了 LLM 在性能关键型代码生成中的实际高影响力应用，表明 AI 辅助开发可以在减少人工工作量的同时大幅改进生产系统。 新解析器是由 AI 生成的手写递归下降解析器，取代了基于 ANTLR 的解析器。作者并行使用了多个长时间运行的 Claude Code 会话来生成代码，其中包括大量测试。

hackernews · robbie-c · 6月24日 18:05 · [社区讨论](https://news.ycombinator.com/item?id=48663544)

**背景**: 解析器将源代码（如 SQL）转换为结构化格式（AST）以便分析和执行。与 ANTLR 等解析器生成器相比，手写解析器通常更快且能产生更好的错误信息，但传统上编写和维护的工作量更大。该项目利用 LLM 自动化了这部分工作，同时保留了性能优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://posthog.com/blog/sql-parser">I wrote a 70x faster SQL parser while barely looking at the code</a></li>
<li><a href="https://www.linkedin.com/posts/robbiecoomber_i-rewrote-posthogs-sql-parser-and-made-it-activity-7475585969623269376-oGbq">I rewrote PostHog's SQL parser and made it 70x faster while ...</a></li>

</ul>
</details>

**社区讨论**: 评论者就手写解析器与生成解析器的优劣展开了辩论，有人认为手写解析器比通常认为的更容易维护。其他人则称赞在具有可靠 oracle 的问题上使用 AI，但担心过度依赖 AI 可能会阻碍长期的知识增长。

**标签**: `#SQL`, `#parser`, `#AI-assisted development`, `#performance`, `#PostHog`

---

<a id="item-11"></a>
## [LLM 生成的求职申请侵蚀真实性](https://simonwillison.net/2026/Jun/24/tom-macwright/#atom-everything) ⭐️ 8.0/10

Tom MacWright 观察到，求职申请和作品集越来越多地由 LLM 共同撰写，使得候选人难以区分且缺乏个性。 这一趋势削弱了招聘中的真实性，使雇主更难评估候选人的真实匹配度，并可能贬低求职市场中的人类努力。 MacWright 指出，LLM 生成的申请通常链接到 LLM 生成的作品集和 GitHub 项目，提交信息也完全由 LLM 生成，无法揭示候选人的真实能力。

rss · Simon Willison · 6月24日 18:13

**背景**: 大型语言模型（如 GPT-4）可以生成模仿人类写作的文本。求职者开始使用这些工具来撰写简历、求职信甚至代码作品集，这虽然节省时间，但也产生了千篇一律、缺乏个性的内容，无法传达个人特质或经历。

**标签**: `#AI`, `#careers`, `#hiring`, `#authenticity`, `#LLM`

---

<a id="item-12"></a>
## [TRM 思考奖励模型量化大模型推理质量](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247899199&idx=3&sn=b0d6764e50d881295fd85b75f8f9434a) ⭐️ 8.0/10

思考奖励模型（TRM）作为 ICML 2026 Oral 论文被接收并发布，旨在量化大模型推理过程的质量。该开源项目已在 GitHub 上获得 4.2k 星标。 这提供了一种不仅评估答案正确性，还能评估推理过程质量的方法，对提升模型透明度和可靠性至关重要。它可能影响大模型强化学习中奖励模型的设计方式。 TRM 采用门控机制，仅在答案正确时应用奖励塑造，避免模型从错误轨迹中学习。实验表明，该方法在多个模型和任务上均带来了性能提升。

rss · 量子位 · 6月24日 04:00

**背景**: 大模型常常能给出正确答案，但推理过程可能存在缺陷。传统的奖励模型只关注最终答案的正确性，忽略了推理路径。TRM 通过评估思考过程本身来解决这一问题，使用基于推理质量训练的奖励模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aitntnews.com/newDetail.html?newId=26520">TRM思考奖励模型上线，大模型推理质量终于能量化了 | ICML‘26 Oral</a></li>
<li><a href="https://36kr.com/p/3866659734279170">TRM思考奖励模型上线，大模型推理质量终于能量化了-36氪</a></li>
<li><a href="https://blog.csdn.net/2501_94005722/article/details/162271719">ICML‘26 Oral | TRM思考奖励模型上线，大模型推理质量终于能量化了-CS...</a></li>

</ul>
</details>

**标签**: `#大模型`, `#推理质量`, `#奖励模型`, `#ICML`, `#开源`

---

<a id="item-13"></a>
## [Databricks 领导者倡导开放前沿生态系统](https://www.latent.space/p/databricks) ⭐️ 8.0/10

在一次罕见的联合采访中，Databricks 技术领导者 Matei Zaharia 和 Reynold Xin 主张前沿生态系统必须开放，以使每家公司都能构建 Agent Cloud。 这一愿景可能塑造 AI 代理基础设施的未来，推动开放性和互操作性而非专有锁定，这对于企业广泛采用 AI 代理至关重要。 采访涵盖了开放生态系统的技术和战略理由，包括 Databricks 的开源根基（如 Apache Spark）如何影响其对 AI 代理的方法。

rss · Latent Space · 6月24日 18:53

**背景**: Databricks 是一个领先的数据和 AI 平台，基于 Apache Spark 和 Delta Lake 等开源技术构建。'Agent Cloud' 的概念指的是一个平台，公司可以在其中构建、部署和管理与数据交互并自主执行任务的 AI 代理。开放生态系统意味着使用开放标准和 API 以避免供应商锁定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.databricks.com/">Databricks: Leading Data and AI Platform for Enterprises</a></li>
<li><a href="https://streampoint-research.com/databricks-ecosystem/">Understanding the Databricks Ecosystem: A Complete Guide</a></li>

</ul>
</details>

**标签**: `#AI`, `#open source`, `#data infrastructure`, `#agents`, `#Databricks`

---

<a id="item-14"></a>
## [Claude Tag：Slack 中的多人、主动、持久化 AI 代理](https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive) ⭐️ 8.0/10

Anthropic 推出了 Claude Tag，这是其 Slack 集成的一次重大升级，在 Slack 频道中引入了多人、主动和持久化的 AI 代理。 此次升级将 Claude 从被动响应的聊天机器人转变为持久的团队成员，能够监控频道、主动行动并与多个用户同时协作，显著提升团队生产力和 AI 辅助工作流程。 Claude Tag 是多人协作的，即单个 Claude 实例与频道中的所有人交互，而不是每个用户拥有独立实例。它还具有主动性和持久性，能够从对话中学习、监控任务并随着时间的推移自主工作。

rss · Latent Space · 6月24日 07:14

**背景**: Slack 中的传统 AI 助手通常是被动响应的，仅在明确提及时才回应。Claude Tag 代表了向持久化、主动代理的转变，这些代理可以作为后台队友，这一趋势也体现在其他编码代理如 Claude Code 和 Codex 中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive">[AINews] Claude Tag: Multiplayer, Proactive, Persistent Agents in Slack</a></li>
<li><a href="https://venturebeat.com/technology/anthropic-launches-claude-tag-replacing-its-slack-app-with-a-persistent-ai-teammate-that-learns-monitors-and-works-autonomously">Anthropic launches Claude Tag, replacing its Slack app with a ...</a></li>

</ul>
</details>

**标签**: `#Claude`, `#Slackbot`, `#AI agents`, `#multiplayer`, `#product update`

---

<a id="item-15"></a>
## [上下文窗口不等于记忆：AI Agent 开发者的关键认知](https://machinelearningmastery.com/context-windows-are-not-memory-what-ai-agent-developers-need-to-understand/) ⭐️ 8.0/10

本文澄清了 LLM 中的大上下文窗口并不等同于 Agent 记忆，并介绍了检索增强生成（RAG）和上下文窗口压缩等有效记忆管理技术。 理解这一区别对 AI Agent 开发者至关重要，因为仅依赖上下文窗口会导致长期记忆不佳和可扩展性问题。正确的记忆技术使 Agent 能够在长时间会话中保持连贯且上下文感知的交互。 文章强调上下文窗口大小有限且会话结束后信息丢失，而 Agent 记忆涉及跨轮次存储、检索和压缩信息。RAG 和滑动窗口压缩等技术被作为实用解决方案提出。

rss · Machine Learning Mastery · 6月24日 12:00

**背景**: 大型语言模型（LLM）在固定大小的上下文窗口内处理输入，这决定了它们一次能考虑多少文本。Agent 记忆是指允许 AI Agent 保留并使用过去交互信息的机制，类似于人类记忆。检索增强生成（RAG）将 LLM 与外部知识检索相结合，而上下文窗口压缩则减少历史数据的 token 占用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NirDiamant/Agent_Memory_Techniques">NirDiamant/Agent_Memory_Techniques - GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation</a></li>
<li><a href="https://www.modular.com/ai-resources/context-window-compression-techniques-to-fit-more-information-into-less-space">Context Window Compression : Techniques to Fit More Information...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#LLMs`, `#Memory`, `#Context Window`, `#Retrieval`

---