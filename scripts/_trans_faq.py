"""One-shot translator for Appendix A FAQ."""
import polib

PATH = 'source/locale/zh_CN/LC_MESSAGES/chapters/13-appendices/a-faq.po'
T = {}

T['Appendix A — Frequently Asked Questions'] = '附录 A —— 常见问题'

T['Questions are grouped by reader role. Answers are ≤ 150 words; roughly one-third carry a `{ref}` link back into the book body so a curious reader can drop into the canonical section.'] = \
    '问题按读者角色分组。每条回答不超过 150 词；大约三分之一会带上一条 `{ref}` 回指书本正文，方便好奇的读者跳进权威小节。'

T['For Individual Engineers'] = '面向一线工程师'

T['Do I need to adopt all three guardians at once?'] = \
    '我需要一次把三大护法全采纳吗？'

T["No — Chapter 12's 30/60/90 checklist is explicit that a team ships *one cell in thirty days, one row or column in sixty*. SDD × Bridle is the usual starting point because `AGENTS.md` is cheap to author and pays off every single turn thereafter. See {ref}`sdd-x-bridle` for the canonical artefact. If you are working alone, TDD × Fence is a defensible alternative: a single `PreToolUse` hook that refuses edits while the test tree is red gives you immediate daily leverage."] = \
    '不需要 —— 第 12 章的 30/60/90 清单说得很清楚，一支团队是 *三十天里交付一格，六十天里交付一行或一列*。SDD × 缰绳 是常见的起点，因为 `AGENTS.md` 写起来便宜、在此后的每一回合都能回本。权威制品见 {ref}`sdd-x-bridle`。若你独自作战，TDD × 护栏 也是一个合理替代：一条 `PreToolUse` 钩子——在测试树变红时拒绝编辑——每天都能立刻给你杠杆。'

T['How is this different from my existing CI pipeline?'] = \
    '这跟我现有的 CI 流水线有何不同？'

T['CI is the *Paddock* of TDD and MDD. This book argues that Paddock alone is insufficient — the Bridle steers before the CI ever runs, the Fence fires at keystroke rather than merge, and the Groom tends the gates themselves. If your CI pipeline catches bugs on Friday evening that could have been caught at commit time on Tuesday morning, your Fence column is underinvested.'] = \
    'CI 是 TDD 与 MDD 的 *牧场*。本书主张：仅有牧场是不够的——缰绳在 CI 跑起来之前就在掰方向；护栏在按键时就触发，而不是合并时；梳理则在照看这些关卡本身。如果你的 CI 流水线是在周五晚上抓到那些本可以在周二早上 commit 时就抓到的 bug，那你的"护栏"这一列投资不足。'

T['What if my team uses Cursor, not Claude Code?'] = \
    '如果我团队用的是 Cursor，不是 Claude Code，怎么办？'

T['The twelve-cell matrix is platform-agnostic. Cursor supports `AGENTS.md`, `.cursor/rules/`, and hooks; the mapping from the Ch.05 artefacts is almost mechanical. The one exception is the `SKILL.md` format, which is Claude-Code-specific as of 2026-04; Cursor users replace it with their own `.cursor/rules/` files of comparable scope.'] = \
    '这套十二格矩阵与平台无关。Cursor 支持 `AGENTS.md`、`.cursor/rules/` 以及钩子；从第 05 章那些制品映射过去几乎是机械性的。唯一例外是 `SKILL.md` 这种格式——截至 2026-04，它是 Claude Code 专属的；Cursor 用户用自己 `.cursor/rules/` 下作用范围相当的文件替换即可。'

T["I already write tests. Isn't that TDD enough?"] = \
    '我已经在写测试了，难道这还不算 TDD？'

T['Having tests is necessary but not sufficient; TDD × Bridle requires the tests to be *failing-first and visible to the agent as input*. See {ref}`tdd-x-bridle`. If your tests were written after the feature was merged, they contribute to TDD × Paddock at best and almost nothing to TDD × Bridle.'] = \
    '写了测试是必要的，但还不充分；TDD × 缰绳 要求这些测试 *先红、且作为输入对智能体可见*。参见 {ref}`tdd-x-bridle`。如果你的测试是在功能合并之后才写的，那么它们顶多算在 TDD × 牧场 里，对 TDD × 缰绳 几乎没贡献。'

