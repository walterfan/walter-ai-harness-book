"""One-shot translator for Ch.11 lazy-ai-coder."""
import polib

PATH = 'source/locale/zh_CN/LC_MESSAGES/chapters/11-lazy-ai-coder.po'
T = {}

T['Case Study: Lazy AI Coder — A Four-Act Worked Example'] = \
    '案例研究：Lazy AI Coder —— 一则四幕剧形式的实证示例'

T["*If the framework cannot score the book's own host repository and then improve it, the framework is wrong.*"] = \
    '*若这套框架连"给本书所承载的仓库打分、再改进它"这件事都做不了，那这框架就是错的。*'

T["Every case study so far has been *about* someone else's harness. This chapter is different: it applies the three-guardian × four-zone matrix to the very repository this book ships from — [`walterfan/lazy-ai-coder`](https://github.com/walterfan/lazy-ai-coder) — and lands real fixes on `main`. The chapter is staged as four acts."] = \
    '到目前为止，每一篇案例研究都 *关于* 别人的挽具。本章不同：它把"三大护法 × 四区域"矩阵，套到本书所承载的那个仓库——[`walterfan/lazy-ai-coder`](https://github.com/walterfan/lazy-ai-coder)——上，并把真正的修复合入 `main`。本章以四幕剧的形式展开。'

T["**Status.** This chapter remains `status: draft` until the Section 14 commits land on the host repository's `main` branch. The book-lint script walks Act 3's commit SHAs through `git cat-file -e`; until at least two resolve, the chapter is excluded from the toctree. See §14.5."] = \
    '**状态。** 在第 14 节的那批 commit 合入宿主仓库 `main` 分支之前，本章一直保持 `status: draft`。book-lint 脚本会用 `git cat-file -e` 遍历第三幕里所列的 commit SHA；在至少两条解析成功之前，本章会被从 toctree 中排除。参见 §14.5。'

T['Act 1 — Audit'] = '第一幕 —— 审计'

T["The starting point is a HarnessCard capturing the repository's state as of the change's start commit. Evidence for each cell is a concrete file path inside the repository; the full scorecard is shipped as a hands-on artefact readers can diff against."] = \
    '起点是一份 HarnessCard，记录仓库在这一轮变更开始那笔 commit 时的状态。每一格的证据都是仓库内一条具体的文件路径；完整打分表以 hands-on 制品形式交付，读者可与之做 diff。'

