---
status: draft
chapter-type: case-study
case-study-kind: open-source
---

# Case Study: Superpowers

> *Not a framework. Not a platform. A library of skills that teach the agent how to think twice before it writes.*

Superpowers, authored by Joseph Vincent and released as open source under
the `obra/superpowers` repository {cite}`vincent2025superpowers,vincent2025superpowersrepo`,
is the philosophical opposite of OpenHarness: where OpenHarness ships a
runtime and a sandbox, Superpowers ships *only* a set of `SKILL.md`
files that structure *how* an agent (specifically, Claude Code) frames
its own work. The whole project is essentially three dozen markdown
files. That is the point.

## §08.1 — Skills-first workflow

The canonical Superpowers workflow is a five-step arc:

1. **Brainstorming** (`skills/brainstorming/SKILL.md`) — refuse to
   implement until intent is clarified.
2. **Writing plans** (`skills/writing-plans/SKILL.md`) — compile the
   brainstorm into a written plan with review checkpoints.
3. **Test-driven development** (`skills/test-driven-development/SKILL.md`)
   — implement only against a failing test.
4. **Code review** (`skills/requesting-code-review/SKILL.md`) — explicit
   review with named rubric before merging.
5. **Finishing** (`skills/finishing-a-development-branch/SKILL.md`) —
   integration, cleanup, PR.

Each step is a skill the agent opts into (or is nudged into) via the
`using-superpowers` meta-skill. Anthropic's skills documentation
{cite}`anthropic2024skills` describes the mechanism; Superpowers is the
most complete public library of skills authored against it.

## §08.2 — A representative skill (≤ 20 lines)

The `test-driven-development/SKILL.md` file is the load-bearing one; it
is also the shortest. The excerpt below reproduces its core (with
ellipses marking omitted prose) and is quoted under the upstream
licence:

```markdown
# Test-Driven Development

## When to use

Use when implementing any feature or bugfix, before writing implementation code.

## What this skill does

1. Writes a failing test that captures the requirement.
2. Runs the test suite and confirms only this test fails.
3. Implements the minimum code to make the test pass.
4. Refactors while the test stays green.

## Red flags that stop this skill

- "I'll write the test after." — no. The skill exits.
- A passing first test — suspect; re-read the requirement.
```

This is a skill file, *not* a code module — the agent's behaviour is
changed by reading prose, not by invoking an API. Mills' Socratic
design essay {cite}`mills2015socratic` and Zeller's systematic debugging
{cite}`zeller2009whyprogramsfail` are the intellectual ancestors: the
skill asks the agent to interrogate itself before committing to action.

## §08.3 — OpenHarness vs Superpowers: complementary, not competing

OpenHarness provides the *engine*; Superpowers provides the *discipline*.
A production harness usually wants both. The two projects differ along
three axes worth making explicit for a reader choosing between them:

```{list-table}
:header-rows: 1
:widths: 20 40 40

* - Axis
  - OpenHarness
  - Superpowers
* - Primary artefact
  - Python package + Docker sandbox
  - `~/.claude/skills/**/SKILL.md` markdown files
* - Guardian emphasis
  - TDD × Fence, MDD × Fence (via permissions, sandbox)
  - SDD × Bridle, TDD × Bridle (via skill invocations)
* - Adoption cost
  - High — new dependency, new runtime
  - Low — copy markdown into `~/.claude/skills/`
```

## §08.4 — 12-cell highlight map

```{list-table}
:header-rows: 1
:widths: 20 8 72

* - Cell
  - Score
  - Evidence
* - SDD × Bridle
  - 5
  - Entire project exists to strengthen this cell; `using-superpowers/SKILL.md` + ~30 sibling skills directly shape the agent's pre-edit context.
* - SDD × Fence
  - 2
  - Skills are prose; no schema validator for skill front-matter.
* - SDD × Paddock
  - 4
  - `requesting-code-review/SKILL.md` + `receiving-code-review/SKILL.md` are role-scoped acceptance gates.
* - SDD × Groom
  - 3
  - `finishing-a-development-branch/SKILL.md` and the brainstorm-to-plan chain keep skills themselves fresh.
* - TDD × Bridle
  - 5
  - `test-driven-development/SKILL.md` is load-bearing across the entire library.
* - TDD × Fence
  - 3
  - Skill prose refuses to proceed on red tests; actual enforcement still relies on Claude Code hooks at the host repo.
* - TDD × Paddock
  - 2
  - No integration suite shipped by Superpowers itself.
* - TDD × Groom
  - 2
  - Flaky-test policy not defined at library level.
* - MDD × Bridle
  - 2
  - No north-star metric in the library.
* - MDD × Fence
  - 1
  - No cost cap, no rate limit, no circuit breaker.
* - MDD × Paddock
  - 1
  - No release SLIs (library is stateless markdown).
* - MDD × Groom
  - 2
  - Weekly audit not defined; upstream changelog captures drift.
```

