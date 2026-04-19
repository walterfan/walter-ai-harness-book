---
status: draft
chapter-type: methodology
---

# The Three Guardians: SDD, TDD, MDD

> *Harness Engineering does not invent a new engineering discipline. It
> recruits three existing ones, reorders them, and front-loads them into
> the space where an agent operates.*

Chapter 03 defined Harness Engineering as the practice of shaping the
structures *around* an AI coding agent so the software it produces is
**verifiable**, **observable**, and **understandable**. Those three
adjectives are not rhetorical flourishes. Each one names a mature
software-engineering discipline with a forty-year pedigree and a canonical
literature. This chapter introduces the three and explains the single
most important choice this book makes — **why they must be applied in the
order SDD → TDD → MDD, not the traditional TDD → MDD → SDD**, once an AI
agent enters the loop.

## Why the causal order flips with an agent in the loop

In traditional software engineering, the writable unit is source code and
the human is the author. Tests come first (TDD) because the test is the
first executable specification and the human will spend hours pushing
code at it until both agree. Documentation (SDD in its classical,
*documentation*-centric framing) is often written last — if at all — and
metrics (MDD) are monitored in production as a safety net. The causal
chain looks like *test → implement → observe*, with the human-authored
code at the centre.

In AI-assisted engineering, the writable unit shifts upstream. What the
human authors is the **prompt, skill file, `AGENTS.md`, and
`CLAUDE.md`** — the agent authors the code. And the agent will *very
confidently hallucinate behaviour* if the specification it reads is
ambiguous, so any test written before the specification is pinned will
encode the hallucination rather than catch it
{cite}`peng2023copilotstudy,ziegler2022productivity`. The causal chain
therefore inverts to *specify → test → observe*:

- **SDD first** — because the specification is now the primary human-authored artefact; it shapes *what the agent tries to build*.
- **TDD second** — because tests now *verify the agent's interpretation* of the spec, rather than serving as the first spec themselves.
- **MDD third** — because metrics close the loop by *confirming the spec + tests keep matching production reality* over time, not as a late-stage safety net.

The rest of this chapter walks the three guardians in that causal order,
gives each a classical definition, an AI-era interpretation, and one
concrete harness example. The chapter ends with a forward pointer to
Chapter 05, where the three guardians become the rows of the book's
**3 × 4 matrix** against the four zones (Bridle / Fence / Paddock /
Groom).

## Guardian I — SDD (Specification-Driven Development)

### Classical definition

Specification-Driven Development is the practice of writing a
machine-checkable description of a system's behaviour *before* the system
is built, and treating that description as the primary artefact that
evolves with the code. Its canonical lineage runs from Meyer's *Design
by Contract* {cite}`meyer1992contracts` (preconditions, postconditions,
invariants as first-class citizens), through Adzic's *Specification by
Example* {cite}`adzic2011specbyexample` (executable examples as the
living contract between product and engineering), to Martraire's *Living
Documentation* {cite}`martraire2019living` (documentation that is
generated from, and validated against, the code it describes). The
unifying claim across forty years is that **ambiguous specifications
produce ambiguous software**, and the cheapest place to fix ambiguity is
the spec.

### AI-era interpretation

When the agent is the author, the specification becomes the *input*
rather than an afterthought. Three artefacts do most of the work:

- **`AGENTS.md` / `CLAUDE.md`** — house rules, file boundaries, invariants the agent must respect before editing {cite}`anthropic2024claudecode`.
- **`SKILL.md` files** — step-by-step procedures the agent is expected to follow for recurring tasks {cite}`vincent2025superpowers`.
- **MCP server manifests** — machine-readable tool contracts that say *what* the agent can do and *what each call costs* {cite}`anthropic2024mcp`.

These are not documentation about the code. They are **input to the
coding process itself** — read by the agent on every turn, not read once
by a new hire and forgotten. That is why SDD moves to the head of the
causal chain: an agent with a stale or ambiguous `AGENTS.md` will author
stale or ambiguous code from turn one, and no amount of downstream
testing can recover the intent the spec failed to pin.

