"""One-shot translator for Ch.06 Operating a Harness."""
import polib

PATH = 'source/locale/zh_CN/LC_MESSAGES/chapters/06-operating-a-harness.po'
T = {}

T['Operating a Harness: Entropy, Observability, Approval Gates, Meta-Harness Evolution'] = \
    '运行一具挽具：熵、可观测性、审批关卡与元挽具演进'

T['*A harness is not a project you ship; it is an environment you tend.*'] = \
    '*挽具不是一件交付就完事的项目，它是一片你要持续照料的环境。*'

T['Chapter 05 rendered the twelve cells as a static matrix. This chapter answers the operational question the matrix leaves open: once the cells are filled, what does *Monday through Friday* look like? The answer organises around four concerns — **entropy management**, **observability practice**, **approval gates**, **meta-harness evolution** — and draws three structural patterns directly from the `lazy-scrum-team` workflow repository that Chapter 09 treats in full.'] = \
    '第 05 章把那十二个格子画成了一张静态矩阵。本章回答矩阵留下的运行层问题：格子被填满之后，*周一到周五* 究竟是什么样子？答案围绕四项关切组织——**熵管理**、**可观测性实践**、**审批关卡**、**元挽具演进**——并直接从第 09 章将要完整讨论的 `lazy-scrum-team` 工作流仓库里借来三种结构性的模式。'

T['Concern 1 — Entropy management'] = '关切一 —— 熵管理'

T['What it is'] = '这是什么'

T["Every harness accumulates entropy: stale `verified:` headers, dead links in `AGENTS.md`, npm dependencies two minor versions behind the upstream audit feed, Rust crates whose `cargo audit` flags fired last week and were silently closed. Left alone, entropy turns a working harness into a *decorative* one — the files still exist, reviewers still tick the boxes, but the agent and the humans both route around them. Cunningham's 1992 technical-debt metaphor {cite}`cunningham1992debt` and Tom et al.'s 2013 systematic review {cite}`tom2013debtinterest` both apply, but this chapter calls the phenomenon *entropy* specifically to stress that the harness decays even when the code it wraps does not."] = \
    '每一具挽具都在累积熵：过期的 `verified:` 头、`AGENTS.md` 里的死链、比上游审计源落后两个 minor 版本的 npm 依赖、上周 `cargo audit` 报警而后被悄悄关掉的 Rust crate。放任不管，熵会把一具能工作的挽具变成一具 *装饰性* 的挽具——文件还在、评审人还在打勾，但智能体和人都绕着它走。Cunningham 1992 年提出的技术债比喻 {cite}`cunningham1992debt`、以及 Tom 等人 2013 年的系统综述 {cite}`tom2013debtinterest` 都适用，但本章特意把这种现象叫做 *熵*，以强调：即便挽具所包裹的代码并未衰变，挽具本身仍在衰变。'

T['Day-to-day practice'] = '日常做法'

T["Entropy is controlled by two recurring jobs: a **doc-sync check** that refuses merges when docs and code drift (`doc-sync-check.sh` below), and a **weekly audit workflow** that runs `cargo audit` / `npm audit` / `gitleaks` in a single pass and writes a dated report under `reports/`. Two reports that diff are *the* entropy signal; teams that do not keep two weeks of reports cannot tell entropy from the weather."] = \
    '熵靠两项反复运行的作业来压住：一条 **文档同步检查**——当文档与代码漂移时拒绝合并（下方的 `doc-sync-check.sh`），以及一条 **每周审计工作流**——在一遍流水里跑完 `cargo audit`／`npm audit`／`gitleaks`，并在 `reports/` 下写一份带日期的报告。两份报告之间的 diff，就是 *那条* 熵信号；不保留至少两周报告的团队，没法把熵和天气分开。'

code_8 = '''#!/usr/bin/env bash
# verified: 2026-04-17 · entropy · refuse the merge when docs and code drift
set -euo pipefail

# Any source file touched in this MR that has a docstring-exposed API must
# also have been listed in the MR's doc-update checklist.
changed=$(git diff --name-only origin/main...HEAD)
undoc=$(python scripts/which_need_docs.py <<<"$changed" || true)
if [ -n "$undoc" ]; then
  echo "::error::the following changed files export public symbols but have no matching doc update:"
  echo "$undoc"
  exit 1
fi
'''
T[code_8] = code_8

code_9 = '''# verified: 2026-04-17 · entropy · weekly dep/secret audit — .github/workflows/entropy-audit.yml
name: entropy-audit
on:
  schedule: [{cron: "0 8 * * MON"}]  # every Monday 08:00 UTC
  workflow_dispatch:

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: cargo audit
        run: cargo install cargo-audit --locked && cargo audit
      - name: npm audit
        run: npm audit --audit-level=moderate || true
      - name: gitleaks
        uses: gitleaks/gitleaks-action@v2
      - name: write weekly report
        run: python scripts/entropy_report.py > reports/entropy-$(date +%F).md
'''
T[code_9] = code_9

