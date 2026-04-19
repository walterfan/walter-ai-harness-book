"""One-shot translator for Ch.12 Where We Go from Here."""
import polib

PATH = 'source/locale/zh_CN/LC_MESSAGES/chapters/12-where-we-go-from-here.po'
T = {}

T['Where We Go from Here'] = '从这里出发，往哪走'

T['*A book that does not end with a checklist is a book that does not expect to be used.*'] = \
    '*一本不以清单收尾的书，就是一本不打算被拿来用的书。*'

T['§12.1 — The Thesis in One Page'] = '§12.1 —— 一页纸上的立论'

T["The book's analytical spine fits onto one page: three guardians × four zones = twelve cells, each cell an artefact a team can ship. Every cell below is a `{ref}` link back into its Chapter 05 H3 subsection."] = \
    '本书的分析骨架，一页就装得下：三大护法 × 四区域 ＝ 十二格，每一格都是一件团队可以交付的制品。下表每一格都是一条 `{ref}` 链接，回指第 05 章里对应的 H3 小节。'

T['**Bridle** — steers before writing'] = '**缰绳** —— 在下笔之前先掰方向'
T['**Fence** — refuses bad work'] = '**护栏** —— 拒掉不合格的活'
T["**Paddock** — bounds the agent's roam"] = '**牧场** —— 圈定智能体能跑的范围'
T['**Groom** — tends the harness itself'] = '**梳理** —— 照看挽具本身'

T['**SDD**'] = '**SDD**'
T['{ref}`sdd-x-bridle`'] = '{ref}`sdd-x-bridle`'
T['{ref}`sdd-x-fence`'] = '{ref}`sdd-x-fence`'
T['{ref}`sdd-x-paddock`'] = '{ref}`sdd-x-paddock`'
T['{ref}`sdd-x-groom`'] = '{ref}`sdd-x-groom`'

T['**TDD**'] = '**TDD**'
T['{ref}`tdd-x-bridle`'] = '{ref}`tdd-x-bridle`'
T['{ref}`tdd-x-fence`'] = '{ref}`tdd-x-fence`'
T['{ref}`tdd-x-paddock`'] = '{ref}`tdd-x-paddock`'
T['{ref}`tdd-x-groom`'] = '{ref}`tdd-x-groom`'

T['**MDD**'] = '**MDD**'
T['{ref}`mdd-x-bridle`'] = '{ref}`mdd-x-bridle`'
T['{ref}`mdd-x-fence`'] = '{ref}`mdd-x-fence`'
T['{ref}`mdd-x-paddock`'] = '{ref}`mdd-x-paddock`'
T['{ref}`mdd-x-groom`'] = '{ref}`mdd-x-groom`'

T['All twelve `{ref}` links resolve to live subsections in Ch.05; a reader who clicks any one of them lands on a working artefact and a definition.'] = \
    '全部十二条 `{ref}` 链接都指向第 05 章中实打实的小节；读者点开任何一条，都会落在一件可用的制品与一则定义上。'

T['§12.2 — 30/60/90-Day Action Checklist'] = '§12.2 —— 30/60/90 天行动清单'

T["The book's single most important claim is that you do not need to adopt all twelve cells at once. You pick **one**, ship it, ship the *column* or the *row* it sits in, then run a full HarnessCard review. Below are the three sub-tasks with hands-on pointers; a standalone copy lives at `_handson/12-where-we-go-from-here/checklist-30-60-90.md`."] = \
    '本书最重要的那一条主张是：你 *不必* 把十二格一次性全采纳。你挑 **一格**、把它交付、再把它所在的那一 *列* 或 *行* 交付，然后跑一轮完整的 HarnessCard 评审。下面是这三个子任务，带 hands-on 指针；独立副本放在 `_handson/12-where-we-go-from-here/checklist-30-60-90.md`。'

T['Day 1–30 · One Cell'] = 'Day 1–30 · 一格'

T['Pick one matrix cell, ship one artefact for it, run it against the HarnessCard rubric from Appendix D.'] = \
    '挑一格矩阵单元，为它交付一件制品，再拿附录 D 的 HarnessCard 评分尺跑一遍。'

