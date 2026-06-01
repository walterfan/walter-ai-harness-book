---
status: draft
chapter-type: narrative
---

# 插章：AI Agent 与编程工具的结构

> *你没法驾驭一个你没有拆开看过的东西。*

第 03 章给 Harness Engineering 下了定义：它不是造智能体，而是造智能体周围的环境。本插章补上中间那块剖面图：现代 AI Agent 与 AI 编程工具，到底由哪些层组成？它为什么会跑偏？又该把马具接在哪些位置，才能让它更接近"按照我的想法、规则和习惯，从头到尾完成一个项目"？

先给结论：**不要把智能体想成"一个会写代码的大模型"。** 更准确的模型是：

```text
用户输入 → 上下文装配 → 大模型决策 → 工具调用 → 观察结果
       ↖          记忆更新 ← 状态更新 ← 结果解释 ←
```

也就是说，真正需要被驾驭的不是模型权重本身，而是这条循环里的 **输入、上下文、工具、记忆、停止条件、反馈信号**。一具好马具不是让模型"更聪明"，而是让这条循环每一步都更难偏离你的意图。

## 05.1 Agent Loop：最小心智模型

现代编码智能体的核心，是一个 *observe → decide → act* 的循环。ReAct 把"推理（Reasoning）"与"行动（Acting）"放进同一条轨道 {cite}`yao2022react`；Toolformer 则把工具使用推进为语言模型行动面的第一等公民 {cite}`schick2023toolformer`。落到编码工具里，这条循环通常长这样：

```{mermaid}
flowchart LR
  U["用户输入<br/>task / intent / constraints"] --> C["上下文装配<br/>repo files / docs / memory / rules"]
  C --> M["大模型决策<br/>plan / next action / tool choice"]
  M --> T["工具调用<br/>edit / shell / test / search / MCP"]
  T --> O["观察结果<br/>stdout / diff / error / test result"]
  O --> S["状态与记忆更新<br/>short-term / long-term"]
  S --> M
  M --> F["最终输出<br/>patch / explanation / PR / handoff"]
```

每一圈 loop 都可能变好，也可能变坏。智能体第一次读错意图，第二圈就会把错误当成上下文继续使用；一次工具输出被误解，下一圈就可能在错误前提上继续施工；一段过时的长期记忆被召回，整个项目会沿着旧架构走。Harness Engineering 的切入点，就是让这些错误尽早暴露、尽早被拒绝、尽早被回灌。

## 05.2 七个承重点

### 用户输入：目标不是 prompt，而是任务契约

用户输入不是"请帮我做 X"这么一句话。对编码智能体来说，真正有用的输入至少包含四项：

- **目标**：要交付什么行为。
- **边界**：哪些目录、接口、依赖不能碰。
- **验收**：什么测试、截图、命令或指标算完成。
- **偏好**：团队的命名、错误处理、日志、提交风格。

如果这些没有写清，智能体不会停下来等待澄清；它会选一个看似合理的解释，然后自信地写下去。第 07 章把这种失败叫 **歧义放大**。

对应马具：`AGENTS.md`、issue 模板、验收表、设计草案、任务拆分 skill。

### 上下文窗口：长不等于准

Context window 是智能体当下能看到的那一卷材料。它可能包括当前对话、打开的文件、检索片段、错误日志、测试结果、规则文件和工具 schema。Karpathy 所谓 context engineering，讲的正是如何组合这份输入窗口 {cite}`karpathy2025context`。

上下文越长，召回越多，但污染也越多。三段"差不多相关"的旧实现，可能比没有上下文更糟：模型会把它们取平均，生成第四种同样平庸的实现。RAG 的价值不是"把更多东西塞进来"，而是把 **该看的东西** 放进来，把 **不该看的东西** 拦在外面 {cite}`lewis2020rag`。

对应马具：sources-of-truth 索引、上下文白名单、弃用路径黑名单、检索质量评审、坏链扫描。

### 记忆：短期记忆负责连贯，长期记忆负责惯性

短期记忆通常是本轮对话、scratchpad、计划列表、最近工具输出。它让智能体能连续工作，也会让一次错误解释在后续 loop 中反复扩散。

