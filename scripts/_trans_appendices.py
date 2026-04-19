"""One-shot translator for Appendices C, D, E, and index."""
import polib

BASE = 'source/locale/zh_CN/LC_MESSAGES/chapters/13-appendices/'

# ------------------------------------------------------------
# Appendix C — Reading List & External Resources
# ------------------------------------------------------------
T_C = {}
T_C['Appendix C — Reading List & External Resources'] = \
    '附录 C —— 阅读单与外部资源'
T_C['Every entry below cites a BibTeX key; the canonical record — author, title, DOI, URL — stays in `_bib/*.bib`, not inline. Readers who want the full references should consult `references.md` (bibliography).'] = \
    '下面每一条都以一个 BibTeX key 引用；权威记录——作者、标题、DOI、URL——都住在 `_bib/*.bib` 里，不嵌在正文中。想看完整引用的读者请去 `references.md`（参考文献）。'

T_C['Foundations'] = '理论根基'
T_C['Theoretical and historical papers the framework rests on:'] = \
    '本框架所依赖的那些理论与历史论文：'
T_C["Lehman's 1980 laws of software evolution {cite}`lehman1980laws`."] = \
    'Lehman 1980 年的软件演化定律 {cite}`lehman1980laws`。'
T_C["Cunningham's 1992 debt metaphor {cite}`cunningham1992debt`."] = \
    'Cunningham 1992 年的技术债隐喻 {cite}`cunningham1992debt`。'
T_C["Conway's 1968 law {cite}`conway1968law`."] = \
    'Conway 1968 年的定律 {cite}`conway1968law`。'
T_C["Meyer's 1992 design-by-contract paper {cite}`meyer1992contracts`."] = \
    'Meyer 1992 年的契约式设计论文 {cite}`meyer1992contracts`。'
T_C["Ford, Parsons & Kua's 2017 *Building Evolutionary Architectures* {cite}`ford2017buildingevolutionary`."] = \
    'Ford、Parsons 与 Kua 2017 年的 *Building Evolutionary Architectures* {cite}`ford2017buildingevolutionary`。'
T_C['Feathers 2004 *Working Effectively with Legacy Code* {cite}`feathers2004legacy`.'] = \
    'Feathers 2004 年的 *Working Effectively with Legacy Code* {cite}`feathers2004legacy`。'

T_C['The Three Guardians (SDD / TDD / MDD)'] = '三大护法（SDD ／ TDD ／ MDD）'
T_C['Martraire 2019 *Living Documentation* — SDD lineage {cite}`martraire2019living`.'] = \
    'Martraire 2019 年 *Living Documentation* —— SDD 谱系 {cite}`martraire2019living`。'
T_C['Adzic 2011 *Specification by Example* — SDD × Paddock lineage {cite}`adzic2011specbyexample`.'] = \
    'Adzic 2011 年 *Specification by Example* —— SDD × 牧场 谱系 {cite}`adzic2011specbyexample`。'
T_C['Beck 2002 *TDD by Example* — TDD lineage {cite}`beck2002tdd`.'] = \
    'Beck 2002 年 *TDD by Example* —— TDD 谱系 {cite}`beck2002tdd`。'
T_C['Zeller 2009 *Why Programs Fail* — TDD debugging lineage {cite}`zeller2009whyprogramsfail`.'] = \
    'Zeller 2009 年 *Why Programs Fail* —— TDD 调试谱系 {cite}`zeller2009whyprogramsfail`。'
T_C['Bacchelli & Bird 2013 modern-code-review study {cite}`bacchelli2013codereview`.'] = \
    'Bacchelli 与 Bird 2013 年的现代代码评审研究 {cite}`bacchelli2013codereview`。'
T_C['Majors, Fong-Jones & Miranda 2022 *Observability Engineering* — MDD lineage {cite}`majors2022observability`.'] = \
    'Majors、Fong-Jones 与 Miranda 2022 年 *Observability Engineering* —— MDD 谱系 {cite}`majors2022observability`。'
