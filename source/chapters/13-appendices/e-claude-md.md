---
status: draft
chapter-type: appendix
---

# Appendix E — Sample `CLAUDE.md` Template

This appendix consolidates the hands-on fragments from Chapters 03, 04,
05, and 06 (including the Tauri-Todo arc) into a single `CLAUDE.md` a
reader can drop directly into a fresh repository. Every block carries a
`<!-- origin: ..., zone: ..., guardian: ... -->` header comment so the
resulting file remains auditable against the twelve-cell matrix.

**Licensing.** The template below is published under MIT; copy, modify,
and redistribute without further acknowledgement. Citations are tracked
in `_bib/*.bib` and do not travel with the template itself; the CAR
HarnessCard schema {cite}`car2025decomposition` is the upstream
disclosure format it is designed to feed.

## The consolidated template

```markdown
# CLAUDE.md

<!-- origin: chapters/03-what-is-harness-engineering.md, zone: Bridle, guardian: SDD -->
## Role and scope
You are a coding agent for <project-name>. You may edit <allowed paths>.
You must not touch <forbidden paths>. Every new public function gets a
docstring and a test; no exceptions.

<!-- origin: chapters/04-three-guardians.md, zone: Bridle, guardian: SDD -->
## Spec discipline
Before editing any source file, read the matching spec under `specs/`
(or, if absent, `docs/adr/`). If the spec is older than the code by
more than 30 days, surface this as a risk and pause.

<!-- origin: chapters/04-three-guardians.md, zone: Bridle, guardian: TDD -->
## Test discipline
Before writing implementation code, locate or author the failing test
that captures the requirement. A commit that does not green one test
does not advance the project.

<!-- origin: chapters/04-three-guardians.md, zone: Bridle, guardian: MDD -->
## Metric discipline
Before merging any change that touches a user-facing path, confirm the
metrics north-star (`mean agent turns to green` on the fixed benchmark)
has not regressed.

<!-- origin: chapters/05-harness-anatomy.md · SDD × Paddock -->
## Acceptance Gate (Verification Table)

| # | Requirement                          | Checked by        |
|---|--------------------------------------|-------------------|
| 1 | Acceptance tests green               | Test Engineer     |
| 2 | `AGENTS.md` rules unchanged or versioned | Architect     |
| 3 | `CHANGELOG.md` entry under Unreleased | PO               |

<!-- origin: chapters/05-harness-anatomy.md · TDD × Fence -->
## Pre-edit hooks (Claude Code)

Install `.claude/hooks.json` as follows:

```json
{
  "hooks": {
    "PreToolUse": [
      {"matcher": "Write|Edit|MultiEdit",
       "command": "pytest -q -m 'not slow'",
       "stopOnFailure": true}
    ]
  }
}
```

<!-- origin: chapters/05-harness-anatomy.md · MDD × Fence -->
## Cost cap

A per-session cap of $2.00 and a monthly cap of $800.00 apply; breaches
refuse new tool calls until manual reset. The per-repo configuration
file lives at `.harness/cost-cap.yaml`.

<!-- origin: chapters/06-operating-a-harness.md · SDD × Groom -->
## Weekly groom schedule

Monday: run the entropy audit workflow; file issues for any new CVE,
stale `verified:` header, or broken link.
Friday: verify spec surface has no drift > 3 items; otherwise trigger a
mid-sprint re-spec.

<!-- origin: _handson/06-operating-a-harness/tauri-todo/, Bridle, SDD -->
## Tauri-Todo house rules (when the repo is a Tauri 2 app)

- Rust crate `src-tauri/` owns IPC, storage, and OS integration.
- TypeScript app in `src/` owns UI and input validation only.
- Never call OS APIs directly from TS; route through `invoke()`.
- Never add a dependency without `cargo audit` in the same commit.

<!-- origin: chapters/06-operating-a-harness.md · TDD × Fence + SDD × Fence -->
## Committed gates

A commit is only valid if, in order:
1. `pytest -q` passes.
2. `ruff check .` (or language-equivalent linter) passes.
3. `gitleaks` finds no secrets.
4. `make prompts-lint` (or equivalent spec validator) passes.
5. No `TODO` markers added without a matching issue link.

<!-- origin: chapters/13-appendices/d-harnesscard.md · meta -->
## HarnessCard self-disclosure

When you finish a non-trivial change, update `HarnessCard.md` at the
repo root and append a one-line entry to `HARNESSCARD-CHANGELOG.md`
naming which cell's score moved and by how much.
```

## Copy-paste note

The block above is MIT-licensed and intentionally text-only — no images,
no external fetches, no secrets. It is designed to be dropped into a
reader's repo as `CLAUDE.md` with no further editing required other
than substituting `<project-name>` and `<allowed paths>`.