长期记忆通常是知识库、向量索引、规则文件、历史总结、项目 wiki。它让智能体继承团队习惯，也会让过时架构继续阴魂不散。对长期记忆来说，最危险的状态不是"没有"，而是"有，但没人知道它已经旧了"。

对应马具：`verified:` 日期、Groom job、过期记忆清单、ADR 状态、memory reset 规则。

### 工具：智能体真正改变世界的手

模型只生成 token；工具才改变世界。编辑文件、运行 shell、调用浏览器、访问 MCP server、发 PR、查日志、跑部署，都是工具面的一部分。MCP 把工具契约做成可声明、可发现、可组合的协议面 {cite}`anthropic2024mcp`。

工具面有三类典型风险：

- **工具幻觉**：模型以为有某个工具或参数，但实际没有。
- **权限过宽**：工具能做的事超过当前任务需要。
- **观察误读**：工具返回错误，模型却把它当成功继续推进。

对应马具：工具 schema 检查、权限白名单、危险工具审批、命令输出解析、失败码硬拒绝。

### Prompt、rule、skill：过程被写成制品

Prompt 是一次性的说法；rule 是仓库里的家规；skill 是可复用的流程。它们都在塑造智能体"下一步该怎么做"，但承重能力不同。

一条 prompt 能解决一次任务；一条 skill 能解决一类任务；一条被 hook 约束的 skill，才能成为团队纪律。没有护栏的 skill，容易退化为"我会按照 TDD 技能来做"这种合规口号。

对应马具：`SKILL.md`、`.cursor/rules`、Claude Code commands、`AGENTS.md`、skill 前置条件检查。

### Controller：循环预算、停止条件与升级路径

Agent Loop 需要一个 controller：决定下一步是否继续、调用哪个工具、何时停止、何时向人类升级。很多"跑偏"不是模型第一步错了，而是 controller 没有及时刹车。

常见失控模式：

- 连续三次测试失败仍继续乱改。
- 成本超过阈值仍继续请求模型。
- diff 变得过大仍不切小任务。
- 任务目标变化后仍沿着旧 plan 前进。

对应马具：turn budget、cost cap、diff size cap、失败重试上限、升级规则、SessionEnd 总结。

### 输出：最终答案不是终点，证据才是终点

编码智能体的最终输出不应只是"我完成了"。工程上有用的输出至少包含：

- 改了哪些文件。
- 跑了哪些命令。
- 哪些检查通过。
- 哪些风险仍未处理。
- 哪个证据能证明需求被满足。

对应马具：PR 模板、Verification Table、HarnessCard delta、release note、可复现脚本。

## 05.3 跑偏的七种原因

| 跑偏原因 | 表面症状 | 真正问题 | 对应马具 |
|---|---|---|---|
| 目标含糊 | 代码能跑，但不是你要的 | 用户输入没有验收条件 | SDD × 缰绳 |
| 上下文污染 | 生成了混合风格实现 | 检索召回了旧路径或坏例子 | SDD × 梳理 |
| 工具幻觉 | 调了不存在的命令或参数 | 工具 schema 不被验证 | SDD × 护栏 |
| 权限过宽 | 改了不该改的目录 | 工具面没有边界 | TDD × 护栏 / 牧场 |
| 红树继续写 | 测试失败后越改越多 | 没有及时拒绝 | TDD × 护栏 |
| 成本失控 | 结果一样，账单变大 | loop 缺少成本信号 | MDD × 护栏 |
| 记忆漂移 | 按旧架构写新代码 | 长期记忆无人维护 | SDD × 梳理 |

这张表的重点是：跑偏很少只有一个原因。一次"智能体不听话"，往往同时包含含糊任务、污染上下文、过宽工具和缺失反馈。Harness Engineering 的价值，是把这些原因拆开，让每个原因都能落到一件可改的制品上。

## 05.4 针对性驾驭：把马具接到正确层