T_C['Sculley et al. 2015 ML technical-debt paper — MDD cautionary tale {cite}`sculley2015mltechdebt`.'] = \
    'Sculley 等 2015 年的 ML 技术债论文 —— MDD 的警世寓言 {cite}`sculley2015mltechdebt`。'

T_C['Benchmarks'] = '基准测试'
T_C['Public benchmarks referenced in the case-study chapters:'] = \
    '案例研究章节中引用到的公开基准测试：'
T_C['LangChain 2026 Terminal Bench 2.0 blog post {cite}`langchain2026tbench`.'] = \
    'LangChain 2026 年 Terminal Bench 2.0 的博客文章 {cite}`langchain2026tbench`。'
T_C['Peng et al. 2023 Copilot productivity study {cite}`peng2023copilotstudy`.'] = \
    'Peng 等 2023 年的 Copilot 生产力研究 {cite}`peng2023copilotstudy`。'
T_C['Ziegler et al. 2022 productivity study {cite}`ziegler2022productivity`.'] = \
    'Ziegler 等 2022 年的生产力研究 {cite}`ziegler2022productivity`。'

T_C['Open-Source Reference Implementations'] = '开源参考实现'
T_C['The harness projects the book scores as case studies:'] = \
    '本书作为案例研究打过分的那些挽具项目：'
T_C['HKUDS OpenHarness {cite}`hkuds2025openharness` — Ch.07.'] = \
    '港大 DS Lab 的 OpenHarness {cite}`hkuds2025openharness` —— 第 07 章。'
T_C['Joseph Vincent Superpowers {cite}`vincent2025superpowers,vincent2025superpowersrepo` — Ch.08.'] = \
    'Joseph Vincent 的 Superpowers {cite}`vincent2025superpowers,vincent2025superpowersrepo` —— 第 08 章。'
T_C['lazy-scrum-team Claude Code / Cursor skill {cite}`lazyscrumteam2026` — Ch.09.'] = \
    'lazy-scrum-team Claude Code／Cursor 技能 {cite}`lazyscrumteam2026` —— 第 09 章。'
T_C['OpenAI harness / RFT toolkit {cite}`openai2026harness` — adjacent.'] = \
    'OpenAI harness ／ RFT 工具包 {cite}`openai2026harness` —— 相邻项目。'

T_C['Ongoing Resources'] = '持续更新的资源'
T_C['Curated lists, vendor docs, and public discussions that update faster than this book:'] = \
    '那些比本书更新更快的精选列表、厂商文档与公开讨论：'
T_C["`walkinglabs/awesome-harness-engineering` — the canonical ongoing curated list {cite}`walkinglabs2026awesome`. **Scope difference from this book.** This book is a long-form methodology with strong opinions, dual-track research-plus-practice, and an enforceable dual-track lint rule; the *awesome* list is an ongoing unopinionated curation of papers, posts, and projects. The two are complements, not substitutes."] = \
    '`walkinglabs/awesome-harness-engineering` —— 权威的、持续更新的精选列表 {cite}`walkinglabs2026awesome`。**与本书的范围差别**：本书是一份长篇方法论，带强立场、"研究 ＋ 实践"双轨、以及一条可强制执行的双轨 lint 规则；而 *awesome* 列表则是一份不持立场、持续更新的论文、博文与项目精选。二者是互补关系，不是替代关系。'
T_C['Anthropic Claude Code documentation and launch posts {cite}`anthropic2024claudecode,anthropic2024skills`.'] = \
    'Anthropic 的 Claude Code 文档与发布文章 {cite}`anthropic2024claudecode,anthropic2024skills`。'
T_C['MCP specification and reference servers {cite}`anthropic2024mcp`.'] = \
    'MCP 规范及其参考实现 server {cite}`anthropic2024mcp`。'