The causal mechanism worth naming is **ambiguity amplification**. A
human reading an ambiguous spec will typically *notice* the ambiguity —
they hesitate, re-read, ask a colleague, or guess conservatively. A
language model does none of these things by default. Given "write an
idiomatic error handler", it will emit *some* concrete handler with
full confidence; the ambiguity in the prompt is laundered into
false precision in the code. One ambiguous bullet in `AGENTS.md`
therefore becomes a hundred confidently-written, subtly-different
implementations over the next quarter. The cost of the ambiguity is
multiplied by the agent's throughput — which is precisely why spec
tightening is the highest-leverage investment the moment an agent
enters the loop.

```{admonition} Pitfall — Spec drift (the silent SDD failure)
:class: warning

`AGENTS.md` said *"all database writes go through `repo.Repository`"*.
Six sprints later, three service files bypass the repository and
write via `sqlx` directly — a pattern introduced during an incident
and never rolled back. The `AGENTS.md` bullet still reads the same.
The agent, reading `AGENTS.md` as authoritative, continues to generate
code that *conforms to the spec* while the codebase *increasingly
does not*. Every new file the agent writes widens the gap because it
is correct-against-the-spec; every new file a human writes widens the
gap because it is correct-against-the-codebase. **Symptom**: reviewers
disagree about what the rule "really" means; new code is sometimes
rejected and sometimes accepted for the same pattern; the agent's
violations correlate with the spec, not with reviewer preference.
**Fix**: a scheduled job (a Groom) compares `AGENTS.md`'s
machine-checkable claims against the codebase weekly; when they
diverge, *one* of them is wrong, and the review must pick which.
```

### Harness example

The SDD guardian ships as an `AGENTS.md` fragment that names (a) the
entrypoint, (b) the file boundary rules, (c) the storage contract signed
by a test, and (d) the invariant enforced by a checker script. The
fragment lives under `_handson/04-three-guardians/AGENTS.md.fragment`
(see §04.Hands-On). A developer who commits this file before a single
prompt is sent has taken the first concrete Harness Engineering step in
their repo.

## Guardian II — TDD (Test-Driven Development)

### Classical definition

Test-Driven Development, as articulated by Beck's *TDD by Example*
{cite}`beck2002tdd`, follows a **red → green → refactor** loop: write a
failing test, write the smallest change that makes it pass, then refactor
under the safety of the now-passing test. Tests are both specification
(executable, so unambiguous) and regression net (durable, so drift-catching).
Four decades of industry practice have shown that teams that hold the
loop tight ship fewer defects per change and tolerate refactors at
higher velocity {cite}`forsgren2018accelerate`.

### AI-era interpretation

With an agent in the loop, the **red-first** half of the loop becomes
more important and the **refactor** half becomes more automatable. More
important because the human-authored test is now the *only* thing that
verifies the agent understood the spec — skip it and the agent's
confidently-hallucinated code passes into the repo unchallenged
{cite}`peng2023copilotstudy`. More automatable because once the test is
red, the agent is very good at producing *some* code that turns it
green; the human's job is reduced to deciding whether the resulting code
*also* deserves to pass a more adversarial test the human did not yet
write {cite}`ziegler2022productivity`.

Operationally this reshapes the human workflow:

- The human writes the failing test and a one-paragraph spec delta.
- The agent turns the test green.
- The human reviews the diff for *silent* invariants the test did not cover, adds one more failing test, and repeats.

This is still TDD, but the human now spends most of their TDD time on
the *test* side of the loop and almost none on the *implement* side. The
harness must make that split cheap: hooks that block commits on red
tests {cite}`humble2010continuousdelivery`, quarantine buckets for
flaky tests, and a fast lane that reruns only the tests affected by a
diff.

The distinctive AI-era failure mechanism is **test-pinning of the
wrong interpretation**. The human writes a test that is *technically*
correct for the behaviour they had in mind, but leaves one interpretive
degree of freedom the agent resolves opportunistically. The test goes
green. The code encodes the agent's resolution, not the human's
intent. Two months later, an incident reveals the divergence — and the
test, now load-bearing, is cited as evidence that "the behaviour was
specified". It was not; only one of many behaviours consistent with the
test was specified. Every such test hardens the agent's original
misunderstanding into the repository's memory. The cure is not "more
tests" but *adversarial tests*: tests written specifically to falsify
the cheapest path from prompt to green.

