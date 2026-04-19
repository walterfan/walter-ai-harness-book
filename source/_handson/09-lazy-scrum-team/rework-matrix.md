<!-- verified: 2026-04-17 · Ch.09 lazy-scrum-team hands-on · adaptable version -->

# Rework Matrix (adaptable)

Copy this file into your own repo under `docs/rework/README.md`. Adjust
the row/column set to your team's role cast; the *shape* — finder × fixer,
with a named rework artefact per cell — is what matters.

|               | PO       | Architect | Developer | Test Engineer | Final Acceptance |
|---------------|----------|-----------|-----------|---------------|------------------|
| **PO**        | —        | `spec-delta.md`   | —                | `acceptance.md`        | —                          |
| **Architect** | —        | —                 | `adr-rework.md`  | —                      | —                          |
| **Developer** | `spec-question.md` | —       | —                | —                      | —                          |
| **Test**      | `acceptance-gap.md` | —      | `bug-report.md`  | —                      | —                          |
| **Final Acc** | `reject-reason.md` | `reject-reason.md` | `reject-reason.md` | `reject-reason.md` | —                     |

Rule: no defect crosses a hand-off without a rework artefact attached.
"Just fix it" is an anti-pattern that burns institutional memory.
