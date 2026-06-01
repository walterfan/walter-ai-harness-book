---
status: draft
chapter-type: case-study
case-study-kind: open-source
worked-example: true
---

# 案例研究：OpenSpec —— 把意图变成可合并的工程制品

> *OpenSpec 最有意思的地方，不是它让人"先写文档"，而是它把文档切成一组能被智能体读取、验证、推进、归档的制品。*

本章分析本地快照 `/Users/walterfan/workspace/ai/OpenSpec`。这是一套 TypeScript / Node.js CLI，npm 包名为 `@fission-ai/openspec`，定位是 *AI-native system for spec-driven development*。它的 README 把产品哲学压成五句：fluid not rigid、iterative not waterfall、easy not complex、built for brownfield、scalable from personal projects to enterprises。换成马具工程语言，就是：OpenSpec 不试图替智能体写代码，而是把"写代码之前与之后必须被保留下来的意图"变成一组可解析的、可审计的、可归档的工作制品。

本章不是使用教程。它把 OpenSpec 当成一具马具来解剖：看它怎样把 proposal、specs、design、tasks 串成工件图；怎样把同一组 workflow 注入 Codex、Claude、Cursor、Gemini、GitHub Copilot 等多种 agent 客户端；又怎样用自己的 `openspec/` 目录管理 OpenSpec 自身的演化。

## 15.1 —— 一眼看清这具马具

OpenSpec 的核心不是某一个命令，而是三层结构：

1. **目录契约。** repo 中的 `openspec/specs/` 是当前行为的 source of truth；`openspec/changes/<name>/` 是一项尚未归档的变更；`openspec/changes/archive/` 是已完成变更的历史。
2. **工件图。** schema 把 `proposal → specs/design → tasks → apply` 变成显式依赖。`openspec status --json` 告诉智能体哪些工件已完成、哪些被依赖阻塞。
3. **agent 分发层。** OpenSpec 生成 skills 与 slash commands，把同一套工作流投递到不同客户端的惯用目录里，例如 `.claude/skills/`、`.codex/`、`.cursor/`、`.github/`。

本地快照里，OpenSpec 已经有 **40** 份主规格、**82** 个归档变更、**89** 个测试文件、**25** 个 agent command adapter、**2** 套内置 schema。这些数字说明它不是"演示项目里的一组 markdown"，而是一个用自己管理自己的活系统。

## 15.2 —— 三个最承重的实现选择

第一，OpenSpec 把要求写成 **delta**，不是完整未来态。`openspec/specs/openspec-conventions/spec.md` 要求变更目录里的 spec 使用 `## ADDED Requirements`、`## MODIFIED Requirements`、`## REMOVED Requirements`、`## RENAMED Requirements`。归档时再按 requirement header 匹配并合并。这个设计很适合 brownfield：你不用重写整个世界，只要声明这次行为契约变哪里。

第二，OpenSpec 把 workflow 从硬编码 prompt 中抽出来。`schemas/spec-driven/schema.yaml` 明确列出 `proposal`、`specs`、`design`、`tasks` 四个 artifact，每个 artifact 都有 `requires`、`template`、`instruction`。`src/core/artifact-graph/graph.ts` 用 Kahn 算法算构建顺序，`getNextArtifacts()` 判断下一步能做什么。于是智能体不是凭聊天记忆推进，而是沿着一张可计算的依赖图推进。

第三，OpenSpec 承认 agent 工具生态是碎片化的。`src/core/config.ts` 里列出 20 多种工具；`src/core/command-generation/adapters/` 把同一份 `CommandContent` 格式化成各工具自己的命令文件。这个选择把 OpenSpec 从"某个 IDE 的功能"变成"跨 agent 的规格层"。

这三个选择可以压成一句话：**OpenSpec 把意图从聊天窗口里搬出来，落到可版本化的工件图里，再把这张图翻译给不同 agent 客户端。** 这就是它相对普通 spec 模板的本质差异。模板只规定"文档长什么样"；OpenSpec 规定"文档之间如何依赖、如何推进、如何验证、如何归档"。

## 15.3 —— OpenSpec 的六个精华模式

OpenSpec 最值得搬走的，不是文件名，也不是 `/opsx:*` 命令本身，而是六个可复用模式。