T["The deeper mechanism is **differential decay**. The code's entropy is paid for by every bug, every review comment, every failed build — thousands of small pressures keeping it close to reality. The harness's entropy is paid for by *nothing*: a stale `AGENTS.md` rule does not crash anything, it just silently mis-steers. Over a quarter the two diverge — the code stays current, the harness drifts — and the harness's rot is the most invisible kind precisely because it is not self-announcing. That is why Groom is a column, not a footnote."] = \
    '更深一层的机制，叫 **差分衰减**。代码的熵，由每一条 bug、每一条评审意见、每一次构建失败来偿还——成千上万股小的压力让它贴近现实。而挽具的熵，由 *没有任何东西* 偿还：一条过期的 `AGENTS.md` 规则不会崩任何东西，它只会悄无声息地把方向引偏。一个季度下来，两者发散——代码保持当下，挽具开始漂移——而挽具的腐烂是最看不见的那种腐烂，恰恰因为它不会自己喊出来。这就是梳理为什么是一 *列* 而不是一条脚注。'

T['Pitfall — "We will audit when things break"'] = '陷阱——"出了事再审计"'

T['A team postpones the weekly entropy audit because "nothing is on fire". Six months later something is on fire: a dependency with a known CVE shipped to production, traced back to a `npm audit` warning from March that nobody saw because there was no weekly report to compare against April\'s. **Why**: entropy audits are *calibration*, not diagnosis — their value comes from producing a baseline week-to-week. A team that only runs the audit during incidents has no baseline, so the audit output reads as noise. **Symptom**: CVE patch turnaround is measured in months not days; `npm audit --audit-level=high` returns dozens of findings with no opinion on which are new; the first action in every incident is "let\'s check if we had warnings for this". **Fix**: the audit runs on a calendar, even (especially) when nothing is wrong; the dated `reports/` directory is the baseline; the weekly diff is the signal.'] = \
    '一支团队推迟每周的熵审计，因为"没什么在着火"。六个月后真的着火了：一条带已知 CVE 的依赖被带到了生产，一路回溯，发现三月份就有一条 `npm audit` 告警——没人看见，因为当时没有周报可以和四月份那份对照。**为什么**：熵审计是 *校准*，不是诊断——它的价值来自于"一周一周产生基线"。只在事故期间跑审计的团队，没有基线，审计输出就读成噪声。**症状**：CVE 的修复周转以月计而非以天计；`npm audit --audit-level=high` 返回几十条结果，却没有意见说哪些是新增的；每次事故的第一步都是"我们来看看当时有没有告警"。**解法**：审计按日历跑，*即便*（尤其是）没事的时候也跑；带日期的 `reports/` 目录就是基线；周与周之间的 diff 才是信号。'

T['Concern 2 — Observability practice'] = '关切二 —— 可观测性实践'

T["Observability in a harness context means three surfaces are continuously readable {cite}`majors2022observability`: (a) production SLIs the product team already watches, (b) harness-internal signals the product team usually doesn't — token cost, cache hit rate, agent turns-to-green {cite}`langchain2026tbench` — and (c) *spec-observance* signals that compare the `AGENTS.md` surface against the behaviour seen in logs."] = \
    '在挽具的语境里，可观测性意味着三面被持续可读 {cite}`majors2022observability`：(a) 产品团队本来就在盯的生产 SLI；(b) 产品团队通常 *不* 盯的那类挽具内部信号——token 成本、缓存命中率、智能体 turns-to-green {cite}`langchain2026tbench`；(c) *规约遵循度* 信号——把 `AGENTS.md` 这张面，与日志里看到的行为对起来比。'

T["A minimal observability setup starts with exposing Claude Code's `/cost` endpoint to Prometheus and letting the existing dashboards stack do the rest. The exercise is three lines of scrape config, not a platform redesign:"] = \
    '一份最小化的可观测性配置，从把 Claude Code 的 `/cost` 端点暴露给 Prometheus 开始，剩下的交给现有的 dashboard 栈去做。这事是三行 scrape 配置，不是一次平台重设计：'

code_16 = '''# verified: 2026-04-17 · observability · Prometheus scrape-config for Claude Code /cost
scrape_configs:
  - job_name: claude_code_cost
    metrics_path: /cost
    scrape_interval: 60s
    static_configs:
      - targets: ["localhost:8911"]
    metric_relabel_configs:
      - source_labels: [__name__]
        regex: "cc_(tokens|usd|cache_hits|turns)_total"
        action: keep
'''
T[code_16] = code_16

