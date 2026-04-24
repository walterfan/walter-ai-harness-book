---
status: draft
chapter-type: presentation
---

# Slides 大纲

```{admonition} 使用方式
:class: tip

本文件是 **每页一张 slide 的大纲** —— 每一个 `##` 对应一张 slide。

- **bullet** 是片上文字（精简，不超过 5 行；每行原则上不超过 10 个汉字）。
- **引用块** `>` 是 speaker notes（讲稿备注），不上屏。
- 可以直接复制到 Keynote / Google Slides / PowerPoint 的 Outline 视图
  一次性导入，也可以用 [slidev](https://sli.dev/) 或 [Marp](https://marp.app/)
  渲染。
- 如果你想直接拿一份 **排好版的 Marp 幻灯片**，见
  `../_handson/13-one-hour-talk/SLIDES.md`；本文件是它的来源大纲。

一共 **~30 张 slide**（开场 / 结尾各 1 张 + 8 段内容 × 2–4 张 + F.2 穿插 2 张）。
排练时如果某张停留超 3 分钟，说明那张内容太多，需要拆或砍。

**术语约定**：`AGENTS.md / CLAUDE.md 兼容层 / SKILL.md / MCP / pre-commit /
Bridle / Fence / Paddock / Groom / SDD / TDD / MDD / HarnessCard`
不翻译。
```

---

## Slide 1 —— 标题页

- Harnessing AI —— 给 AI 套上缰绳
- 一小时部门内部分享
- Walter Fan · 2026

> 开场不要急着讲话。让标题停 10 秒。报家门 1 句。
> 承诺 —— *"我今天只讲主脊，不陷细节；最后留 4 分钟给 Q&A。"*

---

## Slide 2 —— 议程

- 8 段 × 约 7 分钟 + Q&A 4 分钟
- F.0 开场 → F.8 收尾
- 每段都有 **一张白板 + 一句中心论点 + 回书锚点**

> 15 秒。不念完整张表。只说 —— *"我会走 8 段，每段 7 分钟；
> 最后留 4 分钟 Q&A。整场没有问答环节 —— 所有问题都请憋到最后
> 一次性问。"*

---

## Slide 3 —— F.0 开场：Model → Environment

- M → E
- 杠杆点移动了
- 过去：调模型；现在：造环境

> 在白板左边写大写 "M"，右边写大写 "E"。
> 画箭头 **2022–2024: M ← 调得更听话** / **2026: E ← 建得让模型干不坏事**。
> 说 —— *"过去我们想着怎么把模型调得更听话；现在我们想着怎么把
> 环境建得让一个普通模型也干不坏事。"*

---

## Slide 4 —— F.0 · 三条 2026 年的事实

- OpenAI Codex：8 周 100 万行生产代码，0 行人手写
- LangChain：不换模型，改脚手架，Terminal Bench 2.0 进前 5
- Anthropic：权限 / 技能 / MCP 的工程时间 > 模型权重

> 每条 15 秒，一共 45 秒。念完之后加一句 ——
> *"三件事的共性是 —— 他们变的都不是模型，是模型周围的东西。"*

---

## Slide 5 —— F.1 · 四阶段演化

- 2022–2024 · **Prompt** · 怎么问？
- 2025 · **Context** · 给看什么？
- 2025–2026 · **Skill** · 怎么把流程写下来？
- 2026– · **Harness** · 造什么环境？

> 画时间轴时故意停在 **Skill** 这一格，问一句 *"那 2026 以后呢？"*
> 让听众接 "Harness"（大概率有人接得上）。

---

## Slide 6 —— F.1 · 每阶段的主要制品

- Prompt：一条巧妙的提示字符串
- Context：一张检索图
- Skill：`SKILL.md` / command
- Harness：**仓库本身** —— `AGENTS.md` + 护栏 + 钩子 + 巡检

> 强调 **"仓库本身"** —— 这是 Harness 和前三阶段最大的分野。
> 前三阶段可以一个工程师单独做；Harness 必须以仓库为单位做。

---

## Slide 7 —— F.1 · 两句带走

1. 前三阶段调"询问层"，Harness 把干预点移到"环境层"
2. 前三阶段个人做，Harness **以仓库为单位**做

> 放慢念。这两句是 F.1 的全部。
> 如果超时，可以把前面的 Slide 6 砍掉，直接从 Slide 5 跳到这里。

---

## Slide 8 —— F.2 · 一句话定义

- Harness Engineering =
- **刻意设计、运行、演化**
- AI 编码智能体**周围的结构**
- 目的：让产出 **可验证 / 可观测 / 可理解**

> 可验证 / 可观测 / 可理解三词竖着写在白板左栏，停 3 秒再说 ——
> *"这三词不是修辞。每一个背后都有一门四十年历史的工程学科。"*

---

## Slide 9 —— F.2 · 是 × 5

1. 面向智能体的规约（`AGENTS.md`/`CLAUDE.md` 兼容层/`SKILL.md`/MCP manifest）
2. 审批门与护栏（pre-commit / lint / PR review / CI）
3. 沙箱（容器 / VM / 只读挂载 / 临时 worktree）
4. 面向智能体的文档（runbook / ADR / skill）
5. 度量与反馈面（成本 / 违规数 / turns-to-green）

> **快念**。每条 10 秒。重点不在记住每条，而在听众形成
> *"原来 harness 的范围是这些东西"* 的整体印象。

---

## Slide 10 —— F.2 · 不是 × 5

- **不是** 推理运行栈（AI Engineering）
- **不是** ML 评测基准
- **不是** IDE 插件（Cursor / Copilot 是客户端）
- **不是** Agent 框架 SDK（LangChain / AutoGen）
- **不是** 部署流水线（DevOps）

> 比"是"还要快。每条 8 秒。
> 关键在于收尾那句 **归属检验** ——
> *"commit 之前 = harness；commit 之后 = DevOps。"*

---

## Slide 11 —— F.2 · PDCA × 防跑偏

- P：**规约** · D：**人 + AI 写** · C：**测 / lint / CI** · A：**Groom + 恢复**
- **规则**：可执行条文（路径 / 成本 / hook）
- **校验**：合入前客观信号
- **恢复**：revert / 绿色 commit 重启上下文

> 画 `P→D→C→A` 小环，D 格里写 tiny「AI」。金句 —— *"D 很快、C 很慢必跑偏。"*
> 与 `index.md` F.2 穿插段同文；**可砍**省进 F.3。

---

## Slide 12 —— F.2 · Agent Loop（驯服把手）

- 用户输入 → context → decision → tools → observation
- memory / skill / controller 让 loop 持续
- 跑偏时：看 trace，不看态度
- Harness 接在输入、context、tools、loop、输出证据上
- **少即是多**：收敛方向、立规矩、progressive disclosure

> 只画一圈，不展开系统图。强调 —— *"Harness 决定 agent 在什么制度下写你的代码。"*
> 细节指到第 03B 章，现场不要陷进 memory 实现。补一句 —— *"不要把整座图书馆塞进 context，LLM 已经知道很多；你要给它边界和判据。"*
> 下一张接 F.3 因果翻转。

---

## Slide 13 —— F.3 · 因果顺序反转

```
传统：  test   →  implement  →  observe
AI：    specify → test       →  observe
```

- 人写代码：测试是第一份规约
- 智能体写代码：**规约前置**，测试抓幻觉
- 不是推翻传统工程，是让老原则重新发光

> 画完后停 5 秒不说话，让听众自己读出 *"咦，SDD 顶到最前面去了"*。
> 然后说 —— *"为什么翻转？因为人写的主要制品从代码移到了规约。小步提交、测试先行、可回滚、可追踪，在 agent 时代更值钱。"*

---

## Slide 14 —— F.3 · 三护法

- **SDD** · Specification-Driven · 说 · 可理解
- **TDD** · Test-Driven · 证 · 可验证
- **MDD** · Metric-Driven · 观 · 可观测

> 三个单词 + 三个动词 + 三个形容词。**念完即走**。
> 一个要提防的误读：*"我们已经有 CI 了啊。"* —— 回一句：
> *"CI 是 TDD/MDD 的牧场；harness 在键盘按下那一刻就发声。"*

---

## Slide 15 —— F.4 · 3 × 4 矩阵（全屏）

```
          Bridle    Fence      Paddock     Groom
          写前      写时        写后        维护

SDD (说)  AGENTS    lint       gate        索引
TDD (证)  pre-edit  pre-commit CI          flaky 隔离
MDD (观)  北极星    成本上限    SLI         指标轮替
```

> **本场最重要的一张 slide**。不要用动画 —— 一上来就全显示。
> 讲稿停在这里 4 分钟：4 列各 30 秒 + 3 行各 30 秒 + 收尾 30 秒。
> 收尾那句：*"这张表是剩下 30 分钟的地图。"*

---

## Slide 16 —— F.4 · 四区域各一句

- **Bridle（缰绳）** 敲第一个键之前 *看什么、听什么*
- **Fence（护栏）** 不管作者是谁，*一律拒绝* 坏制品
- **Paddock（牧场）** *可以撒欢的那块地* 的边界
- **Groom（梳理）** 维护 *马具本身* 的重复性工作

> 如果 Slide 13 时间用完了，这张可以砍。否则 1 分钟讲完。
> 强调 Groom —— *"没有 Groom 的马具，是装饰。"*

---

## Slide 17 —— F.5 · 四个案例横轴

```
OpenHarness  Superpowers  lazy-scrum-team  Claude Code
运行时+沙箱   技能库       工作流编码        闭源产品
(第 07 章)   (第 08 章)   (第 09 章)       (第 10 章)
```

- 同一张矩阵，落在四种形态的项目上

> 画完后问一句 —— *"大家手里这个 repo，更像左边还是右边？"*
> 停两秒再继续。

---

## Slide 18 —— F.5 · 每案一句

- **OpenHarness** —— 唯一"读过第 05 章才写的"开源参考实现
- **Superpowers** —— 哲学反面：只出技能不出运行时
- **lazy-scrum-team** —— 把 Scrum 角色与交接当马具
- **Claude Code** —— 闭源；职责分布在 prompt+hooks+skills 三处

> 每个 60 秒。重点是让听众 **识别** 自己项目最像哪个，不是评判哪个更好。
> 一句带走 —— *"矩阵是尺子，案例是刻度。挑最像你技术栈的那一个抄。"*

---

## Slide 19 —— F.6 · Lazy AI Coder 四幕

```
Act 1    Act 2        Act 3       Act 4
审计     短板         修复         度量 delta
Audit    Short-       Fixes        Measure
         comings
```

- 本书对自己的仓库做了一次实盘
- 矩阵 → 审计 → 修复 → 重打分

> 开场一句 —— *"如果这套框架连书自己的宿主仓库都打不分、改不动，
> 那它就是错的。"*

---

## Slide 20 —— F.6 · Act 4 的 delta

- SDD 均值 **1.75 → 3.00**（+1.25）
- TDD 均值 **2.00 → 2.75**（+0.75）
- MDD 均值 **1.50 → 1.50**（+0.00）
- **总分 1.75 → 2.42**（+0.67）

> 念 "1.75" 慢，念 "3.00" 快 —— 听众自己会算 delta。
> 提防 —— *"HarnessCard ≠ 虚荣分数。只要你公开评分尺、证据指针、
> delta，它就是分析工具不是虚荣。"*
> 说明 —— *"MDD 没动是故意的。90 天内先把 SDD 做到及格才配谈 MDD。"*

---

## Slide 21 —— F.7 · 三个里程碑

```
Day 1–30     Day 31–60        Day 61–90
一格         一行 或 一列      一次完整评审
```

- **不必一次做完 12 格**
- 挑一格 → 扩到行/列 → 公开打分

> 画完后直接问 —— *"如果我们部门只做 Day 30 这一步，
> 你会选 SDD × Bridle 还是 TDD × Fence？为什么？"*
> 这一问会让下一张 slide 的 Q&A 氛围自动热起来。

---

## Slide 22 —— F.7 · Day 30 三个推荐切入点

- **SDD × Bridle** —— 写一份 `AGENTS.md`
  （便宜，之后每一轮都赚）
- **TDD × Fence** —— 装一条 `PreToolUse` 钩子
  （测试红时拒写；单兵受益）
- **MDD × Fence** —— LLM 调用加会话成本上限
  （过线拒新调用）

> 三条都是"单兵 Day 1 就能上"的格。
> 团队通常从 SDD × Bridle 起步；单兵通常从 TDD × Fence 起步。

---

## Slide 23 —— F.7 · 三个要提防的陷阱

- **"Day 30 搞定了"陷阱** —— 无 Groom，90 天后分数回落
- **"Groom 以后再说"陷阱** —— 一开始就不放 Groom = 装饰
- **"凑齐了再发布"陷阱** —— 等 12 格 ≥ 3 再上线 = 永远不上

> 这张是 F.7 的收口。念完三条再放 Slide 22。
> 强调中间那条 —— *"没有 Groom 的马具，不是马具，是装饰。"*

---

## Slide 24 —— F.8 · 三句要被记住的话

1. Harness Engineering 不是加一层流程，是 **提取会机械拒绝坏工作的那一小撮制品**
2. **SDD → TDD → MDD**，顺序不能乱
3. 不做 12 格 —— **挑 1 格，30 天上线，90 天公开 HarnessCard**

> **逐字念**。这是全场信号量最高的一张 slide。
> 念完后停 3 秒，再开 Q&A mic。

---

## Slide 25 —— F.8 · 常见问 Q1

- Q：**跟 CI 流水线有什么区别？**
- A：CI 是 TDD / MDD 的 **牧场**
  - 合入那一刻发声
- Harness 在 **键盘按下那一刻** 发声

> 60–90 秒。如果听众追问 *"那我们把 CI 加个 pre-commit 不就行了？"* ——
> 回答 *"那就是 Fence。你已经在做 harness 了，只是还没意识到。"*

---

## Slide 26 —— F.8 · 常见问 Q2 + Q3

- Q：**三个护法一定要全上吗？**
  - A：不用。Day 30 一格就算进展
- Q：**这不就是 DevOps 重新包装？**
  - A：不是。**commit 前 = harness；commit 后 = DevOps**

> 每问 45 秒。不要展开。
> 如果听众继续追问 DevOps 边界，引到附录 A（FAQ）。

---

## Slide 27 —— F.8 · 收尾画面

- 只剩下 E
- 从今天起，**先从环境开始**
- *谁愿意做 Day 30 的那一格？*

> 把开场那张 M → E 图擦掉一半，只留 E。
> 最后一句是 **行动号召** —— 让分享会从"听讲"变成"行动"。
> 当场记下志愿者的名字。

---

## Slide 28 —— 资源链接

- 本书仓库：<https://github.com/walterfan/async-harness-book>
- 讲稿 / 大纲 / 幻灯片：`source/chapters/00-presentation/`
- Marp 版幻灯片：`_handson/13-one-hour-talk/SLIDES.md`
- 30/60/90 清单：`_handson/12-where-we-go-from-here/`
- HarnessCard 模板：附录 D · `CLAUDE.md` 兼容样板：附录 E
- Agent Loop 插章：第 03B 章 · 工程师落地手册：附录 F

> 停在这一页不关机。让想私下追问的同事有时间逮住讲者。
> 附录 C 的阅读单打印出来当 handout 发。

---

## Slide 29 —— 谢谢

- 谢谢
- 问题 & 讨论
- 联系方式见仓库 README

> 最后 2–3 分钟 Q&A。
> 如果没人问，可以自问自答 —— *"我猜有人会问 X，答案是 Y。"*
> 这是一种可用的"暖场"手法，尤其在中国技术分享会里。

---

## Slide 30（可选）—— 工作坊手册索引

- **30 分钟版**：F.0 → F.1 → F.2 → F.4 → F.7
- **60 分钟版**：全跑
- **90 分钟版**：F.7 后加 25 分钟动手填 HarnessCard

> 这张只在 90 分钟工作坊场景展示。详见 `outline.md · 应急切法` 一节。
