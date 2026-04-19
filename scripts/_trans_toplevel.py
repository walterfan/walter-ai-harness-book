"""One-shot translator for top-level colophon, index, references."""
import polib

# ------------------------------------------------------------
# colophon.po
# ------------------------------------------------------------
T_COL = {}
T_COL['Colophon'] = '版记'
T_COL['How this book was built'] = '本书是怎样造出来的'
T_COL['*Harnessing AI: The Craft of Shaping Agents* — rendered in Chinese as 《驾驭工程：给 AI 套上缰绳》 — is produced from a single English Markdown source tree under ``book/source/``, translated into Simplified Chinese via ``sphinx-intl`` gettext catalogs, and rendered to HTML by **Sphinx** + **MyST** + **sphinxcontrib-bibtex** + the **Read the Docs** theme. Citations live in BibTeX files under ``_bib/``; diagrams are authored as ``{mermaid}`` (inline) or ``{plantuml}`` (separate ``.puml`` file) directives. A structural linter — ``make book-lint`` — enforces the three-guardian × four-zone matrix contract, the dual-track chapter skeleton, Chapter 03\'s definition sections, Chapter 05\'s provenance declaration, Chapter 11\'s four-act structure, and Chapter 12\'s 30/60/90 checklist discipline.'] = \
    '*Harnessing AI: The Craft of Shaping Agents* —— 中文名《驾驭工程：给 AI 套上缰绳》—— 是从 ``book/source/`` 下一棵单一的英文 Markdown 源码树生成的，经由 ``sphinx-intl`` 的 gettext catalog 翻译成简体中文，再由 **Sphinx** ＋ **MyST** ＋ **sphinxcontrib-bibtex** ＋ **Read the Docs** 主题渲染成 HTML。引用住在 ``_bib/`` 下的 BibTeX 文件里；图则用 ``{mermaid}``（嵌入式）或 ``{plantuml}``（独立 ``.puml`` 文件）directive 编写。一把结构 linter —— ``make book-lint`` —— 负责强制执行那份"三护法 × 四区域"矩阵契约、双轨章骨架、第 03 章的定义小节、第 05 章的出处声明、第 11 章的四幕结构、以及第 12 章的 30／60／90 清单纪律。'

T_COL['The book is its own harness demonstration'] = \
    '本书本身就是它自己的那套挽具示范'
T_COL['The book is written the way it preaches. We apply the 3×4 matrix to the book itself, and cross-reference each cell to the chapter that taught the concept:'] = \
    '本书是按它自己宣讲的那套方式写出来的。我们把那张 3×4 矩阵施加在本书自身之上，并把每一格回指到教过该概念的那一章：'

T_COL['**Bridle (guidance)** — ``_bib/`` supplies the canonical citation record; every chapter\'s Research Foundations section carries ``{cite}`` roles resolving to entries here. See {ref}`sdd-x-bridle` for the general pattern.'] = \
    '**缰绳（引导）** —— ``_bib/`` 提供权威引用记录；每一章的 Research Foundations 小节中的 ``{cite}`` 角色，都会解析到这里的条目。通用模式见 {ref}`sdd-x-bridle`。'
T_COL['**Fence (constraints)** — ``make book-lint`` enforces every structural contract; the ``book-structure`` spec, in turn, enforces what ``book-lint`` must check. See {ref}`sdd-x-fence` for the general pattern and {ref}`tdd-x-fence` for the hook-level twin.'] = \
    '**护栏（约束）** —— ``make book-lint`` 强制执行每一份结构契约；``book-structure`` 规约，反过来，又强制规定 ``book-lint`` 必须去检查哪些东西。通用模式见 {ref}`sdd-x-fence`，钩子层的孪生兄弟见 {ref}`tdd-x-fence`。'
T_COL['**Paddock (boundaries / acceptance)** — a strict Sphinx build (``-W --keep-going -n``) gates every PR touching ``book/**``. See {ref}`tdd-x-paddock` for the general pattern.'] = \
    '**牧场（边界 ／ 验收）** —— 一次严格的 Sphinx 构建（``-W --keep-going -n``）会为每一份触及 ``book/**`` 的 PR 把关。通用模式见 {ref}`tdd-x-paddock`。'
T_COL['**Groom (maintenance)** — ``make book-intl`` keeps the zh_CN ``.po`` catalogs fresh; the translation-freshness banner surfaces rot automatically. See {ref}`sdd-x-groom` and {ref}`mdd-x-groom` for the grooming patterns the book\'s own workflow instantiates.'] = \
    '**梳理（维护）** —— ``make book-intl`` 让 zh_CN 的 ``.po`` catalog 保持新鲜；翻译新鲜度横幅会自动把朽坏浮上来。本书自身工作流所实例化的那些梳理模式，见 {ref}`sdd-x-groom` 与 {ref}`mdd-x-groom`。'

