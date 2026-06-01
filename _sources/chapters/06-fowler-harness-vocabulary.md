---
status: draft
chapter-type: narrative
---

# 插章：Fowler 的 Harness 词汇 —— 两条正交轴与一份 Java 最小示例

> *别再追问"agent 用哪个模型"。先问一句：你给它修好回家的路了吗？*

第 03 章给出了驾驭工程的定义；第 07 章拆了记忆系统；第 08 章拆了 agent loop。本插章夹在第 08 章与第 10 章 SDD → TDD → MDD 三大护法之间，专门补一件事：**把 Martin Fowler 在 *Harness engineering for coding agent users* 里给这门学科留下的词汇，正式接进本书的术语表，并配一份能直接抄进 Java Web 项目的最小马具示例**{cite}`fowler2026harness`。

Fowler 这篇文章的贡献，不在于发明了什么新工具，而在于给"模型外面那一圈结构"凑齐了两条非常实用的正交轴：

- **Feedforward × Feedback**：按时间方向分，是 *事前引导* 还是 *事后反馈*。
- **Computational × Inferential**：按执行方式分，是 *机器能确定算出来* 还是 *要靠模型语义判断*。

外加一个用来评估"这份代码库到底好不好拴"的形容词：**Harnessability**。

这三个词在本书前两章已被默默使用，但没有正式登台。本插章把它们摆上桌面，并指出本书三大护法 × 四区域矩阵和 Fowler 这套词汇之间的精确对应。

## 06.1 LangChain 公式：Agent = Model + Harness

LangChain 在 *The Anatomy of an Agent Harness* 里把这件事压成一行公式：**Agent = Model + Harness**{cite}`langchain2026anatomy`。

公式很简短，但它一次性回答了两个常被混为一谈的问题：

- "我用什么模型？" —— 那是 Model 那一侧的事。
- "我用模型来干什么、它能看到什么、它做错了我怎么知道？" —— 那是 Harness 那一侧的事，也是本书唯一关心的那一侧。

这个公式把"换更强的模型"和"搭更好的马具"区分开。前者是供应链问题，后者是工程问题。一个能干的工程团队不该把所有希望都押在前者上 —— LangChain 自己在 Terminal-Bench 2.0 上的那次实验给出了一份单项最强的经验证据：只换马具、不换模型，他们的智能体从 52.8 % 抬到了 66.5 %，从 Top-30 层一路冲进 Top-5{cite}`langchain2026tbench`。

裸模型像一个聪明却没读过你们代码的新人。它能写代码，可它不知道哪几个目录碰不得、哪条接口背着历史包袱、哪条慢测试其实是上次事故留下的疤。Harness 做的事，就是把这些隐性约束写出来、摆到智能体伸手可及的地方，并在它走偏时及时把它叫停。

## 06.2 第一条轴：Feedforward × Feedback

把控制手段按 *时间方向* 分成两类，是 Fowler 这篇文章里最朴素也最好用的一刀。

- **Feedforward —— 事前引导**。agent 动手 *之前*，先告诉它该往哪走、什么风格是对的、哪些边界不能碰。
  典型制品：`AGENTS.md`、项目规则、`SKILL.md`、架构原则、安全开发要求、"怎么启动、怎么跑测试、怎么提交"的 skill。

- **Feedback —— 事后反馈**。agent 动手 *之后*，观察结果，让它自我修正。
  典型制品：单元测试失败、lint 报错、类型检查失败、架构边界测试失败、AI reviewer 指出"这里的修复只是掩盖症状"。

两者缺一不可，理由是对称的。

只有 feedback、没有 feedforward，agent 像一个总被老师批改作业、却从不听课的学生 —— 它能改错，但同样的错会反复出现。只有 feedforward、没有 feedback，则像把规章制度贴满墙、却没人检查执行情况 —— 看起来很严谨，落地全靠运气。工程上真正有用的是一个小循环：**先引导，再检查；检查出问题，再改进引导**。别让同一个坑反复绊倒同一个 agent。

这条轴和本书第 10 章的三大护法是直接对应的：

