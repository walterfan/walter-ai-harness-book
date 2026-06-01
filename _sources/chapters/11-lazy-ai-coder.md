---
status: draft
chapter-type: case-study
case-study-kind: open-source
worked-example: true
---

# 案例研究：Lazy AI Coder —— 一则四幕剧形式的实证示例

> *若这套框架连"给本书所承载的仓库打分、再改进它"这件事都做不了，那这框架就是错的。*

到目前为止，每一篇案例研究都 *关于* 别人的马具。本章不同：它把"三大护法 × 四区域"矩阵，套到本书所承载的那个仓库——[`walterfan/async-harness-book`](https://github.com/walterfan/async-harness-book)——上，并把真正的修复合入 `main`。本章以四幕剧的形式展开。

```{note}
**状态。** 本章会保持 `status: draft`，直到第三幕列出的修复 commit
合入宿主仓库的 `main` 分支。book-lint 脚本会用 `git cat-file -e`
遍历第三幕的 commit SHA；在至少两笔解析成功之前，本章仍应被视为一份
待验证案例。
```

## 第一幕 —— 审计

起点是一份 HarnessCard，记录仓库在这一轮变更开始那笔 commit 时的状态。每一格的证据都是仓库内一条具体的文件路径；完整打分表以 hands-on 制品形式交付，读者可与之做 diff。

```{literalinclude} ../_handson/11-lazy-ai-coder/HarnessCard-Act1.md
:language: markdown
```

这份审计稳稳地落在矩阵的左下角：SDD × 护栏、SDD × 梳理、TDD × 护栏、以及 MDD × 缰绳／梳理，是五个最弱的格子。Cunningham 1992 年的"技术债"隐喻 {cite}`cunningham1992debt`，以及 Feathers 的 *Working Effectively with Legacy Code* {cite}`feathers2004legacy`，提供了解释"为什么这很重要"的词汇：这不是一份 *糟糕的* 仓库，而是一份 *其马具累积了普通可生存之债* 的仓库——任其发展就会复利恶化。Lehman 的演化定律 {cite}`lehman1980laws` 预言的正是这个模式。

## 第二幕 —— 缺陷

五项具体缺陷——每一项都附有严重度、证据指针、以及它映射到的矩阵坐标：

1. **缺少 `make prompts-lint`。** `config/prompts.yaml` 未经 schema 校验就被提交；格式被破坏的模板只能在运行时才被发现。（**SDD × 护栏**，`major`；证据 `config/prompts.yaml`。）
2. **MCP 工具 schema 未与其 handler 做一致性校验。** 新加了一个 handler 却没有 schema（反之亦然）——CI 照样绿灯放行。（**TDD × 护栏**，`major`；证据 `internal/mcp/server.go`、`internal/mcp/handlers.go`。）
3. **LLM 调用没有成本可观测面板。** 月度花销在供应商账单到来之前完全不可见。（**MDD × 缰绳**，`major`；证据是 `deploy/` 下没有任何面板配置。）
4. **`CLAUDE.md` 与 `AGENTS.md` 已与 `openspec/` 工作笔记漂移。** 这两份"门面文档"引用了已经不存在的概念，却没有引用现在已经存在的概念。（**SDD × 梳理**，`minor`；证据 `CLAUDE.md`、`AGENTS.md`、`openspec/`。）
5. **没有 pre-commit 钩子来拦住"被提交进来的密钥"。** `.env` 文件已被 gitignore 忽略，但作为安全网的钩子层整个缺席。（**TDD × 护栏** 与 **MDD × 缰绳** 联合，`critical`；证据：仓库根目录不存在 `.pre-commit-config.yaml`。）

Adzic 的 *Specification by Example* {cite}`adzic2011specbyexample` 与 DORA 度量 {cite}`forsgren2018accelerate`，框定了补救工作的方向：每一项缺陷，都要被转化为一道可执行关卡——它的存在或缺席，本身就成为一条被度量的指标。

## 第三幕 —— 把马具工程真正落下去

四项修复合入 `main`，每一项都收束到单一矩阵格子上，并以 commit SHA 为引用。下文的 SHA 槽位会在后续修复合入时填入；book-lint 脚本在每次构建时都会用 `git cat-file -e` 遍历它们。

```{list-table}
:header-rows: 1
:widths: 28 26 16 30

* - 修复
  - 格子
  - 严重度
  - Commit SHA
* - `make prompts-lint` ＋ `scripts/prompts_lint.py`
  - SDD × 护栏
  - major
  - `<待填 SHA>`（修复 1）
* - MCP 工具的 "schema vs handler" 一致性检查
  - TDD × 护栏
  - major
  - `<待填 SHA>`（修复 2）
* - `openspec/docs/sources-of-truth.md` 索引，用以调和 `CLAUDE.md` ＋ `AGENTS.md`
  - SDD × 梳理
  - minor
  - `<待填 SHA>`（修复 3）
* - 带 gitleaks ＋ `make secrets-check` 的 `.pre-commit-config.yaml` 基线
  - TDD × 护栏 联合 MDD × 缰绳
  - critical
  - `<待填 SHA>`（修复 4）
```

每一份 PR 的描述里，都按名引用本章（`book — Ch.11 Act 3`），并附上一行 *HarnessCard delta* 说明：哪一格的分数在动、动了多少。

## 第四幕 —— 丈量增量

在第三幕的 commit 合入之后，写出第二份 HarnessCard，把格子得分与第一幕做 diff，并报告量化增量：

```{literalinclude} ../_handson/11-lazy-ai-coder/HarnessCard-Act4.md
:language: markdown
```

本章契约 *要求* 至少两条量化指标；hands-on 版的 HarnessCard 报告了四条：

- **prompts-lint 规则条数**：0 → 7。
- **CI 上的 MCP schema 不一致数**：N/A → 0（全新检查）。
- **secrets 扫描覆盖率（已提交文件占比，%）**：0 → 100。
- **`sources-of-truth.md` 条目数**：0 → ≥ 6。

HarnessCard 总均值从 1.75 升到 2.42 —— +0.67 的改善集中落在两个"护栏"格（各 +3）和 SDD × 梳理（+2）上。第四幕刻意不动 MDD 那一行；第 12 章的 30/60/90 计划会在下一个季度接手。

### 这个 delta *不能* 证明什么

第三幕的四个 commit，把 HarnessCard 均值抬升了 0.67。这是一个真实的数字，也是一个 *有边界* 的数字——在把它当作"马具在起作用"的证据去引用之前，值得先仔细读清楚。

- **这个 delta 度量的是投入，不是产出。** 格子得分上升，意味着仓库里多了一批"评分尺会给分"的制品；它还不等于智能体的输出变好了。DORA 风格的产出指标（部署频率、变更失败率、平均恢复时间），才是"投入有所回报"的证据——第 12 章的 90 天复盘，才是期望这些产出真正移动的时点，而不是第四幕的这张快照。
- **打分人与作者是同一个人。** 第一幕的基线与第四幕的重评，都由同一位工程师执笔，用同一把评分尺，且对"改了什么"心知肚明。这对于"自审计"来说是诚实的，但不是独立验证——这些分数是校准，不是度量。读者在自己仓库上复制这套模式时，应预期自己也会有类似偏置。
- **四项修复里有三项是"护栏"形的。** 护栏格最容易抬分——因为"拒绝"是机械且可测的。缰绳格和牧场格抬得更慢——因为它们需要改变人和智能体所 *做* 的事，不是仅仅改变 CI 拒绝什么。一份 HarnessCard 的均值主要由"护栏收益"主导，在第一个季度里是一种诚实的模式；但一份 *连续四个季度* 其 delta *只有* 护栏的 HarnessCard，则是一支"只投资于拒绝、却未抬升意图与验收"的团队的画像。

```{admonition} 陷阱 —— HarnessCard 虚荣增量
:class: warning

一支团队跑完第 11 章的 playbook，合入了四个"护栏"commit，向上汇报 +0.67 的均值 delta。领导很满意。两个季度之后，产出指标一动未动；这个团队于是加码，又合入四个"护栏"commit；均值再次上升。马具在长胖；产出没在长。**为什么**：HarnessCard 是一份 *诊断* —— 它的角色是"识别弱格"，不是"被优化的对象"。一支为"分数"而非"产出"优化的团队，在跑的是 Goodhart 律的一个变种（Cunningham 的债务隐喻 {cite}`cunningham1992debt` 反着用一次：你 *确实* 可以去还一笔本来根本没在收利息的债）。**症状**：格子得分在涨，仪表盘没在涨；回顾会上对"马具工作"描述得温情脉脉，事故复盘里对"产品工作"描述得痛不欲生。**解法**：每一项 HarnessCard delta 都要配一项它 *被预言会移动* 的产出指标。若一个季度后该产出未移动，则这份 delta 属于虚荣；下一季度的投资应该换到另一格（或彻底换一个维度）。
```

## 阅读单扩展

第四幕的可复现性主张，建立在一段简短 shell 脚本之上——它针对"第四幕 SHA"处的一份全新 clone，跑三个新的 make 目标：

```{literalinclude} ../_handson/11-lazy-ai-coder/reproduce.sh
:language: bash
```

第四项修复里的 `pre-commit-config.yaml` 基线，也一并交付，方便想原样拿走的读者：

```{literalinclude} ../_handson/11-lazy-ai-coder/pre-commit-config.yaml
:language: yaml
```

## 研究脉络

- **技术债** {cite}`cunningham1992debt` —— 第一幕的词汇来源。
- **遗留代码** {cite}`feathers2004legacy` —— 第二幕的补救模式。
- **DORA ／ Accelerate** {cite}`forsgren2018accelerate` —— 第四幕所依据的度量谱系。
- **演化定律** {cite}`lehman1980laws` —— 为什么一旦停止"梳理"投资，总均值就会持续漂移。

## 动手环节

在 `source/_handson/11-lazy-ai-coder/` 下，住着四份可直接拷走的制品：

- `HarnessCard-Act1.md` —— 修复前的基线。
- `HarnessCard-Act4.md` —— 修复后的再审计，含 delta。
- `reproduce.sh` —— 三个 `make` 目标，一段脚本。
- `pre-commit-config.yaml` —— 最终基线的 symlink-safe 拷贝。

当第三幕那批 commit 合入 `main`，HarnessCard 将针对真实 SHA 重新打分，本章状态也会翻为 `status: complete`。
