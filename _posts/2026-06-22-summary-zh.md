---
layout: default
title: "Horizon Summary: 2026-06-22 (ZH)"
date: 2026-06-22
lang: zh
---

> 从 148 条内容中筛选出 15 条重要资讯。

---

1. [AirLLM 在单张 4GB GPU 上运行 70B 大模型](#item-1) ⭐️ 8.0/10
2. [字节跳动开源 DeerFlow 超级智能体框架](#item-2) ⭐️ 8.0/10
3. [Moebius：轻量级图像修复媲美百亿参数模型](#item-3) ⭐️ 8.0/10
4. [DragMesh-2：与铰接物体的灵巧手交互新方法](#item-4) ⭐️ 8.0/10
5. [Hotz：AI 末日叙事推高估值](#item-5) ⭐️ 8.0/10
6. [Google IPv6 流量突破 50% 里程碑](#item-6) ⭐️ 8.0/10
7. [三星向员工部署 ChatGPT Enterprise 和 Codex](#item-7) ⭐️ 8.0/10
8. [本地 LLM 推理优化完全指南](#item-8) ⭐️ 8.0/10
9. [Qwen 在关键人物离职后转向闭源](#item-9) ⭐️ 8.0/10
10. [爱好者仅花 800 美元训练 500M 参数 LLM 和 330M 图像生成器](#item-10) ⭐️ 8.0/10
11. [本地视觉模型最佳选择：第二次基准测试更新](#item-11) ⭐️ 8.0/10
12. [Gemma 4 QAT 模型对 KV 缓存量化表现出鲁棒性](#item-12) ⭐️ 8.0/10
13. [PermaVid：通过解耦上下文内存实现一致视频生成](#item-13) ⭐️ 8.0/10
14. [发布 GPT-2 中等规模的免 Softmax 注意力模型](#item-14) ⭐️ 8.0/10
15. [AI 生成书籍和音乐激增，数量超过人类作品](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AirLLM 在单张 4GB GPU 上运行 70B 大模型](https://github.com/lyogavin/airllm) ⭐️ 8.0/10

AirLLM 是一个开源推理优化库，现在可以在单张 4GB GPU 上运行 700 亿参数的大语言模型，无需量化、蒸馏或剪枝。它还支持在 8GB 显存上运行 405B Llama 3.1。 这一突破消除了对昂贵多 GPU 设备的需求，使拥有消费级 GPU 的开发者和研究人员能够实验最先进的模型，从而普及大型 LLM 的访问。它可能加速边缘 AI 和本地部署场景中的创新。 AirLLM 采用逐层推理技术，每次只将一个 transformer 层加载到 GPU 内存中，从而大幅降低峰值内存使用。该技术不牺牲模型精度，因为它避免了量化或其他压缩方法。

github_trending · GitHub Trending · 6月22日 04:34

**背景**: 像 Llama 3 70B 这样的大语言模型由于参数量巨大（超过 130GB），通常需要多块高端 GPU（例如 2× A100 100GB）进行推理。AirLLM 的逐层方法利用了推理过程中每次只有一层处于活跃状态的特性，实现了高效的内存复用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/lyogavin/airllm">GitHub - lyogavin/ airllm : AirLLM 70 B inference with single 4 GB GPU</a></li>
<li><a href="https://huggingface.co/blog/lyogavin/airllm">Unbelievable! Run 70 B LLM Inference on a Single 4 GB GPU with...</a></li>
<li><a href="https://www.blog.brightcoding.dev/2026/02/27/airllm-run-70b-models-on-4gb-gpus-without-compromise">AirLLM: Run 70B Models on 4GB GPUs Without Compromise</a></li>

</ul>
</details>

**社区讨论**: 社区反响极为积极，许多人称赞该工具的实用性和可及性。一些用户对推理速度和批处理限制提出了疑问，但总体情绪非常热烈。

**标签**: `#LLM`, `#inference`, `#GPU`, `#open-source`, `#deep learning`

---

<a id="item-2"></a>
## [字节跳动开源 DeerFlow 超级智能体框架](https://github.com/bytedance/deer-flow) ⭐️ 8.0/10

字节跳动开源了 DeerFlow，这是一个面向长周期任务的超级智能体框架，集成了沙箱、记忆、工具、技能、子智能体和消息网关。该项目单日获得 442 颗星，GitHub 总星数超过 72,000。 DeerFlow 解决了 AI 中长周期任务的挑战，这类任务需要长时间规划和多步骤执行。作为一家大型科技公司开源的项目，它可能加速研究、编程和创意工作中复杂 AI 智能体的开发。 该框架使用 Python 编写，可处理耗时数分钟到数小时的任务。它结合了沙箱（安全执行）、记忆（上下文保持）、工具（外部操作）、技能（专门能力）、子智能体（模块化分解）和消息网关（通信）。

github_trending · GitHub Trending · 6月22日 04:34

**背景**: 长周期任务是 AI 研究中的重大挑战，要求模型在长时间内进行规划和执行，并做出复杂决策。像 DeerFlow 这样的超级智能体框架旨在提供构建此类智能体的结构化方法，集成多个组件以处理不同级别的任务。字节跳动的发布丰富了日益增长的开源智能体框架生态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://john-shulman-gpt4o-gemini-flash.vercel.app/advancements-in-ai-capabilities/long-horizon-tasks">Long - Horizon Tasks – Nextra</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#agent`, `#Python`, `#ByteDance`

---

<a id="item-3"></a>
## [Moebius：轻量级图像修复媲美百亿参数模型](https://huggingface.co/papers/2606.19195) ⭐️ 8.0/10

研究人员提出了 Moebius，一个仅有 0.22B 参数的轻量级图像修复框架，其生成质量可与百亿参数级别的 FLUX.1-Fill-Dev 模型相媲美，同时推理速度提升超过 15 倍。 这一突破使得在资源受限的设备上也能实现高保真图像修复，大幅降低了照片编辑、内容修复等实际应用的部署门槛。 Moebius 引入了 Local-λ Mix Interaction (LλMI)模块，将空间和全局语义先验压缩为固定大小的线性矩阵，并配合完全在潜在空间运行的适应性多粒度蒸馏策略。

huggingface_papers · Hugging Face Papers · 6月19日 00:00

**背景**: 图像修复旨在填补图像中缺失或损坏的区域。像 FLUX.1-Fill-Dev 这样的大规模扩散模型虽然质量高，但需要巨大的计算资源，限制了其使用。知识蒸馏将知识从大型教师模型转移到较小的学生模型，但极端压缩常常导致表示瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hustvl.github.io/Moebius/">Moebius Project Page - hustvl.github.io</a></li>
<li><a href="https://x.com/YS_CodeToRich/status/2068360015090786535">Moebius employs a novel Local-λ Mix Interaction (LλM I) block ...</a></li>

</ul>
</details>

**标签**: `#image inpainting`, `#lightweight model`, `#diffusion model`, `#knowledge distillation`, `#computer vision`

---

<a id="item-4"></a>
## [DragMesh-2：与铰接物体的灵巧手交互新方法](https://huggingface.co/papers/2606.15133) ⭐️ 8.0/10

DragMesh-2 是一个接触驱动的灵巧手与铰接物体交互框架，并提出了 PICA（物理信息感知接触训练机制），该机制无需触觉或力反馈即可增强在变化接触负载下的鲁棒性。 这项工作解决了机器人领域的一个关键挑战：使多指手能够通过持续接触操纵铰接物体（如门或剪刀），这对家用和辅助机器人至关重要。PICA 技术无需昂贵的触觉传感器即可提高策略鲁棒性，使灵巧操作更适用于实际部署。 该方法在七个 GAPartNet 物体上、多种阻尼条件下进行了评估，在接触负载变化下比对比方法具有更强的鲁棒性，同时保持高任务成功率。PICA 在没有触觉或力反馈的情况下将物理信号注入策略学习，解决了在固定动力学下训练的策略过拟合问题。

huggingface_papers · Hugging Face Papers · 6月19日 00:00

**背景**: 与铰接物体的灵巧操作具有挑战性，因为目标部件无法直接驱动，其运动必须通过持续的物理接触产生。传统的几何轨迹回放或开环执行无法建模所需的接触动力学。强化学习策略通常过拟合于标称接触负载，当负载变化时性能下降，尤其是在没有触觉反馈的情况下。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.13644">[2512.13644] World Models for Learning Dexterous Hand-Object ... Contact Driven Functional Grasp Synthesis via Hand-Object ... Tactile-Driven Dexterous In-Hand Writing via Extrinsic ... Tactile-reactive gripper with an active palm for dexterous ... [2504.03515] Dexterous Manipulation through Imitation ... Contact Driven Functional Grasp Synthesis via Hand-Object ...</a></li>
<li><a href="https://arxiv.org/abs/2507.06822">Hierarchical Reinforcement Learning for Articulated Tool ...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#dexterous manipulation`, `#articulated objects`, `#contact-driven`, `#reinforcement learning`

---

<a id="item-5"></a>
## [Hotz：AI 末日叙事推高估值](https://geohot.github.io//blog/jekyll/update/2026/06/21/the-doom-justifies-the-valuation.html) ⭐️ 8.0/10

George Hotz 认为，AI 公司策略性地利用存在风险叙事来为高估值辩护，并将其与 NFT 和元宇宙等过去的科技炒作周期相类比。 这一批评挑战了当前 AI 安全话语及其财务激励，可能重塑投资者和公众对 AI 风险警告的看法。 Hotz 指出，机构投资者通常不理会大规模失业的担忧，表明末日叙事更多是营销或招聘工具，而非真正的估值驱动因素。

hackernews · inatreecrown2 · 6月22日 00:45 · [社区讨论](https://news.ycombinator.com/item?id=48624195)

**背景**: Dario Amodei 和 Sam Altman 等人发出的 AI 安全警告曾被用于倡导监管和吸引投资。Hotz 的文章质疑这些警告的诚意，将其与以往科技泡沫中的炒作周期联系起来。

**社区讨论**: 评论意见不一：一些人同意末日叙事受投资需求激励，而另一些人则认为对 AGI 风险的真正担忧独立于估值存在。少数人注意到文中引用了‘内卷’和‘摆烂’等中文文化术语。

**标签**: `#AI safety`, `#venture capital`, `#hype cycles`, `#technology criticism`, `#George Hotz`

---

<a id="item-6"></a>
## [Google IPv6 流量突破 50% 里程碑](https://blog.apnic.net/2026/04/28/google-hits-50-ipv6/) ⭐️ 8.0/10

Google 的 IPv6 流量已达到其总流量的 50%，标志着全球从 IPv4 向 IPv6 过渡的一个重要里程碑。 这一里程碑表明 IPv6 的采用取得了重大进展，这对于克服 IPv4 地址枯竭并确保互联网的持续发展至关重要。 50% 的数据基于 Google 的全球流量测量，但不同地区和 ISP 的采用率差异很大，许多提供商在部署方面仍然滞后。

hackernews · barqawiz · 6月21日 08:21 · [社区讨论](https://news.ycombinator.com/item?id=48616800)

**背景**: IPv6 是下一代互联网协议，旨在取代地址空间仅约 43 亿的 IPv4。由于需要 ISP 升级、硬件兼容性以及通过 NAT 继续使用 IPv4，这一过渡进展缓慢。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digicert.com/blog/the-state-of-ipv6-adoption-in-2025-progress-pitfalls-and-pathways-forward">digicert.com/blog/the-state-of- ipv 6 - adoption -in-2025-progress-pitfalls...</a></li>
<li><a href="https://en.wikipedia.org/wiki/IPv6_deployment">IPv6 deployment - Wikipedia</a></li>
<li><a href="https://tools.forwardingplane.net/guides/isp-enable/">Enabling IPv6 on US Consumer ISPs - IPv6 is the current ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了 ISP 采用方面的持续差距，用户指出 Virgin Media（英国）和 Odido（荷兰）等主要 ISP 仍不支持 IPv6。还有人指出 GitHub 等平台不支持 IPv6，需要 NAT64 等变通方案。

**标签**: `#IPv6`, `#networking`, `#internet infrastructure`, `#adoption`

---

<a id="item-7"></a>
## [三星向员工部署 ChatGPT Enterprise 和 Codex](https://openai.com/index/samsung-electronics-chatgpt-codex-deployment) ⭐️ 8.0/10

三星电子正在向全球员工部署 ChatGPT Enterprise 和 Codex，这标志着 OpenAI 最大规模的企业 AI 部署之一。 此次部署标志着生成式 AI 在企业中的重大采用，可能提升全球科技领导者的生产力和创新力，并验证了 OpenAI 的企业产品。 ChatGPT Enterprise 提供增强的安全性、隐私和集成能力，而 Codex 是一个 AI 编码助手。此次部署覆盖全球员工，表明是大规模实施。

rss · OpenAI Blog · 6月21日 23:00

**背景**: ChatGPT Enterprise 是 OpenAI 面向企业的 ChatGPT 版本，专为组织使用设计，具有无使用上限、更快性能和 32k 上下文长度等特点。Codex 是一个将自然语言翻译成代码的 AI 系统，帮助开发者。三星的采用反映了大型企业整合 AI 工具以增强运营的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-enterprise/">Introducing ChatGPT Enterprise | OpenAI</a></li>
<li><a href="https://grokipedia.com/page/ChatGPT_Enterprise">ChatGPT Enterprise</a></li>

</ul>
</details>

**标签**: `#AI`, `#Enterprise`, `#OpenAI`, `#Samsung`, `#ChatGPT`

---

<a id="item-8"></a>
## [本地 LLM 推理优化完全指南](https://www.reddit.com/r/LocalLLaMA/comments/1uc3wg9/local_llm_inference_optimization_the_complete/) ⭐️ 8.0/10

一份基于一年实验的本地 LLM 推理优化综合指南已发布，涵盖 VRAM 适配、KV 缓存调优、MoE 放置、MTP、CPU 调优及常见 OOM 陷阱，全部基于 llama.cpp。 该指南为本地 LLM 社区解决了常见痛点，提供了可操作的实用优化技巧，帮助用户在有限硬件上运行更大模型，从而推动强大 AI 的普及。 该指南基于一年的动手实验，涵盖 KV 缓存量化、混合专家模型的专家卸载以及避免内存溢出的 CPU 卸载策略等具体技术。

reddit · r/LocalLLaMA · /u/carteakey · 6月21日 23:01

**背景**: llama.cpp 是一个开源的 C/C++ LLM 推理库，已成为 Ollama 和 LM Studio 等本地推理工具的事实标准。KV 缓存是高效推理的关键技术，通过存储中间键值对避免重复计算。混合专家（MoE）是一种架构，使用多个子模型（专家）来增加模型容量，同时保持计算成本可控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms">Understanding and Coding the KV Cache in LLMs from Scratch</a></li>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts (MoE) Mixture of Experts in Large Language Models - arXiv.org How Mixture-of-Experts LLMs Work - Medium Mixture of Experts Explained - Hugging Face Applying Mixture of Experts in LLM Architectures | NVIDIA ... [2507.11181] Mixture of Experts in Large Language Models Mixture of Experts (MoE) | Sebastian Raschka, PhD</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区称赞该指南价值高且技术深入，用户分享了额外技巧和修正。部分用户讨论了使用 MoE 模型和 VRAM 优化的具体经验。

**标签**: `#llama.cpp`, `#LLM inference`, `#optimization`, `#local LLM`, `#VRAM`

---

<a id="item-9"></a>
## [Qwen 在关键人物离职后转向闭源](https://www.reddit.com/r/LocalLLaMA/comments/1ubjnh5/qwen_is_never_going_to_open_source_qwen_37_arent/) ⭐️ 8.0/10

阿里巴巴旗下的 AI 实验室 Qwen 在解雇了团队负责人林俊阳后，停止了其大型模型的开源发布，成为近期最后一个发布开源模型的中国主要 AI 实验室。 这标志着开源 AI 领域的重大转变，因为 Qwen 模型被广泛用于微调和本地部署；此举可能会减少高质量开源模型的可用性，并影响全球 AI 社区。 Qwen 3.7-Max 和 Qwen 3.7-Plus 仍完全闭源，且有传言称小模型团队已解散；其他中国实验室如 GLM、Kimi、MiniMax、Step、MiMo、DeepSeek 和 AKA 近期都发布了比 Qwen 更新的开源模型。

reddit · r/LocalLLaMA · /u/DistanceSolar1449 · 6月21日 07:25

**背景**: Qwen 曾是领先的中国 AI 实验室之一，以发布开源大语言模型而闻名，这些模型在微调和本地推理中广受欢迎。前 Qwen 团队负责人林俊阳是这些发布背后的关键人物。他的离职导致了战略转变，阿里巴巴现在专注于专有模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aibase.com/news/25894">Head of Alibaba Tongyi Qianwen, Lin Junyang , Announces...</a></li>
<li><a href="https://aiproductivity.ai/news/chinese-labs-delaying-open-source-model-releases/">Chinese AI Labs Are All Withholding Open - Source Models at the...</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区表达了失望和担忧，许多人指出 Qwen 转向闭源对社区来说是一种损失。一些用户指出其他中国实验室仍在发布开源模型，而另一些用户则猜测阿里巴巴内部存在动荡。

**标签**: `#open source`, `#Qwen`, `#AI models`, `#Chinese AI labs`, `#community discussion`

---

<a id="item-10"></a>
## [爱好者仅花 800 美元训练 500M 参数 LLM 和 330M 图像生成器](https://www.reddit.com/r/LocalLLaMA/comments/1ubuy8w/i_pretrained_and_post_trained_a_500m_parameter/) ⭐️ 8.0/10

一位爱好者使用 Modal 平台的 8 块 H200 GPU，从零开始预训练和后期训练了一个 500M 参数的 LLM 和一个 330M 参数的图像生成器，仅花费 800 美元，并发布了模型权重、演示平台以及训练/推理代码。 这表明从零开始预训练大型模型正变得对个人而非仅大型组织可行，可能加速开源 AI 发展并推动模型创建的民主化。 该 LLM 使用了 FineWeb 数据集的 400 亿 token 进行训练，图像生成器采用了 SIGLIP 编码器和受字节跳动 DreamLite 启发的架构。800 美元的总成本涵盖了所有计算和数据费用。

reddit · r/LocalLLaMA · /u/Altruistic-Tea-5612 · 6月21日 16:52

**背景**: 预训练大型语言模型和图像生成器通常需要巨大的计算资源和预算，往往花费数百万美元。FineWeb 是一个高质量的开源 LLM 预训练数据集，SIGLIP 是一种高效的视觉-语言编码器，DreamLite 是一种轻量级的设备端图像生成架构。该项目表明，借助高效架构和现代云 GPU，成本可以大幅降低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1">FineWeb: decanting the web for the finest text data at scale ...</a></li>
<li><a href="https://arxiv.org/abs/2502.14786">[2502.14786] SigLIP 2: Multilingual Vision-Language Encoders ... SigLIP · Hugging Face SigLIP 2: Multilingual Vision-Language Encoders with Improved ... Understanding SIGLIP, the more efficient vision encoder SigLIP | google-research/big_vision | DeepWiki SigLIP 2: Multilingual Vision-Language Encoders with Improved ...</a></li>
<li><a href="https://github.com/ByteVisionLab/DreamLite">DreamLite: A Lightweight On-Device Unified Model for Image Generation ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#pretraining`, `#image generation`, `#open-source`, `#hobby project`

---

<a id="item-11"></a>
## [本地视觉模型最佳选择：第二次基准测试更新](https://www.reddit.com/r/LocalLLaMA/comments/1ubx4rw/best_local_model_for_vision_2nd_benchmark_update/) ⭐️ 8.0/10

作者发布了本地视觉语言模型的第二次基准测试更新，将数据集从 20 张扩展到 30 张图片，从 Ollama 切换到 llama.cpp，并测试了 23 个模型，总共进行了 2070 次测试。关键发现包括思考模式会损害视觉性能，以及 MoE 模型的表现不如同等大小的密集模型。 该基准测试为本地运行视觉模型提供了实用的、按硬件层级划分的建议，帮助用户根据自己的 VRAM 预算选择最佳模型。这些发现挑战了关于视觉任务中思考模式和 MoE 架构的常见假设。 针对 4-8 GB VRAM 的最佳推荐是 Qwen3.5 4B（非思考模式）Q4 量化，得分 75.5/100；12-16 GB 推荐 Qwen3-VL 8B Q8 量化，得分 74.4/100；24+ GB 推荐 Qwen3.6 27B（非思考模式）Q4 量化，得分 79.6/100。基准测试还发现 Q8 量化并非总是有益的，在混合思考模型中可能导致超时。

reddit · r/LocalLLaMA · /u/ex-arman68 · 6月21日 18:18

**背景**: 视觉语言模型（VLM）同时处理图像和文本，但在本地运行需要仔细平衡模型大小、量化和推理设置。量化通过牺牲一定精度来减小模型大小并加快推理速度，Q4 和 Q8 是常见的量化级别。llama.cpp 库允许对图像 token 预算和批处理大小进行精细控制，这显著影响性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/google/gemma-4-12B">google/ gemma - 4 -12B · Hugging Face</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/17172">Proper handling of large images (4k) with llama-server ...</a></li>
<li><a href="https://medium.com/@paul.ilvez/demystifying-llm-quantization-suffixes-what-q4-k-m-q8-0-and-q6-k-really-mean-0ec2770f17d3">Demystifying LLM Quantization Suffixes: What Q4_K_M, Q8_0 ...</a></li>

</ul>
</details>

**标签**: `#local-llm`, `#vision-language-model`, `#benchmark`, `#llama.cpp`, `#open-source-ai`

---

<a id="item-12"></a>
## [Gemma 4 QAT 模型对 KV 缓存量化表现出鲁棒性](https://www.reddit.com/r/LocalLLaMA/comments/1ubl0df/gemma_4_qat_seems_to_respond_significantly_better/) ⭐️ 8.0/10

一位 Reddit 用户报告称，基于 Wikitext 上 16k 上下文的测试，Gemma 4 QAT（量化感知训练）模型在 KV 缓存量化下的 KL 散度显著低于非 QAT 模型。QAT 模型上的 Q8_0 量化显示出 99.9% 的 KL 散度指标，表明性能退化极小。 这一发现表明，QAT 可以使大型语言模型对 KV 缓存量化更加鲁棒，而 KV 缓存量化是减少内存和加速推理的关键优化。它可能使 Gemma 4 模型在消费级硬件上更广泛地部署，而不会牺牲质量。 用户测量了完整 16 位 KV 缓存与量化版本之间的 KL 散度，99.9% 的 KLD 表明注意力行为几乎相同。由于硬件限制，测试仅限于较小的 Gemma 4 模型，31B 模型尚未测试。

reddit · r/LocalLLaMA · /u/rima_2711 · 6月21日 08:48

**背景**: KV 缓存量化通过以较低精度（例如 8 位而非 16 位）存储键值状态来减少 LLM 推理期间的内存使用。量化感知训练（QAT）在训练过程中纳入量化效应，使模型对训练后量化更具弹性。KL 散度衡量输出分布之间的差异，较低的值表示模型行为保留得更好。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/quantization-aware-training">What is quantization aware training? - IBM</a></li>
<li><a href="https://huggingface.co/blog/kv-cache-quantization">Unlocking Longer Generation with Key-Value Cache Quantization</a></li>

</ul>
</details>

**社区讨论**: 该帖子获得了积极反响，用户表示有兴趣在更大模型上复现结果。一些人指出 99.9% 的 KLD 指标很有希望，但提醒实际性能可能有所不同。

**标签**: `#LLM`, `#quantization`, `#KV cache`, `#Gemma`, `#inference optimization`

---

<a id="item-13"></a>
## [PermaVid：通过解耦上下文内存实现一致视频生成](https://www.reddit.com/r/StableDiffusion/comments/1uc928a/permavid_consistent_video_generation_across_edits/) ⭐️ 8.0/10

PermaVid 提出了一种解耦上下文内存方法，可在视频编辑过程中保持一致性，并发布了 400GB 训练数据集以及 GitHub 上的开源代码。 这项工作解决了视频生成中的一个关键挑战——编辑后保持时间和空间一致性——这对于视频编辑和内容创作等实际应用至关重要。大型开源数据集和代码降低了研究人员和开发者推进该领域的门槛。 该方法使用并行视觉记忆分支和解耦的 RGB-深度上下文，将视觉检索与文本引起的稀释分离，从而在长视频序列中实现持久记忆。该数据集托管在 Hugging Face 上，包含 400GB 的训练数据。

reddit · r/StableDiffusion · /u/Sporeboss · 6月22日 03:04

**背景**: 视频生成模型在应用编辑时常常难以保持一致性，因为更改可能导致时间闪烁或上下文丢失。解耦表示学习将不同的变化因素（例如姿态与外观）分离，以提高可控性和稳定性。PermaVid 在此基础上引入了一个专门用于视频编辑任务的记忆机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.16449">[2606.16449] PermaVid: Consistent Video Generation Across Edits...</a></li>
<li><a href="https://www.emergentmind.com/topics/permavid">PermaVid: Persistent Visual Memory</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对 PermaVid 反响积极，用户称赞其开源发布和大型数据集。一些技术讨论集中在记忆机制的效率及其在长视频生成中的潜在应用。

**标签**: `#video generation`, `#AI/ML`, `#open-source`, `#dataset`, `#Stable Diffusion`

---

<a id="item-14"></a>
## [发布 GPT-2 中等规模的免 Softmax 注意力模型](https://www.reddit.com/r/MachineLearning/comments/1ubmybr/i_released_a_softmaxfree_attention_model_at_gpt2/) ⭐️ 8.0/10

一个 GPT-2 中等规模（约 3.54 亿参数，在 115 亿 tokens 上训练）的免 Softmax 注意力模型已发布，带有开放权重和自定义 Triton 内核，通过结构稀疏性和 tile-skipping 实现长上下文 VRAM 节省。 这项工作展示了标准 softmax 注意力的实用替代方案，可能使有限硬件上支持更长的上下文长度，并减少 Transformer 推理中的内存瓶颈。 该模型使用结构稀疏性和 tile-skipping 内核跳过零块的计算，减少长序列的 VRAM 使用。自定义 Triton 内核与模型权重一起开源。

reddit · r/MachineLearning · /u/NonGameCatharsis · 6月21日 10:46

**背景**: 标准注意力机制使用 softmax 操作来归一化注意力分数，对于长序列来说计算成本高且内存密集。免 Softmax 注意力用更简单的归一化（如 L1 范数）替代 softmax，降低复杂度。结构稀疏性和 tile-skipping 通过跳过无关计算进一步优化注意力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2206.08898">[2206.08898] SimA: Simple Softmax-free Attention for Vision ...</a></li>
<li><a href="https://modernorange.io/item/48617387">Softmax-free ~354M: tile - skip kernels for... | Modern Orange</a></li>
<li><a href="https://news.ycombinator.com/item?id=48617387">Softmax-free ~354M: tile - skip kernels for long-context... | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 社区讨论包括关于免 Softmax 方法和 tile-skipping 实现的技术问题，作者积极参与并提供澄清。总体情绪积极，对开源发布和潜在应用感兴趣。

**标签**: `#attention`, `#efficiency`, `#open-source`, `#Triton`, `#long-context`

---

<a id="item-15"></a>
## [AI 生成书籍和音乐激增，数量超过人类作品](https://www.reddit.com/r/artificial/comments/1ubnaqo/the_surge_of_slopsince_the_release_of_chatgpt35/) ⭐️ 8.0/10

自 2022 年底 ChatGPT-3.5 发布以来，到 2025 年底亚马逊电子书数量翻了三倍，完全由 AI 生成内容驱动。Deezer 报告每天上传 7.5 万首 AI 歌曲，占新曲目的 44%，97%的用户无法区分 AI 与人类音乐。 这一激增标志着内容创作的根本性转变，AI 生成作品现在主导平台，引发对真实性、质量以及对人类创作者经济影响的担忧。这些发现凸显了开发检测工具和制定政策以管理 AI 生成内容的紧迫性。 《经济学人》的分析显示，亚马逊电子书数量翻三倍完全归因于 AI 生成的书籍。Deezer 的检测工具发现，高达 85%的 AI 音乐流媒体存在欺诈行为，导致此类曲目被取消变现资格。

reddit · r/artificial · /u/StarlightDown · 6月21日 11:06

**背景**: 2022 年底发布的 ChatGPT-3.5 使先进的 AI 文本生成技术广泛可用，从而轻松创作书籍和音乐。此后，亚马逊和 Deezer 等平台见证了 AI 生成内容的爆炸式增长，这些内容通常与人类作品难以区分。Deezer 开发了一款 AI 音乐检测器来帮助识别此类内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.w3schools.com/gen_ai/chatgpt-3-5/index.php">ChatGPT - 3 . 5 Tutorial</a></li>
<li><a href="https://www.deezer.com/explore/en-us/ai-music-detector/">Free AI Music Detector by Deezer | AI Song checker</a></li>
<li><a href="https://newsroom-deezer.com/2026/01/ai-generated-music-deezer-selling-detection-tool/">How to Detect AI Music: Deezer Sells Its Detection Tool</a></li>

</ul>
</details>

**社区讨论**: Reddit 评论反应不一：一些用户对 AI 内容的主导地位及其可能贬低人类创造力感到担忧，而另一些人则认为 AI 工具可以增强人类生产力。少数评论者指出，AI 生成的书籍质量通常较差，但数量压倒了人工策展。

**标签**: `#AI-generated content`, `#publishing`, `#music`, `#content authenticity`, `#industry disruption`

---