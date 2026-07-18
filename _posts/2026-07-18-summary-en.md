---
layout: default
title: "Horizon Summary: 2026-07-18 (EN)"
date: 2026-07-18
lang: en
---

> From 125 items, 15 important content pieces were selected

---

1. [Open-weights Kimi K3 ranks third in Intelligence Index](#item-1) ⭐️ 9.0/10
2. [Ring-Zero: Scaling Zero RL to Trillion Parameters](#item-2) ⭐️ 9.0/10
3. [Open Interpreter: Rust-Based Coding Agent for Open Models](#item-3) ⭐️ 8.0/10
4. [LobeHub: Chief Agent Operator for AI Teams](#item-4) ⭐️ 8.0/10
5. [Boogu-Image-0.1: Open-Source Multimodal Model Family](#item-5) ⭐️ 8.0/10
6. [AI Finds Critical Bugs in OpenVM's ZkVM](#item-6) ⭐️ 8.0/10
7. [Google-backed FireSat satellites launch for wildfire detection](#item-7) ⭐️ 8.0/10
8. [Bonsai 27B Runs on iPhone with 1-Bit Quantization](#item-8) ⭐️ 8.0/10
9. [Trellis.cpp Now Matches Reference Quality for 3D Assets](#item-9) ⭐️ 8.0/10
10. [DeepSeek V4 Flash Runs 1M Context on RTX 5090 via llama.cpp](#item-10) ⭐️ 8.0/10
11. [InternLM Releases 397B Parameter Open-Source Model](#item-11) ⭐️ 8.0/10
12. [MacBook M5 Max Nearly Matches 2× DGX Spark in LLM Benchmark](#item-12) ⭐️ 8.0/10
13. [Two Functional LoRAs for Krea 2 Released](#item-13) ⭐️ 8.0/10
14. [EU AI Act OpenRAG: Legally Structured Chunks with Embeddings](#item-14) ⭐️ 8.0/10
15. [LLM Steganography Tool Hides Messages in Chat Text](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Open-weights Kimi K3 ranks third in Intelligence Index](https://www.reddit.com/r/artificial/comments/1uyrw6h/kimi_k3_landed_third_on_the_intelligence_index/) ⭐️ 9.0/10

Moonshot AI's open-weights model Kimi K3 scored 57.1 on the Artificial Analysis Intelligence Index, placing third behind Fable 5 (59.9) and GPT-5.6 Sol (58.9), and ahead of Opus 4.8. The model tops Program Bench (77.8) and Frontend Code Arena, and its weights are scheduled for public release on July 27. This marks the first time an open-weights model has come within three points of the best closed models, challenging the dominance of proprietary AI. If the weights are released as promised, it could democratize access to frontier-level intelligence and accelerate open-source AI development. Kimi K3 has 2.8 trillion parameters, making it the largest open model ever, with approximately 1 million context length and pricing about half that of Opus per task. However, the benchmarks include Moonshot's own evaluations, and the model has not yet been independently self-hosted since weights are not released.

reddit · r/artificial · /u/hero88645 · Jul 17, 06:39

**Background**: The Artificial Analysis Intelligence Index is a composite benchmark that evaluates AI models across multiple dimensions including reasoning, coding, and knowledge. Open-weights models allow anyone to download and run the model locally, unlike closed models like GPT-5.6 Sol or Opus 4.8 which are only accessible via API. Kimi K3 is developed by Moonshot AI, a Chinese AI company.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://artificialanalysis.ai/models">Comparison of AI Models across Intelligence , Performance, and Price</a></li>
<li><a href="https://digg.com/tech/we56zqdp">Chinese model Kimi-K3 tops Frontend Code Arena benchmark · Digg</a></li>

</ul>
</details>

**Discussion**: The community is cautiously optimistic, with some questioning the validity of Moonshot's own benchmarks and noting that the model hasn't been independently verified. Others highlight the hidden system prompt issue (85 tokens) and the lack of agentic tool calling evaluation. Many are excited about the potential of running frontier-level models locally once weights drop.

**Tags**: `#AI`, `#open-weights`, `#benchmarks`, `#Kimi K3`, `#large language models`

---

<a id="item-2"></a>
## [Ring-Zero: Scaling Zero RL to Trillion Parameters](https://huggingface.co/papers/2607.12395) ⭐️ 9.0/10

Researchers present Ring-Zero, a stable pipeline for scaling zero reinforcement learning to trillion-parameter models, achieving emergent reasoning and competitive performance on seven math benchmarks. This work demonstrates that scaling zero RL to 1T parameters significantly improves sample efficiency and performance, revealing emergent cognitive behaviors like self-verification and parallel reasoning, which could shift the paradigm in large-scale RL for LLMs. The pipeline incorporates clipped importance sampling, training-inference ratio correction, and mixed-precision control to address issues like poor readability and token redundancy. The model, Ring-2.5-1T-Zero, also introduces a structured evaluation framework for chain-of-thought quality across comprehensibility, reproducibility, and efficiency.

huggingface_papers · Hugging Face Papers · Jul 16, 00:00

**Background**: Zero reinforcement learning (zero RL) uses verifiable rewards without human-annotated data to elicit chain-of-thought reasoning in LLMs. Prior work was limited to small models due to computational constraints, leaving scaling behaviors unexplored. This paper addresses that gap by scaling to 1 trillion parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2510.25528">Zero Reinforcement Learning Towards General Domains</a></li>
<li><a href="https://www.emergentmind.com/topics/training-inference-ratio-correction">Training - Inference Ratio Correction</a></li>
<li><a href="https://www.emergentmind.com/topics/cispo-algorithm">CISPO: Clipped Importance Sampling RL</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#large language models`, `#reasoning`, `#scaling`, `#AI research`

---

<a id="item-3"></a>
## [Open Interpreter: Rust-Based Coding Agent for Open Models](https://github.com/openinterpreter/openinterpreter) ⭐️ 8.0/10

Open Interpreter, a Rust-based coding agent optimized for open models like Kimi K3, has gained 431 stars in a single day on GitHub, reaching over 66,000 total stars. This rapid growth signals strong community interest in low-cost, open-weight coding agents, potentially democratizing AI-assisted development and reducing reliance on proprietary models. Open Interpreter ships with a QA skill that lets any model operate and test interfaces, and it can drive web apps in a real browser or operate native apps via trycua.

github_trending · GitHub Trending · Jul 18, 02:45

**Background**: Kimi K3 is an open model with 2.8 trillion parameters, the largest open model to date, with full weights expected by July 2026. Open Interpreter is designed to work with such large open models, providing a coding agent that can execute complex technical tasks by interacting with development environments.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openinterpreter/openinterpreter">GitHub - openinterpreter/openinterpreter: A coding agent for open ...</a></li>
<li><a href="https://www.openinterpreter.com/">Open Interpreter | Coding agent for open models</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**Tags**: `#AI`, `#coding agent`, `#open models`, `#Rust`, `#developer tools`

---

<a id="item-4"></a>
## [LobeHub: Chief Agent Operator for AI Teams](https://github.com/lobehub/lobehub) ⭐️ 8.0/10

LobeHub, a TypeScript-based open-source platform, has gained over 409 stars in a single day and now totals over 80,000 stars on GitHub, positioning itself as a Chief Agent Operator that manages and orchestrates AI agents into continuous 24/7 operations. This project introduces a novel concept of an AI agent operator that automates the hiring, scheduling, and reporting of multiple AI agents, which is highly relevant to the growing trend of multi-agent orchestration and could significantly boost productivity for developers and businesses. LobeHub is written in TypeScript and has 15,631 forks, indicating strong community involvement. It allows users to stay in charge without staying online by organizing agents into a 7×24 operation.

github_trending · GitHub Trending · Jul 18, 02:45

**Background**: AI agent orchestration refers to the systematic coordination of multiple specialized AI agents within a unified framework to accomplish complex tasks. LobeHub acts as a Chief Agent Operator that hires, schedules, and reports on an entire AI team, similar to how a human manager would oversee a team of workers.

<details><summary>References</summary>
<ul>
<li><a href="https://lobehub.com/">LobeHub - Your Chief Agent Operator</a></li>
<li><a href="https://digg.com/ai/ga7nwocv">LobeHub Launches Chief Agent Operator to Hire AI Agents 24/7 · Digg</a></li>
<li><a href="https://github.com/topics/chief-agent-operator">chief - agent - operator · GitHub Topics · GitHub</a></li>

</ul>
</details>

**Tags**: `#AI`, `#agent orchestration`, `#TypeScript`, `#open source`, `#productivity`

---

<a id="item-5"></a>
## [Boogu-Image-0.1: Open-Source Multimodal Model Family](https://huggingface.co/papers/2607.13125) ⭐️ 8.0/10

Boogu-Image-0.1, an open-source unified multimodal understanding and generation model family, has been released with Base, Turbo, Edit, and Edit-Turbo variants, achieving competitive text-to-image generation, fast inference, and bilingual text rendering. This release bridges the gap between open-source and closed-source multimodal systems by demonstrating that targeted improvements in data quality and training pipelines can achieve near-closed-source performance with limited compute, advancing the open ecosystem. The model was trained on only 208.62 million unique images with a theoretical training cost of approximately $400K, and it uses agentic inference-time scaling to enhance generation and editing performance.

huggingface_papers · Hugging Face Papers · Jul 16, 00:00

**Background**: Unified multimodal understanding and generation models aim to handle both image comprehension and creation within a single framework, unlike traditional systems that separate these tasks. Closed-source models like Nano-Banana-Pro and GPT-Image-2 achieve strong performance through undisclosed system-level integration. Boogu-Image-0.1 is released under the Apache 2.0 license, with weights, code, and recipes publicly available.

<details><summary>References</summary>
<ul>
<li><a href="https://boogu.org/">Boogu - Image - 0 . 1 — Efficient Image Generation Foundation Model</a></li>
<li><a href="https://github.com/boogu-project/Boogu-Image">GitHub - boogu-project/ Boogu - Image : Boogu - Image - 0 . 1 is an...</a></li>
<li><a href="https://www.communeify.com/en/blog/boogu-image-0-1-bilingual-text-to-image-model-analysis/">Full Analysis of Boogu - Image - 0 . 1 : 10B Open-Source AI... | Communeify</a></li>

</ul>
</details>

**Tags**: `#multimodal`, `#text-to-image`, `#open-source`, `#AI`, `#image generation`

---

<a id="item-6"></a>
## [AI Finds Critical Bugs in OpenVM's ZkVM](https://blog.zksecurity.xyz/posts/openvm-bugs/) ⭐️ 8.0/10

AI-assisted analysis discovered vulnerabilities in OpenVM's ZkVM where signature verification could be bypassed, potentially affecting L2 ecosystems. These bugs could compromise the security of L2 solutions relying on OpenVM, highlighting the importance of AI in cryptographic auditing. The vulnerability allows an attacker to forge proofs by bypassing signature verification, similar to verifying a signature on the wrong hash.

hackernews · duha · Jul 17, 14:21 · [Discussion](https://news.ycombinator.com/item?id=48947714)

**Background**: A zkVM (zero-knowledge virtual machine) executes programs and produces cryptographic proofs of correct execution. OpenVM is a modular zkVM framework that supports custom extensions and Rust. Signature verification is critical for ensuring that proofs are authentic and untampered.

<details><summary>References</summary>
<ul>
<li><a href="https://openvm.dev/">A performant and modular zkVM framework built for customization and...</a></li>
<li><a href="https://www.certik.com/blog/what-is-a-zero-knowledge-virtual-machine-zkvm">What Is a Zero - Knowledge Virtual Machine ( zkVM )? - CertiK</a></li>

</ul>
</details>

**Discussion**: Commenters noted the bug is akin to verifying a signature on the wrong hash, and questioned the exploit's impact on L2 ecosystems. One joked about the complexity of cryptography.

**Tags**: `#cryptography`, `#zero-knowledge proofs`, `#security`, `#AI`, `#blockchain`

---

<a id="item-7"></a>
## [Google-backed FireSat satellites launch for wildfire detection](https://arstechnica.com/space/2026/07/google-backed-satellites-for-wildfire-detection-launch-as-smoke-chokes-us-canada/) ⭐️ 8.0/10

The FireSat program, backed by Google, has launched satellites capable of detecting wildfires earlier than existing systems, offering a significant advancement in disaster monitoring. This technology can detect wildfires that other satellites miss, potentially reducing response times and mitigating the devastating impact of wildfires on communities and ecosystems. The FireSat satellites use specialized infrared sensors to detect heat anomalies, enabling early detection even when fires are obscured by smoke or located in remote areas.

rss · Ars Technica AI · Jul 17, 19:50

**Background**: Wildfire detection traditionally relies on ground-based observation and existing satellites, which may have limited sensitivity or revisit times. The FireSat program aims to fill this gap by deploying a constellation of satellites with advanced sensors and AI-powered analysis for near-real-time monitoring.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/descarteslabs-team/the-satellites-hunting-for-megafires-afa1305fdc2c">The Satellites Hunting for Megafires | by Clyde Wheeler | Medium</a></li>
<li><a href="https://www.azosensors.com/article.aspx?ArticleID=3328">Detecting Wildfires Before Disaster Happens</a></li>
<li><a href="https://ororatech.com/resources/news-blog/why-earth-observation-is-the-future-of-fire-detection/">Why Earth Observation is the Future of Wildfire Detection</a></li>

</ul>
</details>

**Tags**: `#wildfire detection`, `#satellite technology`, `#Google`, `#environmental monitoring`, `#disaster response`

---

<a id="item-8"></a>
## [Bonsai 27B Runs on iPhone with 1-Bit Quantization](https://www.reddit.com/r/LocalLLaMA/comments/1uyz9n2/bonsai_27b_runs_locally_on_an_iphone_a_27b_model/) ⭐️ 8.0/10

PrismML released Bonsai 27B, a 27-billion-parameter model compressed to 3.9GB using true 1-bit quantization (binary g128), enabling it to run locally on an iPhone 15 Pro Max while retaining ~90% of original benchmark performance. This breakthrough demonstrates that extremely large language models can be deployed on edge devices like smartphones, dramatically expanding the potential for private, offline AI applications without sacrificing much accuracy. The model uses binary g128 quantization where each weight is a single sign bit and groups of 128 weights share one FP16 scale, achieving ~1.125 bits per weight with no high-precision escape hatches; even embeddings and attention projections are binary. Memory usage is ~5.2GB at 4K context and ~6.8GB at 100K context with 4-bit KV cache.

reddit · r/LocalLLaMA · /u/ElmBark · Jul 17, 13:08

**Background**: Large language models (LLMs) typically require gigabytes of memory and powerful GPUs, making them impractical for mobile devices. Quantization reduces the precision of model weights (e.g., from 16-bit to 1-bit) to shrink size and speed up inference. Previous 1-bit methods often kept some layers at higher precision, but Bonsai applies binary quantization uniformly, achieving extreme compression.

**Discussion**: The community expressed excitement about running a 27B model on a phone, with many praising the ~90% benchmark retention. Some users questioned the practical impact on reasoning and knowledge tasks, noting that those benchmarks dropped more significantly. Others discussed the trade-offs between compression ratio and output quality, and the potential for future improvements.

**Tags**: `#quantization`, `#edge AI`, `#LLM`, `#model compression`, `#mobile deployment`

---

<a id="item-9"></a>
## [Trellis.cpp Now Matches Reference Quality for 3D Assets](https://www.reddit.com/r/LocalLLaMA/comments/1uyw64s/trelliscpp_now_produces_high_quality_assets/) ⭐️ 8.0/10

The open-source project trellis.cpp has fixed critical bugs, achieving image-to-3D asset quality on par with the official reference implementation, now available without CUDA. This makes high-quality open-source 3D generation accessible to anyone with a capable GPU or CPU, democratizing 3D content creation and reducing dependence on proprietary hardware. The project uses GGML for efficient inference on CPU or GPU without CUDA, and can be integrated with Lemonade for an optional text-to-3D pipeline.

reddit · r/LocalLLaMA · /u/ilintar · Jul 17, 10:45

**Background**: TRELLIS is a state-of-the-art image-to-3D generation model that creates 3D meshes from images. GGML is a tensor library for machine learning that enables efficient inference on various hardware, including CPU and non-NVIDIA GPUs. The trellis.cpp project ports the TRELLIS model to GGML, making it more accessible.

<details><summary>References</summary>
<ul>
<li><a href="https://www.trellis-3d.net/">Image to 3 D Model AI Generator | Trellis 3 D</a></li>
<li><a href="https://github.com/ggml-org/ggml">GitHub - ggml -org/ ggml : Tensor library for machine learning · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">llama.cpp - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Reddit community praised the achievement, with users noting the significant quality improvement and thanking the developer for the hard work. Some discussed technical details about the debugging process and potential use cases.

**Tags**: `#3D generation`, `#open source`, `#machine learning`, `#TRELLIS`, `#GGML`

---

<a id="item-10"></a>
## [DeepSeek V4 Flash Runs 1M Context on RTX 5090 via llama.cpp](https://www.reddit.com/r/LocalLLaMA/comments/1uz5w3y/deepseek_v4_flash_on_5090_in_llamacpp_with_1/) ⭐️ 8.0/10

A Reddit user successfully ran DeepSeek V4 Flash with 1 million token context on a single RTX 5090 using llama.cpp, achieving ~650–700 tokens/s prefill and ~17 tokens/s decode speed. This demonstrates that frontier-level MoE models with extremely long context can be deployed on consumer hardware, significantly lowering the barrier for local LLM inference and enabling new applications like long-document analysis. The user used Unsloth's Q8_K_XL GGUF quantization and custom tensor overrides to offload specific expert layers to GPU, with Q8_0 KV cache and flash attention enabled. Loading took 32 seconds.

reddit · r/LocalLLaMA · /u/Shoddy_Bed3240 · Jul 17, 17:14

**Background**: DeepSeek V4 Flash is a Mixture-of-Experts (MoE) model with 284B total parameters and 13B active per token, supporting up to 1M context. llama.cpp is an open-source C++ library for efficient LLM inference on CPUs and GPUs. The RTX 5090 is NVIDIA's latest consumer GPU with 32GB VRAM.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md">llama . cpp /tools/server/README.md at master · ggml-org/ llama . cpp</a></li>
<li><a href="https://unsloth.ai/docs/basics/inference-and-deployment/saving-to-gguf">Saving to GGUF | Unsloth Documentation</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely praised the achievement but noted that decode speed is still slower than Qwen models, and users discussed further optimization opportunities in llama.cpp for MoE models.

**Tags**: `#DeepSeek`, `#llama.cpp`, `#local LLM`, `#RTX 5090`, `#long context`

---

<a id="item-11"></a>
## [InternLM Releases 397B Parameter Open-Source Model](https://www.reddit.com/r/LocalLLaMA/comments/1uzifq8/internlminterns2preview397b_huggingface/) ⭐️ 8.0/10

InternLM has released Intern-S2-Preview-397B, a large language model with 397 billion parameters, available on Hugging Face. This is a preview version of their next-generation model series. This release marks a significant scale-up in open-source LLMs, rivaling proprietary models in size and potentially advancing capabilities in reasoning, coding, and multilingual tasks. It provides the research community with access to a very large model for experimentation and fine-tuning. The model is a preview and likely uses a mixture-of-experts (MoE) architecture to achieve 397B parameters with efficient inference. It is released under an open license, though specific terms may apply.

reddit · r/LocalLLaMA · /u/External_Mood4719 · Jul 18, 01:35

**Background**: InternLM is a series of large language models developed by Shanghai AI Laboratory, known for open-sourcing high-quality LLMs and a full-stack toolchain. Previous models include InternLM 2 and InternLM 3, with sizes up to 20B parameters. The 397B model represents a major jump in scale, leveraging techniques like MoE to balance performance and computational cost.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/internlm">internlm ( Intern Large Models )</a></li>
<li><a href="https://github.com/InternLM/InternLM">GitHub - InternLM / InternLM : Official release of InternLM series ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#open-source`, `#large model`, `#AI research`

---

<a id="item-12"></a>
## [MacBook M5 Max Nearly Matches 2× DGX Spark in LLM Benchmark](https://www.reddit.com/r/LocalLLaMA/comments/1uzaf54/one_macbook_vs_2_dgx_spark_deepseekv4flash_scored/) ⭐️ 8.0/10

A heavily quantized DeepSeek-V4-Flash (80.8 GiB GGUF) on a single MacBook M5 Max achieved 54% accuracy on Terminal-Bench 2.1, while a native FP8/FP4 checkpoint with speculative decoding on 2× DGX Spark scored 52%. This result challenges assumptions that extreme quantization inevitably causes significant accuracy loss, showing that a well-optimized quantized model on consumer hardware can compete with a much more expensive setup. The MacBook used a mixed GGUF with IQ2_XXS/Q2_K experts and higher-precision tensors, averaging ~2.45 bits per weight, while the DGX Spark pair used native FP8 weights with FP4 routed experts and DSpark speculative decoding with 3 draft tokens.

reddit · r/LocalLLaMA · /u/anvarazizov · Jul 17, 19:58

**Background**: GGUF is a binary format for storing quantized LLM weights, enabling models to run on consumer hardware with reduced memory. Speculative decoding uses a small draft model to propose tokens that a larger target model verifies, speeding up inference without changing output distribution. The DGX Spark is NVIDIA's desktop AI supercomputer powered by the GB10 Grace Blackwell chip.

<details><summary>References</summary>
<ul>
<li><a href="https://www.promptquorum.com/local-llms/llm-quantization-explained">Q4_K_M vs Q4_0 vs Q8_0: LLM Quantization Explained (2026)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://www.nvidia.com/en-us/products/workstations/dgx-spark/">Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion highlighted surprise at the small gap, with some attributing it to agent-run variance and the non-deterministic nature of the benchmark. Others noted the Mac's higher context limit and the lack of speculative decoding on the Mac side as potential confounding factors.

**Tags**: `#LLM`, `#benchmark`, `#quantization`, `#local inference`, `#DeepSeek`

---

<a id="item-13"></a>
## [Two Functional LoRAs for Krea 2 Released](https://www.reddit.com/r/StableDiffusion/comments/1uyp5z6/i_released_two_krea_2_functional_loras_identity/) ⭐️ 8.0/10

Two rank-32 functional LoRAs for Krea 2 have been released: an identity reference LoRA that preserves facial identity while changing clothing/pose, and a registered outpainting LoRA that places a source image at a specific canvas location and extends the missing region. These LoRAs enable novel image conditioning behaviors that were previously difficult to achieve, such as identity-preserving editing and precise outpainting, and they come with complete Diffusers pipelines and runnable examples, making them accessible to the community. The identity reference LoRA uses Qwen3-VL image conditioning and clean VAE reference tokens with isolated reference attention and cached reference K/V, while the outpainting LoRA supports one-pass edge placement and a two-pass plan for arbitrary interior placement with seam feathering.

reddit · r/StableDiffusion · /u/Upbeat_Birthday_6123 · Jul 17, 04:13

**Background**: Krea 2 is an open-source 12B-parameter diffusion transformer (DiT) image generation model with two variants: Raw (full-quality) and Turbo (8-step distilled). LoRA (Low-Rank Adaptation) is a technique for fine-tuning large models with small adapter weights. The Diffusers library by Hugging Face provides standard pipelines for running diffusion models.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/yijunwang2/krea2-reid">yijunwang 2 / krea 2 -reid · Hugging Face</a></li>
<li><a href="https://comfyui-wiki.com/en/models/krea">Krea Family: Open Source Diffusion Transformer with... | ComfyUI Wiki</a></li>

</ul>
</details>

**Tags**: `#Stable Diffusion`, `#LoRA`, `#image generation`, `#outpainting`, `#identity reference`

---

<a id="item-14"></a>
## [EU AI Act OpenRAG: Legally Structured Chunks with Embeddings](https://www.reddit.com/r/MachineLearning/comments/1uytlac/eu_ai_act_openrag_933_legally_structured_chunks/) ⭐️ 8.0/10

A new dataset, EU AI Act OpenRAG, provides 933 legally structured chunks of the EU AI Act with BGE-M3 embeddings in a single SQLite file, improving retrieval recall over a sliding-window baseline. This dataset enables more accurate retrieval-augmented generation (RAG) for legal NLP tasks, potentially improving compliance analysis and AI governance research by grounding LLMs in precise legal provisions. The corpus chunks on the regulation's legal structure (articles, recitals, definitions, annex points) and includes exact EUR-Lex links, application-date metadata, and narrow derived labels; retrieval scenario article recall@20 reached 0.541 vs 0.449 baseline.

reddit · r/MachineLearning · /u/Automatic-Forever-63 · Jul 17, 08:18

**Background**: Retrieval-augmented generation (RAG) combines document retrieval with LLM generation to improve factual accuracy. BGE-M3 is a multilingual embedding model supporting dense, sparse, and multi-vector retrieval. EUR-Lex is the official EU law database.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/BAAI/bge-m3?ref=blog-ko.allganize.ai">BAAI/ bge - m 3 · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval - augmented generation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/EUR-Lex">EUR-Lex</a></li>

</ul>
</details>

**Discussion**: The community discussion validates the technical contribution, with users praising the structured chunking approach and requesting additional baselines and comparisons with other legal datasets.

**Tags**: `#RAG`, `#legal NLP`, `#embeddings`, `#EU AI Act`, `#dataset`

---

<a id="item-15"></a>
## [LLM Steganography Tool Hides Messages in Chat Text](https://www.reddit.com/r/artificial/comments/1uz1w22/i_built_a_tool_that_hides_messages_in/) ⭐️ 8.0/10

A proof-of-concept tool called Conversation Stenography uses LLM token probabilities and arithmetic coding to hide encrypted messages in generated text, aiming to bypass automated content scanning. As message scanning becomes more common, this technique offers a potential way to preserve private communication, though it raises ethical concerns about misuse for malicious purposes. The tool uses AES-SIV for encryption and authentication, and requires the receiver to have the same model, tokenizer, configuration, shared secret, and conversation state to decode the message.

reddit · r/artificial · /u/Nethical69 · Jul 17, 14:48

**Background**: Steganography hides the existence of a message, unlike encryption which hides its content. LLM-based steganography leverages the probabilistic nature of language models to embed data in token choices, making the output appear as normal text.

<details><summary>References</summary>
<ul>
<li><a href="https://www.artkpv.net/Tool-Arithmetic-Coding-for-LLM-Steganography/">Arithmetic Coding Steganography Using Frontier Models</a></li>
<li><a href="https://github.com/artkpv/arithmetic-coding-steganography">GitHub - artkpv/ arithmetic - coding - steganography : Arithmetic ...</a></li>
<li><a href="https://arxiv.org/pdf/2410.04328">OD-Stega: LLM -Based Relatively Secure Steganography via...</a></li>

</ul>
</details>

**Discussion**: The community discussion is substantive, with users debating the ethical implications, practicality against advanced scanning, and potential for abuse. Some praise the technical novelty, while others question its statistical undetectability.

**Tags**: `#steganography`, `#LLM`, `#privacy`, `#security`, `#AI`

---