T['For Team Leads'] = '面向团队负责人'

T['How do I convince my team to invest in SDD before shipping?'] = \
    '我怎么说服团队在交付之前先投资 SDD？'

T['Run one worked example: score your current repo against the Appendix D blank template (see {ref}`apd-harnesscard-template`), name the lowest-scoring cell, ship one artefact for it, re-score. A +2 delta on a single cell is visible enough to justify the next iteration. Chapter 11 is the canonical example of this pattern.'] = \
    '做一次实打实的演练：用附录 D 的空白模板（见 {ref}`apd-harnesscard-template`）给你现在的仓库打分、点名那一格得分最低的单元、为它交付一件制品、再重新打分。单格 +2 的 delta 已经足够可见，可以支撑下一轮迭代。第 11 章就是这套打法的经典范例。'

T['How does this interact with DORA metrics?'] = \
    '这跟 DORA 度量怎么配合？'

T['DORA measures outcomes; HarnessCards measure *inputs to those outcomes*. A rising `deployment frequency` or falling `change failure rate` is the downstream effect of a well-tended harness. Tracking both lets you tell "the harness is working" apart from "we happened to get lucky". See §12.2 Day 61-90 for the rubric that ties HarnessCards to production SLIs.'] = \
    'DORA 度量的是产出；HarnessCard 度量的是 *通向这些产出的投入*。`deployment frequency` 抬升、`change failure rate` 下降，是一具被照看良好的挽具的下游效应。两者同时追踪，就能把"挽具在起作用"和"我们刚好走运"分开。把 HarnessCard 绑到生产 SLI 的打分尺，见 §12.2 第 61–90 天那一段。'

T['What is the minimum review ritual my team needs?'] = \
    '我团队所需的最小评审仪式是什么？'

T['One role-scoped Verification Table per PR, as per {ref}`sdd-x-paddock`, and one explicit Hard-vs-Soft gate classification for the CI pipeline. These two artefacts together cost roughly one hour per week to maintain and eliminate the most common failure mode — silent rework that never feeds back into the spec.'] = \
    '每份 PR 配一张按角色划分范围的验证表（见 {ref}`sdd-x-paddock`），以及一份针对 CI 流水线的显式"硬关卡 vs 软关卡"分类。这两件制品合起来每周大约一小时维护，就能消除那种最常见的失败模式——"悄悄返工，从来不回灌回规约"。'

T['How do we handle pushback from engineers who see this as overhead?'] = \
    '对那些把这当成额外开销、要反对的工程师，怎么处理？'

T["Ask them to run the exercise in §12.2 Day 1-30 for one week. If the single-cell ship produces zero measurable benefit, the experiment is over and you have learned something. The book's empirical bet — grounded in Peng et al. {cite}`peng2023copilotstudy` and Ziegler et al. {cite}`ziegler2022productivity` — is that one cell at one week will move a measurable productivity metric by the end of month one."] = \
    '请他们把 §12.2 第 1–30 天的练习跑一周。若单格交付带来的可度量收益是 0，这个实验就算结束——你也学到东西了。本书的经验押注——以 Peng 等 {cite}`peng2023copilotstudy` 与 Ziegler 等 {cite}`ziegler2022productivity` 为依据——是：一格、一周，到第一个月结束时会撬动一条可度量的生产率指标。'

T['How do we tell harness work from harness theatre?'] = \
    '我们怎么把真正的挽具工作，跟挽具剧场区分开？'

