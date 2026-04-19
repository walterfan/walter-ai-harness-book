---
status: draft
chapter-type: conclusion
---

# Where We Go from Here

> *A book that does not end with a checklist is a book that does not expect to be used.*

## §12.1 — The Thesis in One Page

The book's analytical spine fits onto one page: three guardians × four
zones = twelve cells, each cell an artefact a team can ship. Every cell
below is a `{ref}` link back into its Chapter 05 H3 subsection.

```{list-table}
:header-rows: 1
:widths: 10 22 22 22 22

* -
  - **Bridle** — steers before writing
  - **Fence** — refuses bad work
  - **Paddock** — bounds the agent's roam
  - **Groom** — tends the harness itself
* - **SDD**
  - {ref}`sdd-x-bridle`
  - {ref}`sdd-x-fence`
  - {ref}`sdd-x-paddock`
  - {ref}`sdd-x-groom`
* - **TDD**
  - {ref}`tdd-x-bridle`
  - {ref}`tdd-x-fence`
  - {ref}`tdd-x-paddock`
  - {ref}`tdd-x-groom`
* - **MDD**
  - {ref}`mdd-x-bridle`
  - {ref}`mdd-x-fence`
  - {ref}`mdd-x-paddock`
  - {ref}`mdd-x-groom`
```

All twelve `{ref}` links resolve to live subsections in Ch.05; a reader
who clicks any one of them lands on a working artefact and a definition.

## §12.2 — 30/60/90-Day Action Checklist

The book's single most important claim is that you do not need to adopt
all twelve cells at once. You pick **one**, ship it, ship the *column*
or the *row* it sits in, then run a full HarnessCard review. Below are
the three sub-tasks with hands-on pointers; a standalone copy lives at
`_handson/12-where-we-go-from-here/checklist-30-60-90.md`.

### Day 1–30 · One Cell

Pick one matrix cell, ship one artefact for it, run it against the
HarnessCard rubric from Appendix D.

- **SDD × Bridle.** Commit an `AGENTS.md` based on
  `_handson/05-harness-anatomy/sdd-x-bridle/AGENTS.md.sample`; ties into
  {ref}`sdd-x-bridle`.
- **TDD × Fence.** Install a `PreToolUse` hook based on
  `_handson/05-harness-anatomy/tdd-x-fence/hooks.json`; ties into
  {ref}`tdd-x-fence`.
- **MDD × Fence.** Adopt a per-session cost cap from
  `_handson/05-harness-anatomy/mdd-x-fence/cost-cap.yaml`; ties into
  {ref}`mdd-x-fence`.

Ford, Parsons & Kua {cite}`ford2017buildingevolutionary` supply the
framing: one fitness function at a time is already a real improvement.

```{admonition} Pitfall — The Day-30 "we are done" trap
:class: warning

A team ships one cell by Day 30, celebrates, and stops. Ninety days
later the cell has decayed — no Groom job was added, no review
cadence was established, nobody owns the artefact. The +1 became
+0.3 and is trending toward zero. **Why**: a single cell is a
seed, not a crop. The Day-30 milestone exists to prove the team
*can* ship a harness artefact; the Day-60 milestone exists to
prove the team can *keep* one alive. Teams that skip the second
milestone end the quarter with the same harness theatre they
started with, minus a week of engineering time. **Fix**: the
Day-30 exit criterion is not "artefact is merged" but "the
artefact has an owner, a review cadence, and one refused or
measured event in its log". An unused cell is a rehearsal, not a
production.
```

### Day 31–60 · One Row or One Column

Extend to a full row (one guardian across all four zones) or a full
column (one zone across all three guardians).

- **Full SDD row.** Ship Bridle + Fence + Paddock + Groom artefacts from
  `_handson/05-harness-anatomy/sdd-x-*/`. Cells
  {ref}`sdd-x-bridle`, {ref}`sdd-x-fence`, {ref}`sdd-x-paddock`,
  {ref}`sdd-x-groom`.