T_COL['License & attribution'] = '许可证与署名'
T_COL['Prose and diagrams authored for this book: **CC-BY-SA-4.0**.'] = \
    '为本书撰写的正文与图：**CC-BY-SA-4.0**。'
T_COL['Code samples authored for this book: **MIT**, matching the rest of the host repository.'] = \
    '为本书写的代码样例：**MIT**，与宿主仓库的其余部分保持一致。'
T_COL['Quoted excerpts from third-party sources (OpenHarness, Superpowers, 《马书》, etc.) retain their upstream licenses; each excerpt carries an inline attribution footer naming the source and license.'] = \
    '引用自第三方来源（OpenHarness、Superpowers、《马书》等）的片段，保留各自上游的许可证；每一段引文都附一段嵌入式署名脚注，点名出处与许可证。'
T_COL['See ``book/LICENSE`` for the definitive text.'] = \
    '权威条款见 ``book/LICENSE``。'

T_COL['Author & acknowledgements'] = '作者与致谢'
T_COL['Author: Walter Fan. Editorial review, translation, and harness-testing contributions are credited in the chapter where they land. A rolling acknowledgement index lives at the bottom of ``book/CONTRIBUTING.md``.'] = \
    '作者：Walter Fan。编辑评审、翻译、挽具实测方面的贡献，在各自落地的那一章里单独署名。一份滚动更新的致谢索引住在 ``book/CONTRIBUTING.md`` 的末尾。'

T_COL['Credits and thanks'] = '鸣谢'
T_COL['Specific projects, books, and individuals whose work is load-bearing in this book:'] = \
    '那些作品在本书中起到承重作用的具体项目、书籍与个人：'
T_COL['**HKU Data Science Lab** for **OpenHarness** {cite}`hkuds2025openharness` — the open-source reference implementation Chapter 07 treats.'] = \
    '**港大数据科学实验室** 之 **OpenHarness** {cite}`hkuds2025openharness` —— 第 07 章所处理的那份开源参考实现。'
T_COL['**Joseph Vincent (David Vincent, `obra`)** for **Superpowers** {cite}`vincent2025superpowers` — the skills library Chapter 08 treats.'] = \
    '**Joseph Vincent（David Vincent，`obra`）** 之 **Superpowers** {cite}`vincent2025superpowers` —— 第 08 章所处理的那份技能库。'
T_COL['**The `lazy-scrum-team` authors** {cite}`lazyscrumteam2026` — whose workflow-encoded harness is Chapter 09\'s canonical treatment.'] = \
    '**`lazy-scrum-team` 的作者们** {cite}`lazyscrumteam2026` —— 他们那份以工作流编码的挽具，是第 09 章的权威对象。'
T_COL['**Zhang Handong (张汉东)** for **《马书》** {cite}`zhangbook2026` — the reverse-engineering study that makes Chapter 10 tractable.'] = \
    '**张汉东** 之 **《马书》** {cite}`zhangbook2026` —— 正是那份逆向工程研究，让第 10 章得以成立。'
T_COL['**The authors of the CAR / HarnessCard position paper** {cite}`car2025decomposition` — whose disclosure format Appendix D serialises against.'] = \
    '**CAR ／ HarnessCard 立场论文的作者们** {cite}`car2025decomposition` —— 附录 D 所遵循序列化的那套披露格式。'
T_COL['**The `walkinglabs/awesome-harness-engineering` curators** {cite}`walkinglabs2026awesome` — the ongoing curated list that complements this long-form methodology.'] = \
    '**`walkinglabs/awesome-harness-engineering` 的维护者们** {cite}`walkinglabs2026awesome` —— 那份与本书这份长篇方法论互补的、持续更新的精选列表。'

# ------------------------------------------------------------
# index.po
# ------------------------------------------------------------
T_IDX = {}
T_IDX['Part I · Why'] = '第一部分 · 为什么'
T_IDX['Part II · What'] = '第二部分 · 是什么'
T_IDX['Part III · How'] = '第三部分 · 怎么做'
T_IDX['Part IV · Example'] = '第四部分 · 例子'
T_IDX['Part V · Conclusion'] = '第五部分 · 结语'
T_IDX['Part VI · Reference'] = '第六部分 · 参考'

