---
status: draft
chapter-type: methodology
---

# 运行一具马具：熵、可观测性、审批关卡与元马具演进

> *马具不是一件交付就完事的项目，它是一片你要持续照料的环境。*

第 08 章把那十二个格子画成了一张静态矩阵。本章回答矩阵留下的运行层问题：格子被填满之后，*周一到周五* 究竟是什么样子？答案围绕四项关切组织——**熵管理**、**可观测性实践**、**审批关卡**、**元马具演进**——并直接从第 12 章将要完整讨论的 `lazy-scrum-team` 工作流仓库里借来三种结构性的模式。

## 关切一 —— 熵管理

### 这是什么

每一具马具都在累积熵：过期的 `verified:` 头、`AGENTS.md` 里的死链、比上游审计源落后两个 minor 版本的 npm 依赖、上周 `cargo audit` 报警而后被悄悄关掉的 Rust crate。放任不管，熵会把一具能工作的马具变成一具 *装饰性* 的马具——文件还在、评审人还在打勾，但智能体和人都绕着它走。Cunningham 1992 年提出的技术债比喻 {cite}`cunningham1992debt`、以及 Tom 等人 2013 年的系统综述 {cite}`tom2013debtinterest` 都适用，但本章特意把这种现象叫做 *熵*，以强调：即便马具所包裹的代码并未衰变，马具本身仍在衰变。

### 日常做法

熵靠两项反复运行的作业来压住：一条 **文档同步检查**——当文档与代码漂移时拒绝合并（下方的 `doc-sync-check.sh`），以及一条 **每周审计工作流**——在一遍流水里跑完 `cargo audit`／`npm audit`／`gitleaks`，并在 `reports/` 下写一份带日期的报告。两份报告之间的 diff，就是 *那条* 熵信号；不保留至少两周报告的团队，没法把熵和天气分开。

```{literalinclude} ../_handson/09-operating-a-harness/doc-sync-check.sh
:language: bash
```

```{literalinclude} ../_handson/09-operating-a-harness/entropy-audit.yml
:language: yaml
```

更深一层的机制，叫 **差分衰减**。代码的熵，由每一条 bug、每一条评审意见、每一次构建失败来偿还——成千上万股小的压力让它贴近现实。而马具的熵，由 *没有任何东西* 偿还：一条过期的 `AGENTS.md` 规则不会崩任何东西，它只会悄无声息地把方向引偏。一个季度下来，两者发散——代码保持当下，马具开始漂移——而马具的腐烂是最看不见的那种腐烂，恰恰因为它不会自己喊出来。这就是梳理为什么是一 *列* 而不是一条脚注。

```{admonition} 陷阱——"出了事再审计"
:class: warning

一支团队推迟每周的熵审计，因为"没什么在着火"。六个月后真的着火了：一条带已知 CVE 的依赖被带到了生产，一路回溯，发现三月份就有一条 `npm audit` 告警——没人看见，因为当时没有周报可以和四月份那份对照。**为什么**：熵审计是 *校准*，不是诊断——它的价值来自于"一周一周产生基线"。只在事故期间跑审计的团队，没有基线，审计输出就读成噪声。**症状**：CVE 的修复周转以月计而非以天计；`npm audit --audit-level=high` 返回几十条结果，却没有意见说哪些是新增的；每次事故的第一步都是"我们来看看当时有没有告警"。**解法**：审计按日历跑，*即便*（尤其是）没事的时候也跑；带日期的 `reports/` 目录就是基线；周与周之间的 diff 才是信号。
```

## 关切二 —— 可观测性实践

### 这是什么

在马具的语境里，可观测性意味着三面被持续可读 {cite}`majors2022observability`：(a) 产品团队本来就在盯的生产 SLI；(b) 产品团队通常 *不* 盯的那类马具内部信号——token 成本、缓存命中率、智能体 turns-to-green {cite}`langchain2026tbench`；(c) *规约遵循度* 信号——把 `AGENTS.md` 这张面，与日志里看到的行为对起来比。

### 日常做法

