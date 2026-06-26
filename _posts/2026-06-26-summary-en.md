---
layout: default
title: "Horizon Summary: 2026-06-26 (EN)"
date: 2026-06-26
lang: en
---

> From 147 items, 15 important content pieces were selected

---

1. [First Full Herculaneum Scroll Read Using AI](#item-1) ⭐️ 9.0/10
2. [Wan-Streamer v0.1: Real-Time Audio-Visual Foundation Model](#item-2) ⭐️ 9.0/10
3. [817 Cybersecurity Skills Mapped for AI Agents](#item-3) ⭐️ 8.0/10
4. [Google Labs Releases DESIGN.md Spec for Coding Agents](#item-4) ⭐️ 8.0/10
5. [Systematic Study of LLM Agent Memory Systems](#item-5) ⭐️ 8.0/10
6. [IBM Announces Sub-1nm Chip Technology at 0.7nm Node](#item-6) ⭐️ 8.0/10
7. [Oral History of Bank Python: Custom Systems in Investment Banks](#item-7) ⭐️ 8.0/10
8. [Zig's New bitCast Semantics and LLVM Backend Improvements](#item-8) ⭐️ 8.0/10
9. [German Court Holds Google Liable for AI Overview Errors](#item-9) ⭐️ 8.0/10
10. [OpenAI Reports Surge in Internal Codex Token Usage Across Departments](#item-10) ⭐️ 8.0/10
11. [Anthropic accuses Alibaba of massive Claude AI cloning attack](#item-11) ⭐️ 8.0/10
12. [US Government to Individually Approve GPT-5.6 Access](#item-12) ⭐️ 8.0/10
13. [audio.cpp: 12 Audio Models in One C++/ggml Runtime, Up to 5x Faster](#item-13) ⭐️ 8.0/10
14. [JetSpec: Up to 9.64x LLM Speedup via Parallel Tree Drafting](#item-14) ⭐️ 8.0/10
15. [NVIDIA Releases Diffusion-Based Language Model Nemotron-TwoTower](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [First Full Herculaneum Scroll Read Using AI](https://scrollprize.org/firstscroll) ⭐️ 9.0/10

For the first time, an entire Herculaneum scroll has been read using AI and machine learning techniques, unlocking ancient Greek texts preserved by the eruption of Mount Vesuvius in AD 79. This breakthrough demonstrates that AI can unlock vast amounts of ancient literature previously thought lost, potentially transforming our understanding of classical philosophy, history, and daily life. The scroll was read as part of the Vesuvius Challenge, using high-resolution CT scans and machine learning models to detect ink and digitally unwrap the carbonized papyrus. The team also unwrapped 140 columns of new text from another scroll, PHerc.Paris.4.

hackernews · verditelabs · Jun 25, 15:48 · [Discussion](https://news.ycombinator.com/item?id=48675179)

**Background**: The Herculaneum papyri are a collection of about 1,100 carbonized scrolls buried by the eruption of Mount Vesuvius in AD 79. They are too fragile to unroll physically, but modern X-ray imaging and AI can now read the text without damaging them. The Vesuvius Challenge, launched in 2023, offered prizes for the first team to read a scroll using these techniques.

<details><summary>References</summary>
<ul>
<li><a href="https://greekreporter.com/2026/06/26/herculaneum-scroll-complete-text-ai/">Herculaneum Scroll's Complete Text Deciphered Using AI After ...</a></li>
<li><a href="https://www.theregister.com/offbeat/2026/06/25/they-read-the-scroll-thing-ai-helps-decipher-ancient-document-charred-by-vesuvius/5262525">They read the scroll thing! AI helps decipher ancient ...</a></li>
<li><a href="https://www2.cs.uky.edu/dri/herculaneum-papyrus-scrolls/">Herculaneum Papyrus Scrolls - Digital Restoration Initiative</a></li>

</ul>
</details>

**Discussion**: Community members expressed awe at the achievement, with one noting the profound time scale from ancient author to modern AI reader. A team member offered to answer questions about segmentation and ink detection, while another highlighted that only 20% of the Herculaneum site has been excavated, suggesting many more scrolls await discovery.

**Tags**: `#AI`, `#machine learning`, `#archaeology`, `#digital humanities`, `#computer vision`

---

<a id="item-2"></a>
## [Wan-Streamer v0.1: Real-Time Audio-Visual Foundation Model](https://huggingface.co/papers/2606.25041) ⭐️ 9.0/10

Wan-Streamer v0.1 is a native-streaming, end-to-end foundation model that enables real-time, full-duplex audio-visual interaction using a single Transformer with block-causal attention, achieving approximately 200 ms model-side latency and 550 ms total interaction latency. This model eliminates the need for cascaded modules like VAD, ASR, TTS, and video generation, reducing pipeline latency and error accumulation, and represents a paradigm shift toward unified multimodal interactive AI systems. Wan-Streamer uses block-causal attention to coordinate interleaved visual, audio, and text tokens for incremental streaming, with streaming units as short as 160 ms at 25 fps, and supports full-duplex communication with sub-second latency.

huggingface_papers · Hugging Face Papers · Jun 25, 00:00

**Background**: Traditional interactive AI systems rely on separate modules for voice activity detection (VAD), automatic speech recognition (ASR), language understanding, text-to-speech (TTS), and video generation, leading to high latency and error accumulation. Block-causal attention is a variant of causal attention that processes input in blocks, enabling efficient streaming inference. Full-duplex interaction means both parties can send and receive data simultaneously, as in natural conversation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/block-wise-causal-attention">Block-wise Causal Attention</a></li>
<li><a href="https://arxiv.org/abs/2605.30256">[2605.30256] VideoFDB: Evaluating Full-Duplex Vision-Speech ...</a></li>
<li><a href="https://github.com/QwenLM/Qwen3-Omni">GitHub - QwenLM/Qwen3-Omni: Qwen3-omni is a natively end-to ...</a></li>

</ul>
</details>

**Tags**: `#multimodal`, `#real-time interaction`, `#foundation model`, `#audio-visual`, `#transformer`

---

<a id="item-3"></a>
## [817 Cybersecurity Skills Mapped for AI Agents](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10

Mukul975 released a GitHub repository mapping 817 structured cybersecurity skills to six major frameworks (MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF, MITRE F3) using the agentskills.io standard, compatible with 20+ AI platforms. This repository provides a comprehensive, standardized skill set that enables AI agents to perform cybersecurity tasks across multiple platforms, significantly reducing integration effort and promoting interoperability in the AI security ecosystem. The repository covers 29 security domains, is written in Python, and is licensed under Apache 2.0. It has gained over 21,000 stars and 2,400 forks, indicating strong community validation.

github_trending · GitHub Trending · Jun 26, 03:51

**Background**: The agentskills.io standard is an open specification for defining AI agent capabilities, ensuring portability across platforms like Claude Code, GitHub Copilot, and Cursor. MITRE frameworks such as ATT&CK and D3FEND are widely used for categorizing offensive and defensive cybersecurity techniques, while MITRE ATLAS focuses on AI-specific threats.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/agentskills/agentskills">GitHub - agentskills/agentskills: Specification and documentation for Agent Skills · GitHub</a></li>
<li><a href="https://atlas.mitre.org/">MITRE ATLAS™</a></li>
<li><a href="https://d3fend.mitre.org/">D3FEND Matrix | MITRE D3FEND™</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#AI agents`, `#MITRE ATT&CK`, `#NIST CSF`, `#open source`

---

<a id="item-4"></a>
## [Google Labs Releases DESIGN.md Spec for Coding Agents](https://github.com/google-labs-code/design.md) ⭐️ 8.0/10

Google Labs has released DESIGN.md, a format specification that provides coding agents with a persistent, structured understanding of a design system. The repository on GitHub has gained over 1475 stars in a single day. This specification bridges the gap between design systems and AI-assisted development, enabling coding agents to consistently apply visual identity rules. It could significantly improve the quality and consistency of AI-generated user interfaces. DESIGN.md is a plain-text file that combines machine-readable design tokens with human-readable design rationale, serving as a living source of truth. The repository is written in TypeScript and has accumulated nearly 20,000 stars.

github_trending · GitHub Trending · Jun 26, 03:51

**Background**: Coding agents are AI systems that autonomously write or modify code based on instructions. Design systems are collections of reusable components and guidelines that ensure visual consistency. DESIGN.md acts as a bridge, giving agents a structured reference to a project's visual identity.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/google-labs-code/design.md">GitHub - google-labs-code/design.md: A format specification ...</a></li>
<li><a href="https://github.com/google-labs-code/design.md/blob/main/docs/spec.md">design.md/docs/spec.md at main · google-labs-code ... - GitHub</a></li>
<li><a href="https://deepwiki.com/google-labs-code/design.md/2-the-design.md-format">The DESIGN.md Format | google-labs-code/design.md | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#design systems`, `#AI-assisted development`, `#TypeScript`, `#specification`, `#Google Labs`

---

<a id="item-5"></a>
## [Systematic Study of LLM Agent Memory Systems](https://huggingface.co/papers/2606.24775) ⭐️ 8.0/10

This paper presents a systematic experimental study of LLM agent memory from a data management perspective, decomposing memory into four core modules and evaluating 12 representative systems across five workloads. It reveals that no single memory architecture dominates all scenarios and highlights the need for system-level performance analysis beyond end-to-end task metrics, guiding the design of truly agent-native memory systems. The framework includes memory representation and storage, extraction, retrieval and routing, and maintenance modules. Fine-grained ablation studies quantify effects on representation fidelity, retrieval precision, update correctness, and long-horizon stability.

huggingface_papers · Hugging Face Papers · Jun 25, 00:00

**Background**: LLM agent memory has evolved from simple retrieval-augmented generation (RAG) into complex data management systems supporting persistent storage, retrieval, update, consolidation, and lifecycle governance. Existing evaluations often treat memory as a black box, focusing only on end-to-end task success metrics like F1 or BLEU.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.12110">[2502.12110] A-MEM: Agentic Memory for LLM Agents</a></li>
<li><a href="https://github.com/neo4j-labs/agent-memory">GitHub - neo4j-labs/agent-memory: A graph-native memory system for AI agents and context graphs. Store conversations, build knowledge graphs, and let your agents learn from their own reasoning — all backed by Neo4j.</a></li>
<li><a href="https://github.com/MemoriLabs/Memori">GitHub - MemoriLabs/Memori: Memori is agent-native memory infrastructure. A LLM-agnostic layer that turns agent execution and conversation into structured, persistent state for production systems. · GitHub</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#memory systems`, `#system evaluation`, `#AI/ML`, `#data management`

---

<a id="item-6"></a>
## [IBM Announces Sub-1nm Chip Technology at 0.7nm Node](https://newsroom.ibm.com/2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology) ⭐️ 8.0/10

IBM has announced the world's first sub-1 nanometer chip technology, featuring a 0.7nm (7 angstrom) node that packs nearly 100 billion transistors, roughly double the density of its 2nm chip from 2021. This breakthrough demonstrates that transistor scaling can continue into the angstrom era, potentially boosting performance and energy efficiency for AI data centers and other advanced computing applications. The node name '0.7nm' no longer corresponds to any physical dimension on the chip; it instead indicates a generational improvement in density and performance. IBM's technology uses nanostack transistors to achieve the density increase.

hackernews · porridgeraisin · Jun 25, 15:33 · [Discussion](https://news.ycombinator.com/item?id=48674967)

**Background**: In semiconductor manufacturing, node names originally referred to the smallest feature size, but since around the 5nm node, the name has become a marketing term denoting a generation of technology. The industry continues to shrink transistors to improve performance and efficiency, though physical dimensions no longer match node labels.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/gadgets/2026/06/ibm-claims-worlds-first-sub-1-nanometer-chip-technology/">IBM claims world’s first sub - 1 nanometer chip technology</a></li>
<li><a href="https://www.networkworld.com/article/4189510/ibm-unveils-sub-1-nanometer-chip-with-nearly-100-billion-transistors.html">IBM unveils sub - 1 nanometer chip with nearly 100... | Network World</a></li>
<li><a href="https://en.wikipedia.org/wiki/5_nm_process">5 nm process - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism about IBM's claims, noting that node names are decoupled from physical dimensions and that IBM has a history of exaggerated marketing. Some users point out that the 0.7nm label refers to density improvements rather than actual feature sizes, and one commenter links to a detailed technical analysis.

**Tags**: `#semiconductors`, `#chip manufacturing`, `#nanometer scaling`, `#IBM`, `#hardware`

---

<a id="item-7"></a>
## [Oral History of Bank Python: Custom Systems in Investment Banks](https://calpaterson.com/bank-python.html) ⭐️ 8.0/10

An oral history article published in 2021 details the unique, custom Python-based systems used in major investment banks, tracing their origins and evolution. This article reveals a hidden world of software archaeology in finance, showing how banks built proprietary Python ecosystems to meet high-performance trading needs, which contrasts with modern open-source trends. Systems like Goldman Sachs' SecDB/Slang, JPMorgan's Athena, and Barclays' Barbara are discussed, with some code stored in custom object stores rather than on disk.

hackernews · tosh · Jun 25, 20:14 · [Discussion](https://news.ycombinator.com/item?id=48678645)

**Background**: Investment banks have long used Python for rapid prototyping and trading systems, but many developed proprietary forks and custom runtimes to avoid dependency on external OS updates and to achieve low latency. These systems often predate modern open-source solutions, leading to unique in-house architectures.

<details><summary>References</summary>
<ul>
<li><a href="https://calpaterson.com/bank-python.html">An oral history of Bank Python</a></li>
<li><a href="https://www.reddit.com/r/programming/comments/rbvpmy/bank_python_the_strange_world_of_python_as_used/">r/programming on Reddit: Bank Python: The strange world of Python, as used by big investment banks</a></li>

</ul>
</details>

**Discussion**: Commenters provide firsthand accounts, noting that many bank Python systems originated from Goldman's SecDB/Slang, and that attempts to rewrite such systems in smaller hedge funds can be frustrating. They also highlight that custom solutions were often built because mature off-the-shelf alternatives did not exist at the time.

**Tags**: `#Python`, `#banking`, `#software archaeology`, `#finance`, `#history`

---

<a id="item-8"></a>
## [Zig's New bitCast Semantics and LLVM Backend Improvements](https://ziglang.org/devlog/2026/#2026-06-25) ⭐️ 8.0/10

Zig's latest devlog introduces endian-agnostic bitCast semantics and improvements to the LLVM backend, including better incremental compilation. The new bitCast semantics ensure consistent behavior across all target endiannesses when converting between aggregate types like arrays and integers. This change simplifies bit-packed data handling in Zig, making it easier to work with binary headers and protocols without manual endianness management. The LLVM backend improvements enhance compilation performance and developer experience. The new semantics treat bitCast as operating on logical bit representations, making operations like casting [2]u8 to u16 endian-agnostic. The LLVM backend improvements focus on incremental compilation, reducing recompilation times.

hackernews · kouosi · Jun 25, 14:19 · [Discussion](https://news.ycombinator.com/item?id=48673825)

**Background**: Endianness refers to the order of bytes in a multi-byte value; big-endian stores the most significant byte first, while little-endian stores the least significant byte first. Zig's packed structs allow bit-level field packing, and bitCast is used to reinterpret data between types. The LLVM backend is responsible for generating machine code from Zig's intermediate representation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Endianness">Endianness - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/LLVM">LLVM - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members praised the detailed devlog, with zamadatix noting the change will be great for working with bit-packed binary headers. Some commenters discussed the trade-offs of arbitrary-width integers, while others expressed enthusiasm for Zig's technical direction.

**Tags**: `#Zig`, `#compiler`, `#LLVM`, `#systems programming`, `#bit manipulation`

---

<a id="item-9"></a>
## [German Court Holds Google Liable for AI Overview Errors](https://simonwillison.net/2026/Jun/25/ai-and-liability/#atom-everything) ⭐️ 8.0/10

A German court ruled that Google is directly liable for false statements in its AI Overviews, treating them as Google's own words rather than third-party content. Bruce Schneier argues that AI agents should be legally considered agents of their deployers. This landmark ruling sets a precedent for AI liability, potentially forcing companies to ensure accuracy of AI-generated content or face legal consequences. It challenges the notion that AI errors can be dismissed as unavoidable, promoting accountability in AI deployment. The German court distinguished AI Overviews from traditional search snippets, noting that AI can fabricate claims from multiple sources, thus the safe harbor for search engines does not apply. Google has announced it will appeal the ruling.

rss · Simon Willison · Jun 25, 22:28

**Background**: AI overviews are summaries generated by large language models that appear at the top of search results. Unlike traditional search snippets that quote existing web pages, AI overviews can produce entirely new statements, sometimes inaccurate or hallucinated. Previous laws protected search engines from liability for third-party content, but this ruling challenges that protection for AI-generated content.

<details><summary>References</summary>
<ul>
<li><a href="https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/">Landmark German ruling declares Google's AI Overviews are Google's own words and makes it liable for false answers</a></li>
<li><a href="https://www.wired.com/story/a-court-has-ruled-that-google-is-liable-for-false-statements-generated-by-ai-overviews/">A Court Has Ruled That Google Is Liable for False Statements Generated by AI Overviews | WIRED</a></li>
<li><a href="https://www.reuters.com/world/google-appeal-german-court-ruling-assigning-liability-ai-overviews-false-claims-2026-06-12/">Google to challenge German ruling saying it is liable for AI-generated false claims | Reuters</a></li>

</ul>
</details>

**Tags**: `#AI`, `#liability`, `#law`, `#ethics`, `#regulation`

---

<a id="item-10"></a>
## [OpenAI Reports Surge in Internal Codex Token Usage Across Departments](https://www.latent.space/p/ainews-openai-reports-median-internal) ⭐️ 8.0/10

OpenAI reported that median internal Codex output tokens grew 56x in Research, 32x in Customer Support, 27x in Engineering, and 13x in Legal since November 2025. This data demonstrates accelerating real-world adoption of AI coding agents across diverse enterprise functions, signaling a shift in how organizations leverage AI for productivity gains beyond traditional software development. The growth spans non-engineering departments like Legal and Customer Support, indicating Codex is being used for tasks beyond code generation, such as document analysis and workflow automation.

rss · Latent Space · Jun 26, 01:12

**Background**: OpenAI Codex is a suite of AI-driven coding agents that can read, edit, and run code, helping developers build faster and squash bugs. It has over 5 million weekly active users as of mid-2026, with non-developer users growing 189x since August 2025. The token-based pricing model measures usage via input, cached input, and output tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/codex/pricing">Pricing – Codex | OpenAI Developers</a></li>
<li><a href="https://icharles.com/articles/openai-codex-agentic-work-study">OpenAI Codex: 99.8% of Worker Tokens in 2026 - icharles.com</a></li>
<li><a href="https://github.com/openai/codex">GitHub - openai / codex : Lightweight coding agent that runs in your...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#OpenAI`, `#Codex`, `#productivity`, `#enterprise`

---

<a id="item-11"></a>
## [Anthropic accuses Alibaba of massive Claude AI cloning attack](https://arstechnica.com/tech-policy/2026/06/anthropic-claims-alibaba-defied-trump-to-attack-claude-and-steal-capabilities/) ⭐️ 8.0/10

Anthropic has accused Alibaba of orchestrating the largest known AI model extraction attack, using 25,000 accounts and 28.8 million queries to clone its Claude AI model. This incident highlights the growing threat of AI model theft, with significant implications for intellectual property protection and geopolitical tensions between US and Chinese tech firms. The attack allegedly involved 25,000 accounts and 28.8 million exchanges, making it the largest known model extraction attack. Anthropic claims Alibaba defied Trump administration policies in carrying out the operation.

rss · Ars Technica AI · Jun 25, 18:01

**Background**: Model extraction attacks involve querying a proprietary AI model's public API to collect input-output pairs, which are then used to train a surrogate model that mimics the original. Such attacks threaten the intellectual property and competitive advantage of AI companies like Anthropic, which invest heavily in developing advanced models like Claude.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/06/anthropic-claims-alibaba-defied-trump-to-attack-claude-and-steal-capabilities/">Anthropic says Alibaba must be punished for largest Claude ...</a></li>
<li><a href="https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/">Anthropic says Alibaba illicitly extracted Claude AI model ...</a></li>
<li><a href="https://cybersecuritytimes.com/anthropic-accuses-alibaba-of-illicitly-accessing/">Anthropic Accuses Alibaba of “Illicitly” Accessing Its Claude ...</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is not available, but the news has sparked debate about the scale of the attack and its geopolitical implications, with some questioning the evidence and others emphasizing the need for stronger AI security measures.

**Tags**: `#AI`, `#security`, `#corporate espionage`, `#Anthropic`, `#Alibaba`

---

<a id="item-12"></a>
## [US Government to Individually Approve GPT-5.6 Access](https://www.reddit.com/r/LocalLLaMA/comments/1ufo0un/us_govt_to_individually_approve_who_gets_gpt_56/) ⭐️ 8.0/10

The US government plans to individually approve who can access GPT-5.6, a future version of OpenAI's model, according to a Reddit post. This marks a shift toward centralized control over advanced AI distribution. This could set a precedent for government oversight of cutting-edge AI, potentially limiting access for researchers, developers, and competitors. It raises concerns about innovation, open-source AI, and global competitiveness. The news references GPT-5.6, which is not yet released; the latest known version is GPT-5.5 launched in April 2026. The approval process details remain unspecified, but it suggests a per-user licensing or authorization system.

reddit · r/LocalLLaMA · /u/AtlanticHM · Jun 25, 22:02

**Background**: GPT-5 is a multimodal large language model released by OpenAI in August 2025, with subsequent updates like GPT-5.5. The US government has been developing AI regulations through executive orders and agency frameworks, but direct individual approval of model access would be a new level of control.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5">GPT-5</a></li>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT‑5.5 - OpenAI</a></li>
<li><a href="https://legalclarity.org/government-regulations-on-artificial-intelligence-u-s-laws/">Government Regulations on Artificial Intelligence: U.S. Laws</a></li>

</ul>
</details>

**Discussion**: The Reddit community expressed strong concerns about central control, with many arguing it could stifle open-source development and give the government too much power. Some questioned the feasibility and enforcement of such a system.

**Tags**: `#AI regulation`, `#GPT`, `#government policy`, `#AI access`

---

<a id="item-13"></a>
## [audio.cpp: 12 Audio Models in One C++/ggml Runtime, Up to 5x Faster](https://www.reddit.com/r/LocalLLaMA/comments/1ufpnm6/audiocpp_12_audio_models_qwen3tts_pockettts_vevo2/) ⭐️ 8.0/10

audio.cpp is a new native C++ inference framework built on ggml that unifies 12 audio models including TTS, ASR, voice cloning, and voice conversion in a single runtime, achieving up to 5x speedup over Python on CUDA. This project addresses the fragmentation of audio ML models by providing a shared runtime, simplifying deployment and reducing dependency overhead, which could accelerate adoption of audio AI in production environments. Benchmarks show PocketTTS achieves 3.68x speedup on a single run, Qwen3-TTS up to 3.06x on long-form, and Vevo2 up to 5.03x on a single run, all using original weights without quantization. The framework supports CPU, CUDA, Vulkan, and Metal backends.

reddit · r/LocalLLaMA · /u/Acceptable-Cycle4645 · Jun 25, 23:10

**Background**: ggml is a tensor library for machine learning that enables efficient inference on consumer hardware, and is the foundation of popular projects like llama.cpp. Traditionally, audio models require separate Python environments and dependencies, making deployment cumbersome. audio.cpp leverages ggml to run multiple audio models in a single C++ executable, eliminating Python from the inference path.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GGML">GGML</a></li>
<li><a href="https://github.com/QwenLM/Qwen3-TTS">GitHub - QwenLM/Qwen3-TTS: Qwen3-TTS is an open-source series ...</a></li>
<li><a href="https://silentinfotech.com/blog/ai-9/pockettts-lightweight-text-to-speech-ai-model-for-fast-voice-generation-324">PocketTTS AI: Lightweight Text-to-Speech Model for Fast Voice...</a></li>

</ul>
</details>

**Discussion**: The Reddit community praised the project for its performance and unified approach, with users expressing interest in testing on different hardware and contributing. Some noted the early stage and lack of streaming support, but overall sentiment was positive.

**Tags**: `#audio`, `#C++`, `#ggml`, `#TTS`, `#inference`

---

<a id="item-14"></a>
## [JetSpec: Up to 9.64x LLM Speedup via Parallel Tree Drafting](https://www.reddit.com/r/LocalLLaMA/comments/1ufntl5/research_jetspec_speculative_decoding_with/) ⭐️ 8.0/10

JetSpec introduces causal parallel tree drafting for speculative decoding, achieving up to 9.64x end-to-end speedup on MATH-500 and 4.58x on open-ended chat, while maintaining lossless accuracy. It also reaches around 1000 tokens per second on a single B200 GPU. This breakthrough significantly reduces LLM inference latency, making real-time applications more feasible and lowering deployment costs. It addresses a key bottleneck in speculative decoding by jointly optimizing drafting cost and quality. JetSpec uses CUDA graph and kernel optimizations to further boost performance. The method drafts a causality-preserving tree in a single pass, overcoming the dilemma between autoregressive drafting cost and block-diffusion inconsistency.

reddit · r/LocalLLaMA · /u/No_Yogurtcloset_7050 · Jun 25, 21:55

**Background**: Speculative decoding accelerates LLM inference by using a small draft model to generate candidate tokens, which are then verified by the target model. Traditional approaches either use autoregressive drafting (costly for deep trees) or block-diffusion (inconsistent across branches). JetSpec's causal parallel tree drafting combines the benefits of both.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/ai-science/speculative-decoding-make-llm-inference-faster-c004501af120">Speculative Decoding — Make LLM Inference ... | Medium | AI Science</a></li>
<li><a href="https://github.com/JetSpec-project/vllm-jetspec/blob/causal-parallel-drafting/project_plans/causal_tree_draft_exec_plan.md">vllm-jetspec/project_plans/causal_tree_draft_exec_plan.md at ...</a></li>
<li><a href="https://deepwiki.com/harleyszhang/llm_note/4.2-cuda-graph-optimization">CUDA Graph Optimization | harleyszhang/llm_note | DeepWiki</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is active with technical questions about implementation details and comparisons to other methods like DFlash. Overall sentiment is positive, with users impressed by the speedup numbers and eager to test the open-source code.

**Tags**: `#speculative decoding`, `#LLM inference`, `#speedup`, `#parallel tree drafting`, `#CUDA optimization`

---

<a id="item-15"></a>
## [NVIDIA Releases Diffusion-Based Language Model Nemotron-TwoTower](https://www.reddit.com/r/LocalLLaMA/comments/1uf4azy/nvidia_has_released/) ⭐️ 8.0/10

NVIDIA has released Nemotron-TwoTower-30B-A3B-Base-BF16, a diffusion-based language model built on the Nemotron 3 Nano 30B-A3B backbone. It uses a frozen autoregressive context tower and a diffusion denoiser tower to generate blocks of tokens in parallel. This model achieves 2.42x generation throughput over autoregressive baselines while retaining 98.7% of benchmark quality, potentially enabling faster and more efficient LLM inference. It represents a novel approach to language modeling that could influence future model architectures. The model uses a mask-diffusion setup where the diffusion tower iteratively fills masked token blocks. It is based on the Nemotron 3 Nano 30B-A3B, a Mixture-of-Experts (MoE) model with 30B total parameters and 3B active parameters.

reddit · r/LocalLLaMA · /u/nikhilprasanth · Jun 25, 08:34

**Background**: Traditional large language models (LLMs) generate text autoregressively, one token at a time, which limits throughput. Diffusion language models instead generate text by iteratively denoising a sequence of masked tokens in parallel, offering potential speedups. NVIDIA's Nemotron-TwoTower combines a frozen autoregressive tower for context with a diffusion tower for parallel generation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.09992">[2502.09992] Large Language Diffusion Models - arXiv.org</a></li>
<li><a href="https://huggingface.co/unsloth/Nemotron-3-Nano-30B-A3B">unsloth/ Nemotron - 3 - Nano - 30 B - A 3 B · Hugging Face</a></li>
<li><a href="https://medium.com/data-science-in-your-pocket/nemotron-3-nano-30b-implementing-nvidias-1m-context-hybrid-mamba-moe-built-for-agentic-speed-5af245ddd9c4">Nemotron ‑ 3 Nano 30 B : Implementing NVIDIA’s 1M‑Context... | Medium</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is active with technical insights, including comparisons to other diffusion-based models and discussions about the trade-offs between quality and speed. Some users express curiosity about the practical implications for local inference and fine-tuning.

**Tags**: `#NVIDIA`, `#diffusion language model`, `#LLM inference`, `#Nemotron`, `#machine learning`

---