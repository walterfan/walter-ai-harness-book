---
status: draft
chapter-type: methodology
---

# 马具解剖：三大护法 × 四区域

> *一个画不成表格的框架，是口号，不是分析工具。*

第 04 章论证了：任何一具能工作的马具，都必须按那个因果顺序扛住三位承重的护法——SDD、TDD、MDD。本章把这三位护法放到四条操作性的 **区域（zones）**——*缰绳（Bridle）*、*护栏（Fence）*、*牧场（Paddock）*、*梳理（Groom）*——上，得到一张 3 行 × 4 列的矩阵。这十二格，就是本书后续每一章都会回头指的那条分析脊梁。

在切入矩阵本身之前，05.*出处* 先把"四区域"这套词汇的来路讲清楚，也说清本书为什么仍然用它。想先看定义的读者，可以直接跳到 05.*全景*。

## 出处

"四区域"这个比喻——**缰绳（Bridle）**（在智能体动手写代码之前引导它的东西）、**护栏（Fence）**（不论作者是谁都会拒绝坏活的东西）、**牧场（Paddock）**（智能体可以自由走动的那片有界空间）、**梳理（Groom）**（让马具自身保持活着的那类反复发生的维护）——由本书作者在 2026-03-28 那篇博客《Harness Engineering: 给 AI 套上缰绳》中提出 {cite}`walterfan2026guardians`。它是一份 **实践者框架**，不是一份经过同行评议的分类学。有研究背景的读者应当把它当作教学脚手架来用，而不是当作这个领域已经尘埃落定的分解来用。

有三个相邻框架大致覆盖着同一片地图，值得拿来显式地做一次三点定位：

- **CAR 分解 ＋ HarnessCard 报告格式**——由立场论文 *Harness Engineering for Language Agents* 提出 {cite}`car2025decomposition`，把一具马具切分成 **Control（谁来决定运行什么）**、**Agency（智能体自行可以做什么）**、**Runtime（智能体代码所运行其上的那层底座）** 三部分，并把这份分解与一套标准化的 HarnessCard 披露格式配套。CAR 是本书首选的 *学术* 参考；第 07–11 章那几份案例研究 HarnessCard，最终都是以它为目标来序列化的。
- **Thoughtworks 的三段式框架** {cite}`thoughtworks2026harness` 把马具工作看作 *context engineering* ＋ *architectural constraints* ＋ *garbage collection*。这种框法在精神上更接近 DevOps，也是 05.*梳理* 背后"garbage collection"那股直觉最早的来路。
- **LangChain 的五段式智能体解剖** {cite}`langchain2026tbench` 在 Terminal-Bench 2.0 那篇博客里，列出 *prompts / tools / middleware / orchestration / runtime* 作为构件。LangChain 的框法以产品为中心（面向的是框架使用者），而本书的四区域以工作流为中心（面向的是下周要决定"把钱往哪投"的团队负责人）。

既然有了这三个相邻框架，为什么还保留 Bridle／Fence／Paddock／Groom？两个原因。第一，这四个区域 **能与任何一支工程团队已经在跑的工作流 1:1 对应**——我们本来就有代码评审人、CI 关卡、staging 环境、每周杂务清单；四区域只是把它们重新命名成一套把它们视为 *一等马具制品* 的词汇，而不是 DevOps 的附属品。第二，把四区域与 SDD／TDD／MDD 相乘，得到一个 **3 × 4 笛卡尔积**，十二个小格——每格都小到读者可以花一个下午为它交付一件制品。三分法（CAR）适合用来写一篇立场论文；十二格矩阵，则是周一早上被问到 *"下一步往哪投？"* 时你真正想要的那种东西。

比起 Bridle／Fence／Paddock／Groom 更愿意用 CAR 的读者，可以这样对一下：缰绳大致对应 CAR 的 Control；护栏和牧场合起来大致对应 CAR 的 Agency；梳理覆盖的则是 CAR 作为 Runtime 演进来处理的那类横切关切。本书全程使用四区域的命名，但从不声称它比 CAR 更优先；这份对照是一等公民，不是事后补做的。

## 05.全景 —— 3 × 4 矩阵

