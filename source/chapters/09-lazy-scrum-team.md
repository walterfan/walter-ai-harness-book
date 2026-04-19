---
status: draft
chapter-type: case-study
case-study-kind: open-source
---

# Case Study: lazy-scrum-team — A Workflow-Encoded Harness

> *Most teams have roles. Few teams have contracts between those roles. Fewer still have artefacts that make those contracts machine-readable.*

`lazy-scrum-team` {cite}`lazyscrumteam2026` is a Claude Code /
Cursor-compatible skill package that encodes a full Scrum-inspired role
cast as executable workflow. Unlike OpenHarness (a runtime) and
Superpowers (a skill library), `lazy-scrum-team` treats *the workflow
itself* as the harness — the roles, the hand-offs between them, and the
rework artefacts that travel along those hand-offs. This chapter is the
book's canonical treatment of the three patterns Chapter 06 only
referenced: the Artefact State Model, the Rework Matrix, and the Hard
vs Soft Gate classification.

## §09.1 — Role cast

The skill ships seven explicit roles; every role has a one-paragraph
contract and a set of owned artefacts.

```{list-table}
:header-rows: 1
:widths: 20 40 40

* - Role
  - Owns
  - Cannot
* - Product Owner (PO)
  - `specs/*.md`, backlog order
  - write production code; approve PRs
* - Architect
  - ADRs, module boundaries, `storage.rs`-style gate files
  - override PO on feature intent
* - Scrum Master
  - Sprint cadence, state-model integrity
  - write or review code
* - Developer
  - Feature code + unit tests
  - self-merge
* - Code Reviewer
  - Hard-gate checklist, PR approval
  - self-approve; review own code
* - Test Engineer
  - Acceptance tests, coverage floor
  - approve PRs
* - Final Acceptance
  - Release PR + HarnessCard delta
  - perform the review themselves
```

Scrum {cite}`schwaber2020scrum` supplies the role vocabulary; the
skill's innovation is less about roles and more about what happens
*between* them. Conway's Law {cite}`conway1968law` reminds us that the
communication structure leaks into the artefact structure; the skill
uses this as a feature rather than a bug — the hand-off artefacts *are*
the communication channel.

## §09.2 — Pattern 1 — Artefact State Model

Every reviewable artefact in the harness has exactly four states —
`draft → review → approved → archived` — with tightly constrained
transitions. The canonical encoding ships as a YAML file any ticketing
system can import:

```{literalinclude} ../_handson/09-lazy-scrum-team/state-transitions.yaml
:language: yaml
```

Two invariants make the state model load-bearing rather than decorative:
only Final Acceptance can flip `review → approved`, and approved
artefacts cannot return to `draft` without passing through `archived`
first. These two invariants together eliminate the most common failure
mode of review processes — silent rework — because any regression on
an approved artefact is visible as an explicit reopen event.

(ch09-rework-matrix)=
## §09.3 — Pattern 2 — Rework Matrix

The Rework Matrix names, for every finder × fixer pair, the specific
artefact that must accompany the hand-off. Pull-request-as-workflow
research {cite}`gousios2014pullbased` and the classic
specification-by-example corpus {cite}`adzic2011specbyexample` both
argue for machine-readable hand-offs; the Rework Matrix is this book's
opinionated encoding.

```{literalinclude} ../_handson/09-lazy-scrum-team/rework-matrix.md
:language: markdown
```

Concretely: when a Test Engineer rejects a Developer's PR, the rejection
lands as a `bug-report.md` file in the PR body, not as a Slack message.
When the PO rejects the Architect's ADR, it lands as a `spec-delta.md`
under `docs/rework/<sprint>/`. The named file is the contract; "just
fix it" comments are institutional amnesia.

## §09.4 — Pattern 3 — Hard vs Soft Gates

Every gate in the harness declares its class at creation time: a **Hard
gate** that can never be waived and a **Soft gate** that may be waived
by a named role with an expiry date. The classification is reproduced
verbatim into Chapter 06's hands-on directory; the canonical table is:

| Gate                | Class | Waiver rule                                       |
|---------------------|-------|---------------------------------------------------|
| unit-test suite     | Hard  | never waive; fix or revert                        |
| lint                | Hard  | never waive for new code                          |
| coverage floor      | Soft  | Architect + reason; max 7 days                    |
| cost cap            | Soft  | MDD Owner; max 24 hours                            |
| secrets scan        | Hard  | never waive; rotate the secret                     |
| docs link-check     | Soft  | any Reviewer; max until next weekly groom          |

The Humble & Farley *Continuous Delivery* lineage
{cite}`humble2010continuousdelivery` supplies the Hard-gate grammar; the
DORA metrics literature {cite}`forsgren2018accelerate` shows why the
ratio of Soft-gate waivers to Hard-gate passes is itself a health
signal.

## §09.5 — 12-cell highlight map

```{list-table}
:header-rows: 1
:widths: 20 8 72

* - Cell
  - Score
  - Evidence
* - SDD × Bridle
  - 4
  - `roles/*.md` are explicit agent-readable role contracts.
* - SDD × Fence
  - 4
  - State-machine invariants refuse ill-formed transitions.
* - SDD × Paddock
  - 5
  - Verification Table + acceptance review is the canonical SDD paddock.
* - SDD × Groom
  - 3
  - Sprint retrospective recurses into skill updates; cadence varies.
* - TDD × Bridle
  - 3
  - Test Engineer role shapes context but no starter tests committed.
* - TDD × Fence
  - 4
  - Hard-gate policy refuses red-tree merges.
* - TDD × Paddock
  - 4
  - Acceptance review ties test results to the spec.
* - TDD × Groom
  - 3
  - Flaky-test policy implicit; quarantine not named.
* - MDD × Bridle
  - 2
  - No north-star metric defined at skill level.
* - MDD × Fence
  - 2
  - Cost caps not shipped; delegated to the host platform.
* - MDD × Paddock
  - 2
  - SLI gate not in scope.
* - MDD × Groom
  - 2
  - Weekly audit defined but not automated by the skill.
```

Strongest row: **SDD** (mean 4). Strongest column: **Paddock** (mean
3.25). Weakest row: **MDD** (mean 2). The pattern is consistent with a
workflow-encoded harness that optimises for approval discipline rather
than runtime observability.

### Where the workflow-as-harness approach is brittle

The lazy-scrum-team patterns are the book's canonical SDD × Paddock
exemplar, but reading them uncritically risks two structural traps.

- **Roles drift faster than the files that encode them.** The seven
  role contracts in §09.1 assume a team organised into those seven
  functions. Most teams are not — a solo founder is PO, Architect,
  Developer, and Code Reviewer in the same afternoon; a five-person
  startup collapses Test Engineer and Developer. A workflow harness
  that presupposes a role cast the team does not have generates
  friction at every hand-off because the artefact the Rework Matrix
  demands has no natural author. **Fix**: copy the *pattern* (named
  rework artefacts, explicit hand-off contracts) but map it to roles
  your team actually has, even if that means four contracts instead of
  seven. Conway's law {cite}`conway1968law` cuts both ways — the
  workflow must match the communication structure that exists, not the
  one the template assumes.
- **State-machine theatre.** The four states (`draft → review →
  approved → archived`) are load-bearing only if transitions are
  mechanically enforced. A team that writes the YAML but leaves
  transitions to "whoever remembers to update the ticket" gains
  nothing: an approved artefact that silently regresses to draft in
  everyone's heads while staying approved in the tracker is worse
  than no state machine at all, because it combines the cost of the
  process with none of its leverage.

```{admonition} Pitfall — Workflow without tooling
:class: warning

A team adopts the seven role contracts, the Rework Matrix, and the
state machine, all in prose. Adoption looks good for six weeks.
Then a Friday evening incident produces a hotfix PR that the
Developer self-merges — no Code Reviewer, no Final Acceptance, no
state transition recorded. Nobody raised the alarm because the
rules existed only as expectations. **Why**: a prose workflow is a
norm; a norm under pressure yields to the first incident. **Fix**:
wire at least two load-bearing transitions into tooling — branch
protection that refuses self-merge is the minimum, a CODEOWNERS
file that requires the correct role to approve is better. Every
rule that is not mechanically enforced is a rule that will be
suspended on the first bad Friday.
```

## HarnessCard

```{list-table}
:header-rows: 1
:widths: 35 65

* - Field
  - Value
* - HarnessCard schema version
  - CAR-HarnessCard v0.2 {cite}`car2025decomposition`
* - Subject
  - lazy-scrum-team skill, 2026-04 snapshot {cite}`lazyscrumteam2026`
* - License
  - MIT
* - Control layer (CAR)
  - Strongly opinionated via role contracts and state machine.
* - Agency layer (CAR)
  - Delegated to host platform (Claude Code / Cursor).
* - Runtime layer (CAR)
  - None; the skill is prose + YAML only.
* - SDD (mean)
  - 4.0
* - TDD (mean)
  - 3.5
* - MDD (mean)
  - 2.0
* - Primary citation
  - {cite}`lazyscrumteam2026`
```

## Research Foundations

- **Scrum** {cite}`schwaber2020scrum` — the role-vocabulary lineage the
  skill extends with explicit hand-off contracts.
- **Specification by Example** {cite}`adzic2011specbyexample` — the
  executable-spec lineage behind the Verification Table pattern.
- **Conway's Law** {cite}`conway1968law` — the reason role structure
  *must* be encoded in artefact structure.
- **Pull-request-as-workflow** {cite}`gousios2014pullbased` — empirical
  basis for the PR body as a first-class spec surface.
- **DORA / Accelerate** {cite}`forsgren2018accelerate` — the metric
  lineage for measuring whether the gate discipline is working.

## Hands-On

Five copyable artefacts live under
`book/source/_handson/09-lazy-scrum-team/`:

- `roles/po.md`, `roles/code-review.md`, `roles/acceptance-review.md` —
  excerpted and attributed role contracts.
- `state-transitions.yaml` — adaptable state machine.
- `rework-matrix.md` — finder × fixer matrix with named rework artefacts.

A reader who wants to adopt the three patterns *without* adopting the
whole skill can copy these five files, customise the role cast, and have
a working workflow harness before lunch.
