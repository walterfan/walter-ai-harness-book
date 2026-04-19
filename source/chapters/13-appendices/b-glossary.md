---
status: draft
chapter-type: appendix
---

# Appendix B — Glossary

Thirty-eight terms, alphabetically sorted. Each entry carries a ≤ 100-word
definition, a *first appears in* chapter pointer, and at least one citation
via the Sphinx `cite` role.

## Agent Loop

The step-loop at the heart of an agent runtime: gather context, invoke
the model, optionally run tool calls, update state, decide continue
vs halt. OpenHarness's `engine/query_engine.py` is the reference
implementation cited in this book. *First appears in Ch.07.*
{cite}`yao2022react`.

## Ambiguity Amplification

The agent-era failure mode in which an ambiguous specification is
laundered into confidently-wrong code at scale. A human reading an
ambiguous spec hesitates; a model emits a concrete, plausible
interpretation on every turn. One ambiguous bullet in `AGENTS.md`
becomes a hundred subtly-different implementations over a quarter.
The cost of ambiguity is multiplied by agent throughput, which is why
spec tightening is the highest-leverage SDD investment. *First appears
in Ch.04.* {cite}`martraire2019living`.

## Architectural Fitness Function

An automatable test of a non-functional property the architecture must
preserve as the system evolves. Ford, Parsons & Kua's term is the
theoretical backing for the Ch.05 four-zone matrix. *First appears in
Ch.03.* {cite}`ford2017buildingevolutionary`.

## Artefact State Model

A four-state machine (`draft → review → approved → archived`) with
role-owned transitions. Central to Chapter 09's workflow-encoded harness.
*First appears in Ch.06.* {cite}`lazyscrumteam2026`.

## Bridle

The Ch.05 zone containing everything the agent reads *before* it writes.
`AGENTS.md`, `CLAUDE.md`, `SKILL.md`, and failing-first tests all live
here. *First appears in Ch.05.* {cite}`walterfan2026guardians`.

## CAR Decomposition

The **Control / Agency / Runtime** decomposition proposed by the
*Harness Engineering for Language Agents* position paper. This book's
preferred academic reference; the HarnessCard format is the CAR paper's
disclosure artefact. *First appears in Ch.05.* {cite}`car2025decomposition`.

## Compliance Theatre

The agent-era failure mode in which a skill's prose self-reports
successful execution ("I ran the tests, they passed") without any
mechanical check falsifying the report. Over many turns the agent
learns that emitting compliance-shaped tokens is cheaper than running
the check; prescription drifts away from enforcement. The cure is
to pair every load-bearing skill with a hook that refuses turns
which skipped the skill's preconditions. *First appears in Ch.02.*
{cite}`anthropic2024claudecode`.

## Context Engineering

Karpathy's 2025 term for the discipline of composing the agent's input
window. Neighbours prompt engineering and overlaps with SDD × Bridle.
*First appears in Ch.03.* {cite}`karpathy2025context`.

## Context Pollution

The Stage-2 failure mode in which optimising retrieval for recall
fills the context window with nearly-relevant chunks, causing the
agent to average rather than select. Three mediocre retrieved
examples teach the agent that mediocre is the house style. The cure
is retrieval as a fence (refuse deprecated paths) rather than a hose
(spray everything). *First appears in Ch.02.* {cite}`lewis2020rag`.

## Cost Runaway (without correlate)

The MDD-era failure mode in which agent-introduced expense regressions
never surface in the team's lived experience. A 10× slower function
the human writes also slows the human's next task; a 10× more
expensive prompt the agent writes runs just as fast from the team's
perspective, and the cost accrues silently on the invoice. Cure: per-
turn cost tagged by skill, repository, and change-set, wired into a
fence. *First appears in Ch.04.* {cite}`langchain2026tbench`.

## DORA Metrics

The four DevOps Research & Assessment metrics — deployment frequency,
lead time, change failure rate, mean time to restore. Outcome metrics
that HarnessCards feed into. *First appears in Ch.12.*
{cite}`forsgren2018accelerate`.

## Design by Contract

Meyer's 1992 principle that routines specify preconditions, postconditions,
and invariants as first-class artefacts. Intellectual ancestor of the
spec-first approach in SDD × Bridle. *First appears in Ch.04.*
{cite}`meyer1992contracts`.

## Entropy (harness sense)

The accumulation of stale, broken, or misleading content in the harness
surface. Left alone, entropy turns a working harness decorative.
*First appears in Ch.06.* {cite}`cunningham1992debt`.