T['**SDD × Bridle.** Commit an `AGENTS.md` based on `_handson/05-harness-anatomy/sdd-x-bridle/AGENTS.md.sample`; ties into {ref}`sdd-x-bridle`.'] = \
    '**SDD × 缰绳。** 以 `_handson/05-harness-anatomy/sdd-x-bridle/AGENTS.md.sample` 为底，提交一份 `AGENTS.md`；与 {ref}`sdd-x-bridle` 相挂钩。'

T['**TDD × Fence.** Install a `PreToolUse` hook based on `_handson/05-harness-anatomy/tdd-x-fence/hooks.json`; ties into {ref}`tdd-x-fence`.'] = \
    '**TDD × 护栏。** 以 `_handson/05-harness-anatomy/tdd-x-fence/hooks.json` 为底，装一条 `PreToolUse` 钩子；与 {ref}`tdd-x-fence` 相挂钩。'

T['**MDD × Fence.** Adopt a per-session cost cap from `_handson/05-harness-anatomy/mdd-x-fence/cost-cap.yaml`; ties into {ref}`mdd-x-fence`.'] = \
    '**MDD × 护栏。** 采纳 `_handson/05-harness-anatomy/mdd-x-fence/cost-cap.yaml` 中那条"单次会话成本上限"；与 {ref}`mdd-x-fence` 相挂钩。'

T['Ford, Parsons & Kua {cite}`ford2017buildingevolutionary` supply the framing: one fitness function at a time is already a real improvement.'] = \
    'Ford、Parsons 与 Kua {cite}`ford2017buildingevolutionary` 提供了这件事的大框架：一次只上一条 fitness function，就已是一次真实的改进。'

T['Pitfall — The Day-30 "we are done" trap'] = '陷阱 —— 第 30 天 "我们搞完了" 的坑'

T['A team ships one cell by Day 30, celebrates, and stops. Ninety days later the cell has decayed — no Groom job was added, no review cadence was established, nobody owns the artefact. The +1 became +0.3 and is trending toward zero. **Why**: a single cell is a seed, not a crop. The Day-30 milestone exists to prove the team *can* ship a harness artefact; the Day-60 milestone exists to prove the team can *keep* one alive. Teams that skip the second milestone end the quarter with the same harness theatre they started with, minus a week of engineering time. **Fix**: the Day-30 exit criterion is not "artefact is merged" but "the artefact has an owner, a review cadence, and one refused or measured event in its log". An unused cell is a rehearsal, not a production.'] = \
    '一支团队在第 30 天交付了一格，庆祝、然后停下来。九十天之后，这格已经腐化——没有 Groom 任务被加上、没有评审节奏被建立、没有人署名持有这件制品。那个 +1 变成 +0.3，并在往 0 靠拢。**为什么**：单一格子是一粒种子，不是一茬庄稼。第 30 天的里程碑是为了证明这支团队 *能* 交付一件挽具制品；第 60 天的里程碑则是为了证明这支团队 *能让它活下来*。跳过第二个里程碑的团队，季末拿到的还是当初那场挽具剧场，只不过额外赔掉了一周工程师时间。**解法**：第 30 天的出口判据不是"制品已合并"，而是"这件制品有归属、有评审节奏、日志里至少有一次 refused 或 measured 事件"。没被用起来的格子是排练，不是演出。'

T['Day 31–60 · One Row or One Column'] = 'Day 31–60 · 一行，或一列'

T['Extend to a full row (one guardian across all four zones) or a full column (one zone across all three guardians).'] = \
    '扩展到完整一行（一位护法横跨全部四个区域），或完整一列（一个区域横跨全部三位护法）。'

T['**Full SDD row.** Ship Bridle + Fence + Paddock + Groom artefacts from `_handson/05-harness-anatomy/sdd-x-*/`. Cells {ref}`sdd-x-bridle`, {ref}`sdd-x-fence`, {ref}`sdd-x-paddock`, {ref}`sdd-x-groom`.'] = \
    '**完整 SDD 行。** 交付 `_handson/05-harness-anatomy/sdd-x-*/` 下的缰绳 ＋ 护栏 ＋ 牧场 ＋ 梳理 四件制品。对应格子：{ref}`sdd-x-bridle`、{ref}`sdd-x-fence`、{ref}`sdd-x-paddock`、{ref}`sdd-x-groom`。'