T['The *cultural* move — more important than the config — is that someone owns the dashboard and speaks to it in the Monday review. Unowned dashboards rot faster than uninstrumented code {cite}`humble2010continuousdelivery`.'] = \
    '比配置更重要的是那一步 *文化* 动作：有一个人成为这块 dashboard 的 owner，在周一的复盘上照着它发言。没有 owner 的 dashboard，腐烂得比没有埋点的代码还快 {cite}`humble2010continuousdelivery`。'

T['Pitfall — The "spec-observance blindspot"'] = '陷阱——"规约遵循度盲区"'

T["A team wires production SLIs to Prometheus, adds cost-per-turn instrumentation, and watches both religiously — but never instruments *spec observance*. Result: when the agent's code silently diverges from `AGENTS.md`'s claims (new writes bypass the repository pattern, new endpoints skip the auth middleware), the dashboards show green across the board because the divergence is not in the product's latency or the agent's cost — it is in the gap between what the spec promises and what the code does. **Symptom**: incidents caused by \"that's not how we do it here\" with no prior dashboard signal; architects complain that the agent \"doesn't follow the rules\" but the rules are not mechanically monitored. **Fix**: for every load-bearing bullet in `AGENTS.md`, ask \"what metric would go non-zero if this bullet were violated?\" If the answer is *none*, the bullet is unenforceable prose and belongs in the documentation folder, not the spec."] = \
    '一支团队把生产 SLI 接到了 Prometheus、加上每轮成本埋点，两头都盯得一丝不苟——却从来没给 *规约遵循度* 做埋点。结果：当智能体的代码悄悄偏离 `AGENTS.md` 的宣称时（新的写操作绕过 repository 模式、新端点跳过认证中间件），所有 dashboard 都是一片绿，因为偏差不在产品延迟里、也不在智能体成本里——它就在"规约承诺的"和"代码做的"之间那条缝里。**症状**：事故起因是"我们这儿不是这么做的"，此前 dashboard 上没有任何信号；架构师抱怨智能体"不守规矩"，可那些规矩从未被机械化监控。**解法**：对 `AGENTS.md` 里每一条承重条目，问一句"若这条被违反，哪条度量会变为非零？"——答案若是 *没有*，那这条就是无法执行的散文，它属于文档目录，不属于规约。'

T['Concern 3 — Approval gates (Hard vs Soft)'] = '关切三 —— 审批关卡（硬 vs 软）'

T['What they are'] = '这是什么'

T['Gates are the points where a human or automated reviewer says *no, not yet*. Two common failure modes are **undeclared gate class** (everyone assumes a gate is hard until someone needs a waiver at 5pm Friday) and **gate evaporation** (a gate that always passes silently disappears from the team\'s mental model). Both are avoided by borrowing three patterns from the `lazy-scrum-team` workflow skill {cite}`lazyscrumteam2026`:'] = \
    '关卡，是人或自动评审者说 *还不行* 的那些点。两种常见失败模式：**关卡类别未声明**（所有人都默认某道关卡是硬关卡，直到周五下午五点有人需要豁免），以及 **关卡蒸发**（一道总是通过的关卡，会悄悄从团队的心智模型里消失）。这两种失败，都可以靠从 `lazy-scrum-team` 工作流技能 {cite}`lazyscrumteam2026` 借来的三种模式来规避：'

T['**Artefact State Model** — draft → review → approved → archived — with explicit transition rules and role-owned invariants. A concrete encoding is shipped as a YAML file readers can adopt:'] = \
    '**制品状态机** —— draft → review → approved → archived —— 带显式的跃迁规则和按角色署名的不变量。这里给出一份可被读者直接采用的 YAML 编码：'

code_24 = '''# verified: 2026-04-17 · approval gates · lazy-scrum-team Artefact State Model
artefact_state_model_version: "0.1"
states: [draft, review, approved, archived]
transitions:
  - {from: draft,     to: review,   trigger: author_submit}
  - {from: review,    to: draft,    trigger: reviewer_request_changes}
  - {from: review,    to: approved, trigger: reviewer_approve}
  - {from: approved,  to: archived, trigger: release_shipped}
  - {from: archived,  to: review,   trigger: reopen_for_change}
invariants:
  - "an approved artefact cannot go back to draft without an archive step"
  - "only the Final Acceptance role can transition review → approved"
'''
T[code_24] = code_24

T['**Rework Matrix** — the finder × fixer matrix naming the rework artefact that must accompany every hand-off. Chapter 09 carries the canonical treatment.'] = \
    '**返工矩阵** —— 一张"发现者 × 修复者"矩阵，命名了每一次交接都必须随附的返工制品。第 09 章会完整讲这个。'

