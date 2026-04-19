---
status: draft
chapter-type: methodology
---

# Operating a Harness: Entropy, Observability, Approval Gates, Meta-Harness Evolution

> *A harness is not a project you ship; it is an environment you tend.*

Chapter 05 rendered the twelve cells as a static matrix. This chapter
answers the operational question the matrix leaves open: once the cells
are filled, what does *Monday through Friday* look like? The answer
organises around four concerns — **entropy management**,
**observability practice**, **approval gates**, **meta-harness
evolution** — and draws three structural patterns directly from the
`lazy-scrum-team` workflow repository that Chapter 09 treats in full.

## Concern 1 — Entropy management

### What it is

Every harness accumulates entropy: stale `verified:` headers, dead links
in `AGENTS.md`, npm dependencies two minor versions behind the upstream
audit feed, Rust crates whose `cargo audit` flags fired last week and
were silently closed. Left alone, entropy turns a working harness into a
*decorative* one — the files still exist, reviewers still tick the
boxes, but the agent and the humans both route around them. Cunningham's
1992 technical-debt metaphor {cite}`cunningham1992debt` and Tom et
al.'s 2013 systematic review {cite}`tom2013debtinterest` both apply, but
this chapter calls the phenomenon *entropy* specifically to stress that
the harness decays even when the code it wraps does not.

### Day-to-day practice

Entropy is controlled by two recurring jobs: a **doc-sync check** that
refuses merges when docs and code drift (`doc-sync-check.sh` below), and
a **weekly audit workflow** that runs `cargo audit` / `npm audit` /
`gitleaks` in a single pass and writes a dated report under `reports/`.
Two reports that diff are *the* entropy signal; teams that do not keep
two weeks of reports cannot tell entropy from the weather.

```{literalinclude} ../_handson/06-operating-a-harness/doc-sync-check.sh
:language: bash
```

```{literalinclude} ../_handson/06-operating-a-harness/entropy-audit.yml
:language: yaml
```

The deeper mechanism is **differential decay**. The code's entropy is
paid for by every bug, every review comment, every failed build —
thousands of small pressures keeping it close to reality. The
harness's entropy is paid for by *nothing*: a stale `AGENTS.md` rule
does not crash anything, it just silently mis-steers. Over a quarter
the two diverge — the code stays current, the harness drifts — and
the harness's rot is the most invisible kind precisely because it is
not self-announcing. That is why Groom is a column, not a footnote.

```{admonition} Pitfall — "We will audit when things break"
:class: warning

A team postpones the weekly entropy audit because "nothing is on
fire". Six months later something is on fire: a dependency with a
known CVE shipped to production, traced back to a `npm audit`
warning from March that nobody saw because there was no weekly
report to compare against April's. **Why**: entropy audits are
*calibration*, not diagnosis — their value comes from producing a
baseline week-to-week. A team that only runs the audit during
incidents has no baseline, so the audit output reads as noise.
**Symptom**: CVE patch turnaround is measured in months not days;
`npm audit --audit-level=high` returns dozens of findings with no
opinion on which are new; the first action in every incident is
"let's check if we had warnings for this". **Fix**: the audit
runs on a calendar, even (especially) when nothing is wrong; the
dated `reports/` directory is the baseline; the weekly diff is
the signal.
```

## Concern 2 — Observability practice

### What it is

Observability in a harness context means three surfaces are continuously
readable {cite}`majors2022observability`: (a) production SLIs the product
team already watches, (b) harness-internal signals the product team
usually doesn't — token cost, cache hit rate, agent turns-to-green
{cite}`langchain2026tbench` — and (c) *spec-observance* signals that
compare the `AGENTS.md` surface against the behaviour seen in logs.

### Day-to-day practice

A minimal observability setup starts with exposing Claude Code's
`/cost` endpoint to Prometheus and letting the existing dashboards
stack do the rest. The exercise is three lines of scrape config, not a
platform redesign:

```{literalinclude} ../_handson/06-operating-a-harness/prometheus-scrape.yml
:language: yaml
```

The *cultural* move — more important than the config — is that someone
owns the dashboard and speaks to it in the Monday review. Unowned
dashboards rot faster than uninstrumented code
{cite}`humble2010continuousdelivery`.

```{admonition} Pitfall — The "spec-observance blindspot"
:class: warning

A team wires production SLIs to Prometheus, adds cost-per-turn
instrumentation, and watches both religiously — but never
instruments *spec observance*. Result: when the agent's code silently
diverges from `AGENTS.md`'s claims (new writes bypass the
repository pattern, new endpoints skip the auth middleware), the
dashboards show green across the board because the divergence is
not in the product's latency or the agent's cost — it is in the
gap between what the spec promises and what the code does.
**Symptom**: incidents caused by "that's not how we do it here"
with no prior dashboard signal; architects complain that the agent
"doesn't follow the rules" but the rules are not mechanically
monitored. **Fix**: for every load-bearing bullet in `AGENTS.md`,
ask "what metric would go non-zero if this bullet were violated?"
If the answer is *none*, the bullet is unenforceable prose and
belongs in the documentation folder, not the spec.
```

