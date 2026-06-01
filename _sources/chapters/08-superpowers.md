---
status: draft
chapter-type: case-study
case-study-kind: open-source
---

# 案例研究：Superpowers

> *不是框架，不是平台。是一整套技能（skills），教智能体在动笔之前先想两遍。*

Superpowers 由 Joseph Vincent 编写，以 `obra/superpowers` 仓库开源发布 {cite}`vincent2025superpowers,vincent2025superpowersrepo`。它在哲学上是 OpenHarness 的反面：OpenHarness 交付的是运行时和沙箱，Superpowers 交付的 *只是* 一组 `SKILL.md` 文件，用来塑造一个智能体（具体说是 Claude Code）"如何框自己的工作"。整个项目本质上就是三十来份 markdown 文件——这本身，就是它的论点。

## 08.1 —— 以技能为先的工作流

Superpowers 的经典工作流是一条五步弧：

1. **头脑风暴**（`skills/brainstorming/SKILL.md`）—— 在意图被澄清之前，拒绝开始实现。
2. **写计划**（`skills/writing-plans/SKILL.md`）—— 把头脑风暴编译成一份带评审节点的书面计划。
3. **测试驱动开发**（`skills/test-driven-development/SKILL.md`）—— 只对着一条失败的测试来实现。
4. **代码评审**（`skills/requesting-code-review/SKILL.md`）—— 合并之前，进行一次带有明确评价细则的显式评审。
5. **收尾**（`skills/finishing-a-development-branch/SKILL.md`）—— 集成、清理、提 PR。

每一步都是智能体通过 `using-superpowers` 这条元技能 *选择* 进入（或被 *推* 进入）的一项技能。Anthropic 的 skills 文档 {cite}`anthropic2024skills` 描述了这套机制；Superpowers 是迄今为止、针对这套机制最完整的公开技能库。

## 08.2 —— 一条代表性的技能（不超过 20 行）

`test-driven-development/SKILL.md` 是承重的那一份，同时也是最短的一份。下面摘录了它的核心（用省略号标出省略的散文），并在上游许可证下引用：

```markdown
# Test-Driven Development

## When to use

Use when implementing any feature or bugfix, before writing implementation code.

## What this skill does

1. Writes a failing test that captures the requirement.
2. Runs the test suite and confirms only this test fails.
3. Implements the minimum code to make the test pass.
4. Refactors while the test stays green.

## Red flags that stop this skill

- "I'll write the test after." — no. The skill exits.
- A passing first test — suspect; re-read the requirement.
```

这是一份技能文件，*不是* 一个代码模块——智能体的行为是靠读散文被改变的，而不是靠调用 API。Mills 的 Socratic design 论文 {cite}`mills2015socratic`、以及 Zeller 的系统性调试 {cite}`zeller2009whyprogramsfail`，是这类做法的思想先人：技能要求智能体在提交行动之前，先审问自己。

## 08.3 —— OpenHarness vs Superpowers：互补，不是竞争

OpenHarness 提供的是 *引擎*；Superpowers 提供的是 *纪律*。一具生产级马具通常两样都要。这两个项目沿着三条轴彼此不同，对于要在二者之间做取舍的读者，有必要把这三条轴显式列出：

```{list-table}
:header-rows: 1
:widths: 20 40 40

* - 轴
  - OpenHarness
  - Superpowers
* - 首要制品
  - Python 包 ＋ Docker 沙箱
  - `~/.claude/skills/**/SKILL.md` 这些 markdown 文件
* - 护法侧重
  - TDD × 护栏、MDD × 护栏（通过权限、沙箱）
  - SDD × 缰绳、TDD × 缰绳（通过技能的被调用）
* - 采用成本
  - 高——新依赖、新运行时
  - 低——把 markdown 拷进 `~/.claude/skills/` 就完
```

## 08.4 —— 十二格亮点图

```{list-table}
:header-rows: 1
:widths: 20 8 72

* - 格子
  - 得分
  - 证据
* - SDD × 缰绳
  - 5
  - 整个项目的存在，就是为了强化这一格；`using-superpowers/SKILL.md` 加上约 30 条兄弟技能，直接塑造智能体动笔之前的上下文。
* - SDD × 护栏
  - 2
  - 技能是散文；针对技能 front-matter 没有 schema 校验器。
* - SDD × 牧场
  - 4
  - `requesting-code-review/SKILL.md` ＋ `receiving-code-review/SKILL.md` 构成按角色划定的验收关卡。
* - SDD × 梳理
  - 3
  - `finishing-a-development-branch/SKILL.md` 以及"头脑风暴 → 计划"那条链，本身就在让技能保持新鲜。
* - TDD × 缰绳
  - 5
  - `test-driven-development/SKILL.md` 在整个技能库里承重。
* - TDD × 护栏
  - 3
  - 技能里的散文在测试为红时拒绝继续；真正的执行层面，仍然依赖宿主仓库的 Claude Code hook。
* - TDD × 牧场
  - 2
  - Superpowers 自身不附带集成测试套件。
* - TDD × 梳理
  - 2
  - flaky 测试的处置策略，在技能库层面并未定义。
* - MDD × 缰绳
  - 2
  - 技能库里没有一条北极星度量。
* - MDD × 护栏
  - 1
  - 没有成本上限，没有限流，没有熔断。
* - MDD × 牧场
  - 1
  - 没有发布 SLI（这个库是一份无状态的 markdown）。
* - MDD × 梳理
  - 2
  - 没有定义每周审计；漂移由上游 changelog 捕捉。
```

