---
status: draft
chapter-type: case-study
case-study-kind: closed-source
---

# 案例研究：通过《马书》看 Claude Code

> *本书中唯一一份闭源案例。带着这一点去读。*

## 逆向工程免责声明

Claude Code 产品是闭源的。本章的分析依赖三类证据，按权威性递减排列：

1. **Anthropic 的官方公开文档与发布文章** {cite}`anthropic2024claudecode` 以及 MCP 规范 {cite}`anthropic2024mcp` —— 第一权威。
2. **运行时实测行为**：作者在 2026-03 到 2026-04 的观察窗口里，在 macOS 与 Linux 上运行 Claude Code CLI，记入会话日志的观察结果。
3. **张汉东《马书》2026 年的逆向工程分析** {cite}`zhangbook2026` —— 下文称 *马书* ——一份公开发行的中文研究，系统拆解了 Claude Code 的内置提示、技能库、hooks 契约与工具 schema。

**观察窗口。** 下文所有结论只反映 Claude Code 在 **2026-03-01 到 2026-04-15** 之间的行为。此窗口之外的行为不保证一致。

**撤回承诺。** 若 Anthropic 发布官方文档或公开声明与下文任一结论冲突，本章将在 30 天内更新，并把被撤回的结论划掉，附上注明日期的说明。本书把逆向观察视为 *临时性* 结论，而非权威结论。

**版权。** 本章不会原样转载《马书》或 Claude Code 的内部捆绑内容，单段引用不超过合理使用上限的 20 行，在可能处标注《马书》页码。

## 10.1 —— 用三大护法 × 四区域矩阵来读 Claude Code

如实测所见、并被《马书》所记载：Claude Code 把马具职责，分布在三个彼此重叠的表面上：

- **内置系统提示**（缰绳，主要是 SDD）—— 一份数 KB 的长文档；《马书》跨多章复刻并批注过它；里面包含角色设定、工具使用的启发式规则、引用格式、以及显式的"红旗自问清单"。
- **hooks 契约**（护栏，横跨 TDD 与 MDD）—— `.claude/hooks.json` 支持 `PreToolUse`、`PostToolUse`、`SessionEnd`、`UserPromptSubmit` 几类匹配器；`PreToolUse` 钩子以非零退出码结束，就会拒掉那次工具调用。
- **技能系统**（缰绳 ＋ 牧场，主要是 SDD）—— `~/.claude/skills/` 下的 `SKILL.md` 文件，智能体根据 front-matter 里的 `description:` 自动发现并调用。

以下是《马书》对内置提示的一段简短摘录（原文为中文；为便于叙述，译文由作者自行翻译）：

```text
[摘录，≤ 20 行，译自《马书》第 4 章 4.2，p. 113]

系统消息尾部：
    - 被问到事实性问题时，至少引用一处来源。
    - 写代码时，优先"修改"而非"新建"。
    - 输出中绝不要包含"由 AI 生成"的落款。
    - 若有 skill 适用，作答之前先读并遵循它。
    - 把用户文件视作权威；未确认之前不覆盖。
```

《马书》主张——实测行为也佐证——这些"提示尾部规则"是本产品里最承重的那一件 SDD × 缰绳 制品。

## 10.2 —— 十二格亮点图（含置信等级）

下表每一格都标注一条置信等级：`observed`（直接可在运行时行为中复现）、`inferred`（由《马书》＋ 官方文档 ＋ 实测三角印证推得）、或 `speculative`（当前是最佳猜测，未来的官方披露可能把它升级或推翻）。