T['One diagnostic, asked every Monday: *what did the harness refuse, measure, or steer this past week, and was it right to do so?* A healthy harness produces a concrete answer — a commit it blocked, a tool call it caught, a dashboard signal it crossed. A theatrical harness produces a list of *additions* ("we wrote a new skill", "we added a hook") with no corresponding events. If the team can only answer the additions question, the harness is growing but not leveraging. Glossary entry *Harness Theatre* enumerates the common subtypes; the Ch.06 closing note gives the canonical diagnostic.'] = \
    '一条每周一都要问的诊断：*上周这具挽具拒了什么、度量了什么、掰过什么方向，这些做得对吗？* 一具健康的挽具能给出具体答案——它挡下了一次 commit、抓住了一次工具调用、越过了一条仪表盘信号。一具剧场化的挽具只会产出一串 *加法*（"我们写了个新 skill"、"我们加了一条钩子"），没有对应事件。若团队只答得出"加法"那一问，说明挽具在长肥、却没在起杠杆。术语表中的 *挽具剧场* 条目列出了常见子类；第 06 章收尾那一段给出的是正式诊断。'

T['Our HarnessCard scores keep rising but nothing downstream moves. Why?'] = \
    '我们 HarnessCard 的得分一直在涨，下游却没什么动静。为什么？'

T["The vanity-delta pattern Chapter 11 names explicitly. The HarnessCard is a *diagnostic* rubric — its role is to identify weak cells, not to be optimised against. When cell scores rise but DORA metrics don't follow, the team is paying down debt that was not costing anything. **Fix**: pair every planned HarnessCard delta with one outcome metric it is *predicted* to move (deployment frequency, change failure rate, incident count). If the outcome does not move after a quarter, the previous quarter's investment was vanity, and next quarter's investment should target a different cell — or ask whether the product is bottlenecked by something other than the harness entirely."] = \
    '这就是第 11 章点名的"虚荣 delta"模式。HarnessCard 是一份 *诊断* 打分尺——它的角色是"识别弱格"，不是"被优化的对象"。当格子得分在涨、DORA 指标却不跟着动，那支团队是在偿还一笔本来根本没在收利息的债。**解法**：为每一项计划中的 HarnessCard delta，配一条它 *被预言要移动* 的产出指标（部署频率、变更失败率、事故数）。若一个季度后该产出未动，上一个季度的投资就是虚荣；下一个季度的投资应换到另一格——或者反思：产品的瓶颈是不是根本就不在挽具上。'

T['For Skeptics'] = '面向怀疑者'

T["Isn't this just rebranded DevOps?"] = \
    '这不就是 DevOps 换个说法吗？'

T["DevOps packages CI/CD, infra-as-code, and deployment automation; this book argues that agent-era software engineering needs a vocabulary *upstream* of those practices — the Bridle steers before the CI runs, the SDD guardian shapes the spec before the code is written. Chapter 03's comparison table lays out the boundary explicitly. DevOps remains necessary and is not replaced by harness work."] = \
    'DevOps 打包的是 CI/CD、基础设施即代码、部署自动化；本书主张——智能体时代的软件工程，需要一套 *上游* 于这些实践的词汇：缰绳在 CI 跑起来之前就在掰方向，SDD 那位护法在代码写下来之前就在塑造规约。第 03 章的对比表把这条边界画得很明确。DevOps 依旧是必需的，并不被挽具工作所取代。'

T["Isn't this just prompt engineering?"] = \
    '这不就是 prompt engineering 吗？'

T["Prompt engineering is one cell (SDD × Bridle). The other eleven cells — fences, paddocks, grooms, TDD, MDD — are irreducible to prompt authorship. Karpathy's context-engineering framing {cite}`karpathy2025context` is a step beyond prompt engineering; the three-guardian × four-zone matrix is a step beyond that."] = \
    'Prompt engineering 只是一格（SDD × 缰绳）。其余十一格——护栏、牧场、梳理、TDD、MDD——都不能被还原为"写 prompt"。Karpathy 的 context engineering 说法 {cite}`karpathy2025context` 在 prompt engineering 之上再走了一步；这套"三大护法 × 四区域"矩阵，又在那之上再走一步。'

T["You cite the author's own blog a lot. Isn't that a red flag?"] = \
    '你大量引用作者自己的博客，这不是危险信号吗？'

T["The four-zone naming is explicitly acknowledged as practitioner-origin in §05.Provenance; the academic grounding is the CAR / HarnessCard paper {cite}`car2025decomposition` and the five industrial triangulation sources listed throughout. The book never hides that the naming is the author's; what it does is triangulate against three independently-developed adjacent frameworks."] = \
    '四区域这套命名，在 §05.Provenance 中被明确承认为"从业者起源"；学术根基是 CAR／HarnessCard 论文 {cite}`car2025decomposition`，以及本书各处列出的五个独立工业三角来源。本书从不掩饰"这份命名是作者的"；它所做的，是让这套命名与三套独立发展起来的相邻框架互相三角印证。'