code_6_en = '''<!-- verified: 2026-04-17 · Ch.11 Act 1 · Audit HarnessCard -->

# HarnessCard — Act 1 (Audit)

**Subject.** `walterfan/lazy-ai-coder`, starting commit SHA: `<TBD — captured at §14 landing>`.

**Date.** 2026-04-17 (pre-fix baseline).

**Schema version.** CAR-HarnessCard v0.2.

| Cell            | Score | Evidence                                      |
|-----------------|-------|-----------------------------------------------|
| SDD × Bridle    | 3     | `CLAUDE.md`, `AGENTS.md` exist but drift from `openspec/`. |
| SDD × Fence     | 1     | No `make prompts-lint`; `config/prompts.yaml` unchecked.  |
| SDD × Paddock   | 2     | Review is GitHub PR default; no Verification Table.       |
| SDD × Groom     | 1     | No sources-of-truth index; docs drift silently.           |
| TDD × Bridle    | 2     | `tests/` exists but not failing-first.                    |
| TDD × Fence     | 1     | No MCP tool schema check; no secrets scan in pre-commit.  |
| TDD × Paddock   | 3     | GitHub Actions CI runs `go test` + Python tests.          |
| TDD × Groom     | 2     | Flake policy undefined; recent flakes closed ad-hoc.      |
| MDD × Bridle    | 1     | No cost dashboard; LLM spend unobservable.                |
| MDD × Fence     | 2     | Rate limits at provider only; no local cap.               |
| MDD × Paddock   | 2     | Release notes exist; no SLI gate.                         |
| MDD × Groom     | 1     | No weekly audit script.                                   |

**SDD mean.** 1.75.  **TDD mean.** 2.0.  **MDD mean.** 1.5.

**Overall.** 1.75. This is the pre-fix baseline; Act 4 re-scores after
the §14 fixes land.
'''
code_6_zh = '''<!-- verified: 2026-04-17 · Ch.11 Act 1 · Audit HarnessCard -->

# HarnessCard —— 第一幕（审计）

**对象。** `walterfan/lazy-ai-coder`，起始 commit SHA：`<待定 —— §14 合入时登记>`。

**日期。** 2026-04-17（修复前的基线）。

**Schema 版本。** CAR-HarnessCard v0.2。

| 格子            | 得分  | 证据                                           |
|-----------------|-------|------------------------------------------------|
| SDD × 缰绳      | 3     | `CLAUDE.md`、`AGENTS.md` 存在，但已与 `openspec/` 漂移。|
| SDD × 护栏      | 1     | 无 `make prompts-lint`；`config/prompts.yaml` 未被校验。|
| SDD × 牧场      | 2     | 评审走 GitHub PR 默认流程；没有验证表。        |
| SDD × 梳理      | 1     | 没有"真相来源"索引；文档在无声漂移。           |
| TDD × 缰绳      | 2     | `tests/` 已存在，但不是 failing-first。         |
| TDD × 护栏      | 1     | 没有 MCP 工具 schema 检查；pre-commit 无密钥扫描。|
| TDD × 牧场      | 3     | GitHub Actions CI 跑 `go test` ＋ Python 测试。 |
| TDD × 梳理      | 2     | flake 策略未定义；近期 flake 靠临时处理关掉。  |
| MDD × 缰绳      | 1     | 无成本仪表盘；LLM 花销不可观测。               |
| MDD × 护栏      | 2     | 只有 provider 层的速率限制；无本地上限。       |
| MDD × 牧场      | 2     | 发布说明存在；无 SLI 关卡。                    |
| MDD × 梳理      | 1     | 没有每周审计脚本。                             |

**SDD 均值。** 1.75。  **TDD 均值。** 2.0。  **MDD 均值。** 1.5。

**总分。** 1.75。这是修复前的基线；第四幕会在 §14 的修复合入后重新打分。
'''
T[code_6_en] = code_6_zh

T["The audit lands squarely in the lower-left corner of the matrix: SDD × Fence, SDD × Groom, TDD × Fence, and MDD × Bridle / Groom are the five weakest cells. Cunningham's 1992 technical-debt metaphor {cite}`cunningham1992debt` and Feathers' *Working Effectively with Legacy Code* {cite}`feathers2004legacy` supply the vocabulary for why this matters: this is not a *bad* repository, it is a repository whose harness has accumulated ordinary, survivable debt that will compound if left alone. Lehman's evolution laws {cite}`lehman1980laws` predict exactly this pattern."] = \
    '这份审计稳稳地落在矩阵的左下角：SDD × 护栏、SDD × 梳理、TDD × 护栏、以及 MDD × 缰绳／梳理，是五个最弱的格子。Cunningham 1992 年的"技术债"隐喻 {cite}`cunningham1992debt`，以及 Feathers 的 *Working Effectively with Legacy Code* {cite}`feathers2004legacy`，提供了解释"为什么这很重要"的词汇：这不是一份 *糟糕的* 仓库，而是一份 *其挽具累积了普通可生存之债* 的仓库——任其发展就会复利恶化。Lehman 的演化定律 {cite}`lehman1980laws` 预言的正是这个模式。'

T['Act 2 — Shortcomings'] = '第二幕 —— 缺陷'

T['Five concrete shortcomings, each with a severity label, an evidence pointer, and the matrix-cell coordinate it maps onto:'] = \
    '五项具体缺陷——每一项都附有严重度、证据指针、以及它映射到的矩阵坐标：'

T['**Missing `make prompts-lint`.** `config/prompts.yaml` is committed without schema validation; broken templates can only be found at runtime. (**SDD × Fence**, `major`; evidence `config/prompts.yaml`.)'] = \
    '**缺少 `make prompts-lint`。** `config/prompts.yaml` 未经 schema 校验就被提交；格式被破坏的模板只能在运行时才被发现。（**SDD × 护栏**，`major`；证据 `config/prompts.yaml`。）'

