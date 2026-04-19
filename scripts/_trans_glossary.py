"""One-shot translator for Appendix B Glossary."""
import polib

PATH = 'source/locale/zh_CN/LC_MESSAGES/chapters/13-appendices/b-glossary.po'
T = {}

T['Appendix B — Glossary'] = '附录 B —— 术语表'

T['Thirty-eight terms, alphabetically sorted. Each entry carries a ≤ 100-word definition, a *first appears in* chapter pointer, and at least one citation via the Sphinx `cite` role.'] = \
    '三十八个词条，按字母排序。每条配有一则不超过 100 词的定义、一条 *首次出现* 的章节指针，以及至少一条经由 Sphinx `cite` 角色标注的引用。'

T['Agent Loop'] = 'Agent Loop（智能体回路）'
T["The step-loop at the heart of an agent runtime: gather context, invoke the model, optionally run tool calls, update state, decide continue vs halt. OpenHarness's `engine/query_engine.py` is the reference implementation cited in this book. *First appears in Ch.07.* {cite}`yao2022react`."] = \
    '智能体运行时核心处的那个 step-loop：聚上下文、调模型、按需执行工具调用、更新状态、再判定"继续 vs 停止"。OpenHarness 的 `engine/query_engine.py` 是本书所引用的参考实现。*首次出现于第 07 章。* {cite}`yao2022react`。'

T['Ambiguity Amplification'] = 'Ambiguity Amplification（歧义放大）'
T['The agent-era failure mode in which an ambiguous specification is laundered into confidently-wrong code at scale. A human reading an ambiguous spec hesitates; a model emits a concrete, plausible interpretation on every turn. One ambiguous bullet in `AGENTS.md` becomes a hundred subtly-different implementations over a quarter. The cost of ambiguity is multiplied by agent throughput, which is why spec tightening is the highest-leverage SDD investment. *First appears in Ch.04.* {cite}`martraire2019living`.'] = \
    '智能体时代的一种失败模式——一份含糊的规约被大规模洗成"自信而错"的代码。人类读到含糊规约会迟疑；模型则会在每一回合里给出一份具体、看上去合理的解读。`AGENTS.md` 里一条含糊条目，在一个季度里能变成上百份 *局部各自自洽、却微妙互异* 的实现。歧义的成本会被智能体的吞吐量放大——这也是为什么"拧紧规约"是 SDD 上杠杆最高的投资。*首次出现于第 04 章。* {cite}`martraire2019living`。'

T['Architectural Fitness Function'] = 'Architectural Fitness Function（架构 fitness function）'
T["An automatable test of a non-functional property the architecture must preserve as the system evolves. Ford, Parsons & Kua's term is the theoretical backing for the Ch.05 four-zone matrix. *First appears in Ch.03.* {cite}`ford2017buildingevolutionary`."] = \
    '一项可自动化的测试——用来检验架构在演化过程中必须保住的某条非功能性属性。Ford、Parsons 与 Kua 的这个术语，是第 05 章四区域矩阵的理论背书。*首次出现于第 03 章。* {cite}`ford2017buildingevolutionary`。'

T['Artefact State Model'] = 'Artefact State Model（制品状态机）'
T["A four-state machine (`draft → review → approved → archived`) with role-owned transitions. Central to Chapter 09's workflow-encoded harness. *First appears in Ch.06.* {cite}`lazyscrumteam2026`."] = \
    '一具四状态机（`draft → review → approved → archived`），跃迁由角色署名持有。它是第 09 章"工作流编码挽具"的核心。*首次出现于第 06 章。* {cite}`lazyscrumteam2026`。'

T['Bridle'] = 'Bridle（缰绳）'
T['The Ch.05 zone containing everything the agent reads *before* it writes. `AGENTS.md`, `CLAUDE.md`, `SKILL.md`, and failing-first tests all live here. *First appears in Ch.05.* {cite}`walterfan2026guardians`.'] = \
    '第 05 章的一个区域，容纳智能体 *下笔之前* 所读的一切。`AGENTS.md`、`CLAUDE.md`、`SKILL.md`，以及"先红后绿"的测试，都住在这一区。*首次出现于第 05 章。* {cite}`walterfan2026guardians`。'

