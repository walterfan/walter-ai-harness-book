---
status: draft
chapter-type: narrative
---

# 插章：Agent Memory 系统的结构

> *一支不会记住规则、最佳实践和常见陷阱的智能体队伍，只是在用更快的速度重复新人错误。*

第 03 章说，Harness Engineering 的主语不是模型，而是模型周围的结构。第 08 章会拆 Agent Loop。本插章夹在二者之间，只讲其中一块最容易被低估、也最容易腐烂的结构：**记忆系统**。

记忆系统对驾驭工程的重要性不言而喻。没有记忆，智能体每一轮都像临时工：它可能读到当前文件，却不知道团队昨天刚定下的规则；它可能跑通测试，却再次踩进上周刚复盘过的坑；它可能问了用户偏好，却在下一个会话里重新问一遍。这样的智能体不是没有能力，而是没有组织性。

先给结论：**Agent Memory 不是把更多文本塞进上下文窗口，而是把经验分层、设权威、可召回、可过期、可梳理。** 它的工程目标不是"永远记住一切"，而是：

- 稳定规则总能被召回。
- 最近事实能在合适时间出现。
- 过期经验会被降权或清理。
- 敏感内容不会因为被记住而泄露。
- 每条记忆都能解释自己为什么仍然应该被相信。

```{mermaid}
flowchart LR
  E["经验输入<br/>rule / practice / pitfall / preference / event"] --> C["分类<br/>temp / short / long / archive"]
  C --> W["写入契约<br/>key / summary / source / verified_at / importance"]
  W --> R["召回<br/>keyword / metadata / semantic"]
  R --> P["提示词装配<br/>rank / dedupe / budget"]
  P --> A["Agent 行动"]
  A --> O["观察与复盘"]
  O --> G["梳理<br/>prune / refresh / archive / promote"]
  G --> C
```

这张图里最重要的箭头不是"召回"，而是最后那条"梳理"。一套没有梳理的记忆系统，会从团队经验库退化成一块过期经验的垃圾场。

## 04.1 记忆不是缓存

很多团队第一次给智能体加 memory，会从一个最简单的实现开始：把用户说过的话 append 到文件里，下一次按关键词搜出来。这种实现足够启动，但它也最容易制造错觉。它像缓存，却被当成知识库；它像日志，却被当成规则；它像对话历史，却被当成长期事实。

在 Harness Engineering 里，这几类东西必须分开：

- **上下文窗口** 是本轮任务正在看的材料。它昂贵、短命、会被截断。
- **短期记忆** 是跨几轮会话仍有价值的近期事实。它有半衰期。
- **长期记忆** 是稳定偏好、团队规则、架构决策、已验证的陷阱清单。它必须有 key、来源和刷新机制。
- **知识库** 是人和智能体共同维护的权威文档，例如 `AGENTS.md`、`SKILL.md`、ADR、PKB、runbook。
- **日志** 是发生过什么的证据。它可以喂给记忆系统，但不能自动等同于记忆。

把这些混在一起，智能体就会把"某次对话里随口说的话"当成永久规范，把"两个月前的临时绕过"当成最佳实践，把"被废弃的目录结构"当成当前架构。记忆系统的第一条纪律，是**给每种记忆一个生命周期**。

## 04.2 五层记忆：temp、short、long、archive、meta

一个实用的 Agent Memory 系统，至少要把物理存储拆成五层。下面这份分层来自我曾经做的一个 AI Agent 记忆增强设计：从 Markdown append-only 文件升级为 SQLite-backed store，同时保留关键词召回，并在 sqlite-vec 可用时启用语义召回。

