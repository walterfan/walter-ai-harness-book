"""One-shot translator for Ch.09 lazy-scrum-team."""
import polib

PATH = 'source/locale/zh_CN/LC_MESSAGES/chapters/09-lazy-scrum-team.po'
T = {}

T['Case Study: lazy-scrum-team — A Workflow-Encoded Harness'] = \
    '案例研究：lazy-scrum-team —— 用工作流编码出来的挽具'

T['*Most teams have roles. Few teams have contracts between those roles. Fewer still have artefacts that make those contracts machine-readable.*'] = \
    '*多数团队有角色。少数团队在角色之间有契约。更少数的团队，有能让这些契约被机器读懂的制品。*'

T['`lazy-scrum-team` {cite}`lazyscrumteam2026` is a Claude Code / Cursor-compatible skill package that encodes a full Scrum-inspired role cast as executable workflow. Unlike OpenHarness (a runtime) and Superpowers (a skill library), `lazy-scrum-team` treats *the workflow itself* as the harness — the roles, the hand-offs between them, and the rework artefacts that travel along those hand-offs. This chapter is the book\'s canonical treatment of the three patterns Chapter 06 only referenced: the Artefact State Model, the Rework Matrix, and the Hard vs Soft Gate classification.'] = \
    '`lazy-scrum-team` {cite}`lazyscrumteam2026` 是一份兼容 Claude Code／Cursor 的技能包，把一整套受 Scrum 启发的角色班底编码成了可执行的工作流。与 OpenHarness（一套运行时）和 Superpowers（一座技能库）不同，`lazy-scrum-team` 把 *工作流本身* 当作挽具——角色、角色之间的交接、以及沿着这些交接传递的返工制品。本章是本书对第 06 章只点到却未展开的三种模式——制品状态机、返工矩阵、硬关卡 vs 软关卡分类——的正式处理。'

T['§09.1 — Role cast'] = '§09.1 —— 角色班底'

T['The skill ships seven explicit roles; every role has a one-paragraph contract and a set of owned artefacts.'] = \
    '这套技能自带七个显式角色；每个角色配一段契约、以及一组它署名持有的制品。'

T['Role'] = '角色'
T['Owns'] = '持有'
T['Cannot'] = '不得'

T['Product Owner (PO)'] = 'Product Owner（PO）'
T['`specs/*.md`, backlog order'] = '`specs/*.md`，backlog 的排序'
T['write production code; approve PRs'] = '写生产代码；审批 PR'

T['Architect'] = 'Architect（架构师）'
T['ADRs, module boundaries, `storage.rs`-style gate files'] = \
    'ADR、模块边界、类似 `storage.rs` 那样的关卡文件'
T['override PO on feature intent'] = '在功能意图上凌驾于 PO'

T['Scrum Master'] = 'Scrum Master'
T['Sprint cadence, state-model integrity'] = 'sprint 节奏、状态机的完整性'
T['write or review code'] = '写或审查代码'

T['Developer'] = 'Developer（开发）'
T['Feature code + unit tests'] = '功能代码 ＋ 单元测试'
T['self-merge'] = '自行合并'

T['Code Reviewer'] = 'Code Reviewer（评审人）'
T['Hard-gate checklist, PR approval'] = '硬关卡清单、PR 批准'
T['self-approve; review own code'] = '自审自批；审自己的代码'

T['Test Engineer'] = 'Test Engineer（测试工程师）'
T['Acceptance tests, coverage floor'] = '验收测试、覆盖率下限'
T['approve PRs'] = '批准 PR'

T['Final Acceptance'] = 'Final Acceptance（终审）'
T['Release PR + HarnessCard delta'] = '发布 PR ＋ HarnessCard delta'
T['perform the review themselves'] = '自己亲自做评审'

