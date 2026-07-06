---
layout: default
title: "Horizon Summary: 2026-07-06 (ZH)"
date: 2026-07-06
lang: zh
---

> 从 127 条内容中筛选出 15 条重要资讯。

---

1. [Claude Code：智能编码工具在 GitHub 上星数激增](#item-1) ⭐️ 8.0/10
2. [程序即权重：将自然语言规范编译为神经构件](#item-2) ⭐️ 8.0/10
3. [有界记忆测试平台提升 LLM 智能体性能](#item-3) ⭐️ 8.0/10
4. [OpenAI 缩放定律论文被曝致命错误，万亿算力或白费](#item-4) ⭐️ 8.0/10
5. [Mythos 级 AI 预计两年内登陆消费级硬件](#item-5) ⭐️ 8.0/10
6. [LongCat 2.0：1.6T MoE 模型以 MIT 许可开源发布](#item-6) ⭐️ 8.0/10
7. [Llama-Server 重启时丢弃 KV 缓存](#item-7) ⭐️ 8.0/10
8. [LivePortrait 蒸馏模型在浏览器中达到 25fps](#item-8) ⭐️ 8.0/10
9. [突尼斯达里加阿拉伯语开放机器翻译管道](#item-9) ⭐️ 8.0/10
10. [能力门控：基于内部置信度的工具使用门控](#item-10) ⭐️ 8.0/10
11. [Anthropic 与阿里巴巴：蒸馏攻击升级](#item-11) ⭐️ 8.0/10
12. [Chrome DevTools MCP 让 AI 代理调试浏览器](#item-12) ⭐️ 8.0/10
13. [OmniRoute：免费 AI 网关，支持 160 多家提供商，人气飙升](#item-13) ⭐️ 8.0/10
14. [Claude Skills 仓库星标突破两万](#item-14) ⭐️ 8.0/10
15. [免费 LLM API 资源列表在 GitHub 上飙升](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude Code：智能编码工具在 GitHub 上星数激增](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic 的 Claude Code 是一款在终端中运行的智能编码工具，今日新增 156 个 GitHub 星标，总星数达到 136,346，复刻数达到 21,914。 这种高社区参与度反映了对 AI 辅助编码工具日益增长的需求，这些工具超越了自动补全，能够理解整个代码库并自主执行任务。 Claude Code 使用 Python 编写，运行在终端中，允许开发者通过自然语言理解代码、运行命令和管理 git 工作流。

github_trending · GitHub Trending · 7月6日 03:49

**背景**: Claude Code 是由 Anthropic 开发的智能编码工具，Anthropic 也是 Claude 系列大语言模型的公司。与传统的自动补全工具不同，智能编码工具可以读取整个代码库、编辑文件、运行测试，甚至自主部署更改。这代表了从 AI 建议代码到 AI 作为自主编码助手的转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/introduction-to-agentic-coding">Introduction to agentic coding | Claude by Anthropic</a></li>
<li><a href="https://code.claude.com/">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#AI-assisted coding`, `#developer tools`, `#CLI`, `#Python`

---

<a id="item-2"></a>
## [程序即权重：将自然语言规范编译为神经构件](https://huggingface.co/papers/2607.02512) ⭐️ 8.0/10

研究人员提出了模糊函数编程，具体实现为程序即权重（PAW），它使用在 FuzzyBench（1000 万示例）上训练的 4B 编译器，为冻结的 0.6B Qwen3 解释器生成参数高效适配器，从而实现对自然语言规范的本地执行。 PAW 在匹配直接提示 32B 模型性能的同时，仅使用约五十分之一的推理内存，并在 MacBook M3 上以 30 tokens/s 运行，有望减少对大型 LLM API 的依赖，为模糊任务实现廉价、离线的执行。 编译器是一个 4B 模型，为冻结的 0.6B Qwen3 解释器输出参数高效适配器（如 LoRA）；解释器在本地执行编译后的程序，无需进一步 API 调用。FuzzyBench 数据集包含 1000 万个自然语言规范与输入输出示例配对。

huggingface_papers · Hugging Face Papers · 7月3日 00:00

**背景**: 许多编程任务（如日志告警或 JSON 修复）是模糊的——难以用精确规则指定，但易于用自然语言描述。传统上，这类任务被外包给大型语言模型 API，成本高、速度慢且不可复现。PAW 将基础模型重新定位为工具构建者：它一次性编译出可复用的神经构件，然后廉价地离线执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.02512">Program-as-Weights: A Programming Paradigm for Fuzzy Functions</a></li>
<li><a href="https://huggingface.co/papers/2607.02512">Program-as-Weights: A Programming Paradigm for Fuzzy Functions</a></li>
<li><a href="https://www.aib.vote/en/news/program-as-weights-neural-compilation-paradigm">Program-as-Weights Compiles Natural Language into Neural ...</a></li>

</ul>
</details>

**标签**: `#programming paradigm`, `#neural compilation`, `#fuzzy functions`, `#efficient inference`, `#natural language specification`

---

<a id="item-3"></a>
## [有界记忆测试平台提升 LLM 智能体性能](https://huggingface.co/papers/2607.02255) ⭐️ 8.0/10

研究人员推出了 AgenticSTS，这是一个面向长周期 LLM 智能体的有界记忆测试平台，通过类型化检索组装全新提示，从而能够对记忆组件进行隔离分析。在《杀戮尖塔 2》中，固定 A0 消融实验显示，启用战略技能后胜率从 3/10 方向性提升至 6/10。 这项工作通过提供一种清晰的方法来研究显式记忆层如何影响长周期决策，解决了 LLM 智能体设计中的一个关键挑战。有界记忆契约可防止上下文窗口溢出，并支持可重复的消融研究，从而加速构建更强大的自主智能体。 该测试平台在《杀戮尖塔 2》中实现，这是一款复杂游戏，此前前沿 LLM 在最低难度下取得零胜，而人类胜率为 16%。作者发布了 298 条完整轨迹，包含条件标签、冻结记忆快照和分析脚本，以支持可重复研究。

huggingface_papers · Hugging Face Papers · 7月3日 00:00

**背景**: 长周期 LLM 智能体需要在多个步骤中记住过去的观察和决策，但简单地将所有内容附加到提示中会形成混乱且无界的上下文，难以隔离单个记忆组件的影响。AgenticSTS 引入了一种有界契约，每个决策仅看到通过类型化检索组装的全新提示，从而保持上下文大小恒定并支持清晰的消融研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.02255">AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents</a></li>
<li><a href="https://github.com/AlayaLab/AgenticSTS">GitHub - AlayaLab/AgenticSTS: Bounded, typed, ablatable ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Slay_the_Spire_II">Slay the Spire II - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#memory`, `#long-horizon`, `#decision-making`, `#Slay the Spire`

---

<a id="item-4"></a>
## [OpenAI 缩放定律论文被曝致命错误，万亿算力或白费](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652710732&idx=1&sn=2a7cd9a7957e498b613f561e1088f551) ⭐️ 8.0/10

一位 DeepMind 研究员公开声称，OpenAI 的原始缩放定律论文存在致命错误，暗示模型规模、数据与性能之间被广泛接受的关系可能从根本上就是错误的。 如果得到证实，这将使多年来在 AI 扩展上的投资失效，可能浪费数万亿美元的算力资源，并迫使 AI 开发策略进行重大反思。 据报道，该错误影响了指导 GPT-3 开发的原始缩放定律论文，意味着 GPT-3 可能严重“虚胖”，更小的模型也能达到类似性能。

rss · 新智元 · 7月5日 04:42

**背景**: 神经缩放定律是描述 AI 模型性能如何随模型规模、数据集大小或算力增加而提升的经验法则。它们一直是 AI 研究的基石，推动了像 GPT-3 和 GPT-4 这样越来越大模型的发展趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260705A04BW800?adChannelId=tech">OpenAI塌房！Scaling law原作曝bug，万亿算力全白烧</a></li>
<li><a href="https://m.aitntnews.com/newDetail.html?newId=26889">OpenAI塌房！Scaling law原作曝bug，万亿算力全白烧</a></li>
<li><a href="https://www.163.com/dy/article/L13655F90512B07B.html">万亿算力白烧了？ OpenAI“塌房” Scaling Law原作 被曝惊天Bug</a></li>

</ul>
</details>

**标签**: `#Scaling Law`, `#AI`, `#OpenAI`, `#research`, `#controversy`

---

<a id="item-5"></a>
## [Mythos 级 AI 预计两年内登陆消费级硬件](https://www.reddit.com/r/LocalLLaMA/comments/1uoij3s/if_trends_hold_mythosclass_capability_may_be/) ⭐️ 8.0/10

Reddit 上的一篇帖子预测，如果当前趋势持续，目前仅在高端云基础设施上可用的 Mythos 级 AI 能力将在大约两年内运行在高端消费级硬件上。 这一预测表明，尖端 AI 能力可能变得对个人用户和小型企业可用，从而可能使先进 AI 民主化并加速本地 AI 应用。 Mythos 级指的是 Anthropic 最强大的前沿模型，如 Claude Mythos Preview 和 Claude Fable 5，它们在智能体编码和多步推理方面表现出色。该预测依赖于对硬件和模型效率趋势的外推。

reddit · r/LocalLLaMA · /u/PetersOdyssey · 7月6日 00:40

**背景**: Mythos 级模型是 Anthropic 的前沿 AI 系统，代表最高能力层级。由于计算需求，它们目前只能通过云 API 或高端订阅访问。消费级硬件指个人常用的 GPU 和系统，如高端游戏 PC。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.illumio.com/cybersecurity-101/what-is-mythos">Cybersecurity 101: What Is Mythos AI ? Complete Technical... | Illumio</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-claude-fable-5">What Is Claude Fable 5? Anthropic's Mythos - Class ... | MindStudio</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区进行了实质性讨论，一些用户对硬件扩展持乐观态度，另一些则对内存带宽和模型大小限制表示怀疑。几位评论者指出，量化和蒸馏可能加速这一时间线。

**标签**: `#AI`, `#hardware`, `#local-llm`, `#trends`

---

<a id="item-6"></a>
## [LongCat 2.0：1.6T MoE 模型以 MIT 许可开源发布](https://www.reddit.com/r/LocalLLaMA/comments/1unyvnz/longcat_20_16t_48b_active_weights_are_now_open/) ⭐️ 8.0/10

美团发布了 LongCat-2.0，这是一个 1.6 万亿参数的混合专家（MoE）语言模型，每个 token 激活约 480 亿参数，并采用宽松的 MIT 许可证开源。 万亿参数 MoE 模型以 MIT 许可开源，大大降低了开发者和研究人员获取并改进最先进大语言模型的门槛，促进了智能体编程等领域的创新。 LongCat-2.0 支持原生 100 万 token 上下文窗口，并采用 LongCat 稀疏注意力机制实现高效长上下文处理。它与 Claude Code、OpenClaw 和 Hermes 等工具集成，用于智能体编程工作流。

reddit · r/LocalLLaMA · /u/Nunki08 · 7月5日 10:35

**背景**: 混合专家（MoE）是一种神经网络架构，它将计算划分为多个专门的子网络（专家），每个输入仅激活其中一部分。这使得模型可以扩展到万亿参数，同时保持推理成本可控。LongCat-2.0 专为智能体编程任务设计，例如代码理解、生成以及在自动化工作流中的执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://longcat.chat/blog/longcat-2.0/">Introducing LongCat-2.0</a></li>
<li><a href="https://github.com/meituan-longcat/LongCat-2.0">GitHub - meituan-longcat/LongCat-2.0</a></li>
<li><a href="https://www.marktechpost.com/2026/07/05/meituan-releases-longcat-2-0-a-1-6t-parameter-open-moe-model-with-native-1m-context-and-longcat-sparse-attention/">Meituan Releases LongCat-2.0: A 1 . 6 T- Parameter Open MoE Model ...</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区普遍对此次发布表示欢迎，强调 MIT 许可对开源 AI 来说是一个重大胜利。一些用户讨论了运行如此大模型的实际影响，指出虽然 480 亿活跃参数可以管理，但完整的 1.6 万亿参数需要大量存储。其他人则对微调和部署 LongCat-2.0 用于编程智能体表示兴趣。

**标签**: `#LLM`, `#open-source`, `#MoE`, `#AI`, `#model release`

---

<a id="item-7"></a>
## [Llama-Server 重启时丢弃 KV 缓存](https://www.reddit.com/r/LocalLLaMA/comments/1uohsov/llamaserver_is_throwing_away_your_perfectly_good/) ⭐️ 8.0/10

llama-server 的槽保存/恢复功能存在一个 bug，由于检查点元数据未持久化，导致进程重启后恢复的 KV 缓存被丢弃，从而强制进行完整的预填充。已提出一个修复方案，使用侧边文件保存和重新加载检查点元数据。 该 bug 实际上抵消了 KV 缓存持久化在预算硬件上进行长上下文 LLM 推理的优势，浪费了昂贵的预填充工作。该修复恢复了无需重新预填充即可恢复会话的能力，这对交互式和成本敏感的应用至关重要。 根本原因是 llama_state_seq_save_file 序列化了 token 和物理 KV 单元，但没有序列化仅存在于进程内存中的 slot.prompt.checkpoints。修复添加了一个版本化的侧边文件 (.ckpt) 来持久化检查点，将 720 秒的完整预填充减少到 1 秒的增量查询。

reddit · r/LocalLLaMA · /u/apollo_mg · 7月6日 00:07

**背景**: KV 缓存存储先前 token 的键值张量，以避免在自回归解码期间重新计算。预填充是对提示的初始处理，计算成本很高。llama-server 的槽保存/恢复功能旨在将 KV 缓存保存到磁盘并重新加载，从而允许在重启后无需重新预填充即可恢复会话。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/13606">Tutorial: KV cache reuse with llama-server - GitHub</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/20572">Tutorial: Persistent KV cache per session with llama-server ...</a></li>
<li><a href="https://deepwiki.com/ggml-org/llama.cpp/3.6-memory-management-and-kv-cache">Memory Management and KV Cache | ggml-org/llama.cpp | DeepWiki</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论验证了该 bug 和修复，用户注意到显著的性能影响，并赞赏详细的分析。一些评论者讨论了替代方法以及元数据持久化对于可靠缓存重用重要性。

**标签**: `#llama-server`, `#KV cache`, `#bug fix`, `#LLM inference`, `#local LLM`

---

<a id="item-8"></a>
## [LivePortrait 蒸馏模型在浏览器中达到 25fps](https://www.reddit.com/r/LocalLLaMA/comments/1uodoli/liveportrait_distilled_model_that_can_run_at/) ⭐️ 8.0/10

LivePortrait 肖像动画模型的蒸馏版本通过 WebGPU 在浏览器中实现了实时 25fps 推理，而原始 ONNX 版本每帧需要 30 秒。 这一突破使得实时肖像动画可以直接在浏览器中运行，无需服务器端处理，大幅降低了视频通话、游戏和内容创作等交互式应用的门槛。 蒸馏模型仅使用小数据集训练了几个小时，因此不同肖像的质量有所差异；在 NVIDIA RTX 5090 上，每帧耗时不到 30 毫秒，作者邀请用户报告在其他 GPU 上的性能。

reddit · r/LocalLLaMA · /u/stephen_holograf · 7月5日 21:12

**背景**: LivePortrait 是一种肖像动画模型，能够使用驱动视频让静态照片动起来。原始模型体积大且速度慢，不适合实时使用。模型蒸馏将大模型压缩为更小、更快的模型，同时保留大部分精度。WebGPU 是一种浏览器 API，允许直接进行 GPU 计算，从而无需插件即可在浏览器中运行机器学习推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/aihacker111/Efficient-Live-Portrait">GitHub - aihacker111/Efficient-Live-Portrait: Fast running ...</a></li>
<li><a href="https://joanleon.dev/en/webgpu-ml-browser/">ML in the browser with WebGPU : real-time inference | Joan León</a></li>

</ul>
</details>

**社区讨论**: 社区对这一性能飞跃感到兴奋，许多用户分享了在不同 GPU 上的帧率并讨论了潜在的改进。一些人指出质量仍受限于小训练数据集，但总体情绪积极。

**标签**: `#model distillation`, `#real-time inference`, `#WebGPU`, `#portrait animation`, `#browser ML`

---

<a id="item-9"></a>
## [突尼斯达里加阿拉伯语开放机器翻译管道](https://www.reddit.com/r/MachineLearning/comments/1uo92vz/i_built_an_open_fromscratch_mt_pipeline_parallel/) ⭐️ 8.0/10

一名 18 岁学生构建并发布了针对阿拉伯字母书写的突尼斯达里加语的开源机器翻译管道和平行语料库，包括自定义 SentencePiece BPE 分词器和 1560 万参数的 Transformer 模型。 这填补了低资源方言 NLP 资源的关键空白，提供了首个开放的平行语料库和从头训练的基线模型，有望为数百万使用者推动进一步研究和应用。 初始语料库仅包含约 553 个手工制作的句子对，BLEU 分数低至 3.89，作者将其视为诚实基线，随着语料库增长而改进。分词器将阿拉伯数字（3,7,9,5）作为符号保护。

reddit · r/MachineLearning · /u/Dhiadev-tn · 7月5日 18:08

**背景**: 突尼斯达里加语是一种马格里布阿拉伯方言，NLP 资源有限，尤其当用阿拉伯字母（拉丁字母加数字表示阿拉伯音素）书写时。现有阿拉伯语工具通常通过现代标准阿拉伯语（MSA）处理，无法正确处理这种正字法。SentencePiece BPE 是一种子词分词方法，可从数据中学习固定词汇；BLEU 是评估机器翻译质量的常用自动指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tunisian_Arabic">Tunisian Arabic - Wikipedia</a></li>
<li><a href="https://github.com/google/sentencepiece">GitHub - google/sentencepiece: Unsupervised text tokenizer ...</a></li>
<li><a href="https://iq.opengenus.org/bleu-score/">Understanding Bleu Score</a></li>

</ul>
</details>

**社区讨论**: 社区称赞该倡议对低资源 NLP 很有价值，并就数据收集策略和模型改进提出了建设性反馈。一些评论者愿意贡献数据或合作，其他人则讨论了阿拉伯字母分词挑战和对更大语料库的需求。

**标签**: `#machine translation`, `#low-resource NLP`, `#Tunisian Darija`, `#Arabizi`, `#open-source`

---

<a id="item-10"></a>
## [能力门控：基于内部置信度的工具使用门控](https://www.reddit.com/r/MachineLearning/comments/1unw5un/competence_gate_gating_tooluse_on_a_small_models/) ⭐️ 8.0/10

一个用于 Qwen3.5-4B 的 10MB LoRA 适配器，基于内部置信度信号对工具使用进行门控，改进了错误检测并减少了幻觉。该适配器读取内部激活，以决定是直接回答、搜索网络还是从本地文档中检索。 这种方法解决了小型语言模型的一个关键限制：它们无法表达自己的真实置信度。通过使用内部信号，它实现了更可靠的工具使用并减少了幻觉，这对于需要事实准确性和隐私的应用至关重要。 该门控在错误检测上实现了 0.46 的 d′改进，并将私有查询泄露率从 22%降低到 10%。然而，它在 SQuAD 2.0 上并未改善基于文档的问答，因为参数能力信号干扰了证据基础任务。

reddit · r/MachineLearning · /u/Synthium- · 7月5日 07:49

**背景**: LoRA（低秩适应）是一种参数高效的微调方法，通过训练低秩矩阵来适应大型模型。小型语言模型通常难以估计自身的置信度，导致过度自信的错误答案。内部激活可以提供比口头输出更可靠的置信度信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/deep-learning/low-rank-adaptation-lora/">Low Rank Adaptation (LoRA) - GeeksforGeeks</a></li>
<li><a href="https://arxiv.org/abs/2311.08298">[2311.08298] A Survey of Confidence Estimation and ...</a></li>
<li><a href="https://arxiv.org/html/2606.09876">Calibrating Overconfidence Without Sacrificing Confidence ...</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论强调了使用内部置信度信号进行门控的新颖性，一些用户质疑样本量较小（隐私测试 n=60，能力测试 n=126）。作者承认了局限性，并指出该方法与模型无关且开源。

**标签**: `#LoRA`, `#confidence estimation`, `#tool use`, `#small language models`, `#open source`

---

<a id="item-11"></a>
## [Anthropic 与阿里巴巴：蒸馏攻击升级](https://www.reddit.com/r/artificial/comments/1uoana3/a_war_between_anthropic_and_alibaba/) ⭐️ 8.0/10

Anthropic 指控阿里巴巴创建了数万个虚假账户，通过蒸馏攻击窃取 Claude 的知识产权，导致阿里巴巴禁止其员工使用 Claude Code，而 Anthropic 则强化了 Claude Fable 5 以抵御此类攻击。 这一冲突凸显了通过蒸馏攻击窃取 AI 模型这一日益严重的威胁，它可能削弱 AI 公司的竞争优势，并迫使它们实施更严格的防御措施，从而也可能影响合法用户。 蒸馏攻击是指利用模型的公共 API 生成训练数据，用于训练竞争模型，从而窃取其能力。据报道，Anthropic 对 Claude Fable 5 的强化措施导致一些合法用户被锁定，或在无害请求上被拒绝服务。

reddit · r/artificial · /u/RazzmatazzAccurate82 · 7月5日 19:10

**背景**: 蒸馏攻击是一种方法，攻击者利用目标 AI 模型的 API 生成大量输入-输出对数据集，然后用该数据集训练一个更便宜或专有的模型，以模仿目标模型的行为。这使得攻击者能够在未经授权的情况下复制模型的能力。Anthropic 已公开呼吁行业协调应对此类大规模攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks : What They Are and Why... | MindStudio</a></li>
<li><a href="https://replicate.com/anthropic/claude-fable-5">Claude Fable 5 | Anthropic</a></li>

</ul>
</details>

**社区讨论**: Reddit 用户注意到 Claude 对异常提示请求变得更加谨慎，一些用户报告被锁定在 Fable 5 之外。人们担心合法用户在企业间谍活动和防御措施之间受到波及。

**标签**: `#AI`, `#security`, `#distillation`, `#Anthropic`, `#Alibaba`

---

<a id="item-12"></a>
## [Chrome DevTools MCP 让 AI 代理调试浏览器](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

Chrome DevTools 团队发布了官方 MCP 服务器，允许 AI 编码代理通过模型上下文协议检查、调试和控制实时 Chrome 浏览器实例。 该工具将 AI 编码代理与真实浏览器环境连接起来，支持自动调试、无障碍测试和性能审计，有望显著简化 Web 开发工作流程。 该项目使用 TypeScript 编写，在 GitHub 上已获得超过 45,000 颗星，且仅官方支持 Google Chrome 和 Chrome for Testing。用户被警告不要与 MCP 客户端共享敏感数据。

ossinsight · GitHub Trending · 7月6日 03:49

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准，用于规范 AI 系统与外部工具的集成方式。Chrome DevTools MCP 实现了 MCP 服务器，允许 Cursor、Claude 和 Gemini 等代理以编程方式与 DevTools 功能交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp/">GitHub - ChromeDevTools/chrome-devtools-mcp: Chrome DevTools ...</a></li>
<li><a href="https://developer.chrome.com/docs/devtools/agents">Chrome DevTools for agents</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Chrome DevTools`, `#MCP`, `#coding agents`, `#TypeScript`, `#developer tools`

---

<a id="item-13"></a>
## [OmniRoute：免费 AI 网关，支持 160 多家提供商，人气飙升](https://github.com/diegosouzapw/OmniRoute) ⭐️ 8.0/10

OmniRoute 是一个用 TypeScript 编写的免费开源 AI 网关，通过提供单个兼容 OpenAI 的端点来访问 160 多家 AI 提供商（其中 50 多家免费），并支持令牌压缩和自动回退，在 GitHub 上迅速获得了超过 11,900 颗星。 该项目通过将多个提供商统一到一个 API 后面，简化了开发者的 AI 集成，通过令牌压缩降低成本，并通过智能回退提高可靠性，使高级 AI 更易于访问。 OmniRoute 支持 RTK+Caveman 堆叠压缩，可节省 15-95% 的令牌，还支持 MCP/A2A 协议、多模态 API 以及桌面/PWA 客户端。它还提供 17 种路由策略和语义缓存。

ossinsight · GitHub Trending · 7月6日 03:49

**背景**: AI 网关充当应用程序与多个 AI 模型提供商之间的统一接口，处理路由、负载均衡和回退逻辑。RTK 和 Caveman 等令牌压缩技术可减少发送到模型和从模型接收的令牌数量，从而降低成本和延迟。MCP（模型上下文协议）标准化了工具集成，而 A2A 则实现了智能体之间的通信。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://omniroute.online/">OmniRoute — Free AI Gateway for Multi-Provider LLMs</a></li>
<li><a href="https://github.com/mikeruhl/rtk-vs-caveman/blob/main/METHODOLOGY.md">rtk-vs-caveman/METHODOLOGY.md at main · mikeruhl/rtk-vs-caveman</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI gateway`, `#TypeScript`, `#open source`, `#developer tools`, `#AI providers`

---

<a id="item-14"></a>
## [Claude Skills 仓库星标突破两万](https://github.com/alirezarezvani/claude-skills) ⭐️ 8.0/10

GitHub 仓库 alirezarezvani/claude-skills 现已收录 337 个技能、插件和自定义命令，适用于 Claude Code 及其他 8 种编码代理，星标数超过 2 万，并在 GitHub 上趋势上升。 该集合通过提供工程、营销、产品等多个领域的即用技能，显著提升开发者生产力，成为使用 AI 编码代理的团队的宝贵资源。 该仓库包含 30 多个代理、70 多个自定义命令和 330 多个技能，支持 Claude Code、Codex、Gemini CLI、Cursor 及其他编码代理，并提供可自定义的引用和脚本。

ossinsight · GitHub Trending · 7月6日 03:49

**背景**: Claude Code 是 Anthropic 的 AI 编码代理，用于辅助代码生成和编辑。技能是 Markdown 指令文件，教导 Claude Code 特定行为；插件添加支持文件；MCP 服务器连接数据库等外部工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://composio.dev/content/top-claude-skills">Top 10 best Claude Code Skills I would use in 2026 | Composio</a></li>
<li><a href="https://claudemarketplaces.com/skills">Claude Skills Directory — Browse 21,600+ Claude Code Skills</a></li>
<li><a href="https://dev.to/raxxostudios/best-claude-code-skills-plugins-2026-guide-4ak4">Best Claude Code Skills & Plugins (2026 Guide) - DEV Community</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI agents`, `#developer tools`, `#productivity`, `#plugins`

---

<a id="item-15"></a>
## [免费 LLM API 资源列表在 GitHub 上飙升](https://github.com/cheahjs/free-llm-api-resources) ⭐️ 8.0/10

GitHub 仓库'cheahjs/free-llm-api-resources'单日获得 482 颗星，总星数超过 25,000，这是一个精选的免费 LLM 推理 API 列表。 该资源为开发者和研究人员提供了经济高效的大语言模型访问途径，降低了 AI 实验和应用开发的门槛。 该列表包含提供免费 API 密钥或额度的服务，其中许多与 OpenAI SDK 兼容，便于集成到现有项目中。

github_trending · GitHub Trending · 7月6日 03:49

**背景**: 像 GPT-4 和 Llama 这样的大语言模型通常需要付费 API 访问或昂贵的硬件。免费的推理 API 允许用户无需前期成本即可测试和原型设计，促进 AI 社区的创新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/cheahjs/free-llm-api-resources">GitHub - cheahjs/free-llm-api-resources: A list of free LLM ...</a></li>
<li><a href="https://www.opensourceprojects.dev/post/8c81bf8a-ca08-4b24-9b8f-2fa85198c5d7">A list of free LLM inference resources accessible via API.</a></li>
<li><a href="https://github.com/mnfst/awesome-free-llm-apis">GitHub - mnfst/awesome-free-llm-apis: List of Permanent Free ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#API`, `#free resources`, `#machine learning`, `#open source`

---