T['**Full Fence column.** Ship SDD + TDD + MDD fences from `_handson/05-harness-anatomy/*-x-fence/`. Cells {ref}`sdd-x-fence`, {ref}`tdd-x-fence`, {ref}`mdd-x-fence`.'] = \
    '**完整护栏列。** 交付 `_handson/05-harness-anatomy/*-x-fence/` 下的 SDD ＋ TDD ＋ MDD 三道护栏。对应格子：{ref}`sdd-x-fence`、{ref}`tdd-x-fence`、{ref}`mdd-x-fence`。'

T['**Operating drumbeat.** Adopt the weekly entropy audit (`_handson/06-operating-a-harness/entropy-audit.yml`) and the artefact state model (`_handson/06-operating-a-harness/artefact-state-model.yaml`); these harden the Groom row — {ref}`sdd-x-groom`, {ref}`tdd-x-groom`, {ref}`mdd-x-groom`.'] = \
    '**运行节拍。** 采纳每周熵审计（`_handson/06-operating-a-harness/entropy-audit.yml`）与制品状态机（`_handson/06-operating-a-harness/artefact-state-model.yaml`）；这两件一起，把"梳理"那一行夯实 —— {ref}`sdd-x-groom`、{ref}`tdd-x-groom`、{ref}`mdd-x-groom`。'

T["Forsgren, Humble & Kim's DORA-metrics work {cite}`forsgren2018accelerate` argues that a quarterly cadence is the right unit for measurement; day 31–60 is the second month of your first quarter."] = \
    'Forsgren、Humble 与 Kim 的 DORA 度量工作 {cite}`forsgren2018accelerate` 主张：季度节奏才是度量的合适单位；第 31–60 天就是你第一个季度的第二个月。'

T['Pitfall — The Day-60 "row or column?" paralysis'] = '陷阱 —— 第 60 天 "一行还是一列？" 的瘫痪'

T['A team reaches Day 31 with one cell shipped and spends the next three weeks in a committee debate: *row* or *column*? Which guardian? Which zone? By Day 60 no second artefact has shipped; the team reports "strategy work" in retro. **Why**: the row-or- column choice is optimisation theatre — either direction is a real improvement, and the wrong choice (if one exists) is recoverable in the next quarter. Time spent choosing is time not spent shipping. **Fix**: pick the direction whose *weakest cell* is the most embarrassing to name out loud. If you are ashamed to show a colleague your `AGENTS.md` today, ship the full SDD row; if your CI fails intermittently and nobody rotates the key that fixes it, ship the full Fence column. The embarrassment test resolves the paralysis in five minutes and picks the direction that was always going to matter most.'] = \
    '一支团队在第 31 天时已经交付了一格，接下来三周全耗在一场委员会辩论里：是 *一行* 还是 *一列*？哪位护法？哪一区域？到第 60 天，第二件制品一件都没出；团队在回顾会上汇报"战略工作"。**为什么**：一行或一列，本身是一场"优化剧场"——任一方向都是真实改进，而"错误选择"（如果真有的话）在下一个季度都可救。选择时花掉的时间，就是没有交付的时间。**解法**：挑那个 *最弱格子* 最让你不好意思当众说出口的方向。如果今天把 `AGENTS.md` 给同事看你会脸红，就上完整 SDD 行；如果 CI 时不时挂、却没人去轮换那把能修它的密钥，就上完整护栏列。这个"尴尬测试"能在五分钟内解开这场瘫痪，并挑出那个原本就最重要的方向。'

T['Day 61–90 · A Production HarnessCard Review'] = 'Day 61–90 · 一次生产级 HarnessCard 评审'

T['Run a full HarnessCard review on a production codebase using the blank template from Appendix D (see {ref}`apd-harnesscard-template`), land at least one harness-driven improvement, and record the measurable delta.'] = \
    '在一份生产代码库上，用附录 D 的空白模板（见 {ref}`apd-harnesscard-template`）跑一次完整 HarnessCard 评审，合入至少一项由挽具驱动的改进，并记录可度量的 delta。'