T['**MCP tool schemas are not validated against their handlers.** A handler added without a schema (or vice versa) ships green. (**TDD × Fence**, `major`; evidence `internal/mcp/server.go`, `internal/mcp/handlers.go`.)'] = \
    '**MCP 工具 schema 未与其 handler 做一致性校验。** 新加了一个 handler 却没有 schema（反之亦然）——CI 照样绿灯放行。（**TDD × 护栏**，`major`；证据 `internal/mcp/server.go`、`internal/mcp/handlers.go`。）'

T['**No cost-observability dashboard for LLM calls.** Monthly spend is invisible until the provider bill arrives. (**MDD × Bridle**, `major`; evidence — absence of dashboard config under `deploy/`.)'] = \
    '**LLM 调用没有成本可观测面板。** 月度花销在供应商账单到来之前完全不可见。（**MDD × 缰绳**，`major`；证据是 `deploy/` 下没有任何面板配置。）'

T['**`CLAUDE.md` and `AGENTS.md` have drifted from `openspec/` working notes.** The two front-door docs reference concepts that no longer exist and fail to reference concepts that now do. (**SDD × Groom**, `minor`; evidence `CLAUDE.md`, `AGENTS.md`, `openspec/`.)'] = \
    '**`CLAUDE.md` 与 `AGENTS.md` 已与 `openspec/` 工作笔记漂移。** 这两份"门面文档"引用了已经不存在的概念，却没有引用现在已经存在的概念。（**SDD × 梳理**，`minor`；证据 `CLAUDE.md`、`AGENTS.md`、`openspec/`。）'

T['**No pre-commit hook guarding against committed secrets.** `.env` files are ignored but the hook safety net is absent. (**TDD × Fence** / **MDD × Bridle** joint, `critical`; evidence absence of `.pre-commit-config.yaml` at repo root.)'] = \
    '**没有 pre-commit 钩子来拦住"被提交进来的密钥"。** `.env` 文件已被 gitignore 忽略，但作为安全网的钩子层整个缺席。（**TDD × 护栏** 与 **MDD × 缰绳** 联合，`critical`；证据：仓库根目录不存在 `.pre-commit-config.yaml`。）'

T["Adzic's *Specification by Example* {cite}`adzic2011specbyexample` and DORA metrics {cite}`forsgren2018accelerate` frame the remediation: each shortcoming should turn into an executable gate whose presence or absence is itself a measured metric."] = \
    'Adzic 的 *Specification by Example* {cite}`adzic2011specbyexample` 与 DORA 度量 {cite}`forsgren2018accelerate`，框定了补救工作的方向：每一项缺陷，都要被转化为一道可执行关卡——它的存在或缺席，本身就成为一条被度量的指标。'

T['Act 3 — Applying Harness Engineering'] = '第三幕 —— 把挽具工程真正落下去'

T['Four fixes land on `main`, each scoped to a single matrix cell and referenced by commit SHA. The commit-SHA slots below are populated when Section 14 lands; the book-lint script walks them through `git cat-file -e` on every build.'] = \
    '四项修复合入 `main`，每一项都收束到单一矩阵格子上，并以 commit SHA 为引用。下文的 SHA 槽位会在第 14 节合入时填入；book-lint 脚本在每次构建时都会用 `git cat-file -e` 遍历它们。'

T['Fix'] = '修复'
T['Cell'] = '格子'
T['Severity'] = '严重度'
T['Commit SHA'] = 'Commit SHA'

T['`make prompts-lint` + `scripts/prompts_lint.py`'] = \
    '`make prompts-lint` ＋ `scripts/prompts_lint.py`'
T['SDD × Fence'] = 'SDD × 护栏'
T['major'] = 'major'
T['`<TBD>` (§14.1)'] = '`<待定>`（§14.1）'

T['MCP tool schema-vs-handler consistency check'] = \
    'MCP 工具的 "schema vs handler" 一致性检查'
T['TDD × Fence'] = 'TDD × 护栏'
T['`<TBD>` (§14.2)'] = '`<待定>`（§14.2）'

T['`openspec/docs/sources-of-truth.md` index reconciling `CLAUDE.md` + `AGENTS.md`'] = \
    '`openspec/docs/sources-of-truth.md` 索引，用以调和 `CLAUDE.md` ＋ `AGENTS.md`'
T['SDD × Groom'] = 'SDD × 梳理'
T['minor'] = 'minor'
T['`<TBD>` (§14.3)'] = '`<待定>`（§14.3）'

