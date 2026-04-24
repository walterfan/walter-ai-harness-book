---
status: draft
chapter-type: appendix
---

# 附录 C —— 阅读单与外部资源

下面每一条都以一个 BibTeX key 引用；权威记录——作者、标题、DOI、URL——都住在 `_bib/*.bib` 里，不嵌在正文中。想看完整引用的读者请去 `references.md`（参考文献）。

## 理论根基

本框架所依赖的那些理论与历史论文：

- Lehman 1980 年的软件演化定律 {cite}`lehman1980laws`。
- Cunningham 1992 年的技术债隐喻 {cite}`cunningham1992debt`。
- Conway 1968 年的定律 {cite}`conway1968law`。
- Meyer 1992 年的契约式设计论文 {cite}`meyer1992contracts`。
- Ford、Parsons 与 Kua 2017 年的 *Building Evolutionary Architectures* {cite}`ford2017buildingevolutionary`。
- Feathers 2004 年的 *Working Effectively with Legacy Code* {cite}`feathers2004legacy`。

## 三大护法（SDD ／ TDD ／ MDD）

- Martraire 2019 年 *Living Documentation* —— SDD 谱系 {cite}`martraire2019living`。
- Adzic 2011 年 *Specification by Example* —— SDD × 牧场 谱系 {cite}`adzic2011specbyexample`。
- Beck 2002 年 *TDD by Example* —— TDD 谱系 {cite}`beck2002tdd`。
- Zeller 2009 年 *Why Programs Fail* —— TDD 调试谱系 {cite}`zeller2009whyprogramsfail`。
- Bacchelli 与 Bird 2013 年的现代代码评审研究 {cite}`bacchelli2013codereview`。
- Majors、Fong-Jones 与 Miranda 2022 年 *Observability Engineering* —— MDD 谱系 {cite}`majors2022observability`。
- Sculley 等 2015 年的 ML 技术债论文 —— MDD 的警世寓言 {cite}`sculley2015mltechdebt`。

## 基准测试

案例研究章节中引用到的公开基准测试：

- LangChain 2026 年 Terminal Bench 2.0 的博客文章 {cite}`langchain2026tbench`。
- Peng 等 2023 年的 Copilot 生产力研究 {cite}`peng2023copilotstudy`。
- Ziegler 等 2022 年的生产力研究 {cite}`ziegler2022productivity`。

## 开源参考实现

本书作为案例研究打过分的那些马具项目：

- 港大 DS Lab 的 OpenHarness {cite}`hkuds2025openharness` —— 第 07 章。
- Joseph Vincent 的 Superpowers {cite}`vincent2025superpowers,vincent2025superpowersrepo` —— 第 08 章。
- lazy-scrum-team Claude Code／Cursor 技能 {cite}`lazyscrumteam2026` —— 第 09 章。
- OpenAI harness ／ RFT 工具包 {cite}`openai2026harness` —— 相邻项目。

## 持续更新的资源

那些比本书更新更快的精选列表、厂商文档与公开讨论：

- `walkinglabs/awesome-harness-engineering` —— 权威的、持续更新的精选列表 {cite}`walkinglabs2026awesome`。**与本书的范围差别**：本书是一份长篇方法论，带强立场、"研究 ＋ 实践"双轨、以及一条可强制执行的双轨 lint 规则；而 *awesome* 列表则是一份不持立场、持续更新的论文、博文与项目精选。二者是互补关系，不是替代关系。
- Anthropic 的 Claude Code 文档与发布文章 {cite}`anthropic2024claudecode,anthropic2024skills`。
- MCP 规范及其参考实现 server {cite}`anthropic2024mcp`。
- 张汉东的《马书》—— 对 Claude Code 的中文逆向工程研究 {cite}`zhangbook2026`。

## 相邻领域

那些与马具工程有重叠、却并不等同的领域：

- *DevOps* —— Humble 与 Farley 2010 年的 *Continuous Delivery* {cite}`humble2010continuousdelivery`，以及 Forsgren 等 2018 年的 *Accelerate* {cite}`forsgren2018accelerate`。
- *Scrum 与敏捷流程* —— Schwaber 与 Sutherland 2020 年的 Scrum Guide {cite}`schwaber2020scrum`。
- *技术债管理* —— Tom 等 2013 年的系统综述 {cite}`tom2013debtinterest`。
- *MLOps 与 AI 工程* —— Huyen 2025 年的 *AI Engineering* {cite}`huyen2025aieng`。
- *平台工程* —— CNCF 的平台工程成熟度模型 {cite}`cncf2024platformeng`。
- *可靠性工程* —— Ford 等 2017 年的演化式架构，横跨本组与"理论根基"组 {cite}`ford2017buildingevolutionary`。