T["Scrum {cite}`schwaber2020scrum` supplies the role vocabulary; the skill's innovation is less about roles and more about what happens *between* them. Conway's Law {cite}`conway1968law` reminds us that the communication structure leaks into the artefact structure; the skill uses this as a feature rather than a bug — the hand-off artefacts *are* the communication channel."] = \
    'Scrum {cite}`schwaber2020scrum` 提供了这份角色词汇表；这个技能的创新并不在于角色本身，而在于角色 *之间* 发生了什么。Conway 律 {cite}`conway1968law` 提醒我们：沟通结构会渗进制品结构；这个技能把这件事当作特性而不是缺陷——那些交接制品 *本身* 就是沟通通道。'

T['§09.2 — Pattern 1 — Artefact State Model'] = '§09.2 —— 模式一 —— 制品状态机'

T['Every reviewable artefact in the harness has exactly four states — `draft → review → approved → archived` — with tightly constrained transitions. The canonical encoding ships as a YAML file any ticketing system can import:'] = \
    '挽具中每一份可评审制品都恰好有四种状态——`draft → review → approved → archived`——且跃迁被严格约束。权威编码以 YAML 文件交付，任何 ticket 系统都能导入：'

code_32 = '''# verified: 2026-04-17 · Ch.09 lazy-scrum-team hands-on · adaptable state machine
artefact_state_model_version: "0.1"
states:
  draft:     {color: "#bbb"}
  review:    {color: "#f4c"}
  approved:  {color: "#4c8"}
  archived:  {color: "#888"}
transitions:
  - {from: draft,    to: review,   by: Author,           trigger: submit}
  - {from: review,   to: draft,    by: Reviewer,         trigger: request_changes}
  - {from: review,   to: approved, by: FinalAcceptance,  trigger: approve}
  - {from: approved, to: archived, by: ReleaseManager,   trigger: release_shipped}
  - {from: archived, to: review,   by: Author,           trigger: reopen}
invariants:
  - only_FinalAcceptance_can_approve
  - no_skip_review_from_draft_to_approved
  - archived_artefacts_are_read_only_until_reopened
'''
T[code_32] = code_32

T['Two invariants make the state model load-bearing rather than decorative: only Final Acceptance can flip `review → approved`, and approved artefacts cannot return to `draft` without passing through `archived` first. These two invariants together eliminate the most common failure mode of review processes — silent rework — because any regression on an approved artefact is visible as an explicit reopen event.'] = \
    '有两条不变量，让这个状态机成为承重的、而非装饰性的：只有 Final Acceptance 能翻转 `review → approved`；已被批准的制品，要回到 `draft`，必须先经过 `archived`。这两条不变量合在一起，消除了评审流程里最常见的那种失败模式——*沉默返工*——因为任何对"已批准制品"的回退，都会显式地表现为一次 reopen 事件。'

T['§09.3 — Pattern 2 — Rework Matrix'] = '§09.3 —— 模式二 —— 返工矩阵'

T['The Rework Matrix names, for every finder × fixer pair, the specific artefact that must accompany the hand-off. Pull-request-as-workflow research {cite}`gousios2014pullbased` and the classic specification-by-example corpus {cite}`adzic2011specbyexample` both argue for machine-readable hand-offs; the Rework Matrix is this book\'s opinionated encoding.'] = \
    '返工矩阵针对每一对"发现者 × 修复者"，命名了必须随附这次交接的那件具体制品。把 PR 作为工作流的研究 {cite}`gousios2014pullbased`，以及经典的 specification-by-example 文献 {cite}`adzic2011specbyexample`，都主张"机器可读的交接"；返工矩阵是本书对此的一份带倾向的编码。'

