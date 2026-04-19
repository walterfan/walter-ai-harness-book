"""One-shot translator for Ch.05 Harness Anatomy .po file.

Writes Chinese msgstrs for all untranslated entries. This script is a
throwaway helper used during the book's translation phase.
"""
import polib

PATH = 'source/locale/zh_CN/LC_MESSAGES/chapters/05-harness-anatomy.po'

T = {}

T['Harness Anatomy: Three Guardians × Four Zones'] = '挽具解剖：三大护法 × 四区域'

T['*A framework that cannot be drawn as a table is a slogan, not an analytical tool.*'] = \
    '*一个画不成表格的框架，是口号，不是分析工具。*'

T['Chapter 04 argued that any working harness must carry three load-bearing guardians — SDD, TDD, MDD — in that causal order. This chapter places those three guardians against four operational **zones** — *Bridle*, *Fence*, *Paddock*, *Groom* — to produce a 3-row × 4-column matrix. The twelve cells are the analytical spine every later chapter refers back to.'] = \
    '第 04 章论证了：任何一具能工作的挽具，都必须按那个因果顺序扛住三位承重的护法——SDD、TDD、MDD。本章把这三位护法放到四条操作性的 **区域（zones）**——*缰绳（Bridle）*、*护栏（Fence）*、*牧场（Paddock）*、*梳理（Groom）*——上，得到一张 3 行 × 4 列的矩阵。这十二格，就是本书后续每一章都会回头指的那条分析脊梁。'

T['Before the matrix itself, §05.Provenance says plainly where the four-zone vocabulary comes from and why this book still uses it. Readers who want the definitions first may skip to §05.Overview.'] = \
    '在切入矩阵本身之前，§05.*出处* 先把"四区域"这套词汇的来路讲清楚，也说清本书为什么仍然用它。想先看定义的读者，可以直接跳到 §05.*全景*。'

T['Provenance'] = '出处'

T['The four-zone metaphor — **Bridle** (what steers the agent before it writes code), **Fence** (what refuses bad work regardless of author), **Paddock** (the bounded space inside which the agent may roam), **Groom** (the recurring maintenance that keeps the harness itself alive) — was proposed by the author of this book in the 2026-03-28 blog post *Harness Engineering: 给 AI 套上缰绳* {cite}`walterfan2026guardians`. It is a **practitioner framework**, not a peer-reviewed taxonomy. Readers with a research background should treat it as a pedagogical scaffold, not as a settled decomposition of the field.'] = \
    '"四区域"这个比喻——**缰绳（Bridle）**（在智能体动手写代码之前引导它的东西）、**护栏（Fence）**（不论作者是谁都会拒绝坏活的东西）、**牧场（Paddock）**（智能体可以自由走动的那片有界空间）、**梳理（Groom）**（让挽具自身保持活着的那类反复发生的维护）——由本书作者在 2026-03-28 那篇博客《Harness Engineering: 给 AI 套上缰绳》中提出 {cite}`walterfan2026guardians`。它是一份 **实践者框架**，不是一份经过同行评议的分类学。有研究背景的读者应当把它当作教学脚手架来用，而不是当作这个领域已经尘埃落定的分解来用。'

T['Three adjacent frameworks cover roughly the same territory and deserve explicit triangulation:'] = \
    '有三个相邻框架大致覆盖着同一片地图，值得拿来显式地做一次三点定位：'

T["**CAR decomposition with HarnessCard reporting format** — proposed by the *Harness Engineering for Language Agents* position paper {cite}`car2025decomposition`, which splits a harness into **Control** (who decides what runs), **Agency** (what the agent may do on its own), and **Runtime** (the substrate the agent's code executes on), and pairs the decomposition with a standardised HarnessCard disclosure format. CAR is the book's preferred *academic* reference and is what Chapter 07–11's case-study HarnessCards ultimately serialise against."] = \
    '**CAR 分解 ＋ HarnessCard 报告格式**——由立场论文 *Harness Engineering for Language Agents* 提出 {cite}`car2025decomposition`，把一具挽具切分成 **Control（谁来决定运行什么）**、**Agency（智能体自行可以做什么）**、**Runtime（智能体代码所运行其上的那层底座）** 三部分，并把这份分解与一套标准化的 HarnessCard 披露格式配套。CAR 是本书首选的 *学术* 参考；第 07–11 章那几份案例研究 HarnessCard，最终都是以它为目标来序列化的。'

T['**Thoughtworks\' three-part framing** {cite}`thoughtworks2026harness` treats harness work as *context engineering* + *architectural constraints* + *garbage collection*. This framing is closer in spirit to DevOps and is where the "garbage collection" intuition behind §05.*Groom* originated.'] = \
    '**Thoughtworks 的三段式框架** {cite}`thoughtworks2026harness` 把挽具工作看作 *context engineering* ＋ *architectural constraints* ＋ *garbage collection*。这种框法在精神上更接近 DevOps，也是 §05.*梳理* 背后"garbage collection"那股直觉最早的来路。'

T["**LangChain's five-part agent anatomy** {cite}`langchain2026tbench` lists *prompts / tools / middleware / orchestration / runtime* as the building blocks exposed in the Terminal-Bench 2.0 post. LangChain's framing is product-centric (intended for framework users) where this book's four zones are workflow-centric (intended for team leads deciding what to invest in next week)."] = \
    '**LangChain 的五段式智能体解剖** {cite}`langchain2026tbench` 在 Terminal-Bench 2.0 那篇博客里，列出 *prompts / tools / middleware / orchestration / runtime* 作为构件。LangChain 的框法以产品为中心（面向的是框架使用者），而本书的四区域以工作流为中心（面向的是下周要决定"把钱往哪投"的团队负责人）。'