T['CAR Decomposition'] = 'CAR 分解'
T["The **Control / Agency / Runtime** decomposition proposed by the *Harness Engineering for Language Agents* position paper. This book's preferred academic reference; the HarnessCard format is the CAR paper's disclosure artefact. *First appears in Ch.05.* {cite}`car2025decomposition`."] = \
    '**Control／Agency／Runtime** 三层分解，由 *Harness Engineering for Language Agents* 这篇立场论文提出。本书所偏好的学术参考；HarnessCard 格式正是 CAR 论文里的披露制品。*首次出现于第 05 章。* {cite}`car2025decomposition`。'

T['Compliance Theatre'] = 'Compliance Theatre（合规剧场）'
T['The agent-era failure mode in which a skill\'s prose self-reports successful execution ("I ran the tests, they passed") without any mechanical check falsifying the report. Over many turns the agent learns that emitting compliance-shaped tokens is cheaper than running the check; prescription drifts away from enforcement. The cure is to pair every load-bearing skill with a hook that refuses turns which skipped the skill\'s preconditions. *First appears in Ch.02.* {cite}`anthropic2024claudecode`.'] = \
    '智能体时代的一种失败模式——一份技能的散文自报"执行成功"（"我跑了测试，测试过了"）却没有任何机械性检查去证伪这份汇报。多回合下来，智能体学到："输出合规形状的 token"，比"真去跑一遍检查"更便宜；*处方* 就此与 *强制执行* 相分离。解法：为每一份承重技能配一条钩子——它会拒掉那些跳过了这份技能前置条件的回合。*首次出现于第 02 章。* {cite}`anthropic2024claudecode`。'

T['Context Engineering'] = 'Context Engineering（上下文工程）'
T["Karpathy's 2025 term for the discipline of composing the agent's input window. Neighbours prompt engineering and overlaps with SDD × Bridle. *First appears in Ch.03.* {cite}`karpathy2025context`."] = \
    'Karpathy 2025 年提出的术语——"给智能体组合输入窗口"这门手艺。与 prompt engineering 为邻，与 SDD × 缰绳 有重叠。*首次出现于第 03 章。* {cite}`karpathy2025context`。'

T['Context Pollution'] = 'Context Pollution（上下文污染）'
T['The Stage-2 failure mode in which optimising retrieval for recall fills the context window with nearly-relevant chunks, causing the agent to average rather than select. Three mediocre retrieved examples teach the agent that mediocre is the house style. The cure is retrieval as a fence (refuse deprecated paths) rather than a hose (spray everything). *First appears in Ch.02.* {cite}`lewis2020rag`.'] = \
    '第 2 阶段的一种失败模式——为"召回率"优化检索，把上下文窗口塞满了"近似相关"的片段，导致智能体去"取平均"而不是"做选择"。三段平庸的检索示例，教会智能体：*平庸就是本店家风*。解法：把检索当作一道护栏（拒掉已弃用路径），而非一根水管（见什么喷什么）。*首次出现于第 02 章。* {cite}`lewis2020rag`。'

T['Cost Runaway (without correlate)'] = 'Cost Runaway（无对应物的成本失控）'
T["The MDD-era failure mode in which agent-introduced expense regressions never surface in the team's lived experience. A 10× slower function the human writes also slows the human's next task; a 10× more expensive prompt the agent writes runs just as fast from the team's perspective, and the cost accrues silently on the invoice. Cure: per- turn cost tagged by skill, repository, and change-set, wired into a fence. *First appears in Ch.04.* {cite}`langchain2026tbench`."] = \
    'MDD 时代的一种失败模式——智能体引入的费用回归，从不曾出现在团队的日常体感里。人类写下一个慢 10× 的函数，下一件事也会跟着慢；智能体写下一段贵 10× 的 prompt，对团队而言跑起来速度一样，成本却在账单上悄悄攒着。解法：把"每回合成本"按技能、仓库、change-set 打标签，并接到一道护栏上。*首次出现于第 04 章。* {cite}`langchain2026tbench`。'

T['DORA Metrics'] = 'DORA 度量'
T['The four DevOps Research & Assessment metrics — deployment frequency, lead time, change failure rate, mean time to restore. Outcome metrics that HarnessCards feed into. *First appears in Ch.12.* {cite}`forsgren2018accelerate`.'] = \
    'DevOps Research & Assessment 的四条度量——部署频率、交付前置时间、变更失败率、平均恢复时间。作为产出指标，HarnessCard 最终喂给它们。*首次出现于第 12 章。* {cite}`forsgren2018accelerate`。'