T['How do I know this will still be relevant in 2027?'] = \
    '我怎么知道这本书到 2027 年还有用？'

T["Short answer: you do not. The book's 30-day, 60-day, 90-day structure assumes that *specific artefacts* will age out faster than the *framework* itself. Lehman's evolution laws {cite}`lehman1980laws` apply to the book as much as to any codebase; §12.3 names the open questions whose resolution will most likely drive a second edition."] = \
    '短答：你不知道。本书的 30 天／60 天／90 天结构假设：*具体制品* 会比 *框架本身* 更快老化。Lehman 的演化定律 {cite}`lehman1980laws` 对本书与对任何代码库同样适用；§12.3 点出了那些悬而未决的问题——它们的解决，最有可能驱动一次再版。'

T['My agent passes every check and still ships wrong code. What gives?'] = \
    '我的智能体每道检查都通过，却还是把错代码交上去。什么情况？'

T['Three possibilities, in descending frequency. First, **test-pinning**: the tests pass because the agent landed on one of many interpretations consistent with them; the interpretation the human wanted was never pinned down (Ch.04). Fix by adding adversarial tests that attack the cheapest path to green. Second, **spec drift**: the agent is conforming to `AGENTS.md` while the codebase has silently evolved away from it (Ch.04). Fix by scheduling a weekly spec-vs-code diff. Third, **ambiguity amplification**: one vague bullet in the spec is producing wildly different but all-locally-correct implementations (Ch.04). Fix by tightening that bullet until a hook can check it. All three are visible in the glossary; all three are inline pitfalls in Ch.04.'] = \
    '三种可能，出现频次递减。第一，**错误钉死**：测试之所以过，是因为智能体落在了与测试一致的众多解读之一；人类真正想要的那种解读，从未被钉死（第 04 章）。解法：加一些"针对最便宜变绿路径"的对抗测试。第二，**规约漂移**：智能体在向 `AGENTS.md` 对齐，而代码库已经悄悄漂走（第 04 章）。解法：安排每周一次的"规约 vs 代码" diff。第三，**歧义放大**：规约里一条含糊的条目，正在生出一堆差别巨大却 *局部都对* 的实现（第 04 章）。解法：把那条拧紧，直到有一条钩子能去检查它。这三种在术语表里都有；这三种在第 04 章里都是行内陷阱。'

T['For Chinese-Context Readers'] = '面向中文语境读者'

T['Why are the examples English when my codebase is Chinese?'] = \
    '为什么示例是英文的？我代码库是中文的。'

T["Code artefacts (YAML, JSON Schema, shell scripts) are generally language-neutral and copy verbatim. The prose chapters (`AGENTS.md`, `CLAUDE.md`) benefit from matching your team's working language. The book ships with a Simplified-Chinese translation of the Foreword, Ch.03, Ch.04, Ch.05, and Ch.12 for exactly this reason; the language switcher in the top-left of every page toggles between the two."] = \
    '代码类制品（YAML、JSON Schema、shell 脚本）通常与语言无关，可原样拷贝。散文类章节（`AGENTS.md`、`CLAUDE.md`）则以匹配团队工作语言为宜。正因如此，本书随书附有序言、第 03 章、第 04 章、第 05 章与第 12 章的简体中文译本；每一页左上角的语言切换器可以在两种语言之间切换。'

T['How does《马书》 relate to this book?'] = \
    '《马书》与本书是什么关系？'

T['《马书》 {cite}`zhangbook2026` is an excellent reverse-engineering study of Claude Code specifically. Chapter 10 cites it extensively and is the only chapter that does. This book sits one level up: it builds a *framework* for scoring harnesses in general, of which Claude Code is one instance among several.'] = \
    '《马书》{cite}`zhangbook2026` 是一份针对 Claude Code 的逆向工程研究，做得非常好。第 10 章对它大量引用，也是全书唯一引它的章节。本书站在它之上一层：它构建的是一套 *框架*——一套给"挽具"打分的通用尺子——Claude Code 只是其中一个实例。'

