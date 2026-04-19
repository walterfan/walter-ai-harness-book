---
status: draft
chapter-type: methodology
---

# Harness Anatomy: Three Guardians × Four Zones

> *A framework that cannot be drawn as a table is a slogan, not an
> analytical tool.*

Chapter 04 argued that any working harness must carry three load-bearing
guardians — SDD, TDD, MDD — in that causal order. This chapter places
those three guardians against four operational **zones** — *Bridle*,
*Fence*, *Paddock*, *Groom* — to produce a 3-row × 4-column matrix. The
twelve cells are the analytical spine every later chapter refers back to.

Before the matrix itself, §05.Provenance says plainly where the four-zone
vocabulary comes from and why this book still uses it. Readers who want
the definitions first may skip to §05.Overview.

## Provenance

The four-zone metaphor — **Bridle** (what steers the agent before it
writes code), **Fence** (what refuses bad work regardless of author),
**Paddock** (the bounded space inside which the agent may roam), **Groom**
(the recurring maintenance that keeps the harness itself alive) — was
proposed by the author of this book in the 2026-03-28 blog post *Harness
Engineering: 给 AI 套上缰绳* {cite}`walterfan2026guardians`. It is a
**practitioner framework**, not a peer-reviewed taxonomy. Readers with a
research background should treat it as a pedagogical scaffold, not as a
settled decomposition of the field.

Three adjacent frameworks cover roughly the same territory and deserve
explicit triangulation:

