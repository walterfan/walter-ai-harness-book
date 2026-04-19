<!-- verified: 2026-04-17 · Ch.09 lazy-scrum-team hands-on · excerpted + attributed -->

# Role: Final Acceptance

*Excerpted from the lazy-scrum-team skill's `roles/acceptance-review.md`;
MIT-licensed; full definition in the skill repository.*

## Owns

- The transition from `review` → `approved` in the Artefact State Model.
- The HarnessCard delta annotation on the release PR.

## Produces

- Release note in `CHANGELOG.md`.
- HarnessCard score delta (one-line summary per cell change).

## Cannot

- Perform the review themselves; Code Review role does that.
- Waive Hard gates.

## Hand-off contract

Code Review → Final Acceptance: PR has ≥ 1 explicit approval and every
Hard gate green.
Final Acceptance → PO: rework artefact is `reject-reason.md` citing the
specific acceptance criterion that failed.
