---
layout: default
title: "Horizon Summary: 2026-09-24 (ZH)"
date: 2026-09-24
lang: zh
---

> 从 151 条内容中筛选出 15 条重要资讯。

---

1. [PACT：统一大模型强化学习中的词元级信用分配](#item-1) ⭐️ 8.0/10
2. [高通为骁龙 X2 系列带来 Linux 支持](#item-2) ⭐️ 8.0/10
3. [Anthropic 称 Claude 发现了一种新型类 CRISPR 酶系统](#item-3) ⭐️ 8.0/10
4. [Token 便宜到无需计量：LLM 调用或将比 grep 更便宜](#item-4) ⭐️ 8.0/10
5. [Radicle 披露网络协议严重未加密漏洞](#item-5) ⭐️ 8.0/10
6. [Claude Opus 5.5 成为 AINews 默认模型，AI 价格普降 40-50%](#item-6) ⭐️ 8.0/10
7. [Google DeepMind 发布 Gemini 3.8 Flash TTS 与 Flash-Lite TTS](#item-7) ⭐️ 8.0/10
8. [OpenAI 发布 MentalHealthBench，用于评估 AI 心理健康对话能力](#item-8) ⭐️ 8.0/10
9. [Meta AI 利用家庭帖子构建儿童详细档案](#item-9) ⭐️ 8.0/10
10. [Zenity Labs 演示投毒文档可借企业 AI 代理窃取数据](#item-10) ⭐️ 8.0/10
11. [谷歌开源 AX：用 Go 编写的智能体编排运行时](#item-11) ⭐️ 8.0/10
12. [Univer：专为 AI 智能体打造的开源 Office 运行时](#item-12) ⭐️ 8.0/10
13. [browser-use/video-use：用编码智能体编辑视频](#item-13) ⭐️ 8.0/10
14. [claude-mem 为 AI 智能体带来跨会话持久记忆](#item-14) ⭐️ 8.0/10
15. [Realtime-Venus：具备异步工具委派能力的主动式全双工对话系统](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [PACT：统一大模型强化学习中的词元级信用分配](https://huggingface.co/papers/2609.26355) ⭐️ 8.0/10

一篇新论文提出了三个正则性条件——完备性、前缀一致性和中性，并证明它们唯一地确定了大语言模型强化学习中的词元级信用。基于此，作者提出了策略对齐评论家训练（PACT），采用“先演员后评论家”的更新顺序并施加重要性采样校正，在四个智能体数学推理基准上取得 72.87%的平均准确率，在 SWE-bench Verified 上取得 67.4%的通过率。 词元级信用分配一直缺乏普遍接受的数学定义，导致响应级奖励与逐词元训练信号之间的关系不清晰。这项工作提供了统一的理论基础，解释了同策略蒸馏（OPD）和 RLOO 等现有算法，其 PACT 方法在数学推理上比 GRPO 和 PPO 分别高出 8.80 和 13.16 个百分点，显示出对 LLM 后训练的实际提升。 论文表明，同策略蒸馏中的理想教师充当隐式评论家，且响应级的 RLOO 信号尽管粒度更粗，其期望策略梯度贡献仍与词元级信用相匹配。论文还证明了在有界结果奖励下信用近似稀疏，并指出广义优势估计（GAE）中的中间评论家误差可能变得与底层信用相当，这促使 PACT 采用重要性采样校正。

huggingface_papers · Hugging Face Papers · 9月24日 00:00

**背景**: 强化学习已成为大语言模型后训练的核心环节，模型生成推理轨迹并根据最终结果获得奖励。一个关键挑战是信用分配：确定长响应中哪些词元应对成功或失败的结果负责。演员-评论家方法将策略（演员）与价值估计器（评论家）结合以降低方差，而 RLOO 等方法使用留一法基线来构造无偏的优势估计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hugocisneros.com/notes/token_credit_assignment/">Token-level credit assignment in reasoning traces</a></li>
<li><a href="https://aiwiki.ai/wiki/rloo">RLOO ( REINFORCE Leave - One - Out ) | AI Wiki</a></li>
<li><a href="https://apxml.com/courses/intermediate-reinforcement-learning/chapter-5-actor-critic-methods">Actor - Critic Methods in Reinforcement Learning</a></li>

</ul>
</details>

**标签**: `#reinforcement-learning`, `#large-language-models`, `#credit-assignment`, `#actor-critic`, `#post-training`

---

<a id="item-2"></a>
## [高通为骁龙 X2 系列带来 Linux 支持](https://www.qualcomm.com/news/onq/2026/09/snapdragon-summit-agentic-ai-pcs-linux) ⭐️ 8.0/10

高通在 2026 年骁龙峰会上宣布，骁龙 X2 系列将获得 Linux 支持，并计划将包括 Hexagon NPU 和 Adreno GPU 在内的核心驱动上游到 Linux 主线内核。该平台将从 Windows 和 Googlebook 扩展到 Linux，为开发者、设备制造商和客户打开新的大门。 这对运行 Linux 的 ARM 笔记本来说是重要一步，因为此前几代骁龙 X 芯片因驱动支持不完整而难以作为日常主力机使用。将核心驱动上游化有望显著改善兼容性，推动 OEM 厂商预装 Linux，并增强高通在笔记本市场相对苹果 M 系列和 x86 竞争对手的地位。 此次上游化工作明确涵盖 Hexagon NPU 和 Adreno GPU，社区报告还指出 OpenBSD 开发者 Tobias Heider 已提交早期 OpenBSD/arm64 支持，使 HP Elitebook X G2q 在 ACPI 模式下实现 USB、键盘和触控板可用。他还据称确认 ARM EL2 可工作，这意味着相比前几代产品支持 KVM 虚拟化。

hackernews · aaronday · 9月23日 22:38 · [社区讨论](https://news.ycombinator.com/item?id=49823582)

**背景**: 骁龙 X2 系列是高通面向笔记本的第二代 ARM 处理器家族，接替 2025 年发布的第一代骁龙 X Elite 和 X Plus。ARM 笔记本在 Linux 上历来困难重重，因为即使某款 SoC 获得上游支持，厂商也常常不为其具体机型提供设备树，导致用户无法启动。高通选择将驱动上游化而非保持半专有状态，正是为了解决这一长期痛点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.qualcomm.com/news/onq/2026/09/snapdragon-summit-agentic-ai-pcs-linux">Inside Snapdragon Summit 2026: Agentic AI PCs, Googlebooks and...</a></li>
<li><a href="https://grokipedia.com/page/Snapdragon_X2_series">Snapdragon X2 series</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极且兴奋，评论者称此举“意义重大”，并指出此前缺乏 Linux 支持是购买的主要障碍。讨论重点包括希望高通为每一款笔记本机型上游设备树、称赞 X2 性能是苹果 M 系列最接近的竞争者，以及开发者 Tobias Heider 提交的早期 OpenBSD/arm64 代码作为实质性进展的证据。

**标签**: `#Linux`, `#ARM`, `#Qualcomm`, `#Snapdragon`, `#Open Source`

---

<a id="item-3"></a>
## [Anthropic 称 Claude 发现了一种新型类 CRISPR 酶系统](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) ⭐️ 8.0/10

Anthropic 报告称，其 AI 模型 Claude 在其新成立的生命科学研究实验室中作为智能体工作，发现了一种此前未被描述的酶系统，该系统在巨型噬菌体 DNA 中具有类 CRISPR 的串联重复序列，紧邻一个已知的逆转录酶。该系统的功能仍然未知，这是该实验室的首个公开成果。 这一声明之所以重要，是因为它表明 AI 智能体能够从原始序列数据中发现真正新颖的生物结构，可能加速基因编辑工具的发现。同时，它也加剧了关于 AI 驱动的科学发现应如何验证、应给予多少认可或警惕的争论。 其底层的逆转录酶在此前研究中已被识别；Claude 似乎是第一个注意到该系统标志性类 CRISPR 重复阵列的，但该酶的功能仍未知，且尚未有实验验证的报道。评论者指出，目前治疗性基因组编辑主要受递送限制，而非受新核酸酶发现的限制。

hackernews · raahelb · 9月23日 18:06 · [社区讨论](https://news.ycombinator.com/item?id=49820134)

**背景**: CRISPR-Cas 系统是细菌和噬菌体的防御机制，利用重复阵列和相关酶来靶向 DNA，并因成为基因组编辑工具而闻名。逆转录酶是将 RNA 复制为 DNA 的酶，而 retron 是细菌遗传元件，将逆转录酶与重复序列配对。Anthropic 最近成立了一个生命科学研究实验室和 Claude Science 工作台，旨在推动 AI 辅助的科学研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thenextweb.com/news/anthropic-claude-enzyme-system-crispr-like-repeats">Anthropic says Claude found a new enzyme system with CRISPR - like ...</a></li>
<li><a href="https://arxiv.org/pdf/2509.01398">The Need for Verification in AI-Driven Scientific Discovery</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者意见严重分歧：一些人赞赏通过智能体记录重温发现过程的诗意价值，另一些人则批评其缺乏严谨性、方法和披露，称其为科学发现的可悲借口。几位评论者指出，Anthropic 一边警告不要将 Claude 用于生物工程，一边又宣扬与基因组编辑相关的发现，这颇具讽刺意味；还有一位评论者冷静地将其概括为 Claude 识别出了一种围绕已知逆转录酶的此前未描述的基因组排列。

**标签**: `#AI`, `#CRISPR`, `#bioengineering`, `#scientific discovery`, `#ethics`

---

<a id="item-4"></a>
## [Token 便宜到无需计量：LLM 调用或将比 grep 更便宜](https://jyn.dev/tokens-too-cheap-to-meter/) ⭐️ 8.0/10

jyn.dev 上的一篇文章指出，LLM 的 token 正变得极其便宜，调用 GPT-5.6 Luna 这类模型的成本仅比一次 grep 调用贵 4 到 5 个数量级，按照当前的进步速度，LLM 调用很快就会比 grep 等传统工具调用更便宜。该文在 Hacker News 上引发了 186 条评论的讨论，审视这一趋势在经济、技术和商业模式上的影响。 如果 LLM 调用比传统工具调用更便宜，可能会从根本上重塑软件工程工作流，使 AI 驱动的代码搜索、重构和智能体自动化在经济上可行，达到以往只有确定性工具才能支撑的规模。这一转变将影响开发者、AI 基础设施提供商以及支撑整个 LLM 行业的商业模式。 该论点建立在将当前成本下降趋势外推的基础上，但批评者指出效率提升不可能无限持续（斯坦定律），而且文章对商业模式可行性的分析不足，因为提供商正投入巨额资金建设基础设施，期望未来利润能够支撑。社区成员还质疑，鉴于用户在使用 Emacs、JIRA 和 Salesforce 等工具时遇到的摩擦，'可塑软件'是否真能普及。

hackernews · teoruiz · 9月23日 09:21 · [社区讨论](https://news.ycombinator.com/item?id=49813482)

**背景**: LLM 推理成本已大幅下降——根据 a16z 的'LLMflation'分析，三年内下降了约 1000 倍——Gartner 预测到 2030 年，LLM 推理的成本效率将比 2022 年初的模型高出多达 100 倍。与此同时，grep 是一个有数十年历史的 Unix 命令行文本搜索工具，在本地运行，边际成本几乎为零，因此成为比较确定性工具调用与 AI 驱动工具调用成本的有用基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://a16z.com/llmflation-llm-inference-cost/">Welcome to LLMflation - LLM inference cost is going down fast</a></li>
<li><a href="https://www.linkedin.com/pulse/gartner-predicts-2030-performing-inference-llm-1-trillion-av8hf">Gartner Predicts That by 2030, Performing Inference on an LLM With...</a></li>
<li><a href="https://benchlm.ai/llm-pricing">LLM API Pricing Comparison & Calculator (September 2026)</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对文章的外推持怀疑态度：jetrink 引用斯坦定律认为效率提升不会永远持续；cs702 批评文章在巨额基础设施投资背景下回避了商业模式可行性问题；abirch 则将'便宜到无需计量'的说法与 1954 年核电承诺的落空相类比。rtpg 等人质疑可塑软件能否克服用户因摩擦而不断重复造轮子的倾向，但也有不少人称赞文章富有洞见、发人深省。

**标签**: `#LLM`, `#cost-efficiency`, `#AI economics`, `#software engineering`, `#future of programming`

---

<a id="item-5"></a>
## [Radicle 披露网络协议严重未加密漏洞](https://radicle.dev/2026/09/23/disclosure-of-vulnerability-in-network-protocol) ⭐️ 8.0/10

2026 年 9 月 23 日，Radicle 披露了其网络协议中的两个严重漏洞，指出节点之间的流量以明文传输，既未加密也未认证，影响所有已发布版本。项目方建议用户在安全更新发布前停止通过网络使用私有仓库，而该问题早在 2026 年 6 月 24 日就已被报告，距今约三个月。 这动摇了去中心化代码托管平台的核心价值主张，因为依赖 Radicle 进行私有协作的用户，其仓库数据可能已被任何能观察网络路径的人读取。这也引发了人们对强调加密身份的点对点及去中心化基础设施项目在安全审查实践方面的更广泛质疑。 该漏洞意味着任何能够观察两个节点之间网络路径的人都可以读取明文交换的数据，目前唯一的缓解措施是避免通过网络使用私有仓库。此次披露距离 Konstantinos Maninakis 报告该问题已约三个月，而在公告发布时尚未提供修复版本。

hackernews · lostmsu · 9月23日 15:23 · [社区讨论](https://news.ycombinator.com/item?id=49817524)

**背景**: Radicle 是一个基于 Git 构建的开源点对点代码协作栈，旨在成为 GitHub 等中心化托管平台的主权替代方案，其仓库在对等节点之间复制，没有单一控制实体。它使用加密身份和 gossip 协议让开发者无需中心主机即可协作，其种子节点网络以抗审查的方式传播和托管代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://radicle.dev/2026/09/23/disclosure-of-vulnerability-in-network-protocol.html">Disclosure of Vulnerability in the Network Protocol - radicle.dev</a></li>
<li><a href="https://runtimewire.com/article/radicle-network-protocol-vulnerabilities-private-repositories">Radicle tells users to stop using private repositories over ...</a></li>
<li><a href="https://radicle.dev/">Radicle: the sovereign forge</a></li>

</ul>
</details>

**社区讨论**: 评论者批评激烈，质疑一个围绕加密身份和去中心化构建的项目怎么会忽略跨节点流量的加密，并认为三个月的延迟以及建议停止使用私有仓库的做法不可接受。一些人表示，这一事件证实了他们此前对 Radicle 安全实践和整体成熟度的怀疑。

**标签**: `#security`, `#vulnerability`, `#decentralized`, `#radicle`, `#network-protocol`

---

<a id="item-6"></a>
## [Claude Opus 5.5 成为 AINews 默认模型，AI 价格普降 40-50%](https://www.latent.space/p/ainews-claude-opus-55-the-new-default) ⭐️ 8.0/10

Anthropic 发布了 Claude Opus 5.5，这是其全新 Claude 5.5 系列的首个模型，并已成为 AINews 的新默认模型。OpenAI 大约一小时后发布了 GPT-6 Sol 和 Luna，价格比 GPT-5.6 低约 50%，而各大 AI 供应商整体降价 40-50%。 新前沿模型的发布与 40-50% 的普遍降价同时发生，表明竞争正在加剧，这可能让开发者和企业更容易获得先进的 AI 能力。这也说明 Anthropic 与 OpenAI 在能力和成本上互有攻守，而非某一方明显占据主导。 Claude Opus 5.5 的卖点是以 Opus 的价格提供 Fable 5.1 级别的能力，速度更快、写作更好，并在发布前由 Frontier Design 和 METR 等外部评估机构进行了测试。据 Artificial Analysis 数据，其价格为每百万输入 token 4.00 美元、每百万输出 token 20.00 美元，混合费率约为每百万 token 2.94 美元。

rss · Latent Space · 9月23日 06:41

**背景**: 自 Claude 3 以来，Anthropic 的 Claude 模型一直分为三个规模：Haiku（能力最弱）、Sonnet 和 Opus（能力最强），其中 Opus 层级代表旗舰型号。OpenAI 的 GPT-6 Astra 于 2026 年 9 月 3 日向获批用户首发，次日全面开放。AINews 是一份追踪每日大模型动态的通讯，其默认模型的选择是其作者认为最有用模型的重要信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://artificialanalysis.ai/models/claude-opus-5-5">Claude Opus 5 . 5 (max with fallback) - Intelligence... | Artificial Analysis</a></li>
<li><a href="https://www.latent.space/p/ainews-claude-opus-55-the-new-default">[AINews] Claude Opus 5.5, the new default model for AINews ...</a></li>

</ul>
</details>

**社区讨论**: 有评论指出，OpenAI 以 GPT-6 Sol 和 Luna 做出了勇敢尝试，价格比 GPT-5.6 低 50%，但发布获得 1700 万次观看且仍在增长，这一天仍属于 Claude Opus 5.5。总体情绪是 Anthropic 的发布盖过了 OpenAI 更高效的 GPT-6 模型。

**标签**: `#AI`, `#Claude Opus`, `#pricing`, `#OpenAI`, `#model release`

---

<a id="item-7"></a>
## [Google DeepMind 发布 Gemini 3.8 Flash TTS 与 Flash-Lite TTS](https://deepmind.google/blog/say-hello-to-gemini-38-text-to-speech/) ⭐️ 8.0/10

9 月 23 日，Google DeepMind 推出了两款新的文本转语音模型——Gemini 3.8 Flash TTS 和 Gemini 3.8 Flash-Lite TTS，并陆续在 Google AI Studio、Gemini API、Gemini Enterprise、Gemini Notebook 和 Google Vids 中上线。这两款模型被称为 Google 迄今最具表现力的音频生成模型，新增了语音生成和语音复刻能力。 此次发布将文本转语音从静态预设音色推向动态创作工作室，可能重塑语音交互、无障碍工具、有声书制作和内容创作。由于它同时覆盖消费级、专业级和云端平台，会直接影响在 Google 技术栈上构建语音产品的开发者和企业。 模型支持语音复刻，只需 30 秒音频样本即可重建一致的音色，并内置同意验证、SynthID 水印和 C2PA 凭证。各平台的上线情况并不一致，社区成员指出消费级、专业级和云端产品之间的能力尚未对齐。

rss · Google DeepMind Blog · 9月23日 15:25

**背景**: 文本转语音（TTS）模型将书面文字转换为语音音频，近年来生成式 AI 的进步让合成语音变得自然和富有表现力得多。语音克隆只需一段短样本就能创建可复用的音色，目前多家厂商已广泛提供，这促使 Google 等实验室在推出该功能时加入水印和同意验证等保护措施。Gemini 是 Google DeepMind 的多模态 AI 模型家族，其中 Flash 版本定位为更快、更轻量的选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/">Gemini 3.8 Flash TTS and Gemini 3.8 Flash-Lite TTS - The Keyword</a></li>
<li><a href="https://letsdatascience.com/news/google-launches-gemini-38-text-to-speech-models-cee3c0a7">Google Launches Gemini 3.8 Text-to-Speech Models</a></li>
<li><a href="https://www.unite.ai/google-rolls-out-gemini-3-8-speech-models-in-api-and-ai-studio/">Google Rolls Out Gemini 3.8 Speech Models In API And AI ...</a></li>

</ul>
</details>

**社区讨论**: 评论者欢迎更精细的语音控制和大规模音色库，有人表示它比 GPT-Live 更适合为同人小说音频剧做导演式配音。也有人批评 Google 在消费级、专业级和云端平台之间的可用性和能力不一致，还有人指出语音克隆如今已足够普遍，Google 不再犹豫推出该功能。

**标签**: `#text-to-speech`, `#generative-ai`, `#Google DeepMind`, `#speech-synthesis`, `#AI models`

---

<a id="item-8"></a>
## [OpenAI 发布 MentalHealthBench，用于评估 AI 心理健康对话能力](https://openai.com/index/introducing-mentalhealthbench) ⭐️ 8.0/10

OpenAI 推出了 MentalHealthBench，这是一个由专家参与设计的基准，用于评估 AI 在真实心理健康对话中回应的有用性和安全性。该开放基准包含 1,215 段合成心理健康对话，覆盖不同严重程度、话题和用户画像，包括青少年、成年人、照护者和临床医生，并涵盖多种语言和文化背景。 心理健康是 AI 应用中最敏感、风险最高的领域之一，而该基准提供了一种标准化方法来衡量 AI 在该场景下的有用性和安全性。它可能影响 AI 系统在面向弱势群体使用前的评估和改进方式，进而推动行业评估实践和安全标准的发展。 与现有基准不同，MentalHealthBench 旨在更好地反映真实世界中 AI 在心理健康领域的使用情况，覆盖不同严重程度、对话主题和用户画像，如青少年、成年人、照护者和临床医生，并涵盖多种语言和文化背景。该基准是开放的，使用 1,215 段合成对话而非真实用户数据。

rss · OpenAI Blog · 9月23日 10:00

**背景**: 越来越多的人使用 AI 聊天机器人寻求心理健康支持，但评估其回应是否安全、有用颇具挑战，因为心理健康对话微妙且风险高。基准是标准化的测试集，让研究人员能够比较 AI 模型在特定能力上的表现；MentalHealthBench 是 OpenAI 为此专门创建的测试。它由专家参与设计，意味着心理健康专业人士参与了构建，并且是开放的，以便他人评估自己的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-mentalhealthbench/">Introducing MentalHealthBench - OpenAI</a></li>
<li><a href="https://cdn.openai.com/ctf-cdn/MentalHealthBench_A_Comprehensive_Benchmark_of_AI_Capabilities_in_Realistic_Mental_Health_Conversations.pdf">MentalHealthBench: An Expert-Informed Benchmark of AI ...</a></li>
<li><a href="https://www.unite.ai/openai-debuts-mentalhealthbench-for-ai-mental-health-conversations/">OpenAI Debuts MentalHealthBench for AI Mental Health ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#mental health`, `#benchmark`, `#evaluation`, `#OpenAI`

---

<a id="item-9"></a>
## [Meta AI 利用家庭帖子构建儿童详细档案](https://www.reddit.com/r/artificial/comments/1woo4b9/meta_ai_builds_detailed_profiles_of_children_from/) ⭐️ 8.0/10

一位母亲报告称，Meta AI 通过分析 Meta 平台上多年的家庭帖子，拼凑出她年幼女儿的详细档案，包括姓名、出生信息、照片和位置线索，甚至在收到个人问题时还调出了已删除的照片。该事件于 2026 年 9 月被报道，凸显了 Meta 的 AI 助手可能在未经明确同意的情况下泄露儿童敏感数据。 此案引发了关于 AI 对弱势群体（尤其是儿童）进行画像的严重隐私和伦理担忧，并可能加速对社交媒体平台如何将个人数据用于 AI 训练和推理的监管审查。它影响到数百万在线分享内容的家庭，并凸显了加强数据最小化和同意控制的必要性。 据报道，该画像利用了多年的家庭帖子，并包含已删除的照片和位置信息，这表明 Meta AI 保留或重建了用户认为已被删除的数据。该事件发生在早前关于 Meta AI 提示泄露儿童个人信息的报道之后，表明这是一种模式而非孤立漏洞。

reddit · r/artificial · /u/esporx · 9月24日 01:17

**背景**: Meta AI 是该公司集成在 Facebook、Instagram 和 WhatsApp 中的 AI 助手，能够根据用户数据和平台上分享的内容生成回复。随着 AI 系统越来越能够推断和总结个人信息，人们对儿童隐私、数据保留以及平台构建用户画像缺乏透明度的担忧日益增加。联合国儿童基金会等组织已发布指南，呼吁以儿童为中心的 AI，优先考虑安全、数据保护和问责制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.malwarebytes.com/blog/family-and-parenting/2026/09/meta-ai-builds-detailed-profiles-of-children-from-years-of-family-posts">Meta AI builds detailed profiles of children from years of ...</a></li>
<li><a href="https://oecd.ai/en/incidents/2026-09-08-d6c6">Meta AI Prompts Raise Privacy Concerns After Profiling ...</a></li>
<li><a href="https://www.verisq.ai/intelligence/meta-ai-builds-detailed-profiles-of-children-from-years-of-family-posts-62354">Meta AI Generates Detailed Profiles of Children from Years ...</a></li>

</ul>
</details>

**社区讨论**: Reddit 上 r/artificial 的讨论反映出强烈的担忧和批评，用户们就 AI 对儿童进行画像的伦理问题展开辩论，并呼吁加强监管和家长控制。一些评论者质疑 Meta 的数据保留做法以及现有隐私设置的有效性。

**标签**: `#AI ethics`, `#privacy`, `#Meta`, `#children`, `#data profiling`

---

<a id="item-10"></a>
## [Zenity Labs 演示投毒文档可借企业 AI 代理窃取数据](https://www.reddit.com/r/artificial/comments/1wojadv/agentflayer_enterprise_agents_zenity_labs/) ⭐️ 8.0/10

在 2025 年 8 月的 Black Hat USA 大会上，Zenity Labs 演示了单个投毒文档或消息即可驱使企业 AI 代理的连接器跨多家厂商窃取敏感数据。其中一个演示中，ChatGPT Connectors 从连接的 Google Drive 中读取 API 密钥，并通过精心构造的图片 URL 将其泄露；另一个演示中，Copilot Studio 代理把知识库文件和 Salesforce 记录通过邮件发送给了攻击者。 这一跨厂商演示表明，提示注入不再是理论上的担忧，而是已广泛部署的企业代理中一条具体的数据外泄路径，波及 OpenAI 和微软的产品。任何将 AI 代理连接到 Drive、SharePoint 或 Salesforce 等内部数据源的组织，都应把连接器权限和对外网络访问视为首要的安全边界。 这些攻击滥用的是代理自身合法的工具，而非利用软件漏洞：投毒内容诱导模型使用连接器和对外通道（图片 URL、电子邮件）把数据外送。这意味着仅靠传统的漏洞修补无法解决该风险，因为代理是在攻击者控制的指令下按设计正常行事。

reddit · r/artificial · /u/_clickfix_ · 9月23日 21:46

**背景**: 企业 AI 代理是通过“连接器”接入 Google Drive、SharePoint、Salesforce 等业务系统的助手，能够代表用户读取文件、分析数据并执行操作。提示注入是一种攻击方式：代理读取的不可信文本（如文档或消息）中藏有覆盖用户意图的隐藏指令；当代理同时拥有敏感数据访问权和对外发送请求的能力时，这一组合就变成了数据外泄工具。Black Hat USA 是一年一度的重要安全会议，研究人员常在此披露此类攻击手法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt">Connected apps in ChatGPT - OpenAI Help Center</a></li>
<li><a href="https://www.microsoft.com/en-us/microsoft-365-copilot/microsoft-copilot-studio">Microsoft Copilot Studio | Create AI Agents</a></li>
<li><a href="https://stealthcloud.ai/ai-privacy/prompt-injection-privacy/">Prompt Injection Meets Privacy: The Double Threat</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Enterprise Agents`, `#Prompt Injection`, `#Data Exfiltration`, `#Black Hat`

---

<a id="item-11"></a>
## [谷歌开源 AX：用 Go 编写的智能体编排运行时](https://github.com/google/ax) ⭐️ 8.0/10

谷歌在 GitHub 上发布了一个名为 AX 的开源智能体编排运行时，使用 Go 语言编写，单日新增 1543 颗星，目前总星数约为 9259，Fork 数为 443。 像谷歌这样的大厂以开源运行时切入智能体编排领域，可能会加速多智能体系统构建与部署方式的标准化，同时也为以 Go 为主的技术团队提供了与微软 agent-framework 等 Python 生态框架并列的一流选择。 该仓库被标注为开源分布式智能体运行时，并以 Go 实现，这意味着它更侧重于并发、性能以及生产后端部署，而不仅仅是原型开发；项目仍处于早期阶段，API 和文档可能会发生变化。

github_trending · GitHub Trending · 9月24日 03:44

**背景**: 智能体编排指的是协调多个 AI 智能体，使其通过既定工作流协同完成复杂任务，而不是依赖单个聊天机器人。这类框架通常负责任务路由、状态管理、工具调用以及智能体之间的通信，且大多用 Python 编写，因此谷歌推出基于 Go 的运行时是一个值得关注的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/google/ax">GitHub - google/ax: Google's open agentic orchestration ...</a></li>
<li><a href="https://github.com/google/ax/releases">Releases · google/ax - GitHub</a></li>
<li><a href="https://gitdiscover.org/repositories/google/ax">ax by google - GitHub Repository Analysis | GitDiscover</a></li>

</ul>
</details>

**标签**: `#AI`, `#agents`, `#orchestration`, `#Google`, `#Go`

---

<a id="item-12"></a>
## [Univer：专为 AI 智能体打造的开源 Office 运行时](https://github.com/dream-num/univer) ⭐️ 8.0/10

dream-num/univer 仓库单日新增 1142 颗星，总星数突破 1.64 万，其定位是“面向 AI 智能体的 Office Harness（办公套件运行框架）”。它把电子表格、文档、幻灯片、画布、关系型表格和 PDF 统一到一个开源 TypeScript 运行时中。 AI 智能体此前大多只能处理文本和代码，缺乏可靠读写真实办公文档的手段；统一运行时为智能体提供了可编程的结构化接口来操作电子表格和文档。若被广泛采用，它可能成为智能体办公应用的基础设施，影响整个办公软件生态中的 AI 开发者。 Univer 是一个同构、基于插件架构的 TypeScript 单体仓库，具备 Canvas 渲染、公式引擎以及为智能体基础设施设计的无头 Node.js 模式；项目还宣称支持连接数据、校验、隔离工作树和人工审核。它采用 Apache-2.0 许可证，Office SDK v1.0.0 版本在电子表格、文档和演示之外新增了 Bases、Boards 与 PDF 支持。

github_trending · GitHub Trending · 9月24日 03:44

**背景**: Univer 最初是作为商业办公套件的开源替代品出现的，为 Web 应用提供可嵌入的电子表格、文档和幻灯片组件。“智能体 Harness”是让 AI 智能体可靠驱动某个工具的中间层，负责状态管理、校验和错误恢复，而把这一概念应用到办公文档上是较新的思路。Univer 的插件架构和无头模式让开发者既能在浏览器界面中嵌入同一引擎，也能在服务端运行以实现自动化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/dream-num/univer">GitHub - dream-num/univer: The Office Harness for AI Agents ... Mastering Univer 2026: The Ultimate Developer Roadmap Runtime reuse and Daemon | Univer Office SDK Univer Office SDK @univerjs/core - npm</a></li>
<li><a href="https://pyshine.com/Univer-Open-Source-Office-Runtime-AI-Agents-Can-Drive/">Univer: The Open-Source Office Runtime AI Agents Can Drive</a></li>
<li><a href="https://digg.com/ai/747u377v">Univer launches Office Harness for AI agents - Digg</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Office Suite`, `#TypeScript`, `#Open Source`, `#Productivity Tools`

---

<a id="item-13"></a>
## [browser-use/video-use：用编码智能体编辑视频](https://github.com/browser-use/video-use) ⭐️ 8.0/10

开源 Python 仓库 browser-use/video-use 单日新增 746 颗星，总星数已超过 26,569，分叉数达 3,168。用户只需把原始素材放进文件夹，再与 Claude Code 等编码智能体对话，即可得到最终的 final.mp4。 这表明编码智能体正从软件开发扩展到视频剪辑等创意工作流，有望降低开发者和内容创作者的使用门槛。星数的快速增长也说明社区对智能体驱动的媒体生产工具兴趣浓厚。 该工具 100% 开源，围绕 Claude Code 构建，支持转录、剪辑、去除冗余片段、调色、叠加动画、烧录字幕和渲染。据报道，它采用按动画划分的并行子智能体设计来处理不同的剪辑任务。

github_trending · GitHub Trending · 9月24日 03:44

**背景**: 编码智能体是能够自主阅读、编写和执行代码以完成任务的 AI 系统。browser-use 是一个以浏览器自动化智能体闻名的 GitHub 组织，而 video-use 把同样的智能体思路用到视频剪辑上，让大语言模型来编排剪辑操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/browser-use/video-use">GitHub - browser-use/video-use: Edit videos with coding agents</a></li>
<li><a href="https://thakicloud.com/tech-blog/en/tutorials/video-use-coding-agent-video-editor/">Editing Video With a Coding Agent: A Look Inside the video ...</a></li>
<li><a href="https://mcpservers.org/agent-skills/browser-use/video-use">video - use | Agent Skills Library | MCP Servers</a></li>

</ul>
</details>

**社区讨论**: 该项目由 midudev 分享后迅速在网上传播，早期报道重点介绍了其按动画划分的并行子智能体设计以及免费开源的特点。整体反馈积极，关注点在于一句话就能触发剪辑、字幕、调色、动画和渲染等操作。

**标签**: `#video-editing`, `#coding-agents`, `#python`, `#github-trending`, `#developer-tools`

---

<a id="item-14"></a>
## [claude-mem 为 AI 智能体带来跨会话持久记忆](https://github.com/thedotmack/claude-mem) ⭐️ 8.0/10

GitHub 项目 thedotmack/claude-mem 单日新增 87 颗星，总星数突破 94,000，分叉数达 8,362。这是一个用 TypeScript 编写的工具，能够捕获智能体在一次会话中的所有操作，用 AI 压缩这些内容，并在未来的会话中重新注入相关上下文。 跨会话的持久上下文一直是 AI 编程智能体的痛点，这类智能体通常每次会话都从零开始，不记得之前的工作。一个能兼容 Claude Code、Codex、Gemini、Copilot 等多个平台的工具，有望提升工作连续性，减少开发者重复配置的成本。 该项目使用 TypeScript 编写，声称兼容 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等。其核心机制是用 AI 对会话活动进行压缩，这也引出关于保留细节与摘要之间如何权衡的问题。

github_trending · GitHub Trending · 9月24日 03:44

**背景**: Anthropic 的 Claude Code 和 OpenAI 的 Codex 等 AI 编程智能体是命令行工具，能够读取代码库、编辑文件、运行命令并提交拉取请求。由于这些智能体在两次运行之间通常是无状态的，会话结束后开发者往往会丢失积累的上下文。记忆与上下文管理层因此出现，用于延续这些知识，claude-mem 就是这类跨智能体方案之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent , Terminal, IDE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Codex_(AI_agent)">Codex (AI agent)</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#context management`, `#developer tools`, `#TypeScript`, `#memory persistence`

---

<a id="item-15"></a>
## [Realtime-Venus：具备异步工具委派能力的主动式全双工对话系统](https://huggingface.co/papers/2609.13814) ⭐️ 8.0/10

Realtime-Venus 是一个主动式全双工交互系统，由两个分别训练的 9B 模型组成：用于音视频交互的 Realtime-Venus-Omni 和用于语音交互的 Realtime-Venus-Audio，二者都作为完整的对话前端，在共享的因果时间线上整合连续感知、对话控制与原生语音生成。其双循环运行时让前台交互持续进行，同时由 Realtime-Venus-Harness 异步执行被委派的任务并将结果回传到正在进行的对话中。 这项工作将实时多模态对话从传统的轮流发言推进到能够持续感知、主动发言，并在不打断对话的前提下把推理任务卸载到后台工具的系统。如果这类架构走向成熟，可能会重塑语音助手、具身智能体以及实时视频/语音应用中的人机交互方式，因为在这些场景中延迟和自然打断处理至关重要。 在被评估的在线模型中，Realtime-Venus-Omni 在八项视频基准中的六项上取得最高分，包括 StreamingBench（70.2%）、OVO-Bench（64.7%）和 Daily-Omni（81.3%）；Realtime-Venus-Audio 则在 MMAU（78.0%）、MMAU-Pro（63.2%）、Llama Questions（83.8%）和 Speech CMMLU（67.8%）上领先。在 Full-Duplex-Bench v1.5 上，它能响应用户 75% 的打断，并在附和语、他人定向语音和背景语音三种情况下分别达到 97%、88% 和 86% 的延续率，在这三项延续指标上均超过 Gemini 3.1 Live 和 GPT-4o。

huggingface_papers · Hugging Face Papers · 9月22日 00:00

**背景**: 全双工交互指系统能够同时听和说，而不是等用户说完再回应，这需要处理语音重叠并判断何时插话、何时让出话轮。异步工具执行则指模型可以把任务委派给后台进程并继续对话，而不是阻塞对话等待工具返回结果。Realtime-Venus 将这两种思路结合起来：共享的因果时间线对齐用户输入、模型输出和委派事件，而双循环运行时把实时交互与后台推理分离开来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.13814">Realtime-Venus: A full - duplex interaction system with asynchronous...</a></li>
<li><a href="https://www.envisioning.com/vocab/full-duplex">Full - Duplex Interaction | Envisioning Vocab</a></li>
<li><a href="https://apxml.com/courses/building-advanced-llm-agent-tools/chapter-2-developing-custom-python-tools/asynchronous-tool-operations">Asynchronous LLM Tool Execution</a></li>

</ul>
</details>

**标签**: `#multimodal-interaction`, `#full-duplex`, `#speech-generation`, `#real-time-systems`, `#tool-execution`

---