```{list-table}
:header-rows: 1
:widths: 10 22 22 22 22

* -
  - **缰绳（Bridle）**——在动笔之前引导
  - **护栏（Fence）**——拒绝坏活
  - **牧场（Paddock）**——划定智能体可以走动的范围
  - **梳理（Groom）**——伺候马具自身
* - **SDD**
  - [SDD × 缰绳](sdd-x-bridle)
  - [SDD × 护栏](sdd-x-fence)
  - [SDD × 牧场](sdd-x-paddock)
  - [SDD × 梳理](sdd-x-groom)
* - **TDD**
  - [TDD × 缰绳](tdd-x-bridle)
  - [TDD × 护栏](tdd-x-fence)
  - [TDD × 牧场](tdd-x-paddock)
  - [TDD × 梳理](tdd-x-groom)
* - **MDD**
  - [MDD × 缰绳](mdd-x-bridle)
  - [MDD × 护栏](mdd-x-fence)
  - [MDD × 牧场](mdd-x-paddock)
  - [MDD × 梳理](mdd-x-groom)
```

下面十二个 H3 小节——每格一节，按 **先 SDD 行、再 TDD 行、最后 MDD 行** 的固定顺序排列——是本章的主干。每一章案例研究（07–11）都以同样的十二格为坐标，给一具真实的马具打分。

关于这张矩阵 *应该怎么读*，先说一句。这十二格在分析上彼此独立（一个强壮的 TDD × 护栏并不意味着也会有一个强壮的 SDD × 梳理），但在 *操作* 上彼此耦合——强的格子会替弱的格子顶住一阵，弱的格子也会无声地拖垮强的格子。在读任何一行之前，有三种耦合值得先注意：

- **缰绳的弱，会被护栏的强放大出来。** 一份含糊的 `AGENTS.md`（SDD × 缰绳弱）搭配一条严苛的 pre-commit 钩子（TDD × 护栏强），会产出那种 *干净而错* 的代码：lint 过了、测试过了，而架构违反着规约从未钉住的那份意图。强壮的护栏让虚弱的缰绳看起来像没事——直到架构债在一场事故里浮出水面。
- **牧场的强，会掩盖缰绳的弱。** 一套扎实的 PR 评审仪式（SDD × 牧场强），在一份平庸的 `AGENTS.md` 下也能把团队扛上一年，因为每一次合并都靠评审人顶上来。一旦团队"扩评审人能力"的速度慢于"扩智能体产出"的速度，这份弱就暴露出来——而这永远会发生。
- **梳理是其他三列衰减的归宿。** 缰绳、护栏、牧场这三列上的每一格，默认都在贬值；梳理这一列存在的意义，就是把这份折旧偿还下去。一具梳理列为零的马具，不管开始时投入了多少，都会在两个季度内把其他三列的分数都拖回零。

读下面每一格时，把这种耦合放在心里：一个高分若没有兄弟格子陪着，并不耐用；没有哪一格能独自承重。

(sdd-x-bridle)=
### SDD × 缰绳 —— 引导智能体的规约

**定义。** 这一格里的缰绳，指的是智能体 *在动笔之前会先读* 的任何一份文件，它的首要目的是塑造"智能体试图去建什么"。`AGENTS.md`、`CLAUDE.md`、顶层的 `SKILL.md` 都住在这里；在多智能体团队里，`AGENTS.md` 应当作为 vendor-neutral 的 canonical 入口，`CLAUDE.md` 则作为兼容镜像或 symlink {cite}`agenticai2025agentsmd,anthropic2024claudecode`。一份没人读或已经过时的缰绳，什么也引导不了；因此这位护法的职责不止是让文件在场，更要让它保持新鲜。

`AGENTS.md` 的好版本像机场标识，不像整座城市：一两句项目定位、真实存在的 setup/test/lint/build 命令、关键目录、不能随手碰的 danger zones、以及通往更深知识库的链接。`agents-md-generate` 这个 skill 把这件事做成了可重复工作流：先发现仓库事实，再合并已有 `CLAUDE.md`／`.cursor/rules`／Copilot instructions，最后只生成一份能被验证的入口文件。

```{literalinclude} ../_handson/05-harness-anatomy/sdd-x-bridle/AGENTS.md.sample
:language: markdown
```

(sdd-x-fence)=
### SDD × 护栏 —— 在关卡处强制规约合法性

