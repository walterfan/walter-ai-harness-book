<!-- verified: 2026-04-17 · MDD × Bridle · the one metric that steers -->

# Metrics North-Star

Pick exactly one metric that captures *fitness for purpose* of the harness
itself, then let every other metric be diagnostic of that one.

- **Project-level north-star:** **mean agent turns to green** on a fixed
  benchmark suite, measured weekly.
- **Why:** rising turns-to-green is the earliest observable signal that
  spec (SDD), tests (TDD), or tooling (MDD) has silently degraded.
- **Diagnostic metrics** (each tied to a guardian):
  - SDD — stale `verified:` header count, broken links in `AGENTS.md`
  - TDD — flaky-test count, coverage floor
  - MDD — cost per turn, prompt cache hit rate