code_36_en = '''<!-- verified: 2026-04-17 · Ch.09 lazy-scrum-team hands-on · adaptable version -->

# Rework Matrix (adaptable)

Copy this file into your own repo under `docs/rework/README.md`. Adjust
the row/column set to your team's role cast; the *shape* — finder × fixer,
with a named rework artefact per cell — is what matters.

|               | PO       | Architect | Developer | Test Engineer | Final Acceptance |
|---------------|----------|-----------|-----------|---------------|------------------|
| **PO**        | —        | `spec-delta.md`   | —                | `acceptance.md`        | —                          |
| **Architect** | —        | —                 | `adr-rework.md`  | —                      | —                          |
| **Developer** | `spec-question.md` | —       | —                | —                      | —                          |
| **Test**      | `acceptance-gap.md` | —      | `bug-report.md`  | —                      | —                          |
| **Final Acc** | `reject-reason.md` | `reject-reason.md` | `reject-reason.md` | `reject-reason.md` | —                     |

Rule: no defect crosses a hand-off without a rework artefact attached.
"Just fix it" is an anti-pattern that burns institutional memory.
'''
code_36_zh = '''<!-- verified: 2026-04-17 · Ch.09 lazy-scrum-team hands-on · adaptable version -->

# 返工矩阵（可改写）

把这份文件拷进你自己仓库的 `docs/rework/README.md`。把行列集合改成
你团队实际的角色班底；真正重要的是 *形状*——发现者 × 修复者，
每一格配一件署名返工制品。

|               | PO       | Architect | Developer | Test Engineer | Final Acceptance |
|---------------|----------|-----------|-----------|---------------|------------------|
| **PO**        | —        | `spec-delta.md`   | —                | `acceptance.md`        | —                          |
| **Architect** | —        | —                 | `adr-rework.md`  | —                      | —                          |
| **Developer** | `spec-question.md` | —       | —                | —                      | —                          |
| **Test**      | `acceptance-gap.md` | —      | `bug-report.md`  | —                      | —                          |
| **Final Acc** | `reject-reason.md` | `reject-reason.md` | `reject-reason.md` | `reject-reason.md` | —                     |

规则：任何缺陷跨过一次交接，都必须随附一份返工制品。
"你就赶紧修一下吧"是一种反模式，会烧掉组织记忆。
'''
T[code_36_en] = code_36_zh

T['Concretely: when a Test Engineer rejects a Developer\'s PR, the rejection lands as a `bug-report.md` file in the PR body, not as a Slack message. When the PO rejects the Architect\'s ADR, it lands as a `spec-delta.md` under `docs/rework/<sprint>/`. The named file is the contract; "just fix it" comments are institutional amnesia.'] = \
    '具体地说：当 Test Engineer 驳回一位 Developer 的 PR，驳回意见以一份 `bug-report.md` 的形式落到 PR body 里，而不是变成一条 Slack 消息。当 PO 驳回 Architect 的 ADR，驳回意见以一份 `spec-delta.md` 的形式落到 `docs/rework/<sprint>/` 下。*署名的那份文件* 就是契约；"赶紧修一下"式的评论，等于组织级失忆。'

T['§09.4 — Pattern 3 — Hard vs Soft Gates'] = '§09.4 —— 模式三 —— 硬关卡 vs 软关卡'

T['Every gate in the harness declares its class at creation time: a **Hard gate** that can never be waived and a **Soft gate** that may be waived by a named role with an expiry date. The classification is reproduced verbatim into Chapter 06\'s hands-on directory; the canonical table is:'] = \
    '挽具中每一道关卡，都必须在创建时声明自己的类别：**硬关卡** 永不可豁免；**软关卡** 可由署名角色带到期日豁免。这份分类被原样复刻进第 06 章的 hands-on 目录；权威表格为：'

T['Gate'] = '关卡'
T['Class'] = '类别'
T['Waiver rule'] = '豁免规则'
T['unit-test suite'] = '单元测试套件'
T['Hard'] = '硬'
T['never waive; fix or revert'] = '永不豁免；要么修，要么 revert'
T['lint'] = 'lint'
T['never waive for new code'] = '对新代码永不豁免'
T['coverage floor'] = '覆盖率下限'
T['Soft'] = '软'
T['Architect + reason; max 7 days'] = 'Architect 附理由；最多 7 天'
T['cost cap'] = '成本上限'
T['MDD Owner; max 24 hours'] = 'MDD Owner；最多 24 小时'
T['secrets scan'] = '密钥扫描'
T['never waive; rotate the secret'] = '永不豁免；把密钥轮换掉'
T['docs link-check'] = '文档 link-check'
T['any Reviewer; max until next weekly groom'] = '任一评审人；最多持续到下一次每周 groom'