一份最小化的可观测性配置，从把 Claude Code 的 `/cost` 端点暴露给 Prometheus 开始，剩下的交给现有的 dashboard 栈去做。这事是三行 scrape 配置，不是一次平台重设计：

```{literalinclude} ../_handson/09-operating-a-harness/prometheus-scrape.yml
:language: yaml
```

比配置更重要的是那一步 *文化* 动作：有一个人成为这块 dashboard 的 owner，在周一的复盘上照着它发言。没有 owner 的 dashboard，腐烂得比没有埋点的代码还快 {cite}`humble2010continuousdelivery`。

```{admonition} 陷阱——"规约遵循度盲区"
:class: warning

一支团队把生产 SLI 接到了 Prometheus、加上每轮成本埋点，两头都盯得一丝不苟——却从来没给 *规约遵循度* 做埋点。结果：当智能体的代码悄悄偏离 `AGENTS.md` 的宣称时（新的写操作绕过 repository 模式、新端点跳过认证中间件），所有 dashboard 都是一片绿，因为偏差不在产品延迟里、也不在智能体成本里——它就在"规约承诺的"和"代码做的"之间那条缝里。**症状**：事故起因是"我们这儿不是这么做的"，此前 dashboard 上没有任何信号；架构师抱怨智能体"不守规矩"，可那些规矩从未被机械化监控。**解法**：对 `AGENTS.md` 里每一条承重条目，问一句"若这条被违反，哪条度量会变为非零？"——答案若是 *没有*，那这条就是无法执行的散文，它属于文档目录，不属于规约。
```

## 关切三 —— 审批关卡（硬 vs 软）

### 这是什么

关卡，是人或自动评审者说 *还不行* 的那些点。两种常见失败模式：**关卡类别未声明**（所有人都默认某道关卡是硬关卡，直到周五下午五点有人需要豁免），以及 **关卡蒸发**（一道总是通过的关卡，会悄悄从团队的心智模型里消失）。这两种失败，都可以靠从 `lazy-scrum-team` 工作流技能 {cite}`lazyscrumteam2026` 借来的三种模式来规避：

- **制品状态机** —— draft → review → approved → archived —— 带显式的跃迁规则和按角色署名的不变量。这里给出一份可被读者直接采用的 YAML 编码：

```{literalinclude} ../_handson/09-operating-a-harness/artefact-state-model.yaml
:language: yaml
```

- **返工矩阵** —— 一张"发现者 × 修复者"矩阵，命名了每一次交接都必须随附的返工制品。第 12 章会完整讲这个。

```{literalinclude} ../_handson/09-operating-a-harness/rework-matrix.md
:language: markdown
```

- **硬关卡 vs 软关卡** —— 每一道关卡在创建时就要声明自己的类别；软关卡的豁免必须带上署名角色和到期时间。完整枚举在第 12 章；这里复刻一份模板，对多数新马具已够用：

```{literalinclude} ../_handson/09-operating-a-harness/hard-vs-soft-gates.md
:language: markdown
```

```{admonition} 陷阱——关卡疲劳与"永远豁免"漂移
:class: warning

一支团队以很紧的关卡起步。六周之后，有三道关卡会在超出它原始范围的合法改动上经常触发；豁免在累积；软关卡的默认值悄悄变成 *先豁免，万一出事再查*。一个季度之内，软关卡充其量只是一层 telemetry——它报告的是什么被豁免，而不是什么被拒绝。**为什么**：误报率大约超过 20% 的关卡会失去心理权威；评审人的默认动作，会从 *质疑这个改动* 翻转为 *质疑这道关卡*。一旦翻转，不经过一次显式重置，它不会再翻回来。**症状**：每个 sprint 的豁免数单调上升；"这一次就破例一下"变成一句大家都懂的口头禅；新人学会这道关卡可以被绕过，比学会它是干什么用的更早。**解法**：把豁免率当作一等度量追踪（每一道软关卡的豁免率本身，就是一条 MDD 信号）；当某道关卡的豁免率越过 20%，*把这道关卡的覆盖范围收紧*（削小它的面积，直到它只在真正的违规上触发），而不是放松策略。一道只在该触发时才触发的关卡，是团队会捍卫的关卡；一道一直在触发的关卡，是团队会绕着走的关卡。
```

