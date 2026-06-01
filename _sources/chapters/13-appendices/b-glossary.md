---
status: draft
chapter-type: appendix
---

# 附录 B —— 术语表

三十八个词条，按字母排序。每条配有一则不超过 100 词的定义、一条 *首次出现* 的章节指针，以及至少一条经由 Sphinx `cite` 角色标注的引用。

## Agent Loop（智能体回路）

智能体运行时核心处的那个 step-loop：聚上下文、调模型、按需执行工具调用、更新状态、再判定"继续 vs 停止"。OpenHarness 的 `engine/query_engine.py` 是本书所引用的参考实现。*首次集中讨论于插章；案例展开见第 07 章。* {cite}`yao2022react`。

## Ambiguity Amplification（歧义放大）

智能体时代的一种失败模式——一份含糊的规约被大规模洗成"自信而错"的代码。人类读到含糊规约会迟疑；模型则会在每一回合里给出一份具体、看上去合理的解读。`AGENTS.md` 里一条含糊条目，在一个季度里能变成上百份 *局部各自自洽、却微妙互异* 的实现。歧义的成本会被智能体的吞吐量放大——这也是为什么"拧紧规约"是 SDD 上杠杆最高的投资。*首次出现于第 04 章。* {cite}`martraire2019living`。

## Architectural Fitness Function（架构 fitness function）

一项可自动化的测试——用来检验架构在演化过程中必须保住的某条非功能性属性。Ford、Parsons 与 Kua 的这个术语，是第 05 章四区域矩阵的理论背书。*首次出现于第 03 章。* {cite}`ford2017buildingevolutionary`。

## Artefact State Model（制品状态机）

一具四状态机（`draft → review → approved → archived`），跃迁由角色署名持有。它是第 09 章"工作流编码马具"的核心。*首次出现于第 06 章。* {cite}`lazyscrumteam2026`。

## Bridle（缰绳）

第 05 章的一个区域，容纳智能体 *下笔之前* 所读的一切。`AGENTS.md` 是跨智能体的 canonical 入口；`CLAUDE.md`、`.cursor/rules/`、`SKILL.md`，以及"先红后绿"的测试，都住在这一区，但前两者最好只是客户端兼容层或更窄的局部规则。*首次出现于第 05 章。* {cite}`agenticai2025agentsmd,walterfan2026guardians`。

## CAR 分解

**Control／Agency／Runtime** 三层分解，由 *Harness Engineering for Language Agents* 这篇立场论文提出。本书所偏好的学术参考；HarnessCard 格式正是 CAR 论文里的披露制品。*首次出现于第 05 章。* {cite}`car2025decomposition`。

## Compliance Theatre（合规剧场）

智能体时代的一种失败模式——一份技能的散文自报"执行成功"（"我跑了测试，测试过了"）却没有任何机械性检查去证伪这份汇报。多回合下来，智能体学到："输出合规形状的 token"，比"真去跑一遍检查"更便宜；*处方* 就此与 *强制执行* 相分离。解法：为每一份承重技能配一条钩子——它会拒掉那些跳过了这份技能前置条件的回合。*首次出现于第 02 章。* {cite}`anthropic2024claudecode`。

## Context Engineering（上下文工程）

Karpathy 2025 年提出的术语——"给智能体组合输入窗口"这门手艺。与 prompt engineering 为邻，与 SDD × 缰绳 有重叠。*首次出现于第 02 章；结构性拆解见插章。* {cite}`karpathy2025context`。

## Context Pollution（上下文污染）

第 2 阶段的一种失败模式——为"召回率"优化检索，把上下文窗口塞满了"近似相关"的片段，导致智能体去"取平均"而不是"做选择"。三段平庸的检索示例，教会智能体：*平庸就是本店家风*。解法：把检索当作一道护栏（拒掉已弃用路径），而非一根水管（见什么喷什么）。*首次出现于第 02 章。* {cite}`lewis2020rag`。