code_26_en = '''<!-- verified: 2026-04-17 · approval gates · who sends what back to whom -->

# Rework Matrix

Rows are *who found the defect*, columns are *who must fix it*. Each cell
names the artefact that makes the hand-off explicit.

|               | PO (spec) | Architect (design) | Dev (code) | Test (acceptance) |
|---------------|-----------|--------------------|------------|-------------------|
| **PO**        | —         | `spec-delta.md`    | —          | `acceptance.md`   |
| **Architect** | —         | —                  | `adr-rework.md` | —             |
| **Dev**       | `spec-question.md` | —         | —          | —                 |
| **Test**      | `acceptance-gap.md` | —        | `bug-report.md` | —            |
| **Final Acc** | `reject-reason.md` | `reject-reason.md` | `reject-reason.md` | — |

A defect never crosses this matrix without a rework artefact attached;
"just fix it" is an anti-pattern.
'''
code_26_zh = '''<!-- verified: 2026-04-17 · approval gates · who sends what back to whom -->

# 返工矩阵

行是 *谁发现了这个缺陷*，列是 *谁必须修它*。每一格都指定了让这次交接
显式化的那件制品。

|               | PO（规约） | Architect（设计）    | Dev（代码）        | Test（验收）       |
|---------------|-----------|----------------------|--------------------|--------------------|
| **PO**        | —         | `spec-delta.md`      | —                  | `acceptance.md`    |
| **Architect** | —         | —                    | `adr-rework.md`    | —                  |
| **Dev**       | `spec-question.md` | —           | —                  | —                  |
| **Test**      | `acceptance-gap.md` | —          | `bug-report.md`    | —                  |
| **Final Acc** | `reject-reason.md` | `reject-reason.md` | `reject-reason.md` | —               |

一个缺陷穿过这张矩阵时，绝不能不随附返工制品；
"你就赶紧修一下吧"本身是一种反模式。
'''
T[code_26_en] = code_26_zh

T['**Hard vs Soft Gates** — every gate declares its class at creation, and soft-gate waivers carry a named role and an expiry. The canonical enumeration lives in Chapter 09; the template reproduced here is sufficient for most new harnesses:'] = \
    '**硬关卡 vs 软关卡** —— 每一道关卡在创建时就要声明自己的类别；软关卡的豁免必须带上署名角色和到期时间。完整枚举在第 09 章；这里复刻一份模板，对多数新挽具已够用：'

code_28_en = '''<!-- verified: 2026-04-17 · approval gates · Hard vs Soft classification -->

# Hard vs Soft Gates

Every gate must declare its class at creation time. Misclassification is
the leading cause of gate evaporation.

| Gate kind       | Example                          | Class | Bypass policy                       |
|-----------------|----------------------------------|-------|-------------------------------------|
| unit-test suite | `pytest -q`                      | Hard  | never bypass; fix test or revert     |
| lint            | `ruff check .`                   | Hard  | never bypass for new code            |
| coverage floor  | `coverage >= 80%`                | Soft  | waivable by Architect + reason       |
| cost cap        | `cost/turn ≤ $0.03`              | Soft  | waivable for 24h by MDD owner        |
| secrets scan    | `gitleaks`                       | Hard  | never bypass; rotate the secret      |
| docs link-check | `make book-linkcheck`            | Soft  | waivable if external site is down    |

Soft-gate waivers get a `waiver: <role>, <expiry>` entry in the PR body.
'''
code_28_zh = '''<!-- verified: 2026-04-17 · approval gates · Hard vs Soft classification -->

# 硬关卡 vs 软关卡

每一道关卡，都必须在创建时声明它的类别。误分类，是关卡蒸发最首要的
原因。

| 关卡类型         | 例子                              | 类别 | 绕过策略                            |
|------------------|-----------------------------------|------|-------------------------------------|
| 单元测试         | `pytest -q`                       | 硬   | 永不绕过；要么修测试，要么 revert    |
| lint             | `ruff check .`                    | 硬   | 对新代码，永不绕过                   |
| 覆盖率下限        | `coverage >= 80%`                 | 软   | 可由 Architect 附理由豁免             |
| 成本上限          | `cost/turn ≤ $0.03`               | 软   | 可由 MDD owner 豁免 24h              |
| 密钥扫描          | `gitleaks`                        | 硬   | 永不绕过；轮换那把密钥                |
| 文档 link-check  | `make book-linkcheck`             | 软   | 若外部站点挂了，可豁免                |

软关卡的豁免，要在 PR body 里留下 `waiver: <role>, <expiry>` 条目。
'''
T[code_28_en] = code_28_zh

T['Pitfall — Gate fatigue and the "always-waive" drift'] = '陷阱——关卡疲劳与"永远豁免"漂移'