T['Why keep Bridle / Fence / Paddock / Groom given these three adjacent frameworks? Two reasons. First, the four zones **map 1:1 onto a workflow every engineering team already runs** — we already have code reviewers, CI gates, staging environments, and weekly chore lists; the four zones rename those into a vocabulary that treats them as first-class harness artefacts rather than DevOps afterthoughts. Second, pairing the zones with SDD / TDD / MDD produces a **3 × 4 Cartesian product** with twelve small, concrete cells — each cell small enough that a reader can ship one artefact for it in an afternoon. A three-part decomposition (CAR) is great for writing a position paper; a twelve-cell matrix is what you want when Monday morning asks *"what do we invest in next?"*.'] = \
    '既然有了这三个相邻框架，为什么还保留 Bridle／Fence／Paddock／Groom？两个原因。第一，这四个区域 **能与任何一支工程团队已经在跑的工作流 1:1 对应**——我们本来就有代码评审人、CI 关卡、staging 环境、每周杂务清单；四区域只是把它们重新命名成一套把它们视为 *一等挽具制品* 的词汇，而不是 DevOps 的附属品。第二，把四区域与 SDD／TDD／MDD 相乘，得到一个 **3 × 4 笛卡尔积**，十二个小格——每格都小到读者可以花一个下午为它交付一件制品。三分法（CAR）适合用来写一篇立场论文；十二格矩阵，则是周一早上被问到 *"下一步往哪投？"* 时你真正想要的那种东西。'

T['A reader who prefers CAR over Bridle / Fence / Paddock / Groom can translate: Bridle roughly maps to CAR-Control; Fence and Paddock together roughly map to CAR-Agency; Groom covers cross-cutting concerns CAR handles as Runtime evolution. This book uses the four-zone naming throughout but never claims primacy over CAR; the translation is first-class, not a retrofit.'] = \
    '比起 Bridle／Fence／Paddock／Groom 更愿意用 CAR 的读者，可以这样对一下：缰绳大致对应 CAR 的 Control；护栏和牧场合起来大致对应 CAR 的 Agency；梳理覆盖的则是 CAR 作为 Runtime 演进来处理的那类横切关切。本书全程使用四区域的命名，但从不声称它比 CAR 更优先；这份对照是一等公民，不是事后补做的。'

T['§05.Overview — The 3 × 4 Matrix'] = '§05.全景 —— 3 × 4 矩阵'

T['**Bridle** — steers before writing'] = '**缰绳（Bridle）**——在动笔之前引导'
T['**Fence** — refuses bad work'] = '**护栏（Fence）**——拒绝坏活'
T['**Paddock** — bounds where the agent may roam'] = '**牧场（Paddock）**——划定智能体可以走动的范围'
T['**Groom** — tends the harness itself'] = '**梳理（Groom）**——伺候挽具自身'

T['**SDD**'] = '**SDD**'
T['**TDD**'] = '**TDD**'
T['**MDD**'] = '**MDD**'

T['[SDD × Bridle](sdd-x-bridle)'] = '[SDD × 缰绳](sdd-x-bridle)'
T['[SDD × Fence](sdd-x-fence)'] = '[SDD × 护栏](sdd-x-fence)'
T['[SDD × Paddock](sdd-x-paddock)'] = '[SDD × 牧场](sdd-x-paddock)'
T['[SDD × Groom](sdd-x-groom)'] = '[SDD × 梳理](sdd-x-groom)'
T['[TDD × Bridle](tdd-x-bridle)'] = '[TDD × 缰绳](tdd-x-bridle)'
T['[TDD × Fence](tdd-x-fence)'] = '[TDD × 护栏](tdd-x-fence)'
T['[TDD × Paddock](tdd-x-paddock)'] = '[TDD × 牧场](tdd-x-paddock)'
T['[TDD × Groom](tdd-x-groom)'] = '[TDD × 梳理](tdd-x-groom)'
T['[MDD × Bridle](mdd-x-bridle)'] = '[MDD × 缰绳](mdd-x-bridle)'
T['[MDD × Fence](mdd-x-fence)'] = '[MDD × 护栏](mdd-x-fence)'
T['[MDD × Paddock](mdd-x-paddock)'] = '[MDD × 牧场](mdd-x-paddock)'
T['[MDD × Groom](mdd-x-groom)'] = '[MDD × 梳理](mdd-x-groom)'

T['The twelve H3 subsections below — one per cell, in the fixed order **SDD row, then TDD row, then MDD row** — are the chapter\'s working body. Every case-study chapter (07–11) scores a real harness against the same twelve cells.'] = \
    '下面十二个 H3 小节——每格一节，按 **先 SDD 行、再 TDD 行、最后 MDD 行** 的固定顺序排列——是本章的主干。每一章案例研究（07–11）都以同样的十二格为坐标，给一具真实的挽具打分。'

T['A word on how to *read* the matrix. The twelve cells are analytically independent (a strong TDD × Fence does not imply a strong SDD × Groom) but *operationally coupled* — strong cells cover for weak ones, and weak cells quietly sabotage strong ones. Three couplings worth noticing before reading any row:'] = \
    '关于这张矩阵 *应该怎么读*，先说一句。这十二格在分析上彼此独立（一个强壮的 TDD × 护栏并不意味着也会有一个强壮的 SDD × 梳理），但在 *操作* 上彼此耦合——强的格子会替弱的格子顶住一阵，弱的格子也会无声地拖垮强的格子。在读任何一行之前，有三种耦合值得先注意：'

T['**Bridle weakness amplifies through Fence strength.** A vague `AGENTS.md` (weak SDD × Bridle) paired with a strict pre-commit hook (strong TDD × Fence) produces code that is *clean* and *wrong*: the lint passes, the tests pass, and the architecture violates the intent the spec never pinned down. Strong fences make weak bridles invisible — until the architectural debt surfaces in an incident.'] = \
    '**缰绳的弱，会被护栏的强放大出来。** 一份含糊的 `AGENTS.md`（SDD × 缰绳弱）搭配一条严苛的 pre-commit 钩子（TDD × 护栏强），会产出那种 *干净而错* 的代码：lint 过了、测试过了，而架构违反着规约从未钉住的那份意图。强壮的护栏让虚弱的缰绳看起来像没事——直到架构债在一场事故里浮出水面。'

