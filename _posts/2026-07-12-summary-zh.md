---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> 从 122 条内容中筛选出 15 条重要资讯。

---

1. [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](#item-1) ⭐️ 9.0/10
2. [AI 周报：GPT-5.6、Grok 4.5、Gemini 延期、Copilot 数据](#item-2) ⭐️ 9.0/10
3. [Vidu S1：实时交互式视频生成模型](#item-3) ⭐️ 8.0/10
4. [SciReasoner：跨学科可解释结构推理模型](#item-4) ⭐️ 8.0/10
5. [四块 RTX 5060 Ti 跑 Qwen3.6-27B 代码生成测试](#item-5) ⭐️ 8.0/10
6. [RTX 5090 对比 6000 PRO：分流改装与水冷基准测试](#item-6) ⭐️ 8.0/10
7. [llama.cpp 上 GGUF 模型的雅可比透镜工具](#item-7) ⭐️ 8.0/10
8. [直接人脸相似度损失提升角色 LoRA 训练](#item-8) ⭐️ 8.0/10
9. [VultronRetriever 模型登顶 MTEB，可在 iPhone 上离线运行](#item-9) ⭐️ 8.0/10
10. [苹果起诉 OpenAI 窃取商业机密](#item-10) ⭐️ 8.0/10
11. [OpenAI 安全负责人离职](#item-11) ⭐️ 8.0/10
12. [Superpowers：GitHub 上趋势的智能体技能框架](#item-12) ⭐️ 8.0/10
13. [OpenManus AI 智能体框架在 GitHub 上迅速走红](#item-13) ⭐️ 8.0/10
14. [OpenAI 发布 Codex CLI：基于 Rust 的轻量级编码代理](#item-14) ⭐️ 8.0/10
15. [Hugging Face 推出用于本地语音代理的语音转语音仓库](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 将 Model Runner V2 设为所有稠密模型的默认执行路径，移除了传统的 PagedAttention 实现，并使 Transformers 建模后端的速度与原生 vLLM 持平。该版本还新增了 LLaVA-OneVision-2、GLM-5 等模型，引入了 Streaming Parser Engine，并支持异构词表的通用推测解码。 此版本标志着 vLLM 的重大架构转变，通过将 Model Runner V2 设为标准并移除 PagedAttention，简化了代码库并提升了性能。Transformers 后端的速度持平降低了用户使用 vLLM 高效运行 Hugging Face 模型的门槛，而新模型和推测解码功能则扩展了 vLLM 在生产级 LLM 服务中的适用性。 Model Runner V2 现在支持 EVS、实时嵌入、Mamba 混合模型的前缀缓存，以及带完整 CUDA 图的动态推测解码。Transformers 后端获得了 FP8 MoE 支持，并迁移了 GPTBigCode/Starcoder2 和 RoBERTa。PagedAttention 被完全删除，因为 V1/MRv2 后端已成为标准路径。

github · khluu · 7月11日 20:06

**背景**: vLLM 是一个高性能的开源 LLM 推理和服务库，以其高效管理 KV 缓存内存的 PagedAttention 算法而闻名。Model Runner V2 是一个更新的执行引擎，旨在提升性能和灵活性。Transformers 后端允许 vLLM 原生运行 Hugging Face Transformers 模型，无需专门的 vLLM 模型实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm -project/ vllm</a></li>
<li><a href="https://en.wikipedia.org/wiki/PagedAttention">PagedAttention - Wikipedia</a></li>
<li><a href="https://vllm.ai/blog/2025-04-11-transformers-backend">Transformers modeling backend integration in vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#open source`, `#release`, `#AI infrastructure`

---

<a id="item-2"></a>
## [AI 周报：GPT-5.6、Grok 4.5、Gemini 延期、Copilot 数据](https://www.reddit.com/r/artificial/comments/1utc0he/weekly_recap_gpt56_public_launch_grok_45_gemini/) ⭐️ 9.0/10

OpenAI 于 7 月 9 日公开发布 GPT-5.6 系列（Sol、Terra、Luna），以及全双工语音模型 GPT-Live-1 和 gpt-realtime-2.1。xAI 发布了与 Cursor 联合训练的 Grok 4.5，谷歌将 Gemini 3.5 Pro 推迟至 7 月 17 日，微软披露 M365 付费 Copilot 转化率不足 4.5%。 本周多个前沿模型同步降价，使接近前沿的推理在经济上更适用于更多自动化场景。微软的低转化率表明横向 AI 助手面临采用挑战，而 DeepSeek API 的退役凸显了模型抽象层的必要性。 GPT-5.6 Sol 在 Artificial Analysis Coding Agent Index 上以 80 分达到最先进编码性能，超越 Fable 5 且使用更少 token。Grok 4.5 定价为每百万输入 token 2 美元、输出 token 6 美元，声称在编码、法律和金融任务上达到 Opus 级别性能，但独立评估尚未出炉。

reddit · r/artificial · /u/ksraj1001 · 7月11日 06:10

**背景**: GPT-5.6 系列包含三个层级：Luna（最小、最便宜）、Terra（中端，以更低成本达到此前旗舰性能）和 Sol（最大，前沿推理）。全双工语音模型如 GPT-Live-1 可以同时听和说，实现更自然的对话。微软 Copilot 是集成在 Microsoft 365 中的 AI 助手，但 4.5%的转化率表明其 4.5 亿 M365 用户中付费采用有限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-6/">GPT‑5.6: Frontier intelligence that scales with your ambition</a></li>
<li><a href="https://cursor.com/grok-4-5">Cursor · Grok 4 . 5</a></li>
<li><a href="https://help.openai.com/en/articles/20001325-a-preview-of-gpt-56-sol-terra-and-luna">GPT-5.6 in ChatGPT - OpenAI Help Center</a></li>

</ul>
</details>

**社区讨论**: 社区讨论强调，多家供应商同时降价比任何单一基准更具影响力，微软 4.5%的转化率表明需求在于特定任务自动化而非横向助手。同时提醒由于 DeepSeek API 退役，应抽象模型层。

**标签**: `#AI`, `#GPT-5.6`, `#Grok`, `#Gemini`, `#Microsoft Copilot`

---

<a id="item-3"></a>
## [Vidu S1：实时交互式视频生成模型](https://huggingface.co/papers/2607.03118) ⭐️ 8.0/10

Vidu S1 是一款实时交互式视频生成模型，支持通过语音指令控制数字角色动画，可在消费级 GPU 上实现无限长度输出和高帧率。 这一突破使得实时交互式视频生成在消费级硬件上成为可能，为实时内容创作、虚拟化身和互动娱乐开辟了新可能，无需昂贵的云基础设施。 Vidu S1 在普通消费级 GPU 上可输出高达 42 FPS 的 540p 视频，采用 TurboDiffusion 加速和 TurboServe 高效服务。用户可上传真人、动漫或宠物的自定义图像，并选择不同的语音语调。

huggingface_papers · Hugging Face Papers · 7月10日 00:00

**背景**: 传统视频生成模型速度慢且需要高端硬件，限制了实时交互性。TurboDiffusion 是一个加速框架，可将扩散模型速度提升 100-200 倍，而 TurboServe 优化了服务基础设施。Vidu S1 结合两者，在消费级 GPU 上实现了实时性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/thu-ml/TurboDiffusion">GitHub - thu-ml/TurboDiffusion: TurboDiffusion: 100–200× ...</a></li>

</ul>
</details>

**标签**: `#video generation`, `#real-time`, `#voice control`, `#diffusion models`, `#AI`

---

<a id="item-4"></a>
## [SciReasoner：跨学科可解释结构推理模型](https://huggingface.co/papers/2607.07708) ⭐️ 8.0/10

研究人员推出了 SciReasoner，这是一个多模态科学基础模型，它将蛋白质、分子和晶体的结构元素离散化为统一词汇表，实现可解释推理。该模型在 86 项基准测试中的 67 项上达到最先进性能，包括将基因本体预测的 F_max 从 0.42 提升至 0.55，以及单步逆合成准确率从 0.63 提升至 0.72。 SciReasoner 解决了 AI for Science 中的一个关键挑战，将准确预测与可解释推理相结合，使结构证据在科学约束下可被检查。这有望通过提供结构-性质关系的透明洞察，加速生物学、化学和材料科学领域的发现。 该模型使用统一的结构感知词汇表对坐标、拓扑和周期性连接进行分词，将标记视为可寻址的证据单元。在双盲专家评估中，其推理轨迹在 98%的案例中被认为优于或相当于前沿大语言模型。

huggingface_papers · Hugging Face Papers · 7月9日 00:00

**背景**: 结构-性质关系是生物学、化学和材料科学的基础，功能源于空间和化学组织。传统 AI 模型往往缺乏可解释性，难以理解预测如何从结构证据中得出。SciReasoner 将结构元素离散化为词汇表，使模型能够在保留领域原生信息的同时进行逐步推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2509.21320">[2509.21320] SciReasoner: Laying the Scientific Reasoning ...</a></li>
<li><a href="https://github.com/OpenDCAI/SciReasoner">GitHub - OpenDCAI/SciReasoner</a></li>

</ul>
</details>

**标签**: `#AI for Science`, `#Multimodal Learning`, `#Structural Biology`, `#Materials Science`, `#Interpretability`

---

<a id="item-5"></a>
## [四块 RTX 5060 Ti 跑 Qwen3.6-27B 代码生成测试](https://www.reddit.com/r/LocalLLaMA/comments/1uturng/i_benched_quad_5060tis_for_code_generation_with/) ⭐️ 8.0/10

一位 Reddit 用户对四块 RTX 5060 Ti 组成的系统运行 Qwen3.6-27B 进行代码生成进行了基准测试，在总构建成本约 3000 美元的情况下实现了强劲性能。 这表明一个相对廉价的多 GPU 配置能够以全精度和大上下文运行最先进的 270 亿参数模型，使预算有限的开发者也能获得高质量的本地代码生成能力。 该配置使用四块 RTX 5060 Ti 16GB 显卡，搭配支持 PCIe 分叉的 X570 或 X870E 主板，每块卡实现 16GB/s 双向带宽。该设置以 Q8_0 量化、FP16 KV 缓存并启用 MTP 运行 Qwen3.6-27B，目标支持 256K 上下文。

reddit · r/LocalLLaMA · /u/starkruzr · 7月11日 20:28

**背景**: 本地运行大语言模型需要大量 GPU 显存。Qwen3.6-27B 是一个 270 亿参数的密集模型，针对智能体编码和多模态推理进行了优化，原生支持 256K 上下文。像这样的多 GPU 配置可以运行比单块消费级显卡所能处理的更大模型或更高精度量化版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qwen.ai/blog?id=qwen3.6-27b">Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model</a></li>
<li><a href="https://recipes.vllm.ai/Qwen/Qwen3.6-27B">Qwen/Qwen3.6-27B | vLLM Recipes</a></li>
<li><a href="https://www.kunalganglani.com/blog/running-local-llms-2026-hardware-setup-guide">Local LLM Hardware Guide 2026: VRAM, GPUs, Setup [Tested]</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论称赞了详细的基准测试和成本效益，一些用户质疑四块 5060 Ti 配置的长期可行性，因为可能存在驱动和扩展问题。其他人分享了替代配置，如双 3090 或使用二手服务器 GPU。

**标签**: `#GPU benchmarking`, `#code generation`, `#Qwen3.6-27B`, `#local LLM`, `#hardware`

---

<a id="item-6"></a>
## [RTX 5090 对比 6000 PRO：分流改装与水冷基准测试](https://www.reddit.com/r/LocalLLaMA/comments/1utvbey/performance_comparison_on_full_compute/) ⭐️ 8.0/10

一位 Reddit 用户对 RTX 6000 PRO MaxQ 进行了分流改装和水冷改造，使其功耗达到 600W，然后将其计算和 LLM 提示处理性能与 RTX 5090 和未改装的 RTX 6000 PRO WS 在不同功耗限制下进行了对比。 这次实际对比提供了罕见且真实的数据，展示了分流改装和水冷如何解锁专业 GPU 的额外性能，对于寻求高性价比高性能推理硬件的 AI 研究人员和爱好者来说非常有价值。 分流改装涉及焊接一个 0.002 欧姆电阻，使 GPU 误以为功耗减半从而拉高至 600W，水冷使满载温度保持在 60°C。改装后的 MaxQ 在 600W 下比 RTX 5090 在 600W 下快 12.8%（Anima 计算时间）。

reddit · r/LocalLLaMA · /u/panchovix · 7月11日 20:49

**背景**: 分流改装是一种硬件修改，通过改变功率测量电路上的电阻，使 GPU 超过其默认功耗限制。水冷用于散发额外热量。Anima 基准测试用于评估完整计算性能，而 LLM 提示处理则测试大语言模型的推理速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reddit.com/r/overclocking/comments/x877ov/how_exactly_does_a_shunt_mod_and_gpucpu_current/">How exactly does a shunt mod and gpu/cpu current ... - Reddit</a></li>
<li><a href="https://www.pcworld.com/article/2854038/this-nvidia-rtx-laptop-mod-unlocks-amazing-performance-dont-do-it.html">This Nvidia RTX laptop mod unlocks amazing ... - PCWorld</a></li>
<li><a href="https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-max-q/">RTX PRO 6000 Blackwell Max - Q Workstation Edition | NVIDIA</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论称赞了详细的测试方法和结果，一些用户质疑分流改装在日常使用中的实用性，因为存在损坏显卡的风险。其他人指出，更高功耗带来的性能提升逐渐递减，暗示降压可能更高效。

**标签**: `#GPU benchmarking`, `#LLM inference`, `#hardware modding`, `#performance analysis`, `#NVIDIA`

---

<a id="item-7"></a>
## [llama.cpp 上 GGUF 模型的雅可比透镜工具](https://www.reddit.com/r/LocalLLaMA/comments/1uu32z6/interactive_jacobianlens_visualizer_and_live/) ⭐️ 8.0/10

一款名为 jlens-gguf 的新开源工具首次将 Anthropic 的雅可比透镜技术引入运行在 llama.cpp 上的 GGUF 模型，实现了模型内部状态的可视化和实时操控。 该工具填补了重要空白，使机械可解释性在广泛使用的 llama.cpp 推理引擎上变得可用，让研究人员和爱好者无需依赖 PyTorch 或 Hugging Face 基础设施即可在本地探查和操控大语言模型。 该工具包含一个基于 llama.cpp 的原生 GGUF 服务器，支持观察和操控，同时也能观察正在运行的 llama-server 模型（但无法操控）。透镜的内存开销约为模型大小的 1/8，例如 160GB 的模型需要额外 20GB 内存。

reddit · r/LocalLLaMA · /u/Responsible_Fig_1271 · 7月12日 02:37

**背景**: 雅可比透镜是一种机械可解释性技术，通过将残差流向量线性传输到最终层并解码为词汇标记，来读出内部激活倾向于让模型说什么。GGUF 是 llama.cpp 团队设计的模型格式，用于高效的本地推理；llama.cpp 是一个高性能 C/C++推理引擎，广泛用于在消费级硬件上运行大语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/anthropics/jacobian-lens">GitHub - anthropics/jacobian-lens: Companion code for the ...</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/ llama . cpp : LLM inference in C/C++ · GitHub</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的社区讨论内容充实，用户就内存需求、与 MoE 模型的兼容性以及模型操控的潜在应用提出了技术问题。作者积极回应，澄清细节并参与反馈。

**标签**: `#llama.cpp`, `#GGUF`, `#Jacobian lens`, `#mechanistic interpretability`, `#open-source`

---

<a id="item-8"></a>
## [直接人脸相似度损失提升角色 LoRA 训练](https://www.reddit.com/r/StableDiffusion/comments/1utkvsk/direct_face_similarity_optimization_for_fast/) ⭐️ 8.0/10

一种新的 Stable Diffusion 角色 LoRA 训练方法，通过可微分的人脸嵌入损失直接优化人脸相似度，在 RTX 4090 上仅需 10-12 分钟即可获得比普通 SFT 更好的效果。 该方法大幅缩短训练时间并提升面部一致性，使角色 LoRA 的创建对艺术家和开发者更加便捷高效。 该方法对原始权重使用 INT8，对 LoRA 使用 bf16 加 fp32 主权重，训练时 batch size 为 1，采样步数为 12；每步耗时 4.11 秒，包括图像生成、VAE 解码、人脸检测、损失计算和反向传播。

reddit · r/StableDiffusion · /u/Ok-Constant8386 · 7月11日 13:59

**背景**: LoRA（低秩适应）是一种通过添加小型可训练矩阵来微调大模型的技术，常用于 Stable Diffusion 学习新概念（如角色）。普通 SFT（监督微调）训练模型预测噪声或速度，对于面部一致性可能较慢且效果不佳。人脸相似度损失直接度量人脸嵌入之间的距离，从而实现更有针对性的优化。

**标签**: `#LoRA`, `#face similarity`, `#diffusion models`, `#reinforcement learning`, `#Stable Diffusion`

---

<a id="item-9"></a>
## [VultronRetriever 模型登顶 MTEB，可在 iPhone 上离线运行](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

Vultr 发布了 VultronRetriever 系列嵌入模型，包括 Prime-8B、Core-4.5B 和 Flash-0.8B，它们在 MTEB 排行榜上各自类别中排名第一。这些模型在 iPhone 上完全离线运行问答和文档嵌入的功能已得到演示。 与之前的 9B 类领先模型相比，这些模型实现了高达 16 倍的索引存储缩减和 12 倍的吞吐量提升，从而在边缘设备上实现高性能检索。这可能推动高级检索增强生成（RAG）和端侧 AI 应用的普及。 这些模型采用 Hydra 架构，通过单个视觉语言模型提供后期交互检索和生成功能，内存占用最多减少一半。Flash-0.8B 模型可完全离线每分钟索引多达 60 张图像，性能超越其 5 倍大小的模型。

reddit · r/MachineLearning · /u/madkimchi · 7月11日 15:22

**背景**: MTEB（大规模文本嵌入基准）是广泛用于评估嵌入模型在检索、分类和聚类等任务上表现的排行榜。由 ColBERT 开创的后期交互检索允许查询与文档之间进行细粒度的 token 级匹配，从而提高精度。Hydra 架构将检索和生成统一到一个模型中，降低了系统复杂度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>
<li><a href="https://arxiv.org/abs/2603.28554">[2603.28554] Hydra: Unifying Document Retrieval and ...</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models: ColBERT ...</a></li>

</ul>
</details>

**标签**: `#retrieval`, `#MTEB`, `#edge AI`, `#embedding`, `#NLP`

---

<a id="item-10"></a>
## [苹果起诉 OpenAI 窃取商业机密](https://www.reddit.com/r/artificial/comments/1utkdha/apple_just_sued_openai_and_the_details_are_wild/) ⭐️ 8.0/10

苹果已对 OpenAI 提起诉讼，指控其前高管和工程师窃取了包括硬件设计和专有制造技术在内的商业机密，并招募了超过 400 名苹果员工。 这起诉讼加剧了两大科技公司之间的紧张关系，可能重塑 AI 硬件领域的竞争格局，因为苹果试图保护其知识产权和供应链关系。 苹果指控前硬件主管 Tang Tan 指导员工在面试时携带实际硬件部件，工程师 Chang Liu 在保留苹果云存储访问权限后下载了机密文件。OpenAI 还被指控未经许可使用了苹果的专有金属精加工技术。

reddit · r/artificial · /u/Direct-Attention8597 · 7月11日 13:37

**背景**: 系统级封装（SiP）是一种将多个组件集成到单个封装中的技术，常用于苹果设备。苹果的离职流程通常涉及保护公司数据和设备。该诉讼凸显了 AI 硬件开发中的竞争动态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/10/apple-sues-openai-over-alleged-trade-secret-theft/">Apple sues OpenAI over alleged trade secret theft - TechCrunch</a></li>
<li><a href="https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/">Apple sues OpenAI, accuses ex-employees of stealing trade ...</a></li>
<li><a href="https://officechai.com/ai/how-apple-alleges-former-employees-chang-liu-and-alyssa-peng-stole-its-secrets-for-openai/">How Apple Alleges Former Employees Chang Liu And Alyssa Peng ...</a></li>

</ul>
</details>

**社区讨论**: Reddit 用户对这些详细的指控表示震惊，一些人指出苹果此前与 OpenAI 合作的讽刺之处。其他人则讨论了这对 AI 硬件竞争和员工流动的影响。

**标签**: `#Apple`, `#OpenAI`, `#lawsuit`, `#trade secrets`, `#AI`

---

<a id="item-11"></a>
## [OpenAI 安全负责人离职](https://www.reddit.com/r/artificial/comments/1utb2cp/openais_head_of_safety_is_leaving_the_company/) ⭐️ 8.0/10

据彭博社报道并在 Reddit 上讨论，OpenAI 的安全负责人已离开公司。 这一离职引发了对 OpenAI 在 AI 安全方面承诺的担忧，可能表明这家领先 AI 公司的优先事项发生了转变。 离职的具体原因尚未披露，也不清楚将由谁接替这一职位。

reddit · r/artificial · /u/Horsesrunfree · 7月11日 05:18

**背景**: OpenAI 是一家著名的 AI 研究机构，以开发 GPT-4 等先进模型而闻名。安全负责人负责监督确保 AI 系统负责任地开发并与人类价值观保持一致的工作。

**社区讨论**: Reddit 上的讨论可能包括对 AI 安全文化的担忧以及对内部紧张的猜测，尽管没有提供具体评论。

**标签**: `#OpenAI`, `#AI safety`, `#leadership change`, `#artificial intelligence`

---

<a id="item-12"></a>
## [Superpowers：GitHub 上趋势的智能体技能框架](https://github.com/obra/superpowers) ⭐️ 8.0/10

GitHub 仓库 obra/superpowers 在一天内获得超过 740 颗星，总星数达到 252,502，作为一个智能体技能框架和软件开发方法论。 这种快速增长表明社区对 AI 编码智能体的结构化、可复用技能有强烈兴趣，这可能标准化开发者将 AI 集成到工作流程中的方式。 该框架主要针对 Claude Code、Cursor、Codex、OpenCode 和 Gemini CLI 等 AI 编码智能体，并强调基于上下文触发的可组合技能。

github_trending · GitHub Trending · 7月12日 02:52

**背景**: 智能体技能是一种轻量级、开放格式，通过专门知识和工作流程扩展 AI 智能体能力，由 SKILL.md 文件定义。Agent Skills 开放标准确保不同编码智能体之间的兼容性，实现即插即用的生态系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/obra/superpowers">GitHub - obra/superpowers: An agentic skills framework ...</a></li>
<li><a href="https://agentskills.io/home">Agent Skills Overview - Agent Skills</a></li>
<li><a href="https://agentskills.io/specification">Specification - Agent Skills</a></li>

</ul>
</details>

**标签**: `#software development`, `#methodology`, `#framework`, `#agentic`

---

<a id="item-13"></a>
## [OpenManus AI 智能体框架在 GitHub 上迅速走红](https://github.com/FoundationAgents/OpenManus) ⭐️ 8.0/10

由 FoundationAgents 开发的开源 AI 智能体框架 OpenManus 在一天内获得了 226 颗星，GitHub 总星数达到 57,179 颗。 这种快速增长表明社区对开源 AI 智能体框架的强烈兴趣，这些框架对于构建无需手动脚本的自主工作流和多步骤任务执行至关重要。 该仓库使用 Python 编写，拥有 9,953 个复刻，表明社区贡献活跃。该项目强调开放理念，标语为“没有堡垒，纯粹开放之地”。

github_trending · GitHub Trending · 7月12日 02:52

**背景**: AI 智能体框架使开发者能够构建可解释目标并执行复杂工作流的自主智能体。OpenManus 提供了创建此类智能体的基本能力，注重灵活性和社区驱动开发。FoundationAgents 是一个为通用 AI 智能体构建开源基础设施的组织。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openmanus.github.io/">OpenManus - Open-source Framework for Building AI Agents</a></li>
<li><a href="https://github.com/FoundationAgents">FoundationAgents · GitHub</a></li>
<li><a href="https://www.everydev.ai/developers/foundationagents">FoundationAgents - 1 AI Tool | EveryDev.ai</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Open Source`, `#Python`, `#Framework`

---

<a id="item-14"></a>
## [OpenAI 发布 Codex CLI：基于 Rust 的轻量级编码代理](https://github.com/openai/codex) ⭐️ 8.0/10

OpenAI 发布了 Codex CLI，这是一个用 Rust 构建的轻量级编码代理，可直接在终端中运行，并以开源项目形式托管在 GitHub 上。该仓库已获得超过 97,000 颗星，并在过去一天内新增了 224 颗星。 Codex CLI 代表了一种实用的本地运行编码代理，可无缝集成到开发人员的工作流程中，与 Claude Code 等工具竞争。其高社区关注度表明市场对基于终端的 AI 辅助开发工具有强烈需求。 Codex CLI 使用 Rust 构建，强调性能和轻量级操作，并在用户本地计算机上运行。它与早期的 OpenAI Codex 模型（GPT-3 的后代）不同，专注于基于终端的代理式编码，而非 IDE 集成。

github_trending · GitHub Trending · 7月12日 02:52

**背景**: 编码代理是一种 AI 工具，能够理解代码库并通过自然语言执行编辑文件、运行命令和管理 git 工作流等任务。OpenAI 的 Codex 最初是为 GitHub Copilot 提供支持的模型，但 Codex CLI 是一个新的独立代理。类似工具包括 Anthropic 的 Claude Code，它同样在终端中运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/codex">GitHub - openai/codex: Lightweight coding agent that runs in ...</a></li>
<li><a href="https://openai.com/codex/">Codex in ChatGPT | AI Coding Agents for Software ... - OpenAI</a></li>
<li><a href="https://openai.com/index/openai-codex/">OpenAI Codex</a></li>

</ul>
</details>

**标签**: `#coding agent`, `#AI`, `#terminal`, `#Rust`, `#developer tools`

---

<a id="item-15"></a>
## [Hugging Face 推出用于本地语音代理的语音转语音仓库](https://github.com/huggingface/speech-to-speech) ⭐️ 8.0/10

Hugging Face 发布了一个新的开源仓库 huggingface/speech-to-speech，允许开发者使用开源模型构建本地语音代理。该仓库今日获得 94 颗星，总星数超过 6000，显示出强劲的社区关注度。 该仓库使开发者能够创建完全在本地运行的语音代理，从而增强隐私性并减少对云服务的依赖。这与设备端 AI 和开源语音技术的增长趋势相一致。 该仓库使用 Python 编写，提供利用开源模型构建语音转语音管道的工具。目前已有 857 个复刻，表明社区参与活跃。

github_trending · GitHub Trending · 7月12日 02:52

**背景**: 语音转语音系统将语音输入直接转换为语音输出，通常涉及自动语音识别（ASR）、自然语言处理（NLP）和文本转语音（TTS）组件。本地语音代理在用户设备上运行，无需将数据发送到外部服务器，从而提供更低的延迟和更好的隐私保护。Hugging Face 是开源机器学习模型和工具的领先平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/jesuscopado/local-voice-ai-agent">GitHub - jesuscopado/local-voice-ai-agent: A real-time voice ...</a></li>
<li><a href="https://github.com/ShayneP/local-voice-ai">GitHub - ShayneP/local-voice-ai: Local voice AI powered by ...</a></li>

</ul>
</details>

**标签**: `#speech-to-speech`, `#open-source`, `#voice agents`, `#Hugging Face`, `#AI`

---