T['A team starts with tight gates. After six weeks, three gates fire routinely on legitimate changes that fall outside their original scope; waivers accumulate; the Soft gate default quietly becomes *waive first, investigate if something breaks*. Within a quarter, Soft gates are telemetry at best — they report what was waived, not what was refused. **Why**: gates that fire with a false-positive rate above roughly 20% lose their psychological authority; the reviewer\'s default flips from *challenge the change* to *challenge the gate*. Once flipped, it does not flip back without an explicit reset. **Symptoms**: waiver count per sprint rises monotonically; "exception for this one" becomes a recognised phrase; new joiners learn that the gate is bypassable before they learn what it was for. **Fix**: track waiver-rate as a first-class metric (every Soft gate\'s waiver rate is itself an MDD signal); when a gate\'s rate crosses 20%, *tighten the scope of the gate* (reduce its surface area until it only fires on actual violations) rather than loosening the policy. A gate that only fires when it should is a gate the team defends; a gate that fires constantly is a gate the team routes around.'] = \
    '一支团队以很紧的关卡起步。六周之后，有三道关卡会在超出它原始范围的合法改动上经常触发；豁免在累积；软关卡的默认值悄悄变成 *先豁免，万一出事再查*。一个季度之内，软关卡充其量只是一层 telemetry——它报告的是什么被豁免，而不是什么被拒绝。**为什么**：误报率大约超过 20% 的关卡会失去心理权威；评审人的默认动作，会从 *质疑这个改动* 翻转为 *质疑这道关卡*。一旦翻转，不经过一次显式重置，它不会再翻回来。**症状**：每个 sprint 的豁免数单调上升；"这一次就破例一下"变成一句大家都懂的口头禅；新人学会这道关卡可以被绕过，比学会它是干什么用的更早。**解法**：把豁免率当作一等度量追踪（每一道软关卡的豁免率本身，就是一条 MDD 信号）；当某道关卡的豁免率越过 20%，*把这道关卡的覆盖范围收紧*（削小它的面积，直到它只在真正的违规上触发），而不是放松策略。一道只在该触发时才触发的关卡，是团队会捍卫的关卡；一道一直在触发的关卡，是团队会绕着走的关卡。'

T['Concern 4 — Meta-harness evolution'] = '关切四 —— 元挽具演进'

T["A harness that cannot update itself is a harness locked to its first author's 2024 model of the world. Meta-evolution is the practice of treating the harness as *its own first-class product*: it has releases, it has a changelog, it has metrics about itself, and it upgrades on a cadence rather than on a panic. Ford, Parsons & Kua's evolutionary architecture {cite}`ford2017buildingevolutionary` and Lehman's evolution laws {cite}`lehman1980laws` are the theoretical backing."] = \
    '一具不能自我更新的挽具，是一具被锁死在它最初作者 2024 年那份世界模型里的挽具。元演进，就是把这具挽具当作 *它自己的一等产品* 来看待：它有 release、它有 changelog、它有关于自己的度量、它按节奏升级，而不是一慌就升。Ford／Parsons／Kua 的演化式架构 {cite}`ford2017buildingevolutionary` 与 Lehman 的演化律 {cite}`lehman1980laws`，是这件事的理论靠山。'

T['Meta-evolution is cheap if you do it as a *habit* and catastrophic if you do it as a *project*. The habit looks like:'] = \
    '把元演进作为 *习惯* 来做，成本很低；作为 *项目* 来做，则是灾难。习惯的样子是：'

T["Every HarnessCard update lands as a PR to the harness's own repository, with the same review discipline as production code."] = \
    'HarnessCard 的每一次更新，都以一个 PR 的形式落到挽具自己的仓库里，享有与生产代码同等的评审纪律。'

T['The harness ships a `CHANGELOG.md` dedicated to the harness (not the product), listing every bridle / fence / paddock / groom change.'] = \
    '挽具配备一份专属于挽具（不是产品）的 `CHANGELOG.md`，列出每一次缰绳／护栏／牧场／梳理的变更。'

T['Once a quarter, the team runs a *HarnessCard review* and sets one explicit cell-level goal for the next quarter.'] = \
    '每季度一次，团队跑一场 *HarnessCard 评审*，为下个季度设定一项显式的、格子级的目标。'

T['Pitfall — The meta-harness infinite regress'] = '陷阱——元挽具的无穷倒退'