## 关切四 —— 元马具演进

### 这是什么

一具不能自我更新的马具，是一具被锁死在它最初作者 2024 年那份世界模型里的马具。元演进，就是把这具马具当作 *它自己的一等产品* 来看待：它有 release、它有 changelog、它有关于自己的度量、它按节奏升级，而不是一慌就升。Ford／Parsons／Kua 的演化式架构 {cite}`ford2017buildingevolutionary` 与 Lehman 的演化律 {cite}`lehman1980laws`，是这件事的理论靠山。

### 日常做法

把元演进作为 *习惯* 来做，成本很低；作为 *项目* 来做，则是灾难。习惯的样子是：

1. HarnessCard 的每一次更新，都以一个 PR 的形式落到马具自己的仓库里，享有与生产代码同等的评审纪律。
2. 马具配备一份专属于马具（不是产品）的 `CHANGELOG.md`，列出每一次缰绳／护栏／牧场／梳理的变更。
3. 每季度一次，团队跑一场 *HarnessCard 评审*，为下个季度设定一项显式的、格子级的目标。

```{admonition} 陷阱——元马具的无穷倒退
:class: warning

一支团队把"马具本身就是一件产品"认真起来，然后提出一具 *元马具*：一具用来治理"马具如何演进"的马具。再接着是一具 meta-meta-harness，用来审计这具元马具。两个 sprint 之内，团队已经拥有一座评审人分不清层次的 YAML 塔，没有哪一层对应到任何一条生产信号，而原来那具马具一步也没动。**为什么**：多一层"meta"只多出评审成本、不多出强制力——元马具里的规则是愿望式的，因为没有任何一层 meta-meta *护栏* 去拒绝坏的 meta 变更。这种倒退，只有当你锚定在一条具体生产信号上时，才会收敛。**解法**：只做一层就打住。马具治理智能体；团队治理马具；马具自身那套 PR 评审纪律，已经够做自治。如果你感到有股拉力在把你往"元马具"那边拽，请改问：哪一条生产信号能告诉我们"这具马具已经退化"了？那条信号，接到每周复盘里，就是唯一值得拥有的一层 meta。
```

### "马具剧场"那种失败，给它起个名字

第 01 章承诺过，本章会给一种失败模式起个名字：马具在长大，杠杆却没涨。那种失败模式叫 *马具剧场*，它有一个可靠的诊断：**马具型制品** 数与 **每周被拒绝的制品** 数之比。一具健康的马具，大部分日子里都会拒绝些什么——一次 commit、一次工具调用、一个 PR、一份豁免申请。一具剧场式的马具，在文件数持续上升的同时，连续数周什么都不拒绝。周一复盘上的经典提问，不是 *"我们给马具加了什么？"* 而是 *"马具拒绝了什么？拒绝得对不对？"* 答不出第二个问题的团队，不该给第一个问题加分。

## Tauri-Todo：一个故事弧里的四项关切

下面这段动手故事，用一个真实的 Tauri 2 + Rust + TypeScript 桌面应用，把所有四项运行关切缝进一条连贯的故事弧。可运行的配套仓库在 `walterfan/lazy-todo-app`；下面三段马具片段住在 `source/_handson/09-operating-a-harness/tauri-todo/` 下，合起来构成一具 Tauri 应用所能拥有的最小、但完整的马具。

### 片段 1 —— `CLAUDE.md`（缰绳兼容层）

Rust 的所有权纪律 {cite}`jung2018rustbelt`，以及 Tauri 的 IPC 边界 {cite}`tauri2024security`，在写下应用代码第一行之前，就给智能体提供了两条强结构性约束。下面这份 `CLAUDE.md` 是 Claude Code 兼容层；在新仓库里，同样内容应优先进入 `AGENTS.md`，再由客户端特定文件指回它。