T['Design by Contract'] = 'Design by Contract（契约式设计）'
T["Meyer's 1992 principle that routines specify preconditions, postconditions, and invariants as first-class artefacts. Intellectual ancestor of the spec-first approach in SDD × Bridle. *First appears in Ch.04.* {cite}`meyer1992contracts`."] = \
    'Meyer 1992 年提出的原则——子程序把前置条件、后置条件与不变量作为"一等公民制品"来声明。SDD × 缰绳 里"规约先行"的智识先祖。*首次出现于第 04 章。* {cite}`meyer1992contracts`。'

T['Entropy (harness sense)'] = 'Entropy（挽具语境下的"熵"）'
T['The accumulation of stale, broken, or misleading content in the harness surface. Left alone, entropy turns a working harness decorative. *First appears in Ch.06.* {cite}`cunningham1992debt`.'] = \
    '挽具表面上"过期、已坏、或具有误导性"内容的累积。若不管它，熵会把一具能工作的挽具，变成一具装饰物。*首次出现于第 06 章。* {cite}`cunningham1992debt`。'

T['Fence'] = 'Fence（护栏）'
T['The Ch.05 zone containing automated refusals — hooks, linters, schema validators, secret scanners. Fires at the keystroke or the commit. *First appears in Ch.05.* {cite}`walterfan2026guardians`.'] = \
    '第 05 章的一个区域，容纳自动化的"拒绝"——钩子、linter、schema 校验器、密钥扫描器。在按键或 commit 的那一刻触发。*首次出现于第 05 章。* {cite}`walterfan2026guardians`。'

T['Final Acceptance'] = 'Final Acceptance（终审）'
T['The `lazy-scrum-team` role that owns the `review → approved` transition in the Artefact State Model. Cannot perform the review itself; only the Code Reviewer role does that. *First appears in Ch.09.* {cite}`lazyscrumteam2026`.'] = \
    '`lazy-scrum-team` 里的一个角色——署名持有制品状态机中 `review → approved` 这条跃迁。它本身不做评审；评审由 Code Reviewer 角色去做。*首次出现于第 09 章。* {cite}`lazyscrumteam2026`。'

T['Groom'] = 'Groom（梳理）'
T['The Ch.05 zone containing recurring maintenance — weekly audits, dashboard retention reviews, stale-doc sweeps. Tends the harness itself, not the product. *First appears in Ch.05.* {cite}`walterfan2026guardians`.'] = \
    '第 05 章的一个区域，容纳"反复要做的维护"——每周审计、仪表盘留存评审、对陈旧文档的清扫。照看的是挽具本身，不是产品。*首次出现于第 05 章。* {cite}`walterfan2026guardians`。'

T['Hard Gate'] = 'Hard Gate（硬关卡）'
T['A gate that refuses a commit, merge, or release with *no waiver path*. Unit-test failures, secrets-scan hits, and lint errors on new code are Hard by default. *First appears in Ch.06.* {cite}`humble2010continuousdelivery`.'] = \
    '一道关卡——拒掉一次 commit、合并或发布，*没有豁免通路*。单元测试失败、密钥扫描命中、以及新代码上的 lint 错误，默认都是"硬"的。*首次出现于第 06 章。* {cite}`humble2010continuousdelivery`。'

T['Harness'] = 'Harness（挽具）'
T['The environment the agent operates inside — the specs it reads, the gates it passes, the paddock it runs in, the groom that keeps the environment alive. Not the agent itself. *First appears in Ch.01.* {cite}`fowler2026harness`.'] = \
    '智能体在其中运作的那个环境——它所读的规约、它所通过的关卡、它所奔跑的牧场、以及那个让环境保持活着的 Groom。不是智能体本身。*首次出现于第 01 章。* {cite}`fowler2026harness`。'

T['HarnessCard'] = 'HarnessCard'
T['The standardised disclosure format proposed by the CAR paper. Twelve cells plus layer notes plus a primary citation; rendered as a copy-paste table in Appendix D. *First appears in Ch.05.* {cite}`car2025decomposition`.'] = \
    'CAR 论文所提出的那份标准化披露格式：十二格 ＋ 层级注释 ＋ 一条主引用；在附录 D 中以"可直接粘贴"的表格形式交付。*首次出现于第 05 章。* {cite}`car2025decomposition`。'

