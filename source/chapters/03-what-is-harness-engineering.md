---
status: draft
chapter-type: narrative
---

# What is Harness Engineering?

> *If Chapter 01 is the motivation and Chapter 05 is the method, this chapter
> is the dictionary entry a skeptic should be able to read in fifteen minutes.*

Most readers will not arrive at this book linearly. Some will land here from
a search engine, a conference talk, or a colleague's Slack link. They need
one thing first: a **definition** — concise enough to cite, defended enough
to trust, and bordered enough to distinguish from the five disciplines the
field most often collapses into. This chapter delivers that definition in
five sections, followed by the Research Foundations and Hands-On tracks the
rest of the book enforces on every chapter.

## §03.1 A One-Sentence Definition

> **Harness Engineering is the discipline of deliberately designing, operating,
> and evolving the structures that surround an AI coding agent so that the
> software it produces is verifiable, observable, and understandable.**

Unpack that sentence once. *Deliberately designing* rejects the default
position — that whatever happens to be in the prompt window, the IDE, and
the CI pipeline constitutes an adequate environment for an AI agent.
*Operating and evolving* says a harness is not a one-time setup; entropy
creeps in across runs, and a harness that is not tended drifts into a
collection of stale instructions. *Verifiable, observable, and understandable*
names the three guardians Chapter 04 unpacks — the properties the harness
exists to guarantee. The agent is not the subject of the sentence; the
*structures around it* are. That inversion is the whole of the field.

## §03.2 Operational Boundary

A harness is a concrete, enumerable set of engineering artefacts. The field
becomes tractable only when we say exactly what is in the set and what is
not.

### A harness IS

- **Prompts, skills, and agent-facing specs** — `CLAUDE.md`, `AGENTS.md`,
  `SKILL.md`, MCP server manifests, and system prompts treated as
  versioned, reviewable code {cite}`anthropic2024claudecode,anthropic2024mcp`.
- **Approval gates and fences** — pre-commit hooks, lint rules, PR
  reviewers, required CI checks, and any automation that refuses a bad
  artefact regardless of who (or what) authored it {cite}`humble2010continuousdelivery`.
- **A sandbox** — container, VM, scoped filesystem, or ephemeral worktree
  inside which the agent operates without touching production
  {cite}`car2025decomposition`.
- **Documentation addressed to the agent** — runbooks, architectural
  decision records, and skill files the agent can read on its own to
  reduce ambient hallucination {cite}`martraire2019living`.
- **Metrics and a feedback surface** — observable signals (test pass rate,
  cost per turn, lint violation count, time-to-green) written down somewhere
  the team reviews weekly {cite}`majors2022observability`.

### A harness IS NOT

- **A runtime inference stack.** How the model's tokens are scheduled on
  which GPUs is infrastructure, not harness — that is the domain of *AI
  Engineering* in Huyen's sense {cite}`huyen2025aieng`.
- **An ML evaluation benchmark.** HELM, MMLU, Terminal-Bench and their
  relatives measure an agent; they are *inputs* to harness design, not the
  harness itself {cite}`langchain2026tbench`.
- **An IDE plugin surface.** Cursor, Copilot, Windsurf and their siblings
  are *clients* that consume a harness; the harness lives in the repository
  and outlives any specific editor {cite}`peng2023copilotstudy`.
- **An agent framework SDK.** LangChain, AutoGen, CrewAI, and LangGraph
  expose building blocks for multi-step agents; the harness is what a team
  writes *around* whatever framework it chooses {cite}`langchain2026tbench`.
- **A deployment pipeline.** DevOps owns the path from merged commit to
  production; harness ownership ends at the merged commit
  {cite}`forsgren2018accelerate`.

The membership test is simple: if the artefact shapes what the agent
*tries to produce* before a commit lands, it is harness; if it shapes what
happens *to* a commit afterwards, it is DevOps; if it shapes how the model
itself is served, it is AI Engineering.

Three edge cases recur often enough to be worth walking explicitly; each
is a case where the membership test is easy to misapply.

- **A flaky pre-commit hook**. Is it harness? Yes — it fires before
  commit — but it is a *degraded* harness artefact because it has lost
  the property the harness exists to supply. The fence that refuses
  intermittently teaches the agent (and the humans) that the fence is
  optional. A flaky fence is worse than no fence at all, because it
  combines the cost of the fence with none of its leverage. Fix the
  flakiness or delete the hook; do not leave it half-alive.
- **A dashboard that no one reads**. Is it harness? No — it fails the
  *operated-and-evolved* half of the definition. Instrumentation without
  a review cadence is observability infrastructure, not MDD. Chapter 06's
  Groom column exists specifically to prevent this demotion.