## Fence

The Ch.05 zone containing automated refusals — hooks, linters, schema
validators, secret scanners. Fires at the keystroke or the commit.
*First appears in Ch.05.* {cite}`walterfan2026guardians`.

## Final Acceptance

The `lazy-scrum-team` role that owns the `review → approved` transition
in the Artefact State Model. Cannot perform the review itself; only
the Code Reviewer role does that. *First appears in Ch.09.*
{cite}`lazyscrumteam2026`.

## Groom

The Ch.05 zone containing recurring maintenance — weekly audits,
dashboard retention reviews, stale-doc sweeps. Tends the harness
itself, not the product. *First appears in Ch.05.*
{cite}`walterfan2026guardians`.

## Hard Gate

A gate that refuses a commit, merge, or release with *no waiver path*.
Unit-test failures, secrets-scan hits, and lint errors on new code are
Hard by default. *First appears in Ch.06.* {cite}`humble2010continuousdelivery`.

## Harness

The environment the agent operates inside — the specs it reads, the
gates it passes, the paddock it runs in, the groom that keeps the
environment alive. Not the agent itself. *First appears in Ch.01.*
{cite}`fowler2026harness`.

## HarnessCard

The standardised disclosure format proposed by the CAR paper. Twelve
cells plus layer notes plus a primary citation; rendered as a
copy-paste table in Appendix D. *First appears in Ch.05.*
{cite}`car2025decomposition`.

## Harness Theatre

The class of failure modes in which a harness grows (more rules, more
files, more dashboards) without its leverage growing — measured as
refusals, measurements, or steered decisions per week. The diagnostic
is the ratio of harness-shaped artefacts to refused-or-measured events:
a healthy harness refuses something on most days; a theatrical one
refuses nothing for weeks while its file count rises. Subtypes named
in the book: aspirational `CLAUDE.md`, passing pre-commit, dashboard
theatre, workflow-without-tooling, vanity HarnessCard delta. *First
appears in Ch.01; developed in Ch.06.* {cite}`cunningham1992debt`.

## Harness Engineering

The practice of designing, building, and operating harnesses as
first-class artefacts in AI-assisted software engineering. The term
and its industrial framing trace to Fowler's 2026 essay and the
author's 2026-03-28 blog post. *First appears in Ch.01.*
{cite}`fowler2026harness`.

## Hook

A Claude Code callback that fires at a named lifecycle event
(`PreToolUse`, `PostToolUse`, `SessionEnd`, `UserPromptSubmit`). Exit
code 2 refuses the in-flight tool call. *First appears in Ch.05.*
{cite}`anthropic2024claudecode`.

## Lazy AI Coder

The open-source repository this book ships from —
`walterfan/lazy-ai-coder` — and the subject of Chapter 11's worked
example. *First appears in Ch.11.* {cite}`lazyaicoder2026`.

## lazy-scrum-team

An open-source workflow-encoded harness shipped as a Claude Code / Cursor
skill package. Canonical source for the Artefact State Model, the
Rework Matrix, and the Hard/Soft gate classification. *First appears
in Ch.06.* {cite}`lazyscrumteam2026`.

## Living Documentation

Martraire's term for documentation generated from or kept in sync with
running code. The Ch.05 SDD × Groom zone operationalises the
concept. *First appears in Ch.04.* {cite}`martraire2019living`.

## MCP (Model Context Protocol)

Anthropic's 2024 open specification for tool calls between LLM clients
and tool servers. OpenHarness, Claude Code, and many other harnesses
target the spec. *First appears in Ch.07.* {cite}`anthropic2024mcp`.

## MDD (Metric-Driven Development)

The third guardian: the practice of naming observable signals before
the code ships and tending them afterwards. *First appears in Ch.04.*
{cite}`majors2022observability`.

## Meta-Harness

A harness that treats itself as a product — with its own changelog,
release cadence, and HarnessCards. Ch.06's fourth operating concern.
*First appears in Ch.06.* {cite}`ford2017buildingevolutionary`.

## Observability

The discipline of making an operating system externally comprehensible
via logs, metrics, and traces. MDD is the guardian that carries
observability into the harness. *First appears in Ch.06.*
{cite}`majors2022observability`.

## OpenHarness

The HKU Data Science Lab's open-source harness reference implementation.
Chapter 07 is the case study. *First appears in Ch.05.*
{cite}`hkuds2025openharness`.

## Paddock