### 15.3.1 —— Intent Ledger：把意图做成账本

`openspec/changes/<name>/` 是一份意图账本。`proposal.md` 记录为什么做，`specs/` 记录可验证行为怎么变，`design.md` 记录关键技术取舍，`tasks.md` 记录如何落地。它们不是"写完就丢"的文档，而是一次变更的会计凭证：实现开始前，它们约束智能体；实现过程中，它们吸收新发现；实现结束后，它们被 archive 合并回主规格。

这个模式解决了 AI 编码里一个常见断裂：人类在聊天里说过的限制，智能体两轮之后忘了；智能体在实现中发现的事实，下一轮又沉回聊天历史底部。Intent Ledger 把这些东西放进仓库路径，而不是放在上下文窗口里。

### 15.3.2 —— Artifact Graph：让工作流可计算

许多团队说"先写需求，再写设计，再写任务"，但这句话通常只是流程口号。OpenSpec 把它变成 schema：

```text
proposal
  ├── specs
  └── design
       └── tasks
```

实际 schema 里 `tasks` 同时依赖 `specs` 与 `design`，`apply.requires` 又指向 `tasks`。这意味着 agent 可以问 CLI："现在什么 artifact ready？什么被阻塞？生成这个 artifact 前要读哪些依赖？" 这比提示词里的"请先计划"强得多，因为状态不再靠智能体自觉维持。

### 15.3.3 —— Delta-First Brownfield：只描述变化，不重写世界

OpenSpec 没有要求每次变更都生成一份完整未来态 spec。它让 change spec 只写 delta，再由 archive 阶段合并回 `openspec/specs/`。这对 brownfield 很关键：真实软件的大多数工作是修改既有行为，而不是从空白项目开始写一份总纲。

delta-first 的代价是 archive 复杂度上升，所以 OpenSpec 用 header-based matching 和 validator 把合并前提机械化：MODIFIED 要带完整 requirement block；REMOVED 要指名；RENAMED 要成对。这个选择很有工程味：把复杂度集中在工具里，而不是摊给每一次人工 review。

### 15.3.4 —— Prompt Supply Chain：提示词也有供应链

OpenSpec 的 workflow 指令不是散落在 README、聊天模板、个人记忆里，而是从 schema、templates、project config、rules 拼装出来。`openspec/config.yaml` 可以注入项目上下文；`rules` 可以按 artifact ID 分发约束；`instructions` 命令把上下文、规则、依赖、模板、输出路径装进结构化块。

这等于给 prompt 建了一条供应链：源材料在哪里、谁覆盖谁、输出给哪个 agent、什么时候需要更新，都有路径可查。对长期维护来说，这比"团队共享一段大 prompt"耐用得多。

### 15.3.5 —— Adapter Boundary：把 agent 客户端当成输出目标

Superpowers 深度绑定 Claude Code 的 `SKILL.md` 机制；OpenSpec 则把 agent 客户端当成 target。adapter 不改变核心 workflow，只改变落盘格式和路径。这是一个重要边界：OpenSpec 的领域模型是 proposal/spec/design/tasks，不是 Claude skill、Codex command、Cursor rule 或 Copilot instruction。

因此，当某个客户端改目录规范时，应该改 adapter；不应该改 OpenSpec 的核心概念。这个分层，是它能同时支持 25 个 adapter 的原因。

### 15.3.6 —— Self-Hosting：用自己管理自己

OpenSpec 仓库自己的 `openspec/specs/` 和 `openspec/changes/archive/` 是它最有说服力的部分。一个 spec 工具若不用自己的机制管理自己，很难证明那套机制能承受真实演化。本地快照里的 40 份主规格与 82 个归档变更，说明 OpenSpec 至少把自己的方法吃进了日常维护流程。

这也暴露了它的成熟度边界：self-hosting 证明流程可用，但不自动证明流程有效。要证明有效，还需要把这些 change 与缺陷率、返工率、发布节奏、review 周期等产出指标接起来。

```{admonition} 这不是瀑布
:class: note

OpenSpec 的 `docs/opsx.md` 明确把 OPSX 描述为 actions, not phases。`proposal → specs → design → tasks` 是依赖关系，不是行政闸门。真实工作里，开发者可以实现中途回去改 specs，也可以在发现设计不成立时修订 tasks。马具工程看重的是这些修订被保留下来，而不是假装最初计划从未改变。
```