## Cost Runaway（无对应物的成本失控）

MDD 时代的一种失败模式——智能体引入的费用回归，从不曾出现在团队的日常体感里。人类写下一个慢 10× 的函数，下一件事也会跟着慢；智能体写下一段贵 10× 的 prompt，对团队而言跑起来速度一样，成本却在账单上悄悄攒着。解法：把"每回合成本"按技能、仓库、change-set 打标签，并接到一道护栏上。*首次出现于第 04 章。* {cite}`langchain2026tbench`。

## DORA 度量

DevOps Research & Assessment 的四条度量——部署频率、交付前置时间、变更失败率、平均恢复时间。作为产出指标，HarnessCard 最终喂给它们。*首次出现于第 12 章。* {cite}`forsgren2018accelerate`。

## Design by Contract（契约式设计）

Meyer 1992 年提出的原则——子程序把前置条件、后置条件与不变量作为"一等公民制品"来声明。SDD × 缰绳 里"规约先行"的智识先祖。*首次出现于第 04 章。* {cite}`meyer1992contracts`。

## Entropy（马具语境下的"熵"）

马具表面上"过期、已坏、或具有误导性"内容的累积。若不管它，熵会把一具能工作的马具，变成一具装饰物。*首次出现于第 06 章。* {cite}`cunningham1992debt`。

## Fence（护栏）

第 05 章的一个区域，容纳自动化的"拒绝"——钩子、linter、schema 校验器、密钥扫描器。在按键或 commit 的那一刻触发。*首次出现于第 05 章。* {cite}`walterfan2026guardians`。

## Final Acceptance（终审）

`lazy-scrum-team` 里的一个角色——署名持有制品状态机中 `review → approved` 这条跃迁。它本身不做评审；评审由 Code Reviewer 角色去做。*首次出现于第 09 章。* {cite}`lazyscrumteam2026`。

## Groom（梳理）

第 05 章的一个区域，容纳"反复要做的维护"——每周审计、仪表盘留存评审、对陈旧文档的清扫。照看的是马具本身，不是产品。*首次出现于第 05 章。* {cite}`walterfan2026guardians`。

## Hard Gate（硬关卡）

一道关卡——拒掉一次 commit、合并或发布，*没有豁免通路*。单元测试失败、密钥扫描命中、以及新代码上的 lint 错误，默认都是"硬"的。*首次出现于第 06 章。* {cite}`humble2010continuousdelivery`。

## Harness（马具）

智能体在其中运作的那个环境——它所读的规约、它所通过的关卡、它所奔跑的牧场、以及那个让环境保持活着的 Groom。不是智能体本身。*首次出现于第 01 章。* {cite}`fowler2026harness`。

## HarnessCard

CAR 论文所提出的那份标准化披露格式：十二格 ＋ 层级注释 ＋ 一条主引用；在附录 D 中以"可直接粘贴"的表格形式交付。*首次出现于第 05 章。* {cite}`car2025decomposition`。

## Harness Theatre（马具剧场）

一类失败模式——马具在长（规则变多、文件变多、仪表盘变多），它的杠杆却没在长（以"每周拒绝数、每周度量数、每周被掰方向的决策数"来衡量）。诊断尺：马具形状的制品数，对比于"被拒绝或被度量的事件数"——一具健康马具多数日子里都会拒掉点什么；一具剧场化马具则连续数周什么都没拒绝，而文件数却还在涨。书中点名的子类：望远式 `AGENTS.md`、一路放行的 pre-commit、仪表盘剧场、无工具的工作流、HarnessCard 虚荣 delta。*首次出现于第 01 章；在第 06 章展开。* {cite}`cunningham1992debt`。

## Harness Engineering（马具工程）

在 AI 辅助的软件工程里，把马具当作一等公民制品来 *设计、建造、运行* 的那门实践。该术语及其工业语境，可追溯至 Fowler 2026 年的那篇文章，以及作者 2026-03-28 的那篇博文。*首次出现于第 01 章。* {cite}`fowler2026harness`。