```{list-table}
:header-rows: 1
:widths: 18 6 16 60

* - 格子
  - 得分
  - 置信等级
  - 证据，以及什么会改变这个置信等级
* - SDD × 缰绳
  - 5
  - observed
  - 内置提示 ＋ 技能系统直接塑造每一回合；被《马书》第 4 章 {cite}`zhangbook2026` 与 Anthropic 官方文档 {cite}`anthropic2024claudecode` 双重印证。
* - SDD × 护栏
  - 3
  - inferred
  - `SKILL.md` 的 front-matter schema 无官方文档；格式不对的 skill 会被悄悄跳过。《马书》第 5 章复现了解析器的这种"宽容模式"。
* - SDD × 牧场
  - 3
  - inferred
  - 内置并无验收仪式；评审纪律交由宿主团队自己定。
* - SDD × 梳理
  - 3
  - inferred
  - `/cost`、`/status`、`/clear` 几条斜杠命令支持梳理，但节奏由操作者自己掌控。
* - TDD × 缰绳
  - 3
  - inferred
  - 默认技能与《马书》第 6 章都在鼓励"测试先行"的表述，但并未强制。
* - TDD × 护栏
  - 5
  - observed
  - 非零退出码的 `PreToolUse` 钩子会拒掉编辑；Anthropic 文档有记载，hands-on 的 `hooks.json` 也做了演示。
* - TDD × 牧场
  - 2
  - speculative
  - 若 Anthropic 公开 CI 集成规范，这一格可被升级为 `inferred`。若上线带有文档化退出协议的 `claude-code ci` 子命令，也会改变置信等级。
* - TDD × 梳理
  - 2
  - speculative
  - 若 Anthropic 在模型更新的 release note 中，公开标记"会使旧测试假设失效"的信号，这一格可被升级。
* - MDD × 缰绳
  - 4
  - observed
  - `/cost` 端点 ＋ 状态栏 token 计数器，合起来暴露了一个能用的"北极星候选项"。
* - MDD × 护栏
  - 3
  - inferred
  - API 层有速率限制，但 *本地* 成本上限需要操作者自己写钩子。《马书》第 7 章记录了这些默认限制。
* - MDD × 牧场
  - 2
  - speculative
  - 没有"发布 SLI"这个概念；Claude Code 是客户端工具，不是服务端产品。
* - MDD × 梳理
  - 3
  - inferred
  - Anthropic 每周推送 prompt 库更新，这相当于一路上游的"梳理信号"。
```

至少有一格——**TDD × 牧场**——被显式标为 `speculative`。要把它升级，需要其中之一：要么 Anthropic 上线带文档化、机器可读退出协议的 `claude-code ci` 子命令；要么官方 release note 正式宣告现有行为稳定且公开版本化。

## 10.3 —— hooks 契约 —— Claude Code 的主要护栏

Claude Code 的 `.claude/hooks.json` 是这款产品里 *最可迁移* 的那一块，因为它是纯声明式的。实测结论是：任何钩子以退出码 2 结束，就会拒掉当前那次工具调用；这一点由 Anthropic 官方文档 {cite}`anthropic2024claudecode` 记录，且与实测一致。

```{literalinclude} ../_handson/10-claude-code/hooks.json
:language: json
```

hands-on 制品是 *基于公开文档合成* ——明确不是任何内部文件的拷贝。读者把它搬进自己的 `.claude/` 配置，用的是一份重建版本。

## 10.4 —— 哪些可以搬走，哪些不行

- **可搬走的**：内置提示这种纪律（一份长且承重的系统消息）、`SKILL.md` 的格式（带 front-matter 的简单 markdown）、以及 hooks 契约（由退出码驱动的拒绝机制）。
- **不能直接搬**：Claude 专属的模型供应商耦合、斜杠命令注册表、内置技能库的原文措辞（受版权限制）。

想拿到 *模式* 又不想付 Anthropic 平台成本的读者，可以：(a) 在自己的智能体里复刻第一项（任何会读取长系统消息的智能体都行）；(b) 几乎不费力地复刻第二项（它本来就是 markdown）；(c) 在任何支持 "写前回调" 的智能体里采纳 Claude Code 的钩子语法。

### 闭源马具的结构性风险

从一套闭源系统里学习，其不对称性值得明说——这不是批评 Claude Code，而是在提醒读者：本章的结论该如何（以及不该如何）推广到别处。

