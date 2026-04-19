<!-- verified: 2026-04-17 · Ch.09 lazy-scrum-team hands-on · excerpted + attributed -->

# Role: Product Owner (PO)

*Excerpted from the lazy-scrum-team skill's `roles/po.md`; MIT-licensed;
see the skill repository for the full role definition.*

## Owns

- `specs/*.md` — every feature starts here.
- `CHANGELOG.md` Unreleased section.
- Backlog ordering.

## Produces

- Feature spec with three explicit acceptance criteria.
- Sign-off on the Verification Table (see `acceptance-gate.md`).

## Cannot

- Write production code.
- Approve a PR (Final Acceptance role owns that).

## Hand-off contract

PO → Architect: spec is `approved` in the Artefact State Model.
Architect → PO: rework artefact is `spec-question.md` under
`docs/rework/<sprint>/`.
