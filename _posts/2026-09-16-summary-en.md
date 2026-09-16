---
layout: default
title: "Horizon Summary: 2026-09-16 (EN)"
date: 2026-09-16
lang: en
---

> From 142 items, 15 important content pieces were selected

---

1. [Google DeepMind Releases Gemini 3.8 Live and Live Extended Thinking](#item-1) ⭐️ 9.0/10
2. [Agent-Reach: Free Multi-Platform CLI for AI Agents](#item-2) ⭐️ 8.0/10
3. [Vidu S2 Enables Real-Time 720p Interactive Avatar and Video Editing](#item-3) ⭐️ 8.0/10
4. [ZGCM-1: Fully Open 7B Model for Math and Agentic Search](#item-4) ⭐️ 8.0/10
5. [Ex-Apple Engineer Builds Linux GPU Driver for M4 Mac Mini in One Month](#item-5) ⭐️ 8.0/10
6. [Strix AI agent gains admin access to Baseten's GitHub in 25 minutes](#item-6) ⭐️ 8.0/10
7. [Bruce Schneier Calls to End 25 Years of Mass Surveillance](#item-7) ⭐️ 8.0/10
8. [Java 27 Announced as Community Debates Cadence and Valhalla Delay](#item-8) ⭐️ 8.0/10
9. [Lawfare Calls 153M Driver's License Breach a National Security Disaster](#item-9) ⭐️ 8.0/10
10. [AEF-1 standard for third-party AI evaluators emerges, co-signed by xAI, OpenAI, and Anthropic](#item-10) ⭐️ 8.0/10
11. [Voodoo Dynamic Quant Released Under MIT License](#item-11) ⭐️ 8.0/10
12. [LynnReal-Omni: 32B Unified Video Diffusion Model with ComfyUI Nodes](#item-12) ⭐️ 8.0/10
13. [Meridian brings camera control and bullet time to existing videos](#item-13) ⭐️ 8.0/10
14. [Prior Labs Releases TabPFN-3.5, New SOTA Tabular Foundation Model](#item-14) ⭐️ 8.0/10
15. [Alibaba open-sources hybrid LLM code review tool, gaining 2,756 stars in a day](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google DeepMind Releases Gemini 3.8 Live and Live Extended Thinking](https://deepmind.google/blog/introducing-gemini-3-8-live-and-3-8-live-extended-thinking/) ⭐️ 9.0/10

Google DeepMind announced Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking, two new speech-to-speech models that process visual inputs in near real-time and add background reasoning during live audio sessions. They are positioned as the company's most advanced live dialogue models yet and are available through the Gemini API. The release intensifies competition in real-time, multimodal voice AI, where Google is directly matching OpenAI's GPT-Live family. Developers building voice agents, live translation, and conversational assistants gain a lower-latency default option plus a reasoning-enhanced variant, which could accelerate adoption of speech-first AI interfaces. Gemini 3.8 Live is positioned as the default choice for low-latency voice agent experiences and real-time dialogue without reasoning-induced delays, while the Extended Thinking variant introduces background reasoning during live audio sessions and requires clients to update their integration. Both models are part of the Gemini 3 series of natively multimodal reasoning models.

rss · Google DeepMind Blog · Sep 15, 17:05

**Background**: Multimodal AI models can combine and reason across multiple data types such as text, images, and audio, enabling richer understanding than single-modality systems. Speech-to-speech models like these skip the traditional pipeline of transcribing audio to text and back, allowing more natural, low-latency conversation. Google's Gemini 3 series is its flagship family of natively multimodal reasoning models, and the Live variants extend that line into real-time voice interaction.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking - Google Blog</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live">Gemini 3.8 Live | Gemini API - Google AI for Developers</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking">Gemini 3.8 Live Extended Thinking - Google AI for Developers</a></li>

</ul>
</details>

**Discussion**: Commenters were largely positive: one praised Gemini's Afrikaans conversation and grammar help, and another called it a solid release with good accent handling, pleasant voices, and low latency, noting it finally works on a workspace account. Skeptics questioned whether Google can overtake rivals like Fable and Astra, and one criticized a demo video in which the model lost to a common chess checkmate pattern.

**Tags**: `#AI`, `#Google DeepMind`, `#Gemini`, `#Multimodal Models`, `#Model Release`

---

<a id="item-2"></a>
## [Agent-Reach: Free Multi-Platform CLI for AI Agents](https://github.com/Panniantong/Agent-Reach) ⭐️ 8.0/10

Panniantong/Agent-Reach, a Python-based CLI tool, gained 960 GitHub stars in a single day, bringing its total to over 82,000 stars and 7,155 forks. It lets AI agents read and search Twitter, Reddit, YouTube, GitHub, Bilibili, and XiaoHongShu through one unified command-line interface with zero API fees. API fees and rate limits are a major bottleneck for AI agents that need real-world data, so a free unified access layer across six major platforms could significantly lower costs and complexity for agent developers. Its rapid star growth suggests strong demand for practical, low-cost data access tools in the AI/ML and software engineering communities. The tool is written in Python and positions itself as giving an AI agent "eyes to see the entire internet" by combining reading and search across Twitter, Reddit, YouTube, GitHub, Bilibili, and XiaoHongShu in one CLI. Because it avoids official APIs, users should be aware that it likely relies on web scraping, which can be fragile when platforms change their pages or anti-bot measures.

github_trending · GitHub Trending · Sep 16, 03:55

**Background**: AI agents are autonomous programs that can plan and take actions, but they need data from the web to be useful. Many platforms charge for API access or impose strict rate limits, which makes large-scale data collection expensive. Web scraping is an alternative that extracts content directly from web pages, though it is often less stable than official APIs. Agent-Reach targets this gap by offering one free CLI for multiple platforms, including Chinese services like Bilibili and XiaoHongShu that are less commonly supported by Western tools.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=wk8joeKtXBA">Web Scraping, and how it gives AI Agents 100x more power - YouTube</a></li>
<li><a href="https://www.globaltimes.cn/page/202608/1369095.shtml">Chinese video platform Bilibili relaunches international... - Global Times</a></li>
<li><a href="https://prizmdigital.co.nz/what-is-xiaohongshu/">What is XiaoHongShu (REDNote) | Overview (2026) | Prizm Digital NZ</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#CLI`, `#web scraping`, `#data access`, `#open source`

---

<a id="item-3"></a>
## [Vidu S2 Enables Real-Time 720p Interactive Avatar and Video Editing](https://huggingface.co/papers/2609.11638) ⭐️ 8.0/10

Vidu S2 introduces two models: Vidu S2-Avatar, a real-time interactive digital-character model supporting 720p video generation with dynamic references that can be updated at any moment, and Vidu S2-Editing, a real-time video editing model that handles style rendering, clothing replacement, character replacement, and background replacement. The team also explores real-time spatial video generation for both models, and a playable online demo is available at vidu.com/vidu-stream. This marks a notable step toward real-time, interactive video generation that goes beyond offline clip synthesis, potentially benefiting live streaming, virtual production, gaming, and AR/VR content creation. By combining avatar generation with stream editing and spatial capabilities in one release, Vidu S2 raises the bar for what interactive AI video tools can do in practical, latency-sensitive applications. Compared with Vidu S1, Vidu S2-Avatar adds real-time 720p output, dynamic references that can be swapped mid-generation, and stronger instruction following such as dancing, while experiments show Vidu S2 outperforms all baselines. The spatial video generation capability is described as exploratory, meaning it is a feasibility study rather than a fully productized feature.

huggingface_papers · Hugging Face Papers · Sep 15, 00:00

**Background**: Real-time interactive video generation is an emerging area where models produce or modify video continuously in response to user input, rather than generating a fixed clip in one pass. Spatial video typically refers to video that carries depth or 3D scene information, such as stereo MV-HEVC tracks with spatial metadata, enabling more immersive playback. Vidu S1, the predecessor, was a real-time interactive video generation model for voice-controlled digital characters, and Vidu S2 extends that line with higher resolution, editable streams, and spatial experiments.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/shengshu-ai/Vidu-S">GitHub - shengshu-ai/Vidu-S: Vidu S: Real - Time Interactive, Editable ...</a></li>
<li><a href="https://developer.apple.com/documentation/imageio/creating-spatial-photos-and-videos-with-spatial-metadata">Creating spatial photos and videos with spatial metadata</a></li>

</ul>
</details>

**Tags**: `#video generation`, `#real-time`, `#spatial video`, `#interactive AI`, `#video editing`

---

<a id="item-4"></a>
## [ZGCM-1: Fully Open 7B Model for Math and Agentic Search](https://huggingface.co/papers/2609.13356) ⭐️ 8.0/10

Researchers released ZGCM-1, a fully open 7B dense foundation model trained from scratch with a 256K context window that couples internal reasoning with external tool use. It achieves a ~4.2x efficiency improvement in 16K pre-training time-to-loss and remains competitive with frontier models orders of magnitude larger, such as Qwen3-235B-A22B and GLM-5.1, on challenging math reasoning and agentic search benchmarks. The work shows that compact models can overcome parametric capacity limits by combining deliberate internal thinking with active external tool use, rather than passively memorizing the open web. Its fully open training recipe—including weights, intermediate checkpoints, training code, per-stage data recipes, and W&B logs—gives the community a rare end-to-end reproducible foundation-model pipeline. The architecture combines interleaved gated sliding-window attention with full attention and a stable FP8 Muon optimizer, while training uses a progressive curriculum scaling context across 16K, 64K, and 256K and reformulates interaction traces into Markov Decision Processes. The authors also distill eight actionable empirical findings spanning architectural scaling, SFT quality pruning, long-context generalization, and agentic co-training dynamics.

huggingface_papers · Hugging Face Papers · Sep 15, 00:00

**Background**: Sliding-window attention limits each token to attending only to a nearby window of tokens, which cuts the cost of long-context processing, while full attention lets tokens attend globally; interleaving the two aims to balance efficiency and recall. The Muon optimizer is a momentum-based method that applies Newton-Schulz orthogonalization to gradients and has emerged as an alternative to Adam for large-scale LLM training. A Markov Decision Process formalizes sequential decision-making as states, actions, and rewards, which is the standard framing for reinforcement learning and agentic tool-use trajectories. Agent swarms here refer to multiple autonomous agents coordinating cluster operations, data curation, and diagnostic evaluation during model development.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/gated-sliding-window-attention-g-swa">Gated Sliding-Window Attention (G-SWA) - Emergent Mind</a></li>
<li><a href="https://docs.nvidia.com/nemo/rl/latest/guides/muon-optimizer.html">Muon Optimizer — NeMo-RL - NVIDIA Documentation</a></li>
<li><a href="https://www.sciencedirect.com/topics/computer-science/markov-decision-process">sciencedirect.com/topics/computer-science/ markov - decision - process</a></li>

</ul>
</details>

**Tags**: `#foundation models`, `#efficient training`, `#long context`, `#tool use`, `#open source`

---

<a id="item-5"></a>
## [Ex-Apple Engineer Builds Linux GPU Driver for M4 Mac Mini in One Month](https://codyho.dev/blog/gpu-driver/) ⭐️ 8.0/10

An ex-Apple engineer named Cody Ho developed a working Linux GPU driver for the M4 Mac Mini in just one month, relying heavily on large language models (LLMs) to assist with the development. The project was published on his blog and quickly gained attention on Hacker News, where it sparked 196 upvotes and 119 comments. This achievement demonstrates the potential of LLMs to accelerate reverse engineering and driver development for undocumented hardware, which could dramatically lower the barrier to creating open-source GPU drivers. It also raises important questions about the ethics of using LLMs in open-source projects and the acceptability of contributions from former employees of the hardware vendor. The driver targets the M4 Mac Mini's 10-core GPU, which supports hardware-accelerated ray tracing, dynamic caching, and mesh shading. However, the Asahi Linux project has a strict no-AI policy, meaning this LLM-assisted work cannot be upstreamed into the official Asahi Linux kernel; the author was also previously banned from Asahi Linux for concealing his LLM usage and his background as a former Apple engineer.

hackernews · ADevWithAnIdea · Sep 15, 19:30 · [Discussion](https://news.ycombinator.com/item?id=49717638)

**Background**: Apple Silicon Macs, including the M4 Mac Mini, use custom ARM-based chips with integrated GPUs that lack official Linux support. The Asahi Linux project has been reverse-engineering these chips to provide open-source drivers, but progress on newer chips like the M3 and M4 has been slow, especially for GPU acceleration. LLMs are increasingly used in software development to generate code, but their use in open-source projects raises concerns about licensing, originality, and community trust.

<details><summary>References</summary>
<ul>
<li><a href="https://asahilinux.org/2022/12/gpu-drivers-now-in-asahi-linux/">Apple GPU drivers now in Asahi Linux</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_M4">Apple M4 - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=49717638">Building a Linux GPU Driver for the M4 Mac Mini in One Month</a></li>

</ul>
</details>

**Discussion**: Community reactions were mixed: many praised the technical feat and saw it as a prime use case for LLMs in driver development, while others raised ethical concerns about the author's concealed LLM use and former Apple employment, suggesting the code may face upstream rejection. Some also noted that Asahi Linux's no-AI policy means this work cannot be officially integrated, potentially leading to AI-assisted forks.

**Tags**: `#Linux`, `#GPU Driver`, `#Apple Silicon`, `#LLM`, `#Open Source`

---

<a id="item-6"></a>
## [Strix AI agent gains admin access to Baseten's GitHub in 25 minutes](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

Strix AI, an autonomous penetration-testing agent, discovered a leaked GitHub personal access token for the 'basetenbot' account and used it to gain admin and push access to Baseten's main product repository, GitOps cluster repo, and Homebrew tap within 25 minutes. The token was found in Docker build history after the agent located a Baseten image repository. This incident highlights the growing power of AI agents in automated security research, raising urgent questions about consent, rules of engagement, and whether AI-driven red-teaming should be conducted on prospective vendors without prior authorization. It also underscores the risks of credential leakage in CI/CD pipelines and the need for better secret management. The token granted admin and push access to Baseten's main product repo, the GitOps repo driving their clusters, and their Homebrew tap, plus read/write access to other private repositories including customer-specific repos. Baseten responded by making the Harbor project private and rotating the token, but the initial disclosure timeline shows the token remained active for a period after the first report.

hackernews · bearsyankees · Sep 15, 18:11 · [Discussion](https://news.ycombinator.com/item?id=49716476)

**Background**: Strix is an open-source autonomous AI penetration testing tool developed by OmniSecure, Inc., designed to act like a real hacker by dynamically running code, finding vulnerabilities, and validating them with proof-of-concepts. Baseten is an AI inference platform that helps deploy and operate machine learning models in production. GitHub personal access tokens are credentials that allow programmatic access to repositories, and if leaked, can grant unauthorized access to sensitive code and infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.strix.ai/">Introduction - Strix</a></li>
<li><a href="https://github.com/usestrix/strix">GitHub - usestrix/ strix : Open-source AI penetration testing tool to find...</a></li>
<li><a href="https://www.baseten.co/">Inference Platform : Deploy AI models in production | Baseten</a></li>

</ul>
</details>

**Discussion**: Community comments reflect a mix of appreciation for the disclosure and concern about the ethics of running an AI agent against a prospective vendor without prior negotiation. Some note that the agent likely found something a motivated human could find, just faster, and question whether this is a strong advert for Strix over other agents like Claude or Codex. Others praise Baseten's response and highlight the broader issue of credential leakage in Docker build history.

**Tags**: `#security`, `#AI agents`, `#red teaming`, `#disclosure`, `#GitHub`

---

<a id="item-7"></a>
## [Bruce Schneier Calls to End 25 Years of Mass Surveillance](https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html) ⭐️ 8.0/10

Security expert Bruce Schneier, writing with Cindy Cohn in an essay originally published in Lawfare, argues that 25 years of mass surveillance has failed to deliver security and should be ended. The essay, posted on Schneier's blog, sparked a large Hacker News discussion with 823 points and 303 comments. The essay challenges the post-9/11 consensus that pervasive data collection is necessary for security, and its traction reflects growing bipartisan concern about surveillance powers. It could influence policy debates over programs like the Patriot Act and emerging directives such as NSPM-7. Schneier co-authored the piece with Cindy Cohn, and it originally appeared in Lawfare before being reposted on his blog. The discussion highlights historical precedents like pre-Patriot Act FBI data collection and proposals to limit camera networks to local jurisdictions.

hackernews · iamnothere · Sep 15, 11:26 · [Discussion](https://news.ycombinator.com/item?id=49710883)

**Background**: Mass surveillance refers to the systematic observation or data collection of an entire population or a substantial fraction of it, often through methods like wiretapping, CCTV, and data mining. Bruce Schneier is a renowned cryptographer and security technologist who has long criticized government surveillance programs. The essay's title references roughly 25 years since the expansion of surveillance powers following the September 11 attacks and the passage of the Patriot Act.

<details><summary>References</summary>
<ul>
<li><a href="https://www.schneier.com/">Schneier on Security -</a></li>
<li><a href="https://en.wikipedia.org/wiki/Surveillance">Surveillance - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed with Schneier, with some citing the Tao Te Ching to argue that restrictions breed the disorder they aim to prevent, and others noting that FBI data collection predated the Patriot Act. Proposals included building easy-to-use self-hosted services and limiting camera networks to local jurisdictions, while one commenter warned that NSPM-7 will make mass surveillance far more oppressive.

**Tags**: `#surveillance`, `#privacy`, `#security`, `#policy`, `#civil-liberties`

---

<a id="item-8"></a>
## [Java 27 Announced as Community Debates Cadence and Valhalla Delay](https://mail.openjdk.org/archives/list/announce@openjdk.org/thread/ORGGLMN75HFEWP7YL3ZLGHLYHVIBJDYT/) ⭐️ 8.0/10

OpenJDK has announced Java 27 on its official announce mailing list, continuing the platform's six-month release cadence. The announcement drew heavy community discussion, including confirmation that Project Valhalla will slip to Java 28 as a preview feature. Java remains one of the most widely used enterprise languages, so each release shapes the tooling, frameworks, and long-term support decisions of millions of developers. The discussion around Valhalla's delay and Java's role in greenfield projects highlights growing questions about how the platform evolves relative to competitors like C#. Project Valhalla, an experimental OpenJDK effort to add value objects and primitive-like performance to Java's object model, is now expected to arrive as a preview in Java 28 rather than Java 27. Community members also noted that Java releases rarely include two preview rounds of the same feature, unlike some competing platforms.

hackernews · mkurz · Sep 15, 13:13 · [Discussion](https://news.ycombinator.com/item?id=49712041)

**Background**: OpenJDK is the free, open-source reference implementation of Java SE, and since Java 9 Oracle has shipped a new feature release roughly every six months, with periodic long-term support (LTS) versions. Project Valhalla, announced in 2014 and led by Brian Goetz, aims to combine object-oriented abstractions with primitive-like memory efficiency. These frequent releases mean features often land incrementally, and major language changes like Valhalla can take years to mature.

<details><summary>References</summary>
<ul>
<li><a href="https://openjdk.org/projects/valhalla/">Project Valhalla</a></li>
<li><a href="https://en.wikipedia.org/wiki/Project_Valhalla_(Java_language)">Project Valhalla (Java language)</a></li>
<li><a href="https://blogs.oracle.com/java/update-and-faq-on-the-java-se-release-cadence">Update and FAQ on the Java SE Release Cadence | java</a></li>

</ul>
</details>

**Discussion**: Commenters compared Java's cadence favorably to Microsoft's, noting Oracle ships roughly twice as often and bundles less into the platform. Others debated when Java is the right choice for greenfield projects in 2026, recommended a documentary on Java's history, and expressed frustration that Valhalla keeps slipping while hoping for null type safety in their lifetime.

**Tags**: `#Java`, `#OpenJDK`, `#release`, `#Project Valhalla`, `#programming languages`

---

<a id="item-9"></a>
## [Lawfare Calls 153M Driver's License Breach a National Security Disaster](https://www.lawfaremedia.org/article/america%27s-drivers-licence-breach-is-a-national-security-disaster) ⭐️ 8.0/10

On September 14, 2026, Lawfare published an article titled "America's Driver's License Breach Is a National Security Disaster," reframing a massive leak of 153 million US and Canadian driver's licenses — allegedly stolen from identity-verification vendor IDScan.net and sold on the dark web via a service called Nexus — from a consumer data breach into a national security crisis. The FBI and RCMP are investigating, and the story has reportedly reached the inner circle of President Donald Trump. This breach is significant because driver's licenses are a foundational identity document used for KYC checks, age verification, and access to financial and government services, so compromising 153 million of them undermines trust in the entire identity-verification ecosystem. It also raises urgent questions about accountability, systemic security failures, and whether anything will change compared to past disasters like the 2015 OPM breach. The leaked data reportedly includes 153 million US and Canadian driver's licenses, and the breach has been linked to IDScan.net, a SaaS identity-verification provider; the data appeared on the dark web via a site called Nexus. The incident has prompted an FBI probe and comparisons to the 2015 OPM breach, which compromised millions of security-clearance applicants and fingerprints.

hackernews · hn_acker · Sep 15, 15:58 · [Discussion](https://news.ycombinator.com/item?id=49714547)

**Background**: KYC (Know Your Customer) is a regulatory requirement for financial institutions and other businesses to verify customer identities, often using government-issued documents like driver's licenses. Identity-verification SaaS providers such as IDScan.net collect and process these documents on behalf of clients, making them high-value targets for attackers. The 2015 OPM breach is a historical benchmark for US government data compromises, and Lawfare is a non-profit publication focused on national security law and policy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.saasrise.com/news/darkweb-sale-of-153-million-drivers-licenses-highlights-identityverification-saas-flaws-70f76481-5bd0-4e5f-bc30-8cf1cbc76cae">153M Licenses Leak Exposes SaaS Identity‑Verification Gaps - SaasRise</a></li>
<li><a href="https://tech-insider.org/drivers-license-breach-national-security-disaster-2026/">Driver ' s License Breach Is a National Security Disaster</a></li>
<li><a href="https://shattered.io/nexus-breach-national-security-crisis-lawfare-2026/">3M Passports, 153M IDs: Nexus Now a Security Crisis</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters debated accountability and the limits of KYC, with some calling for personal liability and compensation clawbacks for executives and investors, while others argued that KYC provides only an illusion of security and that AI makes fake documents trivial to generate. Several drew parallels to the 2015 OPM breach, questioning whether any concrete changes would follow this time, and one commenter noted that "computer security is an oxymoron."

**Tags**: `#security`, `#privacy`, `#national-security`, `#data-breach`, `#KYC`

---

<a id="item-10"></a>
## [AEF-1 standard for third-party AI evaluators emerges, co-signed by xAI, OpenAI, and Anthropic](https://www.latent.space/p/ainews-aef-1-standard-emerges-for) ⭐️ 8.0/10

The AI Evaluator Forum has released AEF-1, a voluntary standard titled 'Minimum Operating Conditions for Independent Third Party AI Evaluations,' which leading labs including xAI, OpenAI, and Anthropic have all co-signed. The standard gives independent evaluators a baseline set of conditions they can use to demonstrate how they achieved a credible level of independence in their assessments. This marks a significant step toward standardized, credible third-party evaluation of frontier AI models, a key demand from safety advocates who argue that labs cannot credibly audit themselves. Broad co-signing by competing labs suggests emerging industry alignment on governance norms that could shape regulation and public trust in AI systems. AEF-1 is a voluntary standard rather than a binding regulation, and it explicitly treats assessments carried out under terms set by the party being evaluated as a lower standard of independence than a true independent audit. The standard is referenced in related technical work, such as an IETF draft SCITT profile for pre-run evaluation criteria.

rss · Latent Space · Sep 15, 04:50

**Background**: As AI models grow more capable, governments and researchers have pushed for independent evaluation to verify safety, bias, and robustness claims made by developers. The AI Evaluator Forum is a coalition of independent evaluation organizations that worked with partners across the AI ecosystem to define baseline conditions for credible third-party evaluations. Previously, Anthropic CEO Dario Amodei and Google DeepMind co-founder Demis Hassabis publicly called for embedded third-party evaluators and common safety standards, setting the stage for this kind of industry agreement.

<details><summary>References</summary>
<ul>
<li><a href="https://aievaluatorforum.org/initiatives/minimum-operating-conditions">The AI Evaluator Forum brings together leading independent AI ...</a></li>
<li><a href="https://datatracker.ietf.org/doc/draft-ozturk-scitt-prml-profile/">A SCITT Profile for Pre-Run Evaluation Criteria (PRML)</a></li>
<li><a href="https://www.cbsnews.com/video/anthropic-ceo-calls-for-competitors-to-agree-to-third-party-evaluators-in-push-for-ai-safety/">Anthropic CEO calls for competitors to agree to " third - party ..."</a></li>

</ul>
</details>

**Tags**: `#AI evaluation`, `#AI safety`, `#industry standard`, `#OpenAI`, `#Anthropic`

---

<a id="item-11"></a>
## [Voodoo Dynamic Quant Released Under MIT License](https://www.reddit.com/r/LocalLLaMA/comments/1wgszma/voodoo_dynamic_quant_now_mit_licensed/) ⭐️ 8.0/10

The creator of Voodoo Quant, a novel dynamic quantization method that uses gradient descent to optimize per-tensor quantization layouts for GGUF models, has open-sourced the full toolset under the MIT license on GitHub. Previously kept private for two months, the release includes complete tools for training custom dynamic quants, currently configured for Qwen models but adaptable to other architectures. This open-source release enables the local LLM community to create custom dynamic quants and potentially inspires further research into gradient-descent-based quantization optimization. It also increases transparency in a field where proprietary methods like Unsloth Dynamic 3.0 remain undisclosed, potentially leading to broader adoption and improvements. Voodoo Quant works by running all quantization levels simultaneously and training a scalar gate per tensor per quant level using gradient descent, with a tau annealing schedule and softmax to freeze selections, optimizing for KL divergence against a BF16 reference and a target filesize. The author notes it is research-grade, excels at aggressive quantization levels on smaller models, but is outperformed by Unsloth Dynamic 3.0 at mid-to-high levels and has not been studied at larger model sizes.

reddit · r/LocalLLaMA · /u/1ncehost · Sep 15, 06:59

**Background**: GGUF is a binary file format used by llama.cpp for efficient loading and inference of quantized LLMs, supporting various quantization levels from 2-bit to 8-bit. Dynamic quantization in this context means selecting different quantization levels for each tensor based on the model checkpoint size, unlike static quants that use fixed assignments. Voodoo Quant introduces a novel approach by using gradient descent to optimize these per-tensor selections, contrasting with traditional static analysis methods.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GGUF">GGUF - Wikipedia</a></li>
<li><a href="https://developer.nvidia.com/blog/per-tensor-and-per-block-scaling-strategies-for-effective-fp8-training/">Per-Tensor and Per-Block Scaling Strategies for Effective FP8 Training</a></li>
<li><a href="https://medium.com/@isanghao/optimizing-llm-inference-with-dynamic-quantization-056026701667">Optimizing LLM Inference with Dynamic Quantization - Medium</a></li>

</ul>
</details>

**Tags**: `#quantization`, `#GGUF`, `#local-llm`, `#model-compression`, `#open-source`

---

<a id="item-12"></a>
## [LynnReal-Omni: 32B Unified Video Diffusion Model with ComfyUI Nodes](https://www.reddit.com/r/StableDiffusion/comments/1wh8hov/lynnrealomni_built_on_minmax_h3_weights_comfy/) ⭐️ 8.0/10

LynnReal-Omni is a new unified 32B multimodal diffusion transformer built on the MiniMax H3 architecture that handles text-to-video, image-to-video, pose-guided generation, editing, restoration, and streaming long-video generation in a single framework at four-step fast generation. Its weights and ComfyUI nodes are now publicly available, alongside a 27B Flash variant that performs three-step generation and can render a 22-frame 540p video in 377 ms on a single H100. This release consolidates many previously separate video generation and editing tasks into one open-weight model, which could significantly simplify workflows for the Stable Diffusion and ComfyUI community. The Flash variant's real-time rendering speed lays groundwork for streaming video generation, potentially enabling interactive and agent-driven visual creation. The Standard model generates and decodes a 22-frame 540p video in 843 ms on a single H100, while the Flash variant reduces this to 377 ms through model and decoding acceleration including a lightweight VAE decoder. The framework accepts heterogeneous inputs such as appearance references, editable 3D renders, and game recordings, and introduces MSAVP, a 100-prompt, 20-metric evaluation design covering instruction following, plausibility, visual quality, temporal behavior, and audio coordination.

reddit · r/StableDiffusion · /u/AgeNo5351 · Sep 15, 18:25

**Background**: MiniMax H3 is an open-weight omni-modal video model with a 33B-parameter architecture that supports native 2K output, stereo audio, and instruction-based editing. Multimodal diffusion transformers, popularized by models like Stable Diffusion 3, use a transformer backbone to generate content from multiple input modalities. ComfyUI is an open-source node-based interface for building generative AI workflows, and the release of dedicated nodes means users can run LynnReal-Omni directly within that ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://vesoa.ai/minimax-h3">MiniMax H 3 : Open Omni-Modal AI Video Model | 2K Native Audio</a></li>
<li><a href="https://encord.com/blog/stable-diffusion-3-text-to-image-model/">Stable Diffusion 3: Multimodal Diffusion Transformer Model ...</a></li>
<li><a href="https://docs.comfy.org/">ComfyUI Official Documentation - ComfyUI</a></li>

</ul>
</details>

**Tags**: `#diffusion-models`, `#video-generation`, `#multimodal`, `#comfyui`, `#open-weights`

---

<a id="item-13"></a>
## [Meridian brings camera control and bullet time to existing videos](https://www.reddit.com/r/StableDiffusion/comments/1wh89rt/meridian_camera_control_fov_and_bullet_time_for/) ⭐️ 8.0/10

Meridian is a new video-to-video model built on MiniMax-H3 that generates new viewpoints of existing footage, letting users combine orbits, dollies, and slides into complex camera paths while controlling position, viewing direction, and field of view. It also offers a bullet time mode that freezes action while the camera keeps moving, plus a fast preview that lets users check framing before spending GPU time on generation. This represents a significant step for AI-driven video editing, since most prior camera-control work focused on text-to-video generation rather than re-shooting user-provided footage. If the artifacts on large viewpoint changes can be reduced, it could give filmmakers and creators a practical post-production tool for virtual camera moves. The model is still early-stage, and large viewpoint changes can produce artifacts, so results are most reliable for modest camera moves. It is released by Viggle with an online demo on Hugging Face Spaces and weights on the Hugging Face Hub, and the fast preview works once geometry has been reconstructed.

reddit · r/StableDiffusion · /u/init-5 · Sep 15, 18:17

**Background**: MiniMax-H3 is an open-weights, general-purpose multimodal generation model that can combine text, images, video, and audio to produce 2K video with native stereo audio. Video-to-video camera control is a growing research area, with prior work such as CameraCtrl adding camera pose control to video diffusion models and ReCapture enabling generative camera controls for user-provided videos. Bullet time is the well-known "Matrix-style" effect where action freezes or slows dramatically while the camera continues to move around the scene.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H 3 : An Open Model Breaking the Boundaries Between Tasks...</a></li>
<li><a href="https://hehao13.github.io/projects-CameraCtrl/">CameraCtrl: Enabling Camera Control for Video Diffusion Models - Hao He</a></li>
<li><a href="http://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_ReCapture_Generative_Video_Camera_Controls_for_User-Provided_Videos_using_Masked_CVPR_2025_paper.pdf">[PDF] ReCapture: Generative Video Camera Controls for User-Provided Videos ...</a></li>

</ul>
</details>

**Tags**: `#video-generation`, `#camera-control`, `#AI`, `#stable-diffusion`, `#MiniMax-H3`

---

<a id="item-14"></a>
## [Prior Labs Releases TabPFN-3.5, New SOTA Tabular Foundation Model](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs released TabPFN-3.5 today, a new tabular foundation model that tops both the TabArena and BeyondArena benchmarks and is claimed to be SOTA for datasets with up to 1M rows and 20k features. The release includes three variants: TabPFN-3.5-Fast (in alpha, 6x faster than the base model), TabPFN-3.5-Thinking (available via API, trading compute for accuracy), and TabPFN-3.5-Plus. Tabular data remains one of the most common data types in industry, yet it has lagged behind vision and language in foundation-model progress; a model that leads major benchmarks with large Elo gains could shift how practitioners approach tabular prediction tasks. The +250 Elo improvement over the strongest previous baseline on BeyondArena suggests a substantial capability jump rather than incremental tuning. On BeyondArena, TabPFN-3.5 leads on text-rich, high-cardinality, and high-dimensional data, with +250 Elo over the strongest previous baseline and +150 Elo ahead of the previous overall leader. TabPFN-3.5-Thinking adds +20 Elo over the base model on BeyondArena and +44 Elo on TabArena, though the Fast variant is still in alpha.

reddit · r/MachineLearning · /u/tuanacelik · Sep 15, 16:18

**Background**: TabPFN is a transformer-based foundation model from Prior Labs that uses in-context learning to solve tabular prediction problems in a single forward pass, rather than requiring per-dataset training. TabArena is a continuously maintained 'living' benchmark for tabular machine learning, while BeyondArena is a newer benchmark spanning IID, temporal, and grouped tasks across 142 datasets to test how well tabular foundation models generalize beyond the IID setting. Prior releases such as TabPFN-2.5 and TabPFN-3 established the line of work that TabPFN-3.5 extends.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/PriorLabs/TabPFN">GitHub - PriorLabs/ TabPFN : TabPFN : Foundation Model for Tabular ...</a></li>
<li><a href="https://github.com/autogluon/tabarena">GitHub - autogluon/tabarena: A Living Benchmark for Machine Learning ...</a></li>
<li><a href="https://arxiv.org/abs/2506.16791">TabArena: A Living Benchmark for Machine Learning on Tabular Data</a></li>

</ul>
</details>

**Tags**: `#tabular-data`, `#foundation-models`, `#machine-learning`, `#benchmark`, `#SOTA`

---

<a id="item-15"></a>
## [Alibaba open-sources hybrid LLM code review tool, gaining 2,756 stars in a day](https://github.com/alibaba/open-code-review) ⭐️ 8.0/10

Alibaba has open-sourced open-code-review, a Go-based CLI code review tool that combines deterministic pipelines with LLM agents, and it gained 2,756 GitHub stars in a single day, bringing its total to 29,032 stars and 2,067 forks. The tool produces precise line-level comments and ships with a built-in multi-language ruleset covering NPE, thread-safety, XSS, and SQL injection, while remaining compatible with OpenAI and Anthropic APIs. This release signals that large-scale engineering organizations are converging on hybrid architectures that pair deterministic static analysis with LLM reasoning, rather than relying on either alone. Because it is battle-tested at Alibaba's scale and freely available, it could become a reference implementation for teams building AI-assisted code review into their CI pipelines. The hybrid design uses deterministic pipelines for checks that require precision and reproducibility, while LLM agents handle contextual or semantic review, which helps control token costs and reduce false positives. The tool is written in Go and supports OpenAI- and Anthropic-compatible model endpoints, making it deployable with either commercial or self-hosted models.

github_trending · GitHub Trending · Sep 16, 03:55

**Background**: Code review tools traditionally fall into two camps: deterministic static analysis, which applies fixed rules to find issues like null pointer exceptions (NPE), SQL injection, or XSS, and LLM-based review, which uses large language models to reason about code semantics. Static analysis is fast and reproducible but limited to predefined patterns, while LLM review is flexible but can be slow, costly, and prone to hallucinated findings. A hybrid approach runs the cheap deterministic checks first and then invokes LLM agents only where deeper reasoning is needed, which is the architecture Alibaba has adopted here.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/alibaba/open-code-review">GitHub - alibaba/open-code-review: Fast, efficient, battle-tested at ...</a></li>
<li><a href="https://blog.codacy.com/deterministic-static-analysis-for-ai-coding-workflows-how-to-cut-token-cost-without-weakening-code-review">Deterministic Static Analysis for AI Coding Workflows - Codacy | Blog</a></li>
<li><a href="https://arxiv.org/pdf/2409.02977">Large Language Model-Based Agents for Software Engineering...</a></li>

</ul>
</details>

**Tags**: `#code-review`, `#static-analysis`, `#llm`, `#security`, `#developer-tools`

---