- **CAR decomposition with HarnessCard reporting format** — proposed by
  the *Harness Engineering for Language Agents* position paper
  {cite}`car2025decomposition`, which splits a harness into **Control**
  (who decides what runs), **Agency** (what the agent may do on its
  own), and **Runtime** (the substrate the agent's code executes on),
  and pairs the decomposition with a standardised HarnessCard disclosure
  format. CAR is the book's preferred *academic* reference and is what
  Chapter 07–11's case-study HarnessCards ultimately serialise against.
- **Thoughtworks' three-part framing**
  {cite}`thoughtworks2026harness` treats harness work as *context
  engineering* + *architectural constraints* + *garbage collection*.
  This framing is closer in spirit to DevOps and is where the "garbage
  collection" intuition behind §05.*Groom* originated.
- **LangChain's five-part agent anatomy**
  {cite}`langchain2026tbench` lists *prompts / tools / middleware /
  orchestration / runtime* as the building blocks exposed in the
  Terminal-Bench 2.0 post. LangChain's framing is product-centric
  (intended for framework users) where this book's four zones are
  workflow-centric (intended for team leads deciding what to invest in
  next week).

Why keep Bridle / Fence / Paddock / Groom given these three adjacent
frameworks? Two reasons. First, the four zones **map 1:1 onto a workflow
every engineering team already runs** — we already have code reviewers,
CI gates, staging environments, and weekly chore lists; the four zones
rename those into a vocabulary that treats them as first-class harness
artefacts rather than DevOps afterthoughts. Second, pairing the zones
with SDD / TDD / MDD produces a **3 × 4 Cartesian product** with twelve
small, concrete cells — each cell small enough that a reader can ship
one artefact for it in an afternoon. A three-part decomposition (CAR) is
great for writing a position paper; a twelve-cell matrix is what you
want when Monday morning asks *"what do we invest in next?"*.

A reader who prefers CAR over Bridle / Fence / Paddock / Groom can
translate: Bridle roughly maps to CAR-Control; Fence and Paddock together
roughly map to CAR-Agency; Groom covers cross-cutting concerns CAR
handles as Runtime evolution. This book uses the four-zone naming
throughout but never claims primacy over CAR; the translation is
first-class, not a retrofit.

## §05.Overview — The 3 × 4 Matrix

```{list-table}
:header-rows: 1
:widths: 10 22 22 22 22

* -
  - **Bridle** — steers before writing
  - **Fence** — refuses bad work
  - **Paddock** — bounds where the agent may roam
  - **Groom** — tends the harness itself
* - **SDD**
  - [SDD × Bridle](sdd-x-bridle)
  - [SDD × Fence](sdd-x-fence)
  - [SDD × Paddock](sdd-x-paddock)
  - [SDD × Groom](sdd-x-groom)
* - **TDD**
  - [TDD × Bridle](tdd-x-bridle)
  - [TDD × Fence](tdd-x-fence)
  - [TDD × Paddock](tdd-x-paddock)
  - [TDD × Groom](tdd-x-groom)
* - **MDD**
  - [MDD × Bridle](mdd-x-bridle)
  - [MDD × Fence](mdd-x-fence)
  - [MDD × Paddock](mdd-x-paddock)
  - [MDD × Groom](mdd-x-groom)
```

The twelve H3 subsections below — one per cell, in the fixed order **SDD
row, then TDD row, then MDD row** — are the chapter's working body.
Every case-study chapter (07–11) scores a real harness against the same
twelve cells.

A word on how to *read* the matrix. The twelve cells are analytically
independent (a strong TDD × Fence does not imply a strong SDD × Groom)
but *operationally coupled* — strong cells cover for weak ones, and
weak cells quietly sabotage strong ones. Three couplings worth
noticing before reading any row:

- **Bridle weakness amplifies through Fence strength.** A vague
  `AGENTS.md` (weak SDD × Bridle) paired with a strict pre-commit
  hook (strong TDD × Fence) produces code that is *clean* and *wrong*:
  the lint passes, the tests pass, and the architecture violates the
  intent the spec never pinned down. Strong fences make weak bridles
  invisible — until the architectural debt surfaces in an incident.
- **Paddock strength hides Bridle weakness.** A thorough PR review ritual
  (strong SDD × Paddock) can carry a team for a year with a mediocre
  `AGENTS.md`, because the human reviewer compensates on every merge.
  The weakness appears the moment the team scales reviewer capacity
  less than it scales agent output — which is *always*.
- **Groom is where the other three decay.** Every cell in the Bridle,
  Fence, and Paddock columns depreciates by default; the Groom column
  is what pays the depreciation down. A harness with zeros in the
  Groom column will drift back to zeros in every other column within
  two quarters, regardless of how much was invested up front.

Read each cell below with this coupling in mind: a high score is not
durable without its sibling cells, and no single cell is load-bearing
on its own.

(sdd-x-bridle)=
### SDD × Bridle — Agent-facing specs that steer

**Definition.** A bridle in this cell is any file the agent *reads before
it writes anything* and whose primary purpose is to shape what the agent
tries to build. `AGENTS.md`, `CLAUDE.md`, and top-level `SKILL.md` files
live here {cite}`anthropic2024claudecode`. A bridle that is unread or
stale steers nothing; the guardian responsibility therefore extends to
keeping the file fresh, not merely present.

```{literalinclude} ../_handson/05-harness-anatomy/sdd-x-bridle/AGENTS.md.sample
:language: markdown
```

(sdd-x-fence)=
### SDD × Fence — Spec validity enforced at the gate

**Definition.** A fence in this cell enforces that every spec-shaped
artefact is *well-formed before it becomes authoritative*. Examples:
JSON-Schema validation of prompt templates at commit time, MCP-manifest
schema checks, CI steps that refuse documentation builds with unresolved
`{ref}` links {cite}`martraire2019living`. Without this fence, spec rot
accumulates silently and SDD × Bridle becomes a lie.

```{literalinclude} ../_handson/05-harness-anatomy/sdd-x-fence/prompt-schema.json
:language: json
```

(sdd-x-paddock)=
### SDD × Paddock — Acceptance that matches the spec

**Definition.** A paddock in this cell is a bounded *review ritual* that
confirms delivered work matches the spec, role by role, line by line.
Executable specifications {cite}`adzic2011specbyexample` are the
canonical form; the lazy-scrum-team *Verification Table* pattern
{cite}`lazyscrumteam2026` is a concrete instance the book adopts
throughout.

```{literalinclude} ../_handson/05-harness-anatomy/sdd-x-paddock/acceptance-gate.md
:language: markdown
```

(sdd-x-groom)=
### SDD × Groom — Keeping the spec surface alive

**Definition.** A groom action in this cell is a *recurring maintenance
job* that refreshes the spec surface so the agent's input never silently
rots. Broken-link sweeps, stale `verified:` header rewrites, and weekly
regeneration of auto-generated `AGENTS.md` tables of contents are
typical {cite}`ford2017buildingevolutionary`. Without grooming, SDD
entropy accumulates faster than authors can keep up.

```{literalinclude} ../_handson/05-harness-anatomy/sdd-x-groom/update-docs.sh
:language: bash
```

```{admonition} Pitfall — SDD row failure modes
:class: warning

The SDD row's distinctive failure is not *absence* of specs but
*unfalsifiable* ones. Two cell-specific variants worth naming
(Ch.03's *aspirational `CLAUDE.md`* edge case covers the third):

- **The MCP manifest that outlives its handler.** The schema
  advertises a tool the server no longer implements; the agent
  invokes it confidently and receives a puzzling error. SDD × Fence
  exists to catch exactly this, but only if the fence is wired to
  *both* sides of the schema-to-handler contract.
- **The unversioned spec.** `AGENTS.md` with no changelog, no
  `verified:` date, no sign of having evolved. Reviewers cannot tell
  whether its claims are current or legacy; agent and human both
  read it as authoritative. SDD × Groom is the answer — but only if
  the Groom job fails loudly when the spec has not been touched in
  N weeks.

Row-level test: can you name, for each SDD cell, one artefact in
your repo today and one check that would fire *this week* if it
broke? If any cell's answer is "we trust people to keep it
current", that cell is at zero regardless of the file contents.
```

(tdd-x-bridle)=
### TDD × Bridle — Failing-first tests as input to the agent

**Definition.** A bridle in this cell is a *deliberately red test suite*
committed before the agent is invited in. The agent reads the failing
tests as part of its context and understands *what it must make green*
before writing production code {cite}`beck2002tdd`. The key property is
*red on commit*, not "a test exists somewhere".

```{literalinclude} ../_handson/05-harness-anatomy/tdd-x-bridle/test_loop.py
:language: python
```

(tdd-x-fence)=
### TDD × Fence — Hooks that refuse red-tree commits

**Definition.** A fence in this cell blocks any edit or commit while the
test tree is red. Pre-commit hooks, Claude-Code `PreToolUse` hooks, and
required CI checks all belong here {cite}`humble2010continuousdelivery`.
The distinction from TDD × Paddock is *immediacy* — a TDD fence fires at
the keystroke, a TDD paddock fires at the PR.

```{literalinclude} ../_handson/05-harness-anatomy/tdd-x-fence/hooks.json
:language: json
```

(tdd-x-paddock)=
### TDD × Paddock — CI gate and environment parity

**Definition.** A paddock in this cell is a *required, branch-protected
test run* that happens in an environment faithful to production. It is
the integration-level twin of TDD × Fence: broader in scope, slower in
turnaround, authoritative in verdict {cite}`forsgren2018accelerate`.

```{literalinclude} ../_handson/05-harness-anatomy/tdd-x-paddock/ci-gate.yml
:language: yaml
```

(tdd-x-groom)=
### TDD × Groom — Flake maintenance and test-surface evolution

**Definition.** A groom action in this cell is a *recurring policy* for
handling tests that stop being load-bearing — flakes, long-extinct
regressions, tests that drift out of step with the spec they verified.
Without grooming, the test corpus accumulates dead weight and eventually
*loses* the team's trust {cite}`cunningham1992debt`.

```{literalinclude} ../_handson/05-harness-anatomy/tdd-x-groom/flaky-test-quarantine.md
:language: markdown
```

```{admonition} Pitfall — TDD row failure modes
:class: warning

The TDD row fails in ways the SDD row does not, because tests have
an unusual property: a failing test is *cheap*, but a *passing test
that has lost contact with the behaviour it verifies* is worse than
no test. Three row-level failures:

- **The red-but-ignored test.** A flaky test fails once a week;
  someone adds `@pytest.mark.skip("flaky, fix later")`; "later"
  never comes. The test now consumes CI cycles, pollutes the output,
  and teaches the team that red is ignorable — the opposite of TDD
  × Fence's purpose. If a test is not trusted enough to block a
  commit, it is not trusted enough to live in the main suite. Move
  it to quarantine with a dated owner or delete it.
- **The green-and-stale test.** A test pins behaviour the product
  requirement removed two quarters ago. Nobody notices because it
  stays green. An agent reading the test as part of TDD × Bridle now
  learns a *wrong* contract and writes new code against it. Green
  alone is not evidence of relevance; Groom must periodically ask
  *which spec does each test now correspond to, and is that spec
  still live?*
- **The adversarial test that never got written.** The test the
  human-authored test *should* have been is the one that would have
  found the agent's shortcut. If PRs never add "one more test that
  attacks the cheapest path to green" (see Ch.04's first-try-pass
  pitfall), TDD × Paddock slowly trains the agent rather than
  guarding against it.

Row-level test: does your team's test-to-LOC ratio *increase* after
AI-assisted PRs, or stay flat? If it stays flat, you are under-
investing in the test side of the red-green loop at the precise
moment the loop is cheapest to run.
```

(mdd-x-bridle)=
### MDD × Bridle — The one metric that steers

**Definition.** A bridle in this cell is a *north-star metric* named
before production traffic hits the system. Everything else is
diagnostic. The canonical candidate for an AI coding harness is **mean
agent turns to green** on a fixed benchmark suite
{cite}`langchain2026tbench`.

```{literalinclude} ../_handson/05-harness-anatomy/mdd-x-bridle/metrics-north-star.md
:language: markdown
```

(mdd-x-fence)=
### MDD × Fence — Cost caps and circuit breakers

**Definition.** A fence in this cell is an *automated refusal* the moment
an observed cost, latency, or error-rate signal crosses a pre-declared
threshold. Cost caps on LLM calls, rate limits on tool invocations, and
soft/hard kill-switches are typical {cite}`majors2022observability`.

```{literalinclude} ../_handson/05-harness-anatomy/mdd-x-fence/cost-cap.yaml
:language: yaml
```

(mdd-x-paddock)=
### MDD × Paddock — Release SLIs and staging soak

**Definition.** A paddock in this cell is a *release gate* that requires
production-equivalent signals to hold over a bounded staging window
before the bits are allowed to graduate {cite}`ford2017buildingevolutionary`.
The window itself is the paddock; the SLIs are the fence at its edge.

```{literalinclude} ../_handson/05-harness-anatomy/mdd-x-paddock/release-sli.md
:language: markdown
```

(mdd-x-groom)=
### MDD × Groom — Weekly metric audits and dashboard hygiene

**Definition.** A groom action in this cell is a *weekly review of the
metric surface itself* — which signals are still steering decisions,
which dashboards have no owner, which alerts fire without a runbook.
Lehman's laws {cite}`lehman1980laws` apply to metrics as much as to
code: unmaintained signals decay into noise.

```{literalinclude} ../_handson/05-harness-anatomy/mdd-x-groom/weekly-audit.sh
:language: bash
```

```{admonition} Pitfall — MDD row failure modes
:class: warning

The MDD row fails more quietly than the other two rows because
metrics decay *asymptotically*: a broken test goes red, a stale
spec produces obvious contradictions, but a decaying dashboard
merely becomes less useful. The three row-level failures:

- **The north-star nobody watches.** A metric was declared
  load-bearing, a dashboard was built, a threshold was set — and
  no one looks at it outside incidents. The signal exists but does
  not *steer*; MDD × Bridle has a file and an empty chair. Fix:
  every north-star needs a named owner and a weekly agenda slot,
  or demote it to a diagnostic.
- **The cost cap with no tripwire.** A cost cap is configured at
  the API layer and never fires. Either the cap is too loose (it
  silently permits regression) or the cap is tight enough to matter
  but nobody is paged when it hits. MDD × Fence that never refuses
  anything for a quarter is indistinguishable from no fence at
  all.
- **The SLI that drifted from reality.** The staging SLI still
  measures endpoint P99, but the product shifted last quarter and
  the load-bearing path is now a background job whose latency the
  SLI ignores. Release gates keep passing; regressions ship. MDD ×
  Paddock demands the SLIs be re-audited whenever the product's
  load-bearing path moves — which the agent's velocity now makes
  more frequent, not less.

Row-level test: for each MDD cell, can you name both the signal
*and* the specific decision it drove in the last thirty days? A
signal without a decision it influenced is a dashboard pixel, not
a guardian.
```

## Research Foundations

The matrix's analytical claim rests on five citable pillars:

- **Primary academic source** for Harness Engineering as a distinct
  discipline: the CAR decomposition and HarnessCard reporting format
  {cite}`car2025decomposition`.
- **Industry triangulation** across two independent, non-academic
  framings: Thoughtworks' radar entry {cite}`thoughtworks2026harness`
  and LangChain's five-part anatomy {cite}`langchain2026tbench`.
- **Fitness-function lineage** for the zones: Ford, Parsons & Kua's
  *Building Evolutionary Architectures*
  {cite}`ford2017buildingevolutionary` supplies the vocabulary of
  *architectural fitness functions* the four zones operationalise.
- **Evolution-law lineage** for §05.Groom: Lehman's 1980 laws of
  software evolution {cite}`lehman1980laws` are the underlying theory
  for why the Groom column exists at all.
- **Practitioner lineage** for the zones' AI-era interpretation: the
  author's own 2026-03-28 blog post {cite}`walterfan2026guardians` and
  the lazy-scrum-team workflow repository {cite}`lazyscrumteam2026`.

## Hands-On

Twelve artefacts live under
`book/source/_handson/05-harness-anatomy/`, one per cell, following
the directory layout `<guardian>-x-<zone>/<filename>`:

- **SDD row:** `AGENTS.md.sample`, `prompt-schema.json`,
  `acceptance-gate.md`, `update-docs.sh`
- **TDD row:** `starter-tests/test_loop.py` (under `tdd-x-bridle/`),
  `hooks.json`, `ci-gate.yml`, `flaky-test-quarantine.md`
- **MDD row:** `metrics-north-star.md`, `cost-cap.yaml`,
  `release-sli.md`, `weekly-audit.sh`

Each artefact is inline-rendered above inside its own H3 subsection; the
file on disk is the single source of truth. A reader who wants to ship
one cell at a time may copy any single file and begin. The book's
central recommendation in Chapter 12 is that a team ships **one full row
or one full column in 60 days** — which is thirty days of reading this
chapter and another thirty of shipping four artefacts.