Strongest column: **Bridle** (mean 4.25). Weakest column: **MDD row**
(mean 1.5). Superpowers leans all the way into SDD / TDD × Bridle, which
is consistent with its purpose — it is a skill library, not a runtime.

## §08.5 — When to reach for Superpowers

- Your team already runs Claude Code and wants stronger pre-edit
  discipline without shipping a new platform.
- You have a `CLAUDE.md` but notice agents still skip tests; the TDD
  skill will help.
- You want a review ritual that applies to *both* the agent's output
  and the human's; the code-review skills cover both.

- *Don't* reach for Superpowers if you need runtime isolation (reach for
  OpenHarness or Claude Code's hooks + sandbox) or if you are working
  against a non-Claude agent that does not honour `SKILL.md` files.

### Where Superpowers is structurally weak

The 12-cell scorecard in §08.4 makes the trade-off explicit: Superpowers
is the strongest public example of SDD × Bridle and TDD × Bridle, and
the weakest on the entire MDD row. The asymmetry is *structural* — a
library of markdown files cannot enforce what it prescribes, and cannot
observe whether it was followed. Two failure modes follow directly.

- **Prescription without enforcement.** A skill's prose says "refuse to
  proceed on a red test". If no hook in the host repo *mechanically*
  refuses the proceed, the skill becomes compliance theatre (Chapter 02's
  Stage 3 pitfall applied at point-blank range). Superpowers is
  strongest when paired with Claude Code's hooks; standalone, it is a
  strongly-worded suggestion.
- **No self-observability.** The library has no signal for "the team
  installed 30 skills and uses 4 of them regularly". Skill-sprawl
  (Chapter 02's Stage 3 pitfall) lands hardest in skills-only harnesses
  precisely because there is no metric on skill invocation rates.

```{admonition} Pitfall — "Skills alone are our harness"
:class: warning

A team adopts Superpowers, copies thirty skills into
`~/.claude/skills/`, and declares the harness complete. Three
months later, measured output quality has not moved despite the
team reporting high skill adoption in retros. **Why**: without a
fence that *refuses* turns which skipped a skill, and without a
metric that reports *which* skills fired, the skill library is
operating on the honour system. The team's intent and the agent's
behaviour are measured only through self-report. **Symptom**:
retros describe the skills warmly; incident post-mortems reveal
the relevant skill existed but was not invoked. **Fix**: pair
every load-bearing skill with a `PreToolUse` hook that fails when
the skill's preconditions were not met (red tests, unsigned-off
design, missing acceptance table). Superpowers supplies the
prescription; Claude Code's hooks supply the enforcement. Neither
alone is a harness.
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
  - Superpowers, 2026-04 snapshot {cite}`vincent2025superpowersrepo`
* - License
  - MIT {cite}`vincent2025superpowers`
* - Control layer (CAR)
  - Strongly opinionated via ~30 prose skills.
* - Agency layer (CAR)
  - Unchanged from the host Claude Code installation.
* - Runtime layer (CAR)
  - Deferred to Claude Code; Superpowers does not ship a runtime.
* - SDD (mean)
  - 3.5
* - TDD (mean)
  - 3.0
* - MDD (mean)
  - 1.5
* - Primary citation
  - {cite}`vincent2025superpowers`
```

## Research Foundations

- **TDD** {cite}`beck2002tdd` — academic lineage of the TDD skill.
- **Debugging** {cite}`zeller2009whyprogramsfail` — lineage behind the
  systematic-debugging and receiving-code-review skills.
- **Code review** {cite}`bacchelli2013codereview` — the modern-code-review
  research that motivates the request / receive review skills.
- **Socratic design essays** {cite}`mills2015socratic` — philosophical
  backing for skills that ask the agent questions before letting it act.
- **Anthropic skills documentation** {cite}`anthropic2024skills` — the
  official format specification for `SKILL.md` files.

## Hands-On

Two copyable artefacts live under
`book/source/_handson/08-superpowers/`:

- `SKILL.md` — a drop-in skill readers can copy to
  `~/.claude/skills/spec-first-feature/SKILL.md`.
- `walkthrough.md` — an *install → invoke → observe* walkthrough
  verifying the skill fires end-to-end.