**定义。** 这一格里的护栏，强制每一件形如"规约"的制品，*在它变成权威之前* 就必须格式良好。例如：提示词模板在 commit 时被 JSON-Schema 校验、MCP manifest 的 schema 检查、CI 阶段拒绝包含未解析 `{ref}` 链接的文档构建 {cite}`martraire2019living`。没有这道护栏，规约的腐烂会无声累积，SDD × 缰绳就会沦为一句谎话。

```{literalinclude} ../_handson/05-harness-anatomy/sdd-x-fence/prompt-schema.json
:language: json
```

(sdd-x-paddock)=
### SDD × 牧场 —— 与规约相符的验收

**定义。** 这一格里的牧场，是一场有边界的 *评审仪式*，逐角色、逐行地确认"交付的工作与规约相符"。可执行规约 {cite}`adzic2011specbyexample` 是它的经典形态；lazy-scrum-team 的 *验证表（Verification Table）* 模式 {cite}`lazyscrumteam2026` 是本书全程采用的一个具体实例。

```{literalinclude} ../_handson/05-harness-anatomy/sdd-x-paddock/acceptance-gate.md
:language: markdown
```

(sdd-x-groom)=
### SDD × 梳理 —— 让规约面持续鲜活

**定义。** 这一格里的梳理动作，是一项 *反复运行的维护作业*，用来刷新规约面，以使智能体的输入永远不会悄无声息地腐烂。典型做法：扫坏链、重写过期的 `verified:` 头、重新跑一次 AGENTS.md 的仓库发现、核验里面列出的命令仍然存在、并更新 `last_updated` {cite}`ford2017buildingevolutionary`。没有梳理，SDD 的熵累积速度会快过作者跟得上的速度。

```{literalinclude} ../_handson/05-harness-anatomy/sdd-x-groom/update-docs.sh
:language: bash
```

```{admonition} 陷阱——SDD 行的失败模式
:class: warning

SDD 行的特异失败，不是规约 *缺席*，而是规约 *无法被证伪*。有两种按格子分的变体值得点名（第三种——"愿望型 `AGENTS.md`"，已经被第 03 章覆盖）：

- **比 handler 活得还久的 MCP manifest。** schema 里写着一个服务器早已不再实现的工具；智能体自信地调用它，得到一条莫名其妙的错误。SDD × 护栏正是为了抓这种失败而存在的，但前提是这道护栏 *两端* 都要被接上"schema－handler"契约的两头。
- **没有版本的规约。** 一份 `AGENTS.md`，没有 changelog、没有 `verified:` 日期、看不出被演进过。评审者判断不出里面的主张是当下的还是遗留的；智能体和人都把它当作权威来读。SDD × 梳理是答案——但前提是，当规约 N 周没被碰过时，这项梳理作业会大声失败。

行级自测：针对 SDD 的每一格，你都能点出今天仓库里对应的一件制品、以及一条若它坏掉会在 *本周之内* 触发的检查吗？哪一格的答案若是"我们相信大家会把它保持新鲜"，那无论那一格里的文件内容多好，它的分数都是零。
```

(tdd-x-bridle)=
### TDD × 缰绳 —— 先失败的测试作为给智能体的输入

**定义。** 这一格里的缰绳，是一份 *故意为红* 的测试套件，在智能体被请进来之前就先提交进仓库。智能体把这些失败的测试作为上下文的一部分读进来，从而明白 *在它动手写生产代码之前，必须把哪些测试变绿* {cite}`beck2002tdd`。关键性质是"commit 时是红的"，而不是"某处存在着一条测试"。

```{literalinclude} ../_handson/05-harness-anatomy/tdd-x-bridle/test_loop.py
:language: python
```

(tdd-x-fence)=
### TDD × 护栏 —— 拒绝红树 commit 的钩子

**定义。** 这一格里的护栏，会在测试树为红时拦住任何修改或 commit。pre-commit 钩子、Claude-Code 的 `PreToolUse` 钩子、以及必过的 CI 检查都属于这里 {cite}`humble2010continuousdelivery`。它和 TDD × 牧场的区别在于 *及时性*——TDD 护栏在键盘敲击那一刻就触发，TDD 牧场在 PR 那一刻才触发。

```{literalinclude} ../_handson/05-harness-anatomy/tdd-x-fence/hooks.json
:language: json
```

(tdd-x-paddock)=
### TDD × 牧场 —— CI 关卡与环境对等

