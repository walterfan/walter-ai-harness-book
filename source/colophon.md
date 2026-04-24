---
status: draft
---

# 版记

## 本书是怎样造出来的

《驾驭工程：给 AI 套上缰绳》（英文题名 *Harnessing AI: The Craft of Shaping Agents*）是从 ``source/`` 下一棵中文 Markdown 源码树生成的，再由 **Sphinx** ＋ **MyST** ＋ **sphinxcontrib-bibtex** ＋ **Read the Docs** 主题渲染成 HTML。引用住在 ``_bib/`` 下的 BibTeX 文件里；图则用 ``{mermaid}``（嵌入式）或 ``{plantuml}``（独立 ``.puml`` 文件）directive 编写。一把结构 linter —— ``make book-lint`` —— 负责强制执行那份"三护法 × 四区域"矩阵契约、双轨章骨架、第 03 章的定义小节、第 05 章的出处声明、第 11 章的四幕结构、以及第 12 章的 30／60／90 清单纪律。

## 本书本身就是它自己的那套马具示范

本书是按它自己宣讲的那套方式写出来的。我们把那张 3×4 矩阵施加在本书自身之上，并把每一格回指到教过该概念的那一章：

* **缰绳（引导）** —— ``_bib/`` 提供权威引用记录；每一章的"研究脉络"小节中的 ``{cite}`` 角色，都会解析到这里的条目。通用模式见 {ref}`sdd-x-bridle`。
* **护栏（约束）** —— ``make book-lint`` 强制执行每一份结构契约；``book-structure`` 规约，反过来，又强制规定 ``book-lint`` 必须去检查哪些东西。通用模式见 {ref}`sdd-x-fence`，钩子层的孪生兄弟见 {ref}`tdd-x-fence`。
* **牧场（边界 ／ 验收）** —— 一次严格的 Sphinx 构建（``-W --keep-going -n``）会为每一份触及 ``book/**`` 的 PR 把关。通用模式见 {ref}`tdd-x-paddock`。
* **梳理（维护）** —— ``make html`` 与 ``make book-lint`` 让中文源文、引用、链接和结构约束保持新鲜；本书自身工作流所实例化的那些梳理模式，见 {ref}`sdd-x-groom` 与 {ref}`mdd-x-groom`。

## 许可证与署名

* 为本书撰写的正文与图：**CC-BY-SA-4.0**。
* 为本书写的代码样例：**MIT**，与宿主仓库的其余部分保持一致。
* 引用自第三方来源（OpenHarness、Superpowers、《马书》等）的片段，保留各自上游的许可证；每一段引文都附一段嵌入式署名脚注，点名出处与许可证。

权威条款见 ``book/LICENSE``。

## 作者与致谢

作者：Walter Fan。编辑评审、翻译、马具实测方面的贡献，在各自落地的那一章里单独署名。一份滚动更新的致谢索引住在 ``book/CONTRIBUTING.md`` 的末尾。

## 鸣谢

那些作品在本书中起到承重作用的具体项目、书籍与个人：

* **港大数据科学实验室** 之 **OpenHarness** {cite}`hkuds2025openharness` —— 第 07 章所处理的那份开源参考实现。
* **Joseph Vincent（David Vincent，`obra`）** 之 **Superpowers** {cite}`vincent2025superpowers` —— 第 08 章所处理的那份技能库。
* **`lazy-scrum-team` 的作者们** {cite}`lazyscrumteam2026` —— 他们那份以工作流编码的马具，是第 09 章的权威对象。
* **张汉东** 之 **《马书》** {cite}`zhangbook2026` —— 正是那份逆向工程研究，让第 10 章得以成立。
* **CAR ／ HarnessCard 立场论文的作者们** {cite}`car2025decomposition` —— 附录 D 所遵循序列化的那套披露格式。
* **`walkinglabs/awesome-harness-engineering` 的维护者们** {cite}`walkinglabs2026awesome` —— 那份与本书这份长篇方法论互补的、持续更新的精选列表。
