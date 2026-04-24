---
status: draft
chapter-type: case-study
case-study-kind: open-source
---

# 案例研究：lazy-scrum-team —— 用工作流编码出来的马具

> *多数团队有角色。少数团队在角色之间有契约。更少数的团队，有能让这些契约被机器读懂的制品。*

`lazy-scrum-team` {cite}`lazyscrumteam2026` 是一份兼容 Claude Code／Cursor 的技能包，把一整套受 Scrum 启发的角色班底编码成了可执行的工作流。与 OpenHarness（一套运行时）和 Superpowers（一座技能库）不同，`lazy-scrum-team` 把 *工作流本身* 当作马具——角色、角色之间的交接、以及沿着这些交接传递的返工制品。本章是本书对第 06 章只点到却未展开的三种模式——制品状态机、返工矩阵、硬关卡 vs 软关卡分类——的正式处理。

## 09.1 —— 角色班底

这套技能自带七个显式角色；每个角色配一段契约、以及一组它署名持有的制品。

```{list-table}
:header-rows: 1
:widths: 20 40 40

* - 角色
  - 持有
  - 不得
* - Product Owner（PO）
  - `specs/*.md`，backlog 的排序
  - 写生产代码；审批 PR
* - Architect（架构师）
  - ADR、模块边界、类似 `storage.rs` 那样的关卡文件
  - 在功能意图上凌驾于 PO
* - Scrum Master
  - sprint 节奏、状态机的完整性
  - 写或审查代码
* - Developer（开发）
  - 功能代码 ＋ 单元测试
  - 自行合并
* - Code Reviewer（评审人）
  - 硬关卡清单、PR 批准
  - 自审自批；审自己的代码
* - Test Engineer（测试工程师）
  - 验收测试、覆盖率下限
  - 批准 PR
* - Final Acceptance（终审）
  - 发布 PR ＋ HarnessCard delta
  - 自己亲自做评审
```

Scrum {cite}`schwaber2020scrum` 提供了这份角色词汇表；这个技能的创新并不在于角色本身，而在于角色 *之间* 发生了什么。Conway 律 {cite}`conway1968law` 提醒我们：沟通结构会渗进制品结构；这个技能把这件事当作特性而不是缺陷——那些交接制品 *本身* 就是沟通通道。

## 09.2 —— 模式一 —— 制品状态机

马具中每一份可评审制品都恰好有四种状态——`draft → review → approved → archived`——且跃迁被严格约束。权威编码以 YAML 文件交付，任何 ticket 系统都能导入：

```{literalinclude} ../_handson/09-lazy-scrum-team/state-transitions.yaml
:language: yaml
```

有两条不变量，让这个状态机成为承重的、而非装饰性的：只有 Final Acceptance 能翻转 `review → approved`；已被批准的制品，要回到 `draft`，必须先经过 `archived`。这两条不变量合在一起，消除了评审流程里最常见的那种失败模式——*沉默返工*——因为任何对"已批准制品"的回退，都会显式地表现为一次 reopen 事件。

(ch09-rework-matrix)=
## 09.3 —— 模式二 —— 返工矩阵

返工矩阵针对每一对"发现者 × 修复者"，命名了必须随附这次交接的那件具体制品。把 PR 作为工作流的研究 {cite}`gousios2014pullbased`，以及经典的 specification-by-example 文献 {cite}`adzic2011specbyexample`，都主张"机器可读的交接"；返工矩阵是本书对此的一份带倾向的编码。

```{literalinclude} ../_handson/09-lazy-scrum-team/rework-matrix.md
:language: markdown
```

具体地说：当 Test Engineer 驳回一位 Developer 的 PR，驳回意见以一份 `bug-report.md` 的形式落到 PR body 里，而不是变成一条 Slack 消息。当 PO 驳回 Architect 的 ADR，驳回意见以一份 `spec-delta.md` 的形式落到 `docs/rework/<sprint>/` 下。*署名的那份文件* 就是契约；"赶紧修一下"式的评论，等于组织级失忆。

## 09.4 —— 模式三 —— 硬关卡 vs 软关卡

马具中每一道关卡，都必须在创建时声明自己的类别：**硬关卡** 永不可豁免；**软关卡** 可由署名角色带到期日豁免。这份分类被原样复刻进第 06 章的 hands-on 目录；权威表格为：

| 关卡 | 类别 | 豁免规则 |
|---------------------|-------|---------------------------------------------------|
| 单元测试套件 | 硬 | 永不豁免；要么修，要么 revert |
| lint | 硬 | 对新代码永不豁免 |
| 覆盖率下限 | 软 | Architect 附理由；最多 7 天 |
| 成本上限 | 软 | MDD Owner；最多 24 小时 |
| 密钥扫描 | 硬 | 永不豁免；把密钥轮换掉 |
| 文档 link-check | 软 | 任一评审人；最多持续到下一次每周 groom          |

Humble 与 Farley 的 *Continuous Delivery* 谱系 {cite}`humble2010continuousdelivery`，提供了硬关卡的语法；DORA 度量文献 {cite}`forsgren2018accelerate` 说明了为什么"软关卡豁免数／硬关卡通过数"这一比值，本身就是一条健康信号。

## 09.5 —— 十二格亮点图

```{list-table}
:header-rows: 1
:widths: 20 8 72

* - 格子
  - 得分
  - 证据
* - SDD × 缰绳
  - 4
  - `roles/*.md` 是显式的、智能体可读的角色契约。
* - SDD × 护栏
  - 4
  - 状态机的不变量，拒绝形态不合法的跃迁。
* - SDD × 牧场
  - 5
  - 验证表 ＋ 验收评审，就是 SDD 牧场的经典形态。
* - SDD × 梳理
  - 3
  - sprint 回顾会会反过来更新技能；节奏因团队而异。
* - TDD × 缰绳
  - 3
  - Test Engineer 这个角色塑造上下文，但没有 starter 测试被先行提交。
* - TDD × 护栏
  - 4
  - 硬关卡策略拒绝红色测试树下的合并。
* - TDD × 牧场
  - 4
  - 验收评审把测试结果绑回到规约上。
* - TDD × 梳理
  - 3
  - flaky 测试策略是隐含的；没有显式命名隔离区。
* - MDD × 缰绳
  - 2
  - 在技能层面没有定义北极星度量。
* - MDD × 护栏
  - 2
  - 不自带成本上限；交给宿主平台处理。
* - MDD × 牧场
  - 2
  - SLI 关卡不在范围内。
* - MDD × 梳理
  - 2
  - 每周审计已定义，但未由技能自动化。
```

最强的一行：**SDD**（均值 4）。最强的一列：**牧场**（均值 3.25）。最弱的一行：**MDD**（均值 2）。这个分布与一具"为审批纪律优化、而非为运行时可观测性优化"的工作流式马具完全一致。

### 把工作流当马具，哪里脆弱

lazy-scrum-team 的那些模式，是本书 SDD × 牧场 的经典范例；但不加批判地读进去，会踩两个结构性的坑。

- **角色漂移的速度，比编码它们的那些文件更快。** 09.1 里那七份角色契约，默认团队是按这七项职能组织的。多数团队并不是——一位独立创始人在一个下午里同时是 PO、Architect、Developer、Code Reviewer；一支五人创业团队会把 Test Engineer 与 Developer 合成一个。若一具工作流马具预设了团队并不具备的角色班底，则每一次交接都会生出摩擦，因为返工矩阵要求的那件制品压根没有天然作者。**解法**：拷 *模式*（署名的返工制品、显式的交接契约），但把它映射到你团队 *实际拥有* 的角色上，哪怕这意味着四份契约而不是七份。Conway 律 {cite}`conway1968law` 两头都砍——工作流必须匹配真实存在的沟通结构，而不是模板假设的那种结构。
- **状态机剧场。** 那四个状态（`draft → review → approved → archived`），只有在跃迁被机械化强制执行时才承重。若一支团队写了 YAML 却把跃迁留给"谁记得就去更新 ticket"，那什么也得不到：一份"在所有人心里已悄悄退回 draft、在 tracker 里还挂着 approved"的制品，比完全没有状态机更糟——它把这套流程的成本全占了，却一份杠杆也没拿到。

```{admonition} 陷阱——工作流却没有工具
:class: warning

一支团队用散文把七份角色契约、返工矩阵、状态机全采纳了。采纳情况前六周看上去很好。然后周五晚上来一场事故——一个 hotfix PR 被 Developer 自行合并——没有 Code Reviewer、没有 Final Acceptance、状态跃迁也没记录。没人报警，因为那些规则只作为"期望"存在。**为什么**：散文工作流是一种规范；规范在压力下，会在第一次事故时就屈服。**解法**：至少把两条承重跃迁接进工具——分支保护拒绝自合并是底线；CODEOWNERS 文件要求正确角色来批准，更好。任何没有被机械化强制执行的规则，都会在第一次糟糕的星期五被暂停。
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
  - lazy-scrum-team 技能，2026-04 快照 {cite}`lazyscrumteam2026`
* - 许可证
  - MIT
* - Control 层（CAR）
  - 通过角色契约和状态机，持有强烈主张。
* - Agency 层（CAR）
  - 交由宿主平台处理（Claude Code／Cursor）。
* - Runtime 层（CAR）
  - 无；这个技能只是散文 ＋ YAML。
* - SDD（均值）
  - 4.0
* - TDD（均值）
  - 3.5
* - MDD（均值）
  - 2.0
* - 主要引用
  - {cite}`lazyscrumteam2026`
```

## 研究脉络

- **Scrum** {cite}`schwaber2020scrum` —— 这份角色词汇的谱系；这个技能用"显式交接契约"把它扩展。
- **Specification by Example** {cite}`adzic2011specbyexample` —— 验证表模式背后的"可执行规约"谱系。
- **Conway 律** {cite}`conway1968law` —— 为什么角色结构 *必须* 被编码到制品结构里。
- **把 PR 当工作流** {cite}`gousios2014pullbased` —— "把 PR body 当作一等规约面"的经验基础。
- **DORA ／ Accelerate** {cite}`forsgren2018accelerate` —— 用来度量"这套关卡纪律到底有没有在起作用"的度量谱系。

## 动手环节

在 `source/_handson/09-lazy-scrum-team/` 下，住着五份可直接拷走的制品：

- `roles/po.md`、`roles/code-review.md`、`roles/acceptance-review.md` —— 带出处署名的角色契约节选。
- `state-transitions.yaml` —— 可改写的状态机。
- `rework-matrix.md` —— 带署名返工制品的"发现者 × 修复者"矩阵。

想采用这三种模式却 *不想* 采用整个技能的读者，可以把这五份文件拷走、定制角色班底，并在午饭之前就拥有一具能工作的工作流马具。