```{literalinclude} ../_handson/09-operating-a-harness/tauri-todo/CLAUDE.md
:language: markdown
```

### 片段 2 —— `pre-commit-config.yaml`（护栏）

pre-commit 钩子在键盘敲击那一刻就执行缰绳。Tauri 特有的那几条追加——`cargo clippy -D warnings`、推送时的 `cargo audit`、以及一条 `gitleaks` 钩子——让智能体的 Rust 修改变得和它的 TypeScript 修改一样便宜可审。

```{literalinclude} ../_handson/09-operating-a-harness/tauri-todo/pre-commit-config.yaml
:language: yaml
```

### 片段 3 —— `AGENTS.md`（牧场 + 梳理）

最后，`AGENTS.md` 声明角色班底、可合并 PR 契约（硬关卡必须过，软关卡可带带日期的豁免）、以及每周的梳理排班。每一项都引用到本章前面出现过的某份文件——这把通用的运行原语与这段动手故事弧之间的循环闭上了。

```{literalinclude} ../_handson/09-operating-a-harness/tauri-todo/AGENTS.md
:language: markdown
```

Copilot 生产力相关文献 {cite}`peng2023copilotstudy,ziegler2022productivity` 表明：智能体会对环境里 *已经有* 的那种护栏做加速；上面这几份 Tauri-Todo 片段一次性把三层护栏都配齐。把它们 commit 进一份全新 `lazy-todo-app` 克隆的开发者，在第一个功能落地之前，就已经拥有一具能工作的马具。

## 研究脉络

运行一具马具，靠五条可引用的谱系支着：

- **熵与技术债**——Cunningham 1992 年的债务比喻 {cite}`cunningham1992debt`、以及 Tom 等人 2013 年的系统综述 {cite}`tom2013debtinterest`，为"周一早上的审计"提供了动机。
- **可观测性**——Majors／Fong-Jones／Miranda 的 *Observability Engineering* {cite}`majors2022observability` 把马具内部信号框成了一等公民；LangChain Terminal-Bench 2.0 的数据点 {cite}`langchain2026tbench` 给出了行业里把 *turns-to-green* 当作可观测量的基线。
- **审批关卡与发布纪律**——Humble & Farley 的 *Continuous Delivery* {cite}`humble2010continuousdelivery` 提供了硬关卡的语法；`lazy-scrum-team` 技能 {cite}`lazyscrumteam2026` 把它扩展成了上面用到的那张"角色感知"的返工矩阵。
- **元演进**——Ford／Parsons／Kua {cite}`ford2017buildingevolutionary` 与 Lehman {cite}`lehman1980laws` 立下的基础：一个不持续适应的系统会丢失适配度；马具遵守同一条定律。
- **Tauri-Todo 故事弧的地基**——Jung 等人的 *RustBelt* {cite}`jung2018rustbelt` 给"所有权即马具"的论点奠了地基；Tauri 2 的安全白皮书 {cite}`tauri2024security` 给 IPC 边界的讨论奠了地基；Peng 等人与 Ziegler 等人 {cite}`peng2023copilotstudy,ziegler2022productivity` 说明了为什么当智能体处在回路里时，缰绳是承重的。

## 动手环节

运行原语与 Tauri-Todo 故事弧都住在 `source/_handson/09-operating-a-harness/` 下：

- **运行原语：** `doc-sync-check.sh`、`entropy-audit.yml`、`prometheus-scrape.yml`、`artefact-state-model.yaml`、`rework-matrix.md`、`hard-vs-soft-gates.md`。
- **Tauri-Todo 故事弧：** `tauri-todo/AGENTS.md`、`tauri-todo/CLAUDE.md` 兼容层、`tauri-todo/pre-commit-config.yaml`，以及一份 `tauri-todo/README.md`，交叉链接到可运行的配套仓库 `walterfan/lazy-todo-app`。

这些制品合起来，填满了第 08 章矩阵里整列 MDD、以及 SDD × 梳理 那格里的大部分。剩下的 SDD 与 TDD 格子，住在各自章节的动手环节、以及第四部分随后那几章案例研究里。