T['**Paddock strength hides Bridle weakness.** A thorough PR review ritual (strong SDD × Paddock) can carry a team for a year with a mediocre `AGENTS.md`, because the human reviewer compensates on every merge. The weakness appears the moment the team scales reviewer capacity less than it scales agent output — which is *always*.'] = \
    '**牧场的强，会掩盖缰绳的弱。** 一套扎实的 PR 评审仪式（SDD × 牧场强），在一份平庸的 `AGENTS.md` 下也能把团队扛上一年，因为每一次合并都靠评审人顶上来。一旦团队"扩评审人能力"的速度慢于"扩智能体产出"的速度，这份弱就暴露出来——而这永远会发生。'

T['**Groom is where the other three decay.** Every cell in the Bridle, Fence, and Paddock columns depreciates by default; the Groom column is what pays the depreciation down. A harness with zeros in the Groom column will drift back to zeros in every other column within two quarters, regardless of how much was invested up front.'] = \
    '**梳理是其他三列衰减的归宿。** 缰绳、护栏、牧场这三列上的每一格，默认都在贬值；梳理这一列存在的意义，就是把这份折旧偿还下去。一具梳理列为零的挽具，不管开始时投入了多少，都会在两个季度内把其他三列的分数都拖回零。'

T['Read each cell below with this coupling in mind: a high score is not durable without its sibling cells, and no single cell is load-bearing on its own.'] = \
    '读下面每一格时，把这种耦合放在心里：一个高分若没有兄弟格子陪着，并不耐用；没有哪一格能独自承重。'

T['SDD × Bridle — Agent-facing specs that steer'] = 'SDD × 缰绳 —— 引导智能体的规约'

T['**Definition.** A bridle in this cell is any file the agent *reads before it writes anything* and whose primary purpose is to shape what the agent tries to build. `AGENTS.md`, `CLAUDE.md`, and top-level `SKILL.md` files live here {cite}`anthropic2024claudecode`. A bridle that is unread or stale steers nothing; the guardian responsibility therefore extends to keeping the file fresh, not merely present.'] = \
    '**定义。** 这一格里的缰绳，指的是智能体 *在动笔之前会先读* 的任何一份文件，它的首要目的是塑造"智能体试图去建什么"。`AGENTS.md`、`CLAUDE.md`、顶层的 `SKILL.md` 都住在这里 {cite}`anthropic2024claudecode`。一份没人读或已经过时的缰绳，什么也引导不了；因此这位护法的职责不止是让文件在场，更要让它保持新鲜。'

code_40 = '''<!-- verified: 2026-04-17 · SDD × Bridle · agent-facing spec that steers before writing -->

# AGENTS.md — sample

## Role & Scope
You are a coding agent for `todo-cli`. You may edit files under `todo/` and
`tests/`. You must not touch `scripts/`, `deploy/`, or any `.env*` file.

## House rules
- Before editing any file, list `tests/test_<basename>.py`; if it exists, read it.
- Never invent package names; use the pinned versions in `pyproject.toml`.
- Every new public function gets a docstring and a test; no exceptions.

## Escalation
If a rule above conflicts with user instruction, pause and surface the
conflict explicitly; do not silently override.
'''
T[code_40] = code_40

T['SDD × Fence — Spec validity enforced at the gate'] = 'SDD × 护栏 —— 在关卡处强制规约合法性'

T['**Definition.** A fence in this cell enforces that every spec-shaped artefact is *well-formed before it becomes authoritative*. Examples: JSON-Schema validation of prompt templates at commit time, MCP-manifest schema checks, CI steps that refuse documentation builds with unresolved `{ref}` links {cite}`martraire2019living`. Without this fence, spec rot accumulates silently and SDD × Bridle becomes a lie.'] = \
    '**定义。** 这一格里的护栏，强制每一件形如"规约"的制品，*在它变成权威之前* 就必须格式良好。例如：提示词模板在 commit 时被 JSON-Schema 校验、MCP manifest 的 schema 检查、CI 阶段拒绝包含未解析 `{ref}` 链接的文档构建 {cite}`martraire2019living`。没有这道护栏，规约的腐烂会无声累积，SDD × 缰绳就会沦为一句谎话。'

code_43 = '''{
  "$comment": "verified: 2026-04-17 · SDD x Fence · JSON Schema validated at commit time",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "PromptTemplate",
  "type": "object",
  "required": ["name", "system_prompt", "user_prompt", "tags"],
  "properties": {
    "name":          {"type": "string", "pattern": "^[a-z][a-z0-9_]{2,63}$"},
    "system_prompt": {"type": "string", "minLength": 16},
    "user_prompt":   {"type": "string", "minLength": 16},
    "tags":          {"type": "array", "items": {"type": "string"}, "minItems": 1}
  },
  "additionalProperties": false
}
'''
T[code_43] = code_43

T['SDD × Paddock — Acceptance that matches the spec'] = 'SDD × 牧场 —— 与规约相符的验收'

T['**Definition.** A paddock in this cell is a bounded *review ritual* that confirms delivered work matches the spec, role by role, line by line. Executable specifications {cite}`adzic2011specbyexample` are the canonical form; the lazy-scrum-team *Verification Table* pattern {cite}`lazyscrumteam2026` is a concrete instance the book adopts throughout.'] = \
    '**定义。** 这一格里的牧场，是一场有边界的 *评审仪式*，逐角色、逐行地确认"交付的工作与规约相符"。可执行规约 {cite}`adzic2011specbyexample` 是它的经典形态；lazy-scrum-team 的 *验证表（Verification Table）* 模式 {cite}`lazyscrumteam2026` 是本书全程采用的一个具体实例。'