```{list-table}
:header-rows: 1
:widths: 16 24 26 18 16

* - 层
  - 放什么
  - 生命周期
  - 默认召回
  - 主要风险
* - **Transient / temp**
  - 本 session 的临时状态、未完成参数、工具中间结果
  - session 结束或 TTL 到期即删除
  - 只进 session-aware context
  - 泄漏到全局上下文
* - **Short-term**
  - 近期事件、短期偏好、正在推进的任务、最近总结
  - 按保留期、重要度、访问次数滚动
  - 关键词 + 元数据 + 可选向量
  - 旧事件被误当成稳定事实
* - **Long-term**
  - 稳定规则、用户偏好、团队最佳实践、常见陷阱、长期目标
  - 默认持久，按 key 逻辑 upsert
  - 最高优先级召回
  - 污染后长期影响行为
* - **Archive**
  - 冷的历史总结、从 short-term 退下来的低频记忆
  - 有容量和保留期
  - 查询时显式启用
  - 变成永不清理的墓地
* - **Meta**
  - schema 版本、导入状态、向量可用性、预算、维护游标
  - 跟系统生命周期一致
  - 不直接给模型
  - 配置漂移不可见
```

这五层的价值，不在于名字漂亮，而在于它们给"该不该记住"这个问题提供了默认答案。临时工具结果不该嵌入向量库；短期事件不该永远占住 prompt；长期规则不该被 age-based pruning 悄悄删掉；归档记忆不该默认污染每一轮任务。

## 04.3 长期记忆：规则、最佳实践、常见陷阱

长期记忆是驾驭工程里最值钱、也最危险的一层。它值钱，是因为它承载团队经验；它危险，是因为一条错误长期记忆会稳定地把智能体引向错误方向。

长期记忆至少应当覆盖六类内容：

1. **规则（rules）**：必须遵守的工程约束，例如"不要直接改生成文件"、"数据库迁移必须带回滚计划"。
2. **最佳实践（best practices）**：推荐路径，例如"新增 API 先补 OpenAPI contract，再补 handler"。
3. **常见陷阱（pitfalls）**：已经踩过的坑，例如"这个 repo 的 `make test` 会跳过集成测试，发布前必须跑 `make test-all`"。
4. **偏好（preferences）**：用户或团队稳定偏好，例如语言、命名、提交风格。
5. **事实（facts）**：长期有效的项目事实，例如核心目录、owner、运行环境。
6. **决策（decisions）**：ADR 或设计评审里已经定下来的取舍。

我曾经写的一个 skill `agents-md-generate`， 这个 skill 里有一条非常重要的隐含原则：**面向智能体的长期规则，应当先进入可审阅、可 diff、可链接的制品，再被记忆系统索引或召回。** `AGENTS.md` 是仓库级入口；`SKILL.md` 是流程级记忆；ADR 和 PKB 是架构级记忆。向量库、SQLite 表、摘要缓存都可以加速召回，但它们不应该成为唯一真源。

换句话说：不要把团队规则只藏在 memory database 里。一个好的长期记忆写入，应当长这样：

```text
memory_key: repo.test.full-command
summary: 发布前必须运行 make test-all；make test 只覆盖快速单测。
source: AGENTS.md#commands
verified_at: 2026-05-07
importance: 10
tags: [rule, test, release]
```

这条记忆有 key，可以 upsert；有 source，可以追溯；有 verified_at，可以梳理；有 importance，可以排序；有 tags，可以过滤。最坏情况下，即使向量召回失效，关键词和元数据也仍然能找回它。

## 04.4 写入路径：不是所有事情都配被记住

记忆系统真正的产品设计，不在 recall，而在 write path。因为写错一条长期记忆的代价，远高于少召回一条短期记忆。

一套稳妥的写入面，应当至少分成两条公开工具：

- `remember`：兼容通道，写入短期记忆。适合近期偏好、当前任务状态、可丢弃事件。
- `remember_long_term`：显式长期通道，必须带 `memory_key` 和 `summary`，可选 `raw_content`、`importance`、`tags`。适合规则、最佳实践、常见陷阱、稳定偏好。

