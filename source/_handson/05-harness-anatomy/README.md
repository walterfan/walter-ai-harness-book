<!-- verified: 2026-04-17 -->

# Hands-On · Ch.05 Harness Anatomy

Twelve artefacts, one per cell of the 3×4 matrix. The directory layout
mirrors the matrix: `<guardian>-x-<zone>/<filename>`. Each file is
self-contained (no required imports beyond the file itself), sized to be
readable in under two minutes, and carries a `verified: YYYY-MM-DD` header
comment.

```
sdd-x-bridle/AGENTS.md.sample
sdd-x-fence/prompt-schema.json
sdd-x-paddock/acceptance-gate.md
sdd-x-groom/update-docs.sh
tdd-x-bridle/starter-tests/test_loop.py
tdd-x-fence/hooks.json
tdd-x-paddock/ci-gate.yml
tdd-x-groom/flaky-test-quarantine.md
mdd-x-bridle/metrics-north-star.md
mdd-x-fence/cost-cap.yaml
mdd-x-paddock/release-sli.md
mdd-x-groom/weekly-audit.sh
```

Each artefact is referenced by its cell's H3 subsection in
`chapters/05-harness-anatomy.md` via a `{literalinclude}`.