code_46_en = '''<!-- verified: 2026-04-17 · SDD × Paddock · Verification Table pattern from lazy-scrum-team -->

# Acceptance Gate — Verification Table

A story is `done` only when every row below is checked by the named role.

| # | Requirement                          | Evidence (file or URL)       | Checked by        |
|---|--------------------------------------|------------------------------|-------------------|
| 1 | Acceptance tests green               | CI run link                  | Test Engineer     |
| 2 | `AGENTS.md` rules unchanged or versioned | `git diff` summary       | Architect         |
| 3 | `CHANGELOG.md` entry under Unreleased | diff hunk                   | PO                |
| 4 | No new TODO/FIXME markers added      | `rg -c TODO` before/after    | Code Reviewer     |
| 5 | HarnessCard cell score unchanged or explained | HarnessCard delta note | Final Acceptance  |

Rows may only be marked by the named role; self-certification is rejected.
'''
code_46_zh = '''<!-- verified: 2026-04-17 · SDD × Paddock · Verification Table pattern from lazy-scrum-team -->

# 验收关卡 —— 验证表

只有下表每一行都被对应角色打勾，一个故事才算 `done`。

| # | 需求                                  | 证据（文件或 URL）              | 签字人             |
|---|---------------------------------------|-------------------------------|-------------------|
| 1 | 验收测试变绿                           | CI 跑动链接                    | Test Engineer     |
| 2 | `AGENTS.md` 规则未变、或已版本化        | `git diff` 摘要                | Architect         |
| 3 | `CHANGELOG.md` 在 Unreleased 下有条目   | diff 片段                      | PO                |
| 4 | 无新增 TODO/FIXME 标记                 | `rg -c TODO` 前后对比           | Code Reviewer     |
| 5 | HarnessCard 格子分数不变，或有说明      | HarnessCard delta 备注         | Final Acceptance  |

每一行只能由署名的角色来打勾；自证不被接受。
'''
T[code_46_en] = code_46_zh

T['SDD × Groom — Keeping the spec surface alive'] = 'SDD × 梳理 —— 让规约面持续鲜活'

T['**Definition.** A groom action in this cell is a *recurring maintenance job* that refreshes the spec surface so the agent\'s input never silently rots. Broken-link sweeps, stale `verified:` header rewrites, and weekly regeneration of auto-generated `AGENTS.md` tables of contents are typical {cite}`ford2017buildingevolutionary`. Without grooming, SDD entropy accumulates faster than authors can keep up.'] = \
    '**定义。** 这一格里的梳理动作，是一项 *反复运行的维护作业*，用来刷新规约面，以使智能体的输入永远不会悄无声息地腐烂。典型做法：扫坏链、重写过期的 `verified:` 头、每周重新生成自动化 `AGENTS.md` 目录 {cite}`ford2017buildingevolutionary`。没有梳理，SDD 的熵累积速度会快过作者跟得上的速度。'

code_49 = '''#!/usr/bin/env bash
# verified: 2026-04-17 · SDD × Groom · weekly doc-sync job
# Refreshes living documentation so the spec surface the agent reads does
# not silently drift from the code it describes.
set -euo pipefail

make book-linkcheck || echo "::warning::broken links surfaced"

# regenerate AGENTS.md TOC from source chapters
python scripts/gen_agents_toc.py > AGENTS.md.next
diff -u AGENTS.md AGENTS.md.next && rm AGENTS.md.next \\
  || { mv AGENTS.md.next AGENTS.md; git add AGENTS.md; }

# re-stamp `verified:` headers in _handson/ artefacts modified this week
python scripts/restamp_verified.py book/source/_handson
'''
T[code_49] = code_49

T['Pitfall — SDD row failure modes'] = '陷阱——SDD 行的失败模式'

T["The SDD row's distinctive failure is not *absence* of specs but *unfalsifiable* ones. Two cell-specific variants worth naming (Ch.03's *aspirational `CLAUDE.md`* edge case covers the third):"] = \
    'SDD 行的特异失败，不是规约 *缺席*，而是规约 *无法被证伪*。有两种按格子分的变体值得点名（第三种——"愿望型 `CLAUDE.md`"，已经被第 03 章覆盖）：'

T['**The MCP manifest that outlives its handler.** The schema advertises a tool the server no longer implements; the agent invokes it confidently and receives a puzzling error. SDD × Fence exists to catch exactly this, but only if the fence is wired to *both* sides of the schema-to-handler contract.'] = \
    '**比 handler 活得还久的 MCP manifest。** schema 里写着一个服务器早已不再实现的工具；智能体自信地调用它，得到一条莫名其妙的错误。SDD × 护栏正是为了抓这种失败而存在的，但前提是这道护栏 *两端* 都要被接上"schema－handler"契约的两头。'

T['**The unversioned spec.** `AGENTS.md` with no changelog, no `verified:` date, no sign of having evolved. Reviewers cannot tell whether its claims are current or legacy; agent and human both read it as authoritative. SDD × Groom is the answer — but only if the Groom job fails loudly when the spec has not been touched in N weeks.'] = \
    '**没有版本的规约。** 一份 `AGENTS.md`，没有 changelog、没有 `verified:` 日期、看不出被演进过。评审者判断不出里面的主张是当下的还是遗留的；智能体和人都把它当作权威来读。SDD × 梳理是答案——但前提是，当规约 N 周没被碰过时，这项梳理作业会大声失败。'

T["Row-level test: can you name, for each SDD cell, one artefact in your repo today and one check that would fire *this week* if it broke? If any cell's answer is \"we trust people to keep it current\", that cell is at zero regardless of the file contents."] = \
    '行级自测：针对 SDD 的每一格，你都能点出今天仓库里对应的一件制品、以及一条若它坏掉会在 *本周之内* 触发的检查吗？哪一格的答案若是"我们相信大家会把它保持新鲜"，那无论那一格里的文件内容多好，它的分数都是零。'

T['TDD × Bridle — Failing-first tests as input to the agent'] = 'TDD × 缰绳 —— 先失败的测试作为给智能体的输入'

T["**Definition.** A bridle in this cell is a *deliberately red test suite* committed before the agent is invited in. The agent reads the failing tests as part of its context and understands *what it must make green* before writing production code {cite}`beck2002tdd`. The key property is *red on commit*, not \"a test exists somewhere\"."] = \
    '**定义。** 这一格里的缰绳，是一份 *故意为红* 的测试套件，在智能体被请进来之前就先提交进仓库。智能体把这些失败的测试作为上下文的一部分读进来，从而明白 *在它动手写生产代码之前，必须把哪些测试变绿* {cite}`beck2002tdd`。关键性质是"commit 时是红的"，而不是"某处存在着一条测试"。'

