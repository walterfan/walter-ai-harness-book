<!-- verified: 2026-04-17 · Ch.11 Act 4 · Measuring the Delta -->

# HarnessCard — Act 4 (Post-fix)

**Subject.** `walterfan/lazy-ai-coder`, end-of-Act-3 commit SHA:
`<TBD — captured at §14 landing>`.

**Date.** 2026-04-17 (post-fix, to be re-verified at §14 landing).

**Schema version.** CAR-HarnessCard v0.2.

| Cell            | Act 1 | Act 4 | Delta | Fix                                   |
|-----------------|-------|-------|-------|---------------------------------------|
| SDD × Bridle    | 3     | 3     | 0     | (unchanged in §14 scope)              |
| SDD × Fence     | 1     | 4     | +3    | `make prompts-lint` + schema validator |
| SDD × Paddock   | 2     | 2     | 0     | (unchanged)                           |
| SDD × Groom     | 1     | 3     | +2    | `openspec/docs/sources-of-truth.md` index |
| TDD × Bridle    | 2     | 2     | 0     | (unchanged)                           |
| TDD × Fence     | 1     | 4     | +3    | MCP schema check + gitleaks pre-commit |
| TDD × Paddock   | 3     | 3     | 0     | (unchanged)                           |
| TDD × Groom     | 2     | 2     | 0     | (unchanged)                           |
| MDD × Bridle    | 1     | 1     | 0     | (out of §14 scope)                    |
| MDD × Fence     | 2     | 2     | 0     | (unchanged)                           |
| MDD × Paddock   | 2     | 2     | 0     | (unchanged)                           |
| MDD × Groom     | 1     | 1     | 0     | (unchanged)                           |

**SDD mean.** 1.75 → 3.0 (+1.25).
**TDD mean.** 2.0 → 2.75 (+0.75).
**MDD mean.** 1.5 → 1.5 (+0.0).
**Overall.** 1.75 → 2.42 (+0.67).

## Quantitative metrics

| Metric                       | Act 1 | Act 4 | Delta |
|------------------------------|-------|-------|-------|
| prompts-lint rule count      | 0     | 7     | +7    |
| MCP schema mismatches at CI  | N/A   | 0     | —     |
| secrets-scan coverage (% committed files) | 0     | 100   | +100  |
| `sources-of-truth.md` entries | 0     | ≥ 6   | +6    |
