---
status: draft
chapter-type: conclusion
---

# 从这里出发，往哪走

> *一本不以清单收尾的书，就是一本不打算被拿来用的书。*

## 12.1 —— 一页纸上的立论

本书的分析骨架，一页就装得下：三大护法 × 四区域 ＝ 十二格，每一格都是一件团队可以交付的制品。下表每一格都是一条 `{ref}` 链接，回指第 05 章里对应的 H3 小节。

```{list-table}
:header-rows: 1
:widths: 10 22 22 22 22

* -
  - **缰绳** —— 在下笔之前先掰方向
  - **护栏** —— 拒掉不合格的活
  - **牧场** —— 圈定智能体能跑的范围
  - **梳理** —— 照看马具本身
* - **SDD**
  - {ref}`sdd-x-bridle`
  - {ref}`sdd-x-fence`
  - {ref}`sdd-x-paddock`
  - {ref}`sdd-x-groom`
* - **TDD**
  - {ref}`tdd-x-bridle`
  - {ref}`tdd-x-fence`
  - {ref}`tdd-x-paddock`
  - {ref}`tdd-x-groom`
* - **MDD**
  - {ref}`mdd-x-bridle`
  - {ref}`mdd-x-fence`
  - {ref}`mdd-x-paddock`
  - {ref}`mdd-x-groom`
```

全部十二条 `{ref}` 链接都指向第 05 章中实打实的小节；读者点开任何一条，都会落在一件可用的制品与一则定义上。

## 12.2 —— 30/60/90 天行动清单

本书最重要的那一条主张是：你 *不必* 把十二格一次性全采纳。你挑 **一格**、把它交付、再把它所在的那一 *列* 或 *行* 交付，然后跑一轮完整的 HarnessCard 评审。下面是这三个子任务，带 hands-on 指针；独立副本放在 `_handson/12-where-we-go-from-here/checklist-30-60-90.md`。若你想直接把这套计划搬进团队会议，附录 F 的 {ref}`apf-engineer-playbook` 提供了一份更像工作手册的版本。

### Day 1–30 · 一格

挑一格矩阵单元，为它交付一件制品，再拿附录 D 的 HarnessCard 评分尺跑一遍。

- **SDD × 缰绳。** 运行 `agents-md-generate` 做一次 repo discovery，再以 `_handson/05-harness-anatomy/sdd-x-bridle/AGENTS.md.sample` 为底，提交一份 `AGENTS.md`；与 {ref}`sdd-x-bridle` 相挂钩。
- **TDD × 护栏。** 以 `_handson/05-harness-anatomy/tdd-x-fence/hooks.json` 为底，装一条 `PreToolUse` 钩子；与 {ref}`tdd-x-fence` 相挂钩。
- **MDD × 护栏。** 采纳 `_handson/05-harness-anatomy/mdd-x-fence/cost-cap.yaml` 中那条"单次会话成本上限"；与 {ref}`mdd-x-fence` 相挂钩。

Ford、Parsons 与 Kua {cite}`ford2017buildingevolutionary` 提供了这件事的大框架：一次只上一条 fitness function，就已是一次真实的改进。

```{admonition} 陷阱 —— 第 30 天 "我们搞完了" 的坑
:class: warning

一支团队在第 30 天交付了一格，庆祝、然后停下来。九十天之后，这格已经腐化——没有 Groom 任务被加上、没有评审节奏被建立、没有人署名持有这件制品。那个 +1 变成 +0.3，并在往 0 靠拢。**为什么**：单一格子是一粒种子，不是一茬庄稼。第 30 天的里程碑是为了证明这支团队 *能* 交付一件马具制品；第 60 天的里程碑则是为了证明这支团队 *能让它活下来*。跳过第二个里程碑的团队，季末拿到的还是当初那场马具剧场，只不过额外赔掉了一周工程师时间。**解法**：第 30 天的出口判据不是"制品已合并"，而是"这件制品有归属、有评审节奏、日志里至少有一次 refused 或 measured 事件"。没被用起来的格子是排练，不是演出。
```

### Day 31–60 · 一行，或一列

扩展到完整一行（一位护法横跨全部四个区域），或完整一列（一个区域横跨全部三位护法）。

