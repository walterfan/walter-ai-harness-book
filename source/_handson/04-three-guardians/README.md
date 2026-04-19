<!-- verified: 2026-04-17 · tool-versions: pytest 8.x · python 3.11 -->

# Hands-On · Ch.04 Three Guardians

One artefact per guardian, in the causal order the chapter argues for:

1. `AGENTS.md.fragment` — **SDD (Specification)**: a machine-checkable spec
   block the agent reads *before* it writes any code. Specification shapes
   what the agent tries to build.
2. `tests/test_skeleton.py` — **TDD (Tests)**: a failing test written
   *before* a prompt is sent. Tests verify what the agent actually built.
3. `metrics.yaml` — **MDD (Metrics)**: a minimal signal contract the team
   reviews weekly. Metrics confirm the build keeps working.

The three files are designed to be copied into any repo as a starter
harness. They are sequenced so a reader can ship them in one afternoon —
spec first, one failing test second, one metrics file third — and have a
primitive but real three-guardian loop.