这种分离看似啰嗦，实际是在给智能体加一道语义护栏。它让"我要永久影响未来行为"这件事变得可见、可审阅、可测试。若把长期写入伪装成普通 `remember` 的一个参数，智能体很容易把每一次临时上下文都升格为永久事实。

长期写入还应当使用 **logical upsert**。当 `memory_key` 已存在时，新版本写入 active store，召回时按 key 去重，选择最高 version 或最新 `updated_at`。这样历史库仍可读，但旧规则不会和新规则一起进入 prompt 打架。

## 04.5 召回路径：排序比相似更重要

语义召回很有用，但它不是记忆系统的灵魂。灵魂是排序策略。一个和 query 很相似的短期旧事件，不应该排在一条长期团队规则前面；一个 archive 里的冷记录，不应该默认压过当前 session 的临时状态；一个没有来源的摘要，不应该压过有 `AGENTS.md` anchor 的规则。

实际装配 prompt context 时，可以按这个顺序思考：

1. **Long-term first**：稳定规则、最佳实践、常见陷阱、长期偏好。
2. **Short-term second**：高重要度、近期访问、与任务相关的事件。
3. **Transient only for session**：只在 `SystemContextForSession(session_id, maxChars)` 这类 session-aware 入口中加入。
4. **Archive opt-in**：只有用户或智能体显式查历史时才进来。

语义向量可以参与候选生成，但最后仍要经过 deterministic merge：跨 active DB 和 historical DB 搜索，按 `memory_key` 去重，按层级、重要度、recency、access count、source quality、字符预算排序。RAG 与 context engineering 的教训在这里同样适用：上下文不是越多越好，而是越可信、越新鲜、越贴合任务越好 {cite}`lewis2020rag,karpathy2025context`。

## 04.6 存储形态：一个 active DB，加历史 rolled DB

记忆存储不必一开始就上外部向量数据库。对一支本地或单进程智能体来说，一个 SQLite-backed memory store 往往更容易被驾驭：

- 一个 active writable DB，例如 `<memory_dir>/agent_memory.db`。
- 若 active DB 超过大小预算，例如 9.9 MiB，就 rollover 成带时间戳的 historical DB。
- active 和 historical DB 都参与召回，但新写入只进 active。
- sqlite-vec 可用时，embedding 用 BLOB 存储并参与 cosine distance；不可用时，关键词和元数据召回必须继续可用。
- embedding 生成异步进行，写入 memory row 不等待模型或远端 embedding provider。

这套设计的关键不是 SQLite，而是**有界增长**。记忆系统一旦没有预算，就会变成第二个不受控日志系统。至少要给它这些预算：

- active DB 文件大小。
- 总 store 大小或 historical DB 数量。
- transient row 数与 TTL。
- short-term row 数与 retention。
- archive row 数与 retention。
- raw content 最大字节数。
- embedding row 数或 embedding 总大小。

删除 row 后，SQLite 文件不一定变小；维护作业还要负责 incremental vacuum、WAL checkpoint、必要时的显式 compact。否则"已经 prune 了"只是表面动作，磁盘和 prompt 预算仍会被旧记忆拖住。

## 04.7 梳理：记忆系统的第四列

第 08 章会把"梳理（Groom）"列正式放进马具矩阵。记忆系统是最能说明这列必要性的例子：记忆的价值会随时间衰减，而它造成的行为影响却会持续存在。

一项 memory groom job 应当定期做这些事：

- 删除过期 transient rows。
- 归档或剪枝低价值 short-term rows。
- 刷新长期规则的 `verified_at`，或把它们标成 stale。
- 检查长期记忆的 source link 是否仍然存在。
- 删除低价值 embedding，优先保留 summary。
- 在预算压力下先清 short-term 和 archive，再考虑 long-term embedding。
- 默认禁止删除没有替代版本的 long-term summary。
- 输出 sanitized diagnostics，不打印 raw memory body 或 embedding blob。

