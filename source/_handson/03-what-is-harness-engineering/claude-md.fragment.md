<!-- verified: 2026-04-17 · CLAUDE.md fragment · 10 lines -->

# Project: todo-cli

**Language:** Python 3.11 · **Entry point:** `todo/__main__.py` · **Tests:** `pytest`

## House rules for the agent

- Never edit `todo/storage.py` without first running `pytest tests/test_storage.py`.
- Every new subcommand gets (a) a `--help` string, (b) a `tests/test_<cmd>.py` fixture.
- Commits must pass `pre-commit run --all-files`; see `pre-commit-config.fragment.yaml`.
- Observability contract lives in `harnesscard.fragment.yaml`; update it when adding a guardian.
