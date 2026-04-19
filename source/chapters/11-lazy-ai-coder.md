---
status: draft
chapter-type: case-study
case-study-kind: open-source
worked-example: true
---

# Case Study: Lazy AI Coder — A Four-Act Worked Example

> *If the framework cannot score the book's own host repository and then improve it, the framework is wrong.*

Every case study so far has been *about* someone else's harness. This
chapter is different: it applies the three-guardian × four-zone matrix
to the very repository this book ships from —
[`walterfan/lazy-ai-coder`](https://github.com/walterfan/lazy-ai-coder) —
and lands real fixes on `main`. The chapter is staged as four acts.

```{note}
**Status.** This chapter remains `status: draft` until the Section 14
commits land on the host repository's `main` branch. The book-lint
script walks Act 3's commit SHAs through `git cat-file -e`; until at
least two resolve, the chapter is excluded from the toctree. See §14.5.
```

## Act 1 — Audit

The starting point is a HarnessCard capturing the repository's state as
of the change's start commit. Evidence for each cell is a concrete file
path inside the repository; the full scorecard is shipped as a
hands-on artefact readers can diff against.

```{literalinclude} ../_handson/11-lazy-ai-coder/HarnessCard-Act1.md
:language: markdown
```

The audit lands squarely in the lower-left corner of the matrix: SDD ×
Fence, SDD × Groom, TDD × Fence, and MDD × Bridle / Groom are the five
weakest cells. Cunningham's 1992 technical-debt metaphor
{cite}`cunningham1992debt` and Feathers' *Working Effectively with
Legacy Code* {cite}`feathers2004legacy` supply the vocabulary for why
this matters: this is not a *bad* repository, it is a repository whose
harness has accumulated ordinary, survivable debt that will compound if
left alone. Lehman's evolution laws {cite}`lehman1980laws` predict
exactly this pattern.

## Act 2 — Shortcomings

Five concrete shortcomings, each with a severity label, an evidence
pointer, and the matrix-cell coordinate it maps onto:

1. **Missing `make prompts-lint`.** `config/prompts.yaml` is committed
   without schema validation; broken templates can only be found at
   runtime. (**SDD × Fence**, `major`; evidence `config/prompts.yaml`.)
2. **MCP tool schemas are not validated against their handlers.** A
   handler added without a schema (or vice versa) ships green. (**TDD ×
   Fence**, `major`; evidence `internal/mcp/server.go`,
   `internal/mcp/handlers.go`.)
3. **No cost-observability dashboard for LLM calls.** Monthly spend is
   invisible until the provider bill arrives. (**MDD × Bridle**, `major`;
   evidence — absence of dashboard config under `deploy/`.)
4. **`CLAUDE.md` and `AGENTS.md` have drifted from `openspec/` working
   notes.** The two front-door docs reference concepts that no longer
   exist and fail to reference concepts that now do. (**SDD × Groom**,
   `minor`; evidence `CLAUDE.md`, `AGENTS.md`, `openspec/`.)
5. **No pre-commit hook guarding against committed secrets.** `.env`
   files are ignored but the hook safety net is absent. (**TDD ×
   Fence** / **MDD × Bridle** joint, `critical`; evidence absence of
   `.pre-commit-config.yaml` at repo root.)

Adzic's *Specification by Example* {cite}`adzic2011specbyexample` and
DORA metrics {cite}`forsgren2018accelerate` frame the remediation: each
shortcoming should turn into an executable gate whose presence or
absence is itself a measured metric.

## Act 3 — Applying Harness Engineering

Four fixes land on `main`, each scoped to a single matrix cell and
referenced by commit SHA. The commit-SHA slots below are populated when
Section 14 lands; the book-lint script walks them through `git cat-file
-e` on every build.

```{list-table}
:header-rows: 1
:widths: 28 26 16 30

* - Fix
  - Cell
  - Severity
  - Commit SHA
* - `make prompts-lint` + `scripts/prompts_lint.py`
  - SDD × Fence
  - major
  - `<TBD>` (§14.1)
* - MCP tool schema-vs-handler consistency check
  - TDD × Fence
  - major
  - `<TBD>` (§14.2)
* - `openspec/docs/sources-of-truth.md` index reconciling `CLAUDE.md` + `AGENTS.md`
  - SDD × Groom
  - minor
  - `<TBD>` (§14.3)
* - `.pre-commit-config.yaml` baseline with gitleaks + `make secrets-check`
  - TDD × Fence joint MDD × Bridle
  - critical
  - `<TBD>` (§14.4)
```

Each PR description references this chapter by name (`book —
Ch.11 Act 3`) and carries a one-line *HarnessCard delta* note saying
which cell's score moves and by how much.

## Act 4 — Measuring the Delta

A second HarnessCard, authored after the Act 3 commits land, diffs cell
scores against Act 1 and reports quantitative deltas:

```{literalinclude} ../_handson/11-lazy-ai-coder/HarnessCard-Act4.md
:language: markdown
```

Two quantitative metrics are *required* by the chapter contract; the
hands-on HarnessCard reports four:

- **prompts-lint rule count**: 0 → 7.
- **MCP schema mismatches at CI**: N/A → 0 (new check).
- **secrets-scan coverage (% committed files)**: 0 → 100.
- **`sources-of-truth.md` entries**: 0 → ≥ 6.

The overall HarnessCard mean rises from 1.75 to 2.42 — a +0.67
improvement concentrated in the two Fence cells (+3 each) and SDD ×
Groom (+2). Act 4 deliberately does not touch the MDD row; Chapter 12's
30/60/90 plan picks it up in the next quarter.

### What the delta does *not* prove

Four Act-3 commits raised the HarnessCard mean by 0.67. That is a real
number, and it is also a *bounded* number — worth reading carefully
before quoting it as evidence of a harness working.

- **The delta measures inputs, not outcomes.** Rising cell scores mean
  the repository now has artefacts that the scoring rubric credits;
  they do not yet mean the agent's output has improved. The DORA-style
  outcome metrics (deployment frequency, change failure rate, mean
  time to recovery) are the evidence that the inputs paid off —
  Chapter 12's 90-day review is where those outcomes are expected to
  move, not the Act-4 snapshot.
- **The scorer and the author are the same person.** Act 1's baseline
  and Act 4's re-score were both authored by the same engineer, using
  the same rubric, with full knowledge of what changed. This is
  honest for a self-audit but it is not independent verification —
  the scores are calibration, not measurement. A reader reproducing
  the pattern on their own repo should expect a similar bias in their
  own deltas.
- **Three of four fixes are Fence-shaped.** Fence cells rise most
  easily because refusal is mechanical and measurable. Bridle and
  Paddock cells rise more slowly because they require changes in what
  humans and agents *do*, not just what the CI refuses. A HarnessCard
  mean dominated by Fence gains is an honest first-quarter pattern; a
  HarnessCard whose delta is *only* Fence across four quarters is a
  team investing in refusals without raising intent or acceptance.

```{admonition} Pitfall — HarnessCard vanity delta
:class: warning

A team runs the Chapter 11 playbook, lands four Fence commits, and
reports a +0.67 mean delta to leadership. Leadership is pleased.
Two quarters later, outcome metrics have not moved; the team
doubles down and lands four more Fence commits; the mean rises
again. The harness grows; the outcomes do not. **Why**: the
HarnessCard is a *diagnostic* — its role is to identify weak cells,
not to be optimised against. A team that optimises for the score
rather than the outcome is running a variant of Goodhart's law
(Cunningham's debt metaphor {cite}`cunningham1992debt` applied in
reverse: you *can* pay down debt that was not costing anything).
**Symptom**: cell scores rise, dashboards do not; retros describe
harness work warmly, incidents describe product work painfully.
**Fix**: pair every HarnessCard delta with one outcome metric it
is *predicted* to move. If the outcome does not move after a
quarter, the delta was vanity and the next quarter's investment
should go to a different cell (or a different dimension entirely).
```

## Reading list extension

Act 4's reproducibility claim rests on a short shell script that runs
the three new make targets against a fresh clone at the Act-4 SHA:

```{literalinclude} ../_handson/11-lazy-ai-coder/reproduce.sh
:language: bash
```

The matching `pre-commit-config.yaml` baseline from §14.4 is shipped
alongside for readers who want to lift it verbatim:

```{literalinclude} ../_handson/11-lazy-ai-coder/pre-commit-config.yaml
:language: yaml
```

## Research Foundations

- **Technical debt** {cite}`cunningham1992debt` — vocabulary for Act 1.
- **Legacy code** {cite}`feathers2004legacy` — remediation patterns for
  Act 2.
- **DORA / Accelerate** {cite}`forsgren2018accelerate` — the metric
  lineage behind Act 4.
- **Evolution laws** {cite}`lehman1980laws` — why the overall mean
  continues to drift without Groom investment.

## Hands-On

Four copyable artefacts live under
`book/source/_handson/11-lazy-ai-coder/`:

- `HarnessCard-Act1.md` — pre-fix baseline.
- `HarnessCard-Act4.md` — post-fix re-audit with delta.
- `reproduce.sh` — three `make` targets, one script.
- `pre-commit-config.yaml` — symlink-safe copy of the final baseline.

When §14's commits land on `main`, the HarnessCards are re-scored
against the actual SHAs, the chapter flips to `status: complete`, and
the toctree picks it up.
