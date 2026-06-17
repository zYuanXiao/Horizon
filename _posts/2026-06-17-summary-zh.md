---
layout: default
title: "Horizon Summary: 2026-06-17 (ZH)"
date: 2026-06-17
lang: zh
---

> 从 154 条内容中筛选出 15 条重要资讯。

---

1. [SpaceX 以 600 亿美元收购 Cursor](#item-1) ⭐️ 9.0/10
2. [Copilot 严重漏洞致黑客可窃取 2FA 验证码](#item-2) ⭐️ 9.0/10
3. [Nemotron 3 Ultra：混合 Mamba-Attention 的 MoE 模型，支持 100 万上下文](#item-3) ⭐️ 9.0/10
4. [Karpathy 的 autoresearch 项目自动化 nanochat 训练研究](#item-4) ⭐️ 8.0/10
5. [vLLM：高吞吐量 LLM 推理引擎在 GitHub 上趋势上升](#item-5) ⭐️ 8.0/10
6. [JoyAI-VL-Interaction：实时视觉语言交互 AI](#item-6) ⭐️ 8.0/10
7. [Qwen 发布机器人基础模型套件](#item-7) ⭐️ 8.0/10
8. [机械手表机制的互动深度解析](#item-8) ⭐️ 8.0/10
9. [Meta 正在摧毁其工程组织吗？](#item-9) ⭐️ 8.0/10
10. [将 ast.walk 提速 220 倍](#item-10) ⭐️ 8.0/10
11. [联邦对 Fable 5 的“修复代码”绕过方式感到震惊](#item-11) ⭐️ 8.0/10
12. [x86 模拟器团队在仿真中修复糟糕代码](#item-12) ⭐️ 8.0/10
13. [AI 模型出口管制损害美国网络防御](#item-13) ⭐️ 8.0/10
14. [五角大楼使用 AI 起草国会报告](#item-14) ⭐️ 8.0/10
15. [OpenAI 收入增长但仍亏损数十亿美元](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SpaceX 以 600 亿美元收购 Cursor](https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/) ⭐️ 9.0/10

SpaceX 已同意以 600 亿美元收购 AI 编程助手 Cursor 的开发商 Anysphere，这标志着科技行业最大规模的收购之一。 此次收购表明对 AI 辅助软件开发的巨大押注，可能改变 SpaceX 为火箭和航天器构建软件的方式，并可能重塑 AI 编程工具市场。 这笔交易对 Cursor 的估值约为 2014 年 Mojang（Minecraft）收购价的 20 倍，SpaceX 认为 AI 产品的潜在市场规模达 26 万亿美元，相当于美国 GDP。

hackernews · itsmarcelg · 6月16日 10:44 · [社区讨论](https://news.ycombinator.com/item?id=48553224)

**背景**: Cursor 是一款基于 Visual Studio Code 分支的 AI 驱动代码编辑器，由 2022 年成立的旧金山初创公司 Anysphere 开发。它提供代码生成、调试和重构等 AI 辅助功能。AI 辅助软件开发工具迅速流行，许多开发者采用它们来提高生产力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor ( code editor) - Wikipedia</a></li>
<li><a href="https://www.eesel.ai/blog/anysphere">What is Anysphere ? The company behind Cursor AI | eesel AI</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：有人质疑估值，将其与 Minecraft 25 亿美元的收购相比，也有人讨论 SpaceX 的战略契合度。一些用户已停止使用 Cursor，转而使用 Codex 等替代品，理由是弹出窗口烦人。

**标签**: `#acquisition`, `#AI coding`, `#SpaceX`, `#Cursor`, `#software engineering`

---

<a id="item-2"></a>
## [Copilot 严重漏洞致黑客可窃取 2FA 验证码](https://arstechnica.com/security/2026/06/critical-copilot-vulnerability-allowed-hackers-to-seal-2fa-code-from-users/) ⭐️ 9.0/10

Varonis 威胁实验室发现了 SearchLeak，这是 Microsoft 365 Copilot Enterprise 中的一个严重漏洞链，允许攻击者窃取包括 MFA 验证码和电子邮件在内的敏感数据。微软已于周二修复了这些漏洞。 该漏洞凸显了 LLM 安全方法的系统性失败，因为它可能危及数百万用户的双因素认证码。这强调了在广泛使用的 AI 工具中需要更强大的安全措施。 SearchLeak 串联了三个不同的弱点：参数到提示（P2P）注入、缺乏输出清理以及绕过 Copilot 的安全护栏。根据 M365 与环境的连接方式，影响范围可能进一步扩大。

rss · Ars Technica AI · 6月16日 11:15

**背景**: Microsoft 365 Copilot 是集成到 Microsoft 365 应用中的 AI 助手。像 Copilot 这样的 LLM 可能容易受到提示注入攻击，恶意输入会操纵模型的输出。双因素认证（2FA）码通常通过电子邮件或短信发送，用作额外的安全层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.varonis.com/blog/searchleak">SearchLeak : How We Turned M365 Copilot Into a One-Click Data...</a></li>
<li><a href="https://cyberpress.org/critical-searchleak-vulnerability/">Critical SearchLeak Vulnerability Lets Attackers Steal Emails, MFA...</a></li>
<li><a href="https://arstechnica.com/security/2026/06/critical-copilot-vulnerability-allowed-hackers-to-seal-2fa-code-from-users/">Critical Copilot vulnerability allowed hackers to seal 2 FA code from...</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#LLM`, `#Copilot`, `#2FA`

---

<a id="item-3"></a>
## [Nemotron 3 Ultra：混合 Mamba-Attention 的 MoE 模型，支持 100 万上下文](https://huggingface.co/papers/2606.15007) ⭐️ 9.0/10

NVIDIA 发布了 Nemotron 3 Ultra，这是一个 550B 参数的混合 Mamba-Attention 专家混合模型，支持 100 万 token 的上下文长度，推理吞吐量比最先进的 LLM 高出 6 倍。 该模型显著提升了推理效率和长上下文处理能力，非常适合自主代理任务，其开源发布可能加速高效 LLM 架构的研究。 它采用了 LatentMoE、多 token 预测、NVFP4 预训练、多环境 RLVR 和多教师在线策略蒸馏（MOPD）。模型总参数 550B，活跃参数 55B。

huggingface_papers · Hugging Face Papers · 6月16日 00:00

**背景**: 混合 Mamba-Attention 架构结合了状态空间模型（SSM）和注意力机制，以平衡效率和长距离依赖捕获。专家混合（MoE）模型使用门控机制，每个 token 只激活部分参数，从而减少计算量。多教师在线策略蒸馏（MOPD）是一种后训练技术，利用强化学习从多个教师模型中蒸馏知识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/hybrid-mamba-attention-architectures">Hybrid Mamba - Attention Architectures</a></li>
<li><a href="https://www.emergentmind.com/topics/mamba-attention-hybrid">Mamba - Attention Hybrid Framework</a></li>
<li><a href="https://www.emergentmind.com/topics/multi-teacher-on-policy-distillation-mopd">Multi - Teacher On - Policy Distillation</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Mixture-of-Experts`, `#Mamba`, `#Attention`, `#Efficient Inference`

---

<a id="item-4"></a>
## [Karpathy 的 autoresearch 项目自动化 nanochat 训练研究](https://github.com/karpathy/autoresearch) ⭐️ 8.0/10

Andrej Karpathy 发布了一个名为 autoresearch 的新 GitHub 项目，该项目利用 AI 代理自动进行单 GPU nanochat 训练的研究，旨在无需人工干预的情况下优化训练过程。 该项目代表了向自动化机器学习研究迈出的重要一步，可能减少优化小规模 LLM 训练所需的时间和专业知识，从而加速高效模型开发的进展。 该仓库使用 Python 编写，已获得超过 87,000 颗星和 12,600 个分支，表明社区兴趣浓厚。该项目专注于 nanochat，这是一个可以在单 GPU 上训练的小型聊天模型。

github_trending · GitHub Trending · 6月17日 04:28

**背景**: Nanochat 是一个设计用于在单 GPU 上高效训练的小型语言模型，常作为理解 LLM 训练流程的学习工具。AI 代理是能够自主执行实验设计、超参数调优和结果分析等任务的系统，无需人类指导。Karpathy 是前 OpenAI 和 Tesla AI 负责人，以 nanoGPT 等教育项目闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://build.nvidia.com/station/nanochat">Nanochat Training | DGX Station</a></li>
<li><a href="https://medium.com/@akdemir_bahadir/inside-nanochat-part-5-understanding-training-5e729522ac2a">Inside nanochat Part 5: Understanding Training | by Bahadır... | Medium</a></li>
<li><a href="https://www.vibediary.dev/essays/nanochat">Training an LLM | Diary of a Vibe Coder</a></li>

</ul>
</details>

**社区讨论**: 社区表现出强烈热情，许多人称赞该项目有潜力使 AI 研究民主化。一些评论者对该项目使用的具体算法以及代理如何处理失败案例表示好奇。

**标签**: `#AI`, `#machine learning`, `#research automation`, `#NLP`, `#GitHub trending`

---

<a id="item-5"></a>
## [vLLM：高吞吐量 LLM 推理引擎在 GitHub 上趋势上升](https://github.com/vllm-project/vllm) ⭐️ 8.0/10

vLLM，一个面向大型语言模型的高吞吐量、内存高效的推理引擎，今天在 GitHub 上新增了 124 颗星，总星数达到 83,108 颗。 这种持续的人气凸显了 vLLM 在使 LLM 推理更快、更便宜方面的关键作用，惠及大规模部署 AI 的开发者和组织。 vLLM 支持在线和离线推理模式，并与 Hugging Face 集成，便于部署开源 LLM。

github_trending · GitHub Trending · 6月17日 04:28

**背景**: 大型语言模型（LLM）在推理时需要大量计算资源。vLLM 通过 PagedAttention、连续批处理和高效 KV 缓存管理等技术优化这一过程，相比标准实现实现了更高的吞吐量和更低的内存使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@crclq2018/explaining-the-source-code-behind-the-vllm-fast-inference-engine-91429f54d1f7">Explaining the Code of the vLLM Inference Engine | Medium</a></li>
<li><a href="https://huggingface.co/docs/inference-endpoints/engines/vllm">vLLM · Hugging Face</a></li>
<li><a href="https://vllm-website-lgfeh1mrx-inferact-inc.vercel.app/blog/anatomy-of-vllm">Inside vLLM: Anatomy of a High - Throughput LLM Inference System</a></li>

</ul>
</details>

**标签**: `#LLM`, `#inference`, `#AI`, `#Python`, `#open-source`

---

<a id="item-6"></a>
## [JoyAI-VL-Interaction：实时视觉语言交互 AI](https://huggingface.co/papers/2606.14777) ⭐️ 8.0/10

研究人员发布了 JoyAI-VL-Interaction，一个 8B 参数的视觉语言模型，能够持续观察视频流并自主决定何时响应，实现无需用户提示的实时交互。 这种从回合制到连续交互的范式转变，可以使 AI 系统在安全监控、视频通话、直播等场景中主动提供帮助，在这些场景中等待用户提示是不切实际的。 该模型每秒内部决策保持沉默、响应或委托给后台模型，擅长视觉触发响应和时间感知。完整的可部署系统包括可插拔的 ASR/TTS、记忆、可视化 UI，以及可连接任何 API 或代理的后台大脑。

huggingface_papers · Hugging Face Papers · 6月16日 00:00

**背景**: 当前的大型视觉语言模型大多是回合制的：它们只在被明确提示时才响应。这限制了它们在事件连续发生的动态环境中的实用性。JoyAI-VL-Interaction 引入了一种新范式，模型始终“在场”并自主决定何时行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/">JoyAI-VL- Interaction : Real - time autonomous interaction for...</a></li>
<li><a href="https://huggingface.co/papers/2606.14777">Paper page - JoyAI-VL- Interaction : Real - Time Vision - Language ...</a></li>

</ul>
</details>

**标签**: `#vision-language`, `#real-time`, `#interactive AI`, `#paradigm shift`

---

<a id="item-7"></a>
## [Qwen 发布机器人基础模型套件](https://qwen.ai/blog?id=qwen-robotsuite) ⭐️ 8.0/10

Qwen 发布了 Qwen-Robot Suite，这是一个专为物理世界智能设计的基础模型套件，使机器人能够理解周围环境、遵循指令并适应变化的环境。 该套件可能加速集成机器人系统的开发，有望在一年内推出简单产品，并使 Qwen 在快速增长的机器人和物理 AI 市场中成为关键参与者。 该套件包括用于目标检测、语义分割、深度估计等的模型，如 Qwen-Robot Suite 博客文章所示。这是阿里巴巴向机器人领域拓展 AI 的一部分，尽管阿里巴巴股价今年已下跌 23%。

hackernews · ilreb · 6月16日 13:15 · [社区讨论](https://news.ycombinator.com/item?id=48554814)

**背景**: 基础模型是在大量数据上训练的大型 AI 模型，可适应各种任务。在机器人领域，它们使机器人能够更智能地感知和与物理世界交互。Qwen 是阿里巴巴开发的一系列 AI 模型，该套件将其能力扩展到物理世界智能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qwen.ai/home">Qwen</a></li>
<li><a href="https://stocktwits.com/news-articles/markets/equity/baba-stock-slides-premarket-alibaba-ai-push-robotics-fails-to-lift-retail-mood/cZKWlx6R7EZ">BABA Stock Slides Premarket: Alibaba's New AI Push Into Robotics ...</a></li>
<li><a href="https://www.pi.website/">Physical Intelligence is bringing general-purpose AI into the physical ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论总体积极，用户对快速产品开发和批量生产的潜力表示兴奋。一些人讨论了制造和战争方面的战略意义，而另一些人则指出需要进行技术评估和与替代方案的比较。

**标签**: `#robotics`, `#foundation models`, `#AI`, `#Qwen`, `#physical world intelligence`

---

<a id="item-8"></a>
## [机械手表机制的互动深度解析](https://ciechanow.ski/mechanical-watch/) ⭐️ 8.0/10

ciechanow.ski 发布了一篇互动文章，通过动画和纯原生代码，逐步详细解释了机械手表的工作原理及其每个部件的功能。 这篇文章因其教育价值而突出，使复杂的钟表学概念对广大受众变得易于理解，并展示了纯原生网络技术在创建丰富互动学习体验方面的力量。 该文章完全由手写的 HTML、CSS 和 JavaScript 构建，确保与旧设备（如 iPhone 7）兼容。它涵盖了手表的关键部件，如主发条、齿轮系、擒纵机构和摆轮。

hackernews · razin · 6月16日 11:26 · [社区讨论](https://news.ycombinator.com/item?id=48553550)

**背景**: 机械手表是一种由主发条驱动的计时装置，主发条储存能量并通过一系列齿轮和擒纵机构释放以调节时间。钟表学是研究机械计时装置的学科，涵盖其设计、制造和维修。理解这些部件对于欣赏机械手表背后的工艺至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Horology">Horology</a></li>
<li><a href="https://www.youtube.com/watch?v=9_QsCLYs2mY">How a Mechanical Watch Works - YouTube</a></li>
<li><a href="https://3dlanes.com/whats-up-with-mechanical-watches-and-how-they-work/">3DLANES What’s Up With: Mechanical Watches and How They Work.</a></li>

</ul>
</details>

**社区讨论**: 社区称赞该文章的教育清晰度，一位教师指出简单解释复杂话题的难度。评论者还赞赏使用纯原生代码，确保了广泛的兼容性，一位读者受到启发，在现实中构建了一个手表机芯的分解视图。

**标签**: `#mechanical watch`, `#interactive article`, `#engineering`, `#education`, `#horology`

---

<a id="item-9"></a>
## [Meta 正在摧毁其工程组织吗？](https://newsletter.pragmaticengineer.com/p/why-is-meta-destroying-its-engineering) ⭐️ 8.0/10

一篇文章和讨论探讨了 Meta 的工程组织是否因对 AI 的痴迷和文化转变而恶化，评论者分享了第一手经验和对行业趋势的担忧。 这很重要，因为 Meta 的工程文化长期以来一直是科技行业的标杆，其潜在衰退可能预示着科技公司如何优先考虑 AI 而非核心工程实践的整体转变。 文章指出，Meta 对 AI 的痴迷导致从基础设施组织抽调工程师到 ADO 组织，部分团队 30-50% 的人员被重新分配，并且首席信息安全官等关键高管离职。

hackernews · throwarayes · 6月16日 16:42 · [社区讨论](https://news.ycombinator.com/item?id=48558045)

**背景**: Meta，前身为 Facebook，历史上以其强大的工程文化著称，强调效率和影响力。最近，该公司将重心大幅转向人工智能，围绕 AI 计划重组团队和优先级，一些人认为这正在损害其他工程领域。

**社区讨论**: 评论者表达了不同观点：一些前员工描述了内部自建组织与收购组织相比的低效，而另一些人则警告说，对 AI 的痴迷正在成为整个行业的毒性常态，而不仅仅是 Meta。

**标签**: `#Meta`, `#engineering culture`, `#AI`, `#organizational change`, `#tech industry`

---

<a id="item-10"></a>
## [将 ast.walk 提速 220 倍](https://reflex.dev/blog/why-ast-walk-when-you-can-ast-sprint/) ⭐️ 8.0/10

Reflex 的一篇博客文章详细介绍了如何通过用优化方法替换惯用 Python 代码（例如使用自定义 fast-walk 库）来实现 Python AST 遍历的 220 倍加速。 这一优化显著提升了依赖 AST 遍历的 linter、代码分析工具以及任何 Python 应用的性能，有可能将执行时间从秒级降至毫秒级。 该优化涉及用自定义实现替换 ast.walk，以规避 Python 的开销，例如使用迭代遍历代替递归，并减少函数调用。fast-walk 库已在 GitHub 上发布。

hackernews · palashawas · 6月16日 16:25 · [社区讨论](https://news.ycombinator.com/item?id=48557768)

**背景**: AST（抽象语法树）遍历是 Python 中用于分析或转换代码的常见操作，被 linter 和格式化工具等使用。内置的 ast.walk 函数虽然方便，但由于 Python 的动态特性和基于生成器的递归开销，速度较慢。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://reflex.dev/blog/why-ast-walk-when-you-can-ast-sprint/">Making ast . walk 220x Faster</a></li>
<li><a href="https://github.com/reflex-dev/fast-walk">GitHub - reflex-dev/fast- walk : fast ast walk · GitHub</a></li>
<li><a href="https://runebook.dev/en/docs/python/library/ast/ast.walk">Mastering Python ASTs: Beyond ast . walk ()</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏了首先优化惯用 Python 代码的努力，其中一位指出 Python 会惩罚模块化。其他人则好奇类似的 lint 检查是否可以用 semgrep 规则表达，以及该优化是否能使 libCST 和 bandit 等工具受益。

**标签**: `#Python`, `#AST`, `#performance optimization`, `#code analysis`, `#linters`

---

<a id="item-11"></a>
## [联邦对 Fable 5 的“修复代码”绕过方式感到震惊](https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827) ⭐️ 8.0/10

研究人员展示，一个简单的“修复这段代码”提示即可绕过 Fable 5 的安全护栏，引发联邦担忧，并凸显了保护 LLM 免受意外漏洞生成挑战的难度。 这种绕过方式简单且可能无法修复，破坏了 Anthropic 的策略——即发布一个受到严密保护的模型，同时声称底层 Mythos 模型极其危险。这引发了关于 AI 安全与监管越界的严重问题。 “修复这段代码”提示通过要求模型修复安全漏洞来工作，这无意中作为测试用例的一部分生成了漏洞利用代码。这种越狱被认为几乎无法修复，因为它利用了模型改进代码的核心能力。

hackernews · _tk_ · 6月16日 09:26 · [社区讨论](https://news.ycombinator.com/item?id=48552687)

**背景**: Fable 5 是 Anthropic 的 Mythos 类模型的公开可用、受到严密保护的版本，配备了安全分类器，可阻止生物学、网络安全和 LLM 开发相关查询。LLM 越狱是指试图绕过这些安全措施的行为，通常通过类似社会工程的提示来实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mindstudio.ai/blog/claude-fable-5-safety-guardrails-what-gets-blocked">Claude Fable 5 Safety Guardrails: What Gets Blocked, What Doesn't ...</a></li>
<li><a href="https://www.bitsight.com/blog/claude-fable-5-and-new-reality-ai-enabled-third-party-risk">Claude Fable 5 and the New Reality of AI-Enabled Third-Party Risk</a></li>
<li><a href="https://www.reddit.com/r/artificial/comments/1u2cwfz/claude_fable_5s_security_guardrails_can_be/">Claude Fable 5's security guardrails can be bypassed with a fake ...</a></li>

</ul>
</details>

**社区讨论**: 评论者认为“修复这段代码”绕过方式既巧妙又令人担忧，指出这是一种简单且可能无法修复的越狱。一些人认为联邦的反应是出于意识形态差异的报复性敲诈，而另一些人则质疑发布一个如此容易生成漏洞利用代码的模型是否安全。

**标签**: `#AI safety`, `#jailbreak`, `#LLM`, `#security`, `#policy`

---

<a id="item-12"></a>
## [x86 模拟器团队在仿真中修复糟糕代码](https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419) ⭐️ 8.0/10

微软的 x86 模拟器团队发现一个程序使用展开循环来初始化 64KB 的栈内存，导致性能问题，他们在仿真过程中修补了该代码。 这则轶事说明了兼容层为确保软件正确运行所采取的极端措施，并突显了此类变通方法在现代模拟（如 Proton 和 Wine）中的持续相关性。 该程序使用一个展开到 64KB 指令的循环来初始化栈内存，效率低下。模拟器团队在仿真期间修补了二进制文件，改用标准的栈探测和紧凑循环。

hackernews · paulmooreparks · 6月16日 04:46 · [社区讨论](https://news.ycombinator.com/item?id=48550693)

**背景**: x86 模拟器将 x86 指令翻译到不同架构上运行，通常使用即时编译（JIT）。像 Wine 和 Proton 这样的兼容层也采用类似技术来在 Linux 上运行 Windows 软件。在仿真期间修补糟糕代码是一种已知的变通方法，可以在不修改原始软件的情况下提高性能或修复错误。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419">The time the x 86 emulator team found code so bad that they fixed it...</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了相关故事，例如在 Windows 95 中修补 SimCity 的释放后使用错误，以及现代例子如 Elden Ring 受益于 Proton 热修复。一些人讨论了可能导致这种展开循环的编译器优化标志。

**标签**: `#x86 emulation`, `#compatibility`, `#software engineering`, `#historical anecdote`, `#community discussion`

---

<a id="item-13"></a>
## [AI 模型出口管制损害美国网络防御](https://simonwillison.net/2026/Jun/16/fable-5-export-controls/#atom-everything) ⭐️ 8.0/10

对 Anthropic 的 Claude Fable 5 等 AI 模型的出口管制，阻止了它们修复安全漏洞——一个仅仅要求模型修复代码的“越狱”行为被认定为违规。Kate Moussouris 证实，被禁止的行为实际上是要求模型审查并修补含有已知 CVE 的代码的防御性请求。 这项政策削弱了美国网络防御，因为它扼杀了 AI 模型最有价值的能力：修复安全漏洞。这凸显了非技术决策者与防御者实际需求之间的危险脱节。 所谓的“越狱”包括要求 Fable 5 审查含有已知 CVE 和故意植入漏洞的开源代码，然后通过多步骤手动过程“修复此代码”。Anthropic 遵守政府指令，在全球范围内暂停了 Fable 5 和 Mythos 5，因为它无法可靠地过滤外国用户访问。

rss · Simon Willison · 6月16日 05:20

**背景**: AI 模型的出口管制旨在防止对手利用先进 AI 进行恶意活动，例如策划网络攻击。然而，同样的能力对于防御性网络安全任务（如漏洞检测和修补）也至关重要。通用漏洞与暴露（CVE）系统记录了公开已知的安全漏洞，修复这些漏洞是核心防御活动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/fable-mythos-access">Statement on the US government directive to suspend access to Fable ...</a></li>
<li><a href="https://www.testingcatalog.com/anthropic-suspends-fable-5-and-mythos-5-after-export-order/">Anthropic suspends Fable 5 and Mythos 5 after export order</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures">Common Vulnerabilities and Exposures - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 讨论中普遍赞同该分析，Kate Moussouris 提供了专家评论，指出出口管制荒谬至极，因为它们阻止了 AI 最有价值的防御用途。评论者指出，非技术决策者被误导，认为能够“策划网络攻击”的模型具有独特危险性，从而导致适得其反的政策。

**标签**: `#AI policy`, `#export controls`, `#cybersecurity`, `#AI safety`, `#open source`

---

<a id="item-14"></a>
## [五角大楼使用 AI 起草国会报告](https://arstechnica.com/ai/2026/06/pentagon-boasts-of-using-ai-to-write-reports-mandated-by-congress/) ⭐️ 8.0/10

五角大楼宣布使用生成式 AI 工具起草国会要求的报告，并声称有 150 万人员在使用 AI 工具。 这标志着政府采用 AI 的重要一步，引发了关于透明度、问责制以及 AI 在政策制定中作用的质疑。 五角大楼首席技术官 Emil Michael 将 AI 生成的报告作为 AI 使用的关键例子，但未披露具体使用的 AI 工具和模型。

rss · Ars Technica AI · 6月16日 18:11

**背景**: 生成式 AI 工具（如大型语言模型）可以根据提示生成类似人类的文本。五角大楼一直在探索 AI 在情报和瞄准等领域的应用，近期有报道称其在伊朗打击中使用了 Anthropic 的 Claude。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2026/06/pentagon-boasts-of-using-ai-to-write-reports-mandated-by-congress/">Pentagon boasts of using AI to write reports mandated... - Ars Technica</a></li>
<li><a href="https://www.wionews.com/world/ai-in-warfare-is-here-pentagon-used-anthropic-s-claude-ai-in-iran-strikes-but-it-has-many-llms-and-tools-from-other-firms-what-we-know-1772372063341">AI in warfare is here: Pentagon used Anthropic's Claude AI in Iran...</a></li>

</ul>
</details>

**标签**: `#AI`, `#government`, `#policy`, `#generative AI`, `#defense`

---

<a id="item-15"></a>
## [OpenAI 收入增长但仍亏损数十亿美元](https://arstechnica.com/ai/2026/06/leaked-financial-docs-show-openai-is-losing-billions-of-dollars-a-year/) ⭐️ 8.0/10

泄露的经审计财务文件显示，OpenAI 的收入快速增长，但远不及研发和其他支出，导致每年亏损数十亿美元。 这一披露凸显了领先 AI 开发的巨大成本，并对即使是知名 AI 公司的长期财务可持续性提出疑问，可能影响投资者信心和行业格局。 这些文件经过审计，显示虽然收入在增长，但支出（尤其是研发支出）远超收入，导致净亏损达数十亿美元。

rss · Ars Technica AI · 6月16日 16:18

**背景**: OpenAI 是一家领先的人工智能研究机构，以开发 GPT-4 和 ChatGPT 等模型而闻名。该公司在计算基础设施、人才和研究方面投入了巨额成本，这在 AI 行业中很常见，但很少如此详细地披露。

**标签**: `#OpenAI`, `#financials`, `#AI industry`, `#R&D costs`

---