```{list-table}
:header-rows: 1
:widths: 18 22 22 22 22

* - Agent 层
  - 缰绳
  - 护栏
  - 牧场
  - 梳理
* - 用户输入
  - issue 模板、任务契约
  - prompt schema
  - PO / reviewer 验收
  - 复盘含糊需求
* - 上下文
  - sources-of-truth 索引
  - 禁用路径检查
  - 上下文包评审
  - 坏链与过期文档扫描
* - 记忆
  - `verified:` 日期
  - 过期记忆拒绝
  - ADR 状态机
  - 定期 memory prune
* - 工具
  - 工具说明与示例
  - schema / permission gate
  - 沙箱与审批
  - 工具清单审计
* - Skill / rule
  - `AGENTS.md` / `SKILL.md`
  - skill 前置条件检查
  - 角色化 review
  - skill drift review
* - Controller
  - plan / budget
  - turn cap / cost cap
  - 分阶段验收
  - 失败模式复盘
* - 输出
  - 完成定义
  - PR 模板检查
  - Verification Table
  - HarnessCard delta
```

一旦你用这张表看 AI 编程工具，就会发现"让它不要跑偏"不是一句愿望，而是一组具体工程选择：上下文要筛，工具要限权，loop 要有预算，输出要带证据，长期记忆要有人梳理。

## 05.5 Autonomy Envelope：什么时候可以少人工纠正

"从头到尾不需要人工纠正"不是一个绝对承诺，而是一条 **autonomy envelope（自主工作包络）**。任务落在包络内，智能体可以高度自主；任务跑出包络，智能体必须停下来、请求澄清或升级给人。

一项任务落在包络内，至少满足八个条件：

1. **目标可验收。** 有测试、截图、命令、指标或人工验收表。
2. **边界清楚。** 允许改哪些目录、禁止改哪些目录写在 `AGENTS.md` 或任务契约里。
3. **上下文可信。** sources-of-truth 明确，过期文档有标记。
4. **工具够用但不过宽。** 能运行测试、编辑文件、查文档；不能随手碰生产、密钥、部署。
5. **失败会被拒绝。** 红测试、密钥扫描、schema mismatch、成本超限都会停住 loop。
6. **记忆可刷新。** 长期规则有 owner 和 Groom 节奏。
7. **输出带证据。** 最终回答必须列出 diff、命令、结果和剩余风险。
8. **有升级路径。** 需求冲突、权限不足、连续失败、超预算时必须停下来问。

这八条都满足时，"少人工纠正"才是工程目标；少一半时，它就只是把人类 review 推迟到更痛的时刻。

## 05.6 一条实用调试法：看 trace，不看态度

当智能体跑偏时，不要问"它为什么不听话"。问这七个 trace 问题：

1. 用户输入里有没有完成定义？
2. 它实际看到了哪些文件和规则？
3. 它召回了哪些长期记忆？
4. 它为什么选择这个工具？
5. 工具返回了什么观察结果？
6. 它如何解释这个结果？
7. 哪一条护栏本该挡住它，却没有挡住？

这就是 Agent Loop 版的事故复盘。你不是在评价模型人格，而是在检查一条工程流水线：输入、上下文、工具、记忆、决策、观察、输出，哪一段缺了马具。

## 研究脉络

- **ReAct** {cite}`yao2022react` —— 把 reasoning 与 acting 放进同一条循环，是本章 Agent Loop 图的学术底座。
- **Toolformer** {cite}`schick2023toolformer` —— 工具不是附属品，而是语言模型行动面的核心组成。
- **RAG 与 Context Engineering** {cite}`lewis2020rag,karpathy2025context` —— 上下文不是越多越好，而是一件需要工程化选择、过滤和维护的输入制品。
- **MCP** {cite}`anthropic2024mcp` —— 现代工具面正在从 ad hoc 函数调用，走向可声明、可检查、可组合的协议。
- **Agent Engineering 经验框架** {cite}`anthropic2024agents,langchain2026tbench` —— 业界已经把 prompts、tools、memory、orchestration、runtime 当作智能体产品的主要剖面；本章把这些剖面翻译成 Harness Engineering 的接点。

## 动手环节

本章的两份 hands-on 制品住在 `source/_handson/05-agent-loop-anatomy/`：

- `agent-loop-harness-map.yaml` —— 把 Agent Loop 的七层映射到缰绳、护栏、牧场、梳理。
- `autonomy-envelope-checklist.md` —— 一份 8 条检查表，用来判断某个任务能否交给智能体高度自主完成。

```{literalinclude} ../_handson/05-agent-loop-anatomy/agent-loop-harness-map.yaml
:language: yaml
```

```{literalinclude} ../_handson/05-agent-loop-anatomy/autonomy-envelope-checklist.md
:language: markdown
```
