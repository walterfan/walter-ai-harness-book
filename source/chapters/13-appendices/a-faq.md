---
status: draft
chapter-type: appendix
---

# Appendix A — Frequently Asked Questions

Questions are grouped by reader role. Answers are ≤ 150 words; roughly
one-third carry a `{ref}` link back into the book body so a curious
reader can drop into the canonical section.

## For Individual Engineers

### Do I need to adopt all three guardians at once?

No — Chapter 12's 30/60/90 checklist is explicit that a team ships *one
cell in thirty days, one row or column in sixty*. SDD × Bridle is the
usual starting point because `AGENTS.md` is cheap to author and pays off
every single turn thereafter. See {ref}`sdd-x-bridle` for the canonical
artefact. If you are working alone, TDD × Fence is a defensible
alternative: a single `PreToolUse` hook that refuses edits while the
test tree is red gives you immediate daily leverage.

### How is this different from my existing CI pipeline?

CI is the *Paddock* of TDD and MDD. This book argues that Paddock alone
is insufficient — the Bridle steers before the CI ever runs, the Fence
fires at keystroke rather than merge, and the Groom tends the gates
themselves. If your CI pipeline catches bugs on Friday evening that
could have been caught at commit time on Tuesday morning, your Fence
column is underinvested.

### What if my team uses Cursor, not Claude Code?

The twelve-cell matrix is platform-agnostic. Cursor supports
`AGENTS.md`, `.cursor/rules/`, and hooks; the mapping from the Ch.05
artefacts is almost mechanical. The one exception is the `SKILL.md`
format, which is Claude-Code-specific as of 2026-04; Cursor users
replace it with their own `.cursor/rules/` files of comparable scope.

### I already write tests. Isn't that TDD enough?

Having tests is necessary but not sufficient; TDD × Bridle requires the
tests to be *failing-first and visible to the agent as input*. See
{ref}`tdd-x-bridle`. If your tests were written after the feature was
merged, they contribute to TDD × Paddock at best and almost nothing to
TDD × Bridle.

## For Team Leads

### How do I convince my team to invest in SDD before shipping?

Run one worked example: score your current repo against the Appendix D
blank template (see {ref}`apd-harnesscard-template`), name the
lowest-scoring cell, ship one artefact for it, re-score. A +2 delta on
a single cell is visible enough to justify the next iteration. Chapter
11 is the canonical example of this pattern.

### How does this interact with DORA metrics?

DORA measures outcomes; HarnessCards measure *inputs to those outcomes*.
A rising `deployment frequency` or falling `change failure rate` is the
downstream effect of a well-tended harness. Tracking both lets you tell
"the harness is working" apart from "we happened to get lucky". See
§12.2 Day 61-90 for the rubric that ties HarnessCards to production
SLIs.

### What is the minimum review ritual my team needs?

One role-scoped Verification Table per PR, as per {ref}`sdd-x-paddock`,
and one explicit Hard-vs-Soft gate classification for the CI pipeline.
These two artefacts together cost roughly one hour per week to maintain
and eliminate the most common failure mode — silent rework that never
feeds back into the spec.

### How do we handle pushback from engineers who see this as overhead?

Ask them to run the exercise in §12.2 Day 1-30 for one week. If the
single-cell ship produces zero measurable benefit, the experiment is
over and you have learned something. The book's empirical bet — grounded
in Peng et al. {cite}`peng2023copilotstudy` and Ziegler et al.
{cite}`ziegler2022productivity` — is that one cell at one week will
move a measurable productivity metric by the end of month one.

### How do we tell harness work from harness theatre?

One diagnostic, asked every Monday: *what did the harness refuse,
measure, or steer this past week, and was it right to do so?* A
healthy harness produces a concrete answer — a commit it blocked,
a tool call it caught, a dashboard signal it crossed. A theatrical
harness produces a list of *additions* ("we wrote a new skill",
"we added a hook") with no corresponding events. If the team can
only answer the additions question, the harness is growing but not
leveraging. Glossary entry *Harness Theatre* enumerates the common
subtypes; the Ch.06 closing note gives the canonical diagnostic.

### Our HarnessCard scores keep rising but nothing downstream moves. Why?

The vanity-delta pattern Chapter 11 names explicitly. The HarnessCard
is a *diagnostic* rubric — its role is to identify weak cells, not to
be optimised against. When cell scores rise but DORA metrics don't
follow, the team is paying down debt that was not costing anything.
**Fix**: pair every planned HarnessCard delta with one outcome metric
it is *predicted* to move (deployment frequency, change failure rate,
incident count). If the outcome does not move after a quarter, the
previous quarter's investment was vanity, and next quarter's
investment should target a different cell — or ask whether the
product is bottlenecked by something other than the harness entirely.

## For Skeptics

### Isn't this just rebranded DevOps?