T['**Score.** Fill the twelve-cell blank HarnessCard at {ref}`apd-harnesscard-template` — every cell gets a 0–5 score and a one-line evidence note. Cross-check against {ref}`sdd-x-bridle`, {ref}`tdd-x-fence`, and {ref}`mdd-x-fence` using `_handson/11-lazy-ai-coder/HarnessCard-Act1.md` as a worked precedent.'] = \
    '**打分。** 把 {ref}`apd-harnesscard-template` 里那张十二格的空白 HarnessCard 填满 —— 每格给出 0–5 的分数与一行证据备注。用 `_handson/11-lazy-ai-coder/HarnessCard-Act1.md` 作为实例参考，跟 {ref}`sdd-x-bridle`、{ref}`tdd-x-fence` 与 {ref}`mdd-x-fence` 交叉核对。'

T['**Raise one cell.** Pick the lowest-scoring cell, land one fix scoped to it (a `make` target, a hook, a YAML, a script — see `_handson/11-lazy-ai-coder/reproduce.sh` for the worked pattern) and tie the fix back to the target cell (e.g. {ref}`mdd-x-paddock`).'] = \
    '**抬升一格。** 选得分最低的那一格，合入一项收束在这一格里的修复（一个 `make` 目标、一个钩子、一段 YAML、一段脚本 —— 以 `_handson/11-lazy-ai-coder/reproduce.sh` 为已跑通的样板），并把这项修复绑回它所针对的那一格（例如 {ref}`mdd-x-paddock`）。'

T['**Re-score and attach.** Author the post-fix HarnessCard using `_handson/11-lazy-ai-coder/HarnessCard-Act4.md` as a template, attach it to the release PR, and include a one-line delta note naming which cell moved (e.g. {ref}`sdd-x-groom`) and by how much.'] = \
    '**重评并挂载。** 用 `_handson/11-lazy-ai-coder/HarnessCard-Act4.md` 作模板，写出修复后的 HarnessCard，挂到发布 PR 上，并附一行 delta 备注：指名是哪一格在动（例如 {ref}`sdd-x-groom`）、动了多少。'

T["Lehman's evolution laws {cite}`lehman1980laws` explain why a quarterly re-score is not optional: unmaintained harnesses decay by default."] = \
    'Lehman 的演化定律 {cite}`lehman1980laws` 解释了"季度重评"为什么不是可选项：无人维护的挽具，默认就是会腐化。'

T['Pitfall — Three ways the Day-90 review goes wrong'] = '陷阱 —— 第 90 天评审会翻车的三种方式'

T['**Self-scored.** The engineer who shipped the fix also scores it; scores drift up +0.5 on average. *Fix*: the Day-90 scorer is not the Day-30 shipper.'] = \
    '**自打分。** 交付修复的那位工程师同时也是打分人；分数平均偏移 +0.5。*解法*：第 90 天的打分人，不能是第 30 天的交付人。'

T["**Inputs not outcomes.** Cell scores rise while DORA metrics don't. Every cell score must carry one outcome metric it is *predicted* to move (the Ch.11 *vanity delta* pitfall develops this in full)."] = \
    '**投入而非产出。** 格子得分在涨，DORA 指标却不动。每一项格子得分，都必须配一条它 *被预言要移动* 的产出指标（第 11 章的 *虚荣 delta* 陷阱对此做了完整展开）。'

T["**Raising the top, not the bottom.** The team lifts a 4 to a 5 instead of a 1 to a 2; the mean rises but the weakest load-bearing dimension doesn't. *Fix*: the Day-90 ritual must pick the lowest-scoring cell, even when a stronger cell is tempting."] = \
    '**抬高顶、不抬低底。** 团队把一个 4 抬成 5，而不是把一个 1 抬成 2；均值在升，承重最弱的那个维度却纹丝不动。*解法*：第 90 天的仪式必须去挑得分最低的那一格，哪怕更强的某一格更诱人。'

T['§12.3 — Open Questions'] = '§12.3 —— 悬而未决的问题'

T['At most seven directions where the book raises questions it does not answer. Each carries at least one citation that sketches the adjacent literature.'] = \
    '最多七个方向——在这些方向上，本书提出了自己并未回答的问题。每一条至少配一处引用，勾勒相邻文献。'

