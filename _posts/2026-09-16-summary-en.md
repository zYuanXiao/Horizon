---
layout: default
title: "Horizon Summary: 2026-09-16 (EN)"
date: 2026-09-16
lang: en
---

> From 142 items, 15 important content pieces were selected

---

1. [Google DeepMind Launches Gemini 3.8 Live and Extended Thinking](#item-1) ⭐️ 9.0/10
2. [Alibaba open-sources hybrid LLM code review tool](#item-2) ⭐️ 8.0/10
3. [TradingAgents: Multi-Agent LLM Framework for Financial Trading Gains 727 Stars](#item-3) ⭐️ 8.0/10
4. [Vidu S2 Enables Real-Time Interactive and Spatial Video Generation](#item-4) ⭐️ 8.0/10
5. [Atria Dawn Preview: A Foundation Agentic Model for Scientific Research](#item-5) ⭐️ 8.0/10
6. [Strix.ai AI agent finds Baseten GitHub admin token in 25 minutes](#item-6) ⭐️ 8.0/10
7. [IEEE Spectrum Explores the 2026 Inference Hardware Revolution](#item-7) ⭐️ 8.0/10
8. [Bruce Schneier: 25 Years of Mass Surveillance Is Enough](#item-8) ⭐️ 8.0/10
9. [Driver's License Breach Exposes 153 Million Americans](#item-9) ⭐️ 8.0/10
10. [AEF-1 standard for third-party AI evaluators emerges with xAI, OpenAI, Anthropic backing](#item-10) ⭐️ 8.0/10
11. [CrofAI exposed as OpenRouter wrapper with 20x markup, then vanishes](#item-11) ⭐️ 8.0/10
12. [Apple Ships Foundation Models Natively in macOS 27](#item-12) ⭐️ 8.0/10
13. [Voodoo Dynamic Quant Open-Sourced Under MIT License](#item-13) ⭐️ 8.0/10
14. [LynnReal-Omni: 32B Unified Video Diffusion Model with Open Weights and ComfyUI Nodes](#item-14) ⭐️ 8.0/10
15. [SHADOW-50M: 44M ternary LLM ships in 19.8 MB, runs 1,900 tok/s on CPU](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google DeepMind Launches Gemini 3.8 Live and Extended Thinking](https://deepmind.google/blog/introducing-gemini-3-8-live-and-3-8-live-extended-thinking/) ⭐️ 9.0/10

Google DeepMind announced Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking, two new native speech-to-speech models that support real-time multimodal interaction, background tool calling, and support for 97 languages. Gemini 3.8 Live is built for scale and low-latency conversation, while the Extended Thinking variant targets high-complexity tasks with multi-step reasoning. The release intensifies competition in real-time voice AI, directly mirroring OpenAI's GPT-Live family and pushing production-grade voice agents closer to mainstream adoption. It also signals that Google is betting on native speech-to-speech plus extended reasoning as the next frontier for LLM assistants. The models handle complex reasoning, real-time visual context, and background task execution without interrupting the conversation, and they support 97 languages. Community testers noted low latency and good handling of thick accents, though one demo drew criticism for a chess blunder.

rss · Google DeepMind Blog · Sep 15, 17:05

**Background**: Gemini is Google DeepMind's flagship family of multimodal large language models, and the 'Live' line refers to models designed for real-time, speech-to-speech interaction rather than text-only chat. 'Extended Thinking' denotes a mode where the model spends more compute on step-by-step reasoning before answering, a pattern popularized by recent reasoning-focused LLMs. Native speech-to-speech means audio goes in and audio comes out without an intermediate text transcription step, which typically reduces latency and preserves tone.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking</a></li>
<li><a href="https://www.marktechpost.com/2026/09/15/google-releases-gemini-3-8-live-and-3-8-live-extended-thinking-for-production-grade-voice-agents/">Google Releases Gemini 3.8 Live and 3.8 Live Extended Thinking for Production Grade Voice Agents - MarkTechPost</a></li>
<li><a href="https://www.thurrott.com/a-i/google-gemini-a-i/341685/google-announces-gemini-3-8-live-and-3-8-live-extended-thinking">Google Announces Gemini 3.8 Live and 3.8 Live Extended Thinking - Thurrott.com</a></li>

</ul>
</details>

**Discussion**: Commenters were largely positive, praising low latency, pleasant voices, and strong multilingual ability, with one user calling Afrikaans live chat the most joyful LLM experience they have had. Others questioned whether Google is still trailing rivals and when Gemini 4 might arrive, while one critic mocked a demo video in which the model lost to a common chess checkmate pattern.

**Tags**: `#AI`, `#Google DeepMind`, `#Gemini`, `#LLM`, `#Multimodal`

---

<a id="item-2"></a>
## [Alibaba open-sources hybrid LLM code review tool](https://github.com/alibaba/open-code-review) ⭐️ 8.0/10

Alibaba has open-sourced open-code-review, a Go-based code review tool that combines deterministic pipelines with LLM agents, gaining 2,756 stars in a single day and reaching roughly 29,000 total stars. It produces precise line-level comments and ships with built-in multi-language security rules covering NPE, thread-safety, XSS, and SQL injection, while supporting OpenAI- and Anthropic-compatible APIs. Code review is a major bottleneck in software engineering, and pure-LLM reviewers often produce noisy or hallucinated feedback, so a battle-tested hybrid design from Alibaba could set a new standard for reliable AI-assisted review. The rapid star growth signals strong developer demand for tools that blend deterministic static analysis with LLM reasoning rather than relying on either alone. The tool is written in Go and pairs deterministic pipelines with LLM agents to deliver precise line-level comments, and its built-in ruleset targets common vulnerability classes such as NPE, thread-safety issues, XSS, and SQL injection across multiple languages. It is compatible with both OpenAI and Anthropic APIs, giving teams flexibility in which model provider they use.

github_trending · GitHub Trending · Sep 16, 03:45

**Background**: Traditional code review relies on deterministic static analysis tools that apply fixed rules to detect bugs, but these tools struggle with context-dependent issues. Large language models can reason about code semantics but tend to hallucinate and give vague feedback. Alibaba's tool is a hybrid: deterministic pipelines handle rule-based checks while LLM agents handle nuanced reasoning, and the result is validated at Alibaba's own engineering scale. NPE (null pointer exception) is a common Java runtime error, while XSS and SQL injection are classic web security vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/alibaba/open-code-review">GitHub - alibaba/open-code-review: Fast, efficient, battle-tested at ...</a></li>
<li><a href="https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk">OpenAI SDK compatibility - Claude Platform Docs</a></li>
<li><a href="https://www.reddit.com/r/AI_Agents/comments/1udp99l/the_most_reliable_data_agent_ive_shipped_is_90/">The most reliable data agent I've shipped is ~90% deterministic code ...</a></li>

</ul>
</details>

**Discussion**: Community discussion around hybrid deterministic-plus-LLM agent architectures is broadly positive, with practitioners noting that keeping most logic deterministic and using the LLM mainly for intent parsing yields far more reliable results than pure LLM approaches. Some commenters caution that OpenAI-compatible endpoints do not always support advanced features like reasoning/thinking modes, which is worth verifying before deployment.

**Tags**: `#code-review`, `#static-analysis`, `#llm`, `#developer-tools`, `#go`

---

<a id="item-3"></a>
## [TradingAgents: Multi-Agent LLM Framework for Financial Trading Gains 727 Stars](https://github.com/TauricResearch/TradingAgents) ⭐️ 8.0/10

TauricResearch/TradingAgents, a Python framework that uses multiple LLM-powered agents for financial trading, gained 727 stars in a single day and now has over 106,000 total stars on GitHub. The project, described in an arXiv paper (2412.20138), assigns specialized roles to LLM agents to break down complex trading objectives into manageable tasks. This rapid community validation highlights growing interest in applying multi-agent LLM systems to high-stakes domains like finance, potentially enabling more sophisticated and automated trading strategies. It represents a practical, research-backed use case that could influence both academic research and real-world trading tools. The framework works with any market covered by Yahoo Finance, using exchange-suffixed tickers, and automatically resolves company identity and alpha benchmarks per market. It is written in Python and has over 20,000 forks, indicating active community engagement.

github_trending · GitHub Trending · Sep 16, 03:45

**Background**: TradingAgents is inspired by the structure of real-world trading firms, where different specialists (e.g., fundamental analysts, sentiment analysts) collaborate to make decisions. The framework uses large language models (LLMs) as agents that each play a specific role, mimicking this division of labor. This approach allows complex trading objectives to be decomposed into smaller, manageable tasks that individual agents can handle.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/TauricResearch/TradingAgents">TauricResearch/ TradingAgents : TradingAgents : Multi - Agents LLM ...</a></li>
<li><a href="https://arxiv.org/abs/2412.20138">TradingAgents: Multi-Agents LLM Financial Trading Framework - arXiv</a></li>
<li><a href="https://tradingagents-ai.github.io/">TradingAgents: Multi-Agents LLM Financial Trading Framework</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#multi-agent`, `#financial-trading`, `#Python`, `#framework`

---

<a id="item-4"></a>
## [Vidu S2 Enables Real-Time Interactive and Spatial Video Generation](https://huggingface.co/papers/2609.11638) ⭐️ 8.0/10

Vidu S2 introduces two real-time models: Vidu S2-Avatar, an interactive digital-character model, and Vidu S2-Editing, a real-time video editing model. Compared with Vidu S1, Vidu S2-Avatar supports real-time 720p video generation, dynamic references that can be updated at any moment, and stronger instruction following such as dancing, while Vidu S2-Editing enables real-time style rendering, clothing replacement, character replacement, and background replacement. This marks a significant step toward real-time, interactive video generation that could reshape content creation, virtual avatars, and live streaming workflows. The availability of a playable online demo and claims of outperforming all baselines suggest strong practical impact for AI/ML and graphics communities. The models support high-resolution 720p output and dynamic reference updates, and the team also explores the feasibility of real-time spatial video generation for both Avatar and Editing. A playable online demo is available at https://vidu.com/vidu-stream.

huggingface_papers · Hugging Face Papers · Sep 15, 00:00

**Background**: Real-time video generation is challenging because it requires maintaining temporal and spatial consistency while responding to user input with low latency. Spatial video generation, as explored in frameworks like Spatia, preserves a 3D scene point cloud as persistent memory to maintain long-term consistency, while dynamic reference updates allow the model to swap or adjust reference images on the fly. Vidu S2 builds on the earlier Vidu S1 and targets interactive applications such as digital avatars and live video editing.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.15716">[2512.15716] Spatia: Video Generation with Updatable Spatial Memory</a></li>
<li><a href="https://www.vidu.com/ai-reference-to-video">Reference to Video AI — Keep Characters Consistent | Vidu AI</a></li>

</ul>
</details>

**Tags**: `#video-generation`, `#real-time`, `#interactive`, `#spatial-video`, `#AI`

---

<a id="item-5"></a>
## [Atria Dawn Preview: A Foundation Agentic Model for Scientific Research](https://huggingface.co/papers/2609.15818) ⭐️ 8.0/10

Researchers introduced Atria Dawn Preview, a foundation agentic language model trained via a Verifiable Experience Pipeline that links tool-mediated interactions to executable environments and externally verified outcomes. Across 16 benchmarks covering real-world research, engineering, and digital work, it is competitive with frontier agents and achieves the highest reported score on five of them. The work signals a shift from task-level execution to project-level human-AI partnership, where agents propose methods and implement revisions while humans retain final decisions and guide exploration. This has implications for how scientific research is conducted and how oversight and accountability are preserved as AI agents become participants in building their own successors. The study analyzed 769 task records from 56 participants alongside agent logs, finding that participants rated about one-third of completed AI-assisted tasks as infeasible without AI. The paper is a preview release, and the authors note that progress toward more autonomous AI research requires advancing both discovery capacity and meaningful human oversight.

huggingface_papers · Hugging Face Papers · Sep 15, 00:00

**Background**: Agentic AI refers to semi- or fully autonomous systems that can perceive, reason, and act on their own, typically combining language models with extensible tools. Foundation models are large pretrained models adapted to many downstream tasks, and benchmarks are standardized tests used to compare system performance. The Verifiable Experience Pipeline described here trains the model by grounding its tool use in executable environments whose outcomes can be externally checked, rather than relying only on human preference or static data.

<details><summary>References</summary>
<ul>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#agentic AI`, `#language models`, `#scientific research`, `#benchmarks`, `#human-AI collaboration`

---

<a id="item-6"></a>
## [Strix.ai AI agent finds Baseten GitHub admin token in 25 minutes](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

Strix.ai reported that its autonomous penetration-testing agent discovered an exposed GitHub personal access token for 'basetenbot' within 25 minutes, granting admin and push access to Baseten's main product repo, GitOps repo, and Homebrew tap. Baseten responded by making the Harbor project private and rotating the token, but the incident sparked debate over unsolicited AI-driven security testing on a prospective vendor. This incident highlights the growing power of AI agents to rapidly uncover exposed credentials that humans might overlook, raising urgent questions about disclosure ethics when security testing is performed on a prospective vendor without prior agreement. It also underscores the critical risk of leaked GitHub tokens, which can grant broad access to an organization's code and infrastructure. The token was found in Docker build history after the agent located a Baseten image repository, and it provided read/write access to other private repositories, including customer-specific ones. Baseten's security team confirmed the issue as critical on July 14 and asked Strix to securely delete any images they had pulled.

hackernews · bearsyankees · Sep 15, 18:11 · [Discussion](https://news.ycombinator.com/item?id=49716476)

**Background**: Baseten is an AI inference platform that helps companies deploy and serve machine learning models in the cloud. Strix.ai offers autonomous AI penetration-testing agents that mimic real hackers to find vulnerabilities in code, APIs, and cloud infrastructure. GitHub personal access tokens are credentials that allow programmatic access to repositories; if exposed, they can be exploited to gain unauthorized control over an organization's codebase.

<details><summary>References</summary>
<ul>
<li><a href="https://www.strix.ai/">Strix</a></li>
<li><a href="https://github.com/usestrix/strix">GitHub - usestrix/strix: Open-source AI penetration testing tool to find and ...</a></li>
<li><a href="https://grokipedia.com/page/Baseten">Baseten</a></li>

</ul>
</details>

**Discussion**: Commenters debated the ethics of running an AI pentesting agent against a prospective vendor without prior negotiation, with some noting that the agent's speed in finding exposed secrets is impressive but not necessarily unique. Others questioned whether the disclosure was a genuine security contribution or a marketing stunt, and highlighted the broader issue of how many similar tokens might be exposed.

**Tags**: `#security`, `#AI agents`, `#disclosure`, `#GitHub`, `#ethics`

---

<a id="item-7"></a>
## [IEEE Spectrum Explores the 2026 Inference Hardware Revolution](https://spectrum.ieee.org/inference-hardware-revolution) ⭐️ 8.0/10

IEEE Spectrum published an in-depth article on the emerging 2026 inference hardware revolution, highlighting novel architectures such as logarithmic number systems and rack-scale accelerators, including Tensordyne's Napier rack-scale hardware that claims up to 1,300 tokens per second per user. The piece also notes that Anthropic is paying over a billion dollars per month to lease spare compute from LLM competitor SpaceXAI. As AI inference demand grows, hardware innovation is shifting from a single scaling axis toward a proliferation of architectural approaches, much like the CPU's evolution after transistor scaling slowed. This could reshape the economics of AI deployment and determine which companies lead the next phase of AI infrastructure. Tensordyne's Napier uses a logarithmic number system where storing numbers as exponents lets the chip add instead of multiply, since multiplier circuits draw more power and use more die area than adders. The article also highlights rack-scale designs where many accelerators participate in a single high-speed interconnect domain.

hackernews · vinhnx · Sep 15, 14:24 · [Discussion](https://news.ycombinator.com/item?id=49713024)

**Background**: A logarithmic number system (LNS) is an arithmetic representation that stores real numbers as their exponents, simplifying multiplication, division, roots, and powers into addition and subtraction. Rack-scale accelerators are dense systems in which every GPU or accelerator in a rack operates within a single high-speed interconnect domain, such as NVIDIA's NVLink, enabling much larger models to be served efficiently. AI inference hardware refers to the physical infrastructure that runs a trained model on new data to produce predictions or generations, as opposed to training hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Logarithmic_number_system">Logarithmic number system</a></li>
<li><a href="https://theoutpost.ai/news-story/amd-challenges-nvidia-with-ambitious-rack-scale-ai-accelerators-for-2026-15487/">AMD Challenges NVIDIA with Ambitious Rack - Scale AI Accelerators ...</a></li>
<li><a href="https://telnyx.com/resources/ai-inference-hardware">AI Inference Hardware Guide for Production Deployments</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters largely praised the article, with one drawing a parallel between AI inference evolution and the multi-axis proliferation of CPU innovations after transistor scaling slowed. Others highlighted the logarithmic number system's cleverness, noted that most future benchmark gains may come from this side of the stack, and expressed surprise at the billion-dollar monthly compute lease figure.

**Tags**: `#AI inference`, `#hardware acceleration`, `#computer architecture`, `#logarithmic number systems`, `#IEEE Spectrum`

---

<a id="item-8"></a>
## [Bruce Schneier: 25 Years of Mass Surveillance Is Enough](https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html) ⭐️ 8.0/10

Security expert Bruce Schneier published an essay titled "25 Years of Mass Surveillance Is Enough," arguing that a quarter-century of mass surveillance programs has failed to deliver promised security benefits and should be dismantled. The piece, published on his Schneier on Security blog and cross-posted to Lawfare, sparked a large Hacker News discussion with 822 points and 303 comments. Schneier is one of the most influential voices in computer security, and his argument that mass surveillance fails on its own terms—rather than only on civil-liberties grounds—reframes the policy debate at a time when surveillance powers are expanding. The discussion highlights growing concern that tools like ICE's surveillance of protesters and emerging policies such as NSPM-7 are making mass surveillance more oppressive and pervasive. Schneier's essay notes that mass surveillance is now a routine law-enforcement tool, with ICE using it in immigration actions and against people exercising First Amendment rights to protest. Commenters also point to the Patriot Act as an obvious turning point, while noting the FBI ran public data-collection and keyword-watching programs even earlier.

hackernews · iamnothere · Sep 15, 11:26 · [Discussion](https://news.ycombinator.com/item?id=49710883)

**Background**: Mass surveillance refers to the intricate monitoring of an entire population or a substantial fraction of it, a practice expanded dramatically after the 2001 Patriot Act broadened government spying authority. Bruce Schneier is a cryptographer and public-interest technologist known for books such as Data and Goliath, in which he argues that mass surveillance cannot stop terrorist attacks. Debates over surveillance often center on whether such programs actually improve security or mainly erode privacy and civil liberties.

<details><summary>References</summary>
<ul>
<li><a href="https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html">25 Years of Mass Surveillance Is Enough - Schneier on Security</a></li>
<li><a href="https://www.lawfaremedia.org/article/25-years-of-mass-surveillance-is-enough">25 Years of Mass Surveillance Is Enough | Lawfare</a></li>
<li><a href="https://www.vice.com/en/article/bruce-schneier-mass-surveillance-wont-stop-terror-876/">This Security Expert Thinks Mass Surveillance Doesn't Stop Terror...</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed with Schneier, with one invoking the Tao Te Ching to argue that restriction breeds the disorder it aims to prevent, and another tracing surveillance ambitions back before the Patriot Act. Practical proposals included building and widely distributing easy-to-use self-hosted services to leverage First and Fourth Amendment protections, and limiting camera networks to local jurisdictions rather than giving federal agencies eyes everywhere. Several expressed alarm that NSPM-7 will make mass surveillance far more oppressive.

**Tags**: `#surveillance`, `#privacy`, `#security`, `#policy`, `#civil-liberties`

---

<a id="item-9"></a>
## [Driver's License Breach Exposes 153 Million Americans](https://www.lawfaremedia.org/article/america%27s-drivers-licence-breach-is-a-national-security-disaster) ⭐️ 8.0/10

A massive data breach has reportedly exposed the driver's license records of approximately 153 million Americans, prompting an FBI investigation into what could be one of the largest-ever leaks of government-issued identity documents in North America. The Lawfare article frames this incident as a national security disaster, igniting debate over corporate accountability and the failures of identity verification systems. This breach affects nearly half of the U.S. adult population, creating severe risks of identity theft, fraud, and espionage, while exposing systemic weaknesses in how companies handle sensitive personal data. It underscores the urgent need for stronger corporate accountability and more robust KYC (Know Your Customer) verification processes across industries. The breach reportedly involves driver's license scans stored by a third-party identity verification company, and if confirmed, it would surpass many previous data breaches in scale. The FBI is investigating, but the full scope and the identity of the attackers remain unclear, raising concerns about the security of centralized identity databases.

hackernews · hn_acker · Sep 15, 15:58 · [Discussion](https://news.ycombinator.com/item?id=49714547)

**Background**: Driver's licenses are among the most widely used forms of government-issued identification in the United States, often required for opening bank accounts, boarding flights, and verifying identity for employment. KYC (Know Your Customer) regulations mandate that businesses verify customer identities to prevent fraud and money laundering, but these processes often rely on third-party vendors that store sensitive documents. The 2015 OPM breach, which compromised the personal data of millions of federal employees and security clearance applicants, serves as a historical parallel for the scale and national security implications of such incidents.

<details><summary>References</summary>
<ul>
<li><a href="https://www.usnews.com/news/us/articles/2026-09-02/fbi-says-it-is-investigating-report-that-millions-of-us-drivers-licenses-exposed-in-data-breach">FBI Probes Report of Data Breach Exposing Millions of Drivers ...</a></li>
<li><a href="https://time.com/article/2026/09/03/fbi-probes-reported-dark-web-drivers-license-breach/">FBI Probes Report of Breach Exposing 153 Million Driver's License Scans</a></li>

</ul>
</details>

**Discussion**: Commenters expressed deep frustration with the broken state of identity verification, with some calling for personal liability and clawbacks for executives and investors of breached companies. Others criticized KYC checks as ineffective, especially as AI makes forging documents easier, and drew parallels to the 2015 OPM breach, questioning whether any meaningful changes will occur this time.

**Tags**: `#security`, `#privacy`, `#data-breach`, `#national-security`, `#KYC`

---

<a id="item-10"></a>
## [AEF-1 standard for third-party AI evaluators emerges with xAI, OpenAI, Anthropic backing](https://www.latent.space/p/ainews-aef-1-standard-emerges-for) ⭐️ 8.0/10

The AI Evaluator Forum published AEF-1, a proposed baseline standard and checklist for independent third-party AI evaluations, covering areas such as access and conflicts of interest. The initiative has been co-signed by major AI labs including xAI, OpenAI, and Anthropic, signaling broad industry buy-in. This is a significant step toward professionalizing and standardizing how third-party AI evaluations are conducted, which could shape AI governance and accountability practices across the industry. If widely adopted, AEF-1 could give regulators, enterprises, and the public more trustworthy, independent assessments of AI systems. AEF-1 is framed as a set of 'minimum operating conditions' that third-party evaluators can use to demonstrate how they meet baseline requirements, with emphasis on access to models and managing conflicts of interest. It is a proposed standard rather than a binding regulation, so its real-world impact will depend on voluntary adoption by labs and evaluators.

rss · Latent Space · Sep 15, 04:50

**Background**: As AI systems grow more capable, independent third-party evaluations are seen as crucial for assessing risks because they are separate from the interests of the companies building the models. However, the field has lacked common standards for what counts as a credible evaluation, including how evaluators get access to models and how they handle conflicts of interest. AEF-1, published by the AI Evaluator Forum, aims to fill that gap by defining baseline operating conditions that evaluators can publicly attest to.

<details><summary>References</summary>
<ul>
<li><a href="https://aievaluatorforum.org/initiatives/minimum-operating-conditions">AEF-1: Minimum Operating Conditions for Independent Third Party AI ...</a></li>
<li><a href="https://www.latent.space/p/ainews-aef-1-standard-emerges-for">[AINews] AEF-1 standard emerges for Third Party Evaluators, as Xai ...</a></li>
<li><a href="https://hai.stanford.edu/news/strengthening-ai-accountability-through-better-third-party-evaluations">Strengthening AI Accountability Through Better Third Party ...</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#AI evaluation`, `#standards`, `#industry news`, `#OpenAI`

---

<a id="item-11"></a>
## [CrofAI exposed as OpenRouter wrapper with 20x markup, then vanishes](https://www.reddit.com/r/LocalLLaMA/comments/1wgwe4n/crofai_cheapest_inference_provider_in_the_world/) ⭐️ 8.0/10

CrofAI, which marketed itself as the cheapest inference provider in the world, was exposed as an OpenRouter wrapper that silently routed requests for expensive models like kimi-k3 to cheaper models such as GLM 5.3 Flash, charging up to 20x markup on output tokens. After denying the allegations, publishing a fake 'team takeover' blog post, and being reminded of wire fraud, the owner deleted nahcrof.com and crof.ai, removed the Twitter account, and made the /r/CrofAI subreddit private around September 15. This case highlights a serious trust and transparency problem in the third-party LLM inference market, where users cannot easily verify which model actually serves their requests. It serves as a warning to developers and companies relying on cheap API resellers, and could push the community toward more verifiable providers or self-hosted inference. The investigation found that CrofAI's 'own model family' was also fake: greg-2-ultra routed to GLM 5.2, greg-1-mini to Qwen 3.5 9B, and greg-2-super, greg-1 and greg-1-super to Kimi K2.7 Code, all at significant markups. CrofAI's hardware claims also failed scrutiny, since running Kimi K3 at Q2_K quantization needs about 802GiB while the largest RTX PRO 6000 machine on Vast offers only 765GiB, and a DGX Spark with 128GB cannot run deepseek-v4-flash-0731.

reddit · r/LocalLLaMA · /u/SorosAhaverom · Sep 15, 10:19

**Background**: OpenRouter is a unified API marketplace that lets developers access hundreds of AI models from many providers through a single interface, and it is widely used to compare prices and availability. Inference providers host and serve models, and some resellers wrap other APIs to offer lower prices, which makes it hard for customers to know which model actually handles a request. Model routing, the practice of sending each request to a cheaper or more suitable model, is a legitimate cost-saving technique, but secretly substituting a weaker model while charging for a stronger one is fraud.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://www.codecademy.com/article/what-is-openrouter">What is OpenRouter? A Guide with Practical Examples - Codecademy</a></li>
<li><a href="https://rejoicehub.com/blogs/what-is-a-model-router">What Is a Model Router ? AI Routing Explained</a></li>

</ul>
</details>

**Discussion**: Commenters noted that 'NahCrof' is '4chan in reverse' and pointed out the owner's Discord name 'Devious Flimflam', where 'flimflam' means deception or fraud, suggesting the operation was a deliberate scam from the start. The community also stressed that anyone who bought credits, even if already used, should seek a refund, and treated the episode as a cautionary tale about chasing the cheapest tokens.

**Tags**: `#AI inference`, `#fraud`, `#OpenRouter`, `#LLM pricing`, `#community discussion`

---

<a id="item-12"></a>
## [Apple Ships Foundation Models Natively in macOS 27](https://www.reddit.com/r/LocalLLaMA/comments/1wh5fpa/apple_foundation_models_local_ai_natively_on/) ⭐️ 8.0/10

Apple has made its Apple Foundation Models (AFM) available natively on macOS 27, allowing users to launch a local AI chat directly from the terminal with the command 'fm chat'. The release was shared on r/LocalLLaMA, where users began testing the models and debating their quality and the significance of Apple's move into on-device AI. This is a significant milestone for local AI because Apple is shipping optimized on-device models to every Mac user by default, dramatically lowering the barrier to running LLMs locally without third-party tools. It also signals that major platform vendors are embracing on-device inference, which could accelerate adoption and pressure the open-weight ecosystem to compete on quality and openness. The models are invoked through a simple terminal command, 'fm chat', which can also take a single prompt such as 'fm chat "summarize this text"'; a 'command not found' error typically means the binary is not in PATH or the system predates macOS 27. Apple's AFM family includes a 20-billion-parameter multimodal model (AFM 3 Core Advanced) and cloud variants, with some models reportedly built with Google Gemini collaboration and running on Nvidia GPUs under Apple's Private Cloud Compute.

reddit · r/LocalLLaMA · /u/Cherlokoms · Sep 15, 16:37

**Background**: Apple Foundation Models (AFM) are the generative AI models Apple introduced to power Apple Intelligence features such as the revamped Siri, designed to run on-device on Apple Silicon for privacy and low latency. macOS 27 is the version of Apple's desktop operating system that ships this native integration, letting developers and users access the models directly from the command line rather than only through apps. The move fits a broader trend of running LLMs locally on consumer hardware, where tools like Locally AI and Mirai Labs already offer on-device inference for iPhone, iPad, and Mac.

<details><summary>References</summary>
<ul>
<li><a href="https://gigazine.net/gsc_news/en/20260610-apple-foundation-models/">What's so amazing about the new AI, ' Apple Foundation Models '?</a></li>
<li><a href="https://ai-manual.ru/article/apple-foundation-models-v-macos-27-kak-zapustit-lokalnyij-ai-iz-terminala-komandoj-fm-chat/">Apple Foundation Models в MacOS 27: как запустить... | AiManual</a></li>
<li><a href="https://www.apple.com/apple-intelligence/">Apple Intelligence and Siri - Apple</a></li>

</ul>
</details>

**Discussion**: The Reddit thread shows a mix of enthusiasm and skepticism: the original poster, who prefers open-weight models, still calls Apple's move 'a huge step in the direction of local AI' and asks whether others have tested or built with the models. Commenters debate model quality and the trade-offs between Apple's closed ecosystem and open alternatives, reflecting broader community tension over convenience versus openness.

**Tags**: `#Apple`, `#Local AI`, `#macOS`, `#Foundation Models`, `#On-device AI`

---

<a id="item-13"></a>
## [Voodoo Dynamic Quant Open-Sourced Under MIT License](https://www.reddit.com/r/LocalLLaMA/comments/1wgszma/voodoo_dynamic_quant_now_mit_licensed/) ⭐️ 8.0/10

The author of Voodoo Dynamic Quant has released their gradient-descent-based per-tensor quantization layout optimization method under the MIT license, along with a toolset (https://github.com/curvedinf/voodoo-dyn-quant) for creating custom dynamic quants. The method was previously kept private but is now available to the community to encourage further research and scaling. This open-sourcing provides the local LLM community with a novel state-of-the-art dynamic quantization technique that can be adapted and improved, potentially leading to better model compression and performance at aggressive quantization levels. It also challenges proprietary methods like Unsloth Dynamic 3.0 by offering a transparent, reproducible alternative. Voodoo Quant uses gradient descent to optimize per-tensor quant layouts by training scalar gates for each quant level per tensor, with a KL divergence loss against a BF16 reference and a filesize target. It is currently set up for Qwen models but can be adapted to other architectures; it excels at aggressive quant levels but is research-grade and not yet studied at larger model sizes.

reddit · r/LocalLLaMA · /u/1ncehost · Sep 15, 06:59

**Background**: Quantization compresses large language models by reducing the precision of weights, and the GGUF format supports per-tensor quantization where each tensor can have a different quant level. Dynamic quants select quant levels per tensor for each checkpoint size, unlike static quants that use fixed selections. Voodoo Quant is the first method to use gradient descent to choose these levels, as opposed to static analysis techniques.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GGUF">GGUF - Wikipedia</a></li>
<li><a href="https://huggingface.co/docs/hub/en/gguf">GGUF · Hugging Face</a></li>
<li><a href="https://docs.pytorch.org/docs/2.13/generated/torch.quantize_per_tensor.html">quantize _ per _ tensor — PyTorch 2.13 documentation</a></li>

</ul>
</details>

**Tags**: `#quantization`, `#LLM`, `#GGUF`, `#open-source`, `#model-compression`

---

<a id="item-14"></a>
## [LynnReal-Omni: 32B Unified Video Diffusion Model with Open Weights and ComfyUI Nodes](https://www.reddit.com/r/StableDiffusion/comments/1wh8hov/lynnrealomni_built_on_minmax_h3_weights_comfy/) ⭐️ 8.0/10

LynnReal-Omni is a unified 32B multimodal diffusion transformer built on the MiniMax H3 architecture that consolidates text-to-video, image-to-video, pose-guided generation, style transfer, video editing, degraded-video restoration, and streaming long-video generation into a single framework with four-step fast generation. A 27B Flash variant enables three-step generation, and both the open weights and ComfyUI nodes are now available on Hugging Face and GitHub. This release matters because it consolidates many previously separate video generation and editing tasks into one model, reducing the need to chain multiple specialized pipelines. With open weights and ComfyUI nodes, it gives the Stable Diffusion community a practical, controllable tool for agentic visual creation and real-time streaming video generation. On a single H100, warm generation and decoding of a 22-frame 540p video takes 843 ms with the Standard model and 377 ms with Flash, which uses model and decoding acceleration plus a lightweight VAE decoder. The team also introduces MSAVP, a 100-prompt, 20-metric evaluation design that separates instruction following, generating plausibility, visual quality, temporal behavior, and audio coordination.

reddit · r/StableDiffusion · /u/AgeNo5351 · Sep 15, 18:25

**Background**: MiniMax H3 is a general-purpose omni-modal generative system built on a dense single-stream Transformer that unifies understanding across text, images, and video. A multimodal diffusion transformer applies diffusion-based generation to multiple input modalities, and ComfyUI is a node-based interface where users connect modular nodes to build image and video generation workflows. LynnReal-Omni follows the MiniMax H3 architecture but is an independent community release rather than an official MiniMax product.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between Tasks ...</a></li>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-H3">MiniMaxAI/MiniMax-H3 - Hugging Face</a></li>
<li><a href="https://docs.comfy.org/basic-concepts/nodes">Nodes - ComfyUI</a></li>

</ul>
</details>

**Tags**: `#diffusion-models`, `#video-generation`, `#multimodal`, `#open-weights`, `#comfyui`

---

<a id="item-15"></a>
## [SHADOW-50M: 44M ternary LLM ships in 19.8 MB, runs 1,900 tok/s on CPU](https://www.reddit.com/r/MachineLearning/comments/1wgzpli/i_trained_a_44m_parameter_quantized_llm_from/) ⭐️ 8.0/10

A developer trained SHADOW-50M, a 44M-parameter ternary-weight LLM, from scratch on 45B tokens, producing a complete 19.8 MB model that runs at roughly 1,900 tokens per second on a laptop CPU with about 41 MB RAM. It uses a 73,880-token vocabulary represented by fixed 512-bit fingerprints instead of a trained embedding, a 159 KB compiled kernel, and a hybrid calculation circuit that handles arithmetic, dates, units and sorting directly in the token stream. This is a striking proof of concept for the local and edge LLM space, showing that a useful, fully offline model can fit in under 20 MB and run fast on commodity CPUs without a GPU. It also demonstrates an unusual architecture combining ternary weights, fingerprint-based vocabulary and built-in calculation circuits, which could inspire new approaches to tiny, efficient models. The model is a proof of concept rather than a product, and it loses to a 51.8M-parameter bf16 Llama-style baseline called Supra-50M-Reasoning on standard benchmarks such as ARC-Easy (0.307 vs 0.435), PIQA (0.570 vs 0.600) and WikiText-2 perplexity (186 vs 165). Its archive stores attention states at 1 bit (288 bytes/token) with a 22-byte/token index, and a persistent reinforcement trail improved measured top-1 retrieval from 0.571 to 0.743 without retraining.

reddit · r/MachineLearning · /u/Final-Data-1410 · Sep 15, 12:59

**Background**: Ternary weight quantization restricts neural network weights to just -1, 0 or +1, which drastically shrinks model size and replaces expensive floating-point multiplications with additions or memory lookups; Microsoft's BitNet b1.58 popularized this idea. Most LLMs instead learn a large embedding table to map tokens to vectors, but SHADOW replaces that with fixed 512-bit fingerprints, avoiding a trained embedding entirely. The hybrid calculation circuit is also unusual: rather than calling an external calculator tool, the model emits a marker like [calc]347*86[eq] and a fixed circuit fills in the answer within the same token stream.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/ternary-weight-quantization-scheme">Ternary Weight Quantization</a></li>
<li><a href="https://www.youtube.com/watch?v=hnOpXlVZy6g">BitNet b1.58 How 1.58-Bit Ternary Weights Run LLMs on... - YouTube</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#quantization`, `#edge-computing`, `#efficient-inference`, `#from-scratch-training`

---