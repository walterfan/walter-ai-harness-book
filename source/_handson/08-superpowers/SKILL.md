<!-- verified: 2026-04-17 · Ch.08 Superpowers hands-on · drop-in SKILL.md -->
---
name: spec-first-feature
description: Use when starting any new feature. Writes the AGENTS.md spec block and failing acceptance test before any implementation code.
---

# Spec-First Feature

## When to use

You're starting a new feature and want the harness (SDD × Bridle + TDD ×
Bridle) engaged *before* you write a single line of implementation.

## What it does (in order)

1. Creates or extends `specs/<feature-slug>.md` with a ≤ 150-word feature
   description and three acceptance criteria.
2. Appends a role-scoped block to `AGENTS.md` declaring which files this
   feature may touch.
3. Writes one failing pytest in `tests/test_<slug>.py` that encodes the
   first acceptance criterion.
4. Only *then* invites the author (human or agent) to implement.

## Red flags that would stop this skill

- `specs/` directory does not exist; refuse and explain.
- `tests/` missing a `conftest.py`; surface and ask.
- There is already a `specs/<feature-slug>.md`; ask whether to overwrite.