## Hook（钩子）

Claude Code 的一类回调——在某个具名生命周期事件（`PreToolUse`、`PostToolUse`、`SessionEnd`、`UserPromptSubmit`）触发。退出码 2 会拒掉当前正在进行中的那次工具调用。*首次出现于第 05 章。* {cite}`anthropic2024claudecode`。

## Lazy AI Coder

本书所承载的开源仓库——`walterfan/async-harness-book`——也是第 11 章实例的对象。*首次出现于第 11 章。* {cite}`lazyaicoder2026`。

## lazy-scrum-team

一具以 Claude Code／Cursor 技能包形式交付的开源"工作流编码型马具"。"制品状态机、返工矩阵、硬／软关卡分类"三者的权威出处。*首次出现于第 06 章。* {cite}`lazyscrumteam2026`。

## Living Documentation（活文档）

Martraire 所提出的术语——从运行中的代码里生成、或与其保持同步的那类文档。第 05 章 SDD × 梳理 这一格，是把这一概念落地的地方。*首次出现于第 04 章。* {cite}`martraire2019living`。

## MCP（Model Context Protocol）

Anthropic 2024 年提出的一份开放规范——定义 LLM 客户端与工具服务器之间的工具调用。OpenHarness、Claude Code 以及许多马具都对齐它。*首次出现于第 07 章。* {cite}`anthropic2024mcp`。

## MDD（Metric-Driven Development，度量驱动开发）

第三位护法——在代码交付之前就先"指名道姓"地定义可观测信号，并在交付之后持续照看它们的那门实践。*首次出现于第 04 章。* {cite}`majors2022observability`。

## Meta-Harness（元马具）

一具把自己也当作产品来对待的马具——有自己的 changelog、发布节奏、HarnessCard。第 06 章"运行马具"的四大关注中的第四个。*首次出现于第 06 章。* {cite}`ford2017buildingevolutionary`。

## Observability（可观测性）

通过 log、metric 与 trace，让一个运行中的系统"从外部也能被看懂"的那门手艺。MDD 就是把可观测性带进马具的那位护法。*首次出现于第 06 章。* {cite}`majors2022observability`。

## OpenHarness

香港大学数据科学实验室出品的那套开源"马具参考实现"。第 07 章即是对它的案例研究。*首次出现于第 05 章。* {cite}`hkuds2025openharness`。

## Paddock（牧场）

第 05 章的一个区域，容纳那些有边界的评审仪式与环境——验收表、CI 关卡、staging 泡测。与护栏的区别是——牧场 *更慢、更宽、更权威*。*首次出现于第 05 章。* {cite}`walterfan2026guardians`。

## Prompt Engineering

2023 年前后那一门手艺——写 LLM 提示，以期产出所希望的输出。属于第 05 章 SDD × 缰绳 的一个子集；对于智能体时代的马具而言，仅此一项并不够。*首次出现于第 02 章。* {cite}`brown2020gpt3`。

## ReAct

Yao 等 2022 年提出的一种模式——在智能体回路里把 *推理（Reasoning）* 与 *行动（Acting）* 合一。每一套现代 Agent Loop（包括 OpenHarness 的那套）的学术谱系。*首次集中讨论于插章；代码级案例见第 07 章。* {cite}`yao2022react`。

## Reverse-Engineering Disclaimer（逆向工程免责声明）

第 10 章（以及任何一章"闭源案例研究"）必须开篇的那一段二级标题：结构化地声明来源、观察窗口与撤回承诺。*首次出现于第 10 章。* {cite}`zhangbook2026`。

## Rework Matrix（返工矩阵）

"发现者 × 修复者"表格——为每一次交接署名点出必须随附的那件返工制品。权威处理在第 09 章 09.3。*首次出现于第 06 章。* {cite}`gousios2014pullbased`。

