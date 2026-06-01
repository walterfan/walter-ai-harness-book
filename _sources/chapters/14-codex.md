---
status: draft
chapter-type: case-study
case-study-kind: closed-source
---

# 案例研究：Codex —— 把代理式编码变成一套可审计的工作面

> *Codex 的重点不只是"会写代码的模型"，而是模型周围那一圈可配置、可回滚、可审计的工作环境。*

OpenAI 对 Codex 的公开叙述，已经把注意力从单次补全转向了更完整的代理式编码工作面：`AGENTS.md`、权限规则、hooks、记忆、技能与 worktree，一起构成了一个团队可以调校的马具 {cite}`openai2026codex`。本章把 Codex 当作一具厂商托管的闭源马具来读：不试图复刻产品内部实现，只抽取那些团队能够在自己仓库中明确持有的表面。

```{note}
**边界。** 本章只分析 Codex 的公开可见配置面与可迁移实践。凡涉及运行时内部策略、模型选择、调度器、远端执行环境的判断，都按"不可见"处理；读者不应把本章当作产品内部实现说明。
```

## 14.1 —— Codex 的五个可持有表面

Codex 对团队真正有用的地方，是它把"让智能体怎么工作"这件事拆成几类可以被版本化的材料：

1. **项目手册。** `AGENTS.md` 让仓库拥有一份给智能体看的 onboarding 文件。它不是百科全书，而是入口、边界、验证命令与团队约定。
2. **权限规则。** 规则文件把"哪些命令可以静默运行、哪些必须问人、哪些默认拒绝"做成显式策略。
3. **hooks。** 会话开始、工具调用之后、任务结束时的固定动作，让智能体形成可重复的工作节奏。
4. **记忆。** 长期偏好与一次性任务上下文分开；稳定、低敏、长期有效的偏好才进入记忆。
5. **任务提示模板。** 人类把需求写成小型 work ticket，而不是模糊愿望。

这五个表面分别对应三大护法：`AGENTS.md` 和任务模板主要是 **SDD × 缰绳**；权限规则与 hooks 是 **TDD × 护栏**；记忆与结束自检则落在 **MDD × 梳理**。

## 14.2 —— 十二格亮点图

```{list-table}
:header-rows: 1
:widths: 20 8 72

* - 格子
  - 得分
  - 证据
* - SDD × 缰绳
  - 5
  - `AGENTS.md`、任务提示模板、技能入口共同塑造每回合上下文；这是 Codex 最强的可迁移表面。
* - SDD × 护栏
  - 4
  - 项目手册可以写明目录边界、公开 API、隐私规则与验证矩阵；坏规则仍需靠 hooks 或 CI 执行。
* - SDD × 牧场
  - 3
  - worktree 让任务有独立工作区，但验收标准仍主要由团队在 PR 与 CI 中定义。
* - SDD × 梳理
  - 3
  - `AGENTS.md` 可被版本化评审；但若没有固定审计节奏，它也会像普通文档一样漂移。
* - TDD × 缰绳
  - 3
  - 任务提示模板把"Done When"前置，能引导智能体找测试，但不等于测试先行。
* - TDD × 护栏
  - 5
  - 权限规则与 hooks 能把危险命令、廉价检查、结束自检变成机器执行的边界。
* - TDD × 牧场
  - 3
  - 独立 worktree 降低相互踩踏；真正的发布关卡仍要靠仓库自己的 CI/CD。
* - TDD × 梳理
  - 3
  - hooks 可以记录检查结果；是否把失败模式沉淀回测试套件，是团队责任。
* - MDD × 缰绳
  - 3
  - 结束自检可以要求列出命令、结果、风险；成本和吞吐仍需要外部度量承接。
* - MDD × 护栏
  - 4
  - 权限规则能把高风险命令转成人类确认点，是成本与爆炸半径的实际上限。
* - MDD × 牧场
  - 2
  - Codex 客户端本身不是团队发布系统；生产 SLI 仍要在业务侧定义。
* - MDD × 梳理
  - 4
  - 记忆、会话结束摘要、工作区隔离，给复盘提供了稳定抓手。
```