T['A team takes "the harness is a product" seriously and proposes a *meta-harness*: a harness to govern how the harness evolves. Then a meta-meta-harness to audit the meta-harness. Within two sprints the team has a tower of YAML files that reviewers cannot distinguish, none of which correspond to a production signal, and the original harness has not moved. **Why**: every layer of meta adds review cost without adding enforcement — the meta-harness\'s rules are aspirational because there is no meta-meta *fence* that refuses bad meta changes. The regress resolves only if you anchor at a concrete production signal. **Fix**: stop at one level. The harness governs the agent; the team governs the harness; the harness\'s own PR review discipline is sufficient self-governance. If you feel the pull toward a meta-harness, instead ask: which production signal would tell us the harness has degraded? That signal, wired into a weekly review, is the only meta-layer worth having.'] = \
    '一支团队把"挽具本身就是一件产品"认真起来，然后提出一具 *元挽具*：一具用来治理"挽具如何演进"的挽具。再接着是一具 meta-meta-harness，用来审计这具元挽具。两个 sprint 之内，团队已经拥有一座评审人分不清层次的 YAML 塔，没有哪一层对应到任何一条生产信号，而原来那具挽具一步也没动。**为什么**：多一层"meta"只多出评审成本、不多出强制力——元挽具里的规则是愿望式的，因为没有任何一层 meta-meta *护栏* 去拒绝坏的 meta 变更。这种倒退，只有当你锚定在一条具体生产信号上时，才会收敛。**解法**：只做一层就打住。挽具治理智能体；团队治理挽具；挽具自身那套 PR 评审纪律，已经够做自治。如果你感到有股拉力在把你往"元挽具"那边拽，请改问：哪一条生产信号能告诉我们"这具挽具已经退化"了？那条信号，接到每周复盘里，就是唯一值得拥有的一层 meta。'

T['The "harness theatre" failure, named'] = '"挽具剧场"那种失败，给它起个名字'

T['Chapter 01 promised this chapter would name the failure mode in which a harness grows but its leverage does not. That mode is *harness theatre*, and it has a reliable diagnostic: the ratio of **harness-shaped artefacts** to **refused artefacts per week**. A healthy harness refuses something on most days — a commit, a tool call, a PR, a waiver request. A theatrical harness refuses nothing for weeks while its file count grows. The canonical question to ask in the Monday review is not *"what did we add to the harness?"* but *"what did the harness refuse, and was it right to refuse it?"* Teams that cannot answer the second question should not be adding to the first.'] = \
    '第 01 章承诺过，本章会给一种失败模式起个名字：挽具在长大，杠杆却没涨。那种失败模式叫 *挽具剧场*，它有一个可靠的诊断：**挽具型制品** 数与 **每周被拒绝的制品** 数之比。一具健康的挽具，大部分日子里都会拒绝些什么——一次 commit、一次工具调用、一个 PR、一份豁免申请。一具剧场式的挽具，在文件数持续上升的同时，连续数周什么都不拒绝。周一复盘上的经典提问，不是 *"我们给挽具加了什么？"* 而是 *"挽具拒绝了什么？拒绝得对不对？"* 答不出第二个问题的团队，不该给第一个问题加分。'

T['Tauri-Todo: the four concerns in one arc'] = 'Tauri-Todo：一个故事弧里的四项关切'

T['The following hands-on arc stitches all four operating concerns into a single running story using a real Tauri 2 + Rust + TypeScript desktop application. The runnable companion repository is at `walterfan/lazy-todo-app`; the three harness fragments below live at `book/source/_handson/06-operating-a-harness/tauri-todo/` and compose the smallest complete harness for a Tauri app.'] = \
    '下面这段动手故事，用一个真实的 Tauri 2 + Rust + TypeScript 桌面应用，把所有四项运行关切缝进一条连贯的故事弧。可运行的配套仓库在 `walterfan/lazy-todo-app`；下面三段挽具片段住在 `book/source/_handson/06-operating-a-harness/tauri-todo/` 下，合起来构成一具 Tauri 应用所能拥有的最小、但完整的挽具。'

T['Fragment 1 — `CLAUDE.md` (Bridle)'] = '片段 1 —— `CLAUDE.md`（缰绳）'

T["Rust's ownership discipline {cite}`jung2018rustbelt` and Tauri's IPC boundary {cite}`tauri2024security` give the agent two strong structural constraints before the first line of application code is written. The `CLAUDE.md` below turns those constraints into house rules the agent must read on every turn."] = \
    'Rust 的所有权纪律 {cite}`jung2018rustbelt`，以及 Tauri 的 IPC 边界 {cite}`tauri2024security`，在写下应用代码第一行之前，就给智能体提供了两条强结构性约束。下面这份 `CLAUDE.md` 把这些约束，转成智能体每一轮都必须读一遍的家规。'

code_45 = '''<!-- verified: 2026-04-17 · Tauri-Todo worked arc · Bridle -->

# CLAUDE.md — lazy-todo-app (Tauri 2 + Rust + TypeScript)

## Project shape

- Rust crate `src-tauri/` owns IPC, storage, and OS integration.
- TypeScript app in `src/` owns UI and input validation only.
- Never call OS APIs directly from TS; route through `invoke()` to a
  Rust command.

## Agent rules

- Before editing any `.rs` file, read `tests/rust/` if it exists.
- Never add a dependency without `cargo audit` in the same commit.
- Storage writes must go through `src-tauri/src/storage.rs::save()`;
  direct disk writes elsewhere are rejected by `pre-commit`.

## House style

- `pnpm run fmt` before any commit; `cargo fmt && cargo clippy -- -D warnings` too.
- Errors cross the IPC boundary as `TauriError`, never as `Result<_, String>`.
'''
T[code_45] = code_45

