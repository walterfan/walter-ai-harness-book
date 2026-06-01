---
status: draft
chapter-type: narrative
---

# 什么是 Harness Engineering？

> *如果说第 01 章是动机、第 08 章是方法，那么本章就是一位怀疑者应当能在十五分钟内读完的词条解释。*

大多数读者不会按顺序读到这一章。有的人会从搜索引擎落到这里，有的人从一场大会的演讲，有的人从同事在 Slack 里发来的一个链接。他们先需要的是一件事：一份 **定义**——简明到可以被引用、辩护到可以被信赖、边界清晰到能与这个领域最常被混淆的另外五门学科区分开。本章在五小节里交付这份定义，之后是本书其余章节都要遵循的"研究脉络"和"动手环节"。

## 03.1 一句话定义

> **Harness Engineering（驾驭工程）是这样一门学科：有意识地设计、运行并演进环绕在 AI 编码智能体周围的那些结构，以使它所产出的软件具备可验证、可观测、可理解这三项属性。**

把这句话拆开读一遍。*有意识地设计*，拒绝了那种默认立场——认为不管提示词窗口里、IDE 里、CI 流水线里正好有什么，就已经是智能体的足够环境了。*运行并演进*，则是在说马具不是一次性架起来就完事的东西；熵会在一次次运行之间悄悄爬进来，没人伺候的马具会漂移成一堆过时的指令。*可验证、可观测、可理解*，点出了第 07 章要展开的"三大护法"——马具存在的目的就是为了保证这三项属性。句子的主语不是智能体；*围绕在它周围的那些结构* 才是。这一主语的翻转，就是这整门学科的全部。

## 03.2 操作性边界

马具是一组具体的、可以枚举出来的工程制品。只有当我们把这个集合里 *有什么* 和 *没有什么* 说清楚，这门学科才变得可操作。

### 马具 *是* 什么

- **提示词、技能，以及面向智能体的规约**——`AGENTS.md`（跨智能体的默认入口）、`CLAUDE.md`（兼容镜像或 symlink）、`SKILL.md`、MCP 服务器的 manifest，以及那些被当作纳入版本控制、可审阅的代码来对待的系统提示词 {cite}`agenticai2025agentsmd,anthropic2024claudecode,anthropic2024mcp`。
- **审批关卡与护栏**——pre-commit 钩子、lint 规则、PR 评审人、必过的 CI 检查，以及任何不论作者是谁（或是什么）都会拒绝坏制品的自动化 {cite}`humble2010continuousdelivery`。
- **一个沙箱**——容器、VM、受限文件系统，或临时 worktree——让智能体在其中操作，而不去碰生产环境 {cite}`car2025decomposition`。
- **写给智能体看的文档**——运维手册（runbooks）、架构决策记录（ADR）、以及智能体能独自读取、用来减少环境性幻觉的技能文件 {cite}`martraire2019living`。
- **度量与反馈面**——可观测的信号（测试通过率、每轮成本、lint 违规数、time-to-green）被写在一处、由团队每周复盘 {cite}`majors2022observability`。

### 马具 *不是* 什么

- **运行时推理栈。** 模型的 token 被如何调度到哪些 GPU 上，是基础设施的事，不是马具——那是 Huyen 意义上的 *AI Engineering* 的领地 {cite}`huyen2025aieng`。
- **ML 评测基准。** HELM、MMLU、Terminal-Bench 这一族度量的是智能体本身；它们是马具设计的 *输入*，而不是马具 {cite}`langchain2026tbench`。
- **IDE 插件面。** Cursor、Copilot、Windsurf 等等是消费马具的 *客户端*；马具住在仓库里，比任何一个具体的编辑器活得都长 {cite}`peng2023copilotstudy`。
- **智能体框架 SDK。** LangChain、AutoGen、CrewAI、LangGraph 提供的是多步智能体的构件；马具是团队在它所选框架 *外围* 写出来的东西 {cite}`langchain2026tbench`。
- **部署流水线。** 从已合并的 commit 到生产环境的那条路由 DevOps 负责；马具的职责边界，到"已合并的 commit"为止 {cite}`forsgren2018accelerate`。

归属判定很简单：一件制品塑造的是智能体在 commit 落地之前 *试图产出什么*，它就是马具；它塑造的是 commit 之后 *这个 commit 会被怎么对待*，它就是 DevOps；它塑造的是模型本身如何被服务化，它就是 AI Engineering。

