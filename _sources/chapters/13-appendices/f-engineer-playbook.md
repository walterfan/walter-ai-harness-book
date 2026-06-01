---
status: draft
chapter-type: appendix
---

(apf-engineer-playbook)=
# 附录 F —— 工程师落地手册

本附录回答一个很实际的问题：读完这本书之后，工程师明天该改哪一个文件？它不是新理论，而是把前面章节压成一份可执行 playbook：一个贯穿样例、一张每章行动表、五条迁移路径、四组好坏例子，以及一套按角色分工的落地节奏。

## F.1 贯穿样例：`todo-cli`

假设你维护一份很小的 Python CLI：`todo-cli`。它有 `todo/`、`tests/`、`pyproject.toml`，也许还有一份普通的 `README.md`。它不是平台工程项目，也没有宏大的 AI strategy；它只是一个会被人和智能体反复修改的小仓库。正因为小，它适合展示 Harness Engineering 的最小闭环。

### Day 0 · 没有马具

仓库里通常只有这些东西：

- `README.md` 解释怎么运行项目。
- `tests/` 里有一些 pytest。
- CI 会在 PR 上跑测试。
- 智能体靠当前 prompt、README 和上下文猜团队习惯。

这不是坏仓库，只是 *未被驾驭* 的仓库。它的问题不是没有文档，而是没有任何东西能在智能体下笔之前明确告诉它"本仓库的边界在哪里"，也没有任何东西在它越界时立刻拒绝。

### Day 1 · 最小三件套

第一天只交付三份文件：

- `AGENTS.md`：说明项目是什么、能改哪里、必须跑哪些命令。
- `.pre-commit-config.yaml`：在 commit 前跑 `ruff` 与快速 pytest。
- `HarnessCard.md`：记录这具马具由哪份规约、哪道护栏、哪些信号构成。

这一步对应第 03 章的最小示例。它的价值不在于文件多，而在于三件事第一次对齐：智能体读到的规约、机器执行的护栏、团队复盘的信号。

### Day 7 · 第一条可证伪规则

一周内挑一条最容易被智能体弄错的规则，让它变成可证伪的规则。例如：

```text
坏规则：写代码时保持风格一致。
好规则：修改 `todo/storage.py` 前必须先跑 `pytest tests/test_storage.py`。
```

前者无法被机器拒绝，后者可以被 hook、CI 或 reviewer checklist 检查。第一个星期的目标不是写完所有规则，而是让团队亲眼看到一条规则从散文变成关卡。

### Day 30 · 交付完整 SDD 行

到第 30 天，`todo-cli` 至少应该有完整 SDD 行：

- **SDD × 缰绳**：`AGENTS.md` 是 canonical 入口。
- **SDD × 护栏**：`AGENTS.md` 中列出的命令必须存在；坏链接、坏 schema 会失败。
- **SDD × 牧场**：PR 模板或验收表逐项确认"交付是否符合规约"。
- **SDD × 梳理**：每周检查 `AGENTS.md` 是否仍与代码和命令相符。

这时团队已经不再只是"写了一份 agent 文档"，而是让规约具备了入口、约束、验收和维护节奏。

### Day 60 · 一行或一列

第 60 天不要争论"先补哪一格最优"。用尴尬测试：把当前 `AGENTS.md`、CI、仪表盘或评审流程拿给同事看，哪一项最让你不好意思，就补哪一行或哪一列。

常见选择：

- 智能体总是乱改架构：补完整 SDD 行。
- 测试经常被跳过：补完整护栏列。
- 账单、性能、返工没人看：补完整 MDD 行。

### Day 90 · 第一次生产级 HarnessCard 评审

第 90 天不要只问"我们多了哪些文件"。问三句话：

- 上季度马具拒绝了什么？
- 上季度马具度量了什么？
- 上季度马具让哪一次工程决策改变了方向？

三问都答得出，才说明这具马具在工作。答不出，就说明它还只是制品集合，不是运行中的工程系统。

## F.2 每章行动页

| 章节 | 今天能做什么 | 本周能做什么 | 做成的信号 |
|---|---|---|---|
| 第 02 章 · 四阶段演进 | 给当前仓库标注它主要停在哪一阶段：Prompt、Context、Skill 还是 Harness。 | 找一个阶段跃迁：把一条 prompt 变成 skill，或把一条 skill 变成 hook。 | 同一类任务的返工次数下降。 |
| 第 03 章 · 定义 | 写下本仓库的最小三件套草稿：`AGENTS.md`、pre-commit、HarnessCard。 | 把其中一条规则接到真实命令。 | 至少一次 commit 被正确拒绝。 |
| 第 04 章 · 三大护法 | 选一个最弱护法：SDD、TDD、MDD。 | 给该护法交付一件最小制品。 | 团队能说清这件制品保证了什么属性。 |
| 第 05 章 · 矩阵 | 给 12 格各打 0–5 分，不争论，先填证据。 | 挑最低一格，合入一件制品。 | HarnessCard 有一格提升，且有文件证据。 |
| 第 06 章 · 运行 | 指定一位 Groom owner。 | 安排一次 30 分钟熵审计。 | 有一条过期规则、坏链接或无主仪表盘被处理。 |
| 第 07 章 · OpenHarness | 对照 OpenHarness 的工具边界，列出本仓库智能体可用工具。 | 给高风险工具加审批或沙箱边界。 | 高风险工具调用有日志和 owner。 |
| 第 08 章 · Superpowers | 找一条重复三次以上的工作流。 | 把它写成 skill 或命令清单。 | 智能体不再靠口头 prompt 记流程。 |
| 第 09 章 · lazy-scrum-team | 给关键制品加状态：draft、review、approved、archived。 | 定义谁能批准、谁能退回、退回时附带什么证据。 | 返工不再沉默发生。 |
| 第 10 章 · Claude Code | 清点 hooks、skills、MCP、权限弹窗。 | 把客户端特有配置指回 `AGENTS.md` canonical 入口。 | 客户端配置不再互相复制散文。 |
| 第 11 章 · 自审计 | 用附录 D 给自己的仓库打一张 HarnessCard。 | 合入一个能复现的修复。 | 修复前后有 delta，而不是只有叙述。 |
| 第 12 章 · 30/60/90 | 选一格。 | 给这格安排 owner 和复盘节奏。 | 30 天后它仍然活着。 |

