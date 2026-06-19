---
layout: default
title: "Horizon Summary: 2026-06-19 (ZH)"
date: 2026-06-19
lang: zh
---

> 从 157 条内容中筛选出 15 条重要资讯。

---

1. [发现 1 万个 GitHub 仓库分发木马恶意软件](#item-1) ⭐️ 9.0/10
2. [Poolside 发布 Laguna M.1：面向智能体编程的 225B MoE 模型](#item-2) ⭐️ 9.0/10
3. [cuTile Rust：利用 Rust 所有权实现安全的 GPU 并发](#item-3) ⭐️ 9.0/10
4. [Superpowers：GitHub 上热门的智能体技能框架](#item-4) ⭐️ 8.0/10
5. [MolmoMotion：基于语言指令的 3D 点轨迹预测](#item-5) ⭐️ 8.0/10
6. [Kairos：面向物理 AI 的原生世界模型栈](#item-6) ⭐️ 8.0/10
7. [Token 压缩幻觉：对 RTK 的质疑](#item-7) ⭐️ 8.0/10
8. [参议院通过《拯救 OOI 法案》保护海洋研究](#item-8) ⭐️ 8.0/10
9. [SK 电信深陷 Anthropic Mythos 争议中心](#item-9) ⭐️ 8.0/10
10. [AI 推理模型助力诊断儿童罕见遗传病](#item-10) ⭐️ 8.0/10
11. [行李箱机器人通过真实气体传感器改变 LLM 采样器而“嗨”起来](#item-11) ⭐️ 8.0/10
12. [开源模型市场份额超越闭源模型](#item-12) ⭐️ 8.0/10
13. [Flux.2-klein 被用作视频模型](#item-13) ⭐️ 8.0/10
14. [RNN vs Transformer vs SSM：AI 记忆应该放在哪里？](#item-14) ⭐️ 8.0/10
15. [棋盘 FEN 揭示 VLM 空间推理缺陷](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [发现 1 万个 GitHub 仓库分发木马恶意软件](https://orchidfiles.com/github-repositories-distributing-malware/) ⭐️ 9.0/10

一名安全研究人员发现超过 1 万个 GitHub 仓库正在分发木马恶意软件，这些仓库利用自动化技术逃避检测并针对依赖搜索代理。 这一广泛威胁凸显了重大的供应链攻击途径，自动化代理可能无意中将这些恶意仓库作为依赖项包含进来，从而可能感染数千个下游项目。 攻击者克隆新仓库而非流行仓库，并每隔几小时删除提交并推送新提交以保持隐蔽。这种行为旨在逃避安全工具的检测，并出现在依赖搜索代理的搜索结果中。

hackernews · theorchid · 6月18日 11:45 · [社区讨论](https://news.ycombinator.com/item?id=48583928)

**背景**: 软件供应链攻击针对开源项目的依赖链，恶意代码可通过被攻破的依赖项引入。依赖搜索代理是帮助开发者查找和包含库的自动化工具，但它们可能被欺骗而推荐恶意仓库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://socket.dev/blog/dependency-search">Introducing Dependency Search - Socket</a></li>
<li><a href="https://openssf.org/blog/2025/01/23/predictions-for-open-source-security-in-2025-ai-state-actors-and-supply-chains/">AI, State Actors, and Supply Chains – Open Source Security Foundation</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，该攻击针对的是自动化代理而非人类，并且类似的冒充攻击也发生在合法的开源维护者身上。一些人分享了他们的名字被附加到未知恶意项目上的亲身经历。

**标签**: `#security`, `#malware`, `#github`, `#supply chain attack`, `#open source`

---

<a id="item-2"></a>
## [Poolside 发布 Laguna M.1：面向智能体编程的 225B MoE 模型](https://www.reddit.com/r/LocalLLaMA/comments/1u9b2i3/poolsidelagunam1_hugging_face_225ba23b/) ⭐️ 9.0/10

Poolside 发布了 Laguna M.1，这是一个 225B 参数的混合专家模型，每个 token 激活 23B 参数，针对智能体编程和长周期任务进行了优化，采用 Apache 2.0 许可证。 该模型在 SWE-bench Verified（74.6%）和 Terminal-Bench 2.0（45.8%）等智能体编程基准测试中与前沿模型竞争，使先进的编程 AI 更易于开源社区使用。 Laguna M.1 使用 256 个专家和 top-k=16 路由，70 层全局注意力，支持 262,144 token 的上下文窗口，并支持推理与工具调用的交错执行。

reddit · r/LocalLLaMA · /u/pmttyji · 6月18日 16:30

**背景**: 混合专家（MoE）是一种神经网络架构，每个输入仅激活部分参数，从而在不成比例增加计算成本的情况下扩大模型容量。Laguna M.1 使用的无辅助损失负载均衡避免了可能干扰训练的额外损失项。SwiGLU 是一种门控激活函数，可提升现代 Transformer 的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2408.15664">Auxiliary - Loss - Free Load Balancing Strategy for Mixture-of-Experts</a></li>
<li><a href="https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/">Applying Mixture of Experts in LLM Architectures | NVIDIA Technical Blog</a></li>

</ul>
</details>

**社区讨论**: 一位 Reddit 用户分享了在 4×3090 GPU 上部署类似大型 MoE 模型（GLM-5.2）的实践经验，指出卸载专家时解码速度受 CPU 限制，且从 IQ2 量化到 IQ1 并未提升吞吐量。

**标签**: `#LLM`, `#Mixture-of-Experts`, `#Agentic Coding`, `#Open Source`, `#AI`

---

<a id="item-3"></a>
## [cuTile Rust：利用 Rust 所有权实现安全的 GPU 并发](https://www.reddit.com/r/MachineLearning/comments/1u9j7md/fearless_concurrency_on_the_gpu_safe_gpu/) ⭐️ 9.0/10

研究人员推出了 cuTile Rust，一种基于 tile 的 GPU 编程模型，利用 Rust 的所有权和借用检查机制来保证 GPU 内核的内存安全和无数据竞争。他们还基于 cuTile Rust 构建了 Grout——一个 Qwen3 推理引擎，性能与 vLLM 和 SGLang 相当（例如，在 RTX 5090 上 Qwen3-4B 达到 171 tok/s）。 这项工作通过提供编译器验证的安全保证，解决了 AI 生成的 GPU 代码中日益增长的信任瓶颈。它有望实现更安全、更可靠的 GPU 编程，尤其是在 AI 生成内核日益普及的背景下，并证明了安全性可以在不牺牲性能的前提下实现。 cuTile Rust 编译到 CUDA Tile IR，将 Rust 的所有权模型跨越主机-设备边界。Grout 目前使用了一些不安全的内核，但提供了迁移到安全变体的路径；在 B200 上，安全 GEMM 性能与手写底层版本相差不到 0.3%，逐元素操作达到约 7 TB/s。

reddit · r/MachineLearning · /u/Exciting_Suspect9088 · 6月18日 21:36

**背景**: 传统的 GPU 编程（如 CUDA）依赖于线程级 SIMT 模型，容易引入数据竞争和内存安全漏洞。Rust 的所有权系统在编译时强制执行严格规则，以防止 CPU 代码中的此类问题。cuTile Rust 通过使用基于 tile 的抽象将此扩展到 GPU，其中内核操作输出张量的不相交可变分区，从而从构造上保证安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/nvlabs/cutile-rs">GitHub - NVlabs/cutile-rs: cuTile Rust provides a safe, tile-based kernel...</a></li>
<li><a href="https://arxiv.org/abs/2606.15991">[2606.15991] Fearless Concurrency on the GPU</a></li>
<li><a href="https://arxiv.org/html/2606.15991">Fearless Concurrency on the GPU</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论（未完全显示）可能涉及实际采用、与现有安全 GPU 方法的比较以及对安全保证的热情。作者正在积极与社区互动回答问题。

**标签**: `#Rust`, `#GPU`, `#concurrency`, `#machine learning`, `#inference`

---

<a id="item-4"></a>
## [Superpowers：GitHub 上热门的智能体技能框架](https://github.com/obra/superpowers) ⭐️ 8.0/10

GitHub 仓库 obra/superpowers 单日获得 1429 颗星，总星数超过 23.2 万，推出了一款面向 AI 编码智能体的开源智能体技能框架与软件开发方法论。 这种快速增长表明社区对标准化智能体工作流程有强烈兴趣，可能影响整个行业构建和使用 AI 编码智能体的方式。 该框架使用 Shell 编写，面向 Claude Code、Cursor、Codex、OpenCode 和 Gemini CLI 等智能体，强调基于上下文触发的可组合技能。

github_trending · GitHub Trending · 6月19日 04:25

**背景**: 智能体技能框架提供可复用、可组合的模块来扩展 AI 智能体的能力。Superpowers 是智能体工程生态中众多新兴工具之一，该生态还包括 Kilo、OpenMontage 和 crewAI 等平台，都旨在让 AI 智能体更加自主和高效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Superpowers_agentic_skills_framework">Superpowers (agentic skills framework)</a></li>
<li><a href="https://rywalker.com/research/agentic-skills-frameworks">Agentic Skills Frameworks Compared | Ry Walker Research</a></li>

</ul>
</details>

**标签**: `#agentic-framework`, `#software-development`, `#AI`, `#methodology`, `#open-source`

---

<a id="item-5"></a>
## [MolmoMotion：基于语言指令的 3D 点轨迹预测](https://huggingface.co/papers/2606.18558) ⭐️ 8.0/10

研究人员推出了 MolmoMotion 模型，该模型根据视觉历史记录和语言指令预测 3D 点轨迹，同时发布了 MolmoMotion-1M 数据集和 PointMotionBench 基准。 这项工作使机器人能够根据语言指令更好地理解和预测物体运动，从而改进操作规划，同时还能指导视频生成模型产生更逼真的运动。 MolmoMotion 支持自回归坐标预测和基于流匹配的轨迹生成，在涵盖 111 个物体类别和 61 种运动类型的 PointMotionBench 上显著优于现有基线。

huggingface_papers · Hugging Face Papers · 6月18日 00:00

**背景**: 运动预测对于视觉智能至关重要，它使智能体能够预测物体运动以进行规划和推理。世界坐标系中的 3D 点轨迹提供了一种与类别无关、视角稳定的表示，这种表示紧凑且可直接用于机器人操作和视频合成等下游任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/papers/2606.18558">Paper page - MolmoMotion: Forecasting Point Trajectories in 3 D with...</a></li>
<li><a href="https://allenai.org/blog/molmo-motion">MolmoMotion: Language-guided 3D motion forecasting | Ai2</a></li>
<li><a href="https://molmomotion.github.io/">MolmoMotion: Forecasting Point Trajectories in 3D with Language Instruction</a></li>

</ul>
</details>

**标签**: `#3D motion forecasting`, `#language-conditioned`, `#robot manipulation`, `#video generation`, `#dataset`

---

<a id="item-6"></a>
## [Kairos：面向物理 AI 的原生世界模型栈](https://huggingface.co/papers/2606.16533) ⭐️ 8.0/10

研究人员推出了 Kairos，这是一个原生世界模型框架，通过跨具身数据课程从多样化数据中学习，利用混合线性时间注意力维持持久状态，并支持在服务器和消费级硬件上高效部署。 Kairos 解决了物理 AI 中的关键挑战，使世界模型能够原生地从异构经验中获取知识、保持长时程状态持久性，并在实际部署中高效运行，有望加速机器人和自主系统领域的进展。 该框架引入了带有跨具身数据课程的原生预训练范式、具有混合线性时间注意力（滑动窗口、膨胀滑动窗口和门控线性注意力）的原生统一架构，以及面向低延迟部署的部署感知系统协同设计。理论界限表明，时间分解限制了长时程上的误差累积。

huggingface_papers · Hugging Face Papers · 6月18日 00:00

**背景**: 世界模型是构建物理现实内部表征的 AI 系统，能够理解因果关系、预测未来状态并规划行动。它们正从被动的视觉生成器转变为物理 AI 的基础设施，物理 AI 包括自动驾驶和机器人等应用。跨具身学习聚合来自多种机器人类型的数据以提高泛化能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://govt.chinadaily.com.cn/s/202512/03/WS693019bd498e23165e06b500/world-models-new-driver-for-auto-autonomy.html">World models new driver for auto autonomy | govt.chinadaily.com.cn</a></li>
<li><a href="https://www.humai.blog/world-models-the-quiet-ai-revolution-that-could-make-llms-look-like-a-warmup-act/">World Models : The Quiet AI Revolution That Could Make LLMs Look...</a></li>
<li><a href="https://medium.com/@jianming.wang07/robotic-foundation-models-corl-2024-sergey-levines-talk-notes-e42bb3eb618e">“How Real-World Cross-Embodiment Data Will Lead to Robotic Foundation Models”-CoRL 2024 Sergey Levine’s Talk Notes | by Wang Jianming | Medium</a></li>

</ul>
</details>

**标签**: `#world models`, `#physical AI`, `#robotics`, `#deep learning`, `#AI infrastructure`

---

<a id="item-7"></a>
## [Token 压缩幻觉：对 RTK 的质疑](https://mroczek.dev/articles/the-token-compression-illusion-why-im-skeptical-of-rtk/) ⭐️ 8.0/10

一篇由软件工程师撰写的批判性文章质疑 RTK（Rust Token Killer）的准确性和成本节省有效性，RTK 是一个声称可将常见开发命令的 LLM token 消耗减少 60-90%的 CLI 代理。 这种质疑凸显了 LLM 工具生态系统中对严格基准测试和透明度的日益增长的需求，在该生态系统中，炒作往往超过证据，影响依赖成本节省声明的开发者和公司。 文章指出，RTK 声称的节省可能被游戏化（例如，在 390 万输入 token 中节省 370 万 token），并且缺乏准确性基准，尽管一些用户报告没有关键信息丢失。

hackernews · lackoftactics · 6月18日 17:37 · [社区讨论](https://news.ycombinator.com/item?id=48588755)

**背景**: Token 压缩技术旨在减少 LLM 处理的 token 数量，从而降低成本和延迟。RTK 是一个开源的 Rust 二进制文件，在 CLI 输出到达 LLM 上下文之前对其进行过滤和压缩，声称平均压缩率高达 89%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/rtk-ai/rtk">GitHub - rtk-ai/rtk: CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies · GitHub</a></li>
<li><a href="https://www.rtk-ai.app/">RTK — Rust Token Killer</a></li>
<li><a href="https://madplay.github.io/en/post/rtk-reduce-ai-coding-agent-token-usage">I Only Compressed CLI Output, Yet Tokens Dropped by 80%? | MadPlay🚀</a></li>

</ul>
</details>

**社区讨论**: 社区讨论呈现两极分化：一些人同意质疑，呼吁更严格的评估，而另一些人则为 RTK 辩护，指出 token 节省是真实的，且未观察到准确性下降。作者承认撰写文章是因为对炒作和缺乏准确性指标的担忧。

**标签**: `#LLM`, `#token compression`, `#RTK`, `#critical analysis`, `#AI engineering`

---

<a id="item-8"></a>
## [参议院通过《拯救 OOI 法案》保护海洋研究](https://www.nsf.gov/news/update-ocean-observatories-initiative) ⭐️ 8.0/10

6 月 17 日，美国参议院一致通过了《拯救 OOI 法案》，这项两党法案禁止国家科学基金会拆除或缩减海洋观测计划（OOI）。 这项立法保护了一个关键的气候研究网络，该网络提供实时海洋数据，对于理解气候变化、厄尔尼诺和海洋生态系统至关重要，避免了全球科学的重大损失。 该法案仍需在众议院通过才能成为法律。OOI 在大西洋和太平洋的五个阵列上运行着 900 多个仪器，收集物理、化学和生物数据。

hackernews · andsoitis · 6月18日 23:41 · [社区讨论](https://news.ycombinator.com/item?id=48593093)

**背景**: 海洋观测计划（OOI）是由美国国家科学基金会资助的海洋观测站网络，测量从海底到大气的各种变量。它为气候、海洋酸化和海洋生态系统研究提供长期实时数据。《拯救 OOI 法案》的提出是为了应对 OOI 可能因预算或政策决定而被拆除的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.merkley.senate.gov/merkley-murkowski-lead-the-charge-to-block-the-dismantling-of-one-of-a-kind-ocean-monitoring-network/">Merkley, Murkowski Lead the Charge to Block the Dismantling of One-Of ...</a></li>
<li><a href="https://www.govtrack.us/congress/bills/119/s4822">Saving the OOI Act of 2026 (S. 4822) - GovTrack.us</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ocean_Observatories_Initiative">Ocean Observatories Initiative</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了宽慰和乐观，一些人指出了国会与管理和预算办公室之间关于扣押资金的更广泛背景。一位用户质疑是否有陷阱，而其他人则强调了 NASA 和其他机构面临的持续挑战。

**标签**: `#science policy`, `#oceanography`, `#climate research`, `#US legislation`

---

<a id="item-9"></a>
## [SK 电信深陷 Anthropic Mythos 争议中心](https://www.wired.com/story/sk-telecom-anthropic-mythos-export-controls/) ⭐️ 8.0/10

《连线》报道称，韩国电信巨头、Anthropic 投资者 SK 电信被白宫要求撤销对 Anthropic 的 Mythos AI 模型的访问权限，原因是出口管制担忧，从而引发了 Mythos 争议。 这一事件凸显了 AI 领域不断升级的地缘政治紧张局势，出口管制被用于限制外国对先进模型的访问，可能重塑国际 AI 合作与投资格局。 SK 电信在 2023 年向 Anthropic 投资 1 亿美元，并建立商业合作伙伴关系以开发电信专用 AI 模型。白宫干预专门针对 Mythos，Anthropic 立即遵从。

hackernews · dstala · 6月18日 12:44 · [社区讨论](https://news.ycombinator.com/item?id=48584484)

**背景**: Mythos 是 Anthropic 的强大 AI 模型，出口管制是政府对向外国实体分享敏感技术的限制。该争议涉及对中国关联团体访问 Mythos 的怀疑，导致对外国国民的更广泛限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/sk-telecom-anthropic-mythos-export-controls/">The Korean Telecom Giant at the Center of... | WIRED</a></li>
<li><a href="https://www.semafor.com/article/06/13/2026/white-house-move-to-limit-anthropic-linked-to-concerns-about-chinese-access-to-mythos">White House move to limit Anthropic linked to concerns about Chinese access to Mythos | Semafor</a></li>

</ul>
</details>

**社区讨论**: 评论者争论白宫行动是否出于政治动机，有人认为这是针对 Anthropic 因其被认为的自由派倾向，而其他人则关注对外国公司对美国 AI 供应商信任的实际影响。

**标签**: `#AI`, `#geopolitics`, `#export controls`, `#Anthropic`, `#SK Telecom`

---

<a id="item-10"></a>
## [AI 推理模型助力诊断儿童罕见遗传病](https://openai.com/index/diagnose-rare-childhood-diseases) ⭐️ 8.0/10

研究人员使用 OpenAI 的推理模型分析儿童罕见遗传病的未解病例，成功做出 18 个此前医生未能诊断出的新诊断。 这展示了先进 AI 推理在医疗领域的实际影响力，有望减少罕见病的诊断延迟，改善患儿及其家庭的治疗结果。 该研究使用了 OpenAI 的 o1 推理模型，该模型在诊断推理任务中优于早期模型甚至人类医生，近期 HealthBench 等基准测试已证实这一点。

rss · OpenAI Blog · 6月18日 08:00

**背景**: 罕见遗传病常因复杂性及缺乏专科知识而多年无法确诊。结合临床数据、遗传信息和医学文献的 AI 模型能够提出诊断建议并提供推理过程，帮助医生识别可能遗漏的疾病。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/healthbench/">Introducing HealthBench - OpenAI</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-00290-9">AI succeeds in diagnosing rare diseases</a></li>

</ul>
</details>

**标签**: `#AI in Healthcare`, `#Rare Diseases`, `#OpenAI`, `#Reasoning Models`, `#Medical Diagnosis`

---

<a id="item-11"></a>
## [行李箱机器人通过真实气体传感器改变 LLM 采样器而“嗨”起来](https://www.reddit.com/r/LocalLLaMA/comments/1u9a17y/my_suitcase_robot_gets_high_now_off_a_real_gas/) ⭐️ 8.0/10

一个名为 Sparky 的行李箱机器人使用 MQ-2 气体传感器检测烟雾，并实时动态调整 LLM 采样参数（temperature、top_p、top_k），使其响应逐渐变得“迷幻”且多样化，无需任何预设的“嗨模式”。 该项目展示了物理传感器输入与 LLM 采样的新颖集成，使具身 AI 能够产生真正涌现且不可预测的行为。它为交互式艺术和机器人技术开辟了创造性可能性，使环境刺激直接影响 AI 认知。 MQ-2 传感器每 0.5 秒读取一次，烟雾触发转化为 0-10 的相位，并在数分钟内衰减。随着相位增加，temperature 从 1.0 升至约 1.6，top_p 从 0.95 升至 0.99，top_k 从 64 升至 120，导致选择低概率 token。

reddit · r/LocalLLaMA · /u/CreativelyBankrupt · 6月18日 15:52

**背景**: LLM 采样参数如 temperature、top_p 和 top_k 控制生成文本的随机性和多样性。较高的 temperature 增加随机性，而 top_p（核采样）和 top_k 限制 token 池。MQ-2 是一种半导体气体传感器，可检测多种可燃气体和烟雾，但无法区分大麻烟雾与其他烟雾或 VOC。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/MQ-2_and_MQ-9_gas_sensors">MQ-2 and MQ-9 gas sensors</a></li>
<li><a href="https://aviralrma.medium.com/understanding-llm-parameters-c2db4b07f0ee">Understanding temperature, top_p, top_k, logit_bias in LLM parameters</a></li>
<li><a href="https://www.promptingguide.ai/introduction/settings">LLM Settings - Prompt Engineering Guide</a></li>

</ul>
</details>

**社区讨论**: 社区称赞了这种创意集成和幽默感，许多人询问传感器的特异性。创作者指出 MQ-2 无法区分大麻烟雾与普通烟雾，并征求硬件改进建议，引发了关于气体传感器阵列和机器学习方法的讨论。

**标签**: `#LLM`, `#embodied AI`, `#creative coding`, `#sensor integration`, `#local LLM`

---

<a id="item-12"></a>
## [开源模型市场份额超越闭源模型](https://www.reddit.com/r/LocalLLaMA/comments/1u96545/oss_models_decisively_overtook_proprietary_models/) ⭐️ 8.0/10

根据 OpenRouter 最近三个月的数据，开源模型在市场份额上已决定性地超越闭源模型，标志着 AI 模型格局的历史性转变。 这一趋势表明开源 AI 的信任度和采用率正在上升，可能加速创新、降低成本，并使全球开发者和企业更容易获得先进的 AI 能力。 数据来自 OpenRouter（一个统一 API 网关，可在 60 多个提供商之间路由请求），分析显示开源模型目前消耗的总 token 份额已超过闭源模型。

reddit · r/LocalLLaMA · /u/Comfortable-Rock-498 · 6月18日 13:21

**背景**: OpenRouter 是一家以开发者为中心的 AI 基础设施初创公司，提供访问多个提供商的各种大语言模型（LLM）的市场。该平台跟踪使用统计数据，包括按模型划分的 token 消耗量，这可以作为市场份额的代理指标。来自 Meta、Mistral 等公司的开源模型因其透明性、可定制性和较低成本而日益受到欢迎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/state-of-ai">State of AI 2025: 100T Token LLM Usage Study | OpenRouter</a></li>
<li><a href="https://openrouter.ai/data">Data - Authoritative AI Usage Data for Research | OpenRouter</a></li>
<li><a href="https://openrouter.ai/models">Models | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论普遍认同该数据，用户指出开源模型在微调和隐私方面的实际优势。一些评论者对方法论提出质疑，认为 OpenRouter 数据可能不代表整个市场，但总体情绪对开源势头持积极态度。

**标签**: `#open-source`, `#AI`, `#market share`, `#LLMs`, `#OpenRouter`

---

<a id="item-13"></a>
## [Flux.2-klein 被用作视频模型](https://www.reddit.com/r/StableDiffusion/comments/1u9lmzq/flux2klein_is_secretly_a_video_model_showing_some/) ⭐️ 8.0/10

一位 Reddit 用户展示了一种方法，通过结合光流和修补技术，将 Flux.2-klein 图像模型重新用于视频编辑，无需任何微调或 LoRA 即可生成编辑后的视频序列。 这项技术表明，图像模型可以被创造性地用于视频任务，可能降低视频生成和编辑的门槛，无需专门的视频模型或大量训练。 该流程使用光流将编辑后的第一帧扭曲到后续帧，应用前后一致性检查来遮蔽遮挡区域，然后使用 Flux.2-klein 的修补功能填充遮蔽区域，但结果仍然存在抖动。

reddit · r/StableDiffusion · /u/TensorForger · 6月18日 23:18

**背景**: Flux.2-klein 是 Black Forest Labs 推出的 40 亿参数整流流变压器，用于文本到图像生成和多参考编辑。光流估计帧间运动，修补则填充缺失区域。该方法结合这些技术，从静态图像模型实现类似视频的效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/black-forest-labs/FLUX.2-klein-4B">black-forest-labs/FLUX.2-klein-4B · Hugging Face</a></li>
<li><a href="https://bfl.ai/models/flux-2-klein">FLUX.2 [klein] - Fast, Efficient Image Generation | Black Forest Labs</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论可能称赞其创造性使用和技术深度，一些人指出输出抖动且有改进空间。用户可能讨论替代的光流方法或修补策略以提高质量。

**标签**: `#Flux`, `#video generation`, `#optical flow`, `#inpainting`, `#generative AI`

---

<a id="item-14"></a>
## [RNN vs Transformer vs SSM：AI 记忆应该放在哪里？](https://www.reddit.com/r/artificial/comments/1u9ba5s/rnns_vs_transformers_vs_ssms_where_should_ai/) ⭐️ 8.0/10

一篇 Reddit 帖子从新颖的角度比较了 RNN、Transformer 和 SSM：记忆存在于何处——是微小的循环状态、不断增长的 KV 缓存，还是模型的网络结构——并指出记忆与计算的比例是关键区别。 这种框架将 AI 架构的争论从循环与注意力转向更根本的记忆设计问题，可能影响未来面向持续学习和高效长上下文处理的模型开发。 帖子指出 RNN 的记忆与计算比例不佳（O(N^2)参数对 O(N)状态），而 Transformer 将过去激活存储在随序列长度增长的 KV 缓存中。SSM 和 BDH 等架构旨在将记忆更接近模型的连接结构，使用更大的神经元空间和稀疏正状态。

reddit · r/artificial · /u/dank_philosopher · 6月18日 16:39

**背景**: RNN（循环神经网络）通过维护每一步更新的隐藏状态来处理序列，但该状态是瓶颈。Transformer 使用自注意力和 KV 缓存来关注所有之前的 token，支持并行训练但需要不断增长的内存。SSM（状态空间模型）使用随时间演化的压缩状态表示，提供了折中方案。记忆与计算的比例指的是模型相对于其计算能力拥有的记忆容量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/lbourdois/get-on-the-ssm-train">Introduction to State Space Models (SSM)</a></li>
<li><a href="https://medium.com/@joaolages/kv-caching-explained-276520203249">Transformers KV Caching Explained | by João Lages | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_network_(machine_learning)">Neural network (machine learning) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 讨论线程中包含了对这些观点的实质性评论，一些人同意记忆架构是一个被低估的比较维度，而另一些人质疑 SSM 是否真正解决了记忆瓶颈或只是转移了它。总体情绪是积极且富有学术探讨精神的。

**标签**: `#RNNs`, `#Transformers`, `#SSMs`, `#memory architecture`, `#continual learning`

---

<a id="item-15"></a>
## [棋盘 FEN 揭示 VLM 空间推理缺陷](https://www.reddit.com/r/artificial/comments/1u9e5kn/a_chessboard_is_a_surprisingly_good_way_to_catch/) ⭐️ 8.0/10

VideoDB Labs 的研究人员发现，视觉语言模型（VLM）能正确识别棋子，但在要求输出 FEN 字符串时经常将棋子放在错误的格子上，这暴露了其在精确空间推理和结构化输出准确性方面的缺陷。 这一发现凸显了 VLM 能力中的一个关键缺口，而宽松的描述性基准测试无法捕捉到这一点，对需要精确空间理解的生产系统（如机器人或文档分析）有直接影响。 该基准测试使用 Forsyth–Edwards Notation（FEN）——一种棋盘位置的标准化文本表示——来测试 VLM 将视觉布局映射为结构化字符串的能力；像 GPT-4V 这样的模型尽管能识别棋子类型，却经常混淆棋子位置。

reddit · r/artificial · /u/Apart-Student-7298 · 6月18日 18:24

**背景**: Forsyth–Edwards Notation（FEN）是一种单行字符串，编码了棋盘上所有棋子的位置、轮到哪一方走棋、王车易位权利以及其他游戏状态。它广泛应用于国际象棋软件和数据库中。VLM 是同时处理图像和文本的 AI 模型，但其空间推理能力仍是一个已知的弱点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation">Forsyth–Edwards Notation - Wikipedia</a></li>
<li><a href="https://www.chess.com/terms/fen-chess">FEN (Forsyth-Edwards Notation) - Chess Terms - Chess .com</a></li>
<li><a href="https://github.com/mll-lab-nu/Awesome-Spatial-Intelligence-in-VLM">GitHub - mll-lab-nu/Awesome-Spatial-Intelligence-in-VLM: A paper list for spatial reasoning · GitHub</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论普遍认为这是一个巧妙的基准测试，用户指出在图表解析和地图阅读等任务中存在类似的失败。一些人建议，在 FEN 等结构化输出上进行训练可以提高空间推理能力，而另一些人则质疑这是否是 Transformer 架构固有的问题。

**标签**: `#VLM`, `#spatial reasoning`, `#benchmarking`, `#AI evaluation`, `#chess`

---