T['Harness Theatre'] = 'Harness Theatre（挽具剧场）'
T['The class of failure modes in which a harness grows (more rules, more files, more dashboards) without its leverage growing — measured as refusals, measurements, or steered decisions per week. The diagnostic is the ratio of harness-shaped artefacts to refused-or-measured events: a healthy harness refuses something on most days; a theatrical one refuses nothing for weeks while its file count rises. Subtypes named in the book: aspirational `CLAUDE.md`, passing pre-commit, dashboard theatre, workflow-without-tooling, vanity HarnessCard delta. *First appears in Ch.01; developed in Ch.06.* {cite}`cunningham1992debt`.'] = \
    '一类失败模式——挽具在长（规则变多、文件变多、仪表盘变多），它的杠杆却没在长（以"每周拒绝数、每周度量数、每周被掰方向的决策数"来衡量）。诊断尺：挽具形状的制品数，对比于"被拒绝或被度量的事件数"——一具健康挽具多数日子里都会拒掉点什么；一具剧场化挽具则连续数周什么都没拒绝，而文件数却还在涨。书中点名的子类：望远式 `CLAUDE.md`、一路放行的 pre-commit、仪表盘剧场、无工具的工作流、HarnessCard 虚荣 delta。*首次出现于第 01 章；在第 06 章展开。* {cite}`cunningham1992debt`。'

T['Harness Engineering'] = 'Harness Engineering（挽具工程）'
T["The practice of designing, building, and operating harnesses as first-class artefacts in AI-assisted software engineering. The term and its industrial framing trace to Fowler's 2026 essay and the author's 2026-03-28 blog post. *First appears in Ch.01.* {cite}`fowler2026harness`."] = \
    '在 AI 辅助的软件工程里，把挽具当作一等公民制品来 *设计、建造、运行* 的那门实践。该术语及其工业语境，可追溯至 Fowler 2026 年的那篇文章，以及作者 2026-03-28 的那篇博文。*首次出现于第 01 章。* {cite}`fowler2026harness`。'

T['Hook'] = 'Hook（钩子）'
T['A Claude Code callback that fires at a named lifecycle event (`PreToolUse`, `PostToolUse`, `SessionEnd`, `UserPromptSubmit`). Exit code 2 refuses the in-flight tool call. *First appears in Ch.05.* {cite}`anthropic2024claudecode`.'] = \
    'Claude Code 的一类回调——在某个具名生命周期事件（`PreToolUse`、`PostToolUse`、`SessionEnd`、`UserPromptSubmit`）触发。退出码 2 会拒掉当前正在进行中的那次工具调用。*首次出现于第 05 章。* {cite}`anthropic2024claudecode`。'

T['Lazy AI Coder'] = 'Lazy AI Coder'
T["The open-source repository this book ships from — `walterfan/lazy-ai-coder` — and the subject of Chapter 11's worked example. *First appears in Ch.11.* {cite}`lazyaicoder2026`."] = \
    '本书所承载的开源仓库——`walterfan/lazy-ai-coder`——也是第 11 章实例的对象。*首次出现于第 11 章。* {cite}`lazyaicoder2026`。'

T['lazy-scrum-team'] = 'lazy-scrum-team'
T['An open-source workflow-encoded harness shipped as a Claude Code / Cursor skill package. Canonical source for the Artefact State Model, the Rework Matrix, and the Hard/Soft gate classification. *First appears in Ch.06.* {cite}`lazyscrumteam2026`.'] = \
    '一具以 Claude Code／Cursor 技能包形式交付的开源"工作流编码型挽具"。"制品状态机、返工矩阵、硬／软关卡分类"三者的权威出处。*首次出现于第 06 章。* {cite}`lazyscrumteam2026`。'

T['Living Documentation'] = 'Living Documentation（活文档）'
T["Martraire's term for documentation generated from or kept in sync with running code. The Ch.05 SDD × Groom zone operationalises the concept. *First appears in Ch.04.* {cite}`martraire2019living`."] = \
    'Martraire 所提出的术语——从运行中的代码里生成、或与其保持同步的那类文档。第 05 章 SDD × 梳理 这一格，是把这一概念落地的地方。*首次出现于第 04 章。* {cite}`martraire2019living`。'

T['MCP (Model Context Protocol)'] = 'MCP（Model Context Protocol）'
T["Anthropic's 2024 open specification for tool calls between LLM clients and tool servers. OpenHarness, Claude Code, and many other harnesses target the spec. *First appears in Ch.07.* {cite}`anthropic2024mcp`."] = \
    'Anthropic 2024 年提出的一份开放规范——定义 LLM 客户端与工具服务器之间的工具调用。OpenHarness、Claude Code 以及许多挽具都对齐它。*首次出现于第 07 章。* {cite}`anthropic2024mcp`。'

