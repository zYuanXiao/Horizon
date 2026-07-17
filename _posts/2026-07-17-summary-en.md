---
layout: default
title: "Horizon Summary: 2026-07-17 (EN)"
date: 2026-07-17
lang: en
---

> From 151 items, 15 important content pieces were selected

---

1. [Firefox Compiled to WebAssembly Runs Inside Chrome](#item-1) ⭐️ 9.0/10
2. [Linus Torvalds Endorses AI in Linux Kernel Development](#item-2) ⭐️ 9.0/10
3. [Kimi K3 2.8T-A50B: Largest Open Model, Opus 4.8-Class at Sonnet 5 Price](#item-3) ⭐️ 9.0/10
4. [OpenAI Codex: A Lightweight Coding Agent in Your Terminal](#item-4) ⭐️ 9.0/10
5. [Ring-Zero Scales Zero RL to Trillion Parameters for Emergent Reasoning](#item-5) ⭐️ 9.0/10
6. [Open Interpreter Surges as Coding Agent for Open Models](#item-6) ⭐️ 8.0/10
7. [Boogu-Image-0.1: Open-Source Multimodal Model Family](#item-7) ⭐️ 8.0/10
8. [Car OTA Update Breaks Android Auto, Sparks Software Quality Debate](#item-8) ⭐️ 8.0/10
9. [Sony Deletes Purchased Movies from User Accounts](#item-9) ⭐️ 8.0/10
10. [Schema Harness Hits ~99% on ARC-AGI-3 Public](#item-10) ⭐️ 8.0/10
11. [GPT-5.6 Codex Bug Deletes Files in Full Access Mode](#item-11) ⭐️ 8.0/10
12. [Thinking Machines Lab Releases Inkling Open-Weights Model](#item-12) ⭐️ 8.0/10
13. [Lila Sciences: Future Lab as Data Center](#item-13) ⭐️ 8.0/10
14. [DeepMind and Isomorphic Labs unveil bioresilience AI approach](#item-14) ⭐️ 8.0/10
15. [EU Mandates Google to Share Search Data, Open Android AI](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Firefox Compiled to WebAssembly Runs Inside Chrome](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter has compiled the full Firefox browser (Gecko engine) to WebAssembly, enabling it to run entirely within another browser, as demonstrated by loading a blog inside Firefox inside Chrome. This groundbreaking achievement demonstrates a new paradigm for browser-in-browser execution, potentially enabling secure sandboxing, legacy app compatibility, and novel web platform capabilities. The project used an estimated $25,000 worth of AI tokens (Claude Opus and Fable) but cost much less due to a subscription plan, and all network traffic is proxied through Puter's server using the Wisp protocol over WebSocket.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (Wasm) is a low-level binary instruction format that runs in modern browsers at near-native speed. Compiling a full browser like Firefox to Wasm is extremely challenging due to its size and complexity; the resulting gecko.wasm binary is 233 MB. The project chose Firefox because Gecko has strong single-process support, simplifying the Wasm port.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.puter.com/labs/firefox-wasm/">Firefox in WebAssembly</a></li>
<li><a href="https://news.ycombinator.com/item?id=48926939">Show HN: Firefox in WebAssembly | Hacker News</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/ wisp - protocol : Wisp is a low-overhead...</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was highly positive, with many impressed by the technical feat. Some raised concerns about the cost of proxying traffic and the practicality of running a full browser in Wasm, but the team noted they had to scale servers to handle the traffic spike.

**Tags**: `#WebAssembly`, `#Firefox`, `#Browser`, `#Wasm`, `#Virtualization`

---

<a id="item-2"></a>
## [Linus Torvalds Endorses AI in Linux Kernel Development](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 9.0/10

Linus Torvalds, the creator of Linux, publicly declared that Linux is not an anti-AI project and that AI is a clearly useful tool for kernel development, warning that those who disagree can fork the project or leave. This definitive stance from the top-level maintainer signals a potential policy shift in the Linux kernel community, potentially accelerating the adoption of AI tools in open-source development and influencing other projects. Torvalds stated on the Linux Media Mailing List that he is willing to 'absolutely put my foot down' on this issue, emphasizing that AI's usefulness is no longer in question, though other economic questions remain.

rss · Simon Willison · Jul 16, 13:26

**Background**: The Linux kernel is the core of the Linux operating system, maintained by a large open-source community led by Linus Torvalds. AI tools, such as large language models (LLMs), have been increasingly used for code generation and debugging, but some developers have raised ethical and practical concerns about their use in open-source projects.

**Tags**: `#Linux`, `#AI`, `#Open Source`, `#Kernel Development`, `#Linus Torvalds`

---

<a id="item-3"></a>
## [Kimi K3 2.8T-A50B: Largest Open Model, Opus 4.8-Class at Sonnet 5 Price](https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest) ⭐️ 9.0/10

Moonshot AI released Kimi K3, a 2.8 trillion parameter open Mixture-of-Experts model with a 1M-token context window, claiming performance comparable to Anthropic's Opus 4.8 at pricing similar to Sonnet 5. As the largest open model ever released, Kimi K3 pushes the frontier of open-source AI, potentially democratizing access to near-frontier intelligence and intensifying competition among AI labs. Kimi K3 uses a MoE architecture with 2.8T total parameters and 50B active parameters per token, and features Kimi Delta Attention for efficient long-context processing. Its API pricing is $3/$15 per million tokens (input/output), matching Anthropic's Sonnet 5 pricing.

rss · Latent Space · Jul 17, 01:46

**Background**: Open models have traditionally lagged behind proprietary frontier models in performance. Kimi K3 aims to close this gap by offering a model that rivals Anthropic's Opus 4.8, one of the most capable proprietary models, while being openly available and priced competitively with Sonnet 5.

<details><summary>References</summary>
<ul>
<li><a href="https://kie.ai/blog/what-is-kimi-k3">What Is Kimi K3? Moonshot's 2.8T, 1M-Context Flagship</a></li>
<li><a href="https://www.marktechpost.com/2026/07/16/moonshot-ai-releases-kimi-k3-a-2-8-trillion-parameter-open-moe-model-with-kimi-delta-attention-and-1m-context/">Moonshot AI Releases Kimi K3: A 2.8 Trillion Parameter Open MoE Model With Kimi Delta Attention and 1M Context - MarkTechPost</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the model's high pricing for a Chinese open-weight model, but note it is justified if truly competitive with frontier models. Some see Chinese labs driving commoditization of AI intelligence, while others question the massive investment required.

**Tags**: `#open models`, `#AI`, `#large language models`, `#Kimi K3`, `#machine learning`

---

<a id="item-4"></a>
## [OpenAI Codex: A Lightweight Coding Agent in Your Terminal](https://github.com/openai/codex) ⭐️ 9.0/10

OpenAI Codex, a lightweight coding agent written in Rust, has gained 381 stars today on GitHub, reaching 98,900 total stars. It translates natural language into code directly in the terminal. This tool represents a paradigm shift in developer tooling by enabling natural language to code translation, potentially boosting productivity for millions of developers. Its massive community adoption (98.9k stars) signals strong demand for AI-powered coding assistants. Codex is built in Rust, emphasizing performance and safety, and runs as a terminal-based agent. It is part of OpenAI's suite of AI-driven coding agents designed to automate software engineering tasks.

github_trending · GitHub Trending · Jul 17, 02:55

**Background**: A coding agent is an AI system that autonomously performs coding tasks like writing, reviewing, and refactoring code. OpenAI Codex is one of several popular AI coding agents, alongside tools like Cursor, Claude Code, and GitHub Copilot, each offering different trade-offs between speed, control, and autonomy.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Codex">OpenAI Codex</a></li>
<li><a href="https://grokipedia.com/page/Coding_agent">Coding agent</a></li>
<li><a href="https://www.faros.ai/blog/best-ai-coding-agents-2026">Best AI Coding Agents for 2026: Real-World Developer Reviews</a></li>

</ul>
</details>

**Tags**: `#AI`, `#coding agent`, `#developer tools`, `#natural language processing`, `#Rust`

---

<a id="item-5"></a>
## [Ring-Zero Scales Zero RL to Trillion Parameters for Emergent Reasoning](https://huggingface.co/papers/2607.12395) ⭐️ 9.0/10

Researchers present Ring-Zero, a stable and efficient pipeline for scaling reinforcement learning with verifiable rewards (zero RL) to trillion-parameter models, achieving competitive performance on seven mathematical benchmarks. This work demonstrates that scaling zero RL to trillion-parameter models significantly enhances sample efficiency and performance ceilings, and reveals emergent reasoning behaviors such as self-verification and parallel reasoning, which could reduce the need for hand-crafted heuristics in AI systems. The pipeline incorporates algorithmic and system optimizations including clipped importance sampling, training-inference ratio correction, and mixed-precision control. The training process progresses through an initial discovery phase followed by a sharpening phase.

huggingface_papers · Hugging Face Papers · Jul 16, 00:00

**Background**: Reinforcement learning with verifiable rewards (zero RL) is a paradigm that enhances reasoning in large language models without human-annotated data. Previous work was limited to small models due to computational constraints, leaving scaling behaviors unexplored.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.12395">Ring- Zero : Scaling Zero RL to a Trillion Parameters for Emergent...</a></li>
<li><a href="https://arxiv.org/abs/1905.02363">[1905.02363] Dimension-Wise Importance Sampling Weight Clipping for Sample-Efficient Reinforcement Learning</a></li>
<li><a href="https://arxiv.org/html/2602.01826">Beyond Precision: Training-Inference Mismatch is an Optimization Problem and Simple LR Scheduling Fixes It</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#large language models`, `#reasoning`, `#scaling`, `#zero RL`

---

<a id="item-6"></a>
## [Open Interpreter Surges as Coding Agent for Open Models](https://github.com/openinterpreter/openinterpreter) ⭐️ 8.0/10

Open Interpreter, a coding agent for open models like Kimi K3, gained 661 stars on GitHub in a single day, reaching over 66,000 total stars. The project is written in Rust and focuses on low-cost model performance. This rapid growth signals strong community interest in AI-assisted programming with open models, potentially democratizing coding agents beyond proprietary solutions. It could lower barriers for developers to integrate AI into their workflows. Open Interpreter is a fork of OpenAI's Codex, designed to run in the terminal and execute code across multiple languages. It uses a sandbox for safety and supports models like Kimi K3, which has 2.8 trillion parameters and a 1M token context window.

github_trending · GitHub Trending · Jul 17, 02:55

**Background**: Open Interpreter is a local code execution environment that allows large language models to run code through a ChatGPT-like terminal interface. It emphasizes performance with low-cost models and is written in Rust for speed. Kimi K3 is a recently released open model with 2.8 trillion parameters, making it one of the largest open models available.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openinterpreter/openinterpreter">GitHub - openinterpreter/openinterpreter: A coding agent for low-cost models · GitHub</a></li>
<li><a href="https://www.openinterpreter.com/">Open Interpreter CLI: open source AI coding agent</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**Tags**: `#AI`, `#coding agent`, `#open models`, `#Rust`, `#developer tools`

---

<a id="item-7"></a>
## [Boogu-Image-0.1: Open-Source Multimodal Model Family](https://huggingface.co/papers/2607.13125) ⭐️ 8.0/10

Boogu-Image-0.1 is an open-source unified multimodal understanding and generation model family with Base, Turbo, Edit, and Edit-Turbo variants, achieving competitive text-to-image generation, fast inference, and bilingual text rendering. This work demonstrates that targeted improvements in data quality, training pipelines, and agentic inference-time scaling can substantially enhance generation performance under constrained compute budgets, matching or surpassing other open-source models and approaching closed-source systems. The base model was trained on only 208.62 million unique images with a theoretical training cost of approximately $400K. The model family includes variants for fast inference (Turbo) and instruction-based editing (Edit).

huggingface_papers · Hugging Face Papers · Jul 16, 00:00

**Background**: Unified multimodal understanding and generation models aim to handle both image comprehension and creation in a single framework. Closed-source systems like Nano-Banana-Pro and GPT-Image-2 achieve strong performance through system-level integration, but their internal practices are undisclosed. Boogu-Image-0.1 is released under Apache 2.0 with weights, code, and recipes to advance open-source progress.

**Tags**: `#multimodal`, `#text-to-image`, `#open-source`, `#image generation`, `#AI model`

---

<a id="item-8"></a>
## [Car OTA Update Breaks Android Auto, Sparks Software Quality Debate](https://imdanielkendall.com/the-great-software-regress-how-move-fast-and-break-things-broke-our-lives/) ⭐️ 8.0/10

A car owner reports that an over-the-air (OTA) update from MINI broke Android Auto functionality, requiring a call to the manufacturer to demand a fix. The incident highlights how software updates can degrade user experience without accountability. This matters because as cars become more software-defined, OTA updates can introduce regressions that affect core features like Android Auto, eroding trust and potentially impacting car sales. The discussion reflects broader concerns about software quality in agile development practices. The author's MINI OTA update broke Android Auto, and similar issues have been reported with Kia EV9 updates causing blank screens. The article criticizes the 'move fast and break things' culture and the lack of customer feedback loops in agile development.

hackernews · Expletive4138 · Jul 16, 22:29 · [Discussion](https://news.ycombinator.com/item?id=48941129)

**Background**: Over-the-air (OTA) updates allow car manufacturers to wirelessly update vehicle software, similar to smartphone updates. Android Auto is a system that mirrors phone apps onto the car's display. As cars become more connected, software quality issues can directly impact user experience and safety.

<details><summary>References</summary>
<ul>
<li><a href="https://www.racv.com.au/royalauto/transport/cars/what-are-ota-updates-in-cars-how-they-work.html">What are over -the- air ( OTA ) updates and how they work in cars | RACV</a></li>
<li><a href="https://www.vw.com/en/owners-and-services/apps-and-connected-services/vehicle-software-updates.html">Vehicle Software Updates | Volkswagen</a></li>
<li><a href="https://www.makeuseof.com/what-are-tesla-over-the-air-updates/">Tesla's over -the- air updates can be frustrating, but they're important...</a></li>

</ul>
</details>

**Discussion**: Commenters share similar experiences, with one noting Kia's EV9 update broke CarPlay. Another argues that the cost of shipping broken software has shifted from manufacturers to users, and that customers are unwillingly acting as QA. There is agreement that poor software experiences can harm brand reputation and sales.

**Tags**: `#software quality`, `#agile development`, `#automotive software`, `#OTA updates`, `#user experience`

---

<a id="item-9"></a>
## [Sony Deletes Purchased Movies from User Accounts](https://www.techdirt.com/2026/07/15/sony-deletes-a-bunch-more-movies-from-the-accounts-of-people-who-bought-them/) ⭐️ 8.0/10

Sony has removed several movies from the accounts of users who believed they had purchased them, reigniting the debate over digital ownership and consumer rights. This incident highlights the fragility of digital ownership, where consumers can lose access to content they paid for without compensation, potentially eroding trust in digital storefronts and pushing users toward physical media or piracy. The deletions affect movies purchased through Sony's PlayStation Store, and users report no refunds or prior notice. This is not the first time Sony has removed purchased content; similar incidents occurred in 2024 and 2025.

hackernews · nekusar · Jul 16, 12:13 · [Discussion](https://news.ycombinator.com/item?id=48933419)

**Background**: Digital ownership typically means purchasing a license to access content, not owning the content itself. Companies like Sony can revoke these licenses under terms of service, leaving consumers with no legal recourse. The term 'buy' in digital storefronts is often misleading, as it implies permanent ownership.

**Discussion**: Commenters are divided: some argue that revocations should come with full refunds to balance the economic impact, while others insist that customers should receive actual video files rather than relying on a service. There is also discussion about the legality of a 'Buy' button that functions as a disguised 'Rent' button.

**Tags**: `#digital rights`, `#consumer protection`, `#Sony`, `#digital ownership`, `#media`

---

<a id="item-10"></a>
## [Schema Harness Hits ~99% on ARC-AGI-3 Public](https://schema-harness.github.io/) ⭐️ 8.0/10

Impossible Research's Schema harness achieved approximately 99% on the ARC-AGI-3 public set using frontier models like Opus 4.8 and Fable 5, compared to the baseline of around 13% without the harness. This result highlights the growing importance of harness engineering in AI, suggesting that system-level scaffolding can dramatically boost benchmark performance, potentially reshaping how we evaluate and develop general intelligence. The harness works by using a frontier model to write a simulator for the task and then solving it within that simulator, which is a different approach than directly solving the raw ARC-AGI puzzles. Performance on the held-out set has not yet been confirmed.

hackernews · jasondavies · Jul 16, 15:29 · [Discussion](https://news.ycombinator.com/item?id=48935905)

**Background**: ARC-AGI is a benchmark designed to be easy for humans but hard for AI, testing generalization and reasoning on visual grid puzzles. Harness engineering refers to the infrastructure, orchestration, and scaffolding around AI models that can significantly enhance their capabilities beyond raw model performance.

<details><summary>References</summary>
<ul>
<li><a href="https://schema-harness.github.io/">Frontier Models with Our Harness Achieve ~99% on ARC-AGI-3 Public — Schema</a></li>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - The only AI benchmark that measures AGI progress.</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some see it as a big deal if it holds on the hold-out set, while others argue it measures something different from intended generalization, as the harness essentially gets the model to write a simulator first. Skepticism remains due to the lack of open-sourcing and hold-out validation.

**Tags**: `#ARC-AGI`, `#AI benchmarks`, `#harness engineering`, `#frontier models`, `#generalization`

---

<a id="item-11"></a>
## [GPT-5.6 Codex Bug Deletes Files in Full Access Mode](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

A bug in GPT-5.6's Codex can delete user files when full access mode is enabled without sandboxing, as the model mistakenly deletes $HOME instead of a temporary directory. This bug highlights critical safety risks in AI coding agents, as users who grant file system access may suffer data loss. It underscores the need for robust sandboxing and review mechanisms before deploying such agents. The bug occurs when full access mode is enabled, sandboxing is disabled, and auto review is turned off. The model attempts to override $HOME to define a temporary directory but mistakenly deletes $HOME instead.

rss · Simon Willison · Jul 16, 17:45

**Background**: Codex is an AI coding agent that can execute commands on a user's system. Sandboxing isolates the agent to prevent harmful actions, while full access mode removes those restrictions. The $HOME environment variable points to the user's home directory, which contains personal files.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/320198/20260712/chatgpt-work-launch-went-wrong-gpt-56-sol-deleted-user-files-without-permission.htm">ChatGPT Work Launch Went Wrong: GPT - 5 . 6 Sol Deleted User Files ...</a></li>
<li><a href="https://techcrunch.com/2026/07/14/openais-new-flagship-model-deletes-files-on-its-own-people-keep-warning/">OpenAI's new flagship model deletes files on its own... | TechCrunch</a></li>
<li><a href="https://explainx.ai/blog/chatgpt-codex-5-hour-limit-removed-weekly-reset-july-2026">ChatGPT 5-Hour Limit Removed — July 2026 | explainx.ai... | explainx.ai</a></li>

</ul>
</details>

**Discussion**: The community expressed alarm and frustration, with many users reporting data loss. Some criticized OpenAI for not enforcing sandboxing by default, while others called for better safeguards before deploying such powerful agents.

**Tags**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`, `#bug`

---

<a id="item-12"></a>
## [Thinking Machines Lab Releases Inkling Open-Weights Model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

Thinking Machines Lab, led by Mira Murati, released Inkling, an open-weights multimodal Mixture-of-Experts transformer with 975B total parameters (41B active), licensed under Apache-2.0 and trained on 45 trillion tokens of text, images, audio, and video. Inkling strengthens the US open-weights ecosystem, offering a competitive alternative to Chinese open models and enabling fine-tuning via the Tinker platform, which could democratize access to large multimodal AI. Inkling supports a context window of up to 1 million tokens and is not a frontier model but a strong base for customization; a smaller variant Inkling-Small (276B total, 12B active) is forthcoming. The model card and training data documentation are notably sparse.

rss · Simon Willison · Jul 16, 15:35

**Background**: Mixture-of-Experts (MoE) architectures activate only a subset of parameters per input, enabling large total parameter counts with efficient inference. Open-weights models allow developers to download, fine-tune, and deploy the model freely, fostering innovation and transparency. Thinking Machines Lab is a new AI company founded by former OpenAI CTO Mira Murati.

<details><summary>References</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our open-weights model - Thinking Machines Lab</a></li>
<li><a href="https://thinkingmachines.ai/inkling/">An efficient open - weights model that reasons over text, image, and...</a></li>
<li><a href="https://artificialanalysis.ai/models/inkling">Inkling - Intelligence, Performance & Price Analysis</a></li>

</ul>
</details>

**Tags**: `#open-weights`, `#multimodal`, `#Mixture-of-Experts`, `#AI model release`, `#Thinking Machines Lab`

---

<a id="item-13"></a>
## [Lila Sciences: Future Lab as Data Center](https://www.latent.space/p/the-lab-of-the-future-should-feel) ⭐️ 8.0/10

Lila Sciences envisions the future laboratory as a data center where AI and robotics generate and utilize scientific data as a new frontier for training models. This paradigm shift could dramatically accelerate scientific discovery by treating experimental data as a scalable resource for AI, potentially transforming industries like pharmaceuticals and materials science. The article features insights from Andy Beam and Rafa Gómez-Bombarelli, and Lila Sciences is building an autonomous lab platform for life, chemistry, and materials science.

rss · Latent Space · Jul 16, 13:30

**Background**: Traditional scientific research relies on manual experimentation and hypothesis testing, which is slow and limited in scale. AI-driven scientific experimentation integrates AI with automated workflows to generate hypotheses, plan experiments, and refine models continuously. Lila Sciences aims to create a 'scientific superintelligence' platform that treats the lab as a data center, where robots run experiments and AI learns from the resulting data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lila.ai/">LILA | Scientific Superintelligence</a></li>
<li><a href="https://www.linkedin.com/company/lila-sciences">Lila Sciences | LinkedIn</a></li>
<li><a href="https://www.emergentmind.com/topics/ai-driven-scientific-experimentation">AI - Driven Scientific Experimentation</a></li>

</ul>
</details>

**Tags**: `#AI`, `#scientific research`, `#robotics`, `#data center`, `#Lila Sciences`

---

<a id="item-14"></a>
## [DeepMind and Isomorphic Labs unveil bioresilience AI approach](https://deepmind.google/blog/our-approach-to-bioresilience/) ⭐️ 8.0/10

Google DeepMind and Isomorphic Labs have announced their joint approach to bioresilience, leveraging AI models to enhance the ability of biological systems to adapt to change and resist threats. This initiative marks a significant step in applying AI to global biological challenges, potentially improving pandemic preparedness, drug discovery, and ecological resilience. It also sets a precedent for responsible AI use in biology. The announcement is high-level with few technical specifics, but it builds on DeepMind's AlphaFold technology and Isomorphic Labs' drug discovery expertise. The focus is on preventing AI misuse while aiding outbreak response.

rss · Google DeepMind Blog · Jul 16, 09:30

**Background**: Bioresilience refers to the ability of species or individuals to adapt to environmental changes. DeepMind's AlphaFold can predict protein structures with high accuracy, and Isomorphic Labs applies AI to drug discovery. This collaboration aims to combine these strengths for broader biological resilience.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bioresilience">Bioresilience - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isomorphic_Labs">Isomorphic Labs</a></li>
<li><a href="https://www.artificialintelligence-news.com/news/examining-google-deepmind-ai-bioresilience-push/">Examining Google DeepMind 's AI bioresilience push</a></li>

</ul>
</details>

**Tags**: `#AI`, `#bioresilience`, `#DeepMind`, `#Isomorphic Labs`, `#biology`

---

<a id="item-15"></a>
## [EU Mandates Google to Share Search Data, Open Android AI](https://arstechnica.com/gadgets/2026/07/its-official-eu-will-force-google-to-share-search-data-and-open-up-ai-on-android/) ⭐️ 8.0/10

The European Union has officially mandated Google to share its search data with third parties and open up AI capabilities on Android under the Digital Markets Act (DMA), citing competition concerns. This landmark regulation could reshape the Android ecosystem and AI market in Europe, potentially increasing competition and user choice, while Google warns of privacy and security risks. The DMA requires gatekeepers like Google to ensure interoperability and data access; non-compliance can lead to fines of up to 10% of worldwide turnover.

rss · Ars Technica AI · Jul 16, 20:41

**Background**: The EU Digital Markets Act (DMA) entered into force in November 2022 and became applicable in May 2023, targeting large platforms like Google, Apple, and Meta. It aims to prevent these gatekeepers from abusing market power, including by forcing them to open up their services and data to competitors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/EU_Digital_Markets_Act">EU Digital Markets Act</a></li>
<li><a href="https://en.cryptonomist.ch/2026/04/28/android-ai-openness-eu/">EU pressures Google to open Android AI under DMA rules</a></li>

</ul>
</details>

**Tags**: `#EU regulation`, `#Google`, `#Android`, `#AI`, `#privacy`

---