T_C["Zhang Handong's《马书》 — Chinese-language Claude Code reverse-engineering study {cite}`zhangbook2026`."] = \
    '张汉东的《马书》—— 对 Claude Code 的中文逆向工程研究 {cite}`zhangbook2026`。'

T_C['Adjacent Fields'] = '相邻领域'
T_C['Fields that overlap with harness engineering without being identical:'] = \
    '那些与挽具工程有重叠、却并不等同的领域：'
T_C['*DevOps* — Humble & Farley 2010 *Continuous Delivery* {cite}`humble2010continuousdelivery` and Forsgren et al. 2018 *Accelerate* {cite}`forsgren2018accelerate`.'] = \
    '*DevOps* —— Humble 与 Farley 2010 年的 *Continuous Delivery* {cite}`humble2010continuousdelivery`，以及 Forsgren 等 2018 年的 *Accelerate* {cite}`forsgren2018accelerate`。'
T_C['*Scrum and agile process* — Schwaber & Sutherland 2020 Scrum Guide {cite}`schwaber2020scrum`.'] = \
    '*Scrum 与敏捷流程* —— Schwaber 与 Sutherland 2020 年的 Scrum Guide {cite}`schwaber2020scrum`。'
T_C['*Technical debt management* — Tom et al. 2013 systematic review {cite}`tom2013debtinterest`.'] = \
    '*技术债管理* —— Tom 等 2013 年的系统综述 {cite}`tom2013debtinterest`。'
T_C['*MLOps and AI engineering* — Huyen 2025 *AI Engineering* {cite}`huyen2025aieng`.'] = \
    '*MLOps 与 AI 工程* —— Huyen 2025 年的 *AI Engineering* {cite}`huyen2025aieng`。'
T_C['*Platform engineering* — CNCF platform-engineering maturity model {cite}`cncf2024platformeng`.'] = \
    '*平台工程* —— CNCF 的平台工程成熟度模型 {cite}`cncf2024platformeng`。'
T_C['*Reliability engineering* — Ford et al. 2017 evolutionary architecture crosses both this and the Foundations group {cite}`ford2017buildingevolutionary`.'] = \
    '*可靠性工程* —— Ford 等 2017 年的演化式架构，横跨本组与"理论根基"组 {cite}`ford2017buildingevolutionary`。'

# ------------------------------------------------------------
# Appendix D — HarnessCard Template
# ------------------------------------------------------------
T_D = {}
T_D['Appendix D — HarnessCard Template'] = '附录 D —— HarnessCard 模板'
T_D['The HarnessCard format is a standardised disclosure proposed by the CAR decomposition paper {cite}`car2025decomposition`. This appendix carries three pieces: a **blank template** (copy into your repo), two **filled instances** from Chapter 11 shown side-by-side for delta reading, and a **rubric** defining what each 0–5 score means.'] = \
    'HarnessCard 格式是一份由 CAR 分解论文 {cite}`car2025decomposition` 所提出的标准化披露。本附录承载三块内容：一份 **空白模板**（拷进你自己的仓库）、两份取自第 11 章的 **已填样本**（并排展示以便读 delta）、以及一份 **评分尺**（定义 0–5 每一档的含义）。'

T_D['Blank template'] = '空白模板'
T_D['Copy the block below into a `HarnessCard.md` at your repo root. Replace every `…` with evidence specific to your harness.'] = \
    '把下面这一整段拷进你仓库根目录的 `HarnessCard.md`。把每一个 `…` 替换成你自己挽具的具体证据。'