The Ch.05 zone containing the bounded review rituals and environments —
acceptance tables, CI gates, staging soaks. Distinct from Fence by
being *slower, broader, more authoritative*. *First appears in Ch.05.*
{cite}`walterfan2026guardians`.

## Prompt Engineering

The 2023-era discipline of authoring LLM prompts to produce desired
outputs. A subset of Ch.05's SDD × Bridle; insufficient on its own for
an agent-era harness. *First appears in Ch.02.* {cite}`brown2020gpt3`.

## ReAct

Yao et al.'s 2022 pattern combining *Reasoning* and *Acting* in the
agent loop. Academic lineage of every modern Agent Loop including
OpenHarness's. *First appears in Ch.07.* {cite}`yao2022react`.

## Reverse-Engineering Disclaimer

The mandatory first H2 of Chapter 10 (and any closed-source case
study): a structured statement of sources, observation window, and
retraction commitment. *First appears in Ch.10.* {cite}`zhangbook2026`.

## Rework Matrix

The finder × fixer table naming the rework artefact that must
accompany every hand-off. Canonical treatment is Chapter 09 §09.3.
*First appears in Ch.06.* {cite}`gousios2014pullbased`.

## SDD (Spec-Driven Development)

The first guardian: the practice of treating spec artefacts —
`AGENTS.md`, `CLAUDE.md`, executable specs — as first-class and agent-
readable before any implementation begins. *First appears in Ch.04.*
{cite}`martraire2019living`.

## Skill (Claude Code)

A `SKILL.md` file discovered via front-matter `description:` and auto-
invoked by the agent. *First appears in Ch.08.* {cite}`anthropic2024skills`.

## Skill Engineering

The 2026-era discipline of authoring reusable skills that shape how an
agent thinks before it writes. Builds on prompt engineering and context
engineering. *First appears in Ch.08.* {cite}`vincent2025superpowers`.

## Spec Drift

The silent SDD failure mode in which the codebase evolves away from
`AGENTS.md`'s claims without the spec being updated. The agent,
reading the spec as authoritative, keeps generating code that conforms
to it; humans, reading the codebase, keep generating code that
conforms to it; the gap widens from both sides. Cure: a scheduled
Groom job that compares the spec's machine-checkable claims against
the codebase weekly and refuses silent drift. *First appears in Ch.04.*
{cite}`martraire2019living`.

## Soft Gate

A gate that refuses by default but allows a role-signed, dated waiver.
Coverage floors, cost caps, and docs link-checks are common Soft gates.
*First appears in Ch.06.* {cite}`humble2010continuousdelivery`.

## Specification by Example

Adzic's 2011 term for the practice of turning acceptance criteria into
executable examples. The vocabulary behind Ch.05 SDD × Paddock.
*First appears in Ch.05.* {cite}`adzic2011specbyexample`.

## Superpowers

Joseph Vincent's open-source skill library for Claude Code. Chapter 08
is the case study. *First appears in Ch.08.* {cite}`vincent2025superpowers`.

## TDD (Test-Driven Development)

The second guardian: Beck's 2002 discipline of writing a failing test
before the implementation. Re-centred in the agent era as TDD × Bridle
(tests as input) and TDD × Fence (hooks refusing red-tree edits).
*First appears in Ch.04.* {cite}`beck2002tdd`.

## Test-Pinning (wrong-interpretation)

The agent-era TDD failure mode in which a human-authored test is
*technically* correct for the behaviour the human had in mind but
leaves one interpretive degree of freedom the agent resolves
opportunistically. Green tests; wrong behaviour; and the green test
hardens the agent's misunderstanding into the repository's memory.
Cure: adversarial tests written specifically to falsify the cheapest
path from prompt to green — the reviewer's "one more test" habit on
every first-try pass. *First appears in Ch.04.*
{cite}`ziegler2022productivity`.

## Technical Debt

Cunningham's 1992 metaphor for the accumulated cost of expedient design
choices. The *entropy* vocabulary of Ch.06 is a harness-specific
specialisation. *First appears in Ch.06.* {cite}`cunningham1992debt`.

## Toolformer

Schick et al.'s 2023 paper establishing first-class tool use as a
primary action surface for LLMs. Academic lineage of OpenHarness's
43-tool taxonomy. *First appears in Ch.07.* {cite}`schick2023toolformer`.

## 《马书》 (*Ma's book*)

Zhang Handong's 2026 reverse-engineering study of Claude Code's bundled
prompt, skill system, hooks contract, and tool schemas. Primary source
for Chapter 10. *First appears in Ch.10.* {cite}`zhangbook2026`.