T_IDX['Harnessing AI: The Craft of Shaping Agents'] = \
    '驾驭工程：给 AI 套上缰绳'
T_IDX['*A long-form, bilingual book about **Harness Engineering** — the deliberate practice of shaping the environment in which AI coding agents operate so the software they produce is verifiable, observable, and understandable.*'] = \
    '*一本关于 **挽具工程** 的长篇、双语之作 —— 一种刻意塑造 AI 编码智能体所处环境的实践，好让它们生产出来的软件是可验证、可观测、可理解的。*'

T_IDX['**Author**'] = '**作者**'
T_IDX['Walter Fan'] = 'Walter Fan'
T_IDX['**License**'] = '**许可证**'
T_IDX['CC-BY-SA-4.0 (prose) · MIT (code samples)'] = \
    'CC-BY-SA-4.0（正文）· MIT（代码样例）'
T_IDX['**Status**'] = '**状态**'
T_IDX['Draft — scaffolding in place, chapters being written'] = \
    '草稿 —— 骨架就位，章节正在撰写中'
T_IDX['**Source**'] = '**源码**'
T_IDX['[`book/source/`](https://github.com/walterfan/lazy-ai-coder/tree/main/book/source)'] = \
    '[`book/source/`](https://github.com/walterfan/lazy-ai-coder/tree/main/book/source)'

T_IDX['How to read this book'] = '本书怎么读'
T_IDX['The book follows a six-part argumentative arc — **Why → What → How → Example → Conclusion → Reference**. Most readers should read Parts I and II linearly, then dip into Part III for the methodology they need most, then pick one or two Part IV case studies close to their own stack. Part V is short and action-oriented; Part VI is a reference.'] = \
    '本书循一条六段式的论证弧线 —— **为什么 → 是什么 → 怎么做 → 例子 → 结语 → 参考**。大多数读者应当把第一、第二部分顺着读下去，然后进第三部分挑自己最需要的那一份方法论，再从第四部分挑一两份贴近自身技术栈的案例研究。第五部分短小、偏行动；第六部分是参考。'
T_IDX['Every substantive chapter (Chapters 02–12) follows the same two-section skeleton below its body: ``## Research Foundations`` grounds the argument in citable prior work, and ``## Hands-On`` ships at least one runnable artefact. The chapters deliberately pair theory with practice.'] = \
    '每一份有实质内容的章（第 02 至第 12 章）都在正文下方遵循同一副双节骨架：``## Research Foundations`` 把论证钉在可引用的先前工作之上，``## Hands-On`` 则至少交付一件可跑起来的制品。这些章节是刻意把理论与实践配对的。'

# ------------------------------------------------------------
# references.po
# ------------------------------------------------------------
T_REF = {}
T_REF['References'] = '参考文献'
T_REF['This page lists every work referenced in the book. The first section shows the works actually cited in the prose; the second section shows the complete curated reading list maintained in ``_bib/*.bib`` (including works not yet cited, kept for Appendix&nbsp;C\'s use).'] = \
    '本页列出本书引用到的每一件作品。第一小节展示正文中实际被引用到的那些作品；第二小节展示维护在 ``_bib/*.bib`` 中的完整精选阅读单（包括尚未被引用、但留给附录 C 使用的作品）。'
T_REF['Cited in this book'] = '本书实际引用的作品'
T_REF['Full curated reading list'] = '完整精选阅读单'
T_REF['This section uses ``:all:`` to force rendering of every entry, so Appendix C can point at a comprehensive reading list even before every entry is cited. Per the ``sphinxcontrib-bibtex`` convention, entries shown only here (and not in the section above) are **not** resolvable via ``{cite}`` — they appear as orphan bibliography entries by design.'] = \
    '本小节使用 ``:all:`` 强制渲染每一条条目，这样附录 C 就可以指向一份完整的阅读单 —— 哪怕此时还并非每一条都已被引用。按 ``sphinxcontrib-bibtex`` 的惯例，仅在本小节出现（而未在上面那个小节出现）的条目，是 **不可** 经由 ``{cite}`` 解析的 —— 它们按设计以"孤儿"书目条目的身份出现。'


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
    for m in miss[:3]:
        print('  MISS:', repr(m[:200]))


def main():
    apply('source/locale/zh_CN/LC_MESSAGES/colophon.po', T_COL, 'colophon')
    apply('source/locale/zh_CN/LC_MESSAGES/index.po', T_IDX, 'index')
    apply('source/locale/zh_CN/LC_MESSAGES/references.po', T_REF, 'references')


if __name__ == '__main__':
    main()