code_D_blank_en = '''# HarnessCard — <project name>

**Schema version.** CAR-HarnessCard v0.2.
**Subject.** <repo URL> at commit <SHA>.
**Observation window.** <YYYY-MM-DD> – <YYYY-MM-DD>.
**License.** <SPDX identifier>.

## Layer notes (CAR)

| Layer    | Notes                                                    |
|----------|----------------------------------------------------------|
| Control  | …                                                        |
| Agency   | …                                                        |
| Runtime  | …                                                        |

## Zone notes (Bridle / Fence / Paddock / Groom)

| Zone    | Notes                                                     |
|---------|-----------------------------------------------------------|
| Bridle  | …                                                         |
| Fence   | …                                                         |
| Paddock | …                                                         |
| Groom   | …                                                         |

## 3 × 4 scorecard

| Cell            | Score (0–5) | Evidence (file / URL)           |
|-----------------|-------------|----------------------------------|
| SDD × Bridle    | …           | …                                |
| SDD × Fence     | …           | …                                |
| SDD × Paddock   | …           | …                                |
| SDD × Groom     | …           | …                                |
| TDD × Bridle    | …           | …                                |
| TDD × Fence     | …           | …                                |
| TDD × Paddock   | …           | …                                |
| TDD × Groom     | …           | …                                |
| MDD × Bridle    | …           | …                                |
| MDD × Fence     | …           | …                                |
| MDD × Paddock   | …           | …                                |
| MDD × Groom     | …           | …                                |

**Means.** SDD = …, TDD = …, MDD = …, Overall = …

**Primary citation.** ``<BibTeX key>``.
'''
code_D_blank_zh = '''# HarnessCard —— <项目名>

**Schema 版本。** CAR-HarnessCard v0.2。
**对象。** <仓库 URL>，commit <SHA>。
**观察窗口。** <YYYY-MM-DD> – <YYYY-MM-DD>。
**许可证。** <SPDX 标识符>。

## 层级注释（CAR）

| 层级     | 注释                                                       |
|----------|------------------------------------------------------------|
| Control  | …                                                          |
| Agency   | …                                                          |
| Runtime  | …                                                          |

## 区域注释（缰绳 ／ 护栏 ／ 牧场 ／ 梳理）

| 区域    | 注释                                                        |
|---------|-------------------------------------------------------------|
| 缰绳    | …                                                           |
| 护栏    | …                                                           |
| 牧场    | …                                                           |
| 梳理    | …                                                           |

## 3 × 4 打分表

| 格子            | 得分（0–5） | 证据（文件 ／ URL）             |
|-----------------|-------------|----------------------------------|
| SDD × 缰绳      | …           | …                                |
| SDD × 护栏      | …           | …                                |
| SDD × 牧场      | …           | …                                |
| SDD × 梳理      | …           | …                                |
| TDD × 缰绳      | …           | …                                |
| TDD × 护栏      | …           | …                                |
| TDD × 牧场      | …           | …                                |
| TDD × 梳理      | …           | …                                |
| MDD × 缰绳      | …           | …                                |
| MDD × 护栏      | …           | …                                |
| MDD × 牧场      | …           | …                                |
| MDD × 梳理      | …           | …                                |

**均值。** SDD ＝ …，TDD ＝ …，MDD ＝ …，总分 ＝ …

**主要引用。** ``<BibTeX key>``。
'''
T_D[code_D_blank_en] = code_D_blank_zh

T_D['Two filled instances — Chapter 11 Act 1 vs Act 4'] = \
    '两份已填样本 —— 第 11 章 第一幕 vs 第四幕'
T_D["The two HarnessCards below are the Chapter 11 worked example's before-and-after pair, shown side-by-side with a delta column. The full cards live at `_handson/11-lazy-ai-coder/HarnessCard-Act1.md` and `_handson/11-lazy-ai-coder/HarnessCard-Act4.md`."] = \
    '下面这两份 HarnessCard，是第 11 章那份实例的"前后对"，并排展示，并附一列 delta。完整卡片住在 `_handson/11-lazy-ai-coder/HarnessCard-Act1.md` 与 `_handson/11-lazy-ai-coder/HarnessCard-Act4.md`。'

T_D['Cell'] = '格子'
T_D['Act 1'] = '第一幕'
T_D['Act 4'] = '第四幕'
T_D['Delta'] = 'Delta'
T_D['Fix (from §14)'] = '修复（来自 §14）'