T['`.pre-commit-config.yaml` baseline with gitleaks + `make secrets-check`'] = \
    '带 gitleaks ＋ `make secrets-check` 的 `.pre-commit-config.yaml` 基线'
T['TDD × Fence joint MDD × Bridle'] = 'TDD × 护栏 联合 MDD × 缰绳'
T['critical'] = 'critical'
T['`<TBD>` (§14.4)'] = '`<待定>`（§14.4）'

T["Each PR description references this chapter by name (`book — Ch.11 Act 3`) and carries a one-line *HarnessCard delta* note saying which cell's score moves and by how much."] = \
    '每一份 PR 的描述里，都按名引用本章（`book — Ch.11 Act 3`），并附上一行 *HarnessCard delta* 说明：哪一格的分数在动、动了多少。'

T['Act 4 — Measuring the Delta'] = '第四幕 —— 丈量增量'

T['A second HarnessCard, authored after the Act 3 commits land, diffs cell scores against Act 1 and reports quantitative deltas:'] = \
    '在第三幕的 commit 合入之后，写出第二份 HarnessCard，把格子得分与第一幕做 diff，并报告量化增量：'

code_40_en = '''<!-- verified: 2026-04-17 · Ch.11 Act 4 · Measuring the Delta -->

# HarnessCard — Act 4 (Post-fix)

**Subject.** `walterfan/lazy-ai-coder`, end-of-Act-3 commit SHA:
`<TBD — captured at §14 landing>`.

**Date.** 2026-04-17 (post-fix, to be re-verified at §14 landing).

**Schema version.** CAR-HarnessCard v0.2.

| Cell            | Act 1 | Act 4 | Delta | Fix                                   |
|-----------------|-------|-------|-------|---------------------------------------|
| SDD × Bridle    | 3     | 3     | 0     | (unchanged in §14 scope)              |
| SDD × Fence     | 1     | 4     | +3    | `make prompts-lint` + schema validator |
| SDD × Paddock   | 2     | 2     | 0     | (unchanged)                           |
| SDD × Groom     | 1     | 3     | +2    | `openspec/docs/sources-of-truth.md` index |
| TDD × Bridle    | 2     | 2     | 0     | (unchanged)                           |
| TDD × Fence     | 1     | 4     | +3    | MCP schema check + gitleaks pre-commit |
| TDD × Paddock   | 3     | 3     | 0     | (unchanged)                           |
| TDD × Groom     | 2     | 2     | 0     | (unchanged)                           |
| MDD × Bridle    | 1     | 1     | 0     | (out of §14 scope)                    |
| MDD × Fence     | 2     | 2     | 0     | (unchanged)                           |
| MDD × Paddock   | 2     | 2     | 0     | (unchanged)                           |
| MDD × Groom     | 1     | 1     | 0     | (unchanged)                           |

**SDD mean.** 1.75 → 3.0 (+1.25).
**TDD mean.** 2.0 → 2.75 (+0.75).
**MDD mean.** 1.5 → 1.5 (+0.0).
**Overall.** 1.75 → 2.42 (+0.67).

## Quantitative metrics

| Metric                       | Act 1 | Act 4 | Delta |
|------------------------------|-------|-------|-------|
| prompts-lint rule count      | 0     | 7     | +7    |
| MCP schema mismatches at CI  | N/A   | 0     | —     |
| secrets-scan coverage (% committed files) | 0     | 100   | +100  |
| `sources-of-truth.md` entries | 0     | ≥ 6   | +6    |
'''
code_40_zh = '''<!-- verified: 2026-04-17 · Ch.11 Act 4 · Measuring the Delta -->

# HarnessCard —— 第四幕（修复后）

**对象。** `walterfan/lazy-ai-coder`，第三幕收官时的 commit SHA：
`<待定 —— §14 合入时登记>`。

**日期。** 2026-04-17（修复后，§14 合入时会再校验一次）。

**Schema 版本。** CAR-HarnessCard v0.2。

| 格子            | 第一幕 | 第四幕 | Delta | 修复                                       |
|-----------------|--------|--------|-------|--------------------------------------------|
| SDD × 缰绳      | 3      | 3      | 0     | （不在 §14 范围内，未变）                  |
| SDD × 护栏      | 1      | 4      | +3    | `make prompts-lint` ＋ schema validator   |
| SDD × 牧场      | 2      | 2      | 0     | （未变）                                   |
| SDD × 梳理      | 1      | 3      | +2    | `openspec/docs/sources-of-truth.md` 索引   |
| TDD × 缰绳      | 2      | 2      | 0     | （未变）                                   |
| TDD × 护栏      | 1      | 4      | +3    | MCP schema 检查 ＋ gitleaks pre-commit     |
| TDD × 牧场      | 3      | 3      | 0     | （未变）                                   |
| TDD × 梳理      | 2      | 2      | 0     | （未变）                                   |
| MDD × 缰绳      | 1      | 1      | 0     | （不在 §14 范围内）                        |
| MDD × 护栏      | 2      | 2      | 0     | （未变）                                   |
| MDD × 牧场      | 2      | 2      | 0     | （未变）                                   |
| MDD × 梳理      | 1      | 1      | 0     | （未变）                                   |

**SDD 均值。** 1.75 → 3.0（+1.25）。
**TDD 均值。** 2.0 → 2.75（+0.75）。
**MDD 均值。** 1.5 → 1.5（+0.0）。
**总分。** 1.75 → 2.42（+0.67）。

## 量化指标

| 指标                          | 第一幕 | 第四幕 | Delta |
|-------------------------------|--------|--------|-------|
| prompts-lint 规则条数         | 0      | 7      | +7    |
| CI 上的 MCP schema 不一致数   | N/A    | 0      | —     |
| secrets 扫描覆盖率（已提交文件占比，%） | 0      | 100    | +100  |
| `sources-of-truth.md` 条目数  | 0      | ≥ 6    | +6    |
'''
T[code_40_en] = code_40_zh

