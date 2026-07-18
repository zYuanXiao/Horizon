---
layout: default
title: "Horizon Summary: 2026-07-18 (ZH)"
date: 2026-07-18
lang: zh
---

> 从 125 条内容中筛选出 15 条重要资讯。

---

1. [Kimi K3 开源权重模型挑战顶级闭源模型](#item-1) ⭐️ 9.0/10
2. [Ring-Zero：将零强化学习扩展到万亿参数](#item-2) ⭐️ 9.0/10
3. [PostHog 单日获 438 星，热度飙升](#item-3) ⭐️ 8.0/10
4. [Open Interpreter 每日获星 431 颗，增长迅猛](#item-4) ⭐️ 8.0/10
5. [Boogu-Image-0.1：开源多模态模型家族](#item-5) ⭐️ 8.0/10
6. [德州法院下令暂停色情网站域名](#item-6) ⭐️ 8.0/10
7. [AI 发现 OpenVM 的 ZKVM 中存在严重漏洞](#item-7) ⭐️ 8.0/10
8. [Kaggle AGI 黑客马拉松评审缺陷曝光](#item-8) ⭐️ 8.0/10
9. [谷歌支持的 FireSat 卫星发射用于野火探测](#item-9) ⭐️ 8.0/10
10. [Bonsai 27B 通过 1 位量化在 iPhone 上运行](#item-10) ⭐️ 8.0/10
11. [Trellis.cpp 现达到参考实现的 3D 质量](#item-11) ⭐️ 8.0/10
12. [DeepSeek V4 Flash 在 RTX 5090 上通过 llama.cpp 运行百万上下文](#item-12) ⭐️ 8.0/10
13. [InternLM 发布 397B 参数开源模型](#item-13) ⭐️ 8.0/10
14. [MacBook M5 Max 在 LLM 基准测试中击败两台 DGX Spark](#item-14) ⭐️ 8.0/10
15. [发布两个 Krea 2 功能 LoRA：身份参考与位置外绘](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kimi K3 开源权重模型挑战顶级闭源模型](https://www.reddit.com/r/artificial/comments/1uyrw6h/kimi_k3_landed_third_on_the_intelligence_index/) ⭐️ 9.0/10

这标志着开源权重模型首次如此接近顶级闭源模型的性能，可能使前沿级 AI 的访问更加民主化。如果权重如期发布，开发者和研究人员可以在本地或自己的基础设施上运行接近前沿的模型，减少对专有 API 的依赖。 Kimi K3 拥有 2.8 万亿参数，是迄今为止最大的开源模型，上下文窗口约为 100 万 token。其每任务定价约为 Opus 的一半，但速度也慢约一倍。该模型在 Program Bench 上以 77.8 分位居榜首，并在盲测的 Frontend Code Arena 投票中获胜。

reddit · r/artificial · /u/hero88645 · 7月17日 06:39

**背景**: Artificial Analysis 智能指数是一个综合基准，从推理、编码和知识等多个维度评估 AI 模型。开源权重模型公开发布其训练参数，允许任何人下载和运行，而闭源模型仅提供 API 访问。Kimi K3 由中国 AI 公司 Moonshot AI 开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://artificialanalysis.ai/models">Comparison of AI Models across Intelligence , Performance, and Price</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区表达了兴奋但也持怀疑态度，指出许多基准测试是 Moonshot 自己的，且权重尚未开放独立验证。一些用户强调了该模型在编码任务上的强劲表现和低成本，而另一些用户则质疑发布周的峰值能否持续。

**标签**: `#AI`, `#open-weights`, `#large language model`, `#benchmarks`, `#Kimi K3`

---

<a id="item-2"></a>
## [Ring-Zero：将零强化学习扩展到万亿参数](https://huggingface.co/papers/2607.12395) ⭐️ 9.0/10

该论文提出了一种稳定高效的流水线，将零强化学习（zero RL）扩展到万亿参数模型，实现了涌现推理能力和更高的样本效率。最终模型 Ring-2.5-1T-Zero 在七个数学基准上取得了有竞争力的表现。 这项工作验证了扩展的“苦涩教训”，表明扩展到 1 万亿参数显著提升了样本效率和性能上限。它还揭示了模型会自发发展出自我验证、并行推理等高级认知行为，减少了对人工启发式的需求。 关键的算法和系统优化包括裁剪重要性采样、训练-推理比率校正和混合精度控制。训练过程经历初始发现阶段和随后的锐化阶段，模型展现出拟人化、结构化格式化和上下文焦虑等涌现行为。

huggingface_papers · Hugging Face Papers · 7月16日 00:00

**背景**: 零强化学习（zero RL）将带有可验证奖励的强化学习直接应用于预训练模型，无需监督微调。由于计算限制，先前的研究仅限于小模型，扩展动态未被探索。这项工作解决了朴素扩展中可读性差、令牌冗余和缺乏自适应推理深度等挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.25528">[2510.25528] Zero Reinforcement Learning Towards General Domains</a></li>
<li><a href="https://arxiv.org/html/2602.01826">Beyond Precision: Training-Inference Mismatch is an Optimization Problem and Simple LR Scheduling Fixes It</a></li>
<li><a href="https://arxiv.org/html/2510.26788v1">Defeating the Training-Inference Mismatch via FP16</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#large language models`, `#reasoning`, `#scaling`, `#AI`

---

<a id="item-3"></a>
## [PostHog 单日获 438 星，热度飙升](https://github.com/PostHog/posthog) ⭐️ 8.0/10

PostHog 是一个用于构建自驱型产品的开源平台，在 GitHub 上单日新增 438 颗星，总星数超过 36,000。 这一增长反映了社区对集成 AI 可观测性、分析、会话回放和功能标志等开发者工具的高度兴趣，这些工具对现代产品开发至关重要。 PostHog 使用 Python 编写，提供包括 AI 可观测性、会话回放、功能标志、实验、错误追踪和日志在内的全面工具套件，可通过 Slack、网页、桌面或 MCP 访问。

github_trending · GitHub Trending · 7月18日 02:34

**背景**: PostHog 是一个开源产品分析平台，通过理解用户行为帮助团队构建更好的产品。其“自驱型产品”概念指的是能够利用 AI 和数据自主诊断问题并优化体验的产品。该平台的 AI 可观测性功能专门监控 LLM 和智能体的准确性、成本和安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_observability">AI observability</a></li>
<li><a href="https://en.wikipedia.org/wiki/Session_replay">Session replay</a></li>

</ul>
</details>

**标签**: `#open-source`, `#analytics`, `#developer-tools`, `#AI-observability`, `#Python`

---

<a id="item-4"></a>
## [Open Interpreter 每日获星 431 颗，增长迅猛](https://github.com/openinterpreter/openinterpreter) ⭐️ 8.0/10

Open Interpreter 是一个面向 Kimi K3 等开放模型的编码代理，单日在 GitHub 上获得 431 颗星，总星数超过 66,000。该项目使用 Rust 编写，专注于模拟 OpenAI Codex 的代理框架。 这种快速采用凸显了开发者对能够利用 Kimi K3 等强大开放模型的开源编码代理日益增长的需求。这标志着向低成本、本地可执行的 AI 辅助编码工具的转变，可能使高级编码自动化更加普及。 Open Interpreter 是 OpenAI Codex 的一个分支，针对低成本、开放权重的模型进行了优化。与 Kimi K3 配合使用时，支持高达 1,048,576 个 token 的上下文窗口，其 Rust 实现表明注重性能和安全性。

github_trending · GitHub Trending · 7月18日 02:34

**背景**: 编码代理是能够根据自然语言指令自主编写、执行和调试代码的 AI 系统。Open Interpreter 基于 OpenAI Codex 的概念，但设计为与 Kimi K3 等开放模型配合使用。Kimi K3 是一个拥有 2.8 万亿参数、上下文窗口达 100 万 token 的模型。该项目允许开发者本地或通过 API 运行编码代理，减少对专有服务的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openinterpreter/openinterpreter">GitHub - openinterpreter/openinterpreter: A coding agent for open models like Kimi K3 · GitHub</a></li>
<li><a href="https://www.openinterpreter.com/">Open Interpreter | Coding agent for open models</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**标签**: `#AI`, `#coding agent`, `#open source`, `#Rust`, `#developer tools`

---

<a id="item-5"></a>
## [Boogu-Image-0.1：开源多模态模型家族](https://huggingface.co/papers/2607.13125) ⭐️ 8.0/10

Boogu-Image-0.1 是一个在 Apache 2.0 许可下发布的开源统一多模态理解与生成模型家族，包括 Base、Turbo、Edit 和 Edit-Turbo 变体，在文本到图像生成、快速推理和基于指令的编辑方面取得了有竞争力的性能。 这项工作表明，即使在有限的计算预算下，通过对模型理解、数据质量和训练流程进行针对性改进，并结合智能体推理时扩展，也能显著提升生成和编辑性能，从而推动开源多模态能力的发展。 基础模型仅使用 2.0862 亿张独特图像进行训练，理论训练成本约为 40 万美元，但其性能达到或超越其他开源模型，并接近 GPT-Image-2 等领先闭源系统。

huggingface_papers · Hugging Face Papers · 7月16日 00:00

**背景**: 统一多模态理解与生成模型旨在单个框架内同时处理图像理解和创建。大多数现有开源模型在生成质量上落后于闭源系统。Boogu-Image-0.1 通过引入架构和训练改进（包括在推理时动态分配计算资源以提升输出质量的智能体推理时扩展）来弥补这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://boogu.org/">Boogu - Image - 0 . 1 — Efficient Image Generation Foundation Model</a></li>
<li><a href="https://github.com/boogu-project/Boogu-Image">GitHub - boogu-project/ Boogu - Image : Boogu - Image - 0 . 1 is an...</a></li>
<li><a href="https://huggingface.co/Boogu/Boogu-Image-0.1-Turbo">Boogu/ Boogu - Image - 0 . 1 -Turbo · Hugging Face</a></li>

</ul>
</details>

**标签**: `#multimodal`, `#text-to-image`, `#open-source`, `#AI`, `#generation`

---

<a id="item-6"></a>
## [德州法院下令暂停色情网站域名](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-landmark-legal-victory-lock-pornographic-website-domain-and) ⭐️ 8.0/10

2026 年 1 月 7 日，德州总检察长肯·帕克斯顿获得一项缺席判决，命令暂停域名 motherless.com，因其未能遵守该州的年龄验证法（HB 1181）。 这标志着州法院首次直接命令域名注册商因违反州法律而暂停 .com 域名，引发了对州际商业和州级互联网审查的重大担忧。 被告未出庭，导致缺席判决；该域名由位于弗吉尼亚州雷斯顿的 Verisign 注册，公司运营地在旧金山和澳大利亚墨尔本。

hackernews · letmevoteplease · 7月17日 22:35 · [社区讨论](https://news.ycombinator.com/item?id=48952939)

**背景**: 德州众议院第 1181 号法案于 2023 年 9 月 1 日生效，要求成人网站实施合理的年龄验证方法以确保用户年满 18 岁。该法是州级年龄验证强制要求的更广泛趋势的一部分，这些要求因第一修正案和州际商业问题面临法律挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-landmark-legal-victory-lock-pornographic-website-domain-and">Attorney General Ken Paxton Secures Landmark Legal Victory to Lock Pornographic Website Domain and Protect Minors From Harmful Content | Office of the Attorney General</a></li>
<li><a href="https://facia.ai/blog/age-verification-laws-and-regulations-for-minors/">Age Verification Laws and Regulations For Minor</a></li>

</ul>
</details>

**社区讨论**: 评论者对此先例表示强烈担忧，认为单一州法院不应能暂停一家在当地无业务存在的公司的域名，称这是通往互联网审查的滑坡，并违反州际商业。一些人指出缺席判决在法律上薄弱，无法对抗实际出庭辩护的被告。

**标签**: `#internet governance`, `#censorship`, `#domain names`, `#law`, `#pornography`

---

<a id="item-7"></a>
## [AI 发现 OpenVM 的 ZKVM 中存在严重漏洞](https://blog.zksecurity.xyz/posts/openvm-bugs/) ⭐️ 8.0/10

AI 工具发现了 OpenVM 的零知识虚拟机（ZKVM）中的漏洞，这些漏洞可能破坏零知识证明的完整性。 这些漏洞威胁到依赖 OpenVM 的 ZKVM 的第二层网络的安全性，可能允许攻击者伪造证明并窃取资金。 该漏洞类似于一个签名验证库，它验证签名确实签署了给定的哈希值，但未检查被签署的数据是否哈希为该哈希值。

hackernews · duha · 7月17日 14:21 · [社区讨论](https://news.ycombinator.com/item?id=48947714)

**背景**: 零知识证明允许一方在不泄露任何额外信息的情况下向另一方证明某个陈述为真。ZKVM 执行程序并生成正确执行的证明，这对于通过第二层解决方案扩展区块链至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openvm.dev/">A performant and modular zkVM framework built for customization and...</a></li>
<li><a href="https://github.com/openvm-org/openvm">GitHub - openvm -org/ openvm : A performant and modular zkVM ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员强调了严重性，指出利用这些漏洞可能需要硬重置大多数 L2 生态系统。一位评论者将漏洞解释为缺少哈希检查，使熟悉 SNARK 的人能够理解。

**标签**: `#cryptography`, `#zero-knowledge proofs`, `#AI`, `#security`, `#blockchain`

---

<a id="item-8"></a>
## [Kaggle AGI 黑客马拉松评审缺陷曝光](https://www.kaggle.com/competitions/kaggle-measuring-agi/discussion/724918#3498423) ⭐️ 8.0/10

一位 Kaggle AGI 黑客马拉松参与者揭露了基于 AI 的评审和获奖者选择过程中存在不一致的证据，引发了关于比赛中 AI 评审可靠性的讨论。 这很重要，因为 AI 评审在黑客马拉松和基准测试中越来越普遍，缺陷可能削弱对比赛结果和 AI 评估方法完整性的信任。 该黑客马拉松由 Kaggle 和 Google DeepMind 共同组织，约有 20 名评委，评审期从 1.5 个月延长至 3 个月。社区评论指出，AI 生成的提交和 AI 评委形成了有问题的反馈循环。

hackernews · twerkmeister · 7月17日 11:30 · [社区讨论](https://news.ycombinator.com/item?id=48946010)

**背景**: Kaggle 是一个数据科学竞赛平台，参与者构建模型来解决问题。最近，大型语言模型等 AI 工具被用于生成提交和评估提交，引发了对公平性和人工监督的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/ferdi05/how-i-almost-won-an-nlp-competition-without-knowing-any-machine-learning-24la">How I almost won an NLP competition without... - DEV Community</a></li>
<li><a href="https://technical.ly/civic-news/ai-bias-hackathon-baltimore-beat-hacks-hackers/">New ChatGPT model wins top spot in anti- bias AI hackathon</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 AI 评审表示怀疑，一些人指出 AI 生成的提交和 AI 评委为利用漏洞创造了‘天作之合’。一位评论者强调，暴力方法在 Kaggle 中早已存在，但 AI 放大了问题。Kaggle 的一位产品经理回应，提供了评审期延长的背景，并承诺进行调查。

**标签**: `#Kaggle`, `#AI judging`, `#hackathon integrity`, `#machine learning`, `#evaluation bias`

---

<a id="item-9"></a>
## [谷歌支持的 FireSat 卫星发射用于野火探测](https://arstechnica.com/space/2026/07/google-backed-satellites-for-wildfire-detection-launch-as-smoke-chokes-us-canada/) ⭐️ 8.0/10

谷歌支持的 FireSat 项目首批三颗业务卫星成功发射入轨，旨在比现有卫星更早、更准确地探测野火。 这标志着首个专为野火探测设计的卫星星座投入使用，通过提供现有系统无法发现的小型火灾早期预警，有望挽救生命和财产。 卫星由 Muon Space 建造，由非营利组织 Earth Fire Alliance 管理，可在火灾上空停留数天，且不受烟雾或强风影响。

rss · Ars Technica AI · 7月17日 19:50

**背景**: 传统的野火探测依赖飞机和现有卫星，常常漏掉小型或低温火灾。FireSat 使用先进红外传感器，可探测到后院烧烤般大小的火源，提供关键的早期探测能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/space/2026/07/google-backed-satellites-for-wildfire-detection-launch-as-smoke-chokes-us-canada/">Google - backed satellites for wildfire detection launch... - Ars Technica</a></li>
<li><a href="https://www.latimes.com/environment/story/2026-07-06/new-firesat-satellites-promise-faster-california-wildfire-detection">New FireSat satellites promise faster California wildfire detection - Los Angeles Times</a></li>
<li><a href="https://sites.research.google/gr/wildfires/firesat/">FireSat - Wildfires</a></li>

</ul>
</details>

**标签**: `#wildfire detection`, `#satellite technology`, `#climate tech`, `#Google`, `#disaster response`

---

<a id="item-10"></a>
## [Bonsai 27B 通过 1 位量化在 iPhone 上运行](https://www.reddit.com/r/LocalLLaMA/comments/1uyz9n2/bonsai_27b_runs_locally_on_an_iphone_a_27b_model/) ⭐️ 8.0/10

PrismML 发布了 Bonsai 27B，这是一个通过 1 位量化从 Qwen3.6-27B 压缩而来的 278 亿参数模型，大小从 54GB 降至 3.9GB，使其能够在 iPhone 15 Pro Max 上本地运行。 这一突破表明，拥有 270 亿参数的大语言模型可以在移动设备上运行，且性能损失极小（约达到基准测试的 90%），为无需依赖云端的强大设备端 AI 应用铺平了道路。 该模型使用 binary g128 量化，每个权重仅为一个符号位，每 128 个权重共享一个 FP16 缩放因子，实现约 1.125 比特每权重。即使是嵌入层、注意力投影和语言模型头部也被二值化，这在 1 位方案中并不常见。

reddit · r/LocalLLaMA · /u/ElmBark · 7月17日 13:08

**背景**: 1 位量化将模型权重减少到单个比特（或三值），大幅降低内存和计算需求。此前的工作如 BitNet b1.58 表明，1.58 位模型可以匹配全精度性能。Bonsai 27B 将此应用于 270 亿参数模型，实现了 14 倍的压缩比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-27b">PrismML — Announcing Bonsai 27 B : The First 27 B -Class Model to...</a></li>
<li><a href="https://huggingface.co/prism-ml/Bonsai-27B-gguf">prism - ml / Bonsai - 27 B -gguf · Hugging Face</a></li>
<li><a href="https://kie.ai/blog/what-is-bonsai-27b">What Is Bonsai 27 B ? PrismML 's 3.9 GB Phone-Ready LLM</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对在手机上运行 270 亿参数模型表示兴奋，许多人询问推理速度和实际用例。一些用户对基准测试保留率提出质疑，而另一些用户则称赞将包括嵌入层在内的所有层进行二值化的技术成就。

**标签**: `#quantization`, `#edge AI`, `#LLM`, `#mobile`, `#model compression`

---

<a id="item-11"></a>
## [Trellis.cpp 现达到参考实现的 3D 质量](https://www.reddit.com/r/LocalLLaMA/comments/1uyw64s/trelliscpp_now_produces_high_quality_assets/) ⭐️ 8.0/10

基于 GGML 的 TRELLIS 移植版 trellis.cpp 经过社区协助修复多个 bug 后，现已能生成与参考实现质量相当的 3D 资产。 这使得高质量开源 3D 生成可在任何 GPU 甚至 CPU 上运行，无需 CUDA，从而让更广泛的用户群体能够进行 3D 资产创作。 该修复通过与用户 Iajah 的艰苦调试实现，引擎代码托管在 GitHub 的 pwilkin/trellis.cpp，还可与 Lemonade 集成实现可选的文本到 3D 级联生成。

reddit · r/LocalLLaMA · /u/ilintar · 7月17日 10:45

**背景**: TRELLIS 是一个从图像或文本生成 3D 资产的开源 AI 模型。GGML 是一个用于机器学习的张量库，可在无需 CUDA 的 CPU 和 GPU 上进行高效推理。原始的 TRELLIS 参考实现需要 CUDA，限制了其可访问性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml -org/llama.cpp: LLM inference in C/C++ · GitHub</a></li>
<li><a href="https://huggingface.co/spaces/trellis-community/TRELLIS">TRELLIS - a Hugging Face Space by trellis -community</a></li>
<li><a href="https://www.phoronix.com/news/AMD-Lemonade-11.0">AMD Releases Lemonade 11.0 Local AI Server With... - Phoronix</a></li>

</ul>
</details>

**社区讨论**: 社区反响积极，用户对改进后的质量和可访问性表示兴奋。调试工作是协作完成的，凸显了开源社区的力量。

**标签**: `#3D generation`, `#open source`, `#machine learning`, `#TRELLIS`, `#GGML`

---

<a id="item-12"></a>
## [DeepSeek V4 Flash 在 RTX 5090 上通过 llama.cpp 运行百万上下文](https://www.reddit.com/r/LocalLLaMA/comments/1uz5w3y/deepseek_v4_flash_on_5090_in_llamacpp_with_1/) ⭐️ 8.0/10

一位用户使用 llama.cpp 在 RTX 5090 上成功运行了 DeepSeek V4 Flash，上下文长度达到 100 万 token，预填充速度约 650–700 tokens/s，解码速度约 17 tokens/s。他们分享了详细的配置和基准测试结果，并指出近期 llama.cpp 的改进使其更易用。 这表明拥有极长上下文窗口的大型混合专家模型现在可以在消费级硬件上运行，大大降低了本地 LLM 推理的门槛。同时也凸显了 llama.cpp 的快速优化进展，以及在家运行 DeepSeek V4 Flash 等最先进模型的可行性。 使用的模型是 Unsloth 提供的 DeepSeek-V4-Flash-UD-Q8_K_XL，总参数量 284B，每个 token 激活 13B 参数。配置包括 Q8_0 KV 缓存、将部分专家权重卸载到 CPU，以及使用 24 个 CPU 线程并启用 NUMA 隔离。

reddit · r/LocalLLaMA · /u/Shoddy_Bed3240 · 7月17日 17:14

**背景**: DeepSeek V4 Flash 是一个 284B 参数的混合专家（MoE）模型，支持 100 万 token 的上下文窗口，以 MIT 许可证发布。llama.cpp 是一个高性能的 C/C++ 推理引擎，使用 GGUF 格式，能够在消费级硬件上高效地本地运行大型语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.morphllm.com/deepseek-v4-flash">DeepSeek V 4 Flash : 284B MoE , 1M Context, Benchmarks, Pricing...</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://huggingface.co/docs/inference-endpoints/engines/llama_cpp">llama . cpp · Hugging Face</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#llama.cpp`, `#LLM inference`, `#MoE`, `#local LLM`

---

<a id="item-13"></a>
## [InternLM 发布 397B 参数开源模型](https://www.reddit.com/r/LocalLLaMA/comments/1uzifq8/internlminterns2preview397b_huggingface/) ⭐️ 8.0/10

InternLM 在 HuggingFace 上发布了 Intern-S2-Preview-397B，这是一个 3970 亿参数的开源语言模型预览版。 此次发布通过提供前所未有的规模模型，显著推进了开源大语言模型的发展，有望为社区实现更复杂的推理和生成任务。 该模型为预览版，架构细节尚未完全公开，但预计将延续 InternLM 支持长上下文窗口和高效推理的传统。

reddit · r/LocalLLaMA · /u/External_Mood4719 · 7月18日 01:35

**背景**: InternLM 是由上海人工智能实验室和商汤科技开发的一系列开源大语言模型。该项目旨在让更多人能够使用强大的 AI 模型，之前的版本如 InternLM2.5 和 InternLM3 提供了从 1.8B 到 20B 不等的参数规模。此次发布 397B 模型标志着开源模型在规模上的重大飞跃。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/InternLM/InternLM">GitHub - InternLM / InternLM : Official release of InternLM series...</a></li>
<li><a href="https://ollama.com/internlm">internlm</a></li>

</ul>
</details>

**社区讨论**: Reddit 上 r/LocalLLaMA 社区表现出高度兴趣和兴奋，许多用户讨论了本地部署的影响以及微调的潜力。一些用户指出缺乏详细基准测试，并质疑该模型能否在消费级硬件上运行。

**标签**: `#LLM`, `#open-source`, `#large model`, `#HuggingFace`, `#InternLM`

---

<a id="item-14"></a>
## [MacBook M5 Max 在 LLM 基准测试中击败两台 DGX Spark](https://www.reddit.com/r/LocalLLaMA/comments/1uzaf54/one_macbook_vs_2_dgx_spark_deepseekv4flash_scored/) ⭐️ 8.0/10

一台搭载 M5 Max 的 MacBook 运行高度量化的 DeepSeek-V4-Flash 模型，在 Terminal-Bench 2.1 上达到 54% 的准确率，略高于两台运行原生 FP8/FP4 检查点的 NVIDIA DGX Spark 的 52%。 这一结果挑战了激进量化会严重降低 LLM 性能的假设，表明在消费级硬件上高度压缩的模型在智能体任务中可与专用 AI 工作站相媲美。 MacBook 使用了 80.8 GiB 的 GGUF 文件，采用混合量化（专家层为 IQ2_XXS/Q2_K，敏感张量为 Q8/F16/F32，约 2.45 bits/权重），而 DGX Spark 使用原生 FP8/FP4 权重并搭配推测解码（3 个草稿 token）。

reddit · r/LocalLLaMA · /u/anvarazizov · 7月17日 19:58

**背景**: GGUF 是一种用于存储量化 LLM 权重的二进制格式，使模型能够在消费级硬件上运行，降低内存和计算需求。推测解码使用一个小型草稿模型提出 token，再由大型目标模型并行验证，从而在不改变输出分布的情况下加速推理。DGX Spark 是 NVIDIA 的桌面 AI 超级计算机，搭载 GB10 Grace Blackwell Superchip。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.promptquorum.com/local-llms/llm-quantization-explained">Q4_K_M vs Q4_0 vs Q8_0: LLM Quantization Explained (2026)</a></li>
<li><a href="https://www.nvidia.com/en-us/products/workstations/dgx-spark/">Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论可能围绕高度量化模型与原生模型比较的有效性展开，一些用户指出样本量小且未控制温度为局限性，而另一些用户则对 MacBook 的竞争性表现印象深刻。

**标签**: `#LLM inference`, `#quantization`, `#benchmarking`, `#local AI`, `#hardware comparison`

---

<a id="item-15"></a>
## [发布两个 Krea 2 功能 LoRA：身份参考与位置外绘](https://www.reddit.com/r/StableDiffusion/comments/1uyp5z6/i_released_two_krea_2_functional_loras_identity/) ⭐️ 8.0/10

一位开发者发布了两个针对 Krea 2 的 rank-32 功能 LoRA：一个身份参考 LoRA（ReID），允许通过提示控制服装、姿势和背景的变化；另一个是注册外绘 LoRA，可将源图像放置在更大画布上的指定位置。两者均包含完整的 Diffusers 流水线、权重和可运行示例，托管在 Hugging Face 上。 这些功能 LoRA 为本地 Krea 2 推理带来了新颖的图像条件控制行为，扩展了艺术家和开发者的创作自由度，无需依赖托管 API。开源发布及详细的流水线降低了高级图像生成工作流的门槛。 ReID LoRA 使用 Qwen3-VL 图像条件和干净的 VAE 参考令牌，具有隔离的参考注意力和缓存的 K/V，并包含可选的 YuNet 面部裁剪辅助工具。Outpaint LoRA 支持单次边缘放置和两次内部放置方案，并带有源像素恢复和接缝羽化。两个适配器均针对 Krea 2 Raw 训练，并与蒸馏后的 8 步 Krea 2 Turbo 推理一起使用。

reddit · r/StableDiffusion · /u/Upbeat_Birthday_6123 · 7月17日 04:13

**背景**: Krea 2 是一个开源 AI 图像生成模型，提供 Raw（全质量）和 Turbo（蒸馏）变体。LoRA（低秩适应）是一种使用小型适配器权重微调大模型的技术。Diffusers 是 Hugging Face 的库，用于运行扩散模型的推理。功能 LoRA 教授特定行为（如身份参考），而不仅仅是风格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/yijunwang2/krea2-reid">yijunwang2/krea2-reid · Hugging Face</a></li>
<li><a href="https://comfyui-wiki.com/en/models/krea">Krea Family: Open Source Diffusion Transformer with... | ComfyUI Wiki</a></li>
<li><a href="https://github.com/huggingface/diffusers">GitHub - huggingface/ diffusers : Diffusers : State-of-the-art...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论活跃且富有实质性，用户表示有兴趣在本地测试这些 LoRA，并就 Outpaint 的困难源放置和 ReID 的强烈服装/姿势变化提供反馈。开发者欢迎独立测试和反馈。

**标签**: `#Stable Diffusion`, `#LoRA`, `#image generation`, `#open-source`, `#AI/ML`

---