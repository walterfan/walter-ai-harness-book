<!-- verified: 2026-04-24 · AGENTS.md fragment · minimal SDD Bridle -->

# AGENTS.md — todo-cli

`todo-cli` is a Python CLI for managing local todo items. This file is the
agent-facing entry point; client-specific files such as `CLAUDE.md` may link
back here for compatibility.

## Commands
- Before editing `todo/storage.py`, run `pytest tests/test_storage.py`.
- Before committing, run `pre-commit run --all-files`.

## Agent rules
- Edit only `todo/` and `tests/` unless the task explicitly expands scope.
- Every new subcommand gets a `--help` string and `tests/test_<cmd>.py`.
- Update `harnesscard.fragment.yaml` when adding or changing a guardian.

<!-- last_updated: 2026-04-24 -->
