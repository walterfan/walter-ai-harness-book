<!-- verified: 2026-04-17 · SDD × Paddock · Verification Table pattern from lazy-scrum-team -->

# Acceptance Gate — Verification Table

A story is `done` only when every row below is checked by the named role.

| # | Requirement                          | Evidence (file or URL)       | Checked by        |
|---|--------------------------------------|------------------------------|-------------------|
| 1 | Acceptance tests green               | CI run link                  | Test Engineer     |
| 2 | `AGENTS.md` rules unchanged or versioned | `git diff` summary       | Architect         |
| 3 | `CHANGELOG.md` entry under Unreleased | diff hunk                   | PO                |
| 4 | No new TODO/FIXME markers added      | `rg -c TODO` before/after    | Code Reviewer     |
| 5 | HarnessCard cell score unchanged or explained | HarnessCard delta note | Final Acceptance  |

Rows may only be marked by the named role; self-certification is rejected.