- **观察窗口偏置。** 10.2 的每一条结论都锚定在 2026-03 到 2026-04 的观察窗口。Anthropic 每周都在更新 prompt 库；任何关于"内置提示 *内容*"的结论，其半衰期是以周计的，不是以季度计。这不是缺陷——这是产品的正常演进——但它意味着：把 10.2 当作静态参考的读者，心里那份模型会逐渐过时。
- **不可证伪的 speculative 等级。** 10.2 里有两格挂着 `speculative` 置信等级。诚实地说，这些分数是猜测；更微妙的一层是——*没有 Anthropic 的配合，它们就无法被证伪*。读者应当把 speculative 格视为占位符，而非证据。
- **与 Anthropic 发布节奏的耦合。** 上面每一条"可迁移模式"，都假设 Anthropic 继续按当前轨迹发布（hooks 保持声明式、SKILL.md 保持简单 markdown、内置提示仍可被覆盖）。厂商若决定合并、简化、或替换这些表面，对应那条可迁移性就作废。马具工程意义上正确的做法是——**采纳模式，不要采纳表面**——自己在一层稳定抽象之上写一套 `PreToolUse` 风格钩子语法的团队，能挺过 Claude Code 2.0 的重写；直接绑死当前 `hooks.json` schema 的团队则不能。

```{admonition} 陷阱——把观察当成规范
:class: warning

一支团队读完第 10 章，把 10.3 合成出来的 `hooks.json` 拷过去，在"退出码 2 拒掉当前工具调用"这条实测行为之上建了半年工具链。随后 Anthropic 发布一次 Claude Code 更新——把退出码 2 用于另一种语义，并改以结构化 JSON 响应代之。这套工具有一半悄悄坏了。**为什么**：实测行为从来不是 API ——那是行为，而行为是厂商可以随意修改的。本章的"撤回承诺"覆盖的是本书；没有什么来覆盖团队的工具链。**解法**：在依赖任何一份逆向得来的接口之前，*先* 用自己的抽象把它包住。一只名叫 `refuse_tool_call(reason)` 的函数——今天退出 2、下个季度退出 3——能扛过厂商的内部演进；直接 `sys.exit(2)` 的调用扛不住。这与 Feathers {cite}`feathers2004legacy` 对遗留接口开出的那剂药方是同一种纪律——只不过这次应用在"团队并不拥有"的那套系统上。
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
  - Claude Code，2026-03 到 2026-04 观察窗口 {cite}`anthropic2024claudecode`
* - 许可证
  - 对象本身为闭源；合成示例以 MIT 协议发布
* - Control 层（CAR）
  - 主张极强；内置提示长达数 KB。
* - Agency 层（CAR）
  - 工具访问被 hooks 与用户确认提示强力把守。
* - Runtime 层（CAR）
  - 云端 LLM ＋ 本地 CLI；可通过 hooks 选装 Docker 沙箱。
* - SDD（均值）
  - 3.5（observed=1，inferred=3，speculative=0）
* - TDD（均值）
  - 3.0（observed=1，inferred=1，speculative=2）
* - MDD（均值）
  - 3.0（observed=1，inferred=2，speculative=1）
* - 主要引用
  - {cite}`zhangbook2026`
```

上述每一项分数，都带有 10.2 中对应格子的置信等级。

## 研究脉络

-  **马书** {cite}`zhangbook2026` —— 对内置提示、技能库、hooks 行为的首要逆向工程来源。
- **Anthropic Claude Code 发布文章** {cite}`anthropic2024claudecode` —— 作为权威记录的官方文档。
- **MCP 规范** {cite}`anthropic2024mcp` —— Claude Code 工具生态所对齐的公开规范。
- **CAR 分解** {cite}`car2025decomposition` —— 本章把 HarnessCard 序列化到的那套 schema。

## 动手环节

在 `source/_handson/10-claude-code/` 下，住着一份可直接拷走的制品：

- `hooks.json` —— 一份最小的 `.claude/hooks.json` 示例，含：一条"测试失败就停"的 `PreToolUse` 规则、一条抓取 diff 的 `PostToolUse` 规则，以及一条 `SessionEnd` 成本报告触发器。基于公开文档合成；不是任何内部文件的拷贝。
