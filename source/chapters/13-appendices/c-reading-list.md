---
status: draft
chapter-type: appendix
---

# Appendix C — Reading List & External Resources

Every entry below cites a BibTeX key; the canonical record — author, title,
DOI, URL — stays in `_bib/*.bib`, not inline. Readers who want the full
references should consult `references.md` (bibliography).

## Foundations

Theoretical and historical papers the framework rests on:

- Lehman's 1980 laws of software evolution {cite}`lehman1980laws`.
- Cunningham's 1992 debt metaphor {cite}`cunningham1992debt`.
- Conway's 1968 law {cite}`conway1968law`.
- Meyer's 1992 design-by-contract paper {cite}`meyer1992contracts`.
- Ford, Parsons & Kua's 2017 *Building Evolutionary Architectures*
  {cite}`ford2017buildingevolutionary`.
- Feathers 2004 *Working Effectively with Legacy Code*
  {cite}`feathers2004legacy`.

## The Three Guardians (SDD / TDD / MDD)

- Martraire 2019 *Living Documentation* — SDD lineage
  {cite}`martraire2019living`.
- Adzic 2011 *Specification by Example* — SDD × Paddock lineage
  {cite}`adzic2011specbyexample`.
- Beck 2002 *TDD by Example* — TDD lineage {cite}`beck2002tdd`.
- Zeller 2009 *Why Programs Fail* — TDD debugging lineage
  {cite}`zeller2009whyprogramsfail`.
- Bacchelli & Bird 2013 modern-code-review study
  {cite}`bacchelli2013codereview`.
- Majors, Fong-Jones & Miranda 2022 *Observability Engineering* — MDD
  lineage {cite}`majors2022observability`.
- Sculley et al. 2015 ML technical-debt paper — MDD cautionary tale
  {cite}`sculley2015mltechdebt`.

## Benchmarks

Public benchmarks referenced in the case-study chapters:

- LangChain 2026 Terminal Bench 2.0 blog post
  {cite}`langchain2026tbench`.
- Peng et al. 2023 Copilot productivity study
  {cite}`peng2023copilotstudy`.
- Ziegler et al. 2022 productivity study
  {cite}`ziegler2022productivity`.

## Open-Source Reference Implementations

The harness projects the book scores as case studies:

- HKUDS OpenHarness {cite}`hkuds2025openharness` — Ch.07.
- Joseph Vincent Superpowers
  {cite}`vincent2025superpowers,vincent2025superpowersrepo` — Ch.08.
- lazy-scrum-team Claude Code / Cursor skill
  {cite}`lazyscrumteam2026` — Ch.09.
- OpenAI harness / RFT toolkit {cite}`openai2026harness` — adjacent.

## Ongoing Resources

Curated lists, vendor docs, and public discussions that update faster
than this book:

- `walkinglabs/awesome-harness-engineering` — the canonical ongoing
  curated list {cite}`walkinglabs2026awesome`. **Scope difference from
  this book.** This book is a long-form methodology with strong
  opinions, dual-track research-plus-practice, and an enforceable
  dual-track lint rule; the *awesome* list is an ongoing unopinionated
  curation of papers, posts, and projects. The two are complements, not
  substitutes.
- Anthropic Claude Code documentation and launch posts
  {cite}`anthropic2024claudecode,anthropic2024skills`.
- MCP specification and reference servers {cite}`anthropic2024mcp`.
- Zhang Handong's《马书》 — Chinese-language Claude Code reverse-engineering
  study {cite}`zhangbook2026`.

## Adjacent Fields

Fields that overlap with harness engineering without being identical:

- *DevOps* — Humble & Farley 2010 *Continuous Delivery*
  {cite}`humble2010continuousdelivery` and Forsgren et al. 2018
  *Accelerate* {cite}`forsgren2018accelerate`.
- *Scrum and agile process* — Schwaber & Sutherland 2020 Scrum Guide
  {cite}`schwaber2020scrum`.
- *Technical debt management* — Tom et al. 2013 systematic review
  {cite}`tom2013debtinterest`.
- *MLOps and AI engineering* — Huyen 2025 *AI Engineering*
  {cite}`huyen2025aieng`.
- *Platform engineering* — CNCF platform-engineering maturity model
  {cite}`cncf2024platformeng`.
- *Reliability engineering* — Ford et al. 2017 evolutionary architecture
  crosses both this and the Foundations group
  {cite}`ford2017buildingevolutionary`.