T_D['SDD × Bridle'] = 'SDD × 缰绳'
T_D['3'] = '3'
T_D['0'] = '0'
T_D['unchanged'] = '未变'

T_D['SDD × Fence'] = 'SDD × 护栏'
T_D['1'] = '1'
T_D['4'] = '4'
T_D['+3'] = '+3'
T_D['`make prompts-lint` + schema validator (§14.1)'] = \
    '`make prompts-lint` ＋ schema validator（§14.1）'

T_D['SDD × Paddock'] = 'SDD × 牧场'
T_D['2'] = '2'

T_D['SDD × Groom'] = 'SDD × 梳理'
T_D['+2'] = '+2'
T_D['`sources-of-truth.md` index (§14.3)'] = \
    '`sources-of-truth.md` 索引（§14.3）'

T_D['TDD × Bridle'] = 'TDD × 缰绳'
T_D['TDD × Fence'] = 'TDD × 护栏'
T_D['MCP schema check + gitleaks (§14.2 + §14.4)'] = \
    'MCP schema 检查 ＋ gitleaks（§14.2 ＋ §14.4）'
T_D['TDD × Paddock'] = 'TDD × 牧场'
T_D['TDD × Groom'] = 'TDD × 梳理'

T_D['MDD × Bridle'] = 'MDD × 缰绳'
T_D['out of §14 scope'] = '不在 §14 范围内'
T_D['MDD × Fence'] = 'MDD × 护栏'
T_D['MDD × Paddock'] = 'MDD × 牧场'
T_D['MDD × Groom'] = 'MDD × 梳理'

T_D['**SDD mean.** 1.75 → 3.00 (+1.25). **TDD mean.** 2.00 → 2.75 (+0.75). **MDD mean.** 1.50 → 1.50 (+0.00). **Overall.** 1.75 → 2.42 (+0.67).'] = \
    '**SDD 均值。** 1.75 → 3.00（+1.25）。**TDD 均值。** 2.00 → 2.75（+0.75）。**MDD 均值。** 1.50 → 1.50（+0.00）。**总分。** 1.75 → 2.42（+0.67）。'

T_D['Rubric — what each score means'] = '评分尺 —— 每一档分数的含义'
T_D['Every cell score is a 0–5 integer. The rubric is pinned to CAR-HarnessCard v0.2 {cite}`car2025decomposition` and applies uniformly across all twelve cells.'] = \
    '每一格的得分都是 0–5 的整数。这把评分尺钉在 CAR-HarnessCard v0.2 {cite}`car2025decomposition` 上，十二格通用。'

T_D['Score'] = '得分'
T_D['Meaning'] = '含义'

T_D['**0**'] = '**0**'
T_D['No artefact of any kind for this cell. The guardian × zone intersection is absent.'] = \
    '这一格没有任何形式的制品。这个"护法 × 区域"交点是空缺的。'
T_D['**1**'] = '**1**'
T_D['An ad-hoc artefact exists but is not invoked on a cadence and carries no owner.'] = \
    '存在一件临时凑的制品，但并未按节奏被调用，也无人署名持有。'
T_D['**2**'] = '**2**'
T_D['A committed artefact exists; a named role owns it; review cadence is irregular.'] = \
    '存在一件已提交的制品；有一位署名角色持有它；评审节奏不规律。'
T_D['**3**'] = '**3**'
T_D['Artefact, owner, and cadence all present; the artefact is read by agents (SDD/TDD rows) or scraped (MDD row).'] = \
    '制品、所有者、节奏三者俱全；该制品被智能体读取（SDD／TDD 行）或被抓取（MDD 行）。'
T_D['**4**'] = '**4**'
T_D['Artefact is *enforced* — failure blocks commits, merges, or releases as appropriate.'] = \
    '该制品是 *被强制执行* 的 —— 不合格会按情况挡住 commit、合并或发布。'