T['Two quantitative metrics are *required* by the chapter contract; the hands-on HarnessCard reports four:'] = \
    '本章契约 *要求* 至少两条量化指标；hands-on 版的 HarnessCard 报告了四条：'

T['**prompts-lint rule count**: 0 → 7.'] = '**prompts-lint 规则条数**：0 → 7。'
T['**MCP schema mismatches at CI**: N/A → 0 (new check).'] = \
    '**CI 上的 MCP schema 不一致数**：N/A → 0（全新检查）。'
T['**secrets-scan coverage (% committed files)**: 0 → 100.'] = \
    '**secrets 扫描覆盖率（已提交文件占比，%）**：0 → 100。'
T['**`sources-of-truth.md` entries**: 0 → ≥ 6.'] = \
    '**`sources-of-truth.md` 条目数**：0 → ≥ 6。'

T["The overall HarnessCard mean rises from 1.75 to 2.42 — a +0.67 improvement concentrated in the two Fence cells (+3 each) and SDD × Groom (+2). Act 4 deliberately does not touch the MDD row; Chapter 12's 30/60/90 plan picks it up in the next quarter."] = \
    'HarnessCard 总均值从 1.75 升到 2.42 —— +0.67 的改善集中落在两个"护栏"格（各 +3）和 SDD × 梳理（+2）上。第四幕刻意不动 MDD 那一行；第 12 章的 30/60/90 计划会在下一个季度接手。'

T['What the delta does *not* prove'] = '这个 delta *不能* 证明什么'

T['Four Act-3 commits raised the HarnessCard mean by 0.67. That is a real number, and it is also a *bounded* number — worth reading carefully before quoting it as evidence of a harness working.'] = \
    '第三幕的四个 commit，把 HarnessCard 均值抬升了 0.67。这是一个真实的数字，也是一个 *有边界* 的数字——在把它当作"挽具在起作用"的证据去引用之前，值得先仔细读清楚。'

T["**The delta measures inputs, not outcomes.** Rising cell scores mean the repository now has artefacts that the scoring rubric credits; they do not yet mean the agent's output has improved. The DORA-style outcome metrics (deployment frequency, change failure rate, mean time to recovery) are the evidence that the inputs paid off — Chapter 12's 90-day review is where those outcomes are expected to move, not the Act-4 snapshot."] = \
    '**这个 delta 度量的是投入，不是产出。** 格子得分上升，意味着仓库里多了一批"评分尺会给分"的制品；它还不等于智能体的输出变好了。DORA 风格的产出指标（部署频率、变更失败率、平均恢复时间），才是"投入有所回报"的证据——第 12 章的 90 天复盘，才是期望这些产出真正移动的时点，而不是第四幕的这张快照。'