T['**Meta-harness versioning under multi-tenant LLM deployments.** How should harness rules survive a provider rolling out a model change mid-quarter, especially when customers share a tenant? {cite}`huyen2025aieng`.'] = \
    '**多租户 LLM 部署下的元挽具版本化。** 当供应商在季度中段推送模型变更、尤其当多个客户共享同一租户时，挽具规则该如何存活？{cite}`huyen2025aieng`。'

T['**When to migrate from blog-format `.md` context into a structured RAG pipeline.** Karpathy\'s context-engineering framing {cite}`karpathy2025context` bears on this but does not resolve it.'] = \
    '**何时把博客体 `.md` 上下文迁移到结构化 RAG 管道。** Karpathy 的 context engineering 定义 {cite}`karpathy2025context` 与此相关，但并没有给出答案。'

T['**HarnessCards for polyglot monorepos and cross-geography teams.** Does the 3 × 4 matrix survive scaling up the unit of analysis? {cite}`conway1968law`.'] = \
    '**多语言 monorepo 与跨地域团队的 HarnessCard。** 当分析单位被放大，这套 3 × 4 矩阵还扛得住吗？{cite}`conway1968law`。'

T['**Continuous vs milestone-level entropy measurement.** Can entropy reduction be measured continuously across a sprint, or is milestone measurement the highest useful resolution? {cite}`lehman1980laws`.'] = \
    '**连续型 vs 里程碑型熵度量。** 熵的下降能在一次 sprint 中被连续度量吗？还是说"按里程碑"就已经是最高有用分辨率？{cite}`lehman1980laws`。'

T['**Benchmarks that distinguish good harnesses from bad ones.** The Terminal-Bench 2.0 data point is suggestive but not settled {cite}`langchain2026tbench`.'] = \
    '**能把好挽具与坏挽具区分开的基准测试。** Terminal-Bench 2.0 提供了一个暗示性的数据点，但尚未成为定论 {cite}`langchain2026tbench`。'

T['**HarnessCard disclosure requirements for safety-critical agents.** Should regulators require HarnessCard-style disclosure the way they require SBOMs? {cite}`car2025decomposition`.'] = \
    '**安全关键型智能体的 HarnessCard 披露要求。** 监管机构是否应像要求 SBOM 一样，要求 HarnessCard 式披露？{cite}`car2025decomposition`。'

T['**The half-life of a skill.** How long does a `SKILL.md` keep its load-bearing value before prompt drift erodes it? {cite}`anthropic2024skills`.'] = \
    '**一项技能的半衰期。** 在 prompt 漂移把一份 `SKILL.md` 侵蚀掉之前，它还能承重多久？{cite}`anthropic2024skills`。'

T['§12.4 — What the book is *not* arguing'] = '§12.4 —— 本书 *并未* 主张的事'

T["A reader who has made it this far deserves the honest footnote on what this book's thesis does and does not claim."] = \
    '一位读到这里的读者，有资格拿到一则诚实的脚注——说明本书的主张所包含、以及 *不* 包含的东西。'

T['**Harnesses do not replace taste.** Nothing in the 3×4 matrix tells a team *which problem is worth solving*, which architecture to adopt, or when a `SKILL.md` is answering the wrong question. The harness constrains *how* the agent writes code; it does not originate *what* code is worth writing. Chapter 02\'s Stage-4 pitfall applies at the whole-book level.'] = \
    '**挽具不能替代品味。** 3×4 矩阵里没有一格会告诉一支团队 *哪个问题值得解决*、该采用何种架构、或某份 `SKILL.md` 在回答一个错问题。挽具约束的是"智能体 *怎样* 写代码"；它不产生"*什么* 代码值得写"。第 02 章 Stage-4 的陷阱，在整本书层面同样成立。'

T['**Not every team needs every cell.** The §03.5 *when not to use* section is not a rhetorical concession; a solo prototype, a throwaway script, or a frozen legacy system genuinely do not pay back the harness investment. A team adopting the twelve-cell discipline for a forty-line CSV parser is performing harness theatre whether they know it or not.'] = \
    '**并不是每支团队都需要每一格。** §03.5 的"何时不用"并不是一段修辞让步；独自做的原型、一次性的脚本、一套被冻结的遗留系统，的确不会偿还这份挽具投资。一支为了一段四十行 CSV 解析器就去采用十二格纪律的团队，无论自觉与否，都在上演一场挽具剧场。'