## F.3 五条迁移路径

### 已有 `CLAUDE.md`

不要把 `CLAUDE.md` 和 `AGENTS.md` 维护成两份长文。把项目事实、命令、边界、danger zones 收进 `AGENTS.md`；`CLAUDE.md` 只保留 Claude Code 特有说明，或作为 symlink / 薄镜像指回 `AGENTS.md`。

完成标准：两份文件没有互相矛盾的规则；修改命令或目录边界时，只需要更新一处。

### 已有 `.cursor/rules`

把 `.cursor/rules` 看作客户端窄规则，而不是项目总规约。项目级规则进 `AGENTS.md`；Cursor 专属的 UI、索引、编辑器行为留在 `.cursor/rules`。

完成标准：换成 Codex、Claude Code 或其他 agent client 时，仍能从 `AGENTS.md` 读到项目主规则。

### 已有 CI

CI 是牧场，不等于护栏。把最常见、最便宜、最应该提前失败的检查前移到 pre-commit 或 tool hook：格式、快速单测、schema、密钥扫描。

完成标准：至少一种错误不再等到 PR 才被发现。

### 已有文档站

不是所有文档都该进马具。新员工 onboarding、长篇背景说明仍然是文档；智能体每轮必须遵守的边界、命令和 danger zones 才属于 `AGENTS.md`。

完成标准：`AGENTS.md` 像机场标识，只指路和设边界；深文档用链接引用，不复制。

### 已有 dashboard

先不要新增第十三块面板。挑一条会改变工程决策的北极星指标，例如 turns-to-green、每周被拒绝次数、成本上限触发次数、规约漂移数。

完成标准：周会里有人根据这条指标改变了下一步行动。

## F.4 四组好坏例子

### `AGENTS.md`

坏：

```markdown
请写高质量代码，遵循最佳实践，保持简洁。
```

好：

```markdown
Before editing `todo/storage.py`, run `pytest tests/test_storage.py`.
Do not edit `deploy/` or `.env*` unless the task explicitly asks for it.
Every new CLI command gets a `--help` string and `tests/test_<cmd>.py`.
```

差别：坏例子要求态度，好例子声明边界和命令。

### pre-commit

坏：

```yaml
- id: pytest
  entry: pytest
  args: ["tests/"]
  pass_filenames: false
```

如果 `tests/` 为空，它会永远通过。

好：

```yaml
- id: fast-tests
  entry: pytest -q -m "not slow"
  language: system
  pass_filenames: false
```

再配一条初始化检查：安装当天必须证明它能拒绝一个真实坏例子。

### dashboard

坏：

```text
Agent Dashboard: token count, request count, latency, cache hit, errors, cost...
```

好：

```text
North Star: mean agent turns-to-green on the fixed benchmark.
Owner: MDD owner.
Review cadence: Mondays, 10:00.
Action threshold: +20% week over week opens a Groom ticket.
```

差别：坏例子展示数据，好例子改变行为。

### PR 验收

坏：

```text
LGTM. Tests pass.
```

好：

```markdown
| Check | Evidence | Owner |
|---|---|---|
| `AGENTS.md` unchanged or versioned | diff link | Architect |
| Fast tests pass | CI link | Developer |
| New behavior has acceptance case | test path | Reviewer |
```

差别：坏例子给感觉，好例子给证据和角色。

## F.5 按角色落地

| 角色 | 应该拥有的东西 | 每周要问的问题 |
|---|---|---|
| 一线工程师 | 一条本地可跑的护栏。 | 我今天有没有把一个反复出现的问题变成命令或测试？ |
| Tech Lead | `AGENTS.md` 和架构 danger zones。 | 智能体最近一次越界，是规约没写清，还是护栏没接上？ |
| Reviewer | 验收表和 hard / soft gate 分类。 | 这次 review 是靠记忆，还是靠可复用制品？ |
| EM / TL | HarnessCard 与季度节奏。 | 分数提升有没有对应产出指标？ |
| Oncall | 事故回灌到 Groom 的路径。 | 这次事故有没有产生一条新规则、新测试或新信号？ |

## F.6 第一次落地会议议程

时间盒：45 分钟。

1. 5 分钟：读第 03 章一句话定义。
2. 10 分钟：给当前仓库 12 格打初分，只填证据，不辩论。
3. 10 分钟：找最低分的两格，选更尴尬的一格。
4. 10 分钟：定义一件 30 天内能合入的制品。
5. 5 分钟：指定 owner。
6. 5 分钟：写下成功信号，必须是"被拒绝、被度量、或改变决策"中的一种。

会议结束时只需要产出一张卡片：

```markdown
Cell: SDD × Bridle
Artefact: AGENTS.md
Owner: <name>
First gate: listed test command must exist
Success signal: one incorrect edit is prevented or redirected within 30 days
Review date: <date>
```

这张卡片比十页战略文档更有用。它小、可合并、可复盘，也会迫使团队把 Harness Engineering 从概念变成工作。