**定义。** 这一格里的牧场，是一次 *必过、分支保护下* 的测试运行，发生在一个忠实于生产环境的环境中。它是 TDD × 护栏在集成层面上的孪生兄弟：覆盖更广、周转更慢、判决更权威 {cite}`forsgren2018accelerate`。

```{literalinclude} ../_handson/05-harness-anatomy/tdd-x-paddock/ci-gate.yml
:language: yaml
```

(tdd-x-groom)=
### TDD × 梳理 —— flake 维护与测试面演进

**定义。** 这一格里的梳理动作，是一套处理"不再承重的测试"的 *反复政策*——flake、早已消失的回归、以及与它当初所核验的那份规约脱节的测试。没有梳理，测试语料会不断累积死重，最终 *失去* 团队的信任 {cite}`cunningham1992debt`。

```{literalinclude} ../_handson/05-harness-anatomy/tdd-x-groom/flaky-test-quarantine.md
:language: markdown
```

```{admonition} 陷阱——TDD 行的失败模式
:class: warning

TDD 行的失败方式，跟 SDD 行不同，因为测试有一项不寻常的性质：一条失败的测试 *便宜*；而一条 *仍然通过、但已经与它核验的那份行为失联的测试*，比没有测试还糟。三种行级失败：

- **红却被忽略的测试。** 一条 flaky 测试每周失败一次；有人加了 `@pytest.mark.skip("flaky, fix later")`；那个"later"永远不会来。这条测试如今在消耗 CI 周期、污染输出，并教会团队"红是可以忽略的"——这恰恰是 TDD × 护栏存在目的的反面。如果一条测试被信任不到能挡住 commit 的程度，那它也配不上住在主测试套件里。把它挪进隔离区、署名指定一位 owner、写上日期，否则就删了。
- **绿且过期的测试。** 一条测试钉的是两个季度前产品需求早已移除的行为。没人注意到，因为它一直是绿的。一位在 TDD × 缰绳框架下读这条测试的智能体，如今学到的是一份 *错误的* 契约，然后照着它写新代码。绿本身不等于相关；梳理必须周期性地问：*每一条测试现在对应的是哪一条规约，那条规约还活着吗？*
- **那条从来没被写出来的敌意测试。** 那条人本 *应该* 写但没写的测试，正是能找出智能体捷径的那条。若 PR 里从不追加"再写一条专门攻击通向绿的最省力路径的测试"（参见第 04 章"第一把就过"那条陷阱），TDD × 牧场就会慢慢地 *训练* 智能体，而不是防它。

行级自测：AI 辅助的 PR 之后，你团队的"测试／LOC"比例 *上升* 了，还是没动？如果没动，那你正是在这条红—绿循环最便宜的时刻，对循环的测试一侧投入不足。
```

(mdd-x-bridle)=
### MDD × 缰绳 —— 真正在引导的那一个度量

**定义。** 这一格里的缰绳，是一条在生产流量打到系统上之前 *就已被命名* 的 *北极星度量*。其他的一切都是诊断性的。对一具 AI 编码马具而言，经典候选是：在一份固定基准套件上的 **智能体 mean turns to green**（平均变绿轮数）{cite}`langchain2026tbench`。

```{literalinclude} ../_handson/05-harness-anatomy/mdd-x-bridle/metrics-north-star.md
:language: markdown
```

(mdd-x-fence)=
### MDD × 护栏 —— 成本上限与熔断器

**定义。** 这一格里的护栏，是在"被观测到的成本、延迟、或错误率信号越过预先声明的阈值"那一刻的 *自动化拒绝*。LLM 调用上的成本上限、工具调用的限流、以及软／硬关闭开关都是典型做法 {cite}`majors2022observability`。

```{literalinclude} ../_handson/05-harness-anatomy/mdd-x-fence/cost-cap.yaml
:language: yaml
```

(mdd-x-paddock)=
### MDD × 牧场 —— 发布 SLI 与 staging 浸泡

**定义。** 这一格里的牧场，是一道 *发布关卡*：要求"等价于生产的信号"在一个有界的 staging 窗口里都达标，之后这批二进制才被允许毕业 {cite}`ford2017buildingevolutionary`。窗口本身是牧场；窗口边上的 SLI，则是这道护栏。

```{literalinclude} ../_handson/05-harness-anatomy/mdd-x-paddock/release-sli.md
:language: markdown
```

(mdd-x-groom)=
### MDD × 梳理 —— 每周度量审计与仪表盘卫生