T['**The naming is not settled.** The four-zone vocabulary is practitioner-origin (§05.Provenance). If CAR {cite}`car2025decomposition` or LangChain\'s five-part anatomy {cite}`langchain2026tbench` fits your team better, use that framing and translate. The book\'s bet is on the *three-guardian × twelve-cell decomposition* as a Monday-morning planning tool, not on the zone names as a final taxonomy.'] = \
    '**命名并未板上钉钉。** 这份四区域词汇来自从业者（见 §05.Provenance）。若 CAR {cite}`car2025decomposition` 或 LangChain 的五部分解剖 {cite}`langchain2026tbench` 更适合你的团队，就用那一套框架，并做翻译即可。本书押注的是 *三大护法 × 十二格分解* 作为"周一早上可用的规划工具"，并未押注"这些区域名"成为终极分类法。'

T["**The pitfalls are not exhaustive.** The inline callouts name the failures the author has debugged, watched others debug, or read credible accounts of. They are a starting vocabulary, not a complete bestiary — §12.3 names where new failure modes are most likely to surface next."] = \
    '**那些陷阱并未穷尽。** 行内的 callout 只点出了作者自己调试过、看别人调试过、或读过可信记录的那些失败模式。它们是一份起步词汇表，不是一部完整异兽录——§12.3 指出了下一轮新失败模式最可能冒出来的地方。'

T["If this chapter's 30/60/90 checklist, the 3×4 matrix, and the pitfall vocabulary give your team one refused-commit event, one measured signal, and one revised `AGENTS.md` bullet in the next ninety days, the book has done its job."] = \
    '若本章的 30/60/90 清单、3×4 矩阵、以及这份陷阱词汇表，能在接下来九十天里给你的团队带来：一次被拒的 commit 事件、一条被度量的信号、一条被修订过的 `AGENTS.md` 条目——那本书的活儿就算干完了。'

T['Research Foundations'] = '研究脉络'

T['**DORA / Accelerate** {cite}`forsgren2018accelerate` — cadence and metric lineage for the 30/60/90 framing.'] = \
    '**DORA ／ Accelerate** {cite}`forsgren2018accelerate` —— 支撑 30/60/90 这一框架的节奏与度量谱系。'

T["**Lehman's laws** {cite}`lehman1980laws` — why the 90-day review must recur."] = \
    '**Lehman 定律** {cite}`lehman1980laws` —— 为什么 90 天评审必须周而复始。'

T['**Evolutionary architecture** {cite}`ford2017buildingevolutionary` — the fitness-function lineage for one-cell-at-a-time improvement.'] = \
    '**演化式架构** {cite}`ford2017buildingevolutionary` —— 支撑"一次一格"式改进的那条 fitness-function 谱系。'

T['Hands-On'] = '动手环节'

T['Two copyable artefacts live under `book/source/_handson/12-where-we-go-from-here/`:'] = \
    '在 `book/source/_handson/12-where-we-go-from-here/` 下，住着两份可直接拷走的制品：'

T['`checklist-30-60-90.md` — the checklist as standalone markdown ready to paste into a team wiki.'] = \
    '`checklist-30-60-90.md` —— 以独立 markdown 形式交付的这份清单，适合直接粘进团队 wiki。'

T['`open-questions.md` — the open-questions list as a standalone file researchers can cite.'] = \
    '`open-questions.md` —— 以独立文件形式交付的悬而未决问题清单，便于研究者引用。'


def main():
    po = polib.pofile(PATH)
    hit = 0
    miss = []
    for e in po:
        if not e.msgstr and not e.obsolete:
            if e.msgid in T:
                e.msgstr = T[e.msgid]
                hit += 1
            else:
                miss.append(e.msgid)
    po.save(PATH)
    print(f'translated {hit}; misses {len(miss)}')
    for m in miss[:10]:
        print('  MISS:', repr(m[:160]))
    po2 = polib.pofile(PATH)
    remaining = [e for e in po2 if not e.msgstr and not e.obsolete]
    print(f'remaining: {len(remaining)}')


if __name__ == '__main__':
    main()