code_57 = '''# verified: 2026-04-17 · TDD × Bridle · starter tests steer the agent before it writes
"""A minimal failing-first suite that pins the agent loop shape.

Committing this file before the first prompt means the agent cannot fake
progress: a turn that does not green one of these tests did not advance
the project.
"""
import pytest


def test_loop_halts_on_empty_plan(loop):
    assert loop.step(plan=[]) == "halt"


def test_loop_consumes_one_tool_call_per_step(loop):
    result = loop.step(plan=["noop_tool"])
    assert result.tool_calls == 1


@pytest.fixture
def loop():
    from todo.agent import AgentLoop
    return AgentLoop()
'''
T[code_57] = code_57

T['TDD × Fence — Hooks that refuse red-tree commits'] = 'TDD × 护栏 —— 拒绝红树 commit 的钩子'

T['**Definition.** A fence in this cell blocks any edit or commit while the test tree is red. Pre-commit hooks, Claude-Code `PreToolUse` hooks, and required CI checks all belong here {cite}`humble2010continuousdelivery`. The distinction from TDD × Paddock is *immediacy* — a TDD fence fires at the keystroke, a TDD paddock fires at the PR.'] = \
    '**定义。** 这一格里的护栏，会在测试树为红时拦住任何修改或 commit。pre-commit 钩子、Claude-Code 的 `PreToolUse` 钩子、以及必过的 CI 检查都属于这里 {cite}`humble2010continuousdelivery`。它和 TDD × 牧场的区别在于 *及时性*——TDD 护栏在键盘敲击那一刻就触发，TDD 牧场在 PR 那一刻才触发。'

code_60 = '''{
  "$comment": "verified: 2026-04-17 · TDD x Fence · Claude Code hook blocks on red tests",
  "hooks": {
    "PreToolUse": [
      {"matcher": "Write|Edit|MultiEdit", "command": "pytest -q -m 'not slow'",
       "stopOnFailure": true, "description": "refuse edits while tests are red"}
    ],
    "PostToolUse": [
      {"matcher": "Write|Edit|MultiEdit", "command": "ruff check .",
       "stopOnFailure": false}
    ]
  }
}
'''
T[code_60] = code_60

T['TDD × Paddock — CI gate and environment parity'] = 'TDD × 牧场 —— CI 关卡与环境对等'

T['**Definition.** A paddock in this cell is a *required, branch-protected test run* that happens in an environment faithful to production. It is the integration-level twin of TDD × Fence: broader in scope, slower in turnaround, authoritative in verdict {cite}`forsgren2018accelerate`.'] = \
    '**定义。** 这一格里的牧场，是一次 *必过、分支保护下* 的测试运行，发生在一个忠实于生产环境的环境中。它是 TDD × 护栏在集成层面上的孪生兄弟：覆盖更广、周转更慢、判决更权威 {cite}`forsgren2018accelerate`。'

code_63 = '''# verified: 2026-04-17 · TDD × Paddock · required status check on protected branch
name: ci-gate
on: [pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: {python-version: "3.11"}
      - run: pip install -e ".[test]"
      - run: pytest -q --junitxml=junit.xml
      - if: failure()
        run: echo "::error::gate failed — branch cannot merge"
'''
T[code_63] = code_63

T['TDD × Groom — Flake maintenance and test-surface evolution'] = 'TDD × 梳理 —— flake 维护与测试面演进'

T["**Definition.** A groom action in this cell is a *recurring policy* for handling tests that stop being load-bearing — flakes, long-extinct regressions, tests that drift out of step with the spec they verified. Without grooming, the test corpus accumulates dead weight and eventually *loses* the team's trust {cite}`cunningham1992debt`."] = \
    '**定义。** 这一格里的梳理动作，是一套处理"不再承重的测试"的 *反复政策*——flake、早已消失的回归、以及与它当初所核验的那份规约脱节的测试。没有梳理，测试语料会不断累积死重，最终 *失去* 团队的信任 {cite}`cunningham1992debt`。'

code_66_en = '''<!-- verified: 2026-04-17 · TDD × Groom · flaky-test quarantine policy -->

# Flaky Test Quarantine

A test that fails intermittently without a code change enters quarantine:

1. Move it from `tests/` into `tests/quarantine/`; mark with `@pytest.mark.flaky`.
2. Open an issue tagged `quarantine` with the last three failure logs.
3. CI runs `tests/quarantine/` separately; failures post a comment but do
   not block the merge.
4. If the quarantined test is green for 7 consecutive nightly runs, promote
   it back into `tests/`; if red for 30 days, delete with an explicit
   justification in the commit message.

Quarantine is a paddock *inside* the paddock: a space where flakes cannot
poison the main gate while still being tracked.
'''
code_66_zh = '''<!-- verified: 2026-04-17 · TDD × Groom · flaky-test quarantine policy -->

# Flaky 测试隔离区

一条在没有代码变更的情况下偶尔失败的测试，进入隔离区：

1. 把它从 `tests/` 移到 `tests/quarantine/`；用 `@pytest.mark.flaky` 标注。
2. 开一个带 `quarantine` 标签的 issue，附上最近三次失败日志。
3. CI 单独跑 `tests/quarantine/`；失败会留一条评论，但
   不会阻塞合并。
4. 若这条被隔离的测试连续 7 次夜间构建都为绿，把它提升回 `tests/`；若
   连续 30 天为红，在 commit message 里写明理由后删除它。

隔离区是 *牧场里的牧场*：一个让 flake 既不污染主关卡、
又仍然被跟踪的空间。
'''
T[code_66_en] = code_66_zh

T['Pitfall — TDD row failure modes'] = '陷阱——TDD 行的失败模式'