T["The Humble & Farley *Continuous Delivery* lineage {cite}`humble2010continuousdelivery` supplies the Hard-gate grammar; the DORA metrics literature {cite}`forsgren2018accelerate` shows why the ratio of Soft-gate waivers to Hard-gate passes is itself a health signal."] = \
    'Humble 与 Farley 的 *Continuous Delivery* 谱系 {cite}`humble2010continuousdelivery`，提供了硬关卡的语法；DORA 度量文献 {cite}`forsgren2018accelerate` 说明了为什么"软关卡豁免数／硬关卡通过数"这一比值，本身就是一条健康信号。'

T['§09.5 — 12-cell highlight map'] = '§09.5 —— 十二格亮点图'

T['Cell'] = '格子'
T['Score'] = '得分'
T['Evidence'] = '证据'

T['SDD × Bridle'] = 'SDD × 缰绳'
T['4'] = '4'
T['`roles/*.md` are explicit agent-readable role contracts.'] = \
    '`roles/*.md` 是显式的、智能体可读的角色契约。'

T['SDD × Fence'] = 'SDD × 护栏'
T['State-machine invariants refuse ill-formed transitions.'] = \
    '状态机的不变量，拒绝形态不合法的跃迁。'

T['SDD × Paddock'] = 'SDD × 牧场'
T['5'] = '5'
T['Verification Table + acceptance review is the canonical SDD paddock.'] = \
    '验证表 ＋ 验收评审，就是 SDD 牧场的经典形态。'

T['SDD × Groom'] = 'SDD × 梳理'
T['3'] = '3'
T['Sprint retrospective recurses into skill updates; cadence varies.'] = \
    'sprint 回顾会会反过来更新技能；节奏因团队而异。'

T['TDD × Bridle'] = 'TDD × 缰绳'
T['Test Engineer role shapes context but no starter tests committed.'] = \
    'Test Engineer 这个角色塑造上下文，但没有 starter 测试被先行提交。'

T['TDD × Fence'] = 'TDD × 护栏'
T['Hard-gate policy refuses red-tree merges.'] = \
    '硬关卡策略拒绝红色测试树下的合并。'

T['TDD × Paddock'] = 'TDD × 牧场'
T['Acceptance review ties test results to the spec.'] = \
    '验收评审把测试结果绑回到规约上。'

T['TDD × Groom'] = 'TDD × 梳理'
T['Flaky-test policy implicit; quarantine not named.'] = \
    'flaky 测试策略是隐含的；没有显式命名隔离区。'

T['MDD × Bridle'] = 'MDD × 缰绳'
T['2'] = '2'
T['No north-star metric defined at skill level.'] = \
    '在技能层面没有定义北极星度量。'

T['MDD × Fence'] = 'MDD × 护栏'
T['Cost caps not shipped; delegated to the host platform.'] = \
    '不自带成本上限；交给宿主平台处理。'

T['MDD × Paddock'] = 'MDD × 牧场'
T['SLI gate not in scope.'] = \
    'SLI 关卡不在范围内。'

T['MDD × Groom'] = 'MDD × 梳理'
T['Weekly audit defined but not automated by the skill.'] = \
    '每周审计已定义，但未由技能自动化。'

T['Strongest row: **SDD** (mean 4). Strongest column: **Paddock** (mean 3.25). Weakest row: **MDD** (mean 2). The pattern is consistent with a workflow-encoded harness that optimises for approval discipline rather than runtime observability.'] = \
    '最强的一行：**SDD**（均值 4）。最强的一列：**牧场**（均值 3.25）。最弱的一行：**MDD**（均值 2）。这个分布与一具"为审批纪律优化、而非为运行时可观测性优化"的工作流式挽具完全一致。'

T['Where the workflow-as-harness approach is brittle'] = '把工作流当挽具，哪里脆弱'

T['The lazy-scrum-team patterns are the book\'s canonical SDD × Paddock exemplar, but reading them uncritically risks two structural traps.'] = \
    'lazy-scrum-team 的那些模式，是本书 SDD × 牧场 的经典范例；但不加批判地读进去，会踩两个结构性的坑。'