T_D['**5**'] = '**5**'
T_D['Enforced **and** machine-verifiable **and** the artefact itself is revised on a declared cadence (quarterly or faster).'] = \
    '被强制执行，**而且** 可被机器验证，**而且** 制品本身按一份声明过的节奏（季度或更快）被修订。'

T_D['A score of 4 requires an enforcement mechanism; a score of 5 additionally requires a meta-review schedule. Teams that cannot point to an enforcement artefact should score a 3, not a 4.'] = \
    '拿到 4 分需要一个强制执行机制；拿到 5 分则在此之上还需要一份元评审时间表。指不出"强制执行制品"的团队，应该打 3 分，不是 4 分。'

# ------------------------------------------------------------
# Appendix E — Sample CLAUDE.md Template
# ------------------------------------------------------------
T_E = {}
T_E['Appendix E — Sample `CLAUDE.md` Template'] = '附录 E —— `CLAUDE.md` 样板模板'

T_E['This appendix consolidates the hands-on fragments from Chapters 03, 04, 05, and 06 (including the Tauri-Todo arc) into a single `CLAUDE.md` a reader can drop directly into a fresh repository. Every block carries a `<!-- origin: ..., zone: ..., guardian: ... -->` header comment so the resulting file remains auditable against the twelve-cell matrix.'] = \
    '本附录把第 03、04、05、06 章（含 Tauri-Todo 那条弧线）中的 hands-on 片段，合并成一份 `CLAUDE.md`，供读者直接丢进一份全新仓库使用。每一块都带一条 `<!-- origin: ..., zone: ..., guardian: ... -->` 头注，这样生成出来的文件，仍然可以对照十二格矩阵审计。'

T_E['**Licensing.** The template below is published under MIT; copy, modify, and redistribute without further acknowledgement. Citations are tracked in `_bib/*.bib` and do not travel with the template itself; the CAR HarnessCard schema {cite}`car2025decomposition` is the upstream disclosure format it is designed to feed.'] = \
    '**许可证。** 下面这份模板以 MIT 协议发布；拷贝、修改、再分发皆不需要额外致谢。引用记录住在 `_bib/*.bib` 里，不会随模板一起旅行；CAR HarnessCard schema {cite}`car2025decomposition` 是它被设计去对接的上游披露格式。'

T_E['The consolidated template'] = '合并后的那份模板'

