<!-- verified: 2026-04-17 · approval gates · Hard vs Soft classification -->

# Hard vs Soft Gates

Every gate must declare its class at creation time. Misclassification is
the leading cause of gate evaporation.

| Gate kind       | Example                          | Class | Bypass policy                       |
|-----------------|----------------------------------|-------|-------------------------------------|
| unit-test suite | `pytest -q`                      | Hard  | never bypass; fix test or revert     |
| lint            | `ruff check .`                   | Hard  | never bypass for new code            |
| coverage floor  | `coverage >= 80%`                | Soft  | waivable by Architect + reason       |
| cost cap        | `cost/turn ≤ $0.03`              | Soft  | waivable for 24h by MDD owner        |
| secrets scan    | `gitleaks`                       | Hard  | never bypass; rotate the secret      |
| docs link-check | `make book-linkcheck`            | Soft  | waivable if external site is down    |

Soft-gate waivers get a `waiver: <role>, <expiry>` entry in the PR body.