DevOps packages CI/CD, infra-as-code, and deployment automation; this
book argues that agent-era software engineering needs a vocabulary
*upstream* of those practices — the Bridle steers before the CI runs,
the SDD guardian shapes the spec before the code is written. Chapter
03's comparison table lays out the boundary explicitly. DevOps remains
necessary and is not replaced by harness work.

### Isn't this just prompt engineering?

Prompt engineering is one cell (SDD × Bridle). The other eleven cells —
fences, paddocks, grooms, TDD, MDD — are irreducible to prompt
authorship. Karpathy's context-engineering framing
{cite}`karpathy2025context` is a step beyond prompt engineering; the
three-guardian × four-zone matrix is a step beyond that.

### You cite the author's own blog a lot. Isn't that a red flag?

The four-zone naming is explicitly acknowledged as practitioner-origin
in §05.Provenance; the academic grounding is the CAR / HarnessCard
paper {cite}`car2025decomposition` and the five industrial
triangulation sources listed throughout. The book never hides that the
naming is the author's; what it does is triangulate against three
independently-developed adjacent frameworks.

### How do I know this will still be relevant in 2027?

Short answer: you do not. The book's 30-day, 60-day, 90-day structure
assumes that *specific artefacts* will age out faster than the
*framework* itself. Lehman's evolution laws {cite}`lehman1980laws`
apply to the book as much as to any codebase; §12.3 names the open
questions whose resolution will most likely drive a second edition.

### My agent passes every check and still ships wrong code. What gives?

Three possibilities, in descending frequency. First, **test-pinning**:
the tests pass because the agent landed on one of many interpretations
consistent with them; the interpretation the human wanted was never
pinned down (Ch.04). Fix by adding adversarial tests that attack the
cheapest path to green. Second, **spec drift**: the agent is
conforming to `AGENTS.md` while the codebase has silently evolved
away from it (Ch.04). Fix by scheduling a weekly spec-vs-code diff.
Third, **ambiguity amplification**: one vague bullet in the spec is
producing wildly different but all-locally-correct implementations
(Ch.04). Fix by tightening that bullet until a hook can check it.
All three are visible in the glossary; all three are inline pitfalls
in Ch.04.

## For Chinese-Context Readers

### Why are the examples English when my codebase is Chinese?

Code artefacts (YAML, JSON Schema, shell scripts) are generally
language-neutral and copy verbatim. The prose chapters (`AGENTS.md`,
`CLAUDE.md`) benefit from matching your team's working language. The
book ships with a Simplified-Chinese translation of the Foreword, Ch.03,
Ch.04, Ch.05, and Ch.12 for exactly this reason; the language switcher
in the top-left of every page toggles between the two.

### How does《马书》 relate to this book?

《马书》 {cite}`zhangbook2026` is an excellent reverse-engineering
study of Claude Code specifically. Chapter 10 cites it extensively and
is the only chapter that does. This book sits one level up: it builds
a *framework* for scoring harnesses in general, of which Claude Code is
one instance among several.

### Do I need to read the book in order?

No. If you know the guardians already, start with Chapter 05 (the
matrix), then jump to whichever case study (07–10) covers the harness
closest to your day-to-day, then come back to Chapter 11 for the
lazy-ai-coder worked example. The Foreword and Chapter 02 are useful
background but are not prerequisites for the matrix.

### What Chinese-language resources do you recommend?

《马书》 for Claude Code specifically {cite}`zhangbook2026`; the author's
2026-03-28 blog post for the original four-zone essay
{cite}`walterfan2026guardians`; Appendix C for a broader reading list.

## About the Book Itself

### Why Sphinx instead of mdBook?

Three reasons: native `sphinx-intl` support for bilingual publishing,
`sphinxcontrib-bibtex` for first-class academic citations, and the MyST
directive ecosystem for `{literalinclude}` from hands-on artefacts. A
team with different priorities might reasonably choose mdBook; the
colophon carries the full rationale.

### Why is Chapter 11 in draft status?

Chapter 11 ships `status: draft` until Section 14's four commits land on
the host repository's `main`. The book-lint script walks the Act 3
commit SHAs through `git cat-file -e`; until at least two resolve, the
chapter is excluded from the toctree. See §14 for the current landing
schedule.

### How do I contribute?

See `book/CONTRIBUTING.md` in the source repository. Short summary:
new citations go into the `_bib/*.bib` file matching their kind; new
hands-on artefacts go under `_handson/<chapter-slug>/` with a
`verified: YYYY-MM-DD` header comment; new matrix cells require an
extension to `book_lint.py` to enforce the citation-plus-artefact rule.

### What licence is the book under?

Prose is CC-BY-SA-4.0, code samples are MIT, and quoted excerpts preserve
their upstream licence. See `book/LICENSE` for the complete text.
