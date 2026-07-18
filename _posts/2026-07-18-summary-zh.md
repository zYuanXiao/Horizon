---
layout: default
title: "Horizon Summary: 2026-07-18 (ZH)"
date: 2026-07-18
lang: zh
---

> 从 125 条内容中筛选出 15 条重要资讯。

---

1. [开源权重模型 Kimi K3 在智能指数中排名第三](#item-1) ⭐️ 9.0/10
2. [Ring-Zero：将零强化学习扩展到万亿参数](#item-2) ⭐️ 9.0/10
3. [Open Interpreter：基于 Rust 的开源模型编程代理](#item-3) ⭐️ 8.0/10
4. [LobeHub：AI 团队的智能代理运营平台](#item-4) ⭐️ 8.0/10
5. [Boogu-Image-0.1：开源多模态模型系列](#item-5) ⭐️ 8.0/10
6. [AI 发现 OpenVM 的 ZkVM 存在严重漏洞](#item-6) ⭐️ 8.0/10
7. [谷歌支持的 FireSat 卫星发射用于野火探测](#item-7) ⭐️ 8.0/10
8. [Bonsai 27B 通过 1 位量化在 iPhone 上运行](#item-8) ⭐️ 8.0/10
9. [Trellis.cpp 现可生成与参考质量相当的 3D 资产](#item-9) ⭐️ 8.0/10
10. [DeepSeek V4 Flash 在 RTX 5090 上通过 llama.cpp 运行百万上下文](#item-10) ⭐️ 8.0/10
11. [InternLM 发布 3970 亿参数开源模型](#item-11) ⭐️ 8.0/10
12. [MacBook M5 Max 在 LLM 基准测试中几乎追平 2× DGX Spark](#item-12) ⭐️ 8.0/10
13. [Krea 2 发布两个功能性 LoRA](#item-13) ⭐️ 8.0/10
14. [欧盟 AI 法案 OpenRAG：法律结构化分块与嵌入](#item-14) ⭐️ 8.0/10
15. [LLM 隐写工具将消息隐藏在聊天文本中](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [开源权重模型 Kimi K3 在智能指数中排名第三](https://www.reddit.com/r/artificial/comments/1uyrw6h/kimi_k3_landed_third_on_the_intelligence_index/) ⭐️ 9.0/10

Moonshot AI 的开源权重模型 Kimi K3 在 Artificial Analysis 智能指数上获得 57.1 分，排名第三，仅次于 Fable 5（59.9）和 GPT-5.6 Sol（58.9），领先于 Opus 4.8。该模型在 Program Bench（77.8）和 Frontend Code Arena 上排名第一，其权重计划于 7 月 27 日公开发布。 这标志着开源权重模型首次与最佳闭源模型差距在三分以内，挑战了专有 AI 的主导地位。如果权重如期发布，可能使前沿智能的获取民主化，并加速开源 AI 的发展。 Kimi K3 拥有 2.8 万亿参数，是史上最大的开源模型，上下文长度约 100 万，每任务定价约为 Opus 的一半。但基准测试包含 Moonshot 自家的评估，且由于权重尚未发布，模型尚未被独立自托管。

reddit · r/artificial · /u/hero88645 · 7月17日 06:39

**背景**: Artificial Analysis 智能指数是一个综合基准，从推理、编程和知识等多个维度评估 AI 模型。开源权重模型允许任何人下载并在本地运行，而 GPT-5.6 Sol 或 Opus 4.8 等闭源模型仅能通过 API 访问。Kimi K3 由中国 AI 公司 Moonshot AI 开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://artificialanalysis.ai/models">Comparison of AI Models across Intelligence , Performance, and Price</a></li>
<li><a href="https://digg.com/tech/we56zqdp">Chinese model Kimi-K3 tops Frontend Code Arena benchmark · Digg</a></li>

</ul>
</details>

**社区讨论**: 社区持谨慎乐观态度，一些人质疑 Moonshot 自家基准的有效性，并指出模型尚未被独立验证。其他人则注意到隐藏系统提示问题（85 个 token）以及缺乏代理工具调用评估。许多人对于权重发布后能在本地运行前沿级模型感到兴奋。

**标签**: `#AI`, `#open-weights`, `#benchmarks`, `#Kimi K3`, `#large language models`

---

<a id="item-2"></a>
## [Ring-Zero：将零强化学习扩展到万亿参数](https://huggingface.co/papers/2607.12395) ⭐️ 9.0/10

研究人员提出了 Ring-Zero，这是一个稳定的流水线，用于将零强化学习扩展到万亿参数模型，在七个数学基准上实现了涌现推理和竞争性性能。 这项工作表明，将零强化学习扩展到 1 万亿参数可显著提高样本效率和性能，并揭示出自我验证和并行推理等涌现认知行为，这可能改变大规模强化学习在大型语言模型中的应用范式。 该流水线采用了裁剪重要性采样、训练-推理比率校正和混合精度控制，以解决可读性差和令牌冗余等问题。模型 Ring-2.5-1T-Zero 还引入了一个结构化评估框架，用于从可理解性、可复现性和效率三个维度评估思维链质量。

huggingface_papers · Hugging Face Papers · 7月16日 00:00

**背景**: 零强化学习（zero RL）使用可验证的奖励而无需人工标注数据，以激发大型语言模型中的思维链推理。由于计算限制，先前的工作仅限于小模型，扩展行为未被探索。本文通过扩展到 1 万亿参数填补了这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2510.25528">Zero Reinforcement Learning Towards General Domains</a></li>
<li><a href="https://www.emergentmind.com/topics/training-inference-ratio-correction">Training - Inference Ratio Correction</a></li>
<li><a href="https://www.emergentmind.com/topics/cispo-algorithm">CISPO: Clipped Importance Sampling RL</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#large language models`, `#reasoning`, `#scaling`, `#AI research`

---

<a id="item-3"></a>
## [Open Interpreter：基于 Rust 的开源模型编程代理](https://github.com/openinterpreter/openinterpreter) ⭐️ 8.0/10

Open Interpreter，一个针对 Kimi K3 等开源模型优化的基于 Rust 的编程代理，在 GitHub 上单日获得 431 颗星，总星数超过 66,000。 这种快速增长表明社区对低成本、开放权重的编程代理有强烈兴趣，可能使 AI 辅助开发民主化，并减少对专有模型的依赖。 Open Interpreter 自带 QA 技能，允许任何模型操作和测试接口，并且可以在真实浏览器中驱动 Web 应用或通过 trycua 操作原生应用。

github_trending · GitHub Trending · 7月18日 02:45

**背景**: Kimi K3 是一个拥有 2.8 万亿参数的开源模型，是迄今为止最大的开源模型，完整权重预计于 2026 年 7 月发布。Open Interpreter 旨在与这类大型开源模型配合使用，提供一个能够通过交互开发环境执行复杂技术任务的编程代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openinterpreter/openinterpreter">GitHub - openinterpreter/openinterpreter: A coding agent for open ...</a></li>
<li><a href="https://www.openinterpreter.com/">Open Interpreter | Coding agent for open models</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**标签**: `#AI`, `#coding agent`, `#open models`, `#Rust`, `#developer tools`

---

<a id="item-4"></a>
## [LobeHub：AI 团队的智能代理运营平台](https://github.com/lobehub/lobehub) ⭐️ 8.0/10

LobeHub，一个基于 TypeScript 的开源平台，单日获得超过 409 个星标，GitHub 总星标数突破 8 万，它将自己定位为首席代理运营官，能够管理和编排 AI 代理实现全天候持续运营。 该项目提出了 AI 代理运营官的新概念，能够自动化多个 AI 代理的招聘、调度和报告，这与多代理编排的日益增长趋势高度相关，可能显著提升开发者和企业的生产力。 LobeHub 使用 TypeScript 编写，拥有 15,631 个复刻，表明社区参与度很高。它通过将代理组织成 7×24 小时运营，让用户无需在线也能掌控全局。

github_trending · GitHub Trending · 7月18日 02:45

**背景**: AI 代理编排是指在统一框架内系统协调多个专门 AI 代理以完成复杂任务。LobeHub 充当首席代理运营官，负责招聘、调度和报告整个 AI 团队，类似于人类经理监督工人团队的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lobehub.com/">LobeHub - Your Chief Agent Operator</a></li>
<li><a href="https://digg.com/ai/ga7nwocv">LobeHub Launches Chief Agent Operator to Hire AI Agents 24/7 · Digg</a></li>
<li><a href="https://github.com/topics/chief-agent-operator">chief - agent - operator · GitHub Topics · GitHub</a></li>

</ul>
</details>

**标签**: `#AI`, `#agent orchestration`, `#TypeScript`, `#open source`, `#productivity`

---

<a id="item-5"></a>
## [Boogu-Image-0.1：开源多模态模型系列](https://huggingface.co/papers/2607.13125) ⭐️ 8.0/10

Boogu-Image-0.1 是一个开源的统一多模态理解与生成模型系列，包含 Base、Turbo、Edit 和 Edit-Turbo 等变体，在文本到图像生成、快速推理和双语文本渲染方面取得了有竞争力的表现。 该发布通过展示在数据质量和训练流程上的针对性改进可以在有限计算资源下达到接近闭源系统的性能，从而弥合了开源与闭源多模态系统之间的差距，推动了开放生态系统的发展。 该模型仅使用 2.0862 亿张独立图像进行训练，理论训练成本约为 40 万美元，并采用智能推理时缩放（agentic inference-time scaling）来提升生成和编辑性能。

huggingface_papers · Hugging Face Papers · 7月16日 00:00

**背景**: 统一多模态理解与生成模型旨在单个框架内同时处理图像理解和创建，不同于传统系统将这两项任务分离。闭源模型如 Nano-Banana-Pro 和 GPT-Image-2 通过未公开的系统级集成实现了强大性能。Boogu-Image-0.1 以 Apache 2.0 许可证发布，权重、代码和配方均公开可用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://boogu.org/">Boogu - Image - 0 . 1 — Efficient Image Generation Foundation Model</a></li>
<li><a href="https://github.com/boogu-project/Boogu-Image">GitHub - boogu-project/ Boogu - Image : Boogu - Image - 0 . 1 is an...</a></li>
<li><a href="https://www.communeify.com/en/blog/boogu-image-0-1-bilingual-text-to-image-model-analysis/">Full Analysis of Boogu - Image - 0 . 1 : 10B Open-Source AI... | Communeify</a></li>

</ul>
</details>

**标签**: `#multimodal`, `#text-to-image`, `#open-source`, `#AI`, `#image generation`

---

<a id="item-6"></a>
## [AI 发现 OpenVM 的 ZkVM 存在严重漏洞](https://blog.zksecurity.xyz/posts/openvm-bugs/) ⭐️ 8.0/10

AI 辅助分析发现 OpenVM 的 ZkVM 中存在签名验证可被绕过的漏洞，可能影响 L2 生态系统。 这些漏洞可能危及依赖 OpenVM 的 L2 解决方案的安全性，凸显了 AI 在密码学审计中的重要性。 该漏洞允许攻击者通过绕过签名验证来伪造证明，类似于验证了错误哈希上的签名。

hackernews · duha · 7月17日 14:21 · [社区讨论](https://news.ycombinator.com/item?id=48947714)

**背景**: zkVM（零知识虚拟机）执行程序并生成正确执行的密码学证明。OpenVM 是一个模块化的 zkVM 框架，支持自定义扩展和 Rust 语言。签名验证对于确保证明的真实性和未被篡改至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openvm.dev/">A performant and modular zkVM framework built for customization and...</a></li>
<li><a href="https://www.certik.com/blog/what-is-a-zero-knowledge-virtual-machine-zkvm">What Is a Zero - Knowledge Virtual Machine ( zkVM )? - CertiK</a></li>

</ul>
</details>

**社区讨论**: 评论者指出该漏洞类似于验证了错误哈希上的签名，并质疑该漏洞对 L2 生态系统的影响。有人开玩笑说密码学太复杂了。

**标签**: `#cryptography`, `#zero-knowledge proofs`, `#security`, `#AI`, `#blockchain`

---

<a id="item-7"></a>
## [谷歌支持的 FireSat 卫星发射用于野火探测](https://arstechnica.com/space/2026/07/google-backed-satellites-for-wildfire-detection-launch-as-smoke-chokes-us-canada/) ⭐️ 8.0/10

由谷歌支持的 FireSat 项目已发射卫星，这些卫星能够比现有系统更早地探测到野火，为灾害监测提供了重大进步。 这项技术可以探测到其他卫星遗漏的野火，可能缩短响应时间，减轻野火对社区和生态系统的破坏性影响。 FireSat 卫星使用专门的红外传感器探测热异常，即使火灾被烟雾遮挡或位于偏远地区也能实现早期探测。

rss · Ars Technica AI · 7月17日 19:50

**背景**: 野火探测传统上依赖地面观测和现有卫星，但这些方法可能灵敏度有限或重访周期较长。FireSat 项目旨在通过部署配备先进传感器和 AI 分析功能的卫星星座，实现近实时监测，填补这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/descarteslabs-team/the-satellites-hunting-for-megafires-afa1305fdc2c">The Satellites Hunting for Megafires | by Clyde Wheeler | Medium</a></li>
<li><a href="https://www.azosensors.com/article.aspx?ArticleID=3328">Detecting Wildfires Before Disaster Happens</a></li>
<li><a href="https://ororatech.com/resources/news-blog/why-earth-observation-is-the-future-of-fire-detection/">Why Earth Observation is the Future of Wildfire Detection</a></li>

</ul>
</details>

**标签**: `#wildfire detection`, `#satellite technology`, `#Google`, `#environmental monitoring`, `#disaster response`

---

<a id="item-8"></a>
## [Bonsai 27B 通过 1 位量化在 iPhone 上运行](https://www.reddit.com/r/LocalLLaMA/comments/1uyz9n2/bonsai_27b_runs_locally_on_an_iphone_a_27b_model/) ⭐️ 8.0/10

PrismML 发布了 Bonsai 27B，这是一个通过真正的 1 位量化（binary g128）压缩至 3.9GB 的 270 亿参数模型，使其能够在 iPhone 15 Pro Max 上本地运行，同时保留约 90%的原始基准性能。 这一突破表明，超大型语言模型可以部署在智能手机等边缘设备上，在不牺牲太多准确性的前提下，极大地扩展了私有离线 AI 应用的潜力。 该模型采用 binary g128 量化，每个权重为单个符号位，每 128 个权重共享一个 FP16 缩放因子，达到约 1.125 比特每权重，且没有高精度逃逸通道；甚至嵌入层和注意力投影也是二进制的。在 4K 上下文下内存占用约 5.2GB，在 100K 上下文下使用 4 位 KV 缓存时约 6.8GB。

reddit · r/LocalLLaMA · /u/ElmBark · 7月17日 13:08

**背景**: 大型语言模型通常需要数 GB 的内存和强大的 GPU，使其在移动设备上不实用。量化通过降低模型权重的精度（例如从 16 位降至 1 位）来缩小体积并加速推理。以往的 1 位方法通常保留某些层为更高精度，但 Bonsai 统一应用二进制量化，实现了极致的压缩。

**社区讨论**: 社区对在手机上运行 27B 模型表示兴奋，许多人称赞约 90%的基准保留率。一些用户质疑对推理和知识任务的实际影响，指出这些基准下降更明显。其他人讨论了压缩比与输出质量之间的权衡，以及未来改进的潜力。

**标签**: `#quantization`, `#edge AI`, `#LLM`, `#model compression`, `#mobile deployment`

---

<a id="item-9"></a>
## [Trellis.cpp 现可生成与参考质量相当的 3D 资产](https://www.reddit.com/r/LocalLLaMA/comments/1uyw64s/trelliscpp_now_produces_high_quality_assets/) ⭐️ 8.0/10

开源项目 trellis.cpp 修复了关键错误，实现了与官方参考实现相当的图像到 3D 资产质量，现在无需 CUDA 即可使用。 这使得高质量的开源 3D 生成对拥有合格 GPU 或 CPU 的任何人可用，推动了 3D 内容创作的民主化，并减少了对专有硬件的依赖。 该项目使用 GGML 在无需 CUDA 的情况下在 CPU 或 GPU 上进行高效推理，并可集成 Lemonade 以实现可选的文本到 3D 流程。

reddit · r/LocalLLaMA · /u/ilintar · 7月17日 10:45

**背景**: TRELLIS 是一种先进的图像到 3D 生成模型，可从图像创建 3D 网格。GGML 是一个用于机器学习的张量库，可在包括 CPU 和非 NVIDIA GPU 在内的各种硬件上进行高效推理。trellis.cpp 项目将 TRELLIS 模型移植到 GGML，使其更易于访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.trellis-3d.net/">Image to 3 D Model AI Generator | Trellis 3 D</a></li>
<li><a href="https://github.com/ggml-org/ggml">GitHub - ggml -org/ ggml : Tensor library for machine learning · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">llama.cpp - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区称赞了这一成就，用户注意到质量的显著提升，并感谢开发者的辛勤工作。一些人讨论了调试过程的技术细节和潜在用例。

**标签**: `#3D generation`, `#open source`, `#machine learning`, `#TRELLIS`, `#GGML`

---

<a id="item-10"></a>
## [DeepSeek V4 Flash 在 RTX 5090 上通过 llama.cpp 运行百万上下文](https://www.reddit.com/r/LocalLLaMA/comments/1uz5w3y/deepseek_v4_flash_on_5090_in_llamacpp_with_1/) ⭐️ 8.0/10

一位 Reddit 用户成功在单张 RTX 5090 上通过 llama.cpp 运行 DeepSeek V4 Flash，支持百万 token 上下文，预填充速度约 650–700 tokens/s，解码速度约 17 tokens/s。 这表明前沿的 MoE 模型配合超长上下文可以在消费级硬件上部署，大幅降低了本地 LLM 推理的门槛，并支持长文档分析等新应用。 用户使用了 Unsloth 的 Q8_K_XL GGUF 量化版本，并通过自定义 tensor override 将特定专家层卸载到 GPU，启用了 Q8_0 KV 缓存和 flash attention。加载耗时 32 秒。

reddit · r/LocalLLaMA · /u/Shoddy_Bed3240 · 7月17日 17:14

**背景**: DeepSeek V4 Flash 是一种混合专家（MoE）模型，总参数量 284B，每 token 激活 13B，支持高达 1M 上下文。llama.cpp 是一个开源的 C++ 库，用于在 CPU 和 GPU 上高效推理 LLM。RTX 5090 是 NVIDIA 最新的消费级 GPU，拥有 32GB 显存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md">llama . cpp /tools/server/README.md at master · ggml-org/ llama . cpp</a></li>
<li><a href="https://unsloth.ai/docs/basics/inference-and-deployment/saving-to-gguf">Saving to GGUF | Unsloth Documentation</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论可能称赞了这一成就，但指出解码速度仍慢于 Qwen 模型，用户还讨论了 llama.cpp 中针对 MoE 模型的进一步优化空间。

**标签**: `#DeepSeek`, `#llama.cpp`, `#local LLM`, `#RTX 5090`, `#long context`

---

<a id="item-11"></a>
## [InternLM 发布 3970 亿参数开源模型](https://www.reddit.com/r/LocalLLaMA/comments/1uzifq8/internlminterns2preview397b_huggingface/) ⭐️ 8.0/10

InternLM 发布了 Intern-S2-Preview-397B，这是一个拥有 3970 亿参数的大语言模型，已在 Hugging Face 上开放。这是其下一代模型系列的预览版本。 此次发布标志着开源大语言模型在规模上的重大提升，在参数规模上可与闭源模型媲美，并可能推动推理、编程和多语言任务等能力的进步。它为研究社区提供了一个超大模型用于实验和微调。 该模型为预览版，可能采用混合专家（MoE）架构，以 3970 亿参数实现高效推理。它采用开放许可证发布，但可能有特定条款。

reddit · r/LocalLLaMA · /u/External_Mood4719 · 7月18日 01:35

**背景**: InternLM 是由上海人工智能实验室开发的一系列大语言模型，以开源高质量 LLM 和全栈工具链而闻名。之前的模型包括 InternLM 2 和 InternLM 3，参数规模最高达 200 亿。3970 亿参数模型代表了规模上的重大飞跃，利用 MoE 等技术来平衡性能和计算成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/internlm">internlm ( Intern Large Models )</a></li>
<li><a href="https://github.com/InternLM/InternLM">GitHub - InternLM / InternLM : Official release of InternLM series ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-source`, `#large model`, `#AI research`

---

<a id="item-12"></a>
## [MacBook M5 Max 在 LLM 基准测试中几乎追平 2× DGX Spark](https://www.reddit.com/r/LocalLLaMA/comments/1uzaf54/one_macbook_vs_2_dgx_spark_deepseekv4flash_scored/) ⭐️ 8.0/10

在 Terminal-Bench 2.1 上，一台 MacBook M5 Max 上重度量化的 DeepSeek-V4-Flash（80.8 GiB GGUF）达到了 54% 的准确率，而使用原生 FP8/FP4 检查点并配合推测解码的 2× DGX Spark 得分为 52%。 这一结果挑战了极端量化必然导致显著精度损失的假设，表明经过良好优化的量化模型在消费级硬件上可以与昂贵得多的配置相竞争。 MacBook 使用了混合 GGUF，包含 IQ2_XXS/Q2_K 专家和更高精度的张量，平均每个权重约 2.45 比特；而 DGX Spark 对使用了原生 FP8 权重和 FP4 路由专家，以及 3 个草稿令牌的 DSpark 推测解码。

reddit · r/LocalLLaMA · /u/anvarazizov · 7月17日 19:58

**背景**: GGUF 是一种用于存储量化 LLM 权重的二进制格式，使模型能够在消费级硬件上以更少内存运行。推测解码使用一个小型草稿模型提出令牌，再由更大的目标模型验证，从而在不改变输出分布的情况下加速推理。DGX Spark 是 NVIDIA 的桌面 AI 超级计算机，搭载 GB10 Grace Blackwell 芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.promptquorum.com/local-llms/llm-quantization-explained">Q4_K_M vs Q4_0 vs Q8_0: LLM Quantization Explained (2026)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://www.nvidia.com/en-us/products/workstations/dgx-spark/">Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论中对差距之小感到惊讶，一些人将其归因于智能体运行的方差和基准测试的非确定性。其他人指出 Mac 更高的上下文限制以及 Mac 端未使用推测解码是潜在的混淆因素。

**标签**: `#LLM`, `#benchmark`, `#quantization`, `#local inference`, `#DeepSeek`

---

<a id="item-13"></a>
## [Krea 2 发布两个功能性 LoRA](https://www.reddit.com/r/StableDiffusion/comments/1uyp5z6/i_released_two_krea_2_functional_loras_identity/) ⭐️ 8.0/10

Krea 2 发布了两个 rank-32 的功能性 LoRA：一个身份参考 LoRA，可在改变服装/姿势的同时保留面部身份；另一个是注册外扩 LoRA，可将源图像放置在画布的特定位置并扩展缺失区域。 这些 LoRA 实现了以前难以实现的新颖图像条件控制行为，例如保留身份的编辑和精确外扩，并且附带了完整的 Diffusers 流水线和可运行示例，使社区能够轻松使用。 身份参考 LoRA 使用 Qwen3-VL 图像条件和干净的 VAE 参考 token，具有隔离的参考注意力和缓存的参考 K/V；而外扩 LoRA 支持单次边缘放置和两次传递计划，用于任意内部放置并带有接缝羽化。

reddit · r/StableDiffusion · /u/Upbeat_Birthday_6123 · 7月17日 04:13

**背景**: Krea 2 是一个开源的 12B 参数扩散变换器 (DiT) 图像生成模型，有两个变体：Raw（全质量）和 Turbo（8 步蒸馏）。LoRA（低秩适应）是一种使用小型适配器权重微调大型模型的技术。Hugging Face 的 Diffusers 库提供了运行扩散模型的标准流水线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/yijunwang2/krea2-reid">yijunwang 2 / krea 2 -reid · Hugging Face</a></li>
<li><a href="https://comfyui-wiki.com/en/models/krea">Krea Family: Open Source Diffusion Transformer with... | ComfyUI Wiki</a></li>

</ul>
</details>

**标签**: `#Stable Diffusion`, `#LoRA`, `#image generation`, `#outpainting`, `#identity reference`

---

<a id="item-14"></a>
## [欧盟 AI 法案 OpenRAG：法律结构化分块与嵌入](https://www.reddit.com/r/MachineLearning/comments/1uytlac/eu_ai_act_openrag_933_legally_structured_chunks/) ⭐️ 8.0/10

新数据集 EU AI Act OpenRAG 将欧盟 AI 法案划分为 933 个法律结构化分块，并附有 BGE-M3 嵌入，存储在一个 SQLite 文件中，其检索召回率优于滑动窗口基线。 该数据集能够为法律自然语言处理任务提供更准确的检索增强生成（RAG），通过将大语言模型锚定在精确的法律条款中，有望改进合规分析和 AI 治理研究。 该语料库按法规的法律结构（条款、序言、定义、附录要点）进行分块，并包含精确的 EUR-Lex 链接、适用日期元数据和窄派生标签；检索场景中文章召回率@20 达到 0.541，基线为 0.449。

reddit · r/MachineLearning · /u/Automatic-Forever-63 · 7月17日 08:18

**背景**: 检索增强生成（RAG）将文档检索与大语言模型生成相结合，以提高事实准确性。BGE-M3 是一个多语言嵌入模型，支持稠密、稀疏和多向量检索。EUR-Lex 是欧盟官方法律数据库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/BAAI/bge-m3?ref=blog-ko.allganize.ai">BAAI/ bge - m 3 · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval - augmented generation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/EUR-Lex">EUR-Lex</a></li>

</ul>
</details>

**社区讨论**: 社区讨论验证了该技术贡献，用户称赞结构化分块方法，并请求增加更多基线以及与其他法律数据集的比较。

**标签**: `#RAG`, `#legal NLP`, `#embeddings`, `#EU AI Act`, `#dataset`

---

<a id="item-15"></a>
## [LLM 隐写工具将消息隐藏在聊天文本中](https://www.reddit.com/r/artificial/comments/1uz1w22/i_built_a_tool_that_hides_messages_in/) ⭐️ 8.0/10

一个名为 Conversation Stenography 的概念验证工具利用 LLM 的 token 概率和算术编码，将加密消息隐藏在生成的文本中，旨在绕过自动内容扫描。 随着消息扫描日益普遍，该技术为保护私人通信提供了一种潜在途径，但也引发了关于被滥用于恶意目的的伦理担忧。 该工具使用 AES-SIV 进行加密和认证，接收方需要拥有相同的模型、分词器、配置、共享密钥和对话状态才能解码消息。

reddit · r/artificial · /u/Nethical69 · 7月17日 14:48

**背景**: 隐写术隐藏消息的存在，而加密则隐藏其内容。基于 LLM 的隐写利用语言模型的概率特性，在 token 选择中嵌入数据，使输出看起来像普通文本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.artkpv.net/Tool-Arithmetic-Coding-for-LLM-Steganography/">Arithmetic Coding Steganography Using Frontier Models</a></li>
<li><a href="https://github.com/artkpv/arithmetic-coding-steganography">GitHub - artkpv/ arithmetic - coding - steganography : Arithmetic ...</a></li>
<li><a href="https://arxiv.org/pdf/2410.04328">OD-Stega: LLM -Based Relatively Secure Steganography via...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论内容充实，用户们就伦理影响、对抗高级扫描的实用性以及滥用可能性展开辩论。一些人称赞其技术新颖性，而另一些人则质疑其统计不可检测性。

**标签**: `#steganography`, `#LLM`, `#privacy`, `#security`, `#AI`

---