## Concern 3 — Approval gates (Hard vs Soft)

### What they are

Gates are the points where a human or automated reviewer says *no, not
yet*. Two common failure modes are **undeclared gate class** (everyone
assumes a gate is hard until someone needs a waiver at 5pm Friday) and
**gate evaporation** (a gate that always passes silently disappears from
the team's mental model). Both are avoided by borrowing three patterns
from the `lazy-scrum-team` workflow skill {cite}`lazyscrumteam2026`:

- **Artefact State Model** — draft → review → approved → archived — with
  explicit transition rules and role-owned invariants. A concrete
  encoding is shipped as a YAML file readers can adopt:

```{literalinclude} ../_handson/06-operating-a-harness/artefact-state-model.yaml
:language: yaml
```

- **Rework Matrix** — the finder × fixer matrix naming the rework
  artefact that must accompany every hand-off. Chapter 09 carries the
  canonical treatment.

```{literalinclude} ../_handson/06-operating-a-harness/rework-matrix.md
:language: markdown
```

- **Hard vs Soft Gates** — every gate declares its class at creation, and
  soft-gate waivers carry a named role and an expiry. The canonical
  enumeration lives in Chapter 09; the template reproduced here is
  sufficient for most new harnesses:

```{literalinclude} ../_handson/06-operating-a-harness/hard-vs-soft-gates.md
:language: markdown
```

```{admonition} Pitfall — Gate fatigue and the "always-waive" drift
:class: warning

A team starts with tight gates. After six weeks, three gates fire
routinely on legitimate changes that fall outside their original
scope; waivers accumulate; the Soft gate default quietly becomes
*waive first, investigate if something breaks*. Within a quarter,
Soft gates are telemetry at best — they report what was waived, not
what was refused. **Why**: gates that fire with a false-positive
rate above roughly 20% lose their psychological authority; the
reviewer's default flips from *challenge the change* to *challenge
the gate*. Once flipped, it does not flip back without an explicit
reset. **Symptoms**: waiver count per sprint rises monotonically;
"exception for this one" becomes a recognised phrase; new joiners
learn that the gate is bypassable before they learn what it was
for. **Fix**: track waiver-rate as a first-class metric (every
Soft gate's waiver rate is itself an MDD signal); when a gate's
rate crosses 20%, *tighten the scope of the gate* (reduce its
surface area until it only fires on actual violations) rather
than loosening the policy. A gate that only fires when it should
is a gate the team defends; a gate that fires constantly is a
gate the team routes around.
```

## Concern 4 — Meta-harness evolution

### What it is

A harness that cannot update itself is a harness locked to its first
author's 2024 model of the world. Meta-evolution is the practice of
treating the harness as *its own first-class product*: it has releases,
it has a changelog, it has metrics about itself, and it upgrades on a
cadence rather than on a panic. Ford, Parsons & Kua's evolutionary
architecture {cite}`ford2017buildingevolutionary` and Lehman's evolution
laws {cite}`lehman1980laws` are the theoretical backing.

### Day-to-day practice

Meta-evolution is cheap if you do it as a *habit* and catastrophic if
you do it as a *project*. The habit looks like:

1. Every HarnessCard update lands as a PR to the harness's own
   repository, with the same review discipline as production code.
2. The harness ships a `CHANGELOG.md` dedicated to the harness (not the
   product), listing every bridle / fence / paddock / groom change.
3. Once a quarter, the team runs a *HarnessCard review* and sets one
   explicit cell-level goal for the next quarter.

```{admonition} Pitfall — The meta-harness infinite regress
:class: warning

A team takes "the harness is a product" seriously and proposes a
*meta-harness*: a harness to govern how the harness evolves. Then
a meta-meta-harness to audit the meta-harness. Within two sprints
the team has a tower of YAML files that reviewers cannot
distinguish, none of which correspond to a production signal, and
the original harness has not moved. **Why**: every layer of meta
adds review cost without adding enforcement — the meta-harness's
rules are aspirational because there is no meta-meta *fence* that
refuses bad meta changes. The regress resolves only if you anchor
at a concrete production signal. **Fix**: stop at one level. The
harness governs the agent; the team governs the harness; the
harness's own PR review discipline is sufficient self-governance.
If you feel the pull toward a meta-harness, instead ask: which
production signal would tell us the harness has degraded? That
signal, wired into a weekly review, is the only meta-layer worth
having.
```

### The "harness theatre" failure, named

Chapter 01 promised this chapter would name the failure mode in which
a harness grows but its leverage does not. That mode is *harness
theatre*, and it has a reliable diagnostic: the ratio of
**harness-shaped artefacts** to **refused artefacts per week**. A
healthy harness refuses something on most days — a commit, a tool
call, a PR, a waiver request. A theatrical harness refuses nothing
for weeks while its file count grows. The canonical question to
ask in the Monday review is not *"what did we add to the harness?"*
but *"what did the harness refuse, and was it right to refuse it?"*
Teams that cannot answer the second question should not be adding
to the first.

## Tauri-Todo: the four concerns in one arc

The following hands-on arc stitches all four operating concerns into a
single running story using a real Tauri 2 + Rust + TypeScript desktop
application. The runnable companion repository is at
`walterfan/lazy-todo-app`; the three harness fragments below live at
`book/source/_handson/06-operating-a-harness/tauri-todo/` and
compose the smallest complete harness for a Tauri app.

### Fragment 1 — `CLAUDE.md` (Bridle)

Rust's ownership discipline {cite}`jung2018rustbelt` and Tauri's IPC
boundary {cite}`tauri2024security` give the agent two strong structural
constraints before the first line of application code is written. The
`CLAUDE.md` below turns those constraints into house rules the agent
must read on every turn.

```{literalinclude} ../_handson/06-operating-a-harness/tauri-todo/CLAUDE.md
:language: markdown
```

### Fragment 2 — `pre-commit-config.yaml` (Fence)

Pre-commit hooks enforce the bridle at the keystroke. The Tauri-specific
additions — `cargo clippy -D warnings`, a `cargo audit` at push time,
and a `gitleaks` hook — make the agent's Rust edits as cheap to review
as the TypeScript ones.

```{literalinclude} ../_handson/06-operating-a-harness/tauri-todo/pre-commit-config.yaml
:language: yaml
```

### Fragment 3 — `AGENTS.md` (Paddock + Groom)

Finally, `AGENTS.md` declares the role cast, the mergeable-PR contract
(Hard gates must pass, Soft gates may carry a dated waiver), and the
weekly Groom schedule. Each item references a file earlier in this
chapter — which closes the loop between the generic operating
primitives and the worked arc.

```{literalinclude} ../_handson/06-operating-a-harness/tauri-todo/AGENTS.md
:language: markdown
```

The copilot-productivity literature {cite}`peng2023copilotstudy,ziegler2022productivity`
shows that agents accelerate whichever guardrail the environment already
provides; the Tauri-Todo fragments above supply all three at once. A
developer who commits them into a fresh `lazy-todo-app` clone has a
working harness before the first feature lands.

## Research Foundations

Operating a harness rests on five cited lineages:

- **Entropy and technical debt** — Cunningham's 1992 debt metaphor
  {cite}`cunningham1992debt` and Tom et al.'s 2013 systematic review
  {cite}`tom2013debtinterest` motivate the Monday-morning audit.
- **Observability** — Majors, Fong-Jones & Miranda's *Observability
  Engineering* {cite}`majors2022observability` frames harness-internal
  signals as first-class; the LangChain Terminal-Bench 2.0 data point
  {cite}`langchain2026tbench` provides the industry baseline for
  *turns-to-green* as an observable.
- **Approval gates and release discipline** — Humble & Farley's
  *Continuous Delivery* {cite}`humble2010continuousdelivery` supplies
  the hard-gate grammar; the `lazy-scrum-team` skill
  {cite}`lazyscrumteam2026` extends it to the role-aware rework matrix
  used above.
- **Meta-evolution** — Ford, Parsons & Kua
  {cite}`ford2017buildingevolutionary` and Lehman
  {cite}`lehman1980laws` establish that a system that does not
  continuously adapt loses fitness; the harness obeys the same law.
- **Tauri-Todo arc foundations** — Jung et al.'s *RustBelt*
  {cite}`jung2018rustbelt` grounds the ownership-as-harness argument;
  the Tauri 2 security white paper {cite}`tauri2024security` grounds the
  IPC-boundary discussion; Peng et al. and Ziegler et al.
  {cite}`peng2023copilotstudy,ziegler2022productivity` show why the
  bridle is load-bearing when an agent is in the loop.

## Hands-On

Operating primitives and the Tauri-Todo worked arc live under
`book/source/_handson/06-operating-a-harness/`:

- **Operating primitives:** `doc-sync-check.sh`, `entropy-audit.yml`,
  `prometheus-scrape.yml`, `artefact-state-model.yaml`,
  `rework-matrix.md`, `hard-vs-soft-gates.md`.
- **Tauri-Todo worked arc:** `tauri-todo/CLAUDE.md`,
  `tauri-todo/pre-commit-config.yaml`, `tauri-todo/AGENTS.md`, and a
  `tauri-todo/README.md` cross-linking to the runnable companion
  repository `walterfan/lazy-todo-app`.

Together these artefacts supply every cell in the MDD column of the
Chapter 05 matrix and most of the SDD × Groom cell. The remaining SDD
and TDD cells live in their own chapters' Hands-On tracks and in the
case studies that follow in Part IV.
