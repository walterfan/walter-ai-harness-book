<!-- verified: 2026-04-24 · Ch.12 hands-on · standalone checklist -->

# 30 / 60 / 90-Day Harness Checklist

Copy into your team wiki. Each bullet names a Ch.05 matrix cell and a
`_handson/` artefact pointer so the work can start the same day.

## Day 1–30 · One Cell

- [ ] **SDD × Bridle.** Run the `agents-md-generate` skill, then commit an `AGENTS.md` based on
      `_handson/05-harness-anatomy/sdd-x-bridle/AGENTS.md.sample`.
- [ ] **TDD × Fence.** Install a `PreToolUse` hook based on
      `_handson/05-harness-anatomy/tdd-x-fence/hooks.json`.
- [ ] **MDD × Fence.** Adopt a per-session cost cap from
      `_handson/05-harness-anatomy/mdd-x-fence/cost-cap.yaml`.

## Day 31–60 · One Row or One Column

- [ ] **Full SDD row.** Ship Bridle (`AGENTS.md.sample`), Fence
      (`prompt-schema.json`), Paddock (`acceptance-gate.md`), Groom
      (`update-docs.sh`). Artefacts under
      `_handson/05-harness-anatomy/sdd-x-*/`. In a monorepo, keep the
      root `AGENTS.md` global and add package-level files only where local
      commands or danger zones differ.
- [ ] **Full Fence column.** Ship SDD (`prompt-schema.json`), TDD
      (`hooks.json` + `ci-gate.yml`), MDD (`cost-cap.yaml`). Artefacts
      under `_handson/05-harness-anatomy/*-x-fence/`.
- [ ] **Operating drumbeat.** Adopt the weekly entropy audit from
      `_handson/06-operating-a-harness/entropy-audit.yml` and the
      artefact state model from
      `_handson/06-operating-a-harness/artefact-state-model.yaml`.

## Day 61–90 · A Production HarnessCard Review

- [ ] Use the blank HarnessCard template from Appendix D
      (`chapters/13-appendices/d-harnesscard.md`) to score one
      production codebase.
- [ ] Pick one cell to raise; land one measurable improvement from
      `_handson/11-lazy-ai-coder/reproduce.sh`-style `make` targets.
- [ ] Re-score; attach the second HarnessCard to the release note.