T['Fragment 2 — `pre-commit-config.yaml` (Fence)'] = '片段 2 —— `pre-commit-config.yaml`（护栏）'

T["Pre-commit hooks enforce the bridle at the keystroke. The Tauri-specific additions — `cargo clippy -D warnings`, a `cargo audit` at push time, and a `gitleaks` hook — make the agent's Rust edits as cheap to review as the TypeScript ones."] = \
    'pre-commit 钩子在键盘敲击那一刻就执行缰绳。Tauri 特有的那几条追加——`cargo clippy -D warnings`、推送时的 `cargo audit`、以及一条 `gitleaks` 钩子——让智能体的 Rust 修改变得和它的 TypeScript 修改一样便宜可审。'

code_48 = '''# verified: 2026-04-17 · Tauri-Todo worked arc · Fence
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks: [{id: trailing-whitespace}, {id: end-of-file-fixer}, {id: check-yaml}]
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.4
    hooks: [{id: gitleaks}]
  - repo: local
    hooks:
      - id: cargo-clippy
        name: cargo clippy -D warnings
        entry: bash -c "cd src-tauri && cargo clippy -- -D warnings"
        language: system
        pass_filenames: false
      - id: cargo-audit
        name: cargo audit
        entry: bash -c "cd src-tauri && cargo audit"
        language: system
        pass_filenames: false
        stages: [pre-push]
      - id: pnpm-test
        name: pnpm test
        entry: pnpm test --run
        language: system
        pass_filenames: false
'''
T[code_48] = code_48

T['Fragment 3 — `AGENTS.md` (Paddock + Groom)'] = '片段 3 —— `AGENTS.md`（牧场 + 梳理）'

T['Finally, `AGENTS.md` declares the role cast, the mergeable-PR contract (Hard gates must pass, Soft gates may carry a dated waiver), and the weekly Groom schedule. Each item references a file earlier in this chapter — which closes the loop between the generic operating primitives and the worked arc.'] = \
    '最后，`AGENTS.md` 声明角色班底、可合并 PR 契约（硬关卡必须过，软关卡可带带日期的豁免）、以及每周的梳理排班。每一项都引用到本章前面出现过的某份文件——这把通用的运行原语与这段动手故事弧之间的循环闭上了。'

code_51 = '''<!-- verified: 2026-04-17 · Tauri-Todo worked arc · Role contracts (Paddock + Groom) -->

# AGENTS.md — role contracts for lazy-todo-app

## Roles

- **PO** — owns `specs/*.md`; signs off feature intent before dev starts.
- **Architect** — owns `src-tauri/src/storage.rs` + ADRs under `docs/adr/`.
- **Developer** — implements against tests; never modifies signed ADRs.
- **Reviewer** — runs `hard-vs-soft-gates.md`; cannot self-approve.
- **MDD Owner** — maintains the HarnessCard at repo root; runs the weekly audit.

## Gate contract (Paddock)

A PR is mergeable when:

1. All Hard gates (see `../hard-vs-soft-gates.md`) pass.
2. Soft gates pass OR carry a dated waiver.
3. Reviewer has ticked every row of `acceptance-gate.md`.

## Groom contract

- Monday: MDD Owner runs `../entropy-audit.yml` and opens issues for any
  delta vs last week's report.
- Friday: Architect reviews drift between `specs/` and implemented code;
  if drift > 3 items, triggers a mid-sprint re-spec.
'''
T[code_51] = code_51

T['The copilot-productivity literature {cite}`peng2023copilotstudy,ziegler2022productivity` shows that agents accelerate whichever guardrail the environment already provides; the Tauri-Todo fragments above supply all three at once. A developer who commits them into a fresh `lazy-todo-app` clone has a working harness before the first feature lands.'] = \
    'Copilot 生产力相关文献 {cite}`peng2023copilotstudy,ziegler2022productivity` 表明：智能体会对环境里 *已经有* 的那种护栏做加速；上面这几份 Tauri-Todo 片段一次性把三层护栏都配齐。把它们 commit 进一份全新 `lazy-todo-app` 克隆的开发者，在第一个功能落地之前，就已经拥有一具能工作的挽具。'

T['Research Foundations'] = '研究脉络'

T['Operating a harness rests on five cited lineages:'] = \
    '运行一具挽具，靠五条可引用的谱系支着：'