- **Full Fence column.** Ship SDD + TDD + MDD fences from
  `_handson/05-harness-anatomy/*-x-fence/`. Cells {ref}`sdd-x-fence`,
  {ref}`tdd-x-fence`, {ref}`mdd-x-fence`.
- **Operating drumbeat.** Adopt the weekly entropy audit
  (`_handson/06-operating-a-harness/entropy-audit.yml`) and the artefact
  state model (`_handson/06-operating-a-harness/artefact-state-model.yaml`);
  these harden the Groom row — {ref}`sdd-x-groom`, {ref}`tdd-x-groom`,
  {ref}`mdd-x-groom`.

Forsgren, Humble & Kim's DORA-metrics work {cite}`forsgren2018accelerate`
argues that a quarterly cadence is the right unit for measurement;
day 31–60 is the second month of your first quarter.

```{admonition} Pitfall — The Day-60 "row or column?" paralysis
:class: warning

A team reaches Day 31 with one cell shipped and spends the next
three weeks in a committee debate: *row* or *column*? Which
guardian? Which zone? By Day 60 no second artefact has shipped;
the team reports "strategy work" in retro. **Why**: the row-or-
column choice is optimisation theatre — either direction is a
real improvement, and the wrong choice (if one exists) is recoverable
in the next quarter. Time spent choosing is time not spent
shipping. **Fix**: pick the direction whose *weakest cell* is the
most embarrassing to name out loud. If you are ashamed to show a
colleague your `AGENTS.md` today, ship the full SDD row; if your
CI fails intermittently and nobody rotates the key that fixes it,
ship the full Fence column. The embarrassment test resolves the
paralysis in five minutes and picks the direction that was always
going to matter most.
```

### Day 61–90 · A Production HarnessCard Review

Run a full HarnessCard review on a production codebase using the blank
template from Appendix D (see {ref}`apd-harnesscard-template`), land at
least one harness-driven improvement, and record the measurable delta.

- **Score.** Fill the twelve-cell blank HarnessCard at
  {ref}`apd-harnesscard-template` — every cell gets a 0–5 score and a
  one-line evidence note. Cross-check against
  {ref}`sdd-x-bridle`, {ref}`tdd-x-fence`, and {ref}`mdd-x-fence`
  using `_handson/11-lazy-ai-coder/HarnessCard-Act1.md` as a worked
  precedent.
- **Raise one cell.** Pick the lowest-scoring cell, land one fix scoped
  to it (a `make` target, a hook, a YAML, a script — see
  `_handson/11-lazy-ai-coder/reproduce.sh` for the worked pattern) and
  tie the fix back to the target cell (e.g. {ref}`mdd-x-paddock`).
- **Re-score and attach.** Author the post-fix HarnessCard using
  `_handson/11-lazy-ai-coder/HarnessCard-Act4.md` as a template, attach
  it to the release PR, and include a one-line delta note naming which
  cell moved (e.g. {ref}`sdd-x-groom`) and by how much.

Lehman's evolution laws {cite}`lehman1980laws` explain why a quarterly
re-score is not optional: unmaintained harnesses decay by default.

```{admonition} Pitfall — Three ways the Day-90 review goes wrong
:class: warning

**Self-scored.** The engineer who shipped the fix also scores it;
scores drift up +0.5 on average. *Fix*: the Day-90 scorer is not the
Day-30 shipper.

**Inputs not outcomes.** Cell scores rise while DORA metrics don't.
Every cell score must carry one outcome metric it is *predicted* to
move (the Ch.11 *vanity delta* pitfall develops this in full).

**Raising the top, not the bottom.** The team lifts a 4 to a 5
instead of a 1 to a 2; the mean rises but the weakest load-bearing
dimension doesn't. *Fix*: the Day-90 ritual must pick the
lowest-scoring cell, even when a stronger cell is tempting.
```