## 15.4 —— 十二格亮点图

```{list-table}
:header-rows: 1
:widths: 20 8 72

* - 格子
  - 得分
  - 证据
* - SDD × 缰绳
  - 5
  - `schemas/spec-driven/schema.yaml`、`docs/opsx.md`、生成的 workflow skills 共同把智能体牵到 proposal/spec/design/tasks 这条路径上。
* - SDD × 护栏
  - 4
  - `src/core/validation/validator.ts` 校验 spec 与 change；delta spec 要有 `SHALL`/`MUST`、scenario、无重复与跨段冲突。
* - SDD × 牧场
  - 4
  - `openspec/changes/` 为每项变更提供独立规划空间；archive 之前不污染 `openspec/specs/`。
* - SDD × 梳理
  - 5
  - 本地快照有 82 个归档变更；OpenSpec 用 OpenSpec 记录自己的演化，形成清晰的活文档循环。
* - TDD × 缰绳
  - 3
  - `tasks.md` 把实现拆成可勾选项，能引导测试工作；但测试策略仍依赖项目自身约定。
* - TDD × 护栏
  - 4
  - Vitest、ESLint、TypeScript build 与 validator 构成强护栏；CI 在 PR 跑 build/test，在 main 跑 Linux/macOS/Windows 矩阵。
* - TDD × 牧场
  - 3
  - workspace beta 支持多 repo / folder 的本地视图；但 implementation 仍回到各 repo 自己的测试与发布边界。
* - TDD × 梳理
  - 3
  - 89 个测试文件覆盖 CLI、parser、validator、workspace 等面；缺口是没有把每个 archived change 反向绑定到失败测试。
* - MDD × 缰绳
  - 3
  - telemetry 只记录 command name 与 version，能观察功能使用；尚未形成用户可见的质量北极星。
* - MDD × 护栏
  - 4
  - telemetry 遵守 `OPENSPEC_TELEMETRY=0`、`DO_NOT_TRACK=1`、CI 自动关闭，且不发送参数、路径、内容或 PII。
* - MDD × 牧场
  - 3
  - npm 包、changesets、CI 与 Nix flake 验证给发布提供基础牧场；缺少公开 SLI / release health 面板。
* - MDD × 梳理
  - 4
  - `openspec config profile`、`openspec update`、profile drift 检测让已生成 skills/commands 能随 workflow 配置同步。
```

这张图的强项集中在 SDD：OpenSpec 非常擅长把意图、需求、设计与任务变成 agent 能消费的上下文。TDD 层也不错，因为它把可解析格式与 CI 结合起来。MDD 层稍弱：它已经有隐私友好的 telemetry，但还没有把"规格工作是否真的提升交付质量"变成一条公开北极星。

## 15.5 —— Artifact Graph：OpenSpec 的骨架

OpenSpec 的 `ArtifactGraph` 很小，但它是整套系统的骨架。schema 被解析成 artifact map；`getBuildOrder()` 算拓扑序；`getNextArtifacts(completed)` 返回当前可写的工件；`getBlocked(completed)` 返回缺哪些依赖。这几个函数看似朴素，却把智能体从"下一步做什么全靠提示词"解放出来。

这是一种很值得搬走的马具模式：把 workflow 做成数据，而不是把 workflow 藏在一段长 prompt 里。长 prompt 会漂移、会被复制粘贴污染、会随客户端而变形；schema + graph 则能被测试、能被 diff、能被不同 agent 共享。

`src/commands/workflow/instructions.ts` 是第二个关键点。它生成的 instructions 不是裸 prompt，而是有 `<project_context>`、`<rules>`、`<dependencies>`、`<output>`、`<instruction>`、`<template>` 的结构化上下文。这里的微妙处在于：context 与 rules 被明确标成"给智能体的约束，不要复制进输出文件"。这解决了很多 agent 工作流常见的污染：把系统提示原样写进设计文档。

## 15.6 —— Delta Specs：为 brownfield 而生的规格格式