- **SDD（规约驱动开发）天然属于 Feedforward** —— 它在 agent 动手前钉稳"该建什么"。
- **TDD（测试驱动开发）天然属于 Feedback** —— 测试在 agent 动手后判定"建成的是不是想要的"。
- **MDD（度量驱动开发）兼具两面** —— 度量本身是 Feedback，但 *根据度量调整规约与测试* 是下一轮的 Feedforward。

## 06.3 第二条轴：Computational × Inferential

Fowler 的第二条轴按 *执行方式* 分类，回答的是另一个问题：这道检查是 *算* 出来的，还是 *猜* 出来的？

- **Computational —— 确定性、机器能快速算出来**：测试、lint、type checker、静态分析、架构规则检查、依赖扫描、SAST、secret scan。
- **Inferential —— 需要语义判断**：AI code review、"这是不是过度设计"、"这个测试是不是只测了实现没测行为"、"这段代码虽然能跑但是否符合团队习惯"。

老工程师都知道一条朴素经验：**能用确定性工具解决的问题，不要轻易交给玄学**。

不是说 LLM 不好，而是 *成本与可靠性* 不同。一个 type checker 几秒就能告诉你类型不对，且不会今天说错、明天说对；AI reviewer 能看出更高层次的问题，但它慢、贵，偶尔还会一本正经地胡说八道。请专家会诊很有价值，但你不能让专家每天帮你量体温。

健康的做法因此是：

- 快、便宜、确定的检查，尽量前置到 *本地、pre-commit、agent 工作循环* 里；
- 慢、贵、需要语义判断的检查，放到更合适的位置 —— MR review、nightly job 或关键变更前；
- 不要让 agent 只靠自己"感觉良好"，要给它能 *读懂、能执行、能修正* 的信号。

这其实是传统软件工程 *shift left* 的老道理 {cite}`humble2010continuousdelivery`，只是现在多了一个新角色：coding agent。

## 06.4 两条轴一起看：一张 2 × 2

把这两条轴正交起来，就得到一张能直接拿去和团队对照的 2 × 2：

```{list-table}
:header-rows: 1
:widths: 20 40 40

* -
  - **Computational（机器算）**
  - **Inferential（模型判）**
* - **Feedforward（事前）**
  - schema、JSON schema、OpenAPI、`AGENTS.md` lint、prompt schema 校验
  - 规则审阅、skill 设计评审、约束自然语言化、产品验收样例
* - **Feedback（事后）**
  - 测试、lint、type check、ArchUnit、SAST、secret scan、mutation testing
  - AI code review、PR 评审、"是否解决根因"判断、产品验收
```

这张表的实用价值，在于它能立刻暴露团队的 *偏科*。

绝大多数团队的左下格（Computational × Feedback）发育得最好 —— 那是 CI/CD 时代的遗产。右下格（Inferential × Feedback）是过去两年 AI reviewer 类工具发力的地方。左上格（Computational × Feedforward）经常被忽视：`AGENTS.md` 没有 lint、prompt 没有 schema、skill 没有 precondition hook。右上格（Inferential × Feedforward）最难也最值钱，需要团队把 *老工程师脑子里的隐性约束* 显性化成自然语言并写进规约 —— 这正是第 10 章 SDD 那一节要展开的话题。

## 06.5 三类 Harness：Maintainability、Architecture Fitness、Behaviour

Fowler 还按 *约束对象* 把 harness 分成三类，这组分法可以直接对应到本书第 11 章马具矩阵的三行。

- **Maintainability Harness**：关注代码可维护性 —— 重复、复杂度、覆盖率、风格一致性、死代码、依赖风险。起步最容易，工具最成熟，agent 反馈循环也最直接。它的边界是：能告诉你 *"这个函数太复杂"*，却不一定能告诉你 *"你修错了问题"*。
- **Architecture Fitness Harness**：关注系统是否还保持在我们想要的架构方向上 —— 模块边界有没有被穿透、API 层有没有偷调数据库、日志是否符合可观测性要求、性能预算有没有被破坏、安全规则有没有被绕开。Thoughtworks 早年提出的 **Architectural Fitness Function** 在 agent 时代反而更值钱 {cite}`thoughtworks2026fitness`，因为 agent 写代码很快，**漂移也可能更快** —— 以前是人慢慢把系统写歪，现在是 agent 可以很勤快地帮你写歪。
- **Behaviour Harness**：最难。代码能编译、测试也绿，并不代表它真的满足业务需求 —— 尤其当测试本身也是 agent 写的时候。它可能写一组"自证清白"的测试，看起来覆盖率很漂亮，实际上只是证明它自己的实现符合它自己的想象。当前比较现实的做法是：人类给清晰功能规格、用 approved fixtures 把关键输入输出固化、用端到端测试验证用户可见行为、对 AI 生成测试再做 mutation testing、保留必要的人工验收。