## §12.3 — Open Questions

At most seven directions where the book raises questions it does not
answer. Each carries at least one citation that sketches the adjacent
literature.

- **Meta-harness versioning under multi-tenant LLM deployments.** How
  should harness rules survive a provider rolling out a model change
  mid-quarter, especially when customers share a tenant?
  {cite}`huyen2025aieng`.
- **When to migrate from blog-format `.md` context into a structured
  RAG pipeline.** Karpathy's context-engineering framing
  {cite}`karpathy2025context` bears on this but does not resolve it.
- **HarnessCards for polyglot monorepos and cross-geography teams.**
  Does the 3 × 4 matrix survive scaling up the unit of analysis?
  {cite}`conway1968law`.
- **Continuous vs milestone-level entropy measurement.** Can entropy
  reduction be measured continuously across a sprint, or is milestone
  measurement the highest useful resolution? {cite}`lehman1980laws`.
- **Benchmarks that distinguish good harnesses from bad ones.** The
  Terminal-Bench 2.0 data point is suggestive but not settled
  {cite}`langchain2026tbench`.
- **HarnessCard disclosure requirements for safety-critical agents.**
  Should regulators require HarnessCard-style disclosure the way they
  require SBOMs? {cite}`car2025decomposition`.
- **The half-life of a skill.** How long does a `SKILL.md` keep its
  load-bearing value before prompt drift erodes it?
  {cite}`anthropic2024skills`.

## §12.4 — What the book is *not* arguing

A reader who has made it this far deserves the honest footnote on
what this book's thesis does and does not claim.

- **Harnesses do not replace taste.** Nothing in the 3×4 matrix tells
  a team *which problem is worth solving*, which architecture to
  adopt, or when a `SKILL.md` is answering the wrong question. The
  harness constrains *how* the agent writes code; it does not
  originate *what* code is worth writing. Chapter 02's Stage-4 pitfall
  applies at the whole-book level.
- **Not every team needs every cell.** The §03.5 *when not to use*
  section is not a rhetorical concession; a solo prototype, a
  throwaway script, or a frozen legacy system genuinely do not pay
  back the harness investment. A team adopting the twelve-cell
  discipline for a forty-line CSV parser is performing harness theatre
  whether they know it or not.
- **The naming is not settled.** The four-zone vocabulary is
  practitioner-origin (§05.Provenance). If CAR
  {cite}`car2025decomposition` or LangChain's five-part anatomy
  {cite}`langchain2026tbench` fits your team better, use that framing
  and translate. The book's bet is on the *three-guardian ×
  twelve-cell decomposition* as a Monday-morning planning tool, not
  on the zone names as a final taxonomy.
- **The pitfalls are not exhaustive.** The inline callouts name the
  failures the author has debugged, watched others debug, or read
  credible accounts of. They are a starting vocabulary, not a complete
  bestiary — §12.3 names where new failure modes are most likely to
  surface next.

If this chapter's 30/60/90 checklist, the 3×4 matrix, and the pitfall
vocabulary give your team one refused-commit event, one measured
signal, and one revised `AGENTS.md` bullet in the next ninety days,
the book has done its job.

## Research Foundations

- **DORA / Accelerate** {cite}`forsgren2018accelerate` — cadence and
  metric lineage for the 30/60/90 framing.
- **Lehman's laws** {cite}`lehman1980laws` — why the 90-day review must
  recur.
- **Evolutionary architecture** {cite}`ford2017buildingevolutionary` —
  the fitness-function lineage for one-cell-at-a-time improvement.

## Hands-On

Two copyable artefacts live under
`book/source/_handson/12-where-we-go-from-here/`:

- `checklist-30-60-90.md` — the checklist as standalone markdown ready
  to paste into a team wiki.
- `open-questions.md` — the open-questions list as a standalone file
  researchers can cite.