T['Do I need to read the book in order?'] = \
    '我需要按顺序读这本书吗？'

T['No. If you know the guardians already, start with Chapter 05 (the matrix), then jump to whichever case study (07–10) covers the harness closest to your day-to-day, then come back to Chapter 11 for the lazy-ai-coder worked example. The Foreword and Chapter 02 are useful background but are not prerequisites for the matrix.'] = \
    '不需要。如果你已经熟悉那几位护法，从第 05 章（那张矩阵）开始，然后跳到 07–10 中任一篇最贴近你日常工作的案例研究，再回到第 11 章看那份 lazy-ai-coder 的实例。序言和第 02 章是有用的背景，但不是理解那张矩阵的前置。'

T['What Chinese-language resources do you recommend?'] = \
    '你推荐哪些中文资源？'

T["《马书》 for Claude Code specifically {cite}`zhangbook2026`; the author's 2026-03-28 blog post for the original four-zone essay {cite}`walterfan2026guardians`; Appendix C for a broader reading list."] = \
    '针对 Claude Code，看《马书》{cite}`zhangbook2026`；看作者 2026-03-28 那篇博文，可以读到"四区域"的原始论述 {cite}`walterfan2026guardians`；更全的阅读单见附录 C。'

T['About the Book Itself'] = '关于这本书本身'

T['Why Sphinx instead of mdBook?'] = \
    '为什么选 Sphinx 而不是 mdBook？'

T['Three reasons: native `sphinx-intl` support for bilingual publishing, `sphinxcontrib-bibtex` for first-class academic citations, and the MyST directive ecosystem for `{literalinclude}` from hands-on artefacts. A team with different priorities might reasonably choose mdBook; the colophon carries the full rationale.'] = \
    '三个理由：`sphinx-intl` 原生支持双语出版；`sphinxcontrib-bibtex` 提供一等公民级的学术引用；以及 MyST 指令生态——让我们能用 `{literalinclude}` 从 hands-on 制品里原样嵌入。换一套优先级的团队，选择 mdBook 也完全合理；版权页那页给出了完整理由。'

T['Why is Chapter 11 in draft status?'] = \
    '为什么第 11 章处于 draft 状态？'

T["Chapter 11 ships `status: draft` until Section 14's four commits land on the host repository's `main`. The book-lint script walks the Act 3 commit SHAs through `git cat-file -e`; until at least two resolve, the chapter is excluded from the toctree. See §14 for the current landing schedule."] = \
    '第 11 章保持 `status: draft`，直到第 14 节那四笔 commit 合入宿主仓库的 `main`。book-lint 脚本会用 `git cat-file -e` 遍历第三幕的 commit SHA；在至少两笔解析成功之前，本章会被排除在 toctree 之外。合入时间表见 §14。'

T['How do I contribute?'] = '我怎么贡献？'

T['See `book/CONTRIBUTING.md` in the source repository. Short summary: new citations go into the `_bib/*.bib` file matching their kind; new hands-on artefacts go under `_handson/<chapter-slug>/` with a `verified: YYYY-MM-DD` header comment; new matrix cells require an extension to `book_lint.py` to enforce the citation-plus-artefact rule.'] = \
    '见源代码仓库中的 `book/CONTRIBUTING.md`。一句话总结：新引用放进 `_bib/*.bib` 中按类型匹配的那一份；新 hands-on 制品放在 `_handson/<chapter-slug>/` 下，并带一条 `verified: YYYY-MM-DD` 头注；新矩阵格子需要扩展 `book_lint.py`，以强制执行"引用 ＋ 制品"这条规则。'

T['What licence is the book under?'] = \
    '本书采用什么许可证？'

T['Prose is CC-BY-SA-4.0, code samples are MIT, and quoted excerpts preserve their upstream licence. See `book/LICENSE` for the complete text.'] = \
    '散文部分 CC-BY-SA-4.0，代码示例 MIT，被引用的片段保留其上游许可证。完整文本见 `book/LICENSE`。'


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