这张图的形状很鲜明：Codex 强在"把智能体的工作面做成可配置产品"，弱在"替团队定义业务验收与产出度量"。这正是本书一直强调的分界：厂商可以提供马具表面，团队必须持有马具责任。

## 14.3 —— `AGENTS.md` 是入口，不是杂物间

Codex 的 `AGENTS.md` 最容易被误用成"什么都往里塞"的长文档。更稳的做法是让它保持短小，只回答四类问题：项目地图、上下文指针、工作约定、验证矩阵。

```{literalinclude} ../_handson/14-codex/AGENTS.md.template
:language: markdown
```

这份模板刻意要求把长材料留在 `docs/`、`db/schema/`、`web/src/router/` 之类的真实位置。`AGENTS.md` 的作用是指路，而不是替代整个知识库。

## 14.4 —— 规则与 hooks：把"请小心"变成边界

自然语言提醒很有用，但它不是边界。边界必须能在工具调用之前或之后执行。Chapter 14 的 hands-on 里给出两层：

```{literalinclude} ../_handson/14-codex/rules.toml
:language: toml
```

```{literalinclude} ../_handson/14-codex/hooks.json
:language: json
```

这里的要点不是具体 schema，而是形状：读操作自由、验证操作便宜、破坏性操作问人、秘密相关操作默认拒绝。团队把这个形状包到自己当前版本的 Codex 配置里，就能避免被某个版本的字段名绑死。

## 14.5 —— 记忆只放长期偏好

记忆是最容易污染的表面。把一次性 bug 背景、票号、生产主机、客户样本写进长期记忆，会让后续任务背上隐私与幻觉双重债务。更好的边界是：只保存三个月后仍可能正确、且可以对新同事公开说出的偏好。

```{literalinclude} ../_handson/14-codex/memory.md
:language: markdown
```

同样的原则也适用于提示。一次性任务应该留在当前线程或 issue 里，而不是写进长期记忆；真正可复用的是"如何写好任务"的模板：

```{literalinclude} ../_handson/14-codex/prompt-template.md
:language: markdown
```

## 14.6 —— 给 AI 工具跑的 Codex Harness Checklist

Codex 的可持有表面比 Claude Code 更偏"项目工作面"：`AGENTS.md`、rules、hooks、memory、worktree、任务提示模板。下面这份 checklist 的目标，是让一个审计型 Codex 会话进入任意仓库后，能判断这具马具是否足够让它安全地开始工作。

```{list-table}
:header-rows: 1
:widths: 22 42 36

* - 检查项
  - AI 工具应该怎么查
  - 通过标准
* - `AGENTS.md` 入口
  - 查找根目录与子目录 `AGENTS.md`；记录最近层级如何覆盖全局规则。
  - 根文件少于约 100 行，提供项目地图、上下文指针、工作约定、验证矩阵。
* - 模块局部规则
  - 在将要修改的路径向上查找最近的 `AGENTS.md` 或同类局部说明。
  - 局部规则能解释该模块的测试、边界、生成文件、禁止改动区。
* - 权限规则
  - 查找 `.codex/rules.toml` 或团队等价文件；枚举 `allow`、`ask`、`deny`。
  - 读操作可自由执行；验证命令可执行；破坏性 git、部署、secret 读取必须 ask/deny。
* - Hooks 廉价验证
  - 查找 `.codex/hooks.json` 或等价 hook 配置；按文件类型映射验证命令。
  - 编辑后能触发格式化、lint、typecheck 或窄测试；长测试留给显式验证阶段。
* - Worktree 隔离
  - 运行或记录 `git status --short`、当前分支、是否在独立 worktree；检查未提交改动。
  - 任务开始前知道自己在哪个分支 / worktree；不会覆盖用户未提交改动。
* - Memory 卫生
  - 查看 Codex memory 或团队长期偏好文件；检查是否含 token、host、ticket、一次性上下文。
  - memory 只含稳定、低敏、长期偏好；一时任务上下文留在线程或 issue。
* - Prompt 工单化
  - 检查用户请求或 issue 是否有 Goal、Context Pointers、Constraints、Done When。
  - 非平凡任务先研究 / 计划，再执行；完成标准可验证。
* - 验证矩阵
  - 从 `AGENTS.md`、package files、Makefile、CI 中提取受影响栈的验证命令。
  - 每个被改栈至少有一个明确检查；没有测试时必须说清缺口。
* - 隐私与日志
  - 搜索日志规则、secret scanning、`.env` 处理、PII 禁止输出说明。
  - final summary 不回显秘密、cookies、请求体、客户数据；日志新增语句有敏感级别判断。
* - 结束自检
  - 查 hook 或 final response 约定是否要求列文件、命令、结果、风险、跳过项。
  - 任务结束能留下可审计证据，而不是只说"done"。
* - 梳理节奏
  - 查找 harness review、AGENTS.md 更新记录、rules/hooks 变更记录。
  - 项目有固定节奏清理过期规则、失败 hook、无用 memory 和失效命令。
```