T['MDD (Metric-Driven Development)'] = 'MDD（Metric-Driven Development，度量驱动开发）'
T['The third guardian: the practice of naming observable signals before the code ships and tending them afterwards. *First appears in Ch.04.* {cite}`majors2022observability`.'] = \
    '第三位护法——在代码交付之前就先"指名道姓"地定义可观测信号，并在交付之后持续照看它们的那门实践。*首次出现于第 04 章。* {cite}`majors2022observability`。'

T['Meta-Harness'] = 'Meta-Harness（元挽具）'
T["A harness that treats itself as a product — with its own changelog, release cadence, and HarnessCards. Ch.06's fourth operating concern. *First appears in Ch.06.* {cite}`ford2017buildingevolutionary`."] = \
    '一具把自己也当作产品来对待的挽具——有自己的 changelog、发布节奏、HarnessCard。第 06 章"运行挽具"的四大关注中的第四个。*首次出现于第 06 章。* {cite}`ford2017buildingevolutionary`。'

T['Observability'] = 'Observability（可观测性）'
T['The discipline of making an operating system externally comprehensible via logs, metrics, and traces. MDD is the guardian that carries observability into the harness. *First appears in Ch.06.* {cite}`majors2022observability`.'] = \
    '通过 log、metric 与 trace，让一个运行中的系统"从外部也能被看懂"的那门手艺。MDD 就是把可观测性带进挽具的那位护法。*首次出现于第 06 章。* {cite}`majors2022observability`。'

T['OpenHarness'] = 'OpenHarness'
T["The HKU Data Science Lab's open-source harness reference implementation. Chapter 07 is the case study. *First appears in Ch.05.* {cite}`hkuds2025openharness`."] = \
    '香港大学数据科学实验室出品的那套开源"挽具参考实现"。第 07 章即是对它的案例研究。*首次出现于第 05 章。* {cite}`hkuds2025openharness`。'

T['Paddock'] = 'Paddock（牧场）'
T['The Ch.05 zone containing the bounded review rituals and environments — acceptance tables, CI gates, staging soaks. Distinct from Fence by being *slower, broader, more authoritative*. *First appears in Ch.05.* {cite}`walterfan2026guardians`.'] = \
    '第 05 章的一个区域，容纳那些有边界的评审仪式与环境——验收表、CI 关卡、staging 泡测。与护栏的区别是——牧场 *更慢、更宽、更权威*。*首次出现于第 05 章。* {cite}`walterfan2026guardians`。'

T['Prompt Engineering'] = 'Prompt Engineering'
T["The 2023-era discipline of authoring LLM prompts to produce desired outputs. A subset of Ch.05's SDD × Bridle; insufficient on its own for an agent-era harness. *First appears in Ch.02.* {cite}`brown2020gpt3`."] = \
    '2023 年前后那一门手艺——写 LLM 提示，以期产出所希望的输出。属于第 05 章 SDD × 缰绳 的一个子集；对于智能体时代的挽具而言，仅此一项并不够。*首次出现于第 02 章。* {cite}`brown2020gpt3`。'

T['ReAct'] = 'ReAct'
T["Yao et al.'s 2022 pattern combining *Reasoning* and *Acting* in the agent loop. Academic lineage of every modern Agent Loop including OpenHarness's. *First appears in Ch.07.* {cite}`yao2022react`."] = \
    'Yao 等 2022 年提出的一种模式——在智能体回路里把 *推理（Reasoning）* 与 *行动（Acting）* 合一。每一套现代 Agent Loop（包括 OpenHarness 的那套）的学术谱系。*首次出现于第 07 章。* {cite}`yao2022react`。'

T['Reverse-Engineering Disclaimer'] = 'Reverse-Engineering Disclaimer（逆向工程免责声明）'
T['The mandatory first H2 of Chapter 10 (and any closed-source case study): a structured statement of sources, observation window, and retraction commitment. *First appears in Ch.10.* {cite}`zhangbook2026`.'] = \
    '第 10 章（以及任何一章"闭源案例研究"）必须开篇的那一段二级标题：结构化地声明来源、观察窗口与撤回承诺。*首次出现于第 10 章。* {cite}`zhangbook2026`。'