- **完整 SDD 行。** 交付 `_handson/05-harness-anatomy/sdd-x-*/` 下的缰绳 ＋ 护栏 ＋ 牧场 ＋ 梳理 四件制品。若是 monorepo，同时明确"nearest `AGENTS.md` wins"：根文件只放全局命令与索引，子包文件只放局部命令与边界。对应格子：{ref}`sdd-x-bridle`、{ref}`sdd-x-fence`、{ref}`sdd-x-paddock`、{ref}`sdd-x-groom`。
- **完整护栏列。** 交付 `_handson/05-harness-anatomy/*-x-fence/` 下的 SDD ＋ TDD ＋ MDD 三道护栏。对应格子：{ref}`sdd-x-fence`、{ref}`tdd-x-fence`、{ref}`mdd-x-fence`。
- **运行节拍。** 采纳每周熵审计（`_handson/06-operating-a-harness/entropy-audit.yml`）与制品状态机（`_handson/06-operating-a-harness/artefact-state-model.yaml`）；这两件一起，把"梳理"那一行夯实 —— {ref}`sdd-x-groom`、{ref}`tdd-x-groom`、{ref}`mdd-x-groom`。

Forsgren、Humble 与 Kim 的 DORA 度量工作 {cite}`forsgren2018accelerate` 主张：季度节奏才是度量的合适单位；第 31–60 天就是你第一个季度的第二个月。

```{admonition} 陷阱 —— 第 60 天 "一行还是一列？" 的瘫痪
:class: warning

一支团队在第 31 天时已经交付了一格，接下来三周全耗在一场委员会辩论里：是 *一行* 还是 *一列*？哪位护法？哪一区域？到第 60 天，第二件制品一件都没出；团队在回顾会上汇报"战略工作"。**为什么**：一行或一列，本身是一场"优化剧场"——任一方向都是真实改进，而"错误选择"（如果真有的话）在下一个季度都可救。选择时花掉的时间，就是没有交付的时间。**解法**：挑那个 *最弱格子* 最让你不好意思当众说出口的方向。如果今天把 `AGENTS.md` 给同事看你会脸红，就上完整 SDD 行；如果 CI 时不时挂、却没人去轮换那把能修它的密钥，就上完整护栏列。这个"尴尬测试"能在五分钟内解开这场瘫痪，并挑出那个原本就最重要的方向。
```

### Day 61–90 · 一次生产级 HarnessCard 评审

在一份生产代码库上，用附录 D 的空白模板（见 {ref}`apd-harnesscard-template`）跑一次完整 HarnessCard 评审，合入至少一项由马具驱动的改进，并记录可度量的 delta。

- **打分。** 把 {ref}`apd-harnesscard-template` 里那张十二格的空白 HarnessCard 填满 —— 每格给出 0–5 的分数与一行证据备注。用 `_handson/11-lazy-ai-coder/HarnessCard-Act1.md` 作为实例参考，跟 {ref}`sdd-x-bridle`、{ref}`tdd-x-fence` 与 {ref}`mdd-x-fence` 交叉核对。
- **抬升一格。** 选得分最低的那一格，合入一项收束在这一格里的修复（一个 `make` 目标、一个钩子、一段 YAML、一段脚本 —— 以 `_handson/11-lazy-ai-coder/reproduce.sh` 为已跑通的样板），并把这项修复绑回它所针对的那一格（例如 {ref}`mdd-x-paddock`）。
- **重评并挂载。** 用 `_handson/11-lazy-ai-coder/HarnessCard-Act4.md` 作模板，写出修复后的 HarnessCard，挂到发布 PR 上，并附一行 delta 备注：指名是哪一格在动（例如 {ref}`sdd-x-groom`）、动了多少。

Lehman 的演化定律 {cite}`lehman1980laws` 解释了"季度重评"为什么不是可选项：无人维护的马具，默认就是会腐化。

```{admonition} 陷阱 —— 第 90 天评审会翻车的三种方式
:class: warning

**自打分。** 交付修复的那位工程师同时也是打分人；分数平均偏移 +0.5。*解法*：第 90 天的打分人，不能是第 30 天的交付人。

**投入而非产出。** 格子得分在涨，DORA 指标却不动。每一项格子得分，都必须配一条它 *被预言要移动* 的产出指标（第 11 章的 *虚荣 delta* 陷阱对此做了完整展开）。

**抬高顶、不抬低底。** 团队把一个 4 抬成 5，而不是把一个 1 抬成 2；均值在升，承重最弱的那个维度却纹丝不动。*解法*：第 90 天的仪式必须去挑得分最低的那一格，哪怕更强的某一格更诱人。
```