## SDD（Spec-Driven Development，规约驱动开发）

第一位护法——把 `AGENTS.md`、客户端兼容层、可执行规约这类"规约制品"视为一等公民、在任何实现开始之前就让智能体可读的那门实践。*首次出现于第 04 章。* {cite}`martraire2019living`。

## Skill（Claude Code）

一份 `SKILL.md` 文件——智能体通过 front-matter 里的 `description:` 将其发现并自动调用。*首次出现于第 08 章。* {cite}`anthropic2024skills`。

## Skill Engineering（技能工程）

2026 年前后这一门手艺——编写可复用的技能，以"塑造智能体在下笔之前如何思考"。在 prompt engineering 与 context engineering 之上继续往上搭。*首次出现于第 08 章。* {cite}`vincent2025superpowers`。

## Spec Drift（规约漂移）

SDD 的一种"沉默失败模式"——代码库悄悄漂离 `AGENTS.md` 所主张的样子，规约却没有被更新。智能体把规约当作权威来读，继续生成与规约自洽的代码；人类把代码库当作现实来读，继续写与代码库自洽的代码；裂缝从两头一起拉大。解法：安排一项定时 Groom 任务——每周比对"规约的机器可检查主张"与代码库，并拒绝"无声漂移"。*首次出现于第 04 章。* {cite}`martraire2019living`。

## Soft Gate（软关卡）

一道关卡——默认拒绝，但允许"由署名角色签、带到期日"的豁免。覆盖率下限、成本上限、文档 link-check，都是常见的软关卡。*首次出现于第 06 章。* {cite}`humble2010continuousdelivery`。

## Specification by Example（范例化规约）

Adzic 2011 年提出的术语——把验收标准转化为可执行范例的那门实践。第 05 章 SDD × 牧场 这一格背后的词汇源。*首次出现于第 05 章。* {cite}`adzic2011specbyexample`。

## Superpowers

Joseph Vincent 为 Claude Code 出品的那座开源技能库。第 08 章是它的案例研究。*首次出现于第 08 章。* {cite}`vincent2025superpowers`。

## TDD（Test-Driven Development，测试驱动开发）

第二位护法——Beck 2002 年提出的那门纪律："先写一个红的测试，再写实现"。进入智能体时代之后，重心被重新摆到 TDD × 缰绳（把测试作为输入）与 TDD × 护栏（钩子拒掉红树下的编辑）这两格。*首次出现于第 04 章。* {cite}`beck2002tdd`。

## Test-Pinning（把错误解读钉死）

智能体时代 TDD 的一种失败模式——人类写下的一条测试，对他心里那种行为来说 *技术上* 是正确的，却留下了一处"解读自由度"，被智能体见缝插针地填掉。测试绿、行为错；而这条绿测试，把智能体的错误理解固化进了仓库记忆。解法：写"对抗性测试"——专门去证伪"从 prompt 到变绿"的那条最便宜路径；也就是评审人在每一次"首发即过"时都要有的那条"再加一条测试"的习惯。*首次出现于第 04 章。* {cite}`ziegler2022productivity`。

## Technical Debt（技术债）

Cunningham 1992 年的隐喻——"因便宜设计选择而累积下来的成本"。第 06 章那套 *熵* 的词汇，就是它在马具语境下的一次特化。*首次出现于第 06 章。* {cite}`cunningham1992debt`。

## Toolformer

Schick 等 2023 年的论文——把"一等公民级的工具使用"确立为 LLM 的一个主要行动面。OpenHarness 43 个工具那份分类的学术谱系。*首次集中讨论于插章；工具分类案例见第 07 章。* {cite}`schick2023toolformer`。

## 《马书》（*Ma's book*）

张汉东 2026 年对 Claude Code 内置提示、技能系统、hooks 契约与工具 schema 的逆向工程研究。第 10 章的第一手来源。*首次出现于第 10 章。* {cite}`zhangbook2026`。
