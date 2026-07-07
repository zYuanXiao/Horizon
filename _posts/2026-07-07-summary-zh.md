---
layout: default
title: "Horizon Summary: 2026-07-07 (ZH)"
date: 2026-07-07
lang: zh
---

> 从 128 条内容中筛选出 15 条重要资讯。

---

1. [Januscape：KVM/x86 严重虚拟机逃逸漏洞](#item-1) ⭐️ 9.0/10
2. [Addy Osmani 的 Agent Skills：面向 AI 编码的生产级技能](#item-2) ⭐️ 8.0/10
3. [阿里巴巴 Page-Agent：自然语言控制网页界面](#item-3) ⭐️ 8.0/10
4. [面向 LLM 强化学习的单调推理策略改进](#item-4) ⭐️ 8.0/10
5. [程序即权重：将模糊函数编译为神经工件](#item-5) ⭐️ 8.0/10
6. [Kani：Rust 的位精确模型检查器](#item-6) ⭐️ 8.0/10
7. [Pulpie：20 倍低成本的网页内容提取模型](#item-7) ⭐️ 8.0/10
8. [腾讯发布 Hy3：295B 参数 MoE 模型，采用 Apache 2.0 许可](#item-8) ⭐️ 8.0/10
9. [秘密 Claude 追踪器与 Anthropic 反监控立场矛盾](#item-9) ⭐️ 8.0/10
10. [Kyutai 的 Pocket TTS 从 5 秒音频克隆声音，在 CPU 上运行](#item-10) ⭐️ 8.0/10
11. [Sberbank 发布 GigaChat3.5-432B-A28B MoE 模型，首日支持 GGUF](#item-11) ⭐️ 8.0/10
12. [OpenComputer：为 AI 智能体打造的开源虚拟机](#item-12) ⭐️ 8.0/10
13. [Ascent GX10 运行剪枝后的 162B DeepSeek 模型，上下文达 262k](#item-13) ⭐️ 8.0/10
14. [Krea 2 节点实现多 LoRA 与边界框控制](#item-14) ⭐️ 8.0/10
15. [LingBot-Vision：用于自监督学习的掩码边界建模](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Januscape：KVM/x86 严重虚拟机逃逸漏洞](https://github.com/V4bel/Januscape) ⭐️ 9.0/10

KVM/x86 的影子 MMU 模拟中存在一个释放后使用漏洞（编号 CVE-2026-53359），允许客户虚拟机在 Intel 和 AMD 系统上逃逸到宿主机。目前 PoC 利用代码已公开，但完整的逃逸利用代码暂未发布。 该漏洞对多租户 VM 提供商和沙箱环境构成严重威胁，攻击者可突破客户虚拟机获得宿主机级访问权限。这是继 arm64 逃逸漏洞（ITScape）之后首个公开演示的 KVM/x86 虚拟机逃逸漏洞。 该漏洞自 2008 年就已存在，影响 Intel 和 AMD x86 宿主机。在宿主机操作系统或 BIOS 中禁用嵌套虚拟化可使系统免受此漏洞影响。

hackernews · Imustaskforhelp · 7月6日 17:35 · [社区讨论](https://news.ycombinator.com/item?id=48807908)

**背景**: KVM（基于内核的虚拟机）是 Linux 内核模块，可将宿主机转变为虚拟机监控器，支持运行多个虚拟机。影子 MMU 用于在硬件辅助分页（如 Intel EPT、AMD NPT）不可用或禁用时进行内存虚拟化。嵌套虚拟化允许虚拟机内部运行自己的虚拟机监控器和更多虚拟机，增加了复杂性和攻击面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html">16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems</a></li>
<li><a href="https://lobste.rs/s/jea4xl/januscape_guest_host_escape_kvm_x86">Januscape: Guest-to-Host Escape in KVM/x86 | Lobsters</a></li>
<li><a href="https://lowendtalk.com/discussion/218905/januscape-guest-to-host-escape-in-kvm-x86-cve-2026-53359">Januscape: Guest-to-Host Escape in KVM/x86 (CVE-2026-53359) — LowEndTalk</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，嵌套虚拟化增加了显著的复杂性和历史上的不稳定性，不建议在公共 VM 宿主机上启用。有人质疑为什么在 RHEL 等发行版中 /dev/kvm 是全局可写的，从而允许无特权的本地权限提升。其他人确认禁用嵌套虚拟化可缓解此漏洞。

**标签**: `#security`, `#virtualization`, `#KVM`, `#CVE`, `#x86`

---

<a id="item-2"></a>
## [Addy Osmani 的 Agent Skills：面向 AI 编码的生产级技能](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

Addy Osmani 发布了一个名为 agent-skills 的开源仓库，其中包含 20 个精心策划的生产级工程技能，旨在增强 AI 编码代理的能力。该仓库单日获得超过 1,112 颗星，总星数超过 70,000。 该仓库通过提供结构化的最佳实践工作流，指导 AI 编码代理生成更高质量的代码，满足了 AI 辅助软件工程中的关键需求。它有可能显著提高 AI 编码工具的可靠性和有效性，使在开发流程中采用 AI 的开发者和团队受益。 这些技能涵盖核心工程、AI/ML/数据以及专业工具等领域，编码了高级工程师使用的工作流、质量门禁和最佳实践。该仓库使用 JavaScript 编写，并在 GitHub 上以 MIT 许可证提供。

github_trending · GitHub Trending · 7月7日 03:30

**背景**: AI 编码代理（如 Cursor 和 Zencoder）是帮助开发者生成、审查和调试代码的工具。然而，如果没有适当的指导，这些代理可能会生成缺乏生产级质量的代码。Agent Skills 旨在通过提供可重用的专家级技能库来填补这一空白，使代理能够遵循行业最佳实践。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/addyosmani/agent-skills">GitHub - addyosmani/agent- skills : Production - grade engineering ...</a></li>
<li><a href="https://www.everydev.ai/tools/addy-osmani-agent-skills">Addy Osmani Agent Skills - Skill Library by Addy Osmani | EveryDev.ai</a></li>

</ul>
</details>

**标签**: `#AI`, `#coding agents`, `#software engineering`, `#GitHub trending`

---

<a id="item-3"></a>
## [阿里巴巴 Page-Agent：自然语言控制网页界面](https://github.com/alibaba/page-agent) ⭐️ 8.0/10

阿里巴巴开源了 Page-Agent，这是一个 TypeScript 库，允许用户使用自然语言命令控制网页界面，在 GitHub 上单日获得 892 颗星。 该工具通过允许非技术用户使用自然语言与网站交互，使网页自动化变得大众化，可能改变企业构建 AI 原生 Web 应用的方式。 Page-Agent 是一个页面内 GUI 代理，可通过单个 script 标签或 npm 包集成，支持通过 Chrome 扩展进行多页面浏览和浏览器控制。

github_trending · GitHub Trending · 7月7日 03:31

**背景**: 传统的 GUI 自动化需要脚本或编程知识。Page-Agent 利用 AI 解释自然语言，直接在浏览器中执行点击、填写表单和导航等操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/alibaba/page-agent">GitHub - alibaba/page- agent : JavaScript in - page GUI agent .</a></li>
<li><a href="https://alibaba.github.io/page-agent/">PageAgent - The GUI Agent Living in Your Webpage</a></li>
<li><a href="https://emelia.io/hub/page-agent-alibaba">Page - Agent : Alibaba 's Open Source AI Web Copilot</a></li>

</ul>
</details>

**标签**: `#GUI automation`, `#natural language`, `#TypeScript`, `#web agent`, `#open source`

---

<a id="item-4"></a>
## [面向 LLM 强化学习的单调推理策略改进](https://huggingface.co/papers/2606.29526) ⭐️ 8.0/10

研究人员提出了单调推理策略改进（MIPI），这是一种用于大语言模型强化学习的新目标，确保训练期间的策略改进能够迁移到推理阶段，从而解决训练-推理不匹配问题。 这项工作解决了 LLM 强化学习微调中的一个根本性不稳定问题，对于像聊天和代码生成中使用的推理模型的可靠部署至关重要。 该框架——单调推理策略更新（MIPU）采用两步过程：构建采样器引用的候选更新，并基于推理侧差距代理选择性地接受它们。实验表明，在高不匹配条件下，推理性能和训练稳定性均得到提升。

huggingface_papers · Hugging Face Papers · 7月6日 00:00

**背景**: 强化学习（RL）用于微调大语言模型（LLM）以执行推理等任务。然而，LLM 通常使用独立的训练和推理引擎，导致即使模型参数相同，概率分布也不一致——这种现象称为训练-推理不匹配。这种不匹配引入了离策略性，可能破坏训练稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/papers/2606.29526">Paper page - The Mirage of Optimizing Training Policies : Monotonic ...</a></li>
<li><a href="https://arxiv.org/pdf/2606.29526">The Mirage of Optimizing Training Policies : Monotonic Inference ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#reinforcement learning`, `#policy optimization`, `#training stability`

---

<a id="item-5"></a>
## [程序即权重：将模糊函数编译为神经工件](https://huggingface.co/papers/2607.02512) ⭐️ 8.0/10

研究人员提出模糊函数编程，实例化为程序即权重（PAW），其中在 FuzzyBench 上训练的 4B 编译器为冻结的 0.6B 解释器生成参数高效适配器，使得自然语言定义的函数可以本地执行。 PAW 在性能上匹配 32B 模型，同时仅使用 1/50 的推理内存，并在 MacBook M3 上以 30 tokens/s 运行，这为之前需要大型 API 调用的任务提供了高效的本地 AI 部署可能。 编译器是一个 4B 模型，为冻结的 0.6B Qwen3 解释器生成类似 LoRA 的适配器，FuzzyBench 数据集包含 1000 万个训练样本。该范式将基础模型重新定位为工具构建者，而非逐个输入的问题解决者。

huggingface_papers · Hugging Face Papers · 7月3日 00:00

**背景**: 许多编程任务（如日志过滤或排序）难以用精确规则指定，通常外包给大型语言模型 API，这带来了延迟、成本和可重复性问题。模糊函数编程旨在将自然语言规范编译为本地运行的紧凑神经工件，结合了 LLM 的灵活性和传统程序的效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.02512">[2607.02512] Program-as-Weights: A Programming Paradigm for Fuzzy Functions</a></li>
<li><a href="https://huggingface.co/papers/2607.02512">Paper page - Program-as-Weights: A Programming Paradigm for Fuzzy Functions</a></li>

</ul>
</details>

**标签**: `#programming paradigms`, `#neural compilation`, `#efficient inference`, `#NLP`, `#parameter-efficient fine-tuning`

---

<a id="item-6"></a>
## [Kani：Rust 的位精确模型检查器](https://arxiv.org/abs/2607.01504) ⭐️ 8.0/10

Kani（一个用于 Rust 程序的开源位精确模型检查器）发布了新的论文和教程。 Kani 帮助 Rust 开发者自动验证安全性和正确性属性，减少关键软件中的未定义行为和错误。 Kani 使用 CBMC 作为后端，支持检查 panic、溢出和其他安全违规。教程提供了实用的入门示例。

hackernews · Jimmc414 · 7月6日 15:53 · [社区讨论](https://news.ycombinator.com/item?id=48806410)

**背景**: 模型检查是一种形式化验证技术，通过穷举程序状态来验证属性。位精确模型检查在比特级别操作，能够精确推理整数运算和内存操作。Rust 的安全保证使其成为此类验证工具的自然目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://model-checking.github.io/kani/">Getting started - The Kani Rust Verifier</a></li>
<li><a href="https://github.com/model-checking/kani">GitHub - model - checking / kani : Kani Rust Verifier · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了教程的实用性，并将其与 hypothesis-auto 等类似工具进行比较。对先前工作和相关工具的引用表明对 Rust 验证的积极兴趣。

**标签**: `#Rust`, `#model checking`, `#formal verification`, `#software engineering`

---

<a id="item-7"></a>
## [Pulpie：20 倍低成本的网页内容提取模型](https://usefeyn.com/blog/pulpie-pareto-optimal-models-for-cleaning-the-web/) ⭐️ 8.0/10

Feyn 推出了 Pulpie，这是一系列帕累托最优的编码器模型，能够从原始 HTML 中去除样板内容，以 20 倍更低的成本达到最先进的提取质量。使用 Pulpie 清洗 10 亿个网页的成本为 7,900 美元，而使用 Dripper 则需要 159,000 美元。 这使得大规模 AI 训练和数据管道能够负担得起高质量的网页内容提取，降低了主要的成本障碍。编码器架构的转变可能影响未来网页抓取和文档理解的设计。 Pulpie 模型是编码器，对整个输入 HTML 进行一次前向传播，并将每个块标记为样板或内容，而像 Dripper 这样的解码器则逐个 token 生成输出，使其受内存限制。Pulpie 受计算限制，使得具有相对更多计算能力的廉价 GPU 能够高效运行。

hackernews · snyy · 7月6日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=48806575)

**背景**: 网页内容提取，即去除样板内容，是通过移除广告、导航和其他非必要元素来隔离网页主要内容的任务。传统方法包括基于规则的库（如 Boilerpipe）和较新的基于解码器的神经模型。编码器模型并行处理整个输入，而解码器模型顺序生成输出，通常需要更多内存带宽。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pareto_efficiency">Pareto efficiency - Wikipedia</a></li>
<li><a href="https://mbottoni.github.io/2024/07/21/llm-archs.html">Encoder vs Decoder vs EncoderDecoder Architectures</a></li>
<li><a href="https://michaelmisiewicz.com/posts/scraping-webpages-2022/">How to scrape webpages in 2022 and best ways to remove boilerplate | Michael Misiewicz</a></li>

</ul>
</details>

**社区讨论**: 评论者对特定用例表现出兴趣，如电商产品抓取以及处理图片、表格和影子 DOM。有人指出 Hugging Face 演示在 Mozilla 和深色主题下存在界面问题，但总体情绪积极且对能力充满好奇。

**标签**: `#web scraping`, `#machine learning`, `#NLP`, `#cost efficiency`, `#open source`

---

<a id="item-8"></a>
## [腾讯发布 Hy3：295B 参数 MoE 模型，采用 Apache 2.0 许可](https://simonwillison.net/2026/Jul/6/hy3/#atom-everything) ⭐️ 8.0/10

腾讯发布了 Hy3，这是一个拥有 2950 亿参数的混合专家（MoE）模型，其中 210 亿参数处于激活状态，并采用宽松的 Apache 2.0 许可证。该模型性能优于同类尺寸模型，可与参数规模大 2-5 倍的主流开源模型相媲美。 Hy3 的强劲性能和 Apache 2.0 许可证使其成为开源 AI 生态系统的重要补充，可能加速研究和应用。其在 OpenRouter 上免费提供至 7 月 21 日，降低了开发者和研究人员尝试最先进模型的门槛。 全精度 Hy3 模型在 Hugging Face 上大小为 598GB，而 FP8 量化版本为 300GB。它支持 256K token 的上下文长度，并包含 38 亿个 MTP（多 token 预测）层参数。

rss · Simon Willison · 7月6日 23:57

**背景**: 混合专家（MoE）是一种神经网络架构，它使用多个专门的子网络（专家）和一个门控机制，对每个输入仅激活部分专家，从而在较低计算成本下实现大模型容量。多 token 预测（MTP）是一种训练技术，模型同时预测多个未来 token，以提高效率和性能。FP8 量化通过用 8 位浮点格式表示权重和激活值，减小模型大小和内存占用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://deepwiki.com/deepseek-ai/DeepSeek-V3/4.4-multi-token-prediction-(mtp)">Multi-Token Prediction ( MTP ) | deepseek-ai/DeepSeek-V3 | DeepWiki</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#LLM`, `#MoE`, `#Tencent`

---

<a id="item-9"></a>
## [秘密 Claude 追踪器与 Anthropic 反监控立场矛盾](https://arstechnica.com/tech-policy/2026/07/anthropic-outed-for-claude-tracker-that-secretly-monitored-chinese-users/) ⭐️ 8.0/10

Anthropic 被指控通过嵌入在 Claude Code 中的追踪器秘密监控中国用户，一名工程师确认这曾是一个实验，现已结束。 这一争议削弱了用户对 Anthropic 的信任，并对其隐私承诺及公开反对大规模监控的立场提出了严重质疑。 据 Anthropic 工程师 Thariq Shihipar 称，该追踪器于 2026 年 3 月作为实验被添加到 Claude Code 中，后被用户发现并在社交媒体上曝光。

rss · Ars Technica AI · 7月6日 16:44

**背景**: Anthropic 曾公开反对大规模监控，包括因监控担忧而拒绝五角大楼要求允许 Claude 用于“所有合法目的”。其 CEO Dario Amodei 曾表达对大规模国内监控和全自主武器的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/07/anthropic-outed-for-claude-tracker-that-secretly-monitored-chinese-users/">Secret Claude tracker shocks users after... - Ars Technica</a></li>
<li><a href="https://www.asapdrew.com/p/anthropic-ai-mass-surveillance">Anthropic 's "AI Mass Surveillance " Stand Doesn't Survive Scr...</a></li>
<li><a href="https://washingtonmonthly.com/2026/04/02/the-pentagons-orwellian-case-against-anthropic/">The Pentagon’s “Orwellian” Case Against Anthropic</a></li>

</ul>
</details>

**社区讨论**: 用户在社交媒体上表达了震惊和背叛感，许多人指责 Anthropic 虚伪。也有人为公司辩护，认为追踪器可能只是良性的使用量测量工具。

**标签**: `#privacy`, `#AI ethics`, `#surveillance`, `#Anthropic`, `#Claude`

---

<a id="item-10"></a>
## [Kyutai 的 Pocket TTS 从 5 秒音频克隆声音，在 CPU 上运行](https://www.reddit.com/r/LocalLLaMA/comments/1up07mk/kyutais_pocket_tts_clones_a_voice_from_5_seconds/) ⭐️ 8.0/10

Kyutai 发布了 Pocket TTS，这是一个约 1 亿参数的流式语言模型，通过 Mimi 神经编解码器生成音频令牌，可在 CPU 上仅凭 5 秒参考音频实现零样本声音克隆，采用 MIT 许可证。 这是首个支持零样本声音克隆的 CPU 友好型 TTS 模型，填补了 Kokoro 和 Supertonic 等其他模型仅提供固定音色的空白，非常适合交互式和隐私敏感型应用。 Pocket TTS 在不同文本长度下实现了平坦的实时因子 (RTF) 0.69–0.76，逐令牌流式生成音频，在基准测试中 UTMOS 得分为 4.10，但速度比某些替代方案慢。

reddit · r/LocalLLaMA · /u/gvij · 7月6日 15:14

**背景**: 传统 TTS 系统使用声学模型加声码器，而 Pocket TTS 采用自回归语言模型结合 Mimi 神经编解码器，该编解码器以 12.5 Hz 将语义和声学信息组合成令牌。RTF（实时因子）衡量生成一秒音频所需的计算时间，越低越好。UTMOS 是一种客观神经指标，用于预测语音质量的平均意见分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/kyutai/mimi">kyutai/ mimi · Hugging Face</a></li>
<li><a href="https://www.emergentmind.com/topics/utmos-score">UTMOS Score : Neural MOS Evaluation</a></li>
<li><a href="https://huggingface.co/datasets/Jarbas/ovos-tts-bench">Jarbas/ovos- tts -bench · Datasets at Hugging Face</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论强调了 Pocket TTS 架构的新颖性及其在 CPU 上独特的声音克隆能力，用户表示有兴趣在带口音的英语和非英语语音上测试它。一些人注意到其速度较慢，但一致认为它是该领域最有趣的模型。

**标签**: `#TTS`, `#voice cloning`, `#machine learning`, `#open source`, `#benchmark`

---

<a id="item-11"></a>
## [Sberbank 发布 GigaChat3.5-432B-A28B MoE 模型，首日支持 GGUF](https://www.reddit.com/r/LocalLLaMA/comments/1uotkm7/new_model_gigachat35432ba28b_with_day0_gguf/) ⭐️ 8.0/10

Sberbank 发布了 GigaChat3.5-432B-A28B，这是一个 4320 亿参数的混合专家（MoE）模型，并立即提供了 GGUF 量化支持，可通过 llama.cpp 进行本地推理。GGUF 版本已在 Hugging Face 上提供，并且已提交拉取请求以将支持集成到 llama.cpp 主分支中。 此次发布对本地 LLM 社区意义重大，因为它通过量化技术使得在消费级硬件上立即实验大型 MoE 模型成为可能。这展示了主要组织支持 llama.cpp 等开源本地推理生态系统的增长趋势。 该模型总参数量为 4320 亿，但由于 MoE 架构，每个 token 仅激活 280 亿参数，使其比同等规模的稠密模型更高效。GGUF 格式支持多种量化级别（例如 2 位到 8 位），以适应不同的硬件限制。

reddit · r/LocalLLaMA · /u/unbannedfornothing · 7月6日 10:34

**背景**: 混合专家（MoE）是一种模型架构，它将网络划分为多个“专家”，并使用门控机制为每个输入仅激活一部分专家，从而降低计算成本。GGUF 是一种用于存储量化模型权重的文件格式，针对使用 llama.cpp 进行推理进行了优化，llama.cpp 是一个流行的开源库，用于在 CPU 和 GPU 上本地运行 LLM。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@mne/explaining-the-mixture-of-experts-moe-architecture-in-simple-terms-85de9d19ea73">Explaining the Mixture-of-Experts ( MoE ) Architecture in... | Medium</a></li>
<li><a href="https://huggingface.co/docs/diffusers/quantization/gguf">GGUF · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>

</ul>
</details>

**标签**: `#LLM`, `#GGUF`, `#open-source`, `#MoE`, `#local-inference`

---

<a id="item-12"></a>
## [OpenComputer：为 AI 智能体打造的开源虚拟机](https://www.reddit.com/r/LocalLLaMA/comments/1up6swc/opencomputer_an_open_source_computer_built_for/) ⭐️ 8.0/10

AnythingLLM 团队发布了 OpenComputer，这是一个开源的隔离虚拟机环境，专为安全的 AI 智能体执行而设计，允许完全控制 PC 而不危及主机系统。 OpenComputer 通过在智能体自动化旁边提供人类可访问的界面，解决了智能体系统中的关键安全和用户体验差距，使强大的智能体能力对非技术用户变得实用。 基础镜像约为 3GB 的 Debian 13.5 和 XFCE4，每个智能体仅占用约 100MB，推理与虚拟机无关，支持本地、云端或服务器后端。它避免使用基于截图的导航，而是利用辅助功能树和 CLI。

reddit · r/LocalLLaMA · /u/tcarambat · 7月6日 19:01

**背景**: AI 智能体通常需要完全的系统访问权限来安装应用和操作 UI，这带来了安全风险。现有的解决方案如 Docker 沙箱或 Microsoft MXC 虽然隔离了智能体，但缺乏人性化的界面。OpenComputer 提供了一个完整的桌面环境，人类和智能体可以协作使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://anythingllm.com/">AnythingLLM | The all-in-one AI application for everyone</a></li>
<li><a href="https://lmstudio.ai/models/gemma-4">Gemma 4</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#open source`, `#VM isolation`, `#agent safety`, `#LLM`

---

<a id="item-13"></a>
## [Ascent GX10 运行剪枝后的 162B DeepSeek 模型，上下文达 262k](https://www.reddit.com/r/LocalLLaMA/comments/1up6t50/got_my_ascent_gx10_two_days_ago_ran_reappruned/) ⭐️ 8.0/10

一位用户在单个 Ascent GX10 Spark 上成功运行了经过 REAP 剪枝的 NVFP4 DeepSeek-V4-Flash 模型（162B 活跃参数），在高达 262k 上下文长度下实现了稳定的吞吐量。 这表明剪枝后的 MoE 模型可以在紧凑的桌面级 AI 超级计算机上高效运行，可能为研究和开发实现大规模 LLM 的本地部署。 该模型是 DeepSeek-V4-Flash 的 162B 参数变体，使用 REAP（路由器加权激活剪枝）进行剪枝，并量化到 NVFP4 精度。Ascent GX10 是一款基于 NVIDIA DGX Spark 的个人 AI 超级计算机，配备 GB10 Superchip 和 128GB LPDDR5x 内存。

reddit · r/LocalLLaMA · /u/Dry-Tough-8068 · 7月6日 19:01

**背景**: REAP 是一种剪枝技术，根据路由器权重和激活模式移除混合专家（MoE）模型中不太重要的专家，在保持性能的同时减小模型尺寸。NVFP4 是一种 4 位浮点精度格式，可进一步缩小模型体积。Ascent GX10 是一款桌面级 AI 超级计算机，专为本地推理和开发设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.candede.com/articles/advanced-llm-compression-reap/">Advanced LLM Compression: A Deep Dive into REAP</a></li>
<li><a href="https://www.localainews.co/news/multimodal/nemotron-3-nano-omni-30b-a3b-reasoning-nvfp4-opens-local-multimodal-ai/">Nemotron-3-Nano-Omni-30B-A3B-Reasoning- NVFP 4 Opens Local...</a></li>
<li><a href="https://www.amazon.ca/Supercomputer-Superchip-Supports-OpenClaw-Stackable/dp/B0G1MQYHRD/ref=zg_bs_g_677250011_d_sccl_24/134-7740804-6287904?psc=1">ASUS Ascent GX 10 AI Supercomputer, DGX Spark , NVIDIA GB10...</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区称赞了基准测试结果和自定义 Grafana 仪表板，一些用户讨论了剪枝与合并专家的权衡。其他人则对可复现性以及 Ascent GX10 在本地 LLM 工作中的潜力表示兴趣。

**标签**: `#hardware`, `#LLM inference`, `#pruning`, `#benchmarking`, `#long context`

---

<a id="item-14"></a>
## [Krea 2 节点实现多 LoRA 与边界框控制](https://www.reddit.com/r/StableDiffusion/comments/1uotykv/i_created_a_node_for_krea2_that_adds_multilora/) ⭐️ 8.0/10

一个名为 ComfyUI-Krea2-Regional-MultiLoRA 的 Krea 2 自定义节点，通过激活差值注入在空间上隔离 LoRA 效果，实现了多 LoRA 支持与逐区域边界框控制，防止身份泄露。 这解决了多角色图像生成中 LoRA 身份相互渗透的长期问题，实现了类似 Ideogram 4 的精确构图控制。用户可以在单个图像中放置多个角色、物体和背景，而不会出现身份混合。 该节点使用硬空间掩码（激活差值注入）而非注意力偏置，确保 LoRA 效果严格限制在其边界框内。它支持无限区域，自动将区域行与绘制的框同步，并且 fp8 安全，以 Krea 2 原生 CFG 1 运行。

reddit · r/StableDiffusion · /u/tekprodfx16 · 7月6日 10:55

**背景**: LoRA（低秩适应）是一种针对特定概念（如角色或风格）微调大模型的技术。在多 LoRA 生成中，当 LoRA 效果重叠时会出现身份泄露，导致面部融合或特征平均。Krea 2 是一个开源图像生成模型，通过其 Qwen3-VL 文本编码器支持边界框布局控制。Ideogram 4 引入了类似的逐元素边界框提示以实现精确构图。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/CliffNodes/Krea2-Multi-Character-Lora-Node-w-bounding-box-By-Fedor">GitHub - CliffNodes/ Krea 2 -Multi-Character-Lora-Node...</a></li>
<li><a href="https://happyin.space/image-generation/lora-identity-disentanglement-in-flux2-klein-9b/">LoRA Identity Disentanglement in... - Happyin Knowledge Space</a></li>
<li><a href="https://news.creeta.com/en/ideogram-4-json-layout-bounding-box-2026/">Ideogram 4 .0 JSON Layout & Bounding Box Control 2026</a></li>

</ul>
</details>

**标签**: `#Stable Diffusion`, `#LoRA`, `#Krea 2`, `#image generation`, `#AI art`

---

<a id="item-15"></a>
## [LingBot-Vision：用于自监督学习的掩码边界建模](https://www.reddit.com/r/MachineLearning/comments/1up4cjh/lingbotvision_masked_boundary_modeling_for/) ⭐️ 8.0/10

LingBot-Vision 提出了掩码边界建模方法，教师网络预测密集边界场并强制学生重建这些边界区域，在 1.1B 参数下 NYUv2 线性探测深度估计中达到 0.296 RMSE，优于 DINOv3-7B 的 0.309。 这项工作表明，明确引导自监督学习关注边界区域，可以在显著减少参数和数据的情况下获得最先进的密集预测性能，挑战了 DINOv3 等模型的规模假设。 该方法使用逐像素类别分布表示边界场以避免崩溃，并在监督前对解码片段进行 a-contrario 验证测试。蒸馏后的 ViT-L（0.3B）在 NYUv2 上达到 0.310 RMSE，与 DINOv3-7B 相当，但在 ImageNet 和 ADE20K 上落后。

reddit · r/MachineLearning · /u/StillThese3747 · 7月6日 17:37

**背景**: 视觉自监督学习（SSL）常使用掩码图像建模，模型学习重建被掩码的块。DINOv3 是一种领先的 SSL 方法，使用自蒸馏和中心化/锐化来防止崩溃。线性探测通过在冻结特征上训练线性分类器来评估表示质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2602.22701v1">BRepMAE: Self - Supervised Masked BRep Autoencoders for...</a></li>
<li><a href="https://deepwiki.com/nianticlabs/wavelet-monodepth/4.2-nyuv2-training-and-evaluation">NYUv 2 Training and Evaluation | DeepWiki</a></li>
<li><a href="https://arxiv.org/html/2603.14482">V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论内容充实，作者指出 0.013 RMSE 的差异在探测超参数变化范围内，且未与硬掩码基线（如 AttMask）进行消融实验。评论者还质疑边界强制是否与 DINOv3 中使用的 Gram 锚定互补。

**标签**: `#self-supervised learning`, `#computer vision`, `#pretraining`, `#boundary detection`, `#transformer`

---