T['**Roles drift faster than the files that encode them.** The seven role contracts in §09.1 assume a team organised into those seven functions. Most teams are not — a solo founder is PO, Architect, Developer, and Code Reviewer in the same afternoon; a five-person startup collapses Test Engineer and Developer. A workflow harness that presupposes a role cast the team does not have generates friction at every hand-off because the artefact the Rework Matrix demands has no natural author. **Fix**: copy the *pattern* (named rework artefacts, explicit hand-off contracts) but map it to roles your team actually has, even if that means four contracts instead of seven. Conway\'s law {cite}`conway1968law` cuts both ways — the workflow must match the communication structure that exists, not the one the template assumes.'] = \
    '**角色漂移的速度，比编码它们的那些文件更快。** §09.1 里那七份角色契约，默认团队是按这七项职能组织的。多数团队并不是——一位独立创始人在一个下午里同时是 PO、Architect、Developer、Code Reviewer；一支五人创业团队会把 Test Engineer 与 Developer 合成一个。若一具工作流挽具预设了团队并不具备的角色班底，则每一次交接都会生出摩擦，因为返工矩阵要求的那件制品压根没有天然作者。**解法**：拷 *模式*（署名的返工制品、显式的交接契约），但把它映射到你团队 *实际拥有* 的角色上，哪怕这意味着四份契约而不是七份。Conway 律 {cite}`conway1968law` 两头都砍——工作流必须匹配真实存在的沟通结构，而不是模板假设的那种结构。'

T['**State-machine theatre.** The four states (`draft → review → approved → archived`) are load-bearing only if transitions are mechanically enforced. A team that writes the YAML but leaves transitions to "whoever remembers to update the ticket" gains nothing: an approved artefact that silently regresses to draft in everyone\'s heads while staying approved in the tracker is worse than no state machine at all, because it combines the cost of the process with none of its leverage.'] = \
    '**状态机剧场。** 那四个状态（`draft → review → approved → archived`），只有在跃迁被机械化强制执行时才承重。若一支团队写了 YAML 却把跃迁留给"谁记得就去更新 ticket"，那什么也得不到：一份"在所有人心里已悄悄退回 draft、在 tracker 里还挂着 approved"的制品，比完全没有状态机更糟——它把这套流程的成本全占了，却一份杠杆也没拿到。'

T['Pitfall — Workflow without tooling'] = '陷阱——工作流却没有工具'

T['A team adopts the seven role contracts, the Rework Matrix, and the state machine, all in prose. Adoption looks good for six weeks. Then a Friday evening incident produces a hotfix PR that the Developer self-merges — no Code Reviewer, no Final Acceptance, no state transition recorded. Nobody raised the alarm because the rules existed only as expectations. **Why**: a prose workflow is a norm; a norm under pressure yields to the first incident. **Fix**: wire at least two load-bearing transitions into tooling — branch protection that refuses self-merge is the minimum, a CODEOWNERS file that requires the correct role to approve is better. Every rule that is not mechanically enforced is a rule that will be suspended on the first bad Friday.'] = \
    '一支团队用散文把七份角色契约、返工矩阵、状态机全采纳了。采纳情况前六周看上去很好。然后周五晚上来一场事故——一个 hotfix PR 被 Developer 自行合并——没有 Code Reviewer、没有 Final Acceptance、状态跃迁也没记录。没人报警，因为那些规则只作为"期望"存在。**为什么**：散文工作流是一种规范；规范在压力下，会在第一次事故时就屈服。**解法**：至少把两条承重跃迁接进工具——分支保护拒绝自合并是底线；CODEOWNERS 文件要求正确角色来批准，更好。任何没有被机械化强制执行的规则，都会在第一次糟糕的星期五被暂停。'