T['The TDD row fails in ways the SDD row does not, because tests have an unusual property: a failing test is *cheap*, but a *passing test that has lost contact with the behaviour it verifies* is worse than no test. Three row-level failures:'] = \
    'TDD 行的失败方式，跟 SDD 行不同，因为测试有一项不寻常的性质：一条失败的测试 *便宜*；而一条 *仍然通过、但已经与它核验的那份行为失联的测试*，比没有测试还糟。三种行级失败：'

T['**The red-but-ignored test.** A flaky test fails once a week; someone adds `@pytest.mark.skip("flaky, fix later")`; "later" never comes. The test now consumes CI cycles, pollutes the output, and teaches the team that red is ignorable — the opposite of TDD × Fence\'s purpose. If a test is not trusted enough to block a commit, it is not trusted enough to live in the main suite. Move it to quarantine with a dated owner or delete it.'] = \
    '**红却被忽略的测试。** 一条 flaky 测试每周失败一次；有人加了 `@pytest.mark.skip("flaky, fix later")`；那个"later"永远不会来。这条测试如今在消耗 CI 周期、污染输出，并教会团队"红是可以忽略的"——这恰恰是 TDD × 护栏存在目的的反面。如果一条测试被信任不到能挡住 commit 的程度，那它也配不上住在主测试套件里。把它挪进隔离区、署名指定一位 owner、写上日期，否则就删了。'

T["**The green-and-stale test.** A test pins behaviour the product requirement removed two quarters ago. Nobody notices because it stays green. An agent reading the test as part of TDD × Bridle now learns a *wrong* contract and writes new code against it. Green alone is not evidence of relevance; Groom must periodically ask *which spec does each test now correspond to, and is that spec still live?*"] = \
    '**绿且过期的测试。** 一条测试钉的是两个季度前产品需求早已移除的行为。没人注意到，因为它一直是绿的。一位在 TDD × 缰绳框架下读这条测试的智能体，如今学到的是一份 *错误的* 契约，然后照着它写新代码。绿本身不等于相关；梳理必须周期性地问：*每一条测试现在对应的是哪一条规约，那条规约还活着吗？*'

T['**The adversarial test that never got written.** The test the human-authored test *should* have been is the one that would have found the agent\'s shortcut. If PRs never add "one more test that attacks the cheapest path to green" (see Ch.04\'s first-try-pass pitfall), TDD × Paddock slowly trains the agent rather than guarding against it.'] = \
    '**那条从来没被写出来的敌意测试。** 那条人本 *应该* 写但没写的测试，正是能找出智能体捷径的那条。若 PR 里从不追加"再写一条专门攻击通向绿的最省力路径的测试"（参见第 04 章"第一把就过"那条陷阱），TDD × 牧场就会慢慢地 *训练* 智能体，而不是防它。'

T["Row-level test: does your team's test-to-LOC ratio *increase* after AI-assisted PRs, or stay flat? If it stays flat, you are under- investing in the test side of the red-green loop at the precise moment the loop is cheapest to run."] = \
    '行级自测：AI 辅助的 PR 之后，你团队的"测试／LOC"比例 *上升* 了，还是没动？如果没动，那你正是在这条红—绿循环最便宜的时刻，对循环的测试一侧投入不足。'

T['MDD × Bridle — The one metric that steers'] = 'MDD × 缰绳 —— 真正在引导的那一个度量'

T['**Definition.** A bridle in this cell is a *north-star metric* named before production traffic hits the system. Everything else is diagnostic. The canonical candidate for an AI coding harness is **mean agent turns to green** on a fixed benchmark suite {cite}`langchain2026tbench`.'] = \
    '**定义。** 这一格里的缰绳，是一条在生产流量打到系统上之前 *就已被命名* 的 *北极星度量*。其他的一切都是诊断性的。对一具 AI 编码挽具而言，经典候选是：在一份固定基准套件上的 **智能体 mean turns to green**（平均变绿轮数）{cite}`langchain2026tbench`。'

code_75_en = '''<!-- verified: 2026-04-17 · MDD × Bridle · the one metric that steers -->

# Metrics North-Star

Pick exactly one metric that captures *fitness for purpose* of the harness
itself, then let every other metric be diagnostic of that one.

- **Project-level north-star:** **mean agent turns to green** on a fixed
  benchmark suite, measured weekly.
- **Why:** rising turns-to-green is the earliest observable signal that
  spec (SDD), tests (TDD), or tooling (MDD) has silently degraded.
- **Diagnostic metrics** (each tied to a guardian):
  - SDD — stale `verified:` header count, broken links in `AGENTS.md`
  - TDD — flaky-test count, coverage floor
  - MDD — cost per turn, prompt cache hit rate
'''
code_75_zh = '''<!-- verified: 2026-04-17 · MDD × Bridle · the one metric that steers -->

# 度量 · 北极星

恰好挑一条能捕捉挽具 *本身是否适配其目的（fitness for purpose）* 的度量，
然后让其他所有度量都作为这一条的诊断。

- **项目级北极星：** 在一份固定基准套件上的 **智能体 mean turns to green**
  （平均变绿轮数），每周测一次。
- **为什么：** turns-to-green 的上升，是规约（SDD）、测试（TDD）、
  或工具（MDD）已经悄悄退化的最早可观测信号。
- **诊断度量**（每一条绑一位护法）：
  - SDD —— 过期 `verified:` 头数量、`AGENTS.md` 里的坏链数
  - TDD —— flaky 测试数、覆盖率下限
  - MDD —— 每轮成本、提示词缓存命中率
'''
T[code_75_en] = code_75_zh

T['MDD × Fence — Cost caps and circuit breakers'] = 'MDD × 护栏 —— 成本上限与熔断器'

T['**Definition.** A fence in this cell is an *automated refusal* the moment an observed cost, latency, or error-rate signal crosses a pre-declared threshold. Cost caps on LLM calls, rate limits on tool invocations, and soft/hard kill-switches are typical {cite}`majors2022observability`.'] = \
    '**定义。** 这一格里的护栏，是在"被观测到的成本、延迟、或错误率信号越过预先声明的阈值"那一刻的 *自动化拒绝*。LLM 调用上的成本上限、工具调用的限流、以及软／硬关闭开关都是典型做法 {cite}`majors2022observability`。'