```{admonition} Pitfall — "It passed the test on the first try"
:class: warning

An agent turns a failing test green on its first turn. The reviewer,
relieved, approves the PR. This is the single most common place TDD
fails in the agent era. **Why**: a first-try pass usually means the
test was easier to satisfy than the spec — either the test under-
specified, or the agent happened to land on a corner of the
solution space the test happened to cover. A human, pushed by the
red-green-refactor rhythm, would iterate three or four times and
leave shrapnel the reviewer could learn from; the agent leaves one
clean diff that passes, which *feels* like quality. **Symptom**:
first-try pass rate rises; silent-defect rate rises with it; the
team's test-addition rate per feature falls because "the first test
already covers it". **Fix**: on every first-try pass, the reviewer
writes *one more test* — specifically, a test that attacks the
cheapest shortcut the agent could have taken. If that test also
passes, the confidence was earned; if it fails, you just averted a
silent defect.
```

### Harness example

The TDD guardian ships as a pytest skeleton at
`_handson/04-three-guardians/test_skeleton.py`. It is **deliberately
failing** when first committed — two tests that pin a behaviour the
agent must then build (`add` appends exactly one item; `add` rejects an
empty title). A `pre-commit` hook runs `pytest -q -m "not slow"` so the
red test is a blocker from the very first prompt
{cite}`humble2010continuousdelivery`, not an aspiration checked only in
CI. The sibling `pre-commit-config.fragment.yaml` from Chapter 03's
Hands-On is the matching fence, demonstrating how Ch.03's minimal triad
instantiates the TDD guardian that §04 now names.

## Guardian III — MDD (Metric-Driven Development)

### Classical definition

Metric-Driven Development is the discipline of treating production
signals — not unit-test pass rates alone — as the authoritative feedback
loop on whether a system still does what its spec and tests claimed.
Its intellectual lineage includes Cunningham's technical-debt metaphor
{cite}`cunningham1992debt` (invisible cost accrues until a metric makes
it visible), Majors, Fong-Jones & Miranda's *Observability Engineering*
{cite}`majors2022observability` (high-cardinality events as the
primitive signal), and Lehman's laws of software evolution
{cite}`lehman1980laws` (a useful system must be continually adapted or
its fitness declines — a claim only measurable with metrics). MDD
generalises observability one step further by insisting the metrics are
chosen *before* production issues force them, so the first week of
operation begins with a monitoring contract rather than a blank
dashboard.

### AI-era interpretation

With an agent authoring code, a mature harness monitors at least three
kinds of signals: (a) classical production SLIs (error rate, p99
latency, throughput); (b) harness-internal signals (agent
turns-to-green, cost per turn, prompt cache hit rate)
{cite}`langchain2026tbench`; (c) spec-observance signals (broken-link
count on the docs site, stale `verified:` dates on hands-on artefacts,
schema drift between `AGENTS.md` and the MCP manifest)
{cite}`martraire2019living`. The agent-specific failures the third
family catches — *spec drift* between `AGENTS.md` and the codebase,
and *cost runaway* across agent turns — are treated in depth below
and, for spec drift specifically, in the SDD section's pitfall
callout above.

The failure mechanism unique to the agent era is **cost runaway with
no correlate**. A human engineer who introduces a 10× slower function
is noticed because the human's next task also runs 10× slower. An
agent that introduces a 10× more expensive prompt is not noticed: its
*next* prompt runs just as fast from the team's perspective, and the
cost accrues silently on the invoice. Without a per-turn cost signal
wired into a fence, the first evidence of the regression is either
a rate limit, a bill, or a quarterly review — all of which arrive too
late to correlate to the commit that caused them. MDD's role is to
make that correlation cheap: cost-per-turn tagged by skill, by
repository, and by change-set, so that the incremental cost of any
given harness change is visible the day after it lands, not the
quarter after.

```{admonition} Pitfall — Dashboard theatre
:class: warning

A team builds a twelve-panel Grafana board tracking agent cost,
turns-to-green, cache hit rate, and nine other signals. It is
beautiful. Six weeks later, the question *"which signal moved this
week, and what did we do about it?"* returns blank stares. **Why**:
the dashboard has no owner, no alert thresholds, and no scheduled
review; the signals exist but they do not *steer*. A metric that
nobody is accountable to is diagnostic at best and decorative at
worst. **Symptom**: the dashboard is shown proudly in demos but
never referenced in PRs; incidents are explained by gut feel
despite the data being right there. **Fix**: demote ten of the
twelve panels to a second tab, promote *one* to a north-star with a
named owner, a threshold that fires a page, and a Monday morning
agenda slot. Chapter 05's MDD × Bridle treats the one-north-star
discipline in detail.
```