## 12.3 —— 悬而未决的问题

最多七个方向——在这些方向上，本书提出了自己并未回答的问题。每一条至少配一处引用，勾勒相邻文献。

- **多租户 LLM 部署下的元马具版本化。** 当供应商在季度中段推送模型变更、尤其当多个客户共享同一租户时，马具规则该如何存活？{cite}`huyen2025aieng`。
- **何时把博客体 `.md` 上下文迁移到结构化 RAG 管道。** Karpathy 的 context engineering 定义 {cite}`karpathy2025context` 与此相关，但并没有给出答案。
- **多语言 monorepo 与跨地域团队的 HarnessCard。** 当分析单位被放大，这套 3 × 4 矩阵还扛得住吗？{cite}`conway1968law`。
- **连续型 vs 里程碑型熵度量。** 熵的下降能在一次 sprint 中被连续度量吗？还是说"按里程碑"就已经是最高有用分辨率？{cite}`lehman1980laws`。
- **能把好马具与坏马具区分开的基准测试。** Terminal-Bench 2.0 提供了一个暗示性的数据点，但尚未成为定论 {cite}`langchain2026tbench`。
- **安全关键型智能体的 HarnessCard 披露要求。** 监管机构是否应像要求 SBOM 一样，要求 HarnessCard 式披露？{cite}`car2025decomposition`。
- **一项技能的半衰期。** 在 prompt 漂移把一份 `SKILL.md` 侵蚀掉之前，它还能承重多久？{cite}`anthropic2024skills`。

## 12.4 —— 本书 *并未* 主张的事

一位读到这里的读者，有资格拿到一则诚实的脚注——说明本书的主张所包含、以及 *不* 包含的东西。

- **马具不能替代品味。** 3×4 矩阵里没有一格会告诉一支团队 *哪个问题值得解决*、该采用何种架构、或某份 `SKILL.md` 在回答一个错问题。马具约束的是"智能体 *怎样* 写代码"；它不产生"*什么* 代码值得写"。第 02 章 Stage-4 的陷阱，在整本书层面同样成立。
- **并不是每支团队都需要每一格。** 03.5 的"何时不用"并不是一段修辞让步；独自做的原型、一次性的脚本、一套被冻结的遗留系统，的确不会偿还这份马具投资。一支为了一段四十行 CSV 解析器就去采用十二格纪律的团队，无论自觉与否，都在上演一场马具剧场。
- **命名并未板上钉钉。** 这份四区域词汇来自从业者（见 05.Provenance）。若 CAR {cite}`car2025decomposition` 或 LangChain 的五部分解剖 {cite}`langchain2026tbench` 更适合你的团队，就用那一套框架，并做翻译即可。本书押注的是 *三大护法 × 十二格分解* 作为"周一早上可用的规划工具"，并未押注"这些区域名"成为终极分类法。
- **那些陷阱并未穷尽。** 行内的 callout 只点出了作者自己调试过、看别人调试过、或读过可信记录的那些失败模式。它们是一份起步词汇表，不是一部完整异兽录——12.3 指出了下一轮新失败模式最可能冒出来的地方。

若本章的 30/60/90 清单、3×4 矩阵、以及这份陷阱词汇表，能在接下来九十天里给你的团队带来：一次被拒的 commit 事件、一条被度量的信号、一条被修订过的 `AGENTS.md` 条目——那本书的活儿就算干完了。

## 研究脉络

- **DORA ／ Accelerate** {cite}`forsgren2018accelerate` —— 支撑 30/60/90 这一框架的节奏与度量谱系。
- **Lehman 定律** {cite}`lehman1980laws` —— 为什么 90 天评审必须周而复始。
- **演化式架构** {cite}`ford2017buildingevolutionary` —— 支撑"一次一格"式改进的那条 fitness-function 谱系。

## 动手环节

在 `source/_handson/12-where-we-go-from-here/` 下，住着两份可直接拷走的制品：

- `checklist-30-60-90.md` —— 以独立 markdown 形式交付的这份清单，适合直接粘进团队 wiki。
- `open-questions.md` —— 以独立文件形式交付的悬而未决问题清单，便于研究者引用。