有三种边界情形出现得足够频繁，值得明确走一遍；在这些情形下，上面这条归属判定很容易被误用。

- **一个 flaky 的 pre-commit 钩子。** 算不算马具？算——它在 commit 之前触发——但它是一件 *退化* 的马具制品，因为它丢掉了马具存在所要提供的那份属性。一道时灵时不灵的护栏，教会智能体（和人）一件事：这道护栏是可选的。一道 flaky 的护栏比没有护栏还糟，因为它同时背上了护栏的成本，却交不出护栏的杠杆。修好它的不稳定性，要么就把这条钩子删掉；不要留它半死不活。
- **一块没人看的仪表盘。** 算不算马具？不算——它在定义里 *"运行并演进"* 这半句上就过不了关。没有复盘节奏的埋点，属于可观测性基础设施，而不是 MDD。第 09 章的 *梳理（Groom）* 这一列，正是为了防止它落到这种退位状态。
- **一份挂在仓库顶部的长 `README.md`。** 算不算马具？只有当智能体每一轮都读它，它才算。主要写给新来的人看的 `README.md` 是文档；而一份智能体在会话开始时把前五十行加载进上下文窗口的 `README.md`（可以通过检查智能体的上下文转储来验证）才是马具。文件的名字不决定它归哪一类，*消费者* 决定它归哪一类。

花五分钟，把这条归属判定用在你自己的仓库上。大多数团队都会发现：他们马具里的 *某些* 东西被误归成了文档，而他们文档里的 *某些* 东西被当成马具来用——而这两坨，都没有被该管它们的那门学科好好伺候着。

## 03.3 相邻实践对照

这个领域有四个邻居。把它们混起来，是初次接触时最常见的错误——下面这张对照表就是用来提前化解这种混淆的。

```{list-table}
:header-rows: 1
:widths: 18 22 22 22 16

* - 学科
  - 范围
  - 主要制品
  - 主要失败模式
  - 与 Harness Engineering 的交叠
* - **DevOps** {cite}`humble2010continuousdelivery,forsgren2018accelerate`
  - 从已合并的 commit 到生产环境跑起来
  - 流水线定义、IaC、部署 manifest
  - 脆弱的发布、居高不下的平均恢复时间
  - 共享"审批关卡"这一心智；pre-commit 钩子与必过的 CI 检查是马具 *从* DevOps 工具箱里 *借来* 的制品
* - **MLOps** {cite}`sculley2015mltechdebt,huyen2025aieng`
  - 从数据集到可被调用的模型
  - 训练流水线、特征存储、模型注册表
  - 反馈回路和数据漂移里隐藏着的技术债
  - 共享"版本化"这一纪律；模型评估 harness 把 *信号* 喂给智能体马具，但它位于马具的上游
* - **AI／Agent Engineering** {cite}`huyen2025aieng,langchain2026tbench,anthropic2024agents`
  - 把基础模型组合成能用的应用，以及多步智能体
  - 提示词模板、chain、工具 schema、检索管道
  - 提示词脆弱、工具调用幻觉、无界的智能体循环
  - Harness Engineering 是它 *环境侧* 的对偶；agent engineering 造智能体，harness engineering 造智能体在其中运转的那个场
* - **Platform Engineering（平台工程）** {cite}`cncf2024platformeng`
  - 为产品团队抽象出基础设施的自助开发者平台（IDP）
  - 黄金路径、平台 API、内部开发者门户
  - 平台使用者的认知负担；平台与现实之间的漂移
  - 共享"铺好的路（paved road）"这种理念；一个成熟的 Harness Engineering 团队，最终会把自己的马具作为一款内部平台产品对外暴露
```

一行一行读这张表，能把这个领域的位置看清楚：Harness Engineering 坐在 AI／Agent Engineering（关心的是智能体）和 DevOps（关心的是部署）**之间**，从两边都借来了制品的模式，却哪一边都不归它管。

## 03.4 一个最小示例

搭一具马具不需要平台团队，也不需要预算。它需要的是三份文件，每份不到十行。下面这组三件套就是本书要求读者交付的最小完整马具——一份让智能体读的规约、一道智能体（和人）都绕不过去的护栏、一份由团队对外公开的可观测性回执。