一句话：**行为 harness 还远没成熟。谁说 "agent 已经可以完全替代工程师做需求实现"，多半是还没被线上 bug 结结实实教育过**。

## 06.6 Harnessability：不是所有代码库都一样好"拴"

Fowler 还给出一个评估代码库底子的形容词：**Harnessability**。

不是每个代码库都同样适合被 harness 管起来：

- 强类型语言天然有 type checker；
- 清晰模块边界更容易写架构测试；
- 成熟框架能减少 agent 需要操心的细节。

反过来，一个 *历史包袱很多、结构松散、测试稀薄* 的老系统，**最需要 harness，也最难搭 harness**。这听起来有点残酷，但很真实。

新项目可以从第一天就把 harnessability 当作设计目标：语言、框架、目录结构、测试策略、服务模板，都围绕"未来如何让人和 agent 都不容易犯错"来设计。

老项目则要务实一点。别一上来就想着"全自动智能体开发平台"，先找最疼、最常见、最容易自动化的几个点下手：

- agent 总改错目录？补项目结构说明。
- agent 总忘记跑测试？加本地检查脚本。
- agent 总违反分层？加架构测试。
- agent 总写不合规日志？加 lint 或 review skill。
- agent 总误解任务？改需求模板和验收用例。

**先把重复踩的坑填上**，再谈 platform 化。

## 06.7 一张最小可用 Harness 清单

如果明天就想给团队的 coding agent 加一点约束，这张表足够开工。它不高级，胜在能抄。

```{list-table}
:header-rows: 1
:widths: 22 39 39

* - 场景
  - Feedforward：先告诉它
  - Feedback：做完后检查
* - 新人式迷路
  - 项目结构、启动方式、常用命令
  - smoke test、构建脚本
* - 风格不一致
  - 编码规范、命名习惯、日志规则
  - lint、format、review skill
* - 分层被破坏
  - 架构边界说明、允许依赖列表
  - ArchUnit、import boundary check
* - 测试偷懒
  - 测试策略、验收标准、fixture 规则
  - coverage、mutation testing、人工抽查
* - 安全问题
  - 安全基线、敏感字段规则、权限模型
  - SAST、secret scan、日志隐私检查
* - 任务误解
  - 清晰需求模板、反例、验收样例
  - E2E test、QA review、产品验收
```

工程上很多事都是这样：**先别追求"智能"，先追求"不犯傻"**。

## 06.8 一个 Java Web 项目的最小 harness

光说概念容易飘。下面以一个常见的 Java Web 后台为例 —— Spring Boot + Maven + Controller / Service / Mapper 分层，入口是 HTTP API，后面连数据库和外部服务 —— 把上面四节具体化。

这个项目的风险边界大致如下：外部请求从 Controller 进来，参数可能不可信；Service 承担业务规则和事务边界；Mapper 访问数据库，不能拼接 SQL；日志里不能泄露 token、手机号、邮箱、订单明细等敏感信息；权限检查不能只靠前端"自觉"。这些话如果只在老工程师脑子里，**agent 不会自动知道**。

一个最小可用的 harness 看起来是这样：

```text
my-order-service/
├── AGENTS.md
├── docs/ai/index.md
├── docs/ai/architecture.md
├── docs/ai/api-contracts.md
├── scripts/agent-check.sh
├── src/main/java/com/example/order/
│   ├── controller/
│   ├── service/
│   └── mapper/
├── src/test/java/com/example/order/architecture/LayeringTest.java
└── src/test/resources/fixtures/order-create-success.json
```

这套结构在 Fowler 的四象限里站位非常清晰：

