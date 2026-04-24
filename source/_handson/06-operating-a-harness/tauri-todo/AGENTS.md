<!-- verified: 2026-04-17 · Tauri-Todo worked arc · Role contracts (Paddock + Groom) -->

# AGENTS.md — canonical agent contract for lazy-todo-app

This is the canonical agent-facing contract. `CLAUDE.md` mirrors the
Claude-specific Bridle rules for clients that still look there first.

## Roles

- **PO** — owns `specs/*.md`; signs off feature intent before dev starts.
- **Architect** — owns `src-tauri/src/storage.rs` + ADRs under `docs/adr/`.
- **Developer** — implements against tests; never modifies signed ADRs.
- **Reviewer** — runs `hard-vs-soft-gates.md`; cannot self-approve.
- **MDD Owner** — maintains the HarnessCard at repo root; runs the weekly audit.

## Gate contract (Paddock)

A PR is mergeable when:

1. All Hard gates (see `../hard-vs-soft-gates.md`) pass.
2. Soft gates pass OR carry a dated waiver.
3. Reviewer has ticked every row of `acceptance-gate.md`.

## Groom contract

- Monday: MDD Owner runs `../entropy-audit.yml` and opens issues for any
  delta vs last week's report.
- Friday: Architect reviews drift between `specs/` and implemented code;
  if drift > 3 items, triggers a mid-sprint re-spec.