### 片段 1 —— 让智能体读的那份规约（`AGENTS.md`）

```{literalinclude} ../_handson/03-what-is-harness-engineering/agents-md.fragment.md
:language: markdown
```

这里有三处选择很关键。规则 *少*（只有几条），因为比起长篇大论，智能体更可靠地尊重短的、可枚举的"家规" {cite}`anthropic2024claudecode`。每条规则都是 *机器可核验* 的（它点名一个文件、一条命令、一份配置），于是规约和关卡能对得上。而它采用 `AGENTS.md` 这个固定入口，是为了让 Codex、Cursor、Claude Code、Aider、Gemini CLI 等客户端共享同一份 onboarding 文件；若某个客户端仍偏好 `CLAUDE.md`，让它作为 symlink 或薄镜像指回这里即可 {cite}`agenticai2025agentsmd`。

### 片段 2 —— 人和智能体都绕不过去的那道护栏（`.pre-commit-config.yaml`）

```{literalinclude} ../_handson/03-what-is-harness-engineering/pre-commit-config.fragment.yaml
:language: yaml
```

pre-commit 是一道尽可能最小的 TDD 式关卡：它拒绝坏代码，不管作者是谁 {cite}`beck2002tdd`。ruff 钩子强制代码风格（否则智能体会在五种互相打架的风格之间幻觉出一种），而一个小小的 `pytest -m "not slow"` 钩子保证：没有一个 commit 可以在快通道还没跑绿的情况下落地。这就是第 07 章那条 *可验证性护法* 被压缩进十行里的样子。

### 片段 3 —— 可观测性回执（`harnesscard.yaml`）

```{literalinclude} ../_handson/03-what-is-harness-engineering/harnesscard.fragment.yaml
:language: yaml
```

HarnessCard 是由 CAR 分解那篇论文提出的一种标准化披露格式 {cite}`car2025decomposition`。它在 *一份可作为 commit 被审阅的文件* 里点明：这具马具用的是哪份规约、由哪道关卡强制执行、团队在看哪几路信号。它是一个尽可能最小的 MDD 面（第 07 章那第三条护法）：三行信号，已经足够起一个每周复盘的习惯。

把这三份加在一起的这三十行，已经满足了上面那句一句话的定义。它们是 *有意识设计* 的（不是偶然堆起来的）、是 *被运行和演进* 的（HarnessCard 自己就带着日期），并且明明白白点出了三大护法。任何一支有智能体参与的团队，都可以在一个下午把这一组三件套落地出来——它是一具马具，虽然初级，但真实。

```{admonition} 陷阱——长得像马具、其实不是马具的三份文件
:class: warning

一组 *看起来* 和上面那一组一模一样、却过不了归属判定的三十行三件套，其实容易得惊人。常见的退化形态有三种：

1. **愿望型的 `AGENTS.md`。** 规则被写成愿望——"写地道的 Go"、"倾向于清晰的命名"——没有任何钩子能机械地证伪这些话。智能体于是打出合规的信号、幻觉出自己在遵守。**判定**：每一条规则都必须点名一个文件、一条命令、一份配置。若一条都没有，这就是一份愿望清单，不是规约。
2. **永远能过的 pre-commit。** 一条钩子，拿 `pytest` 去跑一个测试数为零的套件，或者拿 `ruff` 去扫一个被排除掉的目录。它永远通过，而团队根本注意不到自己已经失去了这道护栏。**判定**：首次装上去时，这条钩子必须 *拒绝* 仓库里当前存在的某件制品（哪怕你接着就修掉了它）。从没说过一个 *不* 字的护栏，根本不是护栏。
3. **没有日期的 HarnessCard。** 一份 yaml，提交过一次之后就再也没人动过。信号列表还在，但整整一个季度，没有一路信号变过。**判定**：HarnessCard 必须带一个 `last_reviewed:` 日期，且这个日期不超过三十天；而每一次复盘都必须产出一条 delta 笔记。一份静态的 HarnessCard 是装饰品。

一具在工作的马具和"马具剧场"之间的分界，不在文件数——而在 *随便挑一个周二*，这三份文件中的每一份，能不能拿得出"它在最近拒绝过、量过、或引导过什么"的证据。如果一整个季度的答案都是"不能"，那即便它的内容一字未改，这组三件套也已经衰退成装饰了。
```

## 03.5 什么时候 *不* 用 Harness Engineering