code_E_en = '''# CLAUDE.md

<!-- origin: chapters/03-what-is-harness-engineering.md, zone: Bridle, guardian: SDD -->
## Role and scope
You are a coding agent for <project-name>. You may edit <allowed paths>.
You must not touch <forbidden paths>. Every new public function gets a
docstring and a test; no exceptions.

<!-- origin: chapters/04-three-guardians.md, zone: Bridle, guardian: SDD -->
## Spec discipline
Before editing any source file, read the matching spec under `specs/`
(or, if absent, `docs/adr/`). If the spec is older than the code by
more than 30 days, surface this as a risk and pause.

<!-- origin: chapters/04-three-guardians.md, zone: Bridle, guardian: TDD -->
## Test discipline
Before writing implementation code, locate or author the failing test
that captures the requirement. A commit that does not green one test
does not advance the project.

<!-- origin: chapters/04-three-guardians.md, zone: Bridle, guardian: MDD -->
## Metric discipline
Before merging any change that touches a user-facing path, confirm the
metrics north-star (`mean agent turns to green` on the fixed benchmark)
has not regressed.

<!-- origin: chapters/05-harness-anatomy.md · SDD × Paddock -->
## Acceptance Gate (Verification Table)

| # | Requirement                          | Checked by        |
|---|--------------------------------------|-------------------|
| 1 | Acceptance tests green               | Test Engineer     |
| 2 | `AGENTS.md` rules unchanged or versioned | Architect     |
| 3 | `CHANGELOG.md` entry under Unreleased | PO               |

<!-- origin: chapters/05-harness-anatomy.md · TDD × Fence -->
## Pre-edit hooks (Claude Code)

Install `.claude/hooks.json` as follows:

```json
{
  "hooks": {
    "PreToolUse": [
      {"matcher": "Write|Edit|MultiEdit",
       "command": "pytest -q -m 'not slow'",
       "stopOnFailure": true}
    ]
  }
}
'''
code_E_zh = '''# CLAUDE.md

<!-- origin: chapters/03-what-is-harness-engineering.md, zone: Bridle, guardian: SDD -->
## 角色与范围
你是 <project-name> 的一名编码智能体。你可以编辑 <allowed paths>。
你绝不可触动 <forbidden paths>。每一个新增的 public 函数都要配一条
docstring 与一条测试；没有例外。

<!-- origin: chapters/04-three-guardians.md, zone: Bridle, guardian: SDD -->
## 规约纪律
在编辑任何一份源文件之前，先读 `specs/` 下与之匹配的规约（若不存在，
则看 `docs/adr/`）。若规约比代码老 30 天以上，把这件事作为风险浮上来，
然后暂停。

<!-- origin: chapters/04-three-guardians.md, zone: Bridle, guardian: TDD -->
## 测试纪律
在写实现代码之前，先找到或写出那条把需求钉住的、当前仍红的测试。
若一次 commit 不让至少一条测试由红转绿，它就没让项目往前走。

<!-- origin: chapters/04-three-guardians.md, zone: Bridle, guardian: MDD -->
## 度量纪律
在合并任何一项触及用户侧路径的变更之前，确认那条北极星度量
（固定基准上 `mean agent turns to green`）没有回归。

<!-- origin: chapters/05-harness-anatomy.md · SDD × Paddock -->
## 验收关卡（验证表）

| # | 需求                                  | 由谁核对             |
|---|---------------------------------------|----------------------|
| 1 | 验收测试全绿                          | Test Engineer        |
| 2 | `AGENTS.md` 规则未变、或已版本化      | Architect            |
| 3 | `CHANGELOG.md` 在 Unreleased 下有条目 | PO                   |

<!-- origin: chapters/05-harness-anatomy.md · TDD × Fence -->
## 写前钩子（Claude Code）

按下面的方式安装 `.claude/hooks.json`：

```json
{
  "hooks": {
    "PreToolUse": [
      {"matcher": "Write|Edit|MultiEdit",
       "command": "pytest -q -m 'not slow'",
       "stopOnFailure": true}
    ]
  }
}
'''
T_E[code_E_en] = code_E_zh

T_E['Cost cap'] = '成本上限'
T_E['A per-session cap of $2.00 and a monthly cap of $800.00 apply; breaches refuse new tool calls until manual reset. The per-repo configuration file lives at `.harness/cost-cap.yaml`.'] = \
    '单次会话上限 $2.00，月度上限 $800.00；触顶后，在手动重置之前拒绝新的工具调用。每仓库的配置文件住在 `.harness/cost-cap.yaml`。'

T_E['Weekly groom schedule'] = '每周梳理时间表'
T_E['Monday: run the entropy audit workflow; file issues for any new CVE, stale `verified:` header, or broken link. Friday: verify spec surface has no drift > 3 items; otherwise trigger a mid-sprint re-spec.'] = \
    '周一：跑熵审计工作流；遇到任何新增 CVE、陈旧的 `verified:` 头注、或失效链接，立即开 issue。周五：核验规约表面是否漂移超过 3 项；若超过，触发一次 sprint 中段的重新规约。'

T_E['Tauri-Todo house rules (when the repo is a Tauri 2 app)'] = \
    'Tauri-Todo 家规（当这份仓库是一个 Tauri 2 应用时）'
T_E['Rust crate `src-tauri/` owns IPC, storage, and OS integration.'] = \
    'Rust crate `src-tauri/` 持有 IPC、存储、操作系统集成。'