- `AGENTS.md` —— Inferential × Feedforward（自然语言规约 + 安全开发要求）。
- `scripts/agent-check.sh` —— Computational × Feedback（让 agent 每次改完都有一条确定可执行的验证路径）。
- `LayeringTest.java`（ArchUnit）—— Computational × Feedback，专门约束 *架构漂移*。
- `order-create-success.json`（approved fixture）—— Inferential × Feedforward（人类确认过的验收样例）+ Computational × Feedback（自动化测试运行它）。

下一章（第 10 章）会把这四件制品按 SDD / TDD / MDD 重新归位；本插章的目的只是先把它们 *摆到桌上* 让人看到。

### Feedforward：把规则写给 agent 看

`AGENTS.md` 不必写成公司制度汇编，太长了 agent 也容易抓不住重点。完整可抄的模板在 hands-on 制品里，下面只贴最关键的三段：

- **Architecture** —— 钉死 Controller → Service → Mapper 的方向，DTO 不能暴露 entity，SQL 一律 `#{}` 绑定不得 `${}` 拼接。
- **Security** —— 全部参数校验、授权检查留在 service / controller 边界、日志禁止泄露敏感字段。
- **Before Finishing** —— 一行命令 `./scripts/agent-check.sh`，把"请自行验证"翻译成 *一条确定可执行的路径*。

这段文字的作用不是"教育 AI 要做个好人"，而是 *把团队最在意的约束前置*。分层、SQL、安全、日志一旦错了，review 时再骂 agent 也没用。

### Feedback：给 agent 一个能跑的检查脚本

`scripts/agent-check.sh` 把"agent 改完后该跑什么"写成一条命令。重点不是工具名字，而是 **把"请自行验证"变成一条确定可执行的路径** —— 否则 agent 很容易写一句 *"建议运行测试"* 然后心安理得地收工。

### Architecture Fitness：用 ArchUnit 防止分层漂移

分层规则不能只写在文档里，最好变成测试。ArchUnit 一条 layered architecture 断言，就能让 agent 在 Controller 里偷懒调用 Mapper 时立刻见红，**不必等到人工 review**{cite}`thoughtworks2026fitness`。完整测试源码在 hands-on 制品里。

### Behaviour Harness：用 approved fixture 固化关键行为

行为正确性最难，尤其不能完全相信 agent 自己写的测试。一个实用办法是：*关键输入输出由人先给 approved fixture，agent 可以写实现和补测试，但不能随便改 fixture*。配套规则写进 PR 模板：

- fixture 是人类确认过的验收样例，agent 不得为了让测试通过而修改它；
- 新增行为可以新增 fixture，但要说明业务含义；
- 修改 fixture 必须在 PR 描述里单独解释。

否则 agent 有时会走一条很"聪明"的捷径：**实现不对，就改测试；测试还不对，就改期望值。代码绿了，需求黄了**。

### PR/MR 前的 Harness Gate

最后，把这些检查放进流水线：

```{list-table}
:header-rows: 1
:widths: 26 44 30

* - Gate
  - 目的
  - 失败后谁处理
* - `mvn test`
  - 验证单元测试和架构测试
  - agent 先修
* - `checkstyle` / `spotbugs`
  - 抓风格、空指针、资源释放等问题
  - agent 先修
* - dependency / secret scan
  - 抓依赖漏洞和误提交密钥
  - 人和 agent 一起看
* - AI Review
  - 看是否过度设计、误解需求、测试自嗨
  - 人类 reviewer 复核
* - 人工 Review
  - 做最终语义判断和业务取舍
  - 人负责
```

这就是一个 Java Web 项目的小型 harness：事前有规则、事后有检查、中间有测试、最后有人把关。一句话：**让 agent 写代码之前，先给它修一条能回家的路**。

```{admonition} 陷阱——把 Fowler 词汇用歪的七种姿势
:class: warning

1. **只做 Feedback，不做 Feedforward。** 规则全靠 review 现场口头传，agent 永远第一次犯。
2. **只做 Feedforward，不做 Feedback。** 规则贴满 `AGENTS.md`，但没人检查 agent 是否真的遵守。
3. **把所有判断都交给 Inferential。** 能用 type checker 几秒搞定的事，非要让 AI reviewer 慢慢猜。
4. **把所有判断都交给 Computational。** 拒绝引入语义判断，于是"过度设计""测试自嗨"永远漏过。
5. **`AGENTS.md` 写成公司制度汇编。** 几千字、十几个章节，agent 抓不住重点，人也懒得维护。
6. **`scripts/agent-check.sh` 不存在或时灵时不灵。** agent 学会的第一件事是 *这道检查可以绕过*。
7. **approved fixture 让 agent 自己写。** 验收样例变成 agent 自我证明的工具，行为 harness 当场失效。

行级自测：随便挑一道你最近加给 agent 的约束，能不能立刻说出它落在 2×2 的哪一格？如果不能，这条约束多半还停留在"愿望"，没成为马具。
```