OpenSpec 的 delta spec 设计，明显偏向已有系统。新增需求放 ADDED，修改需求放 MODIFIED，删除需求放 REMOVED，重命名放 RENAMED。MODIFIED 要求拷贝完整 requirement block，而不是只写一句"改一下登录逻辑"。这降低了归档时的信息损失。

`src/core/validation/validator.ts` 对 delta 做了几道实用检查：

- ADDED / MODIFIED 必须有 requirement text。
- normative text 必须包含 `SHALL` 或 `MUST`。
- 每个 requirement 至少有一个 `#### Scenario`。
- 同一 section 内不能重复。
- MODIFIED、ADDED、REMOVED 之间不能互相冲突。
- RENAMED 的 old/new 名称要成对，且不能和 ADDED/MODIFIED 产生歧义。

这套规则不是形式主义。它让 archive 命令有足够信息把 change 合并回主 specs，也让 reviewer 能从文本里看见行为契约，而不是只看实现 diff。和 Adzic 的 Specification by Example {cite}`adzic2011specbyexample` 一样，场景不是装饰；它是未来测试与验收的候选边界。

## 15.7 —— 跨 Agent 分发：最容易被低估的一层

许多规格工具输在最后一公里：它们生成了一份漂亮的文档，却没有进入智能体每天工作的上下文。OpenSpec 的解法是维护一组 adapter，把 workflow 变成各 agent 会自动发现的命令或 skill。

本地快照里，`src/core/config.ts` 直接列出 Amazon Q、Antigravity、Auggie、Claude Code、Cline、Codex、Cursor、Gemini CLI、GitHub Copilot、Kiro、OpenCode、Qwen、RooCode、Windsurf 等工具。`src/core/profile-sync-drift.ts` 再检查生成物是否和当前 profile / delivery 模式一致：该有的 workflow skill 缺了，要提示同步；不该存在的旧 workflow 还在，也要提示同步。

这正是马具工程里的 SDD × 梳理：不是只生成一次 `.claude/skills` 或 `.codex` 文件，然后祈祷它们永远不过期，而是承认 agent 客户端与团队 workflow 会不断变化，所以必须有 drift detection 与 update 机制。

## 15.8 —— Workspace Beta：从 repo-local 到 coordination surface

`docs/concepts.md` 里的 workspace beta 值得单独看。OpenSpec 把 repo-local 项目和 coordination workspace 分开：

- repo-local `openspec/` 存 specs、changes、archive，适合一个 repo 自己持有规划与归档。
- managed workspace 存在 `getGlobalDataDir()/workspaces/<name>/`，里面有 `workspace.yaml`、生成的 `AGENTS.md`、编辑器 workspace 文件，用来把多个 repo 或 folder 链成一个本地视图。

这层抽象很现实。许多 AI 编码任务不是单 repo 的：一个功能可能横跨 API、web、worker、infra。OpenSpec 没有强行把多 repo 规划塞进某个业务 repo，而是把 workspace 定义成"私有本地视图"，再用 stable link names 指向真实路径。这个边界很干净：workspace 提供可见性与上下文，implementation 仍归拥有代码的 repo。

## 15.9 —— OpenSpec vs Superpowers：工件马具与技能马具

第 11 章的 Superpowers 是一套 skill-first 马具：它用约 30 份 `SKILL.md` 教智能体在动笔前先做头脑风暴、计划、TDD、review 与收尾 {cite}`vincent2025superpowersrepo`。OpenSpec 则是 artifact-first：它不只告诉智能体"应该怎么想"，还创建一组可落盘、可验证、可归档的工件。两者都属于 SDD 强马具，但它们强化的是不同肌肉。