T_E['TypeScript app in `src/` owns UI and input validation only.'] = \
    '`src/` 下的 TypeScript 应用只持有 UI 与输入校验。'
T_E['Never call OS APIs directly from TS; route through `invoke()`.'] = \
    '绝不要从 TS 直接调用操作系统 API；一律经由 `invoke()` 转接。'
T_E['Never add a dependency without `cargo audit` in the same commit.'] = \
    '绝不要在同一笔 commit 中引入依赖却不跑 `cargo audit`。'

T_E['Committed gates'] = '提交侧关卡'
T_E['A commit is only valid if, in order:'] = \
    '一次 commit 只有在以下项目按序全部成立时才有效：'
T_E['`pytest -q` passes.'] = '`pytest -q` 通过。'
T_E['`ruff check .` (or language-equivalent linter) passes.'] = \
    '`ruff check .`（或相应语言的等价 linter）通过。'
T_E['`gitleaks` finds no secrets.'] = '`gitleaks` 找不到任何密钥。'
T_E['`make prompts-lint` (or equivalent spec validator) passes.'] = \
    '`make prompts-lint`（或等价的规约校验器）通过。'
T_E['No `TODO` markers added without a matching issue link.'] = \
    '不允许新增 `TODO` 标记而没有与之对应的 issue 链接。'

T_E['HarnessCard self-disclosure'] = 'HarnessCard 自我披露'
T_E["When you finish a non-trivial change, update `HarnessCard.md` at the repo root and append a one-line entry to `HARNESSCARD-CHANGELOG.md` naming which cell's score moved and by how much."] = \
    '每完成一项非小的变更，就更新仓库根目录的 `HarnessCard.md`，并在 `HARNESSCARD-CHANGELOG.md` 追加一行——点名哪一格的分数动了、动了多少。'

T_E['''
## Copy-paste note

The block above is MIT-licensed and intentionally text-only — no images,
no external fetches, no secrets. It is designed to be dropped into a
reader's repo as `CLAUDE.md` with no further editing required other
than substituting `<project-name>` and `<allowed paths>`.
'''] = \
    '''
## 粘贴使用说明

上面这段以 MIT 协议发布，且刻意全为文本——没有图片、没有外部抓取、
没有密钥。它被设计成可以直接丢进读者的仓库、命名为 `CLAUDE.md`，
除了把 `<project-name>` 与 `<allowed paths>` 替换掉之外，不需要任何
额外修改。
'''

# ------------------------------------------------------------
# Appendix Index
# ------------------------------------------------------------
T_IDX = {}
T_IDX['Appendices'] = '附录'
T_IDX['The five lettered appendices collect material that benefits from being separate from the narrative but that readers return to frequently: a role-grouped FAQ, a glossary, a reading list, the HarnessCard template, and a consolidated ``CLAUDE.md`` sample.'] = \
    '这五份带字母的附录汇集了那些"从叙事中分出来更合适、却又会被读者频繁回访"的材料：一份按角色分组的 FAQ、一份术语表、一份阅读单、HarnessCard 模板，以及一份合并起来的 ``CLAUDE.md`` 样板。'


def apply(path, table, label):
    po = polib.pofile(path)
    hit = 0
    miss = []
    for e in po:
        if not e.msgstr and not e.obsolete:
            if e.msgid in table:
                e.msgstr = table[e.msgid]
                hit += 1
            else:
                miss.append(e.msgid)
    po.save(path)
    remaining = len([e for e in polib.pofile(path) if not e.msgstr and not e.obsolete])
    print(f'[{label}] translated {hit}; remaining {remaining}')
    for m in miss[:5]:
        print('  MISS:', repr(m[:200]))


def main():
    apply(BASE + 'c-reading-list.po', T_C, 'C')
    apply(BASE + 'd-harnesscard.po', T_D, 'D')
    apply(BASE + 'e-claude-md.po', T_E, 'E')
    apply(BASE + 'index.po', T_IDX, 'index')


if __name__ == '__main__':
    main()
