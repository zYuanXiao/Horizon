---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> 从 126 条内容中筛选出 15 条重要资讯。

---

1. [Qwen 3.8 发布：2.4T MoE 旗舰模型与开放权重](#item-1) ⭐️ 9.0/10
2. [AirLLM 实现在 4GB GPU 上运行 70B 大模型](#item-2) ⭐️ 8.0/10
3. [Agent-Reach：CLI 工具让 AI 代理零成本访问主流平台](#item-3) ⭐️ 8.0/10
4. [Qwen-UI-Agent：面向真实世界的基座 GUI 智能体](#item-4) ⭐️ 8.0/10
5. [Metis：首个具备原生记忆能力的记忆基础模型](#item-5) ⭐️ 8.0/10
6. [欧盟年龄验证强制硬件认证，引发隐私与 Linux 担忧](#item-6) ⭐️ 8.0/10
7. [微软牵头公开信支持开放权重 AI，回应美国政策辩论](#item-7) ⭐️ 8.0/10
8. [llama.cpp 为 DeepSeek V4 Flash 添加 MTP/DSpark 支持](#item-8) ⭐️ 8.0/10
9. [虚假 16.5T 模型暴露 Hugging Face 参数统计漏洞](#item-9) ⭐️ 8.0/10
10. [Kimi K3 MoE 模型通过 NVMe 流式加载在 8GB 内存的单 CPU 上运行](#item-10) ⭐️ 8.0/10
11. [Mference 引擎在 5.3GB 内存上运行 284B DeepSeek-V4-Flash](#item-11) ⭐️ 8.0/10
12. [MiniMax-H3 开源权重发布，ComfyUI 首日支持](#item-12) ⭐️ 8.0/10
13. [NVIDIA SANA-Video 2.0：混合注意力、快速视频生成，许可尚不明确](#item-13) ⭐️ 8.0/10
14. [NVIDIA 的 Sol-Attn 通过即时注意力稀疏化加速视频生成](#item-14) ⭐️ 8.0/10
15. [欧盟人工智能法案第 50 条生效：强制披露 AI 生成内容](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen 3.8 发布：2.4T MoE 旗舰模型与开放权重](https://www.reddit.com/r/LocalLLaMA/comments/1ve02j9/qwen_38_is_live_now/) ⭐️ 9.0/10

Qwen 3.8 现已上线，其旗舰模型采用 2.4 万亿参数的混合专家（MoE）架构，并承诺即将开放权重。同时确认 27B 变体将于下周发布。 此次发布标志着编码和专业工作能力的重大飞跃，该模型能够自主编码并交付跨越 10 天以上的完整项目。开放权重策略很可能加速 AI 社区的采用和创新，尤其对开发者和研究人员而言。 旗舰模型通过 Qwen Cloud、Token Plan、Qoder 和 QoderWork 提供托管预览。27B 变体预计下周发布，开放权重也承诺即将推出，但具体时间表尚不明确。

reddit · r/LocalLLaMA · /u/Mobile-Pumpkin7944 · 8月3日 01:51

**背景**: Qwen 是阿里巴巴云开发的大型语言模型系列，以开源和专有产品著称。新的 MoE 架构采用混合专家技术，高效扩展参数规模，从而在编码和专业工作等复杂任务上实现更优性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://specpicks.com/reviews/qwen-3-8-open-weights-12gb-gpu-2026">Qwen 3 . 8 Open Weights : What Fits on a 12GB GPU | SpecPicks</a></li>
<li><a href="https://insiderllm.com/guides/open-weights-you-cant-run/">Kimi K3 & Qwen 3 . 8 : Open Weights You Can't Run (2026) | InsiderLLM</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对此次发布感到兴奋，许多用户称赞其惊人的参数规模和开放权重承诺。然而，一些用户对开放权重的实际可用性表示怀疑，指出过去的延迟以及目前仅提供托管预览的情况。

**标签**: `#AI`, `#LLM`, `#Qwen`, `#Open Source`, `#MoE`

---

<a id="item-2"></a>
## [AirLLM 实现在 4GB GPU 上运行 70B 大模型](https://github.com/lyogavin/airllm) ⭐️ 8.0/10

lyogavin 的 GitHub 项目 AirLLM 现在可以在单个 4GB GPU 上运行 70B 参数的大语言模型，这是模型部署效率的重大突破。该项目今日获得 819 颗星，总星数达到 25,799 颗。 这一进展使大语言模型的访问民主化，让硬件资源有限的研究人员和开发者能够尝试最先进的模型。通过降低高端模型推理的门槛，可能加速 AI 应用的创新。 AirLLM 使用 Jupyter Notebook 编写，拥有 2,895 个 fork，表明社区参与活跃。该项目可能使用模型量化和内存优化等技术将 70B 参数适配到 4GB 显存中，但提供的内容中未详细说明具体方法。

github_trending · GitHub Trending · 8月3日 03:03

**背景**: 大语言模型（LLM）通常需要大量 GPU 内存，70B 参数模型往往需要超过 40GB，这使得大多数个人无法使用。AirLLM 通过实现仅 4GB 显存的消费级 GPU 上的推理来解决这一问题，可能采用逐层加载和量化等技术。这与优化 LLM 在边缘设备和低资源环境中部署的更广泛趋势一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/lyogavin/airllm">GitHub - lyogavin/airllm: AirLLM 70B inference with single 4GB GPU · GitHub</a></li>
<li><a href="https://github.com/BretMcDanel/airllm-server">GitHub - BretMcDanel/airllm-server: OpenAI compatible server for AirLLM · GitHub</a></li>

</ul>
</details>

**社区讨论**: 搜索结果中未提供社区评论。

**标签**: `#LLM`, `#GPU`, `#inference`, `#efficiency`, `#open-source`

---

<a id="item-3"></a>
## [Agent-Reach：CLI 工具让 AI 代理零成本访问主流平台](https://github.com/Panniantong/Agent-Reach) ⭐️ 8.0/10

Agent-Reach 是一款 Python CLI 工具，在 GitHub 上获得了显著关注，目前拥有 64,844 颗星，今日新增 659 颗星。它使 AI 代理能够零 API 费用地读取和搜索 Twitter、Reddit、YouTube、GitHub、Bilibili 和 XiaoHongShu 等平台。 该工具解决了 AI 代理在无需 API 费用的情况下访问实时互联网数据的关键需求，可能降低开发者构建 AI 应用的门槛。其快速的星标增长表明社区的高度认可，并暗示它可能成为 AI/ML 生态系统中的标准工具。 该仓库使用 Python 编写，拥有 5,359 个 fork。它通过单一 CLI 接口支持多个平台，包括 Twitter、Reddit、YouTube、GitHub、Bilibili 和 XiaoHongShu。该工具采用网页抓取而非官方 API 的方式，从而绕过 API 费用和速率限制。

github_trending · GitHub Trending · 8月3日 03:03

**背景**: AI 代理通常需要访问外部数据源来执行任务，但官方 API 可能成本高昂且存在使用限制。像 Agent-Reach 这样的 CLI 工具通过直接抓取网页内容提供了一种轻量级替代方案，使开发者更容易将实时数据集成到他们的 AI 工作流中。包含 Bilibili 和 XiaoHongShu 等中国平台反映了该工具的全球吸引力以及这些平台在 AI 社区中日益增长的重要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent">Agent - Wikipedia</a></li>
<li><a href="https://www.bilibili.tv/vip/en">BiliBili</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#CLI tool`, `#web scraping`, `#API alternative`, `#Python`

---

<a id="item-4"></a>
## [Qwen-UI-Agent：面向真实世界的基座 GUI 智能体](https://huggingface.co/papers/2607.28227) ⭐️ 8.0/10

Qwen-UI-Agent 是阿里巴巴推出的新一代基座 GUI 智能体，它整合了移动端、电脑端、网页和 DeepSearch 环境，并采用统一动作空间和 AutoResearch 风格的数据飞轮。它在移动端基准测试中取得了最先进的结果，包括在 MobileWorld 上达到 82.1%，在 MobileWorld-Real 上达到 92.2%，在 AndroidDaily 上达到 97.5%。 这项工作通过支持在真实设备上的可靠操作、跨平台工作流和自主改进，推动了 GUI 智能体向实际部署迈进。它在移动端任务上树立了新的性能标准，并在电脑和浏览器使用方面与 Opus 4.8、Gemini 3.1 Pro 和 GPT-5.6 Sol 等前沿模型相比表现出竞争力。 该智能体采用统一动作空间，将 GUI 操作与 CLI 执行交错进行，并在单个模型回合中生成批量动作。它支持在超过 100 轮的轨迹上进行在线强化学习，并拥有超过 10,000 个并发环境用于 rollout，同时包含一个轻量级 harness 层，用于主动服务启动和有状态工作流。

huggingface_papers · Hugging Face Papers · 7月31日 00:00

**背景**: GUI 智能体是能够与图形用户界面交互以在数字设备上执行任务的人工智能系统。传统的 GUI 智能体通常依赖模拟环境，缺乏处理现实世界复杂性的能力。Qwen-UI-Agent 通过将沙盒环境与大规模真实设备移动运行时相结合来解决这一问题，其 AutoResearch 风格的数据飞轮利用智能体构建任务、诊断失败并规划迭代，从而实现自主改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tongyi-mai.github.io/Qwen-UI-Agent/">Qwen - UI - Agent — Technical Report</a></li>
<li><a href="https://arxiv.org/html/2607.28227v1">Qwen - UI - Agent Technical Report: Toward Next-Generation...</a></li>
<li><a href="https://cctest.ai/en/articles/qwen-ui-agent-a-real-world-centric-foundation-gui-agent">Qwen - UI - Agent Brings GUI Agents to Real Devices - CCTest</a></li>

</ul>
</details>

**标签**: `#GUI agents`, `#AI agents`, `#Foundation models`, `#Reinforcement learning`, `#Human-computer interaction`

---

<a id="item-5"></a>
## [Metis：首个具备原生记忆能力的记忆基础模型](https://huggingface.co/papers/2607.26760) ⭐️ 8.0/10

该论文提出了记忆基础模型的概念，并介绍了 Metis——首个将持久、动态演化的记忆状态直接集成到模型主干中、通过记忆注意力访问的原型。Metis 使用大规模记忆专用数据和多种优化目标进行训练，其记忆更新仅需一次前向传播，无需梯度计算。 这项工作通过将记忆从外部模块转移到基础模型内部，解决了 AI 代理设计中的一个重要空白，有望提高效率并支持端到端优化。它可能改变代理记忆的架构方式，使代理在处理长期上下文时更加自主和高效。 Metis 的在线记忆维护无需梯度，推理时所有学习权重保持冻结，而记忆状态通过标准前向计算自主变换。作者发布了项目和模型检查点以促进未来研究，并提供了对优势、局限和行为的详细分析。

huggingface_papers · Hugging Face Papers · 7月31日 00:00

**背景**: 基础模型是大型预训练模型，可适应多种任务，但通常缺乏原生记忆，在 AI 代理中依赖外部记忆模块。记忆基础模型旨在将记忆内化为模型的一等能力，使模型能够在多次推理中维持持久状态。这一概念借鉴了 LSTM 和神经网络中持久活动等早期工作，但将其应用于现代基础模型架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.26760">[2607.26760] Metis: Memory Foundation Model</a></li>
<li><a href="https://arxiv.org/html/2607.26760">titlefont Metis: Memory Foundation Model</a></li>
<li><a href="https://en.wikipedia.org/wiki/Foundation_model">Foundation model - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#memory`, `#foundation models`, `#architecture`

---

<a id="item-6"></a>
## [欧盟年龄验证强制硬件认证，引发隐私与 Linux 担忧](https://linuxiac.com/eu-age-verification-project-mandates-hardware-bound-attestation/) ⭐️ 8.0/10

欧盟年龄验证项目已确认硬件绑定认证为强制要求，用户必须通过设备硬件而非纯软件方式证明年龄。这一技术要求已在欧盟年龄验证蓝图中详细说明，该蓝图依赖零知识证明（ZKP）密码学来保护隐私。 该政策可能为全球年龄验证树立先例，但引发了关于隐私、数字主权和竞争的重大担忧。它可能将 Linux 用户和自定义 ROM 用户排除在外，迫使他们使用非 Linux 设备或面临在线服务访问受限。 欧盟年龄验证蓝图规定硬件绑定认证为强制要求，但未使用 ZKP 或盲签名，因此硬件 ID 在技术上会暴露。该系统是临时性的，未来计划推出数字钱包应用，允许用户证明年龄等事实而不泄露额外信息。

hackernews · RobotToaster · 8月2日 20:44 · [社区讨论](https://news.ycombinator.com/item?id=49148128)

**背景**: 硬件绑定认证涉及在 TPM 2.0、Apple Secure Enclave 或 Android Keymaster 等安全硬件元素内生成加密密钥，并用其签署认证声明。这证明设备是正品且软件未被篡改。欧盟的年龄验证解决方案旨在保护未成年人上网安全，但其对硬件认证的依赖引发了对隐私和包容性的担忧，尤其是对 Linux 等开源操作系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://linuxiac.com/eu-age-verification-project-mandates-hardware-bound-attestation/">EU Age Verification Project Mandates Hardware-Bound Attestation</a></li>
<li><a href="https://ageverification.dev/">EU Age Verification Blueprint — the dedicated technical portal</a></li>
<li><a href="https://digital-strategy.ec.europa.eu/en/news/commission-makes-available-age-verification-blueprint">Commission makes available an age - verification blueprint</a></li>

</ul>
</details>

**社区讨论**: 社区评论对欧盟的动机表示怀疑，认为这是将现实身份与在线活动联系起来，而不仅仅是保护未成年人。有人担心反竞争效应，因为这实际上强制要求使用 Google 或 Apple 账户，并担心 Linux 用户被排除在外，他们需要第二台非 Linux 设备。技术评论指出，硬件认证会暴露硬件 ID，但通常需要多方共谋才能利用这一点。

**标签**: `#EU policy`, `#privacy`, `#hardware attestation`, `#digital sovereignty`, `#age verification`

---

<a id="item-7"></a>
## [微软牵头公开信支持开放权重 AI，回应美国政策辩论](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 8.0/10

Simon Willison 总结了近期关于 AI 发展的公开信，其中一封由微软牵头、日期为 7 月 24 日的信件获得了包括 NVIDIA、亚马逊和 OpenAI 在内的 235 家公司签署，主张开放权重模型以应对美国可能的限制。Anthropic 拒绝签署并发布了自身立场，而 7 月 28 日另一封名为“Pacing the Frontier”的信件则汇集了前沿 AI 公司的 1324 名员工，呼吁审慎控制 AI 发展节奏。 这凸显了 AI 行业在开放权重模型上的重大分歧，微软和 OpenAI 等主要参与者支持开放，而 Anthropic 则警告风险。这场辩论的结果可能影响美国 AI 政策，进而影响 AI 生态系统的创新、竞争和安全。 微软牵头的信件明确支持蒸馏技术，即模型利用其他模型的输出进行训练，并主张政策制定者不应将其与盗用混为一谈。值得注意的是，Anthropic 在 CEO Dario Amodei 的领导下回应，呼吁打击工业规模的蒸馏操作，同时表示他们从未主张禁止开放权重模型。

rss · Simon Willison · 8月2日 04:16

**背景**: 开放权重模型是指其核心组件（包括训练后的权重）公开发布的 AI 模型，任何人都可以下载和使用。这与保持专有的封闭模型形成对比。关于开放权重模型的争论涉及安全、国家安全和创新等关切，支持者认为开放性有助于审查和改进，而批评者则担心被恶意行为者或威权政府滥用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.nytimes.com/2026/07/28/technology/open-weight-ai.html">What Is Open-Weights A.I.? - The New York Times</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#policy`, `#open-weight models`, `#industry`

---

<a id="item-8"></a>
## [llama.cpp 为 DeepSeek V4 Flash 添加 MTP/DSpark 支持](https://www.reddit.com/r/LocalLLaMA/comments/1vdhgq9/llamacpp_just_added_mtp_dspark_support_for/) ⭐️ 8.0/10

llama.cpp 在最近的更新（PR #25784）中为 DeepSeek V4 Flash 添加了多令牌预测（MTP）和 DSpark 支持。这使得本地推理 DeepSeek V4 Flash 模型时能够使用投机解码功能。 这一更新对本地 LLM 社区意义重大，因为它将一种新颖的投机解码技术引入广泛使用的推理引擎，可能提升 DeepSeek V4 Flash 用户的推理速度和效率。这也凸显了将先进解码方法集成到本地工具中的趋势。 该支持在 PR #25784 中实现，发布版本包含多个平台（macOS、Linux、Windows、Android）的二进制文件。DeepSeek V4 Flash DSpark 模型是一个采用 MIT 许可的草稿模型，其 Q4_K_M 量化版本需要约 99.5 GB 的显存，建议使用 130 GB 以上以获得舒适的推理体验。

reddit · r/LocalLLaMA · /u/rmhubbert · 8月2日 12:58

**背景**: 多令牌预测（MTP）是一种允许语言模型在单次前向传播中生成多个令牌的技术，而不是一次生成一个，从而显著加快推理速度。DSpark 是用于投机解码的草稿模型，其中较小的模型提出令牌，然后由较大的模型验证。llama.cpp 是一个流行的开源库，用于在各种硬件上本地运行 LLM。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://topclanker.com/blog/2026-05-14-llama-cpp-mtp-speed/">Llama . cpp 's Multi-Token Prediction: The Speed Boost Your Local AI...</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark">deepseek -ai/ DeepSeek - V 4 - Flash - DSpark · Hugging Face</a></li>
<li><a href="https://llmrun.dev/model/deepseek-ai-deepseek-v4-flash-dspark">DeepSeek V 4 Flash DSpark — Hardware Requirements... | llmrun</a></li>

</ul>
</details>

**社区讨论**: Reddit 帖子尚未产生评论，但该公告可能会引发关于性能基准、硬件要求以及 llama.cpp 中 MTP 和 DSpark 实现细节的讨论。

**标签**: `#llama.cpp`, `#DeepSeek`, `#MTP`, `#DSpark`, `#local LLM`

---

<a id="item-9"></a>
## [虚假 16.5T 模型暴露 Hugging Face 参数统计漏洞](https://www.reddit.com/r/LocalLLaMA/comments/1vdh1us/vacuum_16t/) ⭐️ 8.0/10

一位 Reddit 用户向 Hugging Face 上传了一个包含 16.5 万亿参数但实际上没有任何数据的模型，利用了该平台仅根据 safetensors 头部计算参数数量的漏洞。这个名为“vacuum-16t”的模型虽然只包含零数据，却登上了 Hub 参数排行榜的榜首。 这一演示凸显了 Hugging Face 模型元数据在信任和验证方面的重大缺陷，可能误导依赖参数数量进行模型选择的用户。它强调了 AI 社区对模型仓库进行更严格验证的必要性。 该模型在 385 个分片中声明了 3,841 个形状为[65536, 65536]的 4 位张量，外加一个形状为[4294967296, 1]的位置嵌入张量，总计 16,501,264,351,232 个参数。由于 Xet 内容定义分块去重，实际上传的数据仅约 692 KB，但存储配额却按 8.25 TB 计费。

reddit · r/LocalLLaMA · /u/alerikaisattera · 8月2日 12:39

**背景**: Hugging Face 通过汇总 safetensors 头部中张量形状的乘积来计算仓库的参数数量，而不读取实际的张量数据。Safetensors 是一种将张量元数据存储在头部的格式，平台信任这些头部进行显示。这一漏洞允许任何人声明任意大的参数数量，而无需上传相应的数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gist.github.com/davidheineman/fb36e0ad79b5b7c044201c1b420fdd03">count huggingface model params · GitHub</a></li>
<li><a href="https://zenn.dev/platina/articles/e65c73cb01a900?locale=en">Reading Safetensors Headers</a></li>

</ul>
</details>

**标签**: `#Hugging Face`, `#model metadata`, `#safetensors`, `#AI community`, `#security`

---

<a id="item-10"></a>
## [Kimi K3 MoE 模型通过 NVMe 流式加载在 8GB 内存的单 CPU 上运行](https://www.reddit.com/r/LocalLLaMA/comments/1vd874t/i_pushed_kimi_k3_onto_one_cpu_with_8_gb_of_ram/) ⭐️ 8.0/10

一位开发者用 C99 编写了一个推理引擎，通过从 NVMe 流式加载专家并打包稠密主干，在仅有 8GB 内存的单 CPU 上运行了 1.56 TB 的混合专家模型 Kimi K3。在最小内存预设下，该引擎实现了约 33 秒/令牌的速度，且在不同内存预算下输出完全一致。 这展示了在极简硬件上运行大规模 MoE 模型的极致资源利用能力，突破了本地 LLM 推理的边界。它提供了关于专家卸载、打包 4 位推理和流式加载的宝贵技术见解，可能激发社区进一步的优化。 该引擎不使用 BLAS、框架或 GPU 路径，仅由六个 C 文件、libm 和 OpenMP 组成，生成 176 KB 的二进制文件。模型需要 1.7 TB 的可用磁盘空间来存储检查点和打包后的主干，引擎还包含一个自测功能，构建 13 层模型以对照 PyTorch 参考验证正确性。

reddit · r/LocalLLaMA · /u/FareedKhan557 · 8月2日 04:26

**背景**: Kimi K3 是 Moonshot AI 推出的开放权重、原生多模态智能体模型，拥有 2.8 万亿参数，采用混合专家（MoE）架构。在 MoE 模型中，每个令牌只激活部分专家，因此尽管总参数量巨大，仍能实现高效推理。开发者的方法利用这种稀疏性，按需从 NVMe 流式加载专家，避免了将整个模型加载到内存中的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts (MoE)</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#MoE`, `#CPU inference`, `#resource optimization`, `#Kimi K3`

---

<a id="item-11"></a>
## [Mference 引擎在 5.3GB 内存上运行 284B DeepSeek-V4-Flash](https://www.reddit.com/r/LocalLLaMA/comments/1vdbix4/deepseekv4flash_284b_on_53gb_of_memory/) ⭐️ 8.0/10

一款名为 Mference 的新开源引擎通过从 SSD 流式加载专家，使得在仅 5.3GB 内存上运行 DeepSeek-V4-Flash 284B-A13B 模型成为可能，在 24GB Mac 上最高可达 4.8 tok/s。它还支持其他 MoE 模型，如 Gemma 4 26B-A4B 和 Qwen 3.6 35B-A3B。 这展示了一种在内存有限的消费级硬件上运行超大规模 MoE 模型的实用方法，可能使最先进的 LLM 更加普及。它可能激发本地推理和内存管理的进一步优化。 该模型采用 2 位动态量化，磁盘占用约 91GB，峰值内存约 6.8GB，实际通常为 5.3GB。该引擎还包含原生 Mac 应用，支持多轮对话、OpenAI 兼容服务器，以及本地 PDF/DOCX/PPTX/XLSX 附件。

reddit · r/LocalLLaMA · /u/Blahblahblakha · 8月2日 07:28

**背景**: 混合专家（MoE）模型每个 token 只激活几十亿参数，因此可以将共享核心和 KV 缓存常驻内存，同时从 SSD 流式加载选中的专家。这种方法用存储带宽换取内存容量，使得大型模型能在内存有限的设备上运行。量化通过降低精度来减小模型大小，而 2 位动态量化是一种激进的形式，能显著缩小内存占用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NeelM0906/Mference/blob/main/docs/BENCHMARKS.md">Mference /docs/BENCHMARKS.md at main · NeelM0906/ Mference</a></li>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization">A Visual Guide to Quantization - by Maarten Grootendorst</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论可能包括对基准测试的技术验证以及对引擎实现的好奇。一些人可能质疑在有限上下文下运行如此大模型的实用性，而另一些人则赞赏内存优化方面的创新。

**标签**: `#LLM`, `#MoE`, `#Local Inference`, `#Memory Optimization`, `#Mac`

---

<a id="item-12"></a>
## [MiniMax-H3 开源权重发布，ComfyUI 首日支持](https://www.reddit.com/r/StableDiffusion/comments/1ve0urz/minimaxh3_weights_up/) ⭐️ 8.0/10

MiniMax 发布了其 H3 多模态视频生成模型的开源权重，ComfyUI 提供了首日支持，并带有优化的工作流和量化权重。此次发布支持文生视频、图生视频、首尾帧生成和参考视频生成，最高可达 2K 分辨率，每段视频最长 15 秒，并带有同步音频。 此次发布使最先进的视频生成模型得以普及，研究人员和爱好者可以在 RTX 3060 等消费级硬件上本地运行。同时，这也巩固了 ComfyUI 作为 AI 视频创作领先平台的地位，可能加速开源 AI 社区的创新。 ComfyUI 工程师剪枝了模型的调制权重（约占总参数的 40%），并用查找表替换，将内存占用从 123.6 GB 减少 66% 至 42.5 GB，且质量无损。权重包含 int8 量化和自定义内核，使得在 12GB 显存 GPU 和 32GB 内存上可生成 480p 视频，生成 5 秒片段耗时不到 9 分钟。

reddit · r/StableDiffusion · /u/blahblahsnahdah · 8月3日 02:28

**背景**: MiniMax-H3 是一个多模态视频生成模型，可接受文本、图像、视频和音频输入，生成带有同步音频的视频。ComfyUI 是一个基于节点的生成式 AI 界面，允许用户创建自定义工作流。该模型已在 Hugging Face 上发布，ComfyUI 提供了多种生成模式的官方工作流模板。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-H3">MiniMaxAI/ MiniMax - H 3 · Hugging Face</a></li>
<li><a href="https://github.com/Comfy-Org/ComfyUI">GitHub - Comfy-Org/ ComfyUI : The most powerful and modular...</a></li>
<li><a href="https://docs.comfy.org/">ComfyUI Official Documentation - ComfyUI</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对此次发布感到兴奋，用户称赞模型的灵活性以及 ComfyUI 团队为在消费级硬件上优化所做的巨大工程努力。一些用户正在测试其极限，注意到它可以生成从 1 秒到 30 秒、多种分辨率的视频。同时，用户对 ComfyUI 团队提供的详细技术解释表示赞赏。

**标签**: `#AI`, `#Machine Learning`, `#Model Release`, `#MiniMax`

---

<a id="item-13"></a>
## [NVIDIA SANA-Video 2.0：混合注意力、快速视频生成，许可尚不明确](https://www.reddit.com/r/StableDiffusion/comments/1vdxwzg/sanavideo_20_nvidias_new_hybridattention_video/) ⭐️ 8.0/10

NVIDIA 发布了 SANA-Video 2.0，这是一个视频扩散变压器，提供 5B 和 14B 参数版本，采用混合线性-softmax 注意力、块注意力残差和 Sol-Engine 加速。它能在单个 RTX 5090 上生成 720p 视频，在相同硬件上比 Wan 2.2-A14B 快达 120 倍。 此次发布意义重大，因为它引入了架构创新，可能使高质量视频生成在消费级 GPU 上更加普及，从而可能改变视频生成模型的格局。然而，许可不明确使得社区能否采用并基于此技术进行开发存在不确定性。 该模型采用 3:1 的门控线性注意力与门控 softmax 锚点比例，实现了 O(N) 缩放和 softmax 级别的表达能力。Sol-Engine 优化提供了 3.58 倍加速，在 H100 上 480p 生成仅需 13.2 秒，720p/5 秒视频生成需 13.06 秒，VBench 得分为 84.30。目前尚未发布代码、权重或许可证。

reddit · r/StableDiffusion · /u/mmowg · 8月3日 00:11

**背景**: 视频扩散变压器通过迭代去噪随机噪声来生成视频，但由于全注意力的二次方成本，它们常常难以处理长序列。线性注意力降低了这一成本，但可能面临低秩瓶颈。SANA-Video 2.0 通过将线性注意力与周期性 softmax 锚点和块注意力残差相结合来解决这一问题，块注意力残差将 softmax 层的高秩特征传播到后续线性层。Sol-Engine 是一个独立的加速框架，通过内核融合、缓存和量化来优化推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.21553">[2607.21553] SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient Video Generation</a></li>
<li><a href="https://nvlabs.github.io/Sana/Video2/">SANA-Video 2.0 | Efficient Video Generation</a></li>
<li><a href="https://arxiv.org/abs/2606.23743">[2606.23743] Sol Video Inference Engine: Agent-Native Full-Stack Acceleration Framework for Efficient Video Generation</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论可能聚焦于其出色的性能和架构创新，用户对 NVIDIA 可能像 SANA 图像模型那样采用 Apache 2.0 许可发布表示兴奋。然而，鉴于近期 PiD 和 Flux 等模型闭源，用户可能对 NVIDIA 的实际意图持怀疑态度。

**标签**: `#video generation`, `#diffusion models`, `#NVIDIA`, `#attention mechanisms`, `#AI research`

---

<a id="item-14"></a>
## [NVIDIA 的 Sol-Attn 通过即时注意力稀疏化加速视频生成](https://www.reddit.com/r/StableDiffusion/comments/1vdsuz4/solattn_accelerating_video_generation_inference/) ⭐️ 8.0/10

NVIDIA Labs 推出了 Sol-Attn，一种无需训练的即时注意力稀疏化方法，可加速扩散变压器中的视频生成推理。该方法在推理过程中动态剪枝注意力计算，减少长 token 序列带来的瓶颈。 这一创新解决了视频生成中的关键瓶颈，即长 token 序列上的注意力计算成本高昂。通过无需重新训练即可加速推理，它可能使高保真视频生成在实时应用和更广泛采用中更加实用。 Sol-Attn 无需训练，可与预训练的视觉生成器配合使用，这使其区别于需要微调的方法。该方法在 arXiv 论文（2607.24027）和 NVIDIA Labs 的 Sana 项目页面上进行了介绍。

reddit · r/StableDiffusion · /u/Total-Resort-3120 · 8月2日 20:36

**背景**: 扩散变压器对于高保真视频生成至关重要，但由于长 token 序列上的注意力计算，其计算成本很高。无需训练的动态稀疏注意力方法旨在通过选择性地跳过不太重要的注意力计算来加速推理，而 Sol-Attn 是该领域的一个新贡献。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvlabs.github.io/Sana/Sol-Attn/">Sol-Attn | On-the-Fly Attention Sparsification</a></li>
<li><a href="https://paperswithcode.co/paper/2607.24027">Sol-Attn: Accelerating Video Generation Inference via On-the-Fly...</a></li>

</ul>
</details>

**标签**: `#video generation`, `#attention sparsification`, `#inference acceleration`, `#NVIDIA`, `#AI research`

---

<a id="item-15"></a>
## [欧盟人工智能法案第 50 条生效：强制披露 AI 生成内容](https://www.reddit.com/r/artificial/comments/1vdlbbx/the_eu_ai_act_makes_failure_to_disclose/) ⭐️ 8.0/10

8 月 2 日，欧盟《人工智能法案》第 50 条生效，要求部署 AI 系统生成或操纵文本以向公众提供公共信息时，必须披露该文本为 AI 生成。除非内容经过人工审查或编辑控制，或用于执法目的，否则此义务适用。 该法规对不合规行为引入了重大处罚，直接影响像普华永道这样被发现在报告中使用 AI 幻觉生成内容的咨询公司。这标志着欧盟在 AI 生成内容的问责和透明度方面迈出了重要一步，为其他地区树立了先例。 披露必须清晰、可区分，并且自然人无需技术工具即可感知。对于经过人工审查或编辑控制的内容以及执法用途存在豁免。该法规还与关于 AI 生成内容透明度的《实践准则》保持一致。

reddit · r/artificial · /u/SpiritRealistic8174 · 8月2日 15:41

**背景**: 欧盟《人工智能法案》是一项全面的 AI 监管法规，其中第 50 条侧重于 AI 生成内容的透明度义务。AI 系统中的“幻觉”现象，即模型生成虚假或捏造信息，已成为关注点，尤其是在准确性至关重要的咨询报告中。该法案旨在减轻信息生态系统中欺骗和操纵的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act">Transparency obligations under Article 50 of the AI Act | Shaping Europe’s digital future</a></li>
<li><a href="https://artificialintelligenceact.eu/transparency-rules-article-50/">The EU AI Act’s Transparency Rules: A Practical Guide to Article 50 | EU Artificial Intelligence Act</a></li>
<li><a href="https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content">Code of Practice on Transparency of AI-generated Content | Shaping Europe’s digital future</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论中提到了普华永道和德勤等咨询公司因 AI 幻觉而面临后果的真实案例，一些用户表示支持该法规，而另一些则质疑其执行可行性。总体情绪是积极的，认为该法案是让组织承担责任必要的一步。

**标签**: `#EU AI Act`, `#AI regulation`, `#content disclosure`, `#compliance`, `#AI-generated content`

---