```{list-table}
:header-rows: 1
:widths: 18 41 41

* - 维度
  - Superpowers
  - OpenSpec
* - 首要制品
  - `SKILL.md`，核心是工作纪律与认知步骤。
  - `proposal.md`、`spec.md`、`design.md`、`tasks.md`，核心是变更账本。
* - 状态存放处
  - 主要在当前对话、计划文本、人类 review 记忆中。
  - 在 `openspec/changes/<name>/` 与 `openspec/specs/` 中。
* - 工作流表达
  - 散文指令：何时使用、红旗、步骤、停止条件。
  - schema + artifact graph：依赖、模板、输出路径、apply readiness。
* - 采用路径
  - 对 Claude Code 极低成本；拷入 skills 即可。
  - 需要初始化 CLI 与项目目录，但跨 agent 更稳。
* - 强项
  - 改变智能体"思考方式"；尤其适合头脑风暴、TDD、review 纪律。
  - 改变团队"状态保存方式"；尤其适合需求漂移、跨轮次、跨人协作。
* - 弱项
  - 缺少机器可见状态；技能是否被执行，常靠自我汇报。
  - 容易被误用为文档流水线；artifact 是否真实更新，仍靠团队纪律。
* - 最佳搭配
  - 作为 agent 的行为教练。
  - 作为变更的事实账本。
```

### 15.9.1 —— Superpowers 强在"动笔前"，OpenSpec 强在"动笔后仍可追踪"

Superpowers 最锋利的一点，是它能在智能体即将冲进实现前拦一下："先 brainstorm"、"先写计划"、"先写红测试"。它改的是 agent 的局部行为，尤其是当前回合的思考顺序。若团队的问题是 agent 太急、太自信、跳过测试，Superpowers 的收益立竿见影。

OpenSpec 的锋利处在另一个位置：一周之后，谁还能知道当初为什么这么改？实现过程中学到的新事实是否回到了规格？归档时当前行为是否更新？这些问题不是 skill 能单独解决的。OpenSpec 用目录、schema、validator、archive 把"记住变化"这件事外部化。

### 15.9.2 —— Superpowers 是认知协议，OpenSpec 是状态协议

Superpowers 的协议对象是智能体："遇到这种任务，你应该调用这个 skill，按这些步骤思考。" OpenSpec 的协议对象是仓库："一次变更应该有这些工件，它们有这些依赖，达到这些条件后才能 apply / archive。"

这一区别解释了两者在十二格里的形状。Superpowers 在 **SDD × 缰绳** 与 **TDD × 缰绳** 上极强，因为它直接重塑 agent 的工作姿态；OpenSpec 在 **SDD × 护栏 / 牧场 / 梳理** 上更强，因为它把格式校验、独立变更空间、归档循环做成了外部状态。

### 15.9.3 —— 两者组合时，分工应该明确

把两者叠在一起，最稳的分工是：

- Superpowers 管 **如何思考**：先澄清、先计划、先写测试、先 review。
- OpenSpec 管 **思考留下什么制品**：proposal、delta specs、design、tasks、archive。
- 宿主仓库 CI / hooks 管 **什么不能通过**：测试失败、spec 格式错误、未归档变更、越权命令。

例如，一个高质量的变更流可以是：

1. 用 Superpowers 的 brainstorming skill 澄清问题边界。
2. 用 OpenSpec `/opsx:propose` 生成变更账本。
3. 用 Superpowers 的 TDD skill 执行 `tasks.md` 中的第一项实现。
4. 用 OpenSpec validator 检查 spec / change 格式。
5. 用 Superpowers 的 code review skill 做合并前审查。
6. 用 OpenSpec archive 把 delta 合并回主规格。

这样 Superpowers 不必承担状态存储，OpenSpec 也不必假装自己能改变智能体的所有局部习惯。两者叠加，才接近一具完整马具。

### 15.9.4 —— 两者的共同盲点：产出度量

Superpowers 没有告诉你哪条 skill 被实际调用、调用后缺陷是否下降；OpenSpec 目前也没有告诉你某类 artifact 是否缩短 review 周期、减少返工、降低变更失败率。它们都能改善输入质量，但都还没有完整证明输出质量。

这给团队一个很实际的落点：采用 Superpowers 或 OpenSpec 后，不要只统计"写了多少 specs"或"安装了多少 skills"。更该看：

- 需求返工次数是否下降。
- PR review 中"需求不清"类评论是否下降。
- 已归档 specs 与当前实现的漂移是否下降。
- 变更失败率、回滚率、平均恢复时间是否改善。

如果这些指标不动，说明马具可能只是在长胖。

## 15.10 —— 风险与盲区

