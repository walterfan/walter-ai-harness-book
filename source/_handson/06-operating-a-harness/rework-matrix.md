<!-- verified: 2026-04-17 · approval gates · who sends what back to whom -->

# Rework Matrix

Rows are *who found the defect*, columns are *who must fix it*. Each cell
names the artefact that makes the hand-off explicit.

|               | PO (spec) | Architect (design) | Dev (code) | Test (acceptance) |
|---------------|-----------|--------------------|------------|-------------------|
| **PO**        | —         | `spec-delta.md`    | —          | `acceptance.md`   |
| **Architect** | —         | —                  | `adr-rework.md` | —             |
| **Dev**       | `spec-question.md` | —         | —          | —                 |
| **Test**      | `acceptance-gap.md` | —        | `bug-report.md` | —            |
| **Final Acc** | `reject-reason.md` | `reject-reason.md` | `reject-reason.md` | — |

A defect never crosses this matrix without a rework artefact attached;
"just fix it" is an anti-pattern.
