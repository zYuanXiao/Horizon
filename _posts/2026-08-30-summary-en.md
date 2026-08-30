---
layout: default
title: "Horizon Summary: 2026-08-30 (EN)"
date: 2026-08-30
lang: en
---

> From 120 items, 15 important content pieces were selected

---

1. [OpenMAIC: Open-Source Multi-Agent Interactive Classroom Surges on GitHub](#item-1) ⭐️ 8.0/10
2. [OpenMontage: Open-Source Agentic Video Production System](#item-2) ⭐️ 8.0/10
3. [WarpSAC: Regime-Aware Off-Policy RL for Massively Parallel Training](#item-3) ⭐️ 8.0/10
4. [Game Engines as Verifiable Data Engines for Scaling World Models](#item-4) ⭐️ 8.0/10
5. [Samsung's PIM: Promising but Challenging Path to Non-von-Neumann Computing](#item-5) ⭐️ 8.0/10
6. [Record Ocean Temperature as Powerful El Niño Forms](#item-6) ⭐️ 8.0/10
7. [Tencent Compresses Hy4-preview to 200GB GGUF, Retaining 98% Performance](#item-7) ⭐️ 8.0/10
8. [Nemotron-3.5-Lightning Gets 16GB GGUF via ShimQuant](#item-8) ⭐️ 8.0/10
9. [Sopro V2 Turbo: 120M Voice Cloning TTS, 5x Real-Time on CPU](#item-9) ⭐️ 8.0/10
10. [HR Endless Sampler Enables Arbitrary-Length Minimax H3 Videos on 16GB VRAM](#item-10) ⭐️ 8.0/10
11. [Fizgig v5 Enables Full Fine-Tuning of MiniMax H3 and Krea 2 on 16GB GPUs](#item-11) ⭐️ 8.0/10
12. [100-Year-Old SPC Algorithm Beats SOTA on TSB-AD Benchmark](#item-12) ⭐️ 8.0/10
13. [LLM Benchmark Scores Show 3x More Variation Between Days Than Within a Day](#item-13) ⭐️ 8.0/10
14. [Google's SKILL.state cuts agent token use by 94% in long sessions](#item-14) ⭐️ 8.0/10
15. [OpenAI to Cut Off Model Supply to Cursor After SpaceX Acquisition](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenMAIC: Open-Source Multi-Agent Interactive Classroom Surges on GitHub](https://github.com/THU-MAIC/OpenMAIC) ⭐️ 8.0/10

OpenMAIC, an open-source multi-agent interactive classroom platform from THU-MAIC, gained 907 stars in a single day, reaching over 22,000 total stars and 4,337 forks on GitHub. It transforms any topic or document into an immersive learning experience with AI teachers and classmates. This rapid popularity highlights the growing demand for AI-driven education tools and multi-agent systems. OpenMAIC could reshape online learning by making interactive, personalized classrooms accessible to anyone, potentially impacting educators, students, and the edtech industry. The platform is built with TypeScript and uses LangGraph for multi-agent orchestration, enabling AI agents to act as teachers and classmates who can speak, draw on a whiteboard, and engage in discussions. It generates slides, quizzes, interactive simulations, and project-based learning activities in one click.

github_trending · GitHub Trending · Aug 30, 04:07

**Background**: Multi-agent systems involve multiple AI agents collaborating to achieve complex goals. In education, this concept is applied to create virtual classrooms where AI agents simulate teachers and peers, providing an interactive and engaging learning environment. OpenMAIC leverages this to turn static content into dynamic lessons.

<details><summary>References</summary>
<ul>
<li><a href="https://open.maic.chat/home">OpenMAIC — Open Multi-Agent Interactive Classroom</a></li>
<li><a href="https://openmaic.io/">OpenMAIC — Open Multi-Agent Interactive Classroom</a></li>
<li><a href="https://github.com/THU-MAIC/OpenMAIC">GitHub - THU-MAIC/OpenMAIC: Open Multi-Agent Interactive ...</a></li>

</ul>
</details>

**Tags**: `#multi-agent`, `#education`, `#AI`, `#open-source`, `#TypeScript`

---

<a id="item-2"></a>
## [OpenMontage: Open-Source Agentic Video Production System](https://github.com/calesthio/OpenMontage) ⭐️ 8.0/10

OpenMontage, an open-source agentic video production system, has gained significant traction on GitHub with 806 stars in a day and over 54,000 total stars. It offers 12 production pipelines, 100+ tools, and 700+ agent skill files, enabling AI coding assistants to handle full video production. This project could democratize video production by allowing users to describe their vision in plain language and have AI handle research, scripting, asset generation, editing, and composition. It represents a significant step in agentic AI applied to creative media, potentially impacting content creators, marketers, and filmmakers. The system includes 12 production pipelines and over 100 tools, with 700+ agent skill and production-knowledge files. It emphasizes real video production using stock footage and open archives, not just animated stills, and is built in Python.

github_trending · GitHub Trending · Aug 30, 04:07

**Background**: Agentic AI refers to systems that can autonomously perform multi-step tasks with minimal human intervention. In video production, such systems can automate tasks like footage retrieval, editing, and rendering, which traditionally require specialized software and skills. OpenMontage leverages this concept to turn AI coding assistants into comprehensive video production studios.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/calesthio/OpenMontage">GitHub - calesthio/ OpenMontage : World's first open -source, agentic...</a></li>
<li><a href="https://openmontage.apposters.com/">World's First Open-Source Agentic Video Production System</a></li>
<li><a href="https://www.aitoolnet.com/openmontage/">OpenMontage - Open -source agentic video production for... - Aitoolnet</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#AI`, `#video-production`, `#agentic`, `#Python`

---

<a id="item-3"></a>
## [WarpSAC: Regime-Aware Off-Policy RL for Massively Parallel Training](https://huggingface.co/papers/2608.24479) ⭐️ 8.0/10

The paper introduces WarpSAC, a family of regime-aware off-policy RL algorithms that adapt stabilization techniques based on data availability. It proposes two variants: WarpSAC-L for data-limited CPU-scale training and WarpSAC-A for data-abundant GPU-parallel training, achieving significant improvements over FlashSAC. This work addresses a critical issue in massively parallel RL, where traditional stabilizers designed for data-limited replay may be suboptimal. By showing that stabilizers are data-regime-dependent and proposing adaptive algorithms, it offers practical improvements that can enhance efficiency and performance in large-scale training and sim-to-real transfer. WarpSAC uses Sample Weight Decay for efficient exploitation and provides two variants: WarpSAC-L (Norm ON, clipped double-Q) for data-limited CPU-scale training, and WarpSAC-A (Norm OFF, single-Q) for data-abundant GPU-parallel training. It improves normalized score-step AUC over FlashSAC by 4.5% across nine CPU-scale environments and 23.1% across fourteen GPU-parallel environments, and increases UnitreeG1TransportBox-v1 success rate from 19.8% to 96.4%.

huggingface_papers · Hugging Face Papers · Aug 27, 00:00

**Background**: Off-policy reinforcement learning relies on replay buffers to reuse past experiences, and various stabilizers such as parameter normalization and clipped double-Q learning are commonly used to improve stability. However, these stabilizers were often developed under data-limited conditions, and massively parallel simulation changes the data regime, making it necessary to adapt them. WarpSAC builds on this insight to design algorithms that adjust stabilizers based on data availability.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.24479">[2608.24479] WarpSAC: Towards the Pinnacle of Scalable Off ...</a></li>
<li><a href="https://cctest.ai/en/articles/warpsac-why-off-policy-rl-needs-data-regime-aware-stabilizers">WarpSAC Makes Off-Policy RL Adapt to the Data Regime - CCTest</a></li>
<li><a href="https://arxiv.org/abs/2604.01913">[2604.01913] The Rank and Gradient Lost in Non-stationarity: Sample Weight Decay for Mitigating Plasticity Loss in Reinforcement Learning</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#off-policy RL`, `#scalable RL`, `#parallel simulation`, `#algorithm`

---

<a id="item-4"></a>
## [Game Engines as Verifiable Data Engines for Scaling World Models](https://huggingface.co/papers/2608.25518) ⭐️ 8.0/10

This paper proposes a new paradigm called Reinforcement Learning with Human-Engine Verification (RLHEV), which uses game engines as executable verification environments to generate grounded reward signals and long-horizon trajectories for RL post-training of spatial world models. It argues that this approach is more efficient than simply scaling up crawled video data. This matters because spatial generation currently relies on fuzzy proxies like CLIP scores, which are biased and hard to support RL post-training. By providing a verifiable reward environment, game engines could enable more effective RL post-training for world models, potentially accelerating progress in spatial intelligence and embodied AI. The paper highlights that game engines can efficiently check collision, physics, navigability, and bounded playability, while developers provide global verification by judging scene acceptance. RLHEV combines dense engine signals with implicit human acceptance feedback from the development process.

huggingface_papers · Hugging Face Papers · Aug 28, 00:00

**Background**: World models aim to maintain a coherent representation of an environment and predict changes in response to actions, which is key to spatial intelligence. In LLM post-training, RL has been successful because code execution provides verifiable rewards; however, spatial generation lacks such verifiable signals, making RL post-training difficult. Game engines offer a natural solution by acting as executable world specifications.

<details><summary>References</summary>
<ul>
<li><a href="https://lightning.ai/docs/torchmetrics/stable/multimodal/clip_score.html">CLIP Score — PyTorch-Metrics 1.9.0 documentation</a></li>
<li><a href="https://arxiv.org/abs/2607.16097">Understanding Reasoning from Pretraining to Post-Training</a></li>
<li><a href="https://hai.stanford.edu/policy/the-world-model-and-spatial-intelligence-era-governing-ai-beyond-language">The World Model and Spatial Intelligence Era: Governing AI ...</a></li>

</ul>
</details>

**Tags**: `#world models`, `#reinforcement learning`, `#game engines`, `#spatial generation`, `#AI research`

---

<a id="item-5"></a>
## [Samsung's PIM: Promising but Challenging Path to Non-von-Neumann Computing](https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing) ⭐️ 8.0/10

At Hot Chips 2026, Samsung presented its Processing-in-Memory (PIM) technology, which integrates compute units directly into memory to reduce data movement. The presentation highlighted potential benefits for AI and data-intensive workloads but also acknowledged significant hurdles in general-purpose applicability and commercial adoption. PIM represents a significant shift from traditional von Neumann architectures, potentially offering major performance and energy efficiency gains for AI and big data applications. However, its success hinges on overcoming programming constraints and achieving commercial viability, which could influence the future direction of hardware design. The technology requires precise knowledge of data dependencies, which limits its applicability to problems like AI, gaming, and crypto. Historical attempts, such as HPE Labs' similar concept a decade ago, faced leadership changes and strategic shifts, underscoring the difficulty of sustaining such projects.

hackernews · ingve · Aug 29, 06:06 · [Discussion](https://news.ycombinator.com/item?id=49487341)

**Background**: Processing-in-Memory (PIM) is a computer architecture where computation is performed directly in memory, avoiding the costly transfer of data between memory and CPU. This approach is part of the broader non-von Neumann computing movement, which seeks to overcome the 'memory wall' bottleneck of traditional architectures. Hot Chips is a leading semiconductor conference where such innovative designs are often showcased.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/In-memory_processing">In-memory processing - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2773064622000160">A survey on processing-in-memory techniques: Advances and ...</a></li>
<li><a href="https://www.emergentmind.com/topics/processing-in-memory-pim">Processing-in-Memory (PIM) Overview - emergentmind.com</a></li>
<li><a href="https://www.geeksforgeeks.org/computer-organization-architecture/computer-organization-von-neumann-architecture/">Von Neumann Architecture - GeeksforGeeks</a></li>
<li><a href="https://www.nature.com/collections/dhdjceebhg">Non von Neumann computing - Nature</a></li>
<li><a href="https://hotchips.org/about/">About - Hot Chips</a></li>

</ul>
</details>

**Discussion**: Community comments reflect a mix of skepticism and historical awareness. Some note that similar ideas have been proposed for decades, and many exotic accelerators never achieve commercial success. Others point out practical limitations, such as the need for data movement in matrix multiplication, and question whether PIM is the right implementation.

**Tags**: `#Processing-in-Memory`, `#Hardware Architecture`, `#AI Accelerators`, `#Hot Chips`, `#Non-von-Neumann`

---

<a id="item-6"></a>
## [Record Ocean Temperature as Powerful El Niño Forms](https://www.latimes.com/environment/story/2026-08-26/highest-ever-ocean-temperature-measured-as-powerful-el-nino-forms) ⭐️ 8.0/10

On August 22, 2026, the global average sea-surface temperature hit a record 70°F (21°C), according to Europe's Copernicus agency, surpassing the previous single-day record set in March 2024. This record coincides with the formation of a powerful El Niño event. This record-high ocean temperature signals accelerating climate change impacts, as El Niño events are now over 36% stronger than 40 years ago due to climate change. The combination of a powerful El Niño and human-caused warming could make 2027 the hottest year on record, with severe consequences for weather patterns, marine life, and communities worldwide. The record was measured by Copernicus, which has tracked daily sea-surface temperatures since 1979. The previous single-day record was set in March 2024. El Niño events are more than 36% stronger today than 40 years ago, according to a study published in Science.

hackernews · measurablefunc · Aug 29, 23:26 · [Discussion](https://news.ycombinator.com/item?id=49494231)

**Background**: El Niño is a climate phenomenon characterized by unusually warm ocean water in the equatorial Pacific, which affects global weather patterns. Sea surface temperature is a key indicator of climate change, as the ocean absorbs much of the excess heat from greenhouse gas emissions. During El Niño, the ocean transfers heat to the atmosphere, potentially amplifying global warming.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/El_Niño–Southern_Oscillation">El Niño–Southern Oscillation - Wikipedia</a></li>
<li><a href="https://www.bbc.com/news/articles/cj97npgk92po">What is El Niño, and how does it affect the weather and temperatures?</a></li>
<li><a href="https://oceanservice.noaa.gov/facts/sea-surface-temperature.html">Why do scientists measure sea surface temperature?</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern and frustration about climate change impacts, with one noting higher water and electricity bills due to non-stop AC use. Another lamented that few seem to care about climate change despite sweltering conditions, and asked for suggestions to get involved. Some comments highlighted the scientific evidence of stronger El Niño events and the lack of action.

**Tags**: `#climate change`, `#El Niño`, `#ocean temperature`, `#environment`

---

<a id="item-7"></a>
## [Tencent Compresses Hy4-preview to 200GB GGUF, Retaining 98% Performance](https://www.reddit.com/r/LocalLLaMA/comments/1w1o324/tencent_compressed_hy4preview_from_15tb_to_about/) ⭐️ 8.0/10

Tencent has compressed its Hy4-preview model from 1.5TB to approximately 200GB using the GGUF format, while retaining about 98% of the original performance. This significant reduction in size enables more practical local deployment of a 770B-parameter MoE model. This achievement is significant because it demonstrates that massive models can be made deployable on consumer hardware without substantial performance loss, potentially democratizing access to state-of-the-art AI. It could influence how other large model developers approach compression and local deployment strategies. Hy4-preview is a Mixture-of-Experts (MoE) model with 770B total parameters, of which 49B are activated per token. The compression likely leverages Tencent's AngelSlim toolkit, which supports various quantization algorithms for large-scale multimodal models, and the GGUF format enables efficient CPU/GPU hybrid inference.

reddit · r/LocalLLaMA · /u/RedditUsr2 · Aug 29, 14:31

**Background**: GGUF is a file format designed for efficient storage and inference of quantized language models, commonly used with llama.cpp for local deployment. Model compression techniques like quantization reduce the precision of weights to shrink file size, trading a small amount of accuracy for significant memory savings. Tencent's Hy4-preview is a recent open-weights model, and this compression makes it feasible to run on devices with limited memory.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Tencent-Hunyuan/Hy4-preview">GitHub - Tencent-Hunyuan/Hy4-preview</a></li>
<li><a href="https://www.modelscope.cn/models/Tencent-Hunyuan/Hy4-preview">Hy4-preview · Models</a></li>
<li><a href="https://aiengineering.academy/Deployment/Quantization/GGUF_Quantization/">GGUF - AI Engineering Academy</a></li>

</ul>
</details>

**Tags**: `#model compression`, `#GGUF`, `#LLM`, `#efficiency`, `#Tencent`

---

<a id="item-8"></a>
## [Nemotron-3.5-Lightning Gets 16GB GGUF via ShimQuant](https://www.reddit.com/r/LocalLLaMA/comments/1w21d86/nemotron35lightning_at_1177_gib_a_16_gb_option/) ⭐️ 8.0/10

A new quantization method called ShimQuant enables a true 3.07 bpw GGUF of NVIDIA Nemotron-3.5-Lightning-30B-A3B at 11.77 GiB, fitting on 16GB GPUs. This requires a patched llama.cpp and is not compatible with stock llama.cpp, LM Studio, or Ollama. This provides the first usable sub-18 GiB option for running Nemotron-3.5-Lightning on 16GB hardware, addressing a significant gap. It also highlights a broader quantizer bug affecting many models, prompting community awareness and potential fixes. The quantizer bug causes k-quants and i-quants to silently fall back to ~4.70 bpw when row widths are not divisible by 256, as in Nemotron. ShimQuant pads rows to multiples of 256 at quantization time and slices activations back at inference, achieving 3.07 bpw with only 9.4% overhead for expert banks.

reddit · r/LocalLLaMA · /u/Daxfortuna · Aug 29, 23:27

**Background**: GGUF quantization methods like k-quants and i-quants require tensor row counts to be multiples of 256. When a model violates this, llama-quantize silently falls back to a default format (often Q4_K_S) while keeping the requested filename, leading to mislabeled files. ShimQuant addresses this by padding rows, enabling true low-bit quantization for such models.

<details><summary>References</summary>
<ul>
<li><a href="https://baguaai.com/the-gguf-quantization-trap-audit-reveals-14-of-models-mislabeled-due-to-silent-fallback/">The GGUF Quantization Trap: Audit Reveals 14% of Models ...</a></li>
<li><a href="https://huggingface.co/BoldingBuilds/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-ShimQuant-GGUF">BoldingBuilds/NVIDIA-Nemotron-3.5-Lightning-30B-A3B- ShimQuant ...</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/5063">Even more quantization types? #5063 - ggml-org llama.cpp - GitHub</a></li>

</ul>
</details>

**Discussion**: The community discussion likely includes technical validation of the bug and the ShimQuant solution, with some users expressing interest in testing the new file. Others may raise concerns about the need for a patched llama.cpp and the lack of support in popular tools like LM Studio and Ollama.

**Tags**: `#quantization`, `#llama.cpp`, `#GGUF`, `#Nemotron`, `#local-llm`

---

<a id="item-9"></a>
## [Sopro V2 Turbo: 120M Voice Cloning TTS, 5x Real-Time on CPU](https://www.reddit.com/r/StableDiffusion/comments/1w1z4sh/we_opensourced_sopro_v2_turbo_a_120m_voice/) ⭐️ 8.0/10

The Sopro V2 Turbo model, a 120M-parameter open-source voice cloning TTS, has been released, running 5x faster than real time on CPU. It includes a local web UI, Python API, and WebGPU/WASM browser support. This open-sourcing makes high-quality voice cloning accessible to a broad audience, enabling private, on-device TTS without cloud dependencies. Its small size and CPU efficiency could spur innovation in edge AI and privacy-focused applications. The model supports English, European Portuguese, French, and German, and can clone a voice from 5-20 seconds of audio with ~300ms to first audio on a laptop CPU. It is available via GitHub, with a Hugging Face Space for easy testing.

reddit · r/StableDiffusion · /u/SammyDaBeast · Aug 29, 21:51

**Background**: Text-to-speech (TTS) models convert text into spoken audio, and voice cloning adapts the output to mimic a specific speaker's voice. Traditional TTS models are often large and require cloud GPUs, but Sopro V2 Turbo's 120M parameters and CPU-friendly design enable local, real-time inference. WebGPU and WASM technologies allow the model to run directly in browsers, enhancing accessibility.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/samuel-vitorino/sopro">GitHub - samuel-vitorino/sopro: A lightweight text-to-speech ...</a></li>
<li><a href="https://research.haloneuro.ai/posts/sopro-v2">Sopro V2: private, fast, on-device text-to-speech · Halo Research</a></li>
<li><a href="https://github.com/kraigjacobson/sopro">GitHub - kraigjacobson/sopro: sopro-v2-turbo TTS packaged as ...</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#voice cloning`, `#open-source`, `#AI/ML`, `#CPU inference`

---

<a id="item-10"></a>
## [HR Endless Sampler Enables Arbitrary-Length Minimax H3 Videos on 16GB VRAM](https://www.reddit.com/r/StableDiffusion/comments/1w25d7g/hr_endless_sampler_now_you_can_create_minimax_h3/) ⭐️ 8.0/10

A new ComfyUI custom node, HR Endless Sampler, allows generating Minimax H3 videos of any length using only 16GB of VRAM. It splits the video into chunks and uses Gemma 4 12B QAT to maintain prompt continuity across chunks. This significantly lowers the barrier for creating long-form AI videos, as previous limits (e.g., 15 seconds for MiniMax H3) and high VRAM requirements are overcome. It empowers creators with consumer GPUs to produce extended, coherent video content, potentially accelerating adoption in filmmaking and content creation. The node automatically attaches the last frames of the previous chunk for video continuation, and Gemma acts as a 'chunk director' to split and time the overall prompt, ensuring each chunk's action matches the intended timeline. It also includes custom preview, save, and load nodes, with EXR support for floating-point color preservation.

reddit · r/StableDiffusion · /u/rhradec · Aug 30, 02:36

**Background**: MiniMax H3 is an open omni-modal generative model that can generate video with native stereo audio at up to 2K resolution and 15 seconds in length. ComfyUI is a node-based interface for AI image and video generation, where custom nodes extend its functionality. Gemma 4 12B QAT is a quantized version of Google's Gemma 4 model, optimized for lower memory usage while maintaining quality.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/MiniMax-AI/MiniMax-H3">GitHub - MiniMax-AI/MiniMax-H3 · GitHub</a></li>
<li><a href="https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-unquantized">google/gemma-4-12B-it-qat-q4_0-unquantized · Hugging Face</a></li>
<li><a href="https://comfyui-wiki.com/en/comfyui-nodes/sampling/sampler">Sampler - ComfyUI Wiki</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely includes positive feedback on the practical solution, questions about implementation details, and reports of the known 'hiccup' where Gemma mislabeled a shot. Users may also discuss the trade-offs of chunking and the potential for even higher resolutions with more VRAM.

**Tags**: `#AI video generation`, `#ComfyUI`, `#Minimax H3`, `#VRAM optimization`, `#Open source`

---

<a id="item-11"></a>
## [Fizgig v5 Enables Full Fine-Tuning of MiniMax H3 and Krea 2 on 16GB GPUs](https://www.reddit.com/r/StableDiffusion/comments/1w1ple8/fizgig_v500_full_finetuning_for_minimax_and_krea/) ⭐️ 8.0/10

Fizgig v5.0.0, released on August 29, introduces full fine-tuning of the MiniMax H3 (33B) and Krea 2 (12.9B) base models on consumer GPUs with as little as 16GB VRAM, using a rotating window technique and 4-bit frozen layers. This replaces the previous LoRA-only approach, allowing full-rank updates to the model weights. This is a significant advancement because it enables full fine-tuning of large multimodal models on consumer hardware, previously requiring high-end GPUs or cloud resources. It democratizes access to model customization, allowing individual developers and researchers to adapt state-of-the-art video and image models to their specific needs without rank bottlenecks. The technique trains only one slice of the model at a time (rotating window), keeps the frozen parts in 4-bit precision, and stores the bf16 master weights in system RAM. Measured peak VRAM usage on a 16GB card is 8.8–12.3GB for H3 and 8.4–11.0GB for Krea 2, with video training confirmed up to 2.3 seconds for H3 on 16GB and up to 3.8 seconds on 32GB. A built-in Checkpoint-to-LoRA tool extracts a shareable LoRA (rank 64) that is nearly indistinguishable from the full checkpoint.

reddit · r/StableDiffusion · /u/shootthesound · Aug 29, 15:32

**Background**: MiniMax H3 is an open-weights, general-purpose multimodal model that can generate 2K video with native stereo audio up to 15 seconds, while Krea 2 is a foundation image model known for its wide creative range. Traditionally, fine-tuning such large models required either high-end GPUs with large VRAM or the use of parameter-efficient methods like LoRA, which limit the model's capacity to learn new concepts. Fizgig is an open-source tool (Apache-2.0) that provides a training pipeline for these models, and this release marks a shift from LoRA-only training to full fine-tuning on consumer hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://comfyui-wiki.com/en/news/2026-08-30-fizgig-v5-full-finetuning">Fizgig v5 Full Fine - Tuning : Train MiniMax H3 and Krea... | ComfyUI Wiki</a></li>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between Tasks and Modalities - MiniMax Research | MiniMax</a></li>
<li><a href="https://fal.ai/minimax-h3">MiniMax H3 - Open-Weights General-Purpose Multimodal Video Model | fal</a></li>

</ul>
</details>

**Discussion**: The community discussion is not provided in the input, so no specific comments are available. However, based on the post's tone and the technical nature, the community likely shows excitement and curiosity about the technique, with questions about implementation details and validation of the reported numbers.

**Tags**: `#fine-tuning`, `#video generation`, `#consumer GPU`, `#MiniMax`, `#Krea`

---

<a id="item-12"></a>
## [100-Year-Old SPC Algorithm Beats SOTA on TSB-AD Benchmark](https://www.reddit.com/r/MachineLearning/comments/1w1wt1s/you_can_beat_sota_time_series_anomaly_detection/) ⭐️ 8.0/10

A researcher, Eamonn Keogh, demonstrated that a simple 100-year-old Statistical Process Control (SPC) algorithm outperforms state-of-the-art time series anomaly detection methods on the TSB-AD benchmark, achieving perfect results on some ECG traces. He argues that the benchmark is too trivial to support meaningful claims of progress. This critique challenges the validity of the widely used TSB-AD benchmark, suggesting that many recent papers in time series anomaly detection may be overfitting to trivial benchmarks. It calls for introspection in the community and could lead to more rigorous evaluation standards. The author provides examples, including ECG traces and 'TAO' traces, which are trivially solved by SPC. He also mentions he has done 90% of the work to introduce more challenging TSAD problems, such as sled dogs, Tuna, Fuel Cells, and Smart Manufacturing datasets.

reddit · r/MachineLearning · /u/eamonnkeogh · Aug 29, 20:16

**Background**: Time Series Anomaly Detection (TSAD) is a hot topic in conferences like NeurIPS, SIGKDD, and VLDB. The TSB-AD benchmark, introduced by Paparrizos et al., is commonly used for evaluation. Statistical Process Control (SPC) is a classical method for monitoring process stability, using control charts to detect anomalies.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/TheDatumOrg/TSB-AD">GitHub - thedatumorg/TSB-AD: Time-Series Anomaly Detection ...</a></li>
<li><a href="https://thedatumorg.github.io/TSB-AD/">TSB-AD - thedatumorg.github.io</a></li>
<li><a href="https://www.sciencedirect.com/topics/engineering/statistical-process-control">sciencedirect.com/topics/engineering/ statistical - process - control</a></li>

</ul>
</details>

**Tags**: `#time series`, `#anomaly detection`, `#benchmarking`, `#machine learning`, `#research critique`

---

<a id="item-13"></a>
## [LLM Benchmark Scores Show 3x More Variation Between Days Than Within a Day](https://www.reddit.com/r/MachineLearning/comments/1w1jp1j/i_analyzed_31352_hourly_llm_benchmark_scores/) ⭐️ 8.0/10

An analysis of 31,352 hourly LLM benchmark scores found within-day variation of 2.8 points and between-day variation of 8.4 points, indicating that between-day variation is approximately 3 times greater. The study was conducted using the open-source AIStupidLevel system, which continuously evaluates models across coding, reasoning, tool calling, and canary tasks. This finding highlights the importance of temporal stability in LLM evaluation, as single-point measurements may be misleading. It provides empirical evidence that sustained performance changes across days are a stronger signal for detecting model drift, which is crucial for production LLM monitoring and selection. The analysis used a normalized 0-100 composite score, with coding responses executed and tool-calling tests run in isolated Docker environments. Tasks were executed five times and aggregated to reduce stochastic variation, and the detection pipeline uses daily medians and sequential change-point detection with statistical and minimum-effect thresholds.

reddit · r/MachineLearning · /u/ionutvi · Aug 29, 11:08

**Background**: LLM benchmarks typically measure performance at a single point in time, but production APIs may exhibit performance drift over time due to model updates, load, or other factors. Temporal evaluation aims to distinguish sustained changes from stochastic variation, which is essential for reliable model monitoring. The AIStupidLevel system, developed by the author, provides continuous benchmarking and drift detection, and its dataset has grown to over 169,000 runs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2406.09170">Test of Time: A Benchmark for Evaluating LLMs on Temporal ... Test of Time: Benchmarking LLMs on Temporal Reasoning Test of Time: A Benchmark for Evaluating LLMs on Temporal ... Test of Time: A Benchmark for Evaluating LLMs on Temporal ... Testing Time: Assessing LLM Performance on Time-Series ... EvolveBench: A Comprehensive Benchmark for Assessing Temporal ...</a></li>
<li><a href="https://huggingface.co/AIStupidLevel">AIStupidLevel (AI Stupid Level) - Hugging Face</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#benchmarking`, `#evaluation`, `#stability`, `#time-series`

---

<a id="item-14"></a>
## [Google's SKILL.state cuts agent token use by 94% in long sessions](https://www.reddit.com/r/artificial/comments/1w1ynrf/google_paper_cuts_agent_token_usage_by_94_in_long/) ⭐️ 8.0/10

Google researchers introduced SKILL.state, a method that replaces conversation history with a structured state representation, reducing token usage by 94% in a 100-step benchmark while maintaining comparable accuracy (0.94 vs 0.91). This breakthrough significantly lowers the cost and latency of long-running AI agent sessions, making them more scalable and practical for real-world applications. It addresses a major bottleneck in agentic AI, where token consumption grows rapidly with each step. The method was tested with Gemini-3-Flash on a 100-step benchmark: SKILL.state used 65k tokens versus 1.1M tokens for a LangGraph-style baseline. A caveat is that the agent must anticipate future information needs; otherwise, it may need to re-retrieve information.

reddit · r/artificial · /u/hakansan · Aug 29, 21:31

**Background**: AI agents typically maintain conversation history as part of their input, causing token usage to grow linearly with session length. SKILL.state instead maintains a structured state that the agent updates with useful information, discarding history. This approach is architecture-agnostic and has been validated across multiple datasets and models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.26263v1">SKILL.state: Scalable Long-Horizon Agent Skills - arXiv.org</a></li>
<li><a href="https://hackernoon.com/most-ai-agent-failures-arent-model-problems-theyre-architecture-problems">Most AI Agent Failures Aren't Model Problems, They're... | HackerNoon</a></li>
<li><a href="https://www.neura.market/blog/agentic-ai-token-use-jumps-14x-what-it-means-for-your-workflows">Agentic AI Token Use Jumps 14x: What It Means for... | Neura Market</a></li>

</ul>
</details>

**Discussion**: Reddit commenters generally praised the efficiency gain but noted the caveat about the agent's ability to predict future needs. Some questioned the benchmark's realism and whether the accuracy difference is significant, while others saw it as a promising direction for reducing agent costs.

**Tags**: `#AI agents`, `#token efficiency`, `#LLM`, `#state management`, `#Google research`

---

<a id="item-15"></a>
## [OpenAI to Cut Off Model Supply to Cursor After SpaceX Acquisition](https://www.reddit.com/r/artificial/comments/1w1w7f9/openai_plans_to_stop_supplying_models_to_cursor/) ⭐️ 8.0/10

OpenAI announced it will wind down its contract supplying models to Cursor, with a proposed shutoff date of November 12, 2026, citing a limited cancellation window triggered by Cursor's change of control after SpaceX's acquisition. Reuters reports that Anthropic plans to increase compute support for Claude models in Cursor. This move highlights the dependency risk in AI coding tools, as a model provider can change access after ownership or contract changes. It also intensifies competition between OpenAI and Anthropic in the AI coding market, with Cursor potentially shifting more toward Claude models. OpenAI's custom agreement with Cursor includes a limited time window to cancel after a change of control, and OpenAI also cites accountability for its upcoming model, Astra. Cursor co-founder Michael Truell said the companies were speaking to resolve the issue, while SpaceX acquired Cursor for $60 billion.

reddit · r/artificial · /u/Codeblix_Ltd · Aug 29, 19:52

**Background**: Cursor is an AI-powered code editor that integrates with various large language models to assist developers. OpenAI is a major provider of such models, and its decision to withdraw from Cursor after SpaceX's acquisition reflects the strategic and competitive dynamics between Elon Musk and Sam Altman. Anthropic, a rival AI company, offers Claude models that are also used in coding tools.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/">Our decision on Cursor following its acquisition by SpaceX | OpenAI</a></li>
<li><a href="https://www.businessinsider.com/openai-ends-cursor-contract-elon-musk-spacex-sam-altman-feud-2026-8">OpenAI Ending Deal With Cursor Because XAI... - Business Insider</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely includes comments about the Elon vs. Altman feud and its real consequences, with users debating the implications for Cursor users and the broader AI tooling ecosystem. Some may express concerns about dependency on single model providers, while others see it as a competitive opportunity for Anthropic.

**Tags**: `#OpenAI`, `#Cursor`, `#AI coding tools`, `#industry news`, `#dependency risk`

---