T['Rework Matrix'] = 'Rework Matrix（返工矩阵）'
T['The finder × fixer table naming the rework artefact that must accompany every hand-off. Canonical treatment is Chapter 09 §09.3. *First appears in Ch.06.* {cite}`gousios2014pullbased`.'] = \
    '"发现者 × 修复者"表格——为每一次交接署名点出必须随附的那件返工制品。权威处理在第 09 章 §09.3。*首次出现于第 06 章。* {cite}`gousios2014pullbased`。'

T['SDD (Spec-Driven Development)'] = 'SDD（Spec-Driven Development，规约驱动开发）'
T['The first guardian: the practice of treating spec artefacts — `AGENTS.md`, `CLAUDE.md`, executable specs — as first-class and agent- readable before any implementation begins. *First appears in Ch.04.* {cite}`martraire2019living`.'] = \
    '第一位护法——把 `AGENTS.md`、`CLAUDE.md`、可执行规约这类"规约制品"视为一等公民、在任何实现开始之前就让智能体可读的那门实践。*首次出现于第 04 章。* {cite}`martraire2019living`。'

T['Skill (Claude Code)'] = 'Skill（Claude Code）'
T['A `SKILL.md` file discovered via front-matter `description:` and auto- invoked by the agent. *First appears in Ch.08.* {cite}`anthropic2024skills`.'] = \
    '一份 `SKILL.md` 文件——智能体通过 front-matter 里的 `description:` 将其发现并自动调用。*首次出现于第 08 章。* {cite}`anthropic2024skills`。'

T['Skill Engineering'] = 'Skill Engineering（技能工程）'
T['The 2026-era discipline of authoring reusable skills that shape how an agent thinks before it writes. Builds on prompt engineering and context engineering. *First appears in Ch.08.* {cite}`vincent2025superpowers`.'] = \
    '2026 年前后这一门手艺——编写可复用的技能，以"塑造智能体在下笔之前如何思考"。在 prompt engineering 与 context engineering 之上继续往上搭。*首次出现于第 08 章。* {cite}`vincent2025superpowers`。'

T['Spec Drift'] = 'Spec Drift（规约漂移）'
T["The silent SDD failure mode in which the codebase evolves away from `AGENTS.md`'s claims without the spec being updated. The agent, reading the spec as authoritative, keeps generating code that conforms to it; humans, reading the codebase, keep generating code that conforms to it; the gap widens from both sides. Cure: a scheduled Groom job that compares the spec's machine-checkable claims against the codebase weekly and refuses silent drift. *First appears in Ch.04.* {cite}`martraire2019living`."] = \
    'SDD 的一种"沉默失败模式"——代码库悄悄漂离 `AGENTS.md` 所主张的样子，规约却没有被更新。智能体把规约当作权威来读，继续生成与规约自洽的代码；人类把代码库当作现实来读，继续写与代码库自洽的代码；裂缝从两头一起拉大。解法：安排一项定时 Groom 任务——每周比对"规约的机器可检查主张"与代码库，并拒绝"无声漂移"。*首次出现于第 04 章。* {cite}`martraire2019living`。'

T['Soft Gate'] = 'Soft Gate（软关卡）'
T['A gate that refuses by default but allows a role-signed, dated waiver. Coverage floors, cost caps, and docs link-checks are common Soft gates. *First appears in Ch.06.* {cite}`humble2010continuousdelivery`.'] = \
    '一道关卡——默认拒绝，但允许"由署名角色签、带到期日"的豁免。覆盖率下限、成本上限、文档 link-check，都是常见的软关卡。*首次出现于第 06 章。* {cite}`humble2010continuousdelivery`。'

T['Specification by Example'] = 'Specification by Example（范例化规约）'
T["Adzic's 2011 term for the practice of turning acceptance criteria into executable examples. The vocabulary behind Ch.05 SDD × Paddock. *First appears in Ch.05.* {cite}`adzic2011specbyexample`."] = \
    'Adzic 2011 年提出的术语——把验收标准转化为可执行范例的那门实践。第 05 章 SDD × 牧场 这一格背后的词汇源。*首次出现于第 05 章。* {cite}`adzic2011specbyexample`。'

