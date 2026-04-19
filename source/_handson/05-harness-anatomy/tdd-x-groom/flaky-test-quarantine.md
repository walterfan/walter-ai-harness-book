<!-- verified: 2026-04-17 · TDD × Groom · flaky-test quarantine policy -->

# Flaky Test Quarantine

A test that fails intermittently without a code change enters quarantine:

1. Move it from `tests/` into `tests/quarantine/`; mark with `@pytest.mark.flaky`.
2. Open an issue tagged `quarantine` with the last three failure logs.
3. CI runs `tests/quarantine/` separately; failures post a comment but do
   not block the merge.
4. If the quarantined test is green for 7 consecutive nightly runs, promote
   it back into `tests/`; if red for 30 days, delete with an explicit
   justification in the commit message.

Quarantine is a paddock *inside* the paddock: a space where flakes cannot
poison the main gate while still being tracked.