T['HarnessCard'] = 'HarnessCard'
T['Field'] = '字段'
T['Value'] = '值'
T['HarnessCard schema version'] = 'HarnessCard schema 版本'
T['CAR-HarnessCard v0.2 {cite}`car2025decomposition`'] = 'CAR-HarnessCard v0.2 {cite}`car2025decomposition`'
T['Subject'] = '对象'
T['lazy-scrum-team skill, 2026-04 snapshot {cite}`lazyscrumteam2026`'] = \
    'lazy-scrum-team 技能，2026-04 快照 {cite}`lazyscrumteam2026`'
T['License'] = '许可证'
T['MIT'] = 'MIT'
T['Control layer (CAR)'] = 'Control 层（CAR）'
T['Strongly opinionated via role contracts and state machine.'] = \
    '通过角色契约和状态机，持有强烈主张。'
T['Agency layer (CAR)'] = 'Agency 层（CAR）'
T['Delegated to host platform (Claude Code / Cursor).'] = \
    '交由宿主平台处理（Claude Code／Cursor）。'
T['Runtime layer (CAR)'] = 'Runtime 层（CAR）'
T['None; the skill is prose + YAML only.'] = \
    '无；这个技能只是散文 ＋ YAML。'
T['SDD (mean)'] = 'SDD（均值）'
T['4.0'] = '4.0'
T['TDD (mean)'] = 'TDD（均值）'
T['3.5'] = '3.5'
T['MDD (mean)'] = 'MDD（均值）'
T['2.0'] = '2.0'
T['Primary citation'] = '主要引用'
T['{cite}`lazyscrumteam2026`'] = '{cite}`lazyscrumteam2026`'

T['Research Foundations'] = '研究脉络'

T['**Scrum** {cite}`schwaber2020scrum` — the role-vocabulary lineage the skill extends with explicit hand-off contracts.'] = \
    '**Scrum** {cite}`schwaber2020scrum` —— 这份角色词汇的谱系；这个技能用"显式交接契约"把它扩展。'
T['**Specification by Example** {cite}`adzic2011specbyexample` — the executable-spec lineage behind the Verification Table pattern.'] = \
    '**Specification by Example** {cite}`adzic2011specbyexample` —— 验证表模式背后的"可执行规约"谱系。'
T["**Conway's Law** {cite}`conway1968law` — the reason role structure *must* be encoded in artefact structure."] = \
    '**Conway 律** {cite}`conway1968law` —— 为什么角色结构 *必须* 被编码到制品结构里。'
T['**Pull-request-as-workflow** {cite}`gousios2014pullbased` — empirical basis for the PR body as a first-class spec surface.'] = \
    '**把 PR 当工作流** {cite}`gousios2014pullbased` —— "把 PR body 当作一等规约面"的经验基础。'
T['**DORA / Accelerate** {cite}`forsgren2018accelerate` — the metric lineage for measuring whether the gate discipline is working.'] = \
    '**DORA ／ Accelerate** {cite}`forsgren2018accelerate` —— 用来度量"这套关卡纪律到底有没有在起作用"的度量谱系。'

T['Hands-On'] = '动手环节'

T['Five copyable artefacts live under `book/source/_handson/09-lazy-scrum-team/`:'] = \
    '在 `book/source/_handson/09-lazy-scrum-team/` 下，住着五份可直接拷走的制品：'

T['`roles/po.md`, `roles/code-review.md`, `roles/acceptance-review.md` — excerpted and attributed role contracts.'] = \
    '`roles/po.md`、`roles/code-review.md`、`roles/acceptance-review.md` —— 带出处署名的角色契约节选。'
T['`state-transitions.yaml` — adaptable state machine.'] = \
    '`state-transitions.yaml` —— 可改写的状态机。'
T['`rework-matrix.md` — finder × fixer matrix with named rework artefacts.'] = \
    '`rework-matrix.md` —— 带署名返工制品的"发现者 × 修复者"矩阵。'

T['A reader who wants to adopt the three patterns *without* adopting the whole skill can copy these five files, customise the role cast, and have a working workflow harness before lunch.'] = \
    '想采用这三种模式却 *不想* 采用整个技能的读者，可以把这五份文件拷走、定制角色班底，并在午饭之前就拥有一具能工作的工作流挽具。'


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