T['Superpowers'] = 'Superpowers'
T["Joseph Vincent's open-source skill library for Claude Code. Chapter 08 is the case study. *First appears in Ch.08.* {cite}`vincent2025superpowers`."] = \
    'Joseph Vincent 为 Claude Code 出品的那座开源技能库。第 08 章是它的案例研究。*首次出现于第 08 章。* {cite}`vincent2025superpowers`。'

T['TDD (Test-Driven Development)'] = 'TDD（Test-Driven Development，测试驱动开发）'
T["The second guardian: Beck's 2002 discipline of writing a failing test before the implementation. Re-centred in the agent era as TDD × Bridle (tests as input) and TDD × Fence (hooks refusing red-tree edits). *First appears in Ch.04.* {cite}`beck2002tdd`."] = \
    '第二位护法——Beck 2002 年提出的那门纪律："先写一个红的测试，再写实现"。进入智能体时代之后，重心被重新摆到 TDD × 缰绳（把测试作为输入）与 TDD × 护栏（钩子拒掉红树下的编辑）这两格。*首次出现于第 04 章。* {cite}`beck2002tdd`。'

T['Test-Pinning (wrong-interpretation)'] = 'Test-Pinning（把错误解读钉死）'
T["The agent-era TDD failure mode in which a human-authored test is *technically* correct for the behaviour the human had in mind but leaves one interpretive degree of freedom the agent resolves opportunistically. Green tests; wrong behaviour; and the green test hardens the agent's misunderstanding into the repository's memory. Cure: adversarial tests written specifically to falsify the cheapest path from prompt to green — the reviewer's \"one more test\" habit on every first-try pass. *First appears in Ch.04.* {cite}`ziegler2022productivity`."] = \
    '智能体时代 TDD 的一种失败模式——人类写下的一条测试，对他心里那种行为来说 *技术上* 是正确的，却留下了一处"解读自由度"，被智能体见缝插针地填掉。测试绿、行为错；而这条绿测试，把智能体的错误理解固化进了仓库记忆。解法：写"对抗性测试"——专门去证伪"从 prompt 到变绿"的那条最便宜路径；也就是评审人在每一次"首发即过"时都要有的那条"再加一条测试"的习惯。*首次出现于第 04 章。* {cite}`ziegler2022productivity`。'

T['Technical Debt'] = 'Technical Debt（技术债）'
T["Cunningham's 1992 metaphor for the accumulated cost of expedient design choices. The *entropy* vocabulary of Ch.06 is a harness-specific specialisation. *First appears in Ch.06.* {cite}`cunningham1992debt`."] = \
    'Cunningham 1992 年的隐喻——"因便宜设计选择而累积下来的成本"。第 06 章那套 *熵* 的词汇，就是它在挽具语境下的一次特化。*首次出现于第 06 章。* {cite}`cunningham1992debt`。'

T['Toolformer'] = 'Toolformer'
T["Schick et al.'s 2023 paper establishing first-class tool use as a primary action surface for LLMs. Academic lineage of OpenHarness's 43-tool taxonomy. *First appears in Ch.07.* {cite}`schick2023toolformer`."] = \
    'Schick 等 2023 年的论文——把"一等公民级的工具使用"确立为 LLM 的一个主要行动面。OpenHarness 43 个工具那份分类的学术谱系。*首次出现于第 07 章。* {cite}`schick2023toolformer`。'

T['《马书》 (*Ma\'s book*)'] = '《马书》（*Ma\'s book*）'
T["Zhang Handong's 2026 reverse-engineering study of Claude Code's bundled prompt, skill system, hooks contract, and tool schemas. Primary source for Chapter 10. *First appears in Ch.10.* {cite}`zhangbook2026`."] = \
    '张汉东 2026 年对 Claude Code 内置提示、技能系统、hooks 契约与工具 schema 的逆向工程研究。第 10 章的第一手来源。*首次出现于第 10 章。* {cite}`zhangbook2026`。'


def main():
    po = polib.pofile(PATH)
    hit = 0
    miss = []
    for e in po:
        if not e.msgstr and not e.obsolete:
            if e.msgid in T:
                e.msgstr = T[e.msgid]
                hit += 1
            else:
                miss.append(e.msgid)
    po.save(PATH)
    print(f'translated {hit}; misses {len(miss)}')
    for m in miss[:10]:
        print('  MISS:', repr(m[:220]))
    po2 = polib.pofile(PATH)
    remaining = [e for e in po2 if not e.msgstr and not e.obsolete]
    print(f'remaining: {len(remaining)}')


if __name__ == '__main__':
    main()