T['**The scorer and the author are the same person.** Act 1\'s baseline and Act 4\'s re-score were both authored by the same engineer, using the same rubric, with full knowledge of what changed. This is honest for a self-audit but it is not independent verification — the scores are calibration, not measurement. A reader reproducing the pattern on their own repo should expect a similar bias in their own deltas.'] = \
    '**打分人与作者是同一个人。** 第一幕的基线与第四幕的重评，都由同一位工程师执笔，用同一把评分尺，且对"改了什么"心知肚明。这对于"自审计"来说是诚实的，但不是独立验证——这些分数是校准，不是度量。读者在自己仓库上复制这套模式时，应预期自己也会有类似偏置。'

T['**Three of four fixes are Fence-shaped.** Fence cells rise most easily because refusal is mechanical and measurable. Bridle and Paddock cells rise more slowly because they require changes in what humans and agents *do*, not just what the CI refuses. A HarnessCard mean dominated by Fence gains is an honest first-quarter pattern; a HarnessCard whose delta is *only* Fence across four quarters is a team investing in refusals without raising intent or acceptance.'] = \
    '**四项修复里有三项是"护栏"形的。** 护栏格最容易抬分——因为"拒绝"是机械且可测的。缰绳格和牧场格抬得更慢——因为它们需要改变人和智能体所 *做* 的事，不是仅仅改变 CI 拒绝什么。一份 HarnessCard 的均值主要由"护栏收益"主导，在第一个季度里是一种诚实的模式；但一份 *连续四个季度* 其 delta *只有* 护栏的 HarnessCard，则是一支"只投资于拒绝、却未抬升意图与验收"的团队的画像。'

T['Pitfall — HarnessCard vanity delta'] = '陷阱 —— HarnessCard 虚荣增量'

T["A team runs the Chapter 11 playbook, lands four Fence commits, and reports a +0.67 mean delta to leadership. Leadership is pleased. Two quarters later, outcome metrics have not moved; the team doubles down and lands four more Fence commits; the mean rises again. The harness grows; the outcomes do not. **Why**: the HarnessCard is a *diagnostic* — its role is to identify weak cells, not to be optimised against. A team that optimises for the score rather than the outcome is running a variant of Goodhart's law (Cunningham's debt metaphor {cite}`cunningham1992debt` applied in reverse: you *can* pay down debt that was not costing anything). **Symptom**: cell scores rise, dashboards do not; retros describe harness work warmly, incidents describe product work painfully. **Fix**: pair every HarnessCard delta with one outcome metric it is *predicted* to move. If the outcome does not move after a quarter, the delta was vanity and the next quarter's investment should go to a different cell (or a different dimension entirely)."] = \
    '一支团队跑完第 11 章的 playbook，合入了四个"护栏"commit，向上汇报 +0.67 的均值 delta。领导很满意。两个季度之后，产出指标一动未动；这个团队于是加码，又合入四个"护栏"commit；均值再次上升。挽具在长胖；产出没在长。**为什么**：HarnessCard 是一份 *诊断* —— 它的角色是"识别弱格"，不是"被优化的对象"。一支为"分数"而非"产出"优化的团队，在跑的是 Goodhart 律的一个变种（Cunningham 的债务隐喻 {cite}`cunningham1992debt` 反着用一次：你 *确实* 可以去还一笔本来根本没在收利息的债）。**症状**：格子得分在涨，仪表盘没在涨；回顾会上对"挽具工作"描述得温情脉脉，事故复盘里对"产品工作"描述得痛不欲生。**解法**：每一项 HarnessCard delta 都要配一项它 *被预言会移动* 的产出指标。若一个季度后该产出未移动，则这份 delta 属于虚荣；下一季度的投资应该换到另一格（或彻底换一个维度）。'

T['Reading list extension'] = '阅读单扩展'

T["Act 4's reproducibility claim rests on a short shell script that runs the three new make targets against a fresh clone at the Act-4 SHA:"] = \
    '第四幕的可复现性主张，建立在一段简短 shell 脚本之上——它针对"第四幕 SHA"处的一份全新 clone，跑三个新的 make 目标：'

