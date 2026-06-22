---
layout: default
title: "Horizon Summary: 2026-06-22 (EN)"
date: 2026-06-22
lang: en
---

> From 148 items, 15 important content pieces were selected

---

1. [AirLLM Runs 70B LLMs on a Single 4GB GPU](#item-1) ⭐️ 8.0/10
2. [ByteDance Open-Sources DeerFlow SuperAgent Framework](#item-2) ⭐️ 8.0/10
3. [Moebius: Lightweight Inpainting Matches 10B Models](#item-3) ⭐️ 8.0/10
4. [DragMesh-2: Robust Dexterous Hand Interaction with Articulated Objects](#item-4) ⭐️ 8.0/10
5. [Hotz: AI Doom Narratives Inflate Valuations](#item-5) ⭐️ 8.0/10
6. [Google IPv6 Traffic Reaches 50% Milestone](#item-6) ⭐️ 8.0/10
7. [Samsung Deploys ChatGPT Enterprise and Codex to Employees](#item-7) ⭐️ 8.0/10
8. [Complete Guide to Local LLM Inference Optimization](#item-8) ⭐️ 8.0/10
9. [Qwen Shifts Away from Open Source After Key Departure](#item-9) ⭐️ 8.0/10
10. [Hobbyist Trains 500M LLM and 330M Image Generator for $800](#item-10) ⭐️ 8.0/10
11. [Best Local Vision Models: 2nd Benchmark Update](#item-11) ⭐️ 8.0/10
12. [Gemma 4 QAT Models Show Robustness to KV Cache Quantization](#item-12) ⭐️ 8.0/10
13. [PermaVid: Consistent Video Generation via Disentangled Context Memory](#item-13) ⭐️ 8.0/10
14. [Softmax-Free Attention Model at GPT-2 Medium Scale Released](#item-14) ⭐️ 8.0/10
15. [AI-Generated Books and Music Surge, Outnumbering Human Works](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AirLLM Runs 70B LLMs on a Single 4GB GPU](https://github.com/lyogavin/airllm) ⭐️ 8.0/10

AirLLM, an open-source inference optimization library, now enables running 70-billion-parameter large language models on a single 4GB GPU without quantization, distillation, or pruning. It also supports 405B Llama 3.1 on 8GB VRAM. This breakthrough democratizes access to large LLMs by eliminating the need for expensive multi-GPU setups, allowing developers and researchers with consumer-grade GPUs to experiment with state-of-the-art models. It could accelerate innovation in edge AI and local deployment scenarios. AirLLM uses layer-wise inference to load only one transformer layer at a time into GPU memory, drastically reducing peak memory usage. The technique does not compromise model accuracy, as it avoids quantization or other compression methods.

github_trending · GitHub Trending · Jun 22, 04:34

**Background**: Large language models like Llama 3 70B typically require multiple high-end GPUs (e.g., 2× A100 100GB) for inference due to their massive parameter size (130GB+). AirLLM's layer-wise approach leverages the observation that only one layer is active at a time during inference, enabling efficient memory reuse.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/lyogavin/airllm">GitHub - lyogavin/ airllm : AirLLM 70 B inference with single 4 GB GPU</a></li>
<li><a href="https://huggingface.co/blog/lyogavin/airllm">Unbelievable! Run 70 B LLM Inference on a Single 4 GB GPU with...</a></li>
<li><a href="https://www.blog.brightcoding.dev/2026/02/27/airllm-run-70b-models-on-4gb-gpus-without-compromise">AirLLM: Run 70B Models on 4GB GPUs Without Compromise</a></li>

</ul>
</details>

**Discussion**: The community response has been overwhelmingly positive, with many praising the practicality and accessibility of the tool. Some users have raised questions about inference speed and batch processing limitations, but overall sentiment is highly enthusiastic.

**Tags**: `#LLM`, `#inference`, `#GPU`, `#open-source`, `#deep learning`

---

<a id="item-2"></a>
## [ByteDance Open-Sources DeerFlow SuperAgent Framework](https://github.com/bytedance/deer-flow) ⭐️ 8.0/10

ByteDance has open-sourced DeerFlow, a SuperAgent framework for long-horizon tasks that integrates sandboxes, memory, tools, skills, subagents, and a message gateway. The project has gained 442 stars in a single day, reaching over 72,000 total stars on GitHub. DeerFlow addresses the challenge of long-horizon tasks in AI, which require planning and execution over extended periods with multiple steps. As an open-source framework from a major tech company, it could accelerate development of complex AI agents for research, coding, and creative work. The framework is written in Python and handles tasks that could take minutes to hours. It combines sandboxes for safe execution, memory for context retention, tools for external actions, skills for specialized capabilities, subagents for modular decomposition, and a message gateway for communication.

github_trending · GitHub Trending · Jun 22, 04:34

**Background**: Long-horizon tasks are a significant challenge in AI research, requiring models to plan and execute over extended periods with complex decision-making. SuperAgent frameworks like DeerFlow aim to provide a structured approach to building such agents, integrating multiple components to handle diverse task levels. ByteDance's release adds to the growing ecosystem of open-source agent frameworks.

<details><summary>References</summary>
<ul>
<li><a href="https://john-shulman-gpt4o-gemini-flash.vercel.app/advancements-in-ai-capabilities/long-horizon-tasks">Long - Horizon Tasks – Nextra</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#agent`, `#Python`, `#ByteDance`

---

<a id="item-3"></a>
## [Moebius: Lightweight Inpainting Matches 10B Models](https://huggingface.co/papers/2606.19195) ⭐️ 8.0/10

Researchers propose Moebius, a lightweight image inpainting framework with only 0.22B parameters that achieves generation quality comparable to the 10B-level FLUX.1-Fill-Dev model, while delivering over 15x faster inference. This breakthrough enables high-fidelity image inpainting on resource-constrained devices, significantly lowering the deployment barrier for practical applications such as photo editing and content restoration. Moebius introduces the Local-λ Mix Interaction (LλMI) block, which compresses spatial and global semantic priors into fixed-size linear matrices, and pairs it with an adaptive multi-granularity distillation strategy operating entirely in latent space.

huggingface_papers · Hugging Face Papers · Jun 19, 00:00

**Background**: Image inpainting aims to fill missing or corrupted regions in images. Large-scale diffusion models like FLUX.1-Fill-Dev achieve high quality but require massive computational resources, limiting their use. Knowledge distillation transfers knowledge from a large teacher model to a smaller student model, but extreme compression often causes a representation bottleneck.

<details><summary>References</summary>
<ul>
<li><a href="https://hustvl.github.io/Moebius/">Moebius Project Page - hustvl.github.io</a></li>
<li><a href="https://x.com/YS_CodeToRich/status/2068360015090786535">Moebius employs a novel Local-λ Mix Interaction (LλM I) block ...</a></li>

</ul>
</details>

**Tags**: `#image inpainting`, `#lightweight model`, `#diffusion model`, `#knowledge distillation`, `#computer vision`

---

<a id="item-4"></a>
## [DragMesh-2: Robust Dexterous Hand Interaction with Articulated Objects](https://huggingface.co/papers/2606.15133) ⭐️ 8.0/10

DragMesh-2 is a contact-driven framework for dexterous hand-object interaction with articulated objects, and it introduces PICA, a physically informed contact-aware training mechanism that enhances robustness under varying contact loads without requiring tactile or force feedback. This work addresses a critical challenge in robotics: enabling multi-finger hands to manipulate articulated objects (like doors or scissors) through sustained contact, which is essential for household and assistive robots. The PICA technique improves policy robustness without expensive tactile sensors, making dexterous manipulation more practical for real-world deployment. The method was evaluated on seven GAPartNet objects across multiple damping conditions, achieving stronger robustness under contact-load variation than compared methods while maintaining high task success. PICA injects physical signals into policy learning without tactile or force feedback, addressing the overfitting issue of policies trained under fixed dynamics.

huggingface_papers · Hugging Face Papers · Jun 19, 00:00

**Background**: Dexterous manipulation with articulated objects is challenging because the target part cannot be directly actuated; its motion must emerge through sustained physical contact. Traditional geometric trajectory replay or open-loop execution fails to model the contact dynamics required. Reinforcement learning policies often overfit to nominal contact loads and degrade when loads change, especially without tactile feedback.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.13644">[2512.13644] World Models for Learning Dexterous Hand-Object ... Contact Driven Functional Grasp Synthesis via Hand-Object ... Tactile-Driven Dexterous In-Hand Writing via Extrinsic ... Tactile-reactive gripper with an active palm for dexterous ... [2504.03515] Dexterous Manipulation through Imitation ... Contact Driven Functional Grasp Synthesis via Hand-Object ...</a></li>
<li><a href="https://arxiv.org/abs/2507.06822">Hierarchical Reinforcement Learning for Articulated Tool ...</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#dexterous manipulation`, `#articulated objects`, `#contact-driven`, `#reinforcement learning`

---

<a id="item-5"></a>
## [Hotz: AI Doom Narratives Inflate Valuations](https://geohot.github.io//blog/jekyll/update/2026/06/21/the-doom-justifies-the-valuation.html) ⭐️ 8.0/10

George Hotz argues that AI companies strategically use existential risk narratives to justify inflated valuations, drawing parallels to past tech hype cycles like NFTs and the metaverse. This critique challenges the prevailing AI safety discourse and its financial incentives, potentially reshaping how investors and the public perceive AI risk warnings. Hotz notes that institutional investors often dismiss mass unemployment fears, suggesting the doom narrative serves more as a marketing or recruiting tool than a genuine valuation driver.

hackernews · inatreecrown2 · Jun 22, 00:45 · [Discussion](https://news.ycombinator.com/item?id=48624195)

**Background**: AI safety warnings from figures like Dario Amodei and Sam Altman have been used to advocate for regulation and attract investment. Hotz's post questions the sincerity of these warnings, linking them to the hype cycles seen in previous tech bubbles.

**Discussion**: Comments are mixed: some agree that doom narratives are incentivized by investment needs, while others argue that genuine concern about AGI risk exists independently of valuation. A few note the cultural references to Chinese terms like 'neijuan' and 'bailan'.

**Tags**: `#AI safety`, `#venture capital`, `#hype cycles`, `#technology criticism`, `#George Hotz`

---

<a id="item-6"></a>
## [Google IPv6 Traffic Reaches 50% Milestone](https://blog.apnic.net/2026/04/28/google-hits-50-ipv6/) ⭐️ 8.0/10

Google's IPv6 traffic has reached 50% of its total traffic, marking a major milestone in the global transition from IPv4 to IPv6. This milestone demonstrates significant progress in IPv6 adoption, which is critical to overcoming IPv4 address exhaustion and ensuring the internet's continued growth. The 50% figure is based on Google's global traffic measurements, but adoption varies widely by region and ISP, with many providers still lagging in deployment.

hackernews · barqawiz · Jun 21, 08:21 · [Discussion](https://news.ycombinator.com/item?id=48616800)

**Background**: IPv6 is the next-generation internet protocol designed to replace IPv4, which has a limited address space of about 4.3 billion addresses. The transition has been slow due to the need for ISP upgrades, hardware compatibility, and the continued use of IPv4 via NAT.

<details><summary>References</summary>
<ul>
<li><a href="https://www.digicert.com/blog/the-state-of-ipv6-adoption-in-2025-progress-pitfalls-and-pathways-forward">digicert.com/blog/the-state-of- ipv 6 - adoption -in-2025-progress-pitfalls...</a></li>
<li><a href="https://en.wikipedia.org/wiki/IPv6_deployment">IPv6 deployment - Wikipedia</a></li>
<li><a href="https://tools.forwardingplane.net/guides/isp-enable/">Enabling IPv6 on US Consumer ISPs - IPv6 is the current ...</a></li>

</ul>
</details>

**Discussion**: Community comments highlight ongoing ISP adoption gaps, with users noting that major ISPs like Virgin Media (UK) and Odido (Netherlands) still lack IPv6 support. Some also point out that platforms like GitHub do not support IPv6, requiring workarounds like NAT64.

**Tags**: `#IPv6`, `#networking`, `#internet infrastructure`, `#adoption`

---

<a id="item-7"></a>
## [Samsung Deploys ChatGPT Enterprise and Codex to Employees](https://openai.com/index/samsung-electronics-chatgpt-codex-deployment) ⭐️ 8.0/10

Samsung Electronics is deploying ChatGPT Enterprise and Codex to employees worldwide, marking one of OpenAI's largest enterprise AI rollouts. This deployment signifies major enterprise adoption of generative AI, potentially boosting productivity and innovation at a global tech leader, and validating OpenAI's enterprise offerings. ChatGPT Enterprise offers enhanced security, privacy, and integration capabilities, while Codex is an AI coding assistant. The rollout covers employees worldwide, indicating a large-scale implementation.

rss · OpenAI Blog · Jun 21, 23:00

**Background**: ChatGPT Enterprise is OpenAI's business-oriented version of ChatGPT, designed for organizational use with features like no usage caps, faster performance, and 32k context length. Codex is an AI system that translates natural language into code, assisting developers. Samsung's adoption reflects a trend of major corporations integrating AI tools to enhance operations.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-enterprise/">Introducing ChatGPT Enterprise | OpenAI</a></li>
<li><a href="https://grokipedia.com/page/ChatGPT_Enterprise">ChatGPT Enterprise</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Enterprise`, `#OpenAI`, `#Samsung`, `#ChatGPT`

---

<a id="item-8"></a>
## [Complete Guide to Local LLM Inference Optimization](https://www.reddit.com/r/LocalLLaMA/comments/1uc3wg9/local_llm_inference_optimization_the_complete/) ⭐️ 8.0/10

A comprehensive guide compiling a year of experiments on local LLM inference optimization using llama.cpp has been published, covering VRAM fitting, KV cache tuning, MoE placement, MTP, CPU tuning, and common OOM traps. This guide addresses a common pain point for the local LLM community by providing actionable, practical optimization tips that can help users run larger models on limited hardware, democratizing access to powerful AI. The guide is based on a year of hands-on experiments and covers specific techniques such as KV cache quantization, expert offloading for Mixture-of-Experts models, and CPU offloading strategies to avoid out-of-memory errors.

reddit · r/LocalLLaMA · /u/carteakey · Jun 21, 23:01

**Background**: llama.cpp is an open-source C/C++ library for LLM inference that has become the de facto standard for local inference tools like Ollama and LM Studio. KV cache is a critical technique for efficient inference, storing intermediate key-value pairs to avoid recomputation. Mixture-of-Experts (MoE) is an architecture that uses multiple sub-models (experts) to increase model capacity while keeping computational cost manageable.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms">Understanding and Coding the KV Cache in LLMs from Scratch</a></li>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts (MoE) Mixture of Experts in Large Language Models - arXiv.org How Mixture-of-Experts LLMs Work - Medium Mixture of Experts Explained - Hugging Face Applying Mixture of Experts in LLM Architectures | NVIDIA ... [2507.11181] Mixture of Experts in Large Language Models Mixture of Experts (MoE) | Sebastian Raschka, PhD</a></li>

</ul>
</details>

**Discussion**: The Reddit community praised the guide as high-value and technically deep, with users sharing additional tips and corrections. Some discussed specific experiences with MoE models and VRAM optimization.

**Tags**: `#llama.cpp`, `#LLM inference`, `#optimization`, `#local LLM`, `#VRAM`

---

<a id="item-9"></a>
## [Qwen Shifts Away from Open Source After Key Departure](https://www.reddit.com/r/LocalLLaMA/comments/1ubjnh5/qwen_is_never_going_to_open_source_qwen_37_arent/) ⭐️ 8.0/10

Qwen, Alibaba's AI lab, has stopped open-sourcing its large models after firing Junyang Lin, the head of the Qwen team, making it the last major Chinese AI lab to release an open-source model recently. This marks a significant shift in the open-source AI landscape, as Qwen models were widely used for fine-tuning and local deployment; the move could reduce the availability of high-quality open-source models and impact the global AI community. Qwen 3.7-Max and Qwen 3.7-Plus remain fully closed-source, and rumors indicate the small-model team has been disbanded; other Chinese labs like GLM, Kimi, MiniMax, Step, MiMo, DeepSeek, and AKA have all released open-source models more recently than Qwen.

reddit · r/LocalLLaMA · /u/DistanceSolar1449 · Jun 21, 07:25

**Background**: Qwen was one of the leading Chinese AI labs known for releasing open-source large language models, which became popular for fine-tuning and local inference. Junyang Lin, the former head of the Qwen team, was a key figure behind these releases. His departure has led to a change in strategy, with Alibaba now focusing on proprietary models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aibase.com/news/25894">Head of Alibaba Tongyi Qianwen, Lin Junyang , Announces...</a></li>
<li><a href="https://aiproductivity.ai/news/chinese-labs-delaying-open-source-model-releases/">Chinese AI Labs Are All Withholding Open - Source Models at the...</a></li>

</ul>
</details>

**Discussion**: The Reddit community expresses disappointment and concern, with many noting that Qwen's shift away from open source is a loss for the community. Some users point out that other Chinese labs are still releasing open-source models, while others speculate about internal turmoil at Alibaba.

**Tags**: `#open source`, `#Qwen`, `#AI models`, `#Chinese AI labs`, `#community discussion`

---

<a id="item-10"></a>
## [Hobbyist Trains 500M LLM and 330M Image Generator for $800](https://www.reddit.com/r/LocalLLaMA/comments/1ubuy8w/i_pretrained_and_post_trained_a_500m_parameter/) ⭐️ 8.0/10

A hobbyist pretrained and post-trained a 500M parameter LLM and a 330M parameter image generator from scratch using 8xH200 GPUs on Modal, spending only $800, and released the weights, a playground, and training/inference code on GitHub. This demonstrates that pretraining large models from scratch is becoming accessible to individuals, not just large organizations, potentially accelerating open-source AI development and democratizing model creation. The LLM was trained on 40B tokens from the FineWeb dataset, and the image generator uses a SIGLIP encoder and an architecture inspired by ByteDance's DreamLite. The total cost of $800 includes all compute and data expenses.

reddit · r/LocalLLaMA · /u/Altruistic-Tea-5612 · Jun 21, 16:52

**Background**: Pretraining large language models and image generators typically requires massive compute resources and budgets, often costing millions of dollars. FineWeb is a high-quality open-source dataset for LLM pretraining, while SIGLIP is an efficient vision-language encoder. DreamLite is a lightweight on-device image generation architecture. This project shows that with efficient architectures and modern cloud GPUs, costs can be drastically reduced.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1">FineWeb: decanting the web for the finest text data at scale ...</a></li>
<li><a href="https://arxiv.org/abs/2502.14786">[2502.14786] SigLIP 2: Multilingual Vision-Language Encoders ... SigLIP · Hugging Face SigLIP 2: Multilingual Vision-Language Encoders with Improved ... Understanding SIGLIP, the more efficient vision encoder SigLIP | google-research/big_vision | DeepWiki SigLIP 2: Multilingual Vision-Language Encoders with Improved ...</a></li>
<li><a href="https://github.com/ByteVisionLab/DreamLite">DreamLite: A Lightweight On-Device Unified Model for Image Generation ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#pretraining`, `#image generation`, `#open-source`, `#hobby project`

---

<a id="item-11"></a>
## [Best Local Vision Models: 2nd Benchmark Update](https://www.reddit.com/r/LocalLLaMA/comments/1ubx4rw/best_local_model_for_vision_2nd_benchmark_update/) ⭐️ 8.0/10

The author published a second benchmark update for local vision-language models, expanding the dataset from 20 to 30 images, switching from Ollama to llama.cpp, and testing 23 models with 2,070 total tests. Key findings include that thinking mode hurts vision performance and that MoE models underperform dense models of similar size. This benchmark provides practical, hardware-tiered recommendations for running vision models locally, helping users choose the best model for their VRAM budget. The findings challenge common assumptions about thinking modes and MoE architectures in vision tasks. The top recommendation for 4-8 GB VRAM is Qwen3.5 4B (nothink) at Q4 with a score of 75.5/100; for 12-16 GB, Qwen3-VL 8B at Q8 scores 74.4/100; and for 24+ GB, Qwen3.6 27B (nothink) at Q4 scores 79.6/100. The benchmark also found that Q8 quantization is not always beneficial and can cause timeouts in hybrid thinking models.

reddit · r/LocalLLaMA · /u/ex-arman68 · Jun 21, 18:18

**Background**: Vision-language models (VLMs) process images and text together, but running them locally requires careful balancing of model size, quantization, and inference settings. Quantization reduces model size and speeds up inference at the cost of some accuracy, with Q4 and Q8 being common levels. The llama.cpp library allows fine-grained control over image token budgets and batch sizes, which significantly affects performance.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/google/gemma-4-12B">google/ gemma - 4 -12B · Hugging Face</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/17172">Proper handling of large images (4k) with llama-server ...</a></li>
<li><a href="https://medium.com/@paul.ilvez/demystifying-llm-quantization-suffixes-what-q4-k-m-q8-0-and-q6-k-really-mean-0ec2770f17d3">Demystifying LLM Quantization Suffixes: What Q4_K_M, Q8_0 ...</a></li>

</ul>
</details>

**Tags**: `#local-llm`, `#vision-language-model`, `#benchmark`, `#llama.cpp`, `#open-source-ai`

---

<a id="item-12"></a>
## [Gemma 4 QAT Models Show Robustness to KV Cache Quantization](https://www.reddit.com/r/LocalLLaMA/comments/1ubl0df/gemma_4_qat_seems_to_respond_significantly_better/) ⭐️ 8.0/10

A Reddit user reported that Gemma 4 QAT (Quantization-Aware Training) models exhibit significantly lower KL divergence under KV cache quantization compared to non-QAT models, based on tests with 16k context on Wikitext. The Q8_0 quantization on QAT models shows a 99.9% KL divergence metric, indicating minimal performance degradation. This finding suggests that QAT can make large language models more robust to KV cache quantization, a key optimization for reducing memory and speeding up inference. It could enable broader deployment of Gemma 4 models on consumer hardware without sacrificing quality. The user measured KL divergence between the full 16-bit KV cache and quantized versions, with 99.9% KLD indicating near-identical attention behavior. The test was limited to smaller Gemma 4 models due to hardware constraints, and the 31B model remains untested.

reddit · r/LocalLLaMA · /u/rima_2711 · Jun 21, 08:48

**Background**: KV cache quantization reduces memory usage during LLM inference by storing key-value states in lower precision (e.g., 8-bit instead of 16-bit). Quantization-Aware Training (QAT) incorporates quantization effects during training, making models more resilient to post-training quantization. KL divergence measures the difference between output distributions, with lower values indicating better preservation of model behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/quantization-aware-training">What is quantization aware training? - IBM</a></li>
<li><a href="https://huggingface.co/blog/kv-cache-quantization">Unlocking Longer Generation with Key-Value Cache Quantization</a></li>

</ul>
</details>

**Discussion**: The post received positive engagement, with users expressing interest in replicating the results on larger models. Some noted that the 99.9% KLD metric is promising but cautioned that real-world performance may vary.

**Tags**: `#LLM`, `#quantization`, `#KV cache`, `#Gemma`, `#inference optimization`

---

<a id="item-13"></a>
## [PermaVid: Consistent Video Generation via Disentangled Context Memory](https://www.reddit.com/r/StableDiffusion/comments/1uc928a/permavid_consistent_video_generation_across_edits/) ⭐️ 8.0/10

PermaVid introduces a disentangled context memory method that maintains consistency across video edits, and releases a 400GB training dataset along with open-source code on GitHub. This work addresses a key challenge in video generation—maintaining temporal and spatial coherence after edits—which is crucial for practical applications like video editing and content creation. The large open-source dataset and code lower the barrier for researchers and developers to advance the field. The method uses a parallel visual memory branch and disentangled RGB-depth context to decouple visual retrieval from text-induced dilution, enabling persistent memory across long video sequences. The dataset is hosted on Hugging Face and includes 400GB of training data.

reddit · r/StableDiffusion · /u/Sporeboss · Jun 22, 03:04

**Background**: Video generation models often struggle with consistency when edits are applied, as changes can cause temporal flickering or loss of context. Disentangled representation learning separates different factors of variation (e.g., pose vs. appearance) to improve control and stability. PermaVid builds on these ideas by introducing a dedicated memory mechanism for video editing tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.16449">[2606.16449] PermaVid: Consistent Video Generation Across Edits...</a></li>
<li><a href="https://www.emergentmind.com/topics/permavid">PermaVid: Persistent Visual Memory</a></li>

</ul>
</details>

**Discussion**: The Reddit community received PermaVid positively, with users praising the open-source release and large dataset. Some technical discussions focused on the memory mechanism's efficiency and potential applications in long-form video generation.

**Tags**: `#video generation`, `#AI/ML`, `#open-source`, `#dataset`, `#Stable Diffusion`

---

<a id="item-14"></a>
## [Softmax-Free Attention Model at GPT-2 Medium Scale Released](https://www.reddit.com/r/MachineLearning/comments/1ubmybr/i_released_a_softmaxfree_attention_model_at_gpt2/) ⭐️ 8.0/10

A softmax-free attention model at GPT-2 Medium scale (~354M parameters, trained on 11.5B tokens) has been released with open weights and custom Triton kernels that implement structural sparsity and tile-skipping for long-context VRAM savings. This work demonstrates a practical alternative to standard softmax attention, potentially enabling longer context lengths on limited hardware and reducing memory bottlenecks in transformer inference. The model uses structural sparsity and tile-skipping kernels to skip computation on zero tiles, reducing VRAM usage for long sequences. The custom Triton kernels are open-sourced alongside the model weights.

reddit · r/MachineLearning · /u/NonGameCatharsis · Jun 21, 10:46

**Background**: Standard attention mechanisms use a softmax operation to normalize attention scores, which can be computationally expensive and memory-intensive for long sequences. Softmax-free attention replaces softmax with simpler normalization like L1-norm, reducing complexity. Structural sparsity and tile-skipping further optimize attention by skipping irrelevant computations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2206.08898">[2206.08898] SimA: Simple Softmax-free Attention for Vision ...</a></li>
<li><a href="https://modernorange.io/item/48617387">Softmax-free ~354M: tile - skip kernels for... | Modern Orange</a></li>
<li><a href="https://news.ycombinator.com/item?id=48617387">Softmax-free ~354M: tile - skip kernels for long-context... | Hacker News</a></li>

</ul>
</details>

**Discussion**: The community discussion includes technical questions about the softmax-free approach and tile-skipping implementation, with the author actively engaging and providing clarifications. Overall sentiment is positive, with interest in the open-source release and potential applications.

**Tags**: `#attention`, `#efficiency`, `#open-source`, `#Triton`, `#long-context`

---

<a id="item-15"></a>
## [AI-Generated Books and Music Surge, Outnumbering Human Works](https://www.reddit.com/r/artificial/comments/1ubnaqo/the_surge_of_slopsince_the_release_of_chatgpt35/) ⭐️ 8.0/10

Since the release of ChatGPT-3.5 in late 2022, the number of e-books on Amazon has tripled by late 2025, driven entirely by AI-generated content. Deezer reports that 75,000 AI songs are uploaded daily, making up 44% of new tracks, with 97% of users unable to distinguish AI from human music. This surge signals a fundamental shift in content creation, where AI-generated works now dominate platforms, raising concerns about authenticity, quality, and economic impact on human creators. The findings highlight the urgent need for detection tools and policy responses to manage AI-generated content. The analysis by The Economist shows that the tripling of Amazon e-books is entirely attributable to AI-generated books. Deezer's detection tool found that up to 85% of AI music streams are fraudulent, leading to demonetization of such tracks.

reddit · r/artificial · /u/StarlightDown · Jun 21, 11:06

**Background**: ChatGPT-3.5, released in late 2022, made advanced AI text generation widely accessible, enabling easy creation of books and music. Platforms like Amazon and Deezer have since seen an explosion of AI-generated content, often indistinguishable from human work. Deezer has developed an AI music detector to help identify such content.

<details><summary>References</summary>
<ul>
<li><a href="https://www.w3schools.com/gen_ai/chatgpt-3-5/index.php">ChatGPT - 3 . 5 Tutorial</a></li>
<li><a href="https://www.deezer.com/explore/en-us/ai-music-detector/">Free AI Music Detector by Deezer | AI Song checker</a></li>
<li><a href="https://newsroom-deezer.com/2026/01/ai-generated-music-deezer-selling-detection-tool/">How to Detect AI Music: Deezer Sells Its Detection Tool</a></li>

</ul>
</details>

**Discussion**: Reddit comments express mixed reactions: some users are alarmed by the dominance of AI content and its potential to devalue human creativity, while others argue that AI tools can augment human productivity. A few commenters note that the quality of AI-generated books is often poor, but the volume overwhelms human curation.

**Tags**: `#AI-generated content`, `#publishing`, `#music`, `#content authenticity`, `#industry disruption`

---