最后一条尤其重要。记忆内容常常包含用户偏好、项目上下文、内部路径、甚至安全边界。一个 debug log 如果把整段 recalled memory block 打出来，记忆系统就从马具变成泄漏面。

```{admonition} 陷阱——记忆系统最常见的七种退化
:class: warning

1. **只记不忘。** 所有事情都 append，什么都不删除，最后召回结果里一半是旧世界。
2. **没有 key 的长期记忆。** 同一条规则被写成十个自然语言变体，召回时互相打架。
3. **把向量相似度当权威。** 相似不等于正确；长期规则必须能压过相似的短期噪声。
4. **规则只在数据库里。** 人类 review 看不到，PR diff 看不到，智能体却被它长期影响。
5. **无来源摘要。** 一条 memory 说"团队要求 X"，但没人知道 X 来自哪里。
6. **敏感内容进日志。** recall 失败时把整段 memory dump 到日志，隐私边界当场破裂。
7. **没有梳理 owner。** 记忆系统上线那天很漂亮，三十天后开始稳定误导智能体。

行级自测：随机抽十条长期记忆，能否为每条说出它的 `memory_key`、来源、上次验证时间、删除或覆盖规则？如果不能，这不是长期记忆，而是长期债务。
```

## 04.8 一条实用调试法：问记忆链路

当智能体"怎么又忘了"或"怎么还记着旧规则"时，不要先责怪模型。沿着记忆链路问七个问题：

1. 这条规则、最佳实践或陷阱有没有进入权威制品，例如 `AGENTS.md`、`SKILL.md`、ADR、PKB？
2. 它有没有被写入长期记忆，且有稳定 `memory_key`？
3. 写入时有没有 source、verified date、importance、tags？
4. 本轮任务的 query 或 prompt 装配是否会召回它？
5. 召回结果是否被更相似但更低权威的短期记忆压住？
6. 这条记忆是否已经 stale，却没有被 groom job 标出？
7. 若它影响了错误行为，哪一道护栏本该拒绝它？

这七个问题把"记忆"从神秘能力拆回工程流水线：写入、存储、召回、排序、装配、行动、复盘。能被拆开的东西，才配被驾驭。

## 研究脉络

- **RAG 与 Context Engineering** {cite}`lewis2020rag,karpathy2025context` 给本章提供了基本边界：记忆系统不是把所有历史塞进 prompt，而是选择、过滤、排序和压缩输入。
- **面向智能体的仓库入口** {cite}`agenticai2025agentsmd,anthropic2024claudecode` 是长期规则的权威位置。`AGENTS.md` 让规则能被多种客户端读取，`CLAUDE.md` 可以作为兼容镜像，而不应成为分叉真源。
- **MCP 与工具契约** {cite}`anthropic2024mcp` 提醒我们，记忆写入和召回都应当被视为工具面的一部分：参数、权限、错误、日志都需要契约。
- **Living Documentation** {cite}`martraire2019living` 是本章"记忆必须可梳理"的文档学底座。长期记忆若不能被验证和刷新，就会退化成长期误导。
- **Evolutionary Architecture** {cite}`ford2017buildingevolutionary` 支持把 memory groom job 看作适配函数：它不是事后清洁，而是系统能否持续适应变化的条件。

## 动手环节

本章的两份 hands-on 制品住在 `source/_handson/04-agent-memory-anatomy/`：

- `memory-layer-map.yaml` —— 一份五层 memory map，可直接拷进项目做设计检查。
- `memory-groom-checklist.md` —— 一份梳理检查表，专门检查规则、最佳实践、常见陷阱是否仍然可信。

```{literalinclude} ../_handson/04-agent-memory-anatomy/memory-layer-map.yaml
:language: yaml
```

```{literalinclude} ../_handson/04-agent-memory-anatomy/memory-groom-checklist.md
:language: markdown
```
