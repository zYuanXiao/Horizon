---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> 从 126 条内容中筛选出 15 条重要资讯。

---

1. [Qwen 3.8 发布：2.4T MoE 旗舰模型，开放权重](#item-1) ⭐️ 9.0/10
2. [AirLLM 让 70B 大模型在单张 4GB GPU 上运行](#item-2) ⭐️ 8.0/10
3. [腾讯云 Agent Memory：面向 AI 代理的团队级记忆中枢](#item-3) ⭐️ 8.0/10
4. [Qwen-UI-Agent：面向真实世界的基座 GUI 智能体](#item-4) ⭐️ 8.0/10
5. [Metis：首个具备原生记忆能力的记忆基础模型](#item-5) ⭐️ 8.0/10
6. [关于 AI 发展的公开信：微软、Anthropic 与前沿节奏](#item-6) ⭐️ 8.0/10
7. [中国 DFSX 宣称内存带宽为 NVIDIA GB200 的两倍](#item-7) ⭐️ 8.0/10
8. [llama.cpp 为 DeepSeek V4 Flash 添加 MTP/DSpark 支持](#item-8) ⭐️ 8.0/10
9. [KV 缓存量化损害 DeepSeek V4 Flash 输出质量](#item-9) ⭐️ 8.0/10
10. [虚假 16.5 万亿参数模型暴露 Hugging Face 参数统计漏洞](#item-10) ⭐️ 8.0/10
11. [Kimi K3 通过 NVMe 流式加载在 8GB 内存的单 CPU 上运行](#item-11) ⭐️ 8.0/10
12. [Mference 引擎在 5.3GB 内存上运行 284B DeepSeek-V4-Flash](#item-12) ⭐️ 8.0/10
13. [NVIDIA SANA-Video 2.0：混合注意力、快速视频生成，许可证未定](#item-13) ⭐️ 8.0/10
14. [Minimax H3 开源权重登陆 ComfyUI，支持 1080p、25 秒视频](#item-14) ⭐️ 8.0/10
15. [欧盟人工智能法案第 50 条生效，强制披露 AI 生成内容](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen 3.8 发布：2.4T MoE 旗舰模型，开放权重](https://www.reddit.com/r/LocalLLaMA/comments/1ve02j9/qwen_38_is_live_now/) ⭐️ 9.0/10

阿里巴巴 Qwen 团队发布了 Qwen 3.8，这是一个 2.4 万亿参数的混合专家（MoE）旗舰模型，并承诺很快开放权重。更小的 27B 变体计划于下周发布。 此次发布代表了开放权重 AI 模型的重大进步，可能使最先进的编码和专业工作能力更加普及。它可能加剧开源模型提供商之间的竞争，并加速企业和开发者社区的采用。 据公告称，旗舰模型能够自主编码并交付跨越 10 天以上的完整项目。目前已在 Qwen Cloud 上线，预计很快开放权重，27B 变体将于下周发布。

reddit · r/LocalLLaMA · /u/Mobile-Pumpkin7944 · 8月3日 01:51

**背景**: Qwen 是阿里巴巴云开发的大语言模型系列，以发布开放权重的稠密和 MoE 模型而闻名。混合专家（MoE）架构每次只激活部分参数，从而在保持计算效率的同时实现大规模扩展。自主编码代理是能够在最少人工干预下规划、编写、测试和调试代码的 AI 系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.labellerr.com/blog/qwen-3-8-alibabas-next-gen-multimodal-ai/">Qwen 3 . 8 : Alibaba's Next-Gen Multimodal AI</a></li>
<li><a href="https://github.com/QwenLM/Qwen3">GitHub - QwenLM/ Qwen 3 : Qwen 3 is the large language model series...</a></li>
<li><a href="https://huggingface.co/Qwen">Org profile for Qwen on Hugging Face, the AI community building the...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Qwen`, `#Open Source`, `#MoE`

---

<a id="item-2"></a>
## [AirLLM 让 70B 大模型在单张 4GB GPU 上运行](https://github.com/lyogavin/airllm) ⭐️ 8.0/10

由 lyogavin 开发的开源项目 AirLLM 单日获得 819 颗星，总星数达 25785。它无需量化、蒸馏或剪枝，即可在单张 4GB GPU 上运行 70B 参数的大语言模型。 这一突破使大语言模型的获取更加普及，让硬件有限的个人和小团队也能运行之前需要多块高端 GPU 的模型。它可能加速资源受限环境中 LLM 的创新和采用。 AirLLM 采用逐层加载技术，从磁盘一次加载一层模型，大幅降低内存占用。它还支持在 8GB 显存上运行 Llama 3.1 405B，并对中文大模型有良好支持。

github_trending · GitHub Trending · 8月3日 02:52

**背景**: 像 70B 这样的大语言模型参数大小约为 130GB，仅加载就需要多块高端 GPU（例如 2 块 A100）。传统优化方法包括量化、蒸馏和剪枝，但 AirLLM 通过逐层加载避免了这些方法，使得在显存极小的消费级硬件上运行成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/lyogavin/airllm">GitHub - lyogavin/ airllm : AirLLM 70 B inference with single 4 GB GPU</a></li>
<li><a href="https://huggingface.co/blog/lyogavin/airllm">Unbelievable! Run 70 B LLM Inference on a Single 4 GB GPU with...</a></li>
<li><a href="https://explainx.ai/blog/airllm-run-70b-llm-4gb-gpu-inference-2026">AirLLM: Run 70B LLM on 4GB GPU, No Quantization (2026) | explainx.ai Blog | explainx.ai</a></li>

</ul>
</details>

**社区讨论**: 社区表现出浓厚兴趣，星标增长迅速，反响积极。用户赞赏其带来的可及性，但也有讨论指出由于磁盘 I/O，推理速度可能存在权衡。

**标签**: `#LLM`, `#GPU`, `#inference`, `#optimization`, `#open-source`

---

<a id="item-3"></a>
## [腾讯云 Agent Memory：面向 AI 代理的团队级记忆中枢](https://github.com/TencentCloud/TencentDB-Agent-Memory) ⭐️ 8.0/10

腾讯云推出的新开源项目 TencentDB Agent Memory 单日获得 602 颗星，总星数达到 11168 颗。它将对话、文档和代码转化为四种可复用的记忆资产：Chat Memory、Skill、LLM-Wiki 和 Code-Graph。 该项目解决了多智能体系统中的关键挑战：持久化、共享记忆。通过提供可治理、可共享的记忆层，它可能显著提升 AI 代理和框架之间的协作与效率，并可能影响企业 AI 系统的构建方式。 该项目使用 TypeScript 编写，支持从对话和任务中自动提取记忆资产，并将文档和代码转换为 Wiki 和 CodeGraph。它强调跨代理和框架对这些资产进行治理、审查和路由。

github_trending · GitHub Trending · 8月3日 02:52

**背景**: AI 代理通常难以在交互中保留上下文，导致重复或不一致的行为。像 Mem0 和 Zep 这样的记忆管理解决方案提供了持久上下文，但 TencentDB Agent Memory 专注于团队级别的共享和治理。LLM-Wiki 的概念，如近期文章所讨论的，将使用结构化 markdown 文件作为代理的活记忆这一想法形式化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/TencentCloud/TencentDB-Agent-Memory">GitHub - TencentCloud/TencentDB-Agent-Memory: TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.</a></li>
<li><a href="https://github.com/TencentCloud/TencentDB-Agent-Memory/blob/main/README_CN.md">TencentDB-Agent-Memory/README_CN.md at main · TencentCloud/TencentDB-Agent-Memory</a></li>
<li><a href="https://www.decodingai.com/p/llm-wiki-agent-memory">LLM Wikis as Living Memory for AI Agents</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Memory Management`, `#Multi-Agent Systems`, `#LLM`, `#Developer Tools`

---

<a id="item-4"></a>
## [Qwen-UI-Agent：面向真实世界的基座 GUI 智能体](https://huggingface.co/papers/2607.28227) ⭐️ 8.0/10

Qwen-UI-Agent 是一个新的基座 GUI 智能体，它在单一动作空间中统一了 GUI 和 CLI 操作，支持长时程任务，并采用 AutoResearch 风格的数据飞轮实现自主改进。它在移动端基准测试中取得了最先进的性能，包括在 MobileWorld 上达到 82.1%，在 MobileWorld-Real 上达到 92.2%。 这项工作通过支持在真实设备上的可靠操作、跨平台工作流以及以最少人力实现自主改进，推动了 GUI 智能体向真实世界部署迈进。它在移动端基准测试中取得了新的最先进成果，并在计算机和浏览器任务上与 Opus 4.8、GPT-5.6 Sol 等前沿模型相比表现出竞争力，可能影响未来人机交互领域的研究和应用。 该智能体将多样化的沙盒环境与大规模真实设备移动运行时相结合，其统一动作空间将 GUI 操作与 CLI 执行交错进行，并在单次模型回合中生成批量动作。在线强化学习支持在超过 100 步的轨迹上进行训练，并拥有超过 10,000 个并发环境，轻量级的 harness 层支持在移动端和计算机上主动启动服务和有状态工作流。

huggingface_papers · Hugging Face Papers · 7月31日 00:00

**背景**: GUI 智能体是能够与图形用户界面交互以在数字设备上执行任务的 AI 系统，例如点击按钮、输入文本或导航菜单。传统的 GUI 智能体通常依赖脚本规则或有限的动作空间，而基于基础模型的智能体可以更灵活地感知屏幕并规划动作。AutoResearch 风格的数据飞轮是一种方法，智能体自动构建任务、诊断失败并规划改进，减少了对人工标注的需求。本报告建立在 MAI-UI 等先前工作的基础上，旨在创建能够在移动端、计算机和网页环境中工作的智能体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tongyi-mai.github.io/Qwen-UI-Agent/Qwen-UI-Agent-Technical-Report.pdf">2026-07-29 Qwen-UI-Agent Technical Report: Toward Next-Generation</a></li>
<li><a href="https://arxiv.org/html/2607.28227v1">Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents</a></li>
<li><a href="https://github.com/QwenLM/Qwen-Agent">GitHub - QwenLM/Qwen-Agent: Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc. · GitHub</a></li>

</ul>
</details>

**标签**: `#GUI agents`, `#AI agents`, `#Foundation models`, `#Human-computer interaction`, `#Reinforcement learning`

---

<a id="item-5"></a>
## [Metis：首个具备原生记忆能力的记忆基础模型](https://huggingface.co/papers/2607.26760) ⭐️ 8.0/10

该论文提出了记忆基础模型的概念，并介绍了 Metis——首个将持久、动态演化的记忆状态直接集成到模型主干中，并通过记忆注意力访问的原型。这实现了无梯度的在线记忆维护和推理过程中的自主记忆程序。 这项工作挑战了 AI 智能体中传统的外部记忆模块设计，可能改变智能体记忆的架构方式。通过使记忆成为原生能力，它有望带来更高效、端到端优化的智能体，并提升长期推理和适应性。 Metis 采用了一种新架构，具有原生记忆状态，将历史信息压缩到模型中。在线记忆维护是无梯度的，仅需一次前向传播，并且在推理过程中所有学习到的权重保持冻结。

huggingface_papers · Hugging Face Papers · 7月31日 00:00

**背景**: 基础模型是在广泛数据上训练的大型 AI 模型，但它们通常缺乏持久记忆，依赖外部模块实现智能体记忆。本文提出将记忆内化为原生能力，将其形式化为持久状态和自主程序，在架构和效率方面可能具有优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.26760">[2607.26760] Metis: Memory Foundation Model</a></li>
<li><a href="https://huggingface.co/papers/2607.26760">Paper page - Metis : Memory Foundation Model</a></li>
<li><a href="https://www.alphaxiv.org/abs/2607.26760">Metis : Memory Foundation Model | alphaXiv</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#memory`, `#foundation models`, `#architecture`, `#research`

---

<a id="item-6"></a>
## [关于 AI 发展的公开信：微软、Anthropic 与前沿节奏](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 8.0/10

Simon Willison 总结了近期关于 AI 发展的公开信，包括微软主导的、由 235 家公司签署的《开放权重与美国 AI 领导力》，Anthropic 的回应，以及由前沿 AI 公司 1324 名员工签署的《前沿节奏》。 这些公开信反映了围绕开放权重 AI 模型和 AI 发展速度的重大政策辩论，对监管、国家安全和开源社区都有影响。主要公司和知名 AI 人物的参与凸显了其重要性。 微软的信支持蒸馏技术，而 Anthropic 反对工业规模的蒸馏操作。《前沿节奏》呼吁国际治理工具来调控自动化 AI 发展，签署者包括 Jakub Pachocki 和 Ilya Sutskever 等人。

rss · Simon Willison · 8月2日 04:16

**背景**: 开放权重模型允许公众访问模型权重，便于定制和审查，而封闭模型则不然。争论的焦点在于平衡创新与安全，担心威权政府滥用以及 AI 权力集中的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/2/july-newsletter/">July 2026 newsletter | Simon Willison ’s Weblog</a></li>

</ul>
</details>

**标签**: `#AI`, `#open source`, `#policy`, `#governance`, `#Simon Willison`

---

<a id="item-7"></a>
## [中国 DFSX 宣称内存带宽为 NVIDIA GB200 的两倍](https://www.reddit.com/r/LocalLLaMA/comments/1vduej3/chinas_dfsx_offers_2x_the_memory_bandwidth_of/) ⭐️ 8.0/10

中国的 DFSX 推出了基于 14nm DF2000 芯片的 TY64 SuperNode，据称其内存带宽达到 960TB/s，是 NVIDIA GB200 NVL72 系统 576TB/s 的两倍。该设计采用 3D 混合键合技术，通过垂直计算-内存塔结构，跳过了传统的微凸块。 这一进展可能显著改变 AI 硬件的竞争格局，尤其是在内存带宽成为关键瓶颈的推理任务中。如果得到验证，它可能挑战 NVIDIA 在 AI 加速器市场的主导地位，并为中国在出口管制背景下提供更自主的替代方案。 TY64 SuperNode 由 64 个 DF2000 芯片组成，提供 33.28 PFLOPS 的 BF16 算力、409.6 TB/s 的内存带宽和 57.6 TB/s 的扩展带宽，功耗为 120 kW（每芯片约 2 kW）。DF2000 芯片本身今年可实现 1.6T 互连和 15 TB/s 内存带宽，以及 1000T BF16 算力。

reddit · r/LocalLLaMA · /u/MundanePercentage674 · 8月2日 21:39

**背景**: 内存带宽是指数据从内存中读取或存储的速率，对于 AI 工作负载至关重要，尤其是在推理任务中，大型模型需要快速的数据访问。NVIDIA 的 GB200 NVL72 系统使用 HBM3e 内存实现了 576 TB/s 的带宽，而 DFSX 的方法采用 3D 混合键合技术垂直堆叠 DRAM 层，可能以更低的成本提供更高的带宽，因为它使用了成熟的 14nm 工艺技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/chinas-dfsx-offers-2x-the-memory-bandwidth-of-nvidias-gb200-nvl72-system-with-a-14nm-supernode-that-skips-microbumps-for-vertical-compute-memory-towers/">China's DFSX Offers 2x The Memory Bandwidth Of NVIDIA's GB200 NVL72 System With a 14nm SuperNode That Skips Microbumps for Vertical Compute-Memory Towers</a></li>
<li><a href="https://x.com/tphuang/status/2083643170525528440">tphuang on X: "What does DFSX chips look like. Here is a showcase of how effective 3D hybrid bonding approach can improve the inference speed. DF2000 using multiple logic chiplet + layers of DRAM can achieve 1.6T interconnect + 15 TB/s memory bandwidth w/ 1000T BF16 compute this year. https://t.co/Ly3Ou82vdm" / X</a></li>
<li><a href="https://www.nexgencloud.com/blog/case-studies/nvidia-gb200-user-guide-specs-features-and-use-cases">NVIDIA GB200 User Guide: Specs, Features and Use Cases</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#memory bandwidth`, `#China`, `#NVIDIA`, `#inference`

---

<a id="item-8"></a>
## [llama.cpp 为 DeepSeek V4 Flash 添加 MTP/DSpark 支持](https://www.reddit.com/r/LocalLLaMA/comments/1vdhgq9/llamacpp_just_added_mtp_dspark_support_for/) ⭐️ 8.0/10

llama.cpp 已合并拉取请求 #25784，为 DeepSeek V4 Flash 的多令牌预测（MTP）和 DSpark 投机解码添加了支持。这使得该模型在本地硬件上的推理更加高效。 此次更新对本地大语言模型社区意义重大，因为它将先进的推理优化带到了消费级硬件上，可能提升速度并减少资源占用。这也凸显了围绕 DeepSeek 模型和投机解码技术不断壮大的生态系统。 该支持包含在 b10228 版本中，提供了适用于 macOS、Linux、Windows 和 Android 等多个平台的二进制文件。DSpark 是一种投机解码框架，旨在加速令牌生成，而 MTP 是一种训练技术，可重新用于推理加速。

reddit · r/LocalLLaMA · /u/rmhubbert · 8月2日 12:58

**背景**: DeepSeek V4 Flash 是一个拥有 1653 亿参数的开源语言模型，支持高达 1,048,576 个令牌的上下文窗口。多令牌预测（MTP）最初是为了提升训练性能而引入的，但其模块可用于在推理时预测多个未来令牌，从而减少解码步骤。投机解码（如 DSpark）使用草稿模型提出令牌，然后由主模型验证，从而提高吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/mtp.html">Accelerating DeepSeek-V3 inference using multi-token prediction in SGLang — Tutorials for AI developers 14.0</a></li>
<li><a href="https://medium.com/@bingqian/understanding-multi-token-prediction-mtp-in-deepseek-v3-ed634810c290">Understanding Multi-Token Prediction (MTP) in DeepSeek-V3 | by Bing | Medium</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/mtp/">Multi-Token Prediction (MTP) | Sebastian Raschka, PhD</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark">deepseek -ai/ DeepSeek - V 4 - Flash - DSpark · Hugging Face</a></li>
<li><a href="https://llmrun.dev/model/deepseek-ai-deepseek-v4-flash-dspark">DeepSeek V 4 Flash DSpark — Hardware Requirements... | llmrun</a></li>
<li><a href="https://kingy.ai/news/deepseek-dspark-speculative-decoding/">DeepSeek DSpark Explained: Speculative Decoding for Faster AI</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#DeepSeek`, `#MTP`, `#DSpark`, `#local LLM`

---

<a id="item-9"></a>
## [KV 缓存量化损害 DeepSeek V4 Flash 输出质量](https://www.reddit.com/r/LocalLLaMA/comments/1vduxth/you_really_should_not_quantize_kv_cache_for/) ⭐️ 8.0/10

一位 Reddit 用户报告称，将 DeepSeek V4 Flash 的 KV 缓存从 BF16 量化到 Q8 会显著降低输出质量，通过困惑度、KL 散度和 token 概率变化来衡量。相比之下，对 Qwen 397B 进行同样的量化影响很小。 这一发现对部署 DeepSeek V4 Flash 的从业者至关重要，因为 KV 缓存量化是减少内存占用和加速推理的常用技术。显著的质量下降表明这种优化可能不适用于该模型，可能影响部署策略和用户体验。 对于 DeepSeek V4 Flash，平均困惑度从 5.8397 增加到 5.8771，平均 KL 散度为 0.1459，最大值为 12.47。相同 top-p token 的比例降至 87.19%，token 概率的 RMS 变化为 11.88%。相比之下，Qwen 397B 的平均 KL 散度仅为 0.0036，相同 top-p 比例为 97.93%。

reddit · r/LocalLLaMA · /u/erazortt · 8月2日 22:01

**背景**: KV 缓存量化减少了 LLM 推理期间使用的键值缓存的内存占用，从而支持更长的上下文和更快的处理。困惑度衡量模型预测样本的好坏，越低越好，而 KL 散度量化原始模型与量化模型输出分布之间的差异。DeepSeek V4 Flash 是一个效率优化的混合专家模型，总参数 284B，激活参数 13B，支持 1M token 的上下文窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V 4 Flash - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/">Quantized KV Cache - vLLM</a></li>

</ul>
</details>

**标签**: `#KV cache quantization`, `#DeepSeek V4 Flash`, `#LLM inference`, `#quality impact`, `#perplexity`

---

<a id="item-10"></a>
## [虚假 16.5 万亿参数模型暴露 Hugging Face 参数统计漏洞](https://www.reddit.com/r/LocalLLaMA/comments/1vdh1us/vacuum_16t/) ⭐️ 8.0/10

一位用户在 Hugging Face 上传了名为“vacuum-16t”的仓库，通过 safetensors 头部声明了 16.5 万亿参数，但实际不包含任何真实数据。尽管模型内容全为零，它仍占据了 Hub 参数排行榜首位。 这一讽刺性行为揭示了关键的信任问题：Hugging Face 仅根据元数据计算参数数量，任何人都可以操纵排行榜。它凸显了 AI 社区需要更稳健的模型评估和验证机制。 该模型在 385 个分片中声明了 3,841 个形状为[65536, 65536]的 F4 张量，外加一个[4294967296, 1]张量，总计 16,501,264,351,232 个参数。尽管声明了 8.25 TB 的数据，由于 Xet 内容定义分块去重，实际上传字节仅约 692 KB，但存储配额仍按完整逻辑大小计费。

reddit · r/LocalLLaMA · /u/alerikaisattera · 8月2日 12:39

**背景**: Hugging Face 的模型页面通过解析 safetensors 头部来显示参数数量，头部包含张量形状和数据类型，而不读取实际张量数据。这种仅基于元数据的方法虽然高效，但容易受到操纵。Safetensors 是一种安全的序列化格式，将张量元数据和原始数据分开存储，其头部包含一个 JSON，包含张量名称、形状和数据偏移量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/docs/safetensors/index">Safetensors · Hugging Face</a></li>
<li><a href="https://huggingface.co/docs/safetensors/metadata_parsing">Metadata Parsing · Hugging Face</a></li>
<li><a href="https://github.com/huggingface/safetensors">GitHub - safetensors/safetensors: Simple, safe way to store and distribute tensors · GitHub</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论可能称赞这一演示的巧妙，并辩论其对模型信任和评估的影响。有些人可能认为参数数量本来就不是一个好指标，而另一些人可能呼吁 Hugging Face 更彻底地验证模型完整性。

**标签**: `#Hugging Face`, `#model evaluation`, `#security`, `#LLM`, `#satire`

---

<a id="item-11"></a>
## [Kimi K3 通过 NVMe 流式加载在 8GB 内存的单 CPU 上运行](https://www.reddit.com/r/LocalLLaMA/comments/1vd874t/i_pushed_kimi_k3_onto_one_cpu_with_8_gb_of_ram/) ⭐️ 8.0/10

一位开发者编写了一个 C99 推理引擎，通过从 NVMe 流式加载专家权重并使用打包的 4 位算术，在仅有 8GB 内存的单 CPU 上运行了 1.56TB 的 MoE 模型 Kimi K3，实现了约每 token 33 秒的速度。 这证明了巨大的 MoE 模型可以在极简硬件上运行，为边缘部署和本地实验开辟了可能性。同时，它展示了新颖的优化技术，可能影响未来的推理框架。 该引擎按需从 NVMe 流式加载 93% 的路由专家，从不常驻内存，并直接从打包的 4 位形式进行乘法运算，无需反量化。在最小预设下峰值 RSS 为 8.24GB，且在不同内存预算下输出字节级一致。

reddit · r/LocalLLaMA · /u/FareedKhan557 · 8月2日 04:26

**背景**: Kimi K3 是 Moonshot AI 推出的 2.8 万亿参数的混合专家（MoE）模型，每个 token 激活 1040 亿参数。MoE 模型每个 token 只激活部分专家，开发者利用这一点从磁盘流式加载专家。打包的 4 位算术降低了内存带宽和存储需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://vast.ai/model/kimi-k3">Kimi K 3 - AI Model Library | Build on Vast.ai</a></li>
<li><a href="https://lmstudio.ai/models/kimi-k3">Kimi K 3</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区称赞这一成就令人印象深刻且巧妙，许多人询问实际权衡和潜在改进。一些人质疑每 token 33 秒的实用性，但承认其教育价值和方法的创新性。

**标签**: `#LLM inference`, `#MoE`, `#CPU inference`, `#optimization`, `#Kimi K3`

---

<a id="item-12"></a>
## [Mference 引擎在 5.3GB 内存上运行 284B DeepSeek-V4-Flash](https://www.reddit.com/r/LocalLLaMA/comments/1vdbix4/deepseekv4flash_284b_on_53gb_of_memory/) ⭐️ 8.0/10

一款名为 Mference 的新推理引擎使得在 24GB Mac 上仅用约 5.3GB 内存即可运行 284B 参数的 DeepSeek-V4-Flash 模型，速度最高可达每秒 4.8 个 token。该引擎通过从 SSD 流式加载专家权重，而非将其常驻内存。 这展示了一种在消费级硬件上运行超大规模混合专家（MoE）模型的实用方法，可能使最先进的 LLM 更加普及。它可能影响未来的本地推理工具，并降低 AI 实验的硬件门槛。 该模型采用 2 位动态量化，磁盘占用约 91GB。引擎还支持 Gemma 4 26B-A4B 和 Qwen 3.6 35B-A3B，并附带原生 Mac 应用，支持多轮对话、OpenAI 兼容服务器以及本地文件附件。

reddit · r/LocalLLaMA · /u/Blahblahblakha · 8月2日 07:28

**背景**: 混合专家（MoE）模型每个 token 只激活一小部分参数，从而实现高效推理。SSD 流式加载利用这一特性，将共享核心和 KV 缓存保留在内存中，按需从磁盘加载选中的专家，从而将 RAM 从固定限制转变为灵活资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mindstudio.ai/blog/ssd-streaming-ai-models-ram-dial">SSD Streaming for AI Models: How to Turn RAM from a Wall into a Dial | MindStudio</a></li>
<li><a href="https://github.com/ml-explore/mlx-lm/issues/1438">Feature request: MoE expert streaming / SSD offload for memory-constrained Apple Silicon (run 395 GB GLM-5.2-mxfp4 on 128 GB RAM) · Issue #1438 · ml-explore/mlx-lm</a></li>
<li><a href="https://mljourney.com/how-to-quantize-llms-to-8-bit-4-bit-2-bit/">How to Quantize LLMs to 8-bit, 4-bit, 2-bit - ML Journey</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对这一技术成就印象深刻，指出虽然该模型在几轮对话后实用性有限，但这是在低内存设备上运行大型 MoE 模型的重要一步。一些用户对作者提到的权衡和未来改进表示好奇。

**标签**: `#MoE`, `#LLM inference`, `#Local LLM`, `#SSD streaming`, `#Mac`

---

<a id="item-13"></a>
## [NVIDIA SANA-Video 2.0：混合注意力、快速视频生成，许可证未定](https://www.reddit.com/r/StableDiffusion/comments/1vdxwzg/sanavideo_20_nvidias_new_hybridattention_video/) ⭐️ 8.0/10

NVIDIA 发布了 SANA-Video 2.0，这是一个视频扩散 Transformer，提供 5B 和 14B 参数版本，采用混合线性-softmax 注意力机制（3:1 比例）和 Sol-Engine 加速，在相同硬件上比 Wan 2.2-A14B 快最多 120 倍。该模型可在单个 RTX 5090 上生成 720p 视频，在 H100 上生成 480p 视频仅需 13.2 秒。 此次发布意义重大，因为它引入了一种新颖的混合注意力架构，将线性注意力的速度与 softmax 注意力的表现力相结合，可能为高效视频生成树立新标准。这也是 NVIDIA 首个明确面向消费级 GPU 的视频模型，可能使高质量视频生成普及到个人创作者和研究人员。 混合注意力使用 75%的门控线性注意力实现 O(N)缩放，以及 25%的门控 softmax 锚点来保持全秩 token 交互，解决了纯线性注意力的秩瓶颈。Sol-Engine 优化包括内核融合、缓存、稀疏注意力、TensorRT 图优化以及 MXFP4/MXFP8 支持，使得在单个 RTX 5090 上实现全 720p 生成。该模型在 VBench 上得分 84.30，在 H100 上生成 720p/5s 视频仅需 13.06 秒。

reddit · r/StableDiffusion · /u/mmowg · 8月3日 00:11

**背景**: 视频扩散模型通过迭代去噪随机噪声来生成视频，注意力机制对于捕捉长距离依赖至关重要。线性注意力提供线性时间复杂度，但存在低秩表示问题，而 softmax 注意力表现力强但复杂度为二次方。混合方法旨在结合两者优点，SANA-Video 2.0 就是一个典型例子。NVIDIA 的 SANA 图像模型以 Apache 2.0 许可证开源，但视频模型的许可证尚未公布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openreview.net/forum?id=4cP69sGjiG">Training-time Selection of Linear Vs. Softmax Attention in Layer-based Hybrid Transformers | OpenReview</a></li>
<li><a href="https://www.emergentmind.com/topics/hybrid-linear-attention-mechanism">Hybrid Linear Attention Mechanism</a></li>
<li><a href="https://arxiv.org/pdf/2603.15031">Attention Residuals</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对性能和架构感到兴奋，但主要担忧是许可证的不确定性。用户猜测 NVIDIA 是否会像图像模型那样开源，还是保持封闭，一些人希望至少提供推理权重。还有讨论将 SANA-Video 2.0 与 Wan 2.2 等其他模型进行比较，注意到其显著的速度优势。

**标签**: `#video generation`, `#diffusion models`, `#NVIDIA`, `#attention mechanisms`, `#AI research`

---

<a id="item-14"></a>
## [Minimax H3 开源权重登陆 ComfyUI，支持 1080p、25 秒视频](https://www.reddit.com/r/StableDiffusion/comments/1vd9o0r/minimax_h3_1080p_25_seconds_text_to_video_in/) ⭐️ 8.0/10

Minimax H3 是一款新的开源权重文本生成视频模型，现已原生支持 ComfyUI，可在消费级硬件上生成高达 1080p 分辨率、25 秒以上的视频片段。模型权重已在 Hugging Face 上发布，优化版本将内存占用减少了 66%。 这标志着高质量 AI 视频生成的民主化迈出了重要一步，因为开源权重模型加上对消费级硬件的友好性能，可以促进更广泛的采用和创新。同时，这也巩固了 ComfyUI 作为可访问 AI 视频工作流领先平台的地位。 该模型支持多种输入模式，包括文本生成视频、图像生成视频、首尾帧生成视频和参考生成视频，最高支持 2K 分辨率和 15 秒片段。ComfyUI 的优化包括剪枝调制权重和 int8 量化，将内存从 123.6 GB 降至 42.5 GB，从而能够在 12GB 显存的 RTX 3060 上运行。

reddit · r/StableDiffusion · /u/comfyanonymous · 8月2日 05:44

**背景**: Minimax H3 是 MiniMax 推出的前沿视频生成模型，其 Hailuo AI 视频平台广为人知。像这样的开源权重模型允许开发者和爱好者本地运行最先进的 AI，促进定制化和隐私保护。ComfyUI 是一个流行的基于节点的 AI 图像和视频生成界面，通过自定义工作流支持多种模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hailuoai.video/tools/minimax-h3">MiniMax H 3 Multimodal AI Video Model | Hailuo AI</a></li>
<li><a href="https://fal.ai/models/minimax/h3/text-to-video">MiniMax H 3 ( Text to Video ) API on fal</a></li>
<li><a href="https://docs.comfy.org/tutorials/video/ltx/ltx-2-3">LTX-2.3: ComfyUI Workflow Examples - ComfyUI</a></li>

</ul>
</details>

**社区讨论**: 社区反应热烈，用户对 ComfyUI 的当日支持和为消费级硬件优化所做的重大工程努力表示赞赏。一些人在讨论模型的能力和潜在限制，而另一些人则渴望在自己的系统上测试它。

**标签**: `#text-to-video`, `#ComfyUI`, `#open-weights`, `#AI video generation`, `#Minimax H3`

---

<a id="item-15"></a>
## [欧盟人工智能法案第 50 条生效，强制披露 AI 生成内容](https://www.reddit.com/r/artificial/comments/1vdlbbx/the_eu_ai_act_makes_failure_to_disclose/) ⭐️ 8.0/10

8 月 2 日，欧盟《人工智能法案》第 50 条生效，要求部署 AI 系统生成或操纵文本以用于公共利益目的的部署者披露该内容为 AI 生成。除非内容经过人工审查或编辑控制，或用于执法目的，否则此义务适用。 该法规对不合规行为引入了重大的法律和财务后果，可能影响像普华永道这样在报告中使用幻觉 AI 生成内容的大型咨询公司。它标志着欧盟范围内对 AI 内容部署问责制的更广泛推动，影响任何向欧盟受众发布 AI 生成文本的组织。 违反第 50 条的处罚可能相当严厉，不合规的罚款最高可达 750 万欧元或全球年营业额的 1.5%。该义务特别针对为告知公众公共利益事项而发布的文本，不适用于经过人工审查或编辑控制的内容，也不适用于执法用途。

reddit · r/artificial · /u/SpiritRealistic8174 · 8月2日 15:41

**背景**: 欧盟《人工智能法案》是一项全面的 AI 监管法规，其中第 50 条侧重于对生成或操纵内容的 AI 系统的透明度义务。AI 幻觉是指 AI 模型产生虚假或捏造信息的情况，这已成为咨询报告中的一个担忧，正如 GPTZero 在普华永道《转型治理》报告中检测到虚假引用所强调的那样。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gdprlocal.com/eu-ai-act-article-50/">EU AI Act Article 50 : Transparency Rules for Businesses - GDPR Local</a></li>
<li><a href="https://sherwood.news/tech/ai-hallucinations-appear-to-be-creeping-into-consulting-reports/">AI hallucinations appear to be creeping into consulting reports</a></li>
<li><a href="https://developmentcorporate.com/corporate-development/ai-hallucinations-in-consulting-reports-are-now-an-enterprise-due-diligence-crisis/">AI Hallucinations in Consulting Reports ... - Development Corporate</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论强调了普华永道和德勤等咨询公司因 AI 幻觉而面临抵制的真实案例，一些用户指出新法规可能导致罚款。对于执法存在怀疑，同时也有人支持加强问责制，一些评论者指出人工审查豁免可能造成漏洞。

**标签**: `#EU AI Act`, `#AI regulation`, `#AI-generated content`, `#compliance`, `#legal`

---