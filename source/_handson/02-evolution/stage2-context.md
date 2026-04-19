# Stage 2 · Context Engineering

[... same task prompt as stage1-prompt.md ...]

### Project context (auto-attached by retrieval)

- `pyproject.toml` — click 8.x, pytest 8.x, python >= 3.11
- `todo_cli/storage.py` — existing `load()` / `save()` for `todos.json`
- `todo_cli/__init__.py` — CLI entrypoint, existing `list` and `done` subcommands
- house rule — every new subcommand gets a paired `tests/test_<cmd>.py`