Harness Engineering 和任何一门学科一样，都是有成本的：三份文件要维护、一个每周复盘的节奏、一张 HarnessCard 要更新。有三种情形，这份成本收不回来：

- **一次性的一次就扔的脚本。** 一段 40 行、解析完 CSV 就退出的脚本不是一个项目；它没有第二次 commit。马具的那份投入，摊不到一个永远不会到来的"第二次 commit"上。
- **完全不用 AI 的个人原型。** 如果一个开发者既没有、也不打算使用 AI 编码智能体，第 04–06 章依然可以作为传统软件工程卫生学来读，但 *马具* 这个标签在这里不帮任何忙——那个被"塑造环境"的"智能体"根本不存在。
- **任何 AI 智能体都不会碰的遗留代码。** 一个 2008 年的 COBOL 系统，已经处在变更冻结下，给它加一份 `AGENTS.md` 毫无收益；把精力花在 Feathers 的那套遗留代码手册上更值得 {cite}`feathers2004legacy`，直到哪天这套代码库带着 AI 重新进入活跃开发。

除此以外的所有情形——从一位独自搞副业、只用 Copilot 做自动补全的开发者，到五十个人跑着自主智能体的平台团队——03.4 那三十行三件套的成本，都低于没有它的成本。

## 研究脉络

03.1 里 Harness Engineering 的定义是 *有意* 构造得坐在几门已有学科之间，而不是另起炉灶；因此它的可信度靠的是一串边界引用，而不是哪一个"唯一源头"。

- **DevOps 基线。** Humble 与 Farley 的 *Continuous Delivery* {cite}`humble2010continuousdelivery`、Forsgren／Humble／Kim 的 *Accelerate* {cite}`forsgren2018accelerate`，合起来建立了一件事：一套"审批关卡"纪律可以在整个行业里被文化化地标准化。马具几乎是原样借走了他们这种以关卡为中心的立场，只是把它从 commit 的 *下游* 重新指向了 *上游*。
- **MLOps 基线。** Sculley 等人 *Hidden Technical Debt in Machine Learning Systems* {cite}`sculley2015mltechdebt`，是关于 ML 流水线里那些隐形粘合代码的经典警示；Huyen 的 *AI Engineering* {cite}`huyen2025aieng` 则把那份批评在"基础模型时代"里做了更新，也就是 03.3 里"AI 不等于马具"这一行背后真正的参考。
- **Agent Engineering 边界。** Anthropic 的 *Building Effective Agents* {cite}`anthropic2024agents` 与 LangChain 的 *Terminal-Bench 2.0* {cite}`langchain2026tbench`，是 2024–2026 年间关于"智能体是什么、该如何评估它"这个问题最常被引用的两份资料；两份都把智能体当成主语，把环境当成实现细节——而本书要翻转的，恰恰就是这个主语／宾语关系。
- **Platform Engineering 边界。** CNCF Platforms Working Group 的 *Platform Engineering Maturity Model* {cite}`cncf2024platformeng`，正是 03.3 里 Platform Engineering 那一行所借用的"铺好的路（paved road）"词汇背后的锚点。
- **Harness Engineering 第一手来源。** 立场论文中提出的 CAR 分解与 HarnessCard {cite}`car2025decomposition`、Fowler 首次为这项实践命名的 bliki 条目 {cite}`fowler2026harness`、OpenAI 在厂商一侧的表述 {cite}`openai2026harness`，以及 Thoughtworks 技术雷达中 trial 环的那条条目 {cite}`thoughtworks2026harness`——每当"Harness Engineering"这个名字本身需要被交叉引用时，本书用的就是这四份第一手参考。

## 动手环节

03.4 里那个最小示例，以三个片段的形式收在 `source/_handson/03-what-is-harness-engineering/` 目录下：

- `agents-md.fragment.md`——给智能体读的那份十行规约。
- `pre-commit-config.fragment.yaml`——那条拒绝坏 commit 的十行护栏。
- `harnesscard.fragment.yaml`——团队对外发布的那份十行可观测性回执。

配套的 `README.md` 给出了阅读顺序，以及每一份文件的意图。如果一位读者今天就只想 *开始* 实践 Harness Engineering，他把这三个片段拷进任何一个仓库，把文件名改一下，就可以启动第 09 章要正式化的那套 HarnessCard 每周复盘循环。