- **A long `README.md` pinned to the top of the repo**. Is it harness?
  Only if the agent reads it on every turn. A `README.md` addressed
  primarily to human newcomers is documentation; a `README.md` whose
  first fifty lines the agent loads into its context window on session
  start (verify by inspecting the agent's context dump) is harness. The
  file's filename does not determine the class; the consumer does.

Apply the membership test to your own repo for five minutes. Most teams
discover that *some* of their harness is accidentally misclassified as
documentation, and *some* of their documentation is accidentally treated
as harness — with neither pool tended by the right discipline.

## §03.3 Adjacent Practices Compared

The field has four close neighbours. Confusing them is the single most
common first-encounter error, which the comparison table below pre-empts.

```{list-table}
:header-rows: 1
:widths: 18 22 22 22 16

* - Discipline
  - Scope
  - Primary artefact
  - Primary failure mode
  - Overlap with Harness Engineering
* - **DevOps** {cite}`humble2010continuousdelivery,forsgren2018accelerate`
  - From merged commit to production running
  - Pipeline definitions, IaC, deployment manifests
  - Fragile releases, long mean time to recovery
  - Shares approval-gate mindset; pre-commit hooks and required CI checks
    are harness artefacts *reused from* the DevOps toolkit
* - **MLOps** {cite}`sculley2015mltechdebt,huyen2025aieng`
  - From dataset to served model
  - Training pipelines, feature stores, model registries
  - Hidden technical debt in feedback loops and data drift
  - Shares versioning discipline; model-evaluation harnesses feed *signals*
    into an agent harness but sit upstream of it
* - **AI / Agent Engineering** {cite}`huyen2025aieng,langchain2026tbench,anthropic2024agents`
  - Composing foundation models into working applications and multi-step
    agents
  - Prompt templates, chains, tool schemas, retrieval pipelines
  - Prompt fragility, tool-call hallucination, unbounded agent loops
  - Harness Engineering is the *environment-side* counterpart; agent
    engineering builds the agent, harness engineering builds what the
    agent operates inside
* - **Platform Engineering** {cite}`cncf2024platformeng`
  - Self-service developer platforms (IDPs) that abstract infra for
    product teams
  - Golden paths, platform APIs, internal dev portals
  - Cognitive load on platform consumers; drift between platform and
    reality
  - Shares the "paved road" ideology; a mature Harness Engineering team
    eventually exposes its harness as an internal platform product
```

Reading the table row by row clarifies the field's position: Harness
Engineering sits **between** AI/Agent Engineering (which is about the agent)
and DevOps (which is about deployment), and borrows artefact patterns from
both while owning neither.

## §03.4 A Minimal Example

A harness does not require a platform team or a budget. It requires three
files, each under ten lines. The triad below is the smallest complete
harness this book will ask the reader to ship — one specification for the
agent to read, one fence the agent (and humans) cannot bypass, and one
observability receipt the team publishes.

### Fragment 1 — The specification the agent reads (`CLAUDE.md`)

```{literalinclude} ../_handson/03-what-is-harness-engineering/claude-md.fragment.md
:language: markdown
```

Three choices matter here. The rules are *few* (four bullets), because
agents respect short, enumerable house rules more reliably than long
essays {cite}`anthropic2024claudecode`. Each rule is *machine-checkable*
(it names a file, a command, or a config), so the spec aligns with the
gate. And it *points at its sibling artefacts* (pre-commit config,
HarnessCard), so the agent reading it knows where to look next.

### Fragment 2 — The fence humans and agents alike cannot bypass (`.pre-commit-config.yaml`)

```{literalinclude} ../_handson/03-what-is-harness-engineering/pre-commit-config.fragment.yaml
:language: yaml
```

Pre-commit is the smallest possible TDD-style gate: it refuses bad code
regardless of authorship {cite}`beck2002tdd`. The ruff hook enforces
style (which the agent would otherwise hallucinate in five competing
flavours) and a tiny `pytest -m "not slow"` hook ensures no commit lands
without a fast-lane green. This is the *verifiability guardian* of
Chapter 04 compressed into ten lines.

### Fragment 3 — The observability receipt (`harnesscard.yaml`)

```{literalinclude} ../_handson/03-what-is-harness-engineering/harnesscard.fragment.yaml
:language: yaml
```

The HarnessCard is a standardised disclosure format proposed by the CAR
decomposition paper {cite}`car2025decomposition`. It names — in one
commit-reviewable file — which spec the harness uses, which gate enforces
it, and which signals the team watches. It is the smallest possible MDD
surface (Chapter 04's third guardian): three lines of signals is enough to
start a weekly review habit.

Taken together, these thirty lines satisfy the one-sentence definition
above. They are *deliberately designed* (not accidentally accumulated),
*operated and evolved* (the HarnessCard dates itself), and they
explicitly name the three guardians. Any team with an agent in the loop
can ship this triad in an afternoon and have a harness — primitive, but
real.

```{admonition} Pitfall — The three files that look like a harness but are not
:class: warning

It is deceptively easy to produce a thirty-line triad that *looks* like
the one above but fails the membership test. Three common degenerate
forms:

1. **The aspirational `CLAUDE.md`.** Rules written as wishes — "write
   idiomatic Go", "prefer clear names" — that no hook can mechanically
   falsify. The agent signals compliance and hallucinates adherence.
   **Test**: every rule must name a file, a command, or a config. If
   none do, it is a wish list.
2. **The passing pre-commit.** A hook that runs `pytest` against a
   suite of zero tests, or `ruff` against files in an excluded
   directory. It always passes; the team loses the fence without ever
   noticing. **Test**: on first install, the hook must *refuse* some
   artefact the repository currently contains (even if you then fix
   that artefact). A fence that has never said *no* is not a fence.
3. **The undated HarnessCard.** A yaml file committed once and never
   touched. The signals remain listed; none of them have moved in a
   quarter. **Test**: the HarnessCard must carry a `last_reviewed:`
   date no more than thirty days old, and the review must produce a
   delta note. A static HarnessCard is ornament.

The distinction between a working harness and harness theatre is not
file count — it is whether *on any given Tuesday* each of the three
files can be shown to have refused, measured, or steered something.
If the answer is no for a whole quarter, the triad has decayed into
decoration even if its contents are unchanged.
```

## §03.5 When Not to Use Harness Engineering

Harness Engineering, like any discipline, has a cost: three files to
maintain, a weekly review cadence, a HarnessCard to update. Three
situations do not pay that cost back:

- **One-off throwaway scripts.** A 40-line script that parses a CSV and
  exits is not a project; it has no second commit. The harness investment
  does not amortise over a second commit that never arrives.
- **Solo prototypes with zero AI usage.** If a developer neither uses nor
  plans to use an AI coding agent, Chapters 04–06 still apply as
  traditional SE hygiene, but the *harness* label is unhelpful — the
  "agent" whose environment is being shaped does not exist.
- **Legacy code no AI agent will ever touch.** A 2008 COBOL system under
  change freeze gains nothing from a `CLAUDE.md`; effort is better spent
  on Feathers' legacy-code playbook {cite}`feathers2004legacy` until the
  code base re-enters active development with AI in the loop.

Anywhere else — from a solo side project with Copilot autocomplete to a
fifty-engineer platform team running autonomous agents — the cost of the
thirty-line triad in §03.4 is lower than the cost of its absence.

## Research Foundations

The definition of Harness Engineering in §03.1 is deliberately constructed
to sit between established disciplines rather than to invent a new one; its
credibility therefore rests on the boundary citations rather than on a
single primary source.

- **DevOps baseline:** Humble & Farley's *Continuous Delivery*
  {cite}`humble2010continuousdelivery` and Forsgren, Humble & Kim's
  *Accelerate* {cite}`forsgren2018accelerate` establish that an approval-gate
  discipline can be culturally normalised across an entire industry; the
  harness borrows their gate-centric stance wholesale while redirecting it
  upstream of the commit rather than downstream.
- **MLOps baseline:** Sculley et al.'s *Hidden Technical Debt in Machine
  Learning Systems* {cite}`sculley2015mltechdebt` is the canonical warning
  about invisible glue code in ML pipelines; Huyen's *AI Engineering*
  {cite}`huyen2025aieng` updates that critique for the foundation-model era
  and is the reference behind the "AI is not harness" row in §03.3.
- **Agent Engineering boundary:** Anthropic's *Building Effective Agents*
  {cite}`anthropic2024agents` and LangChain's *Terminal-Bench 2.0*
  {cite}`langchain2026tbench` are the two most-cited 2024–2026 sources on
  what an agent is and how to evaluate one; both frame the agent as the
  subject and the environment as an implementation detail, which is the
  precise framing this book inverts.
- **Platform Engineering boundary:** the CNCF Platforms Working Group's
  *Platform Engineering Maturity Model* {cite}`cncf2024platformeng`
  anchors the "paved road" vocabulary §03.3 borrows in its Platform
  Engineering row.
- **Harness-Engineering primary sources:** the CAR decomposition and
  HarnessCard from the position paper {cite}`car2025decomposition`,
  Fowler's bliki entry that first named the practice
  {cite}`fowler2026harness`, OpenAI's vendor-side articulation
  {cite}`openai2026harness`, and Thoughtworks' Technology Radar trial-ring
  entry {cite}`thoughtworks2026harness` together constitute the four
  primary-source references this book cross-cites when the label "Harness
  Engineering" itself is at stake.

## Hands-On

The minimal example in §03.4 ships as three fragments under
`book/source/_handson/03-what-is-harness-engineering/`:

- `claude-md.fragment.md` — the ten-line specification the agent reads.
- `pre-commit-config.fragment.yaml` — the ten-line fence that refuses bad
  commits.
- `harnesscard.fragment.yaml` — the ten-line observability receipt the
  team publishes.

The accompanying `README.md` names the reading order and the intent of
each file. A reader who only wants to *start* practising Harness
Engineering today can copy these three fragments into any repo, adjust
the file names, and begin the weekly HarnessCard review loop Chapter 06
formalises.