T["**Entropy and technical debt** — Cunningham's 1992 debt metaphor {cite}`cunningham1992debt` and Tom et al.'s 2013 systematic review {cite}`tom2013debtinterest` motivate the Monday-morning audit."] = \
    '**熵与技术债**——Cunningham 1992 年的债务比喻 {cite}`cunningham1992debt`、以及 Tom 等人 2013 年的系统综述 {cite}`tom2013debtinterest`，为"周一早上的审计"提供了动机。'

T["**Observability** — Majors, Fong-Jones & Miranda's *Observability Engineering* {cite}`majors2022observability` frames harness-internal signals as first-class; the LangChain Terminal-Bench 2.0 data point {cite}`langchain2026tbench` provides the industry baseline for *turns-to-green* as an observable."] = \
    '**可观测性**——Majors／Fong-Jones／Miranda 的 *Observability Engineering* {cite}`majors2022observability` 把挽具内部信号框成了一等公民；LangChain Terminal-Bench 2.0 的数据点 {cite}`langchain2026tbench` 给出了行业里把 *turns-to-green* 当作可观测量的基线。'

T["**Approval gates and release discipline** — Humble & Farley's *Continuous Delivery* {cite}`humble2010continuousdelivery` supplies the hard-gate grammar; the `lazy-scrum-team` skill {cite}`lazyscrumteam2026` extends it to the role-aware rework matrix used above."] = \
    '**审批关卡与发布纪律**——Humble & Farley 的 *Continuous Delivery* {cite}`humble2010continuousdelivery` 提供了硬关卡的语法；`lazy-scrum-team` 技能 {cite}`lazyscrumteam2026` 把它扩展成了上面用到的那张"角色感知"的返工矩阵。'

T['**Meta-evolution** — Ford, Parsons & Kua {cite}`ford2017buildingevolutionary` and Lehman {cite}`lehman1980laws` establish that a system that does not continuously adapt loses fitness; the harness obeys the same law.'] = \
    '**元演进**——Ford／Parsons／Kua {cite}`ford2017buildingevolutionary` 与 Lehman {cite}`lehman1980laws` 立下的基础：一个不持续适应的系统会丢失适配度；挽具遵守同一条定律。'

T["**Tauri-Todo arc foundations** — Jung et al.'s *RustBelt* {cite}`jung2018rustbelt` grounds the ownership-as-harness argument; the Tauri 2 security white paper {cite}`tauri2024security` grounds the IPC-boundary discussion; Peng et al. and Ziegler et al. {cite}`peng2023copilotstudy,ziegler2022productivity` show why the bridle is load-bearing when an agent is in the loop."] = \
    '**Tauri-Todo 故事弧的地基**——Jung 等人的 *RustBelt* {cite}`jung2018rustbelt` 给"所有权即挽具"的论点奠了地基；Tauri 2 的安全白皮书 {cite}`tauri2024security` 给 IPC 边界的讨论奠了地基；Peng 等人与 Ziegler 等人 {cite}`peng2023copilotstudy,ziegler2022productivity` 说明了为什么当智能体处在回路里时，缰绳是承重的。'

T['Hands-On'] = '动手环节'

T['Operating primitives and the Tauri-Todo worked arc live under `book/source/_handson/06-operating-a-harness/`:'] = \
    '运行原语与 Tauri-Todo 故事弧都住在 `book/source/_handson/06-operating-a-harness/` 下：'

T['**Operating primitives:** `doc-sync-check.sh`, `entropy-audit.yml`, `prometheus-scrape.yml`, `artefact-state-model.yaml`, `rework-matrix.md`, `hard-vs-soft-gates.md`.'] = \
    '**运行原语：** `doc-sync-check.sh`、`entropy-audit.yml`、`prometheus-scrape.yml`、`artefact-state-model.yaml`、`rework-matrix.md`、`hard-vs-soft-gates.md`。'

T['**Tauri-Todo worked arc:** `tauri-todo/CLAUDE.md`, `tauri-todo/pre-commit-config.yaml`, `tauri-todo/AGENTS.md`, and a `tauri-todo/README.md` cross-linking to the runnable companion repository `walterfan/lazy-todo-app`.'] = \
    '**Tauri-Todo 故事弧：** `tauri-todo/CLAUDE.md`、`tauri-todo/pre-commit-config.yaml`、`tauri-todo/AGENTS.md`，以及一份 `tauri-todo/README.md`，交叉链接到可运行的配套仓库 `walterfan/lazy-todo-app`。'

T["Together these artefacts supply every cell in the MDD column of the Chapter 05 matrix and most of the SDD × Groom cell. The remaining SDD and TDD cells live in their own chapters' Hands-On tracks and in the case studies that follow in Part IV."] = \
    '这些制品合起来，填满了第 05 章矩阵里整列 MDD、以及 SDD × 梳理 那格里的大部分。剩下的 SDD 与 TDD 格子，住在各自章节的动手环节、以及第四部分随后那几章案例研究里。'


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