**定义。** 这一格里的梳理动作，是一场 *每周对度量面本身的复盘*——哪些信号还在真正引导决策、哪些仪表盘已经没有 owner、哪些告警在没有 runbook 的情况下就会触发。Lehman 的演化律 {cite}`lehman1980laws` 对度量的适用度与对代码一样：没人维护的信号，会衰减成噪声。

```{literalinclude} ../_handson/05-harness-anatomy/mdd-x-groom/weekly-audit.sh
:language: bash
```

```{admonition} 陷阱——MDD 行的失败模式
:class: warning

MDD 行失败得比另外两行更安静，因为度量的衰减是 *渐近* 的：坏掉的测试会红、过期的规约会产出明显的矛盾，而一块正在衰减的仪表盘，只是变得越来越不管用。三种行级失败：

- **没人盯的北极星。** 一条度量被宣布承重、一块仪表盘被搭起来、一个阈值被设上——然后除了事故时以外没人看。信号在，但它不 *引导*；MDD × 缰绳这一格，有文件，有空椅子。**解法**：每一条北极星都必须有一位署名 owner，和每周一个议程格子，否则就把它降级为诊断度量。
- **没有绊线的成本上限。** 在 API 层配了一条成本上限，它从不触发。要么这条上限太松（它沉默地放行了回归），要么它紧到值得关心、却没人在它命中时被呼叫。MDD × 护栏若整整一个季度都没拒绝过任何东西，和"没有护栏"没有区别。
- **与现实脱节的 SLI。** staging 的 SLI 仍然在量端点的 P99，但产品上个季度转了向，真正的承重路径已经变成一个后台作业，而这条 SLI 恰好忽略了它的延迟。发布关卡一路都在过；回归照样上线。MDD × 牧场要求：每当产品的承重路径发生位移，SLI 就必须被重新审计——而智能体的速度，让这种位移变得 *更* 频繁，不是更少。

行级自测：针对 MDD 的每一格，你都能点出 *既有* 那条信号、*也有* 它在过去三十天内驱动的某一项具体决定吗？一条没有驱动任何决定的信号，是仪表盘上的一个像素，而不是一位护法。
```

## 研究脉络

这张矩阵的分析主张，靠五根可引用的支柱支着：

- **首要学术来源**：把 Harness Engineering 作为一门独立学科对待——CAR 分解与 HarnessCard 报告格式 {cite}`car2025decomposition`。
- **业界三点定位**：两份独立、非学术的框法——Thoughtworks 技术雷达的条目 {cite}`thoughtworks2026harness`、以及 LangChain 的五段式解剖 {cite}`langchain2026tbench`。
- **四区域的适配函数谱系**：Ford／Parsons／Kua 的 *Building Evolutionary Architectures* {cite}`ford2017buildingevolutionary` 提供了 *架构适配函数* 这套词汇——四区域把它做成了可操作的形式。
- **05.梳理 背后的演化律谱系**：Lehman 1980 年的软件演化律 {cite}`lehman1980laws`，是"为什么梳理列压根需要存在"这件事背后的底层理论。
- **四区域在 AI 时代诠释的实践者谱系**：作者本人 2026-03-28 那篇博客 {cite}`walterfan2026guardians`，以及 lazy-scrum-team 工作流仓库 {cite}`lazyscrumteam2026`。

## 动手环节

`source/_handson/05-harness-anatomy/` 下住着十二份制品，每格一份，按 `<guardian>-x-<zone>/<filename>` 的目录结构排布：

- **SDD 行：** `AGENTS.md.sample`（agents.md 风格样本）、`prompt-schema.json`、`acceptance-gate.md`、`update-docs.sh`
- **TDD 行：** `starter-tests/test_loop.py`（位于 `tdd-x-bridle/` 下）、`hooks.json`、`ci-gate.yml`、`flaky-test-quarantine.md`
- **MDD 行：** `metrics-north-star.md`、`cost-cap.yaml`、`release-sli.md`、`weekly-audit.sh`

每一份制品的内容都已内联渲染在上面各自的 H3 小节里；磁盘上的那份文件是唯一真源。想一格一格上线的读者，可以拷出任一份文件开始动手。本书在第 12 章的核心建议是：一支团队应当在 **60 天内上线完整的一行或完整的一列**——也就是三十天读本章，另外三十天交付四份制品。