OpenSpec 的最大风险，是它的优势会被误用成"文档生产流水线"。如果团队只是在 `/opsx:propose` 里生成 proposal/spec/design/tasks，然后不在实现中更新它们，OpenSpec 会迅速退化成更漂亮的票据模板。它真正的价值在 archive：把变化后的行为契约合并回 `openspec/specs/`，让下一轮智能体读到的是当前真实系统，而不是上一次计划时的愿望。

第二个风险是 validator 与语义之间仍有距离。`SHALL`、`MUST`、scenario 数量、header 唯一性都可以机器检查，但"这个 requirement 是否真的表达了用户价值"仍要靠 reviewer。OpenSpec 提供的是可审计表面，不是产品判断的替代品。

第三个风险是 adapter 面太宽。25 个 adapter 是分发优势，也意味着每个客户端规则变化都可能引入 drift。`profile-sync-drift.ts` 已经做了生成物层面的梳理，但长期看，OpenSpec 需要持续投资 adapter 合约测试，尤其是那些客户端目录规范常变的工具。

```{admonition} 陷阱 —— 把 specs 当成实现计划
:class: warning

一支团队把所有实现细节都写进 `spec.md`：函数名、类名、数据库字段、第三方库选择，写得很认真。两周后实现发现更好的结构，代码变了，specs 却不敢动，因为它们已经像合同一样沉重。**为什么**：OpenSpec 的主 specs 应该描述可验证行为，而不是冻结实现。实现细节属于 `design.md` 和 `tasks.md`；行为契约才属于 `spec.md`。这也是 OpenSpec 自己的 `openspec/config.yaml` 反复强调的边界：Product language first, implementation mechanics later.
```

## HarnessCard

```{list-table}
:header-rows: 1
:widths: 35 65

* - 字段
  - 值
* - HarnessCard schema 版本
  - CAR-HarnessCard v0.2 {cite}`car2025decomposition`
* - 对象
  - OpenSpec，本地快照 `/Users/walterfan/workspace/ai/OpenSpec`，2026-05-30
* - 许可证
  - MIT
* - Control 层（CAR）
  - schema、workflow skills、project config、rules/context injection 共同塑造智能体行为。
* - Agency 层（CAR）
  - CLI 命令、artifact graph、validator、adapter registry 共同约束 agent 可见动作。
* - Runtime 层（CAR）
  - Node.js ≥20.19、pnpm、Commander CLI、Vitest、GitHub Actions、Nix flake。
* - SDD（0–5）
  - 4.5
* - TDD（0–5）
  - 3.25
* - MDD（0–5）
  - 3.5
* - 主要证据
  - `README.md`、`docs/opsx.md`、`schemas/spec-driven/schema.yaml`、`src/core/artifact-graph/`、`src/core/validation/validator.ts`、`openspec/specs/`
```

## 研究脉络

- **Specification by Example** {cite}`adzic2011specbyexample` —— OpenSpec 把 requirement scenario 变成可解析格式，与"示例即规格"的思想同源。
- **Fowler 的 Harness Engineering 词汇** {cite}`fowler2026harness` —— 本章用"三大护法 × 四区域"来读 OpenSpec。
- **CAR 分解** {cite}`car2025decomposition` —— HarnessCard 使用 Control / Agency / Runtime 三层描述。
- **DORA / Accelerate** {cite}`forsgren2018accelerate` —— OpenSpec 未来若要证明产出改善，需要把规格活动接到交付指标上。

## 动手环节

想亲手验证本章分析，可以在 `/Users/walterfan/workspace/ai/OpenSpec` 里跑以下只读或本地检查命令：

```bash
pnpm run build
pnpm test
pnpm lint
node bin/openspec.js list --specs
node bin/openspec.js schemas --json
node bin/openspec.js validate --specs
```

最值得读的路径是：

- `schemas/spec-driven/schema.yaml` —— 默认 artifact graph。
- `src/core/artifact-graph/graph.ts` —— 拓扑排序、ready / blocked 判断。
- `src/commands/workflow/instructions.ts` —— 给 agent 的结构化上下文生成。
- `src/core/validation/validator.ts` —— spec 与 delta spec 的可执行护栏。
- `src/core/command-generation/adapters/` —— 跨 agent 分发层。
- `openspec/specs/openspec-conventions/spec.md` —— OpenSpec 用来约束自己的元规格。