code_56 = '''#!/usr/bin/env bash
# verified: 2026-04-17 · Ch.11 hands-on · reproduce the HarnessCard delta
# Run from a fresh clone of walterfan/lazy-ai-coder at the Act-4 SHA.
set -euo pipefail

# 1. SDD × Fence — prompts-lint validates config/prompts.yaml
make prompts-lint

# 2. TDD × Fence — MCP tool schema-vs-handler consistency check
make mcp-schema-check

# 3. TDD × Fence — pre-commit hooks refuse secrets
make secrets-check

echo "If all three targets exited 0, the harness is at its Act-4 score."
'''
T[code_56] = code_56

T['The matching `pre-commit-config.yaml` baseline from §14.4 is shipped alongside for readers who want to lift it verbatim:'] = \
    '§14.4 里那份配套的 `pre-commit-config.yaml` 基线，也一并交付，方便想原样拿走的读者：'

code_58 = '''# verified: 2026-04-17 · Ch.11 hands-on · symlink-safe copy of the final pre-commit config
# To be landed on main as part of §14.4.
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - {id: trailing-whitespace}
      - {id: end-of-file-fixer}
      - {id: check-yaml}
      - {id: detect-private-key}
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.4
    hooks: [{id: gitleaks}]
  - repo: local
    hooks:
      - id: prompts-lint
        name: prompts-lint
        entry: python scripts/prompts_lint.py config/prompts.yaml
        language: system
        pass_filenames: false
      - id: mcp-schema-check
        name: mcp-schema-check
        entry: go run ./cmd/mcp-schema-check
        language: system
        pass_filenames: false
'''
T[code_58] = code_58

T['Research Foundations'] = '研究脉络'

T['**Technical debt** {cite}`cunningham1992debt` — vocabulary for Act 1.'] = \
    '**技术债** {cite}`cunningham1992debt` —— 第一幕的词汇来源。'
T['**Legacy code** {cite}`feathers2004legacy` — remediation patterns for Act 2.'] = \
    '**遗留代码** {cite}`feathers2004legacy` —— 第二幕的补救模式。'
T['**DORA / Accelerate** {cite}`forsgren2018accelerate` — the metric lineage behind Act 4.'] = \
    '**DORA ／ Accelerate** {cite}`forsgren2018accelerate` —— 第四幕所依据的度量谱系。'
T['**Evolution laws** {cite}`lehman1980laws` — why the overall mean continues to drift without Groom investment.'] = \
    '**演化定律** {cite}`lehman1980laws` —— 为什么一旦停止"梳理"投资，总均值就会持续漂移。'

T['Hands-On'] = '动手环节'

T['Four copyable artefacts live under `book/source/_handson/11-lazy-ai-coder/`:'] = \
    '在 `book/source/_handson/11-lazy-ai-coder/` 下，住着四份可直接拷走的制品：'

T['`HarnessCard-Act1.md` — pre-fix baseline.'] = \
    '`HarnessCard-Act1.md` —— 修复前的基线。'
T['`HarnessCard-Act4.md` — post-fix re-audit with delta.'] = \
    '`HarnessCard-Act4.md` —— 修复后的再审计，含 delta。'
T['`reproduce.sh` — three `make` targets, one script.'] = \
    '`reproduce.sh` —— 三个 `make` 目标，一段脚本。'
T['`pre-commit-config.yaml` — symlink-safe copy of the final baseline.'] = \
    '`pre-commit-config.yaml` —— 最终基线的 symlink-safe 拷贝。'

T['When §14\'s commits land on `main`, the HarnessCards are re-scored against the actual SHAs, the chapter flips to `status: complete`, and the toctree picks it up.'] = \
    '当 §14 的那批 commit 合入 `main`，HarnessCard 将针对真实 SHA 重新打分、本章状态翻为 `status: complete`，toctree 也随之将它收入。'


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
        print('  MISS:', repr(m[:180]))
    po2 = polib.pofile(PATH)
    remaining = [e for e in po2 if not e.msgstr and not e.obsolete]
    print(f'remaining: {len(remaining)}')


if __name__ == '__main__':
    main()
