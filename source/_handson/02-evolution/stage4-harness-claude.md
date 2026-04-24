# Stage 4 · Harness Engineering
```markdown
# AGENTS.md  (fragment)
## Skills
- `add-cli-subcommand` — for any CLI extension
## Fences (pre-commit)
- ruff check, pytest -q, mypy --strict
## Hooks (PostToolUse)
- after every Edit: run `pytest -q tests/test_<touched-cmd>.py`
```