code_78 = '''# verified: 2026-04-17 · MDD × Fence · budget circuit-breaker, rejected over limit
cost_cap_version: "0.1"
per_session_usd:   2.00
per_day_usd:       50.00
per_month_usd:     800.00
action_on_breach:
  soft: warn_in_status_line
  hard: refuse_new_tool_calls_until_reset
alerts:
  - channel: slack
    at: 0.75  # of the monthly cap
  - channel: email
    at: 0.95
'''
T[code_78] = code_78

T['MDD × Paddock — Release SLIs and staging soak'] = 'MDD × 牧场 —— 发布 SLI 与 staging 浸泡'

T['**Definition.** A paddock in this cell is a *release gate* that requires production-equivalent signals to hold over a bounded staging window before the bits are allowed to graduate {cite}`ford2017buildingevolutionary`. The window itself is the paddock; the SLIs are the fence at its edge.'] = \
    '**定义。** 这一格里的牧场，是一道 *发布关卡*：要求"等价于生产的信号"在一个有界的 staging 窗口里都达标，之后这批二进制才被允许毕业 {cite}`ford2017buildingevolutionary`。窗口本身是牧场；窗口边上的 SLI，则是这道护栏。'

code_81_en = '''<!-- verified: 2026-04-17 · MDD × Paddock · pre-release SLI gate -->

# Release SLI Gate

A release candidate is blocked from production until these SLIs meet their
targets for a rolling 24h window in staging:

| SLI                        | Target       | Window  |
|----------------------------|--------------|---------|
| p99 latency (user paths)   | ≤ 400 ms     | 24h     |
| error rate                 | ≤ 0.1 %      | 24h     |
| harness-internal cost/turn | ≤ $0.03      | 24h     |
| spec-vs-prod drift score   | ≤ 2 findings | 24h     |

The paddock is the rolling 24h staging run; crossing the gate requires all
four targets, not three-of-four.
'''
code_81_zh = '''<!-- verified: 2026-04-17 · MDD × Paddock · pre-release SLI gate -->

# 发布 SLI 关卡

一个候选发布版本在生产环境之外被拦住，直到以下这些 SLI 在 staging 的
一个滚动 24 小时窗口里都达到目标：

| SLI                         | 目标           | 窗口  |
|-----------------------------|----------------|-------|
| p99 延迟（用户路径）         | ≤ 400 ms       | 24h   |
| 错误率                        | ≤ 0.1 %        | 24h   |
| 挽具内部成本／轮             | ≤ $0.03        | 24h   |
| 规约 vs. 生产漂移分          | ≤ 2 条发现     | 24h   |

牧场就是这段滚动 24 小时的 staging 运行；要过这道关，四条目标全部要过，
不接受四过三。
'''
T[code_81_en] = code_81_zh

T['MDD × Groom — Weekly metric audits and dashboard hygiene'] = 'MDD × 梳理 —— 每周度量审计与仪表盘卫生'

T["**Definition.** A groom action in this cell is a *weekly review of the metric surface itself* — which signals are still steering decisions, which dashboards have no owner, which alerts fire without a runbook. Lehman's laws {cite}`lehman1980laws` apply to metrics as much as to code: unmaintained signals decay into noise."] = \
    '**定义。** 这一格里的梳理动作，是一场 *每周对度量面本身的复盘*——哪些信号还在真正引导决策、哪些仪表盘已经没有 owner、哪些告警在没有 runbook 的情况下就会触发。Lehman 的演化律 {cite}`lehman1980laws` 对度量的适用度与对代码一样：没人维护的信号，会衰减成噪声。'

code_84 = '''#!/usr/bin/env bash
# verified: 2026-04-17 · MDD × Groom · weekly audit that tends the metric surface
# Not "collect more metrics" — prune stale ones and verify the living ones
# still steer something.
set -euo pipefail

echo "== metrics retention =="
python scripts/audit_metrics.py --older-than 90d --action list-unused

echo "== dashboard coverage =="
python scripts/audit_dashboards.py --require-owner --require-runbook

echo "== cost trend =="
python scripts/cost_trend.py --since "$(date -d '7 days ago' +%F)"

echo "write the findings to metrics-review-$(date +%F).md and open a PR"
'''
T[code_84] = code_84

T['Pitfall — MDD row failure modes'] = '陷阱——MDD 行的失败模式'

T['The MDD row fails more quietly than the other two rows because metrics decay *asymptotically*: a broken test goes red, a stale spec produces obvious contradictions, but a decaying dashboard merely becomes less useful. The three row-level failures:'] = \
    'MDD 行失败得比另外两行更安静，因为度量的衰减是 *渐近* 的：坏掉的测试会红、过期的规约会产出明显的矛盾，而一块正在衰减的仪表盘，只是变得越来越不管用。三种行级失败：'

T['**The north-star nobody watches.** A metric was declared load-bearing, a dashboard was built, a threshold was set — and no one looks at it outside incidents. The signal exists but does not *steer*; MDD × Bridle has a file and an empty chair. Fix: every north-star needs a named owner and a weekly agenda slot, or demote it to a diagnostic.'] = \
    '**没人盯的北极星。** 一条度量被宣布承重、一块仪表盘被搭起来、一个阈值被设上——然后除了事故时以外没人看。信号在，但它不 *引导*；MDD × 缰绳这一格，有文件，有空椅子。**解法**：每一条北极星都必须有一位署名 owner，和每周一个议程格子，否则就把它降级为诊断度量。'

T['**The cost cap with no tripwire.** A cost cap is configured at the API layer and never fires. Either the cap is too loose (it silently permits regression) or the cap is tight enough to matter but nobody is paged when it hits. MDD × Fence that never refuses anything for a quarter is indistinguishable from no fence at all.'] = \
    '**没有绊线的成本上限。** 在 API 层配了一条成本上限，它从不触发。要么这条上限太松（它沉默地放行了回归），要么它紧到值得关心、却没人在它命中时被呼叫。MDD × 护栏若整整一个季度都没拒绝过任何东西，和"没有护栏"没有区别。'