最强的一列：**缰绳**（均值 4.25）。最弱的一条：**MDD 整行**（均值 1.5）。Superpowers 一整个往 SDD／TDD × 缰绳 那侧倾斜，这与它的目的一致——它是一个技能库，不是一套运行时。

## 08.5 —— 什么时候该抄起 Superpowers

- 你的团队已经在用 Claude Code，想要更强的"动笔前纪律"，又不想额外上一个新平台。
- 你已经有一份 `AGENTS.md` 或 `CLAUDE.md` 兼容层，但留意到智能体仍然跳过测试；TDD 技能能帮上忙。
- 你想要一套评审仪式，*同时* 作用在智能体的产出和人类的产出上；code-review 系列技能两头都覆盖。

- 以下情况 *不要* 抄 Superpowers：你需要的是运行时隔离（应当抄 OpenHarness、或 Claude Code 的 hooks ＋ 沙箱），或者你面对的是一个不尊重 `SKILL.md` 的非 Claude 智能体。

### Superpowers 在结构上弱的地方

08.4 那张十二格记分卡，把这份取舍摆得明明白白：在 SDD × 缰绳 与 TDD × 缰绳 两格上，Superpowers 是最强的公开范例；在整行 MDD 上，它则是最弱的。这种不对称是 *结构性* 的——一堆 markdown 文件，既不能强制执行它所开出的处方，也观测不到处方到底有没有被照办。两种失败模式直接由此而来。

- **开了方子，却没有执行力。** 一份技能的散文说"测试为红时拒绝继续"。若宿主仓库里没有哪一条 hook *机械地* 拒绝"继续"，这份技能就会变成"合规剧场"（第 02 章第 3 阶段那条陷阱，在这里贴脸适用）。Superpowers 与 Claude Code 的 hook 搭配时最强；单独使用时，它就是一条措辞强烈的建议而已。
- **没有自我可观测性。** 这个库没有任何信号能告诉你"团队安装了 30 条技能，只有 4 条是常用的"。Skill-sprawl（第 02 章第 3 阶段那条陷阱）在"只有技能"的马具里打得最狠，恰恰是因为根本没有"技能调用率"这一类度量。

```{admonition} 陷阱——"技能就是我们的马具"
:class: warning

一支团队采用了 Superpowers，把三十条技能拷到 `~/.claude/skills/` 下，然后宣称马具造完了。三个月后，产出质量的可测量值没有动——尽管团队在复盘里报告"技能采纳率很高"。**为什么**：在没有一条 *拒绝* "跳过了某项技能的那次对话轮次" 的护栏、以及没有一条度量报告 "哪些技能实际被触发过" 的情况下，这座技能库是在靠荣誉制度运作。团队的意图与智能体的行为，只能靠自我汇报来度量。**症状**：复盘里对这些技能赞不绝口；事故复盘却揭示，相关技能本来在，只是没被调用。**解法**：为每一条承重技能，配一条 `PreToolUse` hook——当技能的前置条件（红色测试、尚未签字的设计、缺失的验收表）不满足时就失败。Superpowers 提供处方；Claude Code 的 hook 提供执行。单独哪一端，都不是马具。
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
  - Superpowers，2026-04 快照 {cite}`vincent2025superpowersrepo`
* - 许可证
  - MIT {cite}`vincent2025superpowers`
* - Control 层（CAR）
  - 通过约 30 条散文技能，持有强烈主张。
* - Agency 层（CAR）
  - 与宿主 Claude Code 安装相比没有变化。
* - Runtime 层（CAR）
  - 交由 Claude Code 处理；Superpowers 不自带运行时。
* - SDD（均值）
  - 3.5
* - TDD（均值）
  - 3.0
* - MDD（均值）
  - 1.5
* - 主要引用
  - {cite}`vincent2025superpowers`
```

## 研究脉络

- **TDD** {cite}`beck2002tdd` —— TDD 技能的学术谱系。
- **调试** {cite}`zeller2009whyprogramsfail` —— systematic-debugging 和 receiving-code-review 两条技能背后的谱系。
- **代码评审** {cite}`bacchelli2013codereview` —— 现代代码评审的研究，正是 request / receive review 两条技能的动机所在。
- **Socratic design 论文** {cite}`mills2015socratic` —— 给"先向智能体提问、再允许它行动"这类技能提供哲学支撑。
- **Anthropic 的 skills 文档** {cite}`anthropic2024skills` —— `SKILL.md` 文件的官方格式规范。

## 动手环节

在 `source/_handson/08-superpowers/` 下，住着两份可直接拷走的制品：

- `SKILL.md` —— 一份可直接扔进去就能用的技能，读者可以把它拷到 `~/.claude/skills/spec-first-feature/SKILL.md`。
- `walkthrough.md` —— 一段 *安装 → 调用 → 观察* 的走查，用来端到端验证这份技能确实被触发。
