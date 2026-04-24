<!-- verified: 2026-04-24 · Ch.11 Act 1 · Audit HarnessCard -->

# HarnessCard — Act 1 (Audit)

**Subject.** `walterfan/async-harness-book`, starting commit SHA: `<TBD — captured when Act-3 fixes land>`.

**Date.** 2026-04-17 (pre-fix baseline).

**Schema version.** CAR-HarnessCard v0.2.

| Cell            | Score | Evidence                                      |
|-----------------|-------|-----------------------------------------------|
| SDD × Bridle    | 3     | `CLAUDE.md`, `AGENTS.md` exist but drift from `openspec/`. |
| SDD × Fence     | 1     | No `make prompts-lint`; `config/prompts.yaml` unchecked.  |
| SDD × Paddock   | 2     | Review is GitHub PR default; no Verification Table.       |
| SDD × Groom     | 1     | No sources-of-truth index; docs drift silently.           |
| TDD × Bridle    | 2     | `tests/` exists but not failing-first.                    |
| TDD × Fence     | 1     | No MCP tool schema check; no secrets scan in pre-commit.  |
| TDD × Paddock   | 3     | GitHub Actions CI runs `go test` + Python tests.          |
| TDD × Groom     | 2     | Flake policy undefined; recent flakes closed ad-hoc.      |
| MDD × Bridle    | 1     | No cost dashboard; LLM spend unobservable.                |
| MDD × Fence     | 2     | Rate limits at provider only; no local cap.               |
| MDD × Paddock   | 2     | Release notes exist; no SLI gate.                         |
| MDD × Groom     | 1     | No weekly audit script.                                   |

**SDD mean.** 1.75.  **TDD mean.** 2.0.  **MDD mean.** 1.5.

**Overall.** 1.75. This is the pre-fix baseline; Act 4 re-scores after
the 14 fixes land.