T["**The SLI that drifted from reality.** The staging SLI still measures endpoint P99, but the product shifted last quarter and the load-bearing path is now a background job whose latency the SLI ignores. Release gates keep passing; regressions ship. MDD × Paddock demands the SLIs be re-audited whenever the product's load-bearing path moves — which the agent's velocity now makes more frequent, not less."] = \
    '**与现实脱节的 SLI。** staging 的 SLI 仍然在量端点的 P99，但产品上个季度转了向，真正的承重路径已经变成一个后台作业，而这条 SLI 恰好忽略了它的延迟。发布关卡一路都在过；回归照样上线。MDD × 牧场要求：每当产品的承重路径发生位移，SLI 就必须被重新审计——而智能体的速度，让这种位移变得 *更* 频繁，不是更少。'

T["Row-level test: for each MDD cell, can you name both the signal *and* the specific decision it drove in the last thirty days? A signal without a decision it influenced is a dashboard pixel, not a guardian."] = \
    '行级自测：针对 MDD 的每一格，你都能点出 *既有* 那条信号、*也有* 它在过去三十天内驱动的某一项具体决定吗？一条没有驱动任何决定的信号，是仪表盘上的一个像素，而不是一位护法。'

T['Research Foundations'] = '研究脉络'

T["The matrix's analytical claim rests on five citable pillars:"] = \
    '这张矩阵的分析主张，靠五根可引用的支柱支着：'

T['**Primary academic source** for Harness Engineering as a distinct discipline: the CAR decomposition and HarnessCard reporting format {cite}`car2025decomposition`.'] = \
    '**首要学术来源**：把 Harness Engineering 作为一门独立学科对待——CAR 分解与 HarnessCard 报告格式 {cite}`car2025decomposition`。'

T['**Industry triangulation** across two independent, non-academic framings: Thoughtworks\' radar entry {cite}`thoughtworks2026harness` and LangChain\'s five-part anatomy {cite}`langchain2026tbench`.'] = \
    '**业界三点定位**：两份独立、非学术的框法——Thoughtworks 技术雷达的条目 {cite}`thoughtworks2026harness`、以及 LangChain 的五段式解剖 {cite}`langchain2026tbench`。'

T["**Fitness-function lineage** for the zones: Ford, Parsons & Kua's *Building Evolutionary Architectures* {cite}`ford2017buildingevolutionary` supplies the vocabulary of *architectural fitness functions* the four zones operationalise."] = \
    '**四区域的适配函数谱系**：Ford／Parsons／Kua 的 *Building Evolutionary Architectures* {cite}`ford2017buildingevolutionary` 提供了 *架构适配函数* 这套词汇——四区域把它做成了可操作的形式。'

T['**Evolution-law lineage** for §05.Groom: Lehman\'s 1980 laws of software evolution {cite}`lehman1980laws` are the underlying theory for why the Groom column exists at all.'] = \
    '**§05.梳理 背后的演化律谱系**：Lehman 1980 年的软件演化律 {cite}`lehman1980laws`，是"为什么梳理列压根需要存在"这件事背后的底层理论。'

T["**Practitioner lineage** for the zones' AI-era interpretation: the author's own 2026-03-28 blog post {cite}`walterfan2026guardians` and the lazy-scrum-team workflow repository {cite}`lazyscrumteam2026`."] = \
    '**四区域在 AI 时代诠释的实践者谱系**：作者本人 2026-03-28 那篇博客 {cite}`walterfan2026guardians`，以及 lazy-scrum-team 工作流仓库 {cite}`lazyscrumteam2026`。'

T['Hands-On'] = '动手环节'

T['Twelve artefacts live under `book/source/_handson/05-harness-anatomy/`, one per cell, following the directory layout `<guardian>-x-<zone>/<filename>`:'] = \
    '`book/source/_handson/05-harness-anatomy/` 下住着十二份制品，每格一份，按 `<guardian>-x-<zone>/<filename>` 的目录结构排布：'

T['**SDD row:** `AGENTS.md.sample`, `prompt-schema.json`, `acceptance-gate.md`, `update-docs.sh`'] = \
    '**SDD 行：** `AGENTS.md.sample`、`prompt-schema.json`、`acceptance-gate.md`、`update-docs.sh`'
T['**TDD row:** `starter-tests/test_loop.py` (under `tdd-x-bridle/`), `hooks.json`, `ci-gate.yml`, `flaky-test-quarantine.md`'] = \
    '**TDD 行：** `starter-tests/test_loop.py`（位于 `tdd-x-bridle/` 下）、`hooks.json`、`ci-gate.yml`、`flaky-test-quarantine.md`'
T['**MDD row:** `metrics-north-star.md`, `cost-cap.yaml`, `release-sli.md`, `weekly-audit.sh`'] = \
    '**MDD 行：** `metrics-north-star.md`、`cost-cap.yaml`、`release-sli.md`、`weekly-audit.sh`'

T["Each artefact is inline-rendered above inside its own H3 subsection; the file on disk is the single source of truth. A reader who wants to ship one cell at a time may copy any single file and begin. The book's central recommendation in Chapter 12 is that a team ships **one full row or one full column in 60 days** — which is thirty days of reading this chapter and another thirty of shipping four artefacts."] = \
    '每一份制品的内容都已内联渲染在上面各自的 H3 小节里；磁盘上的那份文件是唯一真源。想一格一格上线的读者，可以拷出任一份文件开始动手。本书在第 12 章的核心建议是：一支团队应当在 **60 天内上线完整的一行或完整的一列**——也就是三十天读本章，另外三十天交付四份制品。'


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
        print('  MISS:', repr(m[:120]))

    po2 = polib.pofile(PATH)
    remaining = [e for e in po2 if not e.msgstr and not e.obsolete]
    print(f'remaining: {len(remaining)}')


if __name__ == '__main__':
    main()