Codex 可以把这份检查作为任务前的"起飞前检查"。一份合格输出不需要长，但必须有证据：

```yaml
tool: codex
repo: "<path>"
readiness: ready | ready-with-warnings | blocked
checks:
  - id: agents-entry
    status: pass | warn | fail
    evidence:
      - "<path>:<line>"
    note: "<one sentence>"
blocked_by:
  - "<only if readiness=blocked>"
minimum_next_step: "<single concrete action>"
```

这份 checklist 也可以反向用来写 `AGENTS.md`：如果某一项无法检查，就说明这具马具在那个面上还没有落地。比如没有验证矩阵，不要让智能体猜测试命令；没有权限规则，不要假装"请小心"能挡住一次 `git reset --hard`。

## HarnessCard

```{list-table}
:header-rows: 1
:widths: 35 65

* - 字段
  - 值
* - HarnessCard schema 版本
  - CAR-HarnessCard v0.2 {cite}`car2025decomposition`
* - 对象
  - Codex 公开配置面，2026-05 观察窗口 {cite}`openai2026codex`
* - 许可证
  - Codex 产品本身为闭源；本章 hands-on 示例以 MIT 协议发布
* - Control 层（CAR）
  - `AGENTS.md`、提示模板、记忆共同塑造任务上下文。
* - Agency 层（CAR）
  - 工具与 shell 行动通过权限规则、hooks、人类确认共同约束。
* - Runtime 层（CAR）
  - 本地仓库、worktree、远端模型与客户端运行时的组合；业务验收仍归团队 CI/CD。
* - SDD（0–5）
  - 3.75
* - TDD（0–5）
  - 3.5
* - MDD（0–5）
  - 3.25
* - 主要引用
  - {cite}`openai2026codex`
```

## 研究脉络

- **OpenAI Codex 公开实践** {cite}`openai2026codex` —— 本章的主要厂商来源。
- **AGENTS.md 约定** {cite}`agenticai2025agentsmd` —— 项目级智能体手册的生态背景。
- **CAR 分解** {cite}`car2025decomposition` —— HarnessCard 所使用的三层框架。
- **Fowler 的 Harness Engineering 词汇** {cite}`fowler2026harness` —— 本章把 Codex 映射到"三大护法 × 四区域"的语言来源之一。

## 动手环节

在 `source/_handson/14-codex/` 下，住着五份可直接改造的制品：

- `AGENTS.md.template` —— 一份少于 100 行的项目手册模板。
- `rules.toml` —— 一份命令权限边界的形状示例。
- `hooks.json` —— 会话开始、编辑后廉价检查、结束自检的 hooks 示例。
- `memory.md` —— 长期记忆的内容边界。
- `prompt-template.md` —— 把一次性需求写成小 work ticket 的提示模板。
