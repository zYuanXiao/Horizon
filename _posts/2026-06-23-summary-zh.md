---
layout: default
title: "Horizon Summary: 2026-06-23 (ZH)"
date: 2026-06-23
lang: zh
---

> 从 131 条内容中筛选出 15 条重要资讯。

---

1. [Valve 发布 Steam Machine，倡导开放硬件](#item-1) ⭐️ 9.0/10
2. [提示注入利用大语言模型角色混淆漏洞](#item-2) ⭐️ 9.0/10
3. [DeepSeek 以 600 亿美元估值融资 74 亿美元](#item-3) ⭐️ 9.0/10
4. [中国黑客克隆英伟达 Tesla V100 GPU](#item-4) ⭐️ 9.0/10
5. [OpenMontage：首个开源智能视频制作系统](#item-5) ⭐️ 8.0/10
6. [817 项 AI 代理网络安全技能，映射至六大框架](#item-6) ⭐️ 8.0/10
7. [趣味机器人学习提升技能获取](#item-7) ⭐️ 8.0/10
8. [S-Agent：利用空间工具实现连续 3D 推理](#item-8) ⭐️ 8.0/10
9. [Mitchell Hashimoto 向 Zig 软件基金会承诺捐款 40 万美元](#item-9) ⭐️ 8.0/10
10. [8087 协处理器快速位移位器的芯片分析](#item-10) ⭐️ 8.0/10
11. [Claude Code 的“扩展思考”输出是有损摘要](#item-11) ⭐️ 8.0/10
12. [Linux Secure Boot 证书将于 2025 年到期](#item-12) ⭐️ 8.0/10
13. [Codex 日志漏洞可能导致本地 SSD 写入数 TB 数据](#item-13) ⭐️ 8.0/10
14. [AI 安全不仅仅是带 AI 的网络安全](#item-14) ⭐️ 8.0/10
15. [微软开源 FastContext，助力 LLM 编码代理](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Valve 发布 Steam Machine，倡导开放硬件](https://store.steampowered.com/news/group/45479024/view/685257114654870245) ⭐️ 9.0/10

Valve 于 2026 年 6 月 22 日发布了 Steam Machine，这是一款秉持开放硬件理念的游戏 PC，并采用随机预约系统来对抗机器人和黄牛。 此次发布标志着 Valve 重返专用游戏硬件领域，并强调开放性，可能影响行业对类主机 PC 和反黄牛措施的态度。 Steam Machine 起售价 1049 美元，采用随机预约队列（开放至 6 月 25 日），并允许用户安装其他操作系统或应用，体现了 Valve“宗教般”拒绝构建封闭系统的理念。

hackernews · theschwa · 6月22日 17:09 · [社区讨论](https://news.ycombinator.com/item?id=48632884)

**背景**: Steam Machine 是一款运行 SteamOS 的游戏 PC，SteamOS 基于 Arch Linux，并通过 Proton 兼容层运行 Windows 游戏。Valve 曾在 2015 年尝试过 Steam Machine 计划，但未能成功。新款机型强调开放性和用户自由，与传统主机形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcgamer.com/hardware/valve-says-it-isnt-subsidizing-the-steam-machines-usd1050-price-because-of-its-religious-refusal-to-build-a-more-closed-system/">Valve says it isn't subsidizing the Steam Machine's $1050 price because of its 'religious' refusal to 'build a more closed system' | PC Gamer</a></li>
<li><a href="https://www.tomshardware.com/video-games/console-gaming/valve-opens-steam-machine-reservations-details-usd1-049-starting-price-randomized-queue-to-stop-scalpers-and-limited-inventory">Valve opens Steam Machine reservations — details $1,049 starting price, randomized queue to stop scalpers, and limited inventory | Tom's Hardware</a></li>
<li><a href="https://www.pcgamer.com/hardware/gaming-pcs/steam-machine-reservations/">Sign up for a Steam Machine before June 25: Valve running one-time randomized queue due to limited availability and to 'limit resellers' | PC Gamer</a></li>

</ul>
</details>

**社区讨论**: 社区评论总体积极，称赞随机预约系统的公平性以及开放硬件理念。用户也对公告中展示的真实游戏画面表示赞赏。

**标签**: `#gaming`, `#hardware`, `#valve`, `#steam`, `#pc-gaming`

---

<a id="item-2"></a>
## [提示注入利用大语言模型角色混淆漏洞](https://role-confusion.github.io/) ⭐️ 9.0/10

一篇新论文和博客文章揭示，提示注入攻击通过利用大语言模型中的角色混淆来成功实施，人类红队成员对前沿模型的攻击成功率接近 100%，尽管这些模型在标准基准测试中得分完美。 这项研究暴露了大语言模型处理角色分离时的根本缺陷，动摇了当前依赖角色标签的安全架构。它凸显了静态基准测试的不足，以及针对自适应人类攻击者建立更强大防御的必要性。 论文表明，角色标签（例如系统与用户）仅仅是格式技巧，并未进入模型的内部表示，因此容易被对抗性输入欺骗。人类红队成员可以实时调整攻击策略，而静态基准测试仅衡量针对已知攻击模式的防御能力。

hackernews · x312 · 6月22日 15:48 · [社区讨论](https://news.ycombinator.com/item?id=48631888)

**背景**: 提示注入是一种攻击方式，恶意输入导致大语言模型忽略开发者指令而遵循用户命令。角色混淆发生在模型无法区分系统定义的角色和用户提供的内容时，从而导致意外行为。这项研究将这两种现象联系起来，表明角色混淆是提示注入的根本原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://role-confusion.github.io/">Prompt Injection as Role Confusion</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://en.wikipedia.org/wiki/Red_teaming">Red teaming</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了实际影响：一位用户指出，将内容包裹在<think>标签中是无关紧要的，因为仅凭风格就能绕过护栏。另一位用户称赞博客风格的写作使研究更易理解。一条批评性评论质疑将角色视为安全架构的框架，认为大语言模型并未提供真正的安全保障。

**标签**: `#prompt injection`, `#LLM security`, `#role confusion`, `#AI safety`, `#red teaming`

---

<a id="item-3"></a>
## [DeepSeek 以 600 亿美元估值融资 74 亿美元](https://www.reddit.com/r/LocalLLaMA/comments/1ucwyes/deepseek_raises_74b_usd_at_60b_valuation/) ⭐️ 9.0/10

DeepSeek 完成 74 亿美元融资，估值达 600 亿美元，创始人梁文峰个人投资 30 亿美元。 这笔巨额融资凸显了投资者对领先 AI 公司的强烈兴趣，也标志着 DeepSeek 强大的市场地位。梁文峰的个人投资显示了他对公司未来的非凡信心。 74 亿美元的融资规模是 AI 领域史上最大之一，600 亿美元的估值使 DeepSeek 跻身最具价值的私有 AI 公司之列。梁文峰 30 亿美元的个人投资对创始人而言尤为突出。

reddit · r/LocalLLaMA · /u/FullOf_Bad_Ideas · 6月22日 21:03

**背景**: DeepSeek 是一家以开发大语言模型闻名的中国 AI 初创公司。该公司因其有竞争力的模型和快速增长而受到关注。本轮融资很可能将用于进一步推动研发。

**社区讨论**: Reddit 用户对此次融资表示兴奋，许多人指出创始人的个人投资是强有力的信心投票。一些人讨论了这对 AI 行业的影响以及与其他主要参与者的竞争。

**标签**: `#AI`, `#funding`, `#DeepSeek`, `#valuation`, `#startup`

---

<a id="item-4"></a>
## [中国黑客克隆英伟达 Tesla V100 GPU](https://www.reddit.com/r/LocalLLaMA/comments/1ucokod/chinese_hackers_latest_masterpiece_with_nvidia/) ⭐️ 9.0/10

中国黑客逆向工程了英伟达的 Tesla V100 GPU，制造出名为 Tesla V100 v4 的完全功能克隆版本，支持完整的 NVLink，并以低价出售。 这一突破大幅降低了高性能 AI 硬件的成本，使个人和小型实验室能够获得 Tesla V100 级别的算力，可能颠覆 GPU 市场。 该克隆版本支持最多 8 路 NVLink，提供 16GB 和 32GB 版本，售价分别为 220 美元和 590 美元，并附带 3 年质保。

reddit · r/LocalLLaMA · /u/General_Vermicelli53 · 6月22日 15:58

**背景**: Tesla V100 是 2017 年发布的服务器 GPU，专为 AI 和高性能计算设计，拥有 2963 个引脚，并通过 NVLink 实现高速多 GPU 通信。逆向工程如此复杂的芯片极其困难，需要深厚的硬件和信号分析专业知识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reddit.com/r/LocalLLaMA/comments/1ucokod/chinese_hackers_latest_masterpiece_with_nvidia/">Chinese Hackers Latest Masterpiece with NVIDIA : r/LocalLLaMA - Reddit</a></li>
<li><a href="https://en.wikipedia.org/wiki/NVLink">NVLink - Wikipedia</a></li>
<li><a href="https://habr.com/ru/articles/1030918/">Обзор серверного ускорителя NVIDIA Tesla V 100 16 Gb... / Хабр</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区高度关注，许多用户对这一技术成就表示惊叹，并讨论克隆版本的合法性和可靠性。有人质疑这是否是真正的逆向工程还是重新贴牌的现有显卡，但详细的引脚分析和 NVLink 支持获得了广泛赞誉。

**标签**: `#hardware`, `#reverse-engineering`, `#NVIDIA`, `#GPU`, `#AI`

---

<a id="item-5"></a>
## [OpenMontage：首个开源智能视频制作系统](https://github.com/calesthio/OpenMontage) ⭐️ 8.0/10

OpenMontage，全球首个开源智能视频制作系统，已在 GitHub 上发布，包含 12 条流水线、52 个工具和 500 多项智能体技能。它可以将 AI 编程助手转变为完整的视频制作工作室。 该项目通过免费提供先进的 AI 驱动工具，使专业视频制作民主化，可能颠覆内容创作行业。它使开发者和创作者无需传统编辑专业知识即可制作高质量视频。 该系统包含 12 条制作流水线，用于解说视频、虚拟主播、屏幕演示、电影预告片、动画、播客、本地化和纪录片蒙太奇等。它集成了 52 个工具，涵盖视频生成、图像创建、文本转语音等。

github_trending · GitHub Trending · 6月23日 03:51

**背景**: 智能视频制作指的是使用多个专门智能体自主规划、执行和编辑视频项目的 AI 系统。这种方法类似于 Cursor 对编程的革新，旨在通过将制作时间从几天缩短到几分钟，大幅增加高质量视频内容的供应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/calesthio/OpenMontage">GitHub - calesthio/OpenMontage: World's first open-source, agentic video production system. 12 pipelines, 52 tools, 500+ agent skills. Turn your AI coding assistant into a full video production studio. · GitHub</a></li>
<li><a href="https://a16z.com/its-time-for-agentic-video-editing/">It's time for agentic video editing | Andreessen Horowitz</a></li>

</ul>
</details>

**标签**: `#open-source`, `#video production`, `#AI agents`, `#Python`, `#content creation`

---

<a id="item-6"></a>
## [817 项 AI 代理网络安全技能，映射至六大框架](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10

GitHub 仓库 mukul975/Anthropic-Cybersecurity-Skills 发布，为 AI 代理提供 817 项结构化网络安全技能，映射至 MITRE ATT&CK 和 NIST CSF 2.0 等六大框架，并兼容 20 多个平台。 该仓库标准化了 AI 代理理解和执行网络安全任务的方式，实现了 Claude Code 和 GitHub Copilot 等工具间的互操作性，加速了 AI 在安全运维中的应用。 这些技能涵盖 29 个安全领域，并遵循 agentskills.io 开放标准，支持跨平台移植。该仓库单日获得超过 956 颗星，总星数达 18,853 颗。

github_trending · GitHub Trending · 6月23日 03:51

**背景**: MITRE ATT&CK 是一个全球可访问的对手战术和技术知识库，而 NIST CSF 2.0 提供了管理网络安全风险的框架。agentskills.io 标准定义了 AI 代理能力的可移植格式，使技能可在不同 AI 平台间复用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://attack.mitre.org/">MITRE ATT&CK®</a></li>
<li><a href="https://www.nist.gov/cyberframework">Cybersecurity Framework | NIST</a></li>
<li><a href="https://github.com/agentskills/agentskills">GitHub - agentskills/agentskills: Specification and documentation for Agent Skills · GitHub</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI agents`, `#MITRE ATT&CK`, `#NIST CSF`, `#open source`

---

<a id="item-7"></a>
## [趣味机器人学习提升技能获取](https://huggingface.co/papers/2606.19419) ⭐️ 8.0/10

研究人员提出了趣味自主机器人学习（Playful Agentic Robot Learning），其中具身编码代理通过自主探索和自导式玩耍来学习可复用技能，而无需任何下游任务指令，并引入了 RATs（机器人代理团队）用于玩耍期间的技能获取。 该方法使机器人无需显式任务监督即可构建可复用的技能库，显著提升下游任务性能（最高提升 20.6 个百分点），并能无需微调即可迁移到新代理，推动了具身 AI 和自主机器人学习的发展。 RATs 系统提出新颖的探索性任务，规划并执行机器人代码策略，验证进展，诊断失败，并将成功执行提炼为持久的代码技能库。在 LIBERO-PRO 和 MolmoSpaces 上的实验显示，相比 CaP-Agent0 分别提升了 20.6 和 17.0 个百分点，且学到的技能无需微调即可使 RoboSuite 和真实世界迁移分别提升 8.9 和 8.8 个百分点。

huggingface_papers · Hugging Face Papers · 6月19日 00:00

**背景**: 当前的自主机器人系统可以编写可执行的代码即策略（Code-as-Policy）程序并修正行为，但它们是任务驱动的，只有在收到明确指令后才能获取可复用技能。趣味自主机器人学习在任务到来之前引入了一个自导式玩耍阶段，使机器人能够自主探索和学习技能，类似于动物通过玩耍学习的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.19419">[2606.19419] Playful Agentic Robot Learning</a></li>
<li><a href="https://huggingface.co/papers/2606.19419">Paper page - Playful Agentic Robot Learning</a></li>
<li><a href="https://github.com/Playful-RATs/rats">Playful -RATs/RATs: Implementation of paper " Playful Agentic Robot ..."</a></li>

</ul>
</details>

**标签**: `#robot learning`, `#embodied AI`, `#skill acquisition`, `#reinforcement learning`, `#agentic systems`

---

<a id="item-8"></a>
## [S-Agent：利用空间工具实现连续 3D 推理](https://huggingface.co/papers/2606.20515) ⭐️ 8.0/10

研究人员提出 S-Agent，这是一个空间推理框架，通过时间记忆和分层空间工具增强视觉语言模型（VLM），使其能够从多视角图像中持续理解 3D 世界。 这项工作解决了现有 VLM 的关键局限——静态、无状态推理——通过实现时空证据积累，这对机器人、自动驾驶和增强现实等真实世界空间智能应用至关重要。 S-Agent 将 VLM 用作语义规划器，使用分层空间工具进行 2D 到 3D 的定位，并通过两个记忆模块（场景记忆和智能体记忆）跨帧整合证据。在 S-300K 轨迹上微调的 S-Agent-8B 模型，性能可与 GPT-5.4 和 Gemini 3 等闭源模型相媲美。

huggingface_papers · Hugging Face Papers · 6月19日 00:00

**背景**: 视觉语言模型（VLM）通常独立处理单张图像或帧，缺乏在时间和 3D 空间中进行推理的能力。AI 中的空间推理需要理解连续 3D 环境中物体的位置、方向和关系。S-Agent 引入时间记忆和分层工具来克服这些限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Ropedia/S-Agent">GitHub - Ropedia/S-Agent: S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2603.25411">[2603.25411] HiSpatial: Taming Hierarchical 3D Spatial ... HiSpatial: Taming Hierarchical 3D Spatial Understanding in ... HiSpatial: Taming Hierarchical 3D Spatial Understanding in ... [2511.22961] HMR3D: Hierarchical Multimodal Representation ... HiSpatial: Taming Hierarchical 3D Spatial Understanding in ... HiSpatial: Taming Hierarchical 3D Spatial Understanding in ... CVPR Poster HiSpatial: Taming Hierarchical 3D Spatial ...</a></li>

</ul>
</details>

**标签**: `#spatial reasoning`, `#visual language models`, `#3D understanding`, `#tool-augmented agents`, `#multi-view imagery`

---

<a id="item-9"></a>
## [Mitchell Hashimoto 向 Zig 软件基金会承诺捐款 40 万美元](https://mitchellh.com/writing/zig-donation-2026) ⭐️ 8.0/10

Ghostty 终端模拟器的创建者 Mitchell Hashimoto 承诺向 Zig 软件基金会 (ZSF) 额外捐款 40 万美元，以支持 Zig 编程语言的发展。 这笔巨额捐款凸显了业界对 Zig 作为有前途的系统编程语言的信心日益增强，并为其开源开发提供了关键资金，可能加速其采用和生态系统发展。 此次承诺使 Hashimoto 对 ZSF 的总捐款超过 100 万美元，他强调 Zig 的独特理念，包括拒绝接受 LLM 生成的贡献，这与该语言注重精心设计的理念一致。

hackernews · tosh · 6月22日 13:43 · [社区讨论](https://news.ycombinator.com/item?id=48630020)

**背景**: Zig 是一种通用系统编程语言，旨在改进 C 语言，专注于健壮性、最优性和可重用性。Zig 软件基金会成立于 2020 年，是一个非营利组织，通过捐款和赞助支持该语言的发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language) - Wikipedia</a></li>
<li><a href="https://ziglang.org/zsf/">Zig Software Foundation ⚡ Zig Programming Language</a></li>
<li><a href="https://ziglang.org/">Home ⚡ Zig Programming Language</a></li>

</ul>
</details>

**社区讨论**: 社区称赞了 Hashimoto 的慷慨及其对 Zig 理念的反思，一些人指出 Ghostty 本身已成为一项重要贡献。其他人推荐观看 Zig 创建者的采访以了解该语言的设计原则，并且讨论了 Zig 关于 LLM 贡献的政策。

**标签**: `#Zig`, `#open-source`, `#donation`, `#programming-languages`, `#community`

---

<a id="item-10"></a>
## [8087 协处理器快速位移位器的芯片分析](https://www.righto.com/2020/05/die-analysis-of-8087-math-coprocessors.html) ⭐️ 8.0/10

对 Intel 8087 数学协处理器的详细芯片分析揭示了一种独特的两级桶形移位器设计，先移位位再移位字节，优化了早期浮点硬件的速度和面积。 该分析深入揭示了早期 FPU 设计中的工程权衡，展示了时代限制如何催生出巧妙的电路创新，对理解现代硬件演进仍有参考价值。 该桶形移位器采用两级方法：先在字节内可变位移位，再按整字节移位，相比全桶形移位器降低了复杂度。设计通过自定义布局直接将移位量映射到控制信号，避免了单独的译码器。

hackernews · Jimmc414 · 6月22日 13:40 · [社区讨论](https://news.ycombinator.com/item?id=48629982)

**背景**: Intel 8087 于 1980 年发布，是首款用于 8086/8088 处理器的浮点协处理器，为浮点运算提供硬件支持。桶形移位器是一种组合电路，可在单个时钟周期内将数据字移位可变位数，对于浮点运算中的尾数对齐至关重要。8087 的移位器在严格的面积和功耗限制下设计，产生了创新的权衡方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Barrel_shifter">Barrel shifter</a></li>
<li><a href="https://en.wikipedia.org/wiki/Intel_8087">Intel 8087 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Floating-point_unit">Floating - point unit - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对 8087 与现代硬件之间的性能成本对比感到惊叹，指出性能提升了 1000 万倍。有人质疑为何移位器不采用 log2 结构，文章中的两级设计被认为是一种巧妙的折中。其他人分享了相关的历史 FPU 设计，如使用 BCD 算术的 Northstar S-100 卡。

**标签**: `#hardware`, `#reverse engineering`, `#retrocomputing`, `#FPU`, `#chip design`

---

<a id="item-11"></a>
## [Claude Code 的“扩展思考”输出是有损摘要](https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic/) ⭐️ 8.0/10

一项分析揭示，Claude Code 的“扩展思考”模式中显示的文本并非模型的实际推理过程，而是一个有损摘要，这意味着它会遗漏细节，并且可能无法忠实反映内部思考过程。 这种缺乏透明度的情况引发了安全性和信任方面的担忧，因为隐藏的推理过程可能让攻击者注入恶意指令而不被发现，同时也使用户的提示优化变得更加困难。 这种有损摘要类似于将无损的 BMP 图像转换为有损的 JPEG 再转换回来，导致数据丢失。此外，在隐藏阶段交错进行推理和函数调用可能导致数据泄露。

hackernews · 0o_MrPatrick_o0 · 6月22日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=48630535)

**背景**: 扩展思考是 Claude 的一项功能，允许模型在生成最终答案之前进行逐步推理。然而，展示给用户的输出是推理过程的压缩版本，而非原始的思维链。这种做法在 OpenAI 和 Google 等主要 AI 公司中很常见，它们隐藏模型的实际推理过程以保护专有研发成果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/extended-thinking">Extended thinking - Claude API Docs</a></li>
<li><a href="https://gist.github.com/intellectronica/58571dda3581eec3e17a77741e8c858a">Claude Extended Thinking: The Ultimate Guide · GitHub</a></li>
<li><a href="https://medium.com/@cognidownunder/claude-code-and-extended-thinking-the-hybrid-reasoning-revolution-thats-changing-how-we-code-4c59cb714015">Claude Code and Extended Thinking : The Hybrid Reasoning Revolution That’s Changing How We Code | by Cogni Down Under | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，这并非 Anthropic 独有，OpenAI 和 Google 也隐藏推理过程。一些用户因安全风险和提示优化困难而拒绝使用隐藏推理的模型。其他人则指出，即使原始推理过程可用，它也可能无法忠实反映实际思考。

**标签**: `#AI transparency`, `#reasoning models`, `#security`, `#Anthropic`, `#Claude`

---

<a id="item-12"></a>
## [Linux Secure Boot 证书将于 2025 年到期](https://lwn.net/Articles/1029767/) ⭐️ 8.0/10

依赖微软密钥的 Linux Secure Boot 证书将于 2025 年到期，用户需要通过 fwupd 更新固件，以避免启动失败。 此到期影响所有启用 Secure Boot 的 Linux 用户，若不处理可能导致系统无法启动，因此是一个关键的安全和系统管理问题。 fwupd 守护进程可以自动更新证书，但用户可能需要检查当前证书状态，并确保有足够的 EFI 变量空间来执行更新。

hackernews · weaksauce · 6月22日 18:24 · [社区讨论](https://news.ycombinator.com/item?id=48633941)

**背景**: Secure Boot 是 UEFI 的一项功能，确保只执行经过签名的引导加载程序和内核，防止恶意软件劫持启动过程。Linux 发行版通常使用微软签名的 shim 来启动，而该 shim 的签名证书将于 2025 年到期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lwn.net/Articles/1029767/">Linux and Secure Boot certificate expiration - LWN.net</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fwupd">Fwupd</a></li>
<li><a href="https://www.reddit.com/r/linux/comments/1m69s94/linux_and_secure_boot_certificate_expiration/">Linux and Secure Boot certificate expiration - Reddit</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出缺乏检查证书状态的明确指南，一些用户建议手动注册密钥作为替代方案。其他人则提到 fwupd 更新的高成功率（98-99%），以及像修改 shim 这样的变通方法过于复杂。

**标签**: `#Linux`, `#Secure Boot`, `#firmware`, `#security`, `#system administration`

---

<a id="item-13"></a>
## [Codex 日志漏洞可能导致本地 SSD 写入数 TB 数据](https://github.com/openai/codex/issues/28224) ⭐️ 8.0/10

OpenAI 的 Codex CLI 和 App 存在一个日志漏洞，可能将数 TB 的诊断日志写入本地 SQLite 数据库，从而耗尽磁盘空间并损坏 SSD。OpenAI 已在 CLI 和 Codex App 的更新中发布了修复。 该漏洞可能导致严重的 SSD 磨损，对于重度用户可能将驱动器寿命缩短至一年以内，并可能导致数据丢失或系统不稳定。这凸显了广泛使用的 AI 开发工具中的质量问题。 该漏洞将日志写入 ~/.codex/logs_2.sqlite 的 SQLite 数据库，有用户报告一个 27GB 的文件在运行 VACUUM FULL 后缩小至 73MB。临时解决方法包括创建一个触发器来阻止日志插入。

hackernews · vantareed · 6月22日 07:30 · [社区讨论](https://news.ycombinator.com/item?id=48626930)

**背景**: OpenAI Codex 是一个 AI 编码代理，可自动化软件工程任务。该漏洞源于配置错误的日志接收器，写入过多的诊断数据，可能达到每年 640 TB 的写入量，远超典型 SSD 的耐久度评级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.developersdigest.tech/blog/codex-sqlite-logging-bug-ssd-wear">Codex Logging Bug Can Write Terabytes to Your SSD - Developers Digest</a></li>
<li><a href="https://www.reddit.com/r/OpenAI/comments/1ucf4px/openai_codex_has_a_bug_that_could_kill_your_ssd/">r/OpenAI on Reddit: OpenAI Codex has a bug that could kill your SSD in under a year</a></li>

</ul>
</details>

**社区讨论**: 社区评论对该漏洞的严重性和 OpenAI 最初的沉默表示不满，有人称 Codex 为“垃圾软件”。一位 OpenAI 工程师确认了修复，用户分享了 SQLite 触发器和 VACUUM FULL 等解决方法。

**标签**: `#AI tools`, `#bug report`, `#OpenAI`, `#Codex`, `#data loss`

---

<a id="item-14"></a>
## [AI 安全不仅仅是带 AI 的网络安全](https://www.latent.space/p/gray-swan) ⭐️ 8.0/10

OpenAI 董事会成员 Zico Kolter 与 Gray Swan CEO Matt Fredrikson 讨论了为何 AI 安全从根本上不同于传统网络安全，并强调了 AI 系统红队测试所面临的独特挑战。 这场对话为 AI 治理和安全实践提供了关键见解，因为 AI 系统引入了提示注入和越狱等新型攻击面，传统网络安全方法无法应对。 Gray Swan AI 是一个对抗性评估平台，被领先的前沿实验室用于在公开发布前识别 LLM 中的漏洞，重点关注越狱、提示注入和有害输出。

rss · Latent Space · 6月22日 21:06

**背景**: 红队测试起源于 20 世纪 60 年代，是一种由团队模拟对手来测试组织防御能力的实践。AI 红队测试将其扩展到 AI 特有的漏洞，如指令层次结构利用和工具滥用，需要超越传统攻击向量的创造性探索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Red_teaming">Red teaming</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gray_Swan_AI">Gray Swan AI</a></li>
<li><a href="https://www.grayswan.ai/">Gray Swan - Enterprise Security for AI-Powered Applications</a></li>

</ul>
</details>

**标签**: `#AI security`, `#red-teaming`, `#AI safety`, `#cybersecurity`, `#LLM`

---

<a id="item-15"></a>
## [微软开源 FastContext，助力 LLM 编码代理](https://www.reddit.com/r/LocalLLaMA/comments/1ud1lro/why_is_no_one_talking_about_microsofts_open/) ⭐️ 8.0/10

微软开源了 FastContext，这是一个轻量级的仓库探索子代理，它将仓库探索与任务解决分离，在 SWE-bench 基准测试上实现了高达 60% 的 token 节省和准确率提升。 该发布通过引入专门的子代理提供聚焦上下文，解决了编码代理中一个关键的低效问题——在完整仓库扫描上浪费 token——从而可能降低使用基于 LLM 的编码工具的开发者的成本并提升性能。 FastContext 有两个版本：4B SFT 模型和 4B RL 模型，其中 RL 版本在某些任务上以更少的 token 超越了更大的 30B SFT 探索器。最大 token 节省达到 60.3%（GPT-5.4 在 SWE-QA 上），在 SWE-bench Pro 上的准确率提升高达 +5.5 个百分点。

reddit · r/LocalLLaMA · /u/formatme · 6月23日 00:11

**背景**: LLM 编码代理通常使用单个模型同时处理仓库探索和任务解决，这可能导致 token 效率低下。FastContext 引入了一种子代理架构，按需调用轻量级模型执行并行只读操作（READ、GLOB、GREP），并返回紧凑的文件路径和行范围，从而减少主代理的 token 使用量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/microsoft/FastContext-1.0-4B-SFT">microsoft/FastContext-1.0-4B-SFT · Hugging Face</a></li>
<li><a href="https://arxiv.org/html/2606.14066v1">FastContext: Training Efficient Repository Explorer for Coding Agents</a></li>
<li><a href="https://www.swebench.com/">SWE-bench Leaderboards</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对 FastContext 的潜力表示兴奋，一些用户指出它与其他方法（如 Cognition 的 SWE-1.6）相似。还有关于将 FastContext 本地集成到 oh-my-pi 等工具中的讨论，显示出对实际应用的浓厚兴趣。

**标签**: `#LLM`, `#coding agents`, `#open source`, `#Microsoft`, `#SWE-bench`

---