## 06.9 一条调试法：问 harness 链路

当 agent "怎么又改错了"或"怎么还在踩同一个坑"时，不要先责怪模型。沿着 harness 链路问七个问题：

1. 这条约束有没有进入 Feedforward 制品（`AGENTS.md`、`SKILL.md`、ADR、PKB、prompt schema）？
2. agent 真的会在动手前读到它吗（context window、skill 触发条件、`AGENTS.md` 入口）？
3. 这条约束有没有 Computational Feedback 对应物（测试、lint、type check、ArchUnit）？
4. 该 Feedback 是否被前置到 *agent 工作循环* 而不是 *MR review*？
5. 这条约束的 Inferential Feedback（AI review、人工 review）是否触发？
6. 如果以上都触发了 agent 还是错，问题是否在 *规约本身含糊*（即第 10 章 SDD 的责任）？
7. 是否需要把这条约束从 Inferential 升格为 Computational（写成 schema、lint、测试）？

这七个问题把"agent 又出错了"从神秘事件拆回工程流水线：*Feedforward 是否到位、Feedback 是否触发、Computational 是否优先于 Inferential*。**能被拆开的东西，才配被驾驭**。

## 研究脉络

- **Fowler 给这门学科命名。** *Harness engineering for coding agent users* 是把 Feedforward × Feedback 与 Computational × Inferential 这两条轴系统化提出的来源 {cite}`fowler2026harness`。本书第 02 章已经用它做过 2026 年的坐标桩；本插章则把这套词汇正式接进 Part 2 的术语表。
- **LangChain 的公式与单项证据。** *Anatomy of an Agent Harness* 给出 `Agent = Model + Harness` 的公式 {cite}`langchain2026anatomy`；Terminal-Bench 2.0 的"只换马具"实验则提供了目前最强的一份单项经验证据 {cite}`langchain2026tbench`。
- **Anthropic 与 OpenAI 的厂方实践。** 两家厂商各自给出 *长任务 agent harness* 与 *Codex 在 agent-first world 的 harness 工程* 的工程报告 {cite}`anthropic2026longharness,openai2026harness`，是把本插章 2 × 2 落到生产强度的两份外部参考。
- **Architectural Fitness Function。** Thoughtworks 雷达把架构约束自动化的实践 {cite}`thoughtworks2026fitness`，给本插章 06.5 节的 Architecture Fitness Harness 行提供了原始词汇。
- **Continuous Delivery 与 shift left。** Humble 与 Farley 关于"越便宜越确定的检查越要前置"的论证 {cite}`humble2010continuousdelivery`，是本插章 06.3 节那条 Computational > Inferential 原则的工程史背景。

## 动手环节

本插章的四件 hands-on 制品住在 `source/_handson/06-fowler-harness-vocabulary/`，分别对应 06.8 节四象限里的四件马具：

- `AGENTS.md.template` —— Inferential × Feedforward 的入口文件模板，可直接拷进项目改 `{{...}}` 占位符。
- `agent-check.sh` —— Computational × Feedback 的最小检查脚本，可换成项目实际命令。
- `LayeringTest.java` —— Computational × Feedback 的 Architecture Fitness Function，钉死 Controller → Service → Mapper 边界。
- `order-create-success.json` —— Inferential × Feedforward + Computational × Feedback 的 approved fixture 样例。

```{literalinclude} ../_handson/06-fowler-harness-vocabulary/AGENTS.md.template
:language: markdown
```

```{literalinclude} ../_handson/06-fowler-harness-vocabulary/agent-check.sh
:language: bash
```

```{literalinclude} ../_handson/06-fowler-harness-vocabulary/LayeringTest.java
:language: java
```

```{literalinclude} ../_handson/06-fowler-harness-vocabulary/order-create-success.json
:language: json
```