### Harness example

The MDD guardian ships as a `metrics.yaml` at
`_handson/04-three-guardians/metrics.yaml`. It is fifteen lines of YAML
that names four signals (pytest pass rate, broken-link count, mean
review time, agent turns-to-green), sets a target for each, and — the
cultural move that makes it MDD rather than observability — commits the
team to a **weekly review cadence**. A harness without a review cadence
collects dashboards; a harness with one closes the feedback loop the
two earlier guardians opened.

## Why each guardian fails alone

The matrix interpretation in Chapter 05 depends on the argument that no
single guardian is sufficient. The failure modes are distinct and
self-reinforcing:

- **SDD alone** produces precise specs that no one verifies — the agent follows a well-written `AGENTS.md` into a silently broken implementation because no test ever tried to break it.
- **TDD alone** produces green tests that pin the agent's first
  misunderstanding of the spec — "the code does what the test says"
  becomes true while "the code does what the user needed" quietly
  diverges {cite}`ziegler2022productivity`.
- **MDD alone** produces beautiful dashboards that *diagnose* drift
  after it has happened but cannot *prevent* it, because neither the
  spec nor the tests that would catch drift earlier were ever written.

The three guardians are load-bearing only when they are all three
present, and present in that causal order. Chapter 05 renders that claim
as a 3 × 4 methodology matrix: three guardian rows crossed with four
operational zones (Bridle / Fence / Paddock / Groom), producing twelve
engineering cells that together constitute the book's analytical spine.

## Research Foundations

The three guardians are selected not because they cohere aesthetically
but because each rests on a distinct, citable lineage and each solves a
failure mode the other two cannot.

- **SDD lineage.** Meyer's *Design by Contract* {cite}`meyer1992contracts` established machine-checkable pre/postconditions as first-class engineering artefacts; Adzic's *Specification by Example* {cite}`adzic2011specbyexample` extended that stance to executable business rules; Martraire's *Living Documentation* {cite}`martraire2019living` is the direct ancestor of `AGENTS.md` / `CLAUDE.md` as a continuously validated spec surface.
- **TDD lineage.** Beck's *TDD by Example* {cite}`beck2002tdd` is the canonical text; Humble & Farley's *Continuous Delivery* {cite}`humble2010continuousdelivery` shows how the red-green-refactor loop scales to organisational cadence; the copilot productivity studies {cite}`peng2023copilotstudy,ziegler2022productivity` are the empirical evidence that *untested* agent output silently degrades code quality, which is the AI-era case for keeping the red-first discipline.
- **MDD lineage.** Cunningham's debt metaphor {cite}`cunningham1992debt` motivated making invisible costs visible; Majors, Fong-Jones & Miranda's *Observability Engineering* {cite}`majors2022observability` reframed production signals as primary design concerns; Lehman's evolution laws {cite}`lehman1980laws` argue that a useful system must be continuously re-fit, which is only operationalisable with metrics.
- **Harness-side synthesis.** The 2026-01-30 blog post introducing the Three Guardians {cite}`walterfan2026guardians` is this book's own prior synthesis; readers who want the short version should read it alongside the Thoughtworks radar entry {cite}`thoughtworks2026harness` and the LangChain anatomy post {cite}`langchain2026tbench`.

## Hands-On

Three artefacts ship under
`book/source/_handson/04-three-guardians/`, one per guardian, in
the causal order this chapter argues for:

- **SDD** — `AGENTS.md.fragment`: a machine-checkable spec block that
  names entrypoint, file boundaries, storage contract, and agent rules.
  Fourteen lines; copyable into any repo's `AGENTS.md`.
- **TDD** — `test_skeleton.py`: a deliberately failing pytest module
  that pins `todo add` behaviour *before* a prompt is sent. Run with
  `pytest -q tests/test_skeleton.py`; the test is expected to be red on
  commit and green after the agent's first successful turn.
- **MDD** — `metrics.yaml`: a fifteen-line signal contract naming four
  metrics (pytest pass rate, broken-link count, mean review time, agent
  turns-to-green) and a weekly review cadence.

The accompanying `README.md` names the reading order and the intent of
each file. Committing all three files into any active repository —
alongside the Chapter 03 triad — produces the smallest complete
three-guardian harness this book will ask the reader to operate. The
next chapter turns that harness into a matrix.
