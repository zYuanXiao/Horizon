---
layout: default
title: "Horizon Summary: 2026-09-24 (ZH)"
date: 2026-09-24
lang: zh
---

> 从 151 条内容中筛选出 15 条重要资讯。

---

1. [美国联邦政府将 AI 批评者列为“外国代理人”，引发争议](#item-1) ⭐️ 8.0/10
2. [高通为骁龙 X2 系列带来 Linux 支持](#item-2) ⭐️ 8.0/10
3. [Anthropic 称 Claude 发现了一种新型类 CRISPR 酶系统](#item-3) ⭐️ 8.0/10
4. [代币便宜到无需计量：LLM 成本与工具调用的对比](#item-4) ⭐️ 8.0/10
5. [谷歌发布 Gemini 3.8 文本转语音，支持 30 秒语音克隆](#item-5) ⭐️ 8.0/10
6. [Radicle 披露网络协议严重漏洞：节点流量未加密未认证](#item-6) ⭐️ 8.0/10
7. [Claude Opus 5.5 成为 AINews 默认模型，行业价格普降 40-50%](#item-7) ⭐️ 8.0/10
8. [OpenAI 发布 MentalHealthBench，评估 AI 心理健康对话安全性](#item-8) ⭐️ 8.0/10
9. [Zenity Labs 演示投毒文档可致企业 AI 代理泄露数据](#item-9) ⭐️ 8.0/10
10. [谷歌开源 Go 语言智能体编排运行时 'ax'](#item-10) ⭐️ 8.0/10
11. [browser-use/video-use 让编程智能体编辑视频](#item-11) ⭐️ 8.0/10
12. [ComfyUI 今日新增 209 星，登顶 GitHub 趋势榜](#item-12) ⭐️ 8.0/10
13. [PACT：统一大语言模型强化学习中的词元级信用分配与评论家对齐](#item-13) ⭐️ 8.0/10
14. [Realtime-Venus：双 9B 模型实现主动式全双工对话](#item-14) ⭐️ 7.0/10
15. [Meta 发布新款 VR 眼镜，引发隐私争议](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [美国联邦政府将 AI 批评者列为“外国代理人”，引发争议](https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign) ⭐️ 8.0/10

Ken Klippenstein 的一篇报道称，美国联邦当局正将人工智能的批评者列为“外国代理人”，政府威胁对那些“推进外国势力的宣传或其他目标”的人追究“刑事责任”。该报道在 Hacker News 上引发了 61 条评论的激烈讨论，涉及言论自由、威权主义和 AI 监管等话题。 这一事态在科技政策辩论中引发了对公民自由和言论自由的严重担忧，因为 AI 的批评者可能以国家安全为名面临国家镇压。它可能压制关于 AI 风险的合法公共讨论，并为利用“外国代理人”标签压制国内异见开创先例，影响研究人员、活动人士和行业怀疑者。 政府威胁对“推进外国势力的宣传或其他目标”的人追究“刑事责任”，评论者将这一策略与俄罗斯和中国的《外国代理人法》相提并论。原文章设有付费墙，摘录中未提供关于具体案件或个人的技术细节。

hackernews · nmeagent · 9月24日 00:41 · [社区讨论](https://news.ycombinator.com/item?id=49824686)

**背景**: 《外国代理人法》要求接受外国资金或代表外国利益的个人或组织向政府登记；俄罗斯 2012 年的相关法律因压制非政府组织和独立媒体而广受批评。在美国，《外国代理人登记法》（FARA）历来针对游说者和宣传人员，但将其扩大到 AI 批评者将是一种新颖且有争议的应用。这场辩论正值全球对 AI 安全以及大型科技公司监管俘获的担忧日益加剧之际。

**社区讨论**: 评论者意见尖锐对立：一些人认为中国正在放大 AI 反对声音，并引用司法部案例作为证据；另一些人则反驳说，美国科技公司 CEO 自己就警告 AI 存在灭绝风险，因此“外国代理人”标签毫无必要。多位用户谴责这一策略是直接照搬俄罗斯和中国的威权主义套路，其中一人指出情况“远比标题所暗示的严重”，因为它涉及对 AI 批评者的刑事起诉。

**标签**: `#AI policy`, `#free speech`, `#government regulation`, `#authoritarianism`, `#tech politics`

---

<a id="item-2"></a>
## [高通为骁龙 X2 系列带来 Linux 支持](https://www.qualcomm.com/news/onq/2026/09/snapdragon-summit-agentic-ai-pcs-linux) ⭐️ 8.0/10

高通在骁龙峰会上宣布，骁龙 X2 系列将获得 Linux 支持，公司正将 Hexagon NPU 和 Adreno GPU 的核心驱动上游到主线内核。此举向开发者和合作伙伴开放该平台，而不是维持半专有式的支持。 这对 ARM 笔记本生态是重要一步，因为此前骁龙 X Elite 的 Linux 支持有限，常常成为用户购买的阻碍。驱动上游后，各发行版只需开启配置选项即可支持，而无需维护树外补丁，有望让高性能 ARM Linux 笔记本成为现实选择。 此次上游涵盖 Hexagon NPU 和 Adreno GPU，社区报告显示这些机器上 ARM EL2 可正常工作，意味着具备前几代所没有的 KVM 虚拟化支持。OpenBSD 开发者 Tobias Heider 已提交首批 OpenBSD/arm64 支持，使 HP Elitebook X G2q 在 ACPI 模式下的 USB、键盘和触摸板可以工作。

hackernews · aaronday · 9月23日 22:38 · [社区讨论](https://news.ycombinator.com/item?id=49823582)

**背景**: 上游化是指将驱动代码提交到官方 Linux 内核项目并合并维护，而不是单独发布补丁；这样各发行版只需启用配置选项即可支持硬件。Hexagon NPU 是高通用于端侧 AI 负载的神经网络处理单元，Adreno 则是其骁龙处理器中集成的 GPU 系列。骁龙 X2 是高通最新的基于 ARM 的笔记本芯片系列，与苹果 M 系列以及 Intel、AMD 的 x86 产品竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bootlin.com/engineering/upstreaming/">Upstreaming Linux kernel, drivers and bootloader code – Bootlin</a></li>
<li><a href="https://kernelnewbies.org/UpstreamMerge">UpstreamMerge - Linux Kernel Newbies</a></li>
<li><a href="https://en.wikipedia.org/wiki/Adreno">Adreno - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎这一消息，有人指出高通的 X2 芯片是笔记本形态下最接近苹果 M 系列的竞争者，并优于 Intel 和 AMD 的最佳产品。其他人强调了早期 OpenBSD/arm64 工作并确认了 KVM 支持，也有人对初代 X Elite 未能兑现 Linux 支持承诺表示失望，希望这次会有所不同。

**标签**: `#Linux`, `#Qualcomm`, `#Snapdragon`, `#ARM`, `#Hardware`

---

<a id="item-3"></a>
## [Anthropic 称 Claude 发现了一种新型类 CRISPR 酶系统](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) ⭐️ 8.0/10

Anthropic 宣布其 Claude 模型在一种已知逆转录酶附近识别出一段此前未被描述的类 CRISPR 重复序列阵列，并将该结构命名为阵列相关逆转录酶（ART）。这一声明引发了关于该发现新颖性以及 AI 驱动科学未来的争论。 如果得到验证，这一发现将成为 AI 用于科学的重要里程碑，表明大语言模型能够从原始序列数据中找出候选生物系统。它还加剧了一场更广泛的争论：AI 智能体究竟是真正的科学合作者，还是仅仅在做模式匹配，同时也凸显了 Anthropic 在生物工程问题上自相矛盾的立场。 这一新识别出的系统被称为阵列相关逆转录酶（ART），它将一种逆转录酶与相邻的伙伴基因以及一段由均匀间隔 DNA 重复序列组成的长阵列结合在一起，其结构与 CRISPR 系统相似。评论者提醒说，该发现建立在一种已知的类逆转录子（retron）逆转录酶之上，因此更审慎的表述应是：Claude 在一种已知酶附近识别出了一段此前未被描述的基因组排列。

hackernews · raahelb · 9月23日 18:06 · [社区讨论](https://news.ycombinator.com/item?id=49820134)

**背景**: CRISPR 系统是细菌的免疫机制，它把病毒 DNA 片段储存为重复序列阵列，并用其靶向并切割匹配序列，这正是现代基因编辑的基础。逆转录酶是能把 RNA 反向转录为 DNA 的酶，存在于多种原核生物防御系统中，包括某些 CRISPR-Cas 变体。像 Claude 这样的 AI 模型正越来越多地被用于扫描大规模基因组数据并生成假设，但其输出仍需实验验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://interestingengineering.com/ai-robotics/claude-discovers-crispr-like-enzyme-system">Claude scans 200,000 enzymes, uncover CRISPR -like system in...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reverse_transcriptase">Reverse transcriptase - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7757702/">CRISPR Arrays Away from cas Genes - PMC - NIH</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对炒作持怀疑态度，指出该发现围绕一种已知的类逆转录子逆转录酶展开，而且 CRISPR 的临床应用主要受递送限制，而非靶向能力。也有人对通过智能体对话记录重温发现过程感到兴奋，同时有人批评 Anthropic 一边警告不要将 Claude 用于生物工程，一边又宣扬一项基因编辑发现，并质疑大语言模型究竟如何能对生物化学进行推理。

**标签**: `#AI-for-science`, `#CRISPR`, `#genomics`, `#Anthropic`, `#bioethics`

---

<a id="item-4"></a>
## [代币便宜到无需计量：LLM 成本与工具调用的对比](https://jyn.dev/tokens-too-cheap-to-meter/) ⭐️ 8.0/10

jyn.dev 上的一篇文章认为，LLM 代币正变得如此便宜，可能很快就会比 grep 等工具调用更便宜，并指出调用 GPT-5.6 Luna 仅比 grep 贵 4-5 个数量级。该文章在 Hacker News 上引发了 249 分、185 条评论的热烈讨论，探讨成本降低的极限和 AI 商业模式的可持续性。 如果 LLM 调用变得比本地工具调用更便宜，可能会从根本上改变开发者构建和使用 AI 代理的方式，改变软件工具和自动化的经济性。讨论还凸显了更广泛的担忧：当前 AI 基础设施投资能否被未来利润所证明。 文章的预测依赖于对当前成本降低速度的外推，但评论者指出这种效率提升不可能永远持续，并引用了斯坦因定律。比较还取决于 grep 调用的具体成本，grep 在计算方面基本免费，但可能在延迟或开发者时间上有隐藏成本。

hackernews · teoruiz · 9月23日 09:21 · [社区讨论](https://news.ycombinator.com/item?id=49813482)

**背景**: “便宜到无需计量”一词源自 1954 年刘易斯·斯特劳斯关于核能的演讲，他预测电力将变得如此便宜以至于无需计量。在 LLM 语境中，代币是模型处理的文本单位，由于竞争和效率提升，其成本一直在快速下降。像 grep 这样的工具调用是开发者用来搜索代码的标准命令行实用程序，通常在本地运行是免费的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.llm-prices.com/">LLM pricing calculator</a></li>
<li><a href="https://pricepertoken.com/">Price Per Token</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对“便宜到无需计量”的类比持怀疑态度，一些人引用斯坦因定律认为成本降低不可能无限持续。其他人批评文章忽视了商业模式的可行性，指出巨额基础设施投资需要未来利润来支撑，而这可能无法实现。还有人提到核能未能兑现承诺的历史教训作为警示。

**标签**: `#LLM`, `#AI economics`, `#cost trends`, `#Hacker News discussion`, `#technology forecasting`

---

<a id="item-5"></a>
## [谷歌发布 Gemini 3.8 文本转语音，支持 30 秒语音克隆](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.8 文本转语音模型，其中包括面向创意指导和角色设计的 Gemini 3.8 Flash TTS，仅需一段 30 秒的、用户拥有使用权的语音样本，即可重建一致的语音特征。该版本内置了同意验证、SynthID 水印和 C2PA 凭证，以保护开发者及其配音人员。 这标志着谷歌正式进入主流语音克隆领域，而这一能力此前已由 ElevenLabs、HeyGen 等服务商提供，也说明语音复制正在成为商业 TTS 平台的标准功能。它会影响开发者、创作者和配音演员，同时内置的防护措施试图回应的同意与滥用问题仍将持续存在。 这些模型分为两个层级：面向富有表现力、可创意指导角色声音的 Gemini 3.8 Flash TTS，以及面向大规模应用的模型，其在谷歌消费级、专业级和云平台上的可用性各不相同。语音复制仅需 30 秒样本，与 Fliki、HeyGen 等竞品服务已提供的能力相当。

hackernews · swolpers · 9月23日 15:29 · [社区讨论](https://news.ycombinator.com/item?id=49817615)

**背景**: 文本转语音（TTS）技术将书面文字转换为语音音频，而现代 AI 语音克隆更进一步：通过分析一段短音频样本，捕捉说话者的音色、音高、口音和说话风格，再用该声音生成新的语音。谷歌的 Gemini-TTS 语音复制文档描述了这一能力，其 Google Cloud TTS 服务已提供覆盖数十种语言的数百种自然声音。SynthID 是谷歌用于 AI 生成内容的水印技术，而 C2PA 是一种为媒体附加可验证来源凭证的开放标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/">Gemini 3.8 text-to-speech says hello</a></li>
<li><a href="https://docs.cloud.google.com/text-to-speech/docs/gemini-tts-voice-replication">Gemini-TTS voice replication | Cloud Text-to-Speech | Google ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=49817615">Gemini 3.8 text-to-speech says hello | Hacker News</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者批评谷歌在消费级、专业级和云平台之间可用性不一致，并指出像 Omni Flash 这样的模型在不同平台上的能力甚至也不相同。Simon Willison 认为，语音克隆如今已由其他服务商广泛提供，因此谷歌不再犹豫推出该功能；其他人则分享了本地 TTS 项目，例如报告引文归属准确率达 97.2%的 KeenLore，并称赞 Gemini 3.8 庞大的声音库以及对脚本化广播剧的精细控制。

**标签**: `#text-to-speech`, `#Gemini`, `#voice-cloning`, `#AI-models`, `#Google`

---

<a id="item-6"></a>
## [Radicle 披露网络协议严重漏洞：节点流量未加密未认证](https://radicle.dev/2026/09/23/disclosure-of-vulnerability-in-network-protocol) ⭐️ 8.0/10

Radicle 披露了一个影响其迄今为止所有已发布网络协议版本的严重漏洞，节点之间的流量既未加密也未进行身份认证。该漏洞由 Konstantinos Maninakis 于 2026 年 6 月 24 日报告，但公开公告直到约三个月后的 2026 年 9 月 23 日才发布，期间给出的建议是停止通过网络使用私有仓库。 对于一个核心价值主张建立在密码学身份和用户数据主权之上的去中心化代码协作平台而言，这是一次根本性的安全失败。它削弱了人们对 Radicle 安全成熟度的信任，也为正在评估去中心化方案（以替代 GitHub 等中心化平台）的开发者敲响了警钟。 迄今为止发布的所有 Radicle 版本均受影响，官方建议的临时措施是在安全更新发布前停止通过网络使用私有仓库，实际上等于假定这些仓库已被泄露。公告还指出，该漏洞在公开前已在内部知晓约三个月。

hackernews · lostmsu · 9月23日 15:23 · [社区讨论](https://news.ycombinator.com/item?id=49817524)

**背景**: Radicle 是一个基于 Git 构建的开源点对点代码协作栈，以去中心化方式在对等节点之间复制仓库，没有任何单一实体控制整个网络。它依赖密码学身份来标识代码和社交产物，并利用 Git 在对等节点间高效传输数据，将自己定位为 GitHub 等中心化平台的主权替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://radicle.dev/2026/09/23/disclosure-of-vulnerability-in-network-protocol.html">Disclosure of Vulnerability in the Network Protocol - Radicle</a></li>
<li><a href="https://lwn.net/Articles/1096200/">Critical security vulnerabilities in the Radicle network protocol - LWN.net</a></li>
<li><a href="https://radicle.dev/">Radicle: the sovereign forge</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了强烈不满，质疑一个围绕密码学身份构建的项目怎么会忽略对跨节点流量进行加密和认证，并批评三个月的披露延迟以及将私有仓库视为已泄露的建议。多位用户表示，这一事件印证了他们对 Radicle 成熟度的长期怀疑，并指出诸如 curl 管道到 shell 的安装方式等做法进一步证明了其安全实践的不专业。

**标签**: `#security`, `#vulnerability-disclosure`, `#decentralized-systems`, `#radicle`, `#network-protocol`

---

<a id="item-7"></a>
## [Claude Opus 5.5 成为 AINews 默认模型，行业价格普降 40-50%](https://www.latent.space/p/ainews-claude-opus-55-the-new-default) ⭐️ 8.0/10

Anthropic 的 Claude Opus 5.5 被宣布为 AINews 的新默认模型，同时整个行业出现 40-50% 的价格下调，令 OpenAI 更高效的 GPT-6 Astra 系列相形见绌。根据 Reddit 上的一份对比，Opus 5.5 在 Terminal-Bench 4.0 上得分 66.4%，而 GPT-6 Astra 为 57.9%，其每百万输入/输出 token 价格约为 4 美元/20 美元，而 Astra 为 10 美元/50 美元。 这标志着 AI 模型格局与经济模式的重大转变，竞争压力正推动价格大幅下调，直接惠及基于这些模型进行开发的开发者和企业。此次发布还凸显了模型能力的分化：Opus 5.5 在编程和成本上领先，而 GPT-6 Astra 在推理和网络安全上领先，这意味着模型选择如今高度取决于具体使用场景。 Opus 5.5 提供 100 万 token 的上下文窗口，缓存读取价格为每百万 token 0.20 美元，而 Astra 为 1.00 美元；Astra 在上下文窗口上以 105 万 token 略占优势，并据报道在 ExploitBench 上取得 100% 的成绩，在评估过程中发现了两个此前未知的零日漏洞。Astra 在 ARC-AGI 和 FrontierMath 等原始推理基准上也处于领先，因此整体情况是两款模型各有所长，而非一方绝对占优。

rss · Latent Space · 9月23日 06:41

**背景**: Terminal-Bench 4.0 是由 Laude Institute、斯坦福大学研究人员及开源贡献者推出的一个更难的智能体基准，包含 66 项复杂任务，用于衡量 AI 智能体在沙盒终端中完成真实软件工程工作的能力。ExploitBench 是一个按能力分级的网络安全基准，将漏洞利用分解为 16 个可衡量的标志，涵盖从代码覆盖、崩溃触发到构建利用原语的全过程。ARC-AGI 是一个基于“对人类容易、对 AI 困难”原则设计的基准，用于追踪通向通用智能的进展。这些基准之所以重要，是因为它们让从业者能够基于具体、真实的任务来比较模型，而不是依赖营销宣传。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/terminalbench-4-0">Terminal-Bench 4.0 Benchmark Leaderboard | Artificial Analysis</a></li>
<li><a href="https://exploitbench.ai/">ExploitBench</a></li>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - The only AI benchmark that measures AGI progress.</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论将这一对比视为各有胜负，评论者给出的评分是 Astra 3 分、Opus 5.5 2 分，但指出这一分数掩盖了两款模型擅长不同任务的事实。他们建议在交付软件或对成本敏感的工作中选择 Opus 5.5，而在需要最强推理、安全研究或最大上下文时选择 Astra，同时询问 Terminal-Bench 上的编程差距在实际工作流中是否依然成立。

**标签**: `#AI`, `#Claude`, `#model release`, `#pricing`, `#OpenAI`

---

<a id="item-8"></a>
## [OpenAI 发布 MentalHealthBench，评估 AI 心理健康对话安全性](https://openai.com/index/introducing-mentalhealthbench) ⭐️ 8.0/10

OpenAI 于 2026 年 9 月 23 日发布了 MentalHealthBench，这是一个包含 1,215 段合成心理健康对话的开放基准，并配有 5,262 条评分标准，由来自 22 个国家、19 种语言的 80 多位持证心理学家和精神科医生共同编写。该基准旨在评估 AI 系统在从日常心理健康到危机情境等真实场景中的回应表现。 这填补了负责任 AI 发展中的一个关键空白，为研究人员和开发者提供了一种标准化、由专家参与制定的方法，用于衡量 AI 在敏感心理健康场景中的有用性和安全性。它很可能影响未来用于心理健康支持的 AI 系统的研究和部署标准。 该基准包含 1,215 段合成对话和 5,262 条评分标准，由来自 22 个国家、19 种语言的 80 多位持证心理学家和精神科医生参与编写。它以开放基准的形式发布，允许外部研究人员和开发者评估和比较 AI 系统。

rss · OpenAI Blog · 9月23日 10:00

**背景**: 随着 AI 聊天机器人越来越多地被用于心理健康支持，人们日益担忧它们在用户脆弱时刻是否能提供有用且安全的回应。基准测试是衡量 AI 能力的标准化测试，但专门针对心理健康对话的基准很少。MentalHealthBench 与 VERA-MH 等其他努力一道，试图为这一领域建立行业安全标准。VERA-MH 是一个经过临床验证的心理健康 AI 安全基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-mentalhealthbench/">Introducing MentalHealthBench - OpenAI</a></li>
<li><a href="https://www.unite.ai/openai-debuts-mentalhealthbench-for-ai-mental-health-conversations/">OpenAI Debuts MentalHealthBench for AI Mental Health ...</a></li>
<li><a href="https://aiweekly.co/alerts/openai-releases-mentalhealthbench-with-1215-conversations-from-80-psychologists">OpenAI Releases MentalHealthBench With 1,215 Conversations ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#mental health`, `#benchmark`, `#OpenAI`, `#responsible AI`

---

<a id="item-9"></a>
## [Zenity Labs 演示投毒文档可致企业 AI 代理泄露数据](https://www.reddit.com/r/artificial/comments/1wojadv/agentflayer_enterprise_agents_zenity_labs/) ⭐️ 8.0/10

在 Black Hat USA 2025 上，Zenity Labs 演示了单个投毒文档或消息即可驱使企业 AI 代理的连接器跨多家厂商外泄敏感数据。其中一个演示中，ChatGPT Connectors 从已连接的 Drive 中读取 API 密钥，并通过精心构造的图片 URL 将其泄露；另一个演示中，Copilot Studio 代理将知识库文件和 Salesforce 记录通过邮件发送给攻击者。 这一跨厂商演示表明，间接提示注入已不再是理论问题，而是影响 ChatGPT、Copilot Studio 等主流平台的实际企业风险。它可能推动厂商在代理大规模普及之前重新设计代理权限模型、连接器沙箱和输出过滤机制。 这些攻击滥用的是代理自身合法的工具和连接器，而非利用软件漏洞，这意味着传统的漏洞修补可能无济于事。外泄渠道包括图片 URL 渲染和外发邮件，二者都是代理的正常功能，若不加禁用很难在不破坏功能的前提下加以限制。

reddit · r/artificial · /u/_clickfix_ · 9月23日 21:46

**背景**: 企业 AI 代理是一种通过连接器接入 Google Drive、SharePoint、Salesforce 等业务数据源的助手，能够代表用户读取文件并执行操作。间接提示注入是一种攻击方式，攻击者将恶意指令隐藏在代理随后读取的内容（如文档或网页）中，使代理在用户不知情的情况下执行攻击者的指令。Black Hat USA 是重要的安全会议，研究人员常在此披露此类漏洞以提升行业警觉。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/">Fooling AI Agents: Web-Based Indirect Prompt Injection Observed in the Wild</a></li>
<li><a href="https://openai.com/index/designing-agents-to-resist-prompt-injection/">Designing AI agents to resist prompt injection | OpenAI</a></li>
<li><a href="https://www.microsoft.com/en-us/microsoft-365-copilot/microsoft-copilot-studio/">Microsoft Copilot Studio | Create AI Agents</a></li>

</ul>
</details>

**标签**: `#AI security`, `#enterprise agents`, `#data exfiltration`, `#prompt injection`, `#Black Hat`

---

<a id="item-10"></a>
## [谷歌开源 Go 语言智能体编排运行时 'ax'](https://github.com/google/ax) ⭐️ 8.0/10

谷歌在 GitHub 上开源了一个名为 'ax' 的智能体编排运行时，使用 Go 语言编写，单日新增 1543 颗星，目前累计约 9251 颗星、442 次 fork。 智能体编排是当前 AI 领域最热门的方向之一，而由谷歌这样的大型厂商发布的运行时有可能成为协调多智能体工作流的事实标准，从而影响开发者在云端和本地环境中构建与部署智能体应用的方式。 该项目使用 Go 语言实现，这表明它针对分布式智能体工作负载强调性能与并发能力；搜索结果还将其描述为“分布式智能体运行时”，并提及谷歌相关的 Agent Executor 以及 gVisor 等沙箱技术。

github_trending · GitHub Trending · 9月24日 03:34

**背景**: AI 智能体是能够感知输入、做出决策并采取行动以完成任务的自主软件组件，通常通过调用工具或其他模型来实现。编排指的是协调多个智能体的那一层，负责决定何时运行哪个智能体、它们如何通信以及如何处理故障。谷歌的 'ax' 似乎就是提供这一协调层的开源运行时，其理念与微软 Azure 架构指南中描述的串行、并发、交接等编排模式相似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/google/ax">GitHub - google / ax : Google's open agentic orchestrator · GitHub</a></li>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/agent-executor-googles-distributed-agent-runtime/">Agent Executor, Google’s distributed Agent Runtime | Google ...</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns">AI Agent Orchestration Patterns - Azure Architecture Center</a></li>

</ul>
</details>

**标签**: `#AI`, `#agents`, `#orchestration`, `#open-source`, `#Google`

---

<a id="item-11"></a>
## [browser-use/video-use 让编程智能体编辑视频](https://github.com/browser-use/video-use) ⭐️ 8.0/10

browser-use/video-use 是一个新的 Python 库，让编程智能体能够编辑视频，它在一天内获得了 746 颗星，总星数达到 26,567，fork 数为 3,168。它可与 Claude Code 配合使用，支持任何内容类型，例如口播、蒙太奇、教程、旅行素材和访谈，无需预设或菜单。 该项目表明 AI 编程智能体正从软件任务扩展到创意媒体工作流，可能降低开发者进行视频编辑的门槛。它在 GitHub 上的快速走红说明社区对智能体驱动的媒体工具兴趣浓厚，这可能重塑视频的制作和编辑方式。 该库用 Python 编写，旨在让编程智能体以编程方式生成视频编辑，并提供针对 browser-use 库编写 Python 代码的参考文档。它被特别强调可与 Claude Code 配合使用，并被定位为一种无需预设、无需菜单即可编辑多样化视频内容的方法。

github_trending · GitHub Trending · 9月24日 03:34

**背景**: browser-use 最出名的是其浏览器自动化库，让 AI 智能体能够控制网页浏览器，而 video-use 将这种以智能体为中心的方法扩展到了视频编辑。Claude Code 等编程智能体是能够编写并运行代码来完成任务的 AI 系统，因此 video-use 实际上把视频编辑变成了一项可编程任务。这契合了将 AI 智能体用于创意和媒体制作工作流的更广泛趋势，类似工具还包括 Remotion 以及其他开源 AI 视频编辑器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/browser-use/video-use">browser-use/video-use: Edit videos with coding agents - GitHub</a></li>
<li><a href="https://github.com/browser-use/browser-use">Agents that use the browser. - GitHub</a></li>
<li><a href="https://www.remotion.dev/docs/ai/coding-agents">Prompting videos with coding agents - Remotion</a></li>

</ul>
</details>

**社区讨论**: 该新闻条目未提供社区评论，因此没有可总结的讨论观点。

**标签**: `#AI agents`, `#video editing`, `#Python`, `#open source`, `#developer tools`

---

<a id="item-12"></a>
## [ComfyUI 今日新增 209 星，登顶 GitHub 趋势榜](https://github.com/Comfy-Org/ComfyUI) ⭐️ 8.0/10

开源节点式扩散模型界面 Comfy-Org/ComfyUI 单日新增 209 颗星，总星数突破 134,750，fork 数达 15,953。这个 Python 项目持续登上 GitHub 趋势榜，是 AI 图像与视频生成领域最受欢迎的工具之一。 ComfyUI 的快速增长表明，AI 社区非常看重对扩散模型流程的细粒度、可复现控制，而非简单的提示词输入框。其模块化架构已成为高级 Stable Diffusion 工作流的事实标准，影响着创意专业人士和研究人员构建生成式 AI 工具的方式。 ComfyUI 使用 Python 编写，提供图/节点界面、API 和后端，用户可将 Stable Diffusion、ControlNet、LoRA 适配器等节点串联成自定义流程。其超过 13.4 万星和 1.59 万 fork 反映出庞大的社区自定义节点与工作流生态。

github_trending · GitHub Trending · 9月24日 03:34

**背景**: 扩散模型是一类生成式 AI，通过学习逆转加噪过程来生成图像、视频和音频，代表作品包括 Stable Diffusion 和 DALL-E。ComfyUI 将这些模型封装在节点图架构中，这是一种将原子功能单元连接起来的可视化编程方式，类似 Blender 的着色器节点。用户无需编写代码即可构建复杂的生成流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Diffusion_model">Diffusion model</a></li>
<li><a href="https://en.wikipedia.org/wiki/Node_graph_architecture">Node graph architecture - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diffusion-models`, `#GUI`, `#node-based`, `#AI`, `#open-source`

---

<a id="item-13"></a>
## [PACT：统一大语言模型强化学习中的词元级信用分配与评论家对齐](https://huggingface.co/papers/2609.26355) ⭐️ 8.0/10

该论文提出了三个正则性条件——完备性、前缀一致性和中立性，并证明它们唯一地确定了大语言模型强化学习中的词元级信用。随后提出了策略对齐评论家训练（PACT），采用先演员后评论家的更新顺序并施加重要性采样校正，在四个智能体数学推理基准上取得 72.87%的平均准确率，在 SWE-bench Verified 上取得 67.4%的通过率。 这项工作为词元级信用分配提供了严格的理论基础，表明现有的同策略蒸馏（OPD）和 REINFORCE 留一法（RLOO）等算法都是同一底层信用定义的特例。这种统一可以指导为大语言模型后训练设计更原则化、更有效的演员-评论家训练流程。 论文在有界结果奖励下建立了近似信用稀疏性，并表明广义优势估计（GAE）中的中间评论家误差可能与底层信用相当。PACT 在数学推理上比 GRPO 和 PPO 分别高出 8.80 和 13.16 个百分点，在 SWE-bench Verified 上比 PPO、GRPO 和 SAO 分别高出 2.4、2.0 和 3.8 个百分点。

huggingface_papers · Hugging Face Papers · 9月24日 00:00

**背景**: 强化学习已成为大语言模型后训练的核心，但在长生成序列中为单个词元分配信用缺乏标准的数学定义。演员-评论家方法使用演员选择动作、评论家估计其价值，而 REINFORCE 和 RLOO 等策略梯度方法则从采样奖励中估计梯度。本文通过证明一小组正则性条件唯一确定词元级信用，将这两种视角联系起来，并利用该结果改进评论家训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.11056v1">Rethinking Token-Level Credit Assignment in RLVR - arXiv</a></li>
<li><a href="https://openreview.net/forum?id=GRbI7kqA6S">EXPLOITING TREE STRUCTURE FOR CREDIT ASSIGNMENT IN RL ...</a></li>
<li><a href="https://www.emergentmind.com/topics/actor-critic-reinforcement-learning-algorithm">Actor - Critic Reinforcement Learning</a></li>

</ul>
</details>

**标签**: `#reinforcement-learning`, `#large-language-models`, `#credit-assignment`, `#actor-critic`, `#policy-gradient`

---

<a id="item-14"></a>
## [Realtime-Venus：双 9B 模型实现主动式全双工对话](https://huggingface.co/papers/2609.13814) ⭐️ 7.0/10

研究者发布了 Realtime-Venus，一个主动式全双工交互系统，由两个分别训练的 9B 模型组成：负责音视频交互的 Realtime-Venus-Omni 和负责语音对话的 Realtime-Venus-Audio。其双循环运行时允许前台对话持续进行，同时由 harness 异步执行被委派的任务，并将结果回传到正在进行的对话中。 大多数对话式 AI 仍采用轮流发言、请求—响应的模式，而一个能够持续感知、主动发言并在不阻塞对话的情况下卸载工具任务的系统，指向了更自然的实时助手形态。论文报告在打断与延续指标上超过 Gemini 3.1 Live 和 GPT-4o，说明全双工行为正成为多模态对话的竞争前沿。 据论文所述，Realtime-Venus-Omni 在八项视频基准中的六项领先，包括 StreamingBench（70.2%）、OVO-Bench（64.7%）和 Daily-Omni（81.3%）；Realtime-Venus-Audio 则在 MMAU（78.0%）、MMAU-Pro（63.2%）、Llama Questions（83.8%）和 Speech CMMLU（67.8%）上居首。在 Full-Duplex-Bench v1.5 上，它对 75% 的用户打断做出响应，并在 backchannel、他人指向语音和背景语音三种情形下分别达到 97%、88% 和 86% 的延续率，不过该工作仍是未经同行评审的预印本。

huggingface_papers · Hugging Face Papers · 9月22日 00:00

**背景**: 全双工交互指双方可以在同一信道上同时收发信息，而不是严格轮流发言；对语音 AI 而言，这意味着要处理语音重叠，并决定何时插话、何时让出话轮。Realtime-Venus 还引入了异步委派：对话模型把任务交给后台进程后继续对话，而不是等待结果，这与智能体框架派生后台子智能体的做法类似。其共享因果时间线将用户输入、模型输出和委派事件对齐，使模型能够推理事件发生的先后关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.13814">Realtime-Venus: A full - duplex interaction system with asynchronous...</a></li>
<li><a href="https://www.envisioning.com/vocab/full-duplex">Full - Duplex Interaction | Envisioning Vocab</a></li>
<li><a href="https://www.marktechpost.com/2026/06/16/hermes-agent-adds-asynchronous-subagents-so-delegated-work-no-longer-blocks-the-parent-chat/">Hermes Agent Adds Asynchronous Subagents, So Delegated Work No ...</a></li>

</ul>
</details>

**标签**: `#full-duplex`, `#multimodal interaction`, `#real-time dialogue`, `#speech generation`, `#tool execution`

---

<a id="item-15"></a>
## [Meta 发布新款 VR 眼镜，引发隐私争议](https://www.meta.com/vr-glasses/) ⭐️ 7.0/10

Meta 发布了新款 VR 眼镜，配备基于 micro-OLED 面板的 5K Infinite Display，像素密度达到每度 37 像素，详情见其官网和博客。该消息迅速登上 Hacker News 首页，获得 283 分和 249 条评论。 这款设备代表了 VR 领域硬件的重要进步，但社区的强烈反对表明，Meta 的隐私声誉和过去对 Oculus 用户的做法仍然掩盖了其技术成就。这种矛盾可能影响注重隐私的消费者的采用，并影响竞争对手对自家 VR 产品的定位。 这款 VR 眼镜配备 5K Infinite Display，每度 37 像素，但初步体验指出其视场角（70 x 66 度）比 Quest 3 的 103 x 96 度更窄，一些用户觉得受限。该设备定位为比苹果 Vision Pro 更轻、更便宜的替代品，面向移动媒体消费和生产力场景。

hackernews · polymorph1sm · 9月23日 23:47 · [社区讨论](https://news.ycombinator.com/item?id=49824268)

**背景**: Meta 自 2014 年收购 Oculus 以来一直在开发 VR 和 AR 硬件，并于 2021 年将其 VR 业务重新命名为 Meta。该公司的智能眼镜系列，包括 Ray-Ban Stories 和 Ray-Ban Meta，因录制指示灯和数据收集等隐私问题而受到批评。Hacker News 是由 Y Combinator 运营的知名科技论坛，经常举办关于 Meta 产品和政策的批判性讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Meta_AI_glasses">Meta AI glasses</a></li>

</ul>
</details>

**社区讨论**: 评论者大多称赞硬件的潜力，有人称其“出色”和“更轻更便宜的 AVP”，但许多人批评 Meta 的隐私做法，包括要求上传身份证件和处理 Oculus 用户的方式。一些人希望有一款能运行真实操作系统的生产力设备，而另一些人则担心与 Quest 3 相比视场角过窄。

**标签**: `#VR`, `#Meta`, `#Privacy`, `#Hardware`, `#Hacker News`

---