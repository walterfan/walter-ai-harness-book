# Stage 3 · Skill Engineering
```markdown
---
name: add-cli-subcommand
description: Add a new subcommand to the todo_cli click group
triggers: ["add a subcommand", "extend the CLI"]
---
1. Add the click command to `todo_cli/__init__.py`
2. Use `storage.load()` / `storage.save()` — do not touch JSON directly
3. Write `tests/test_<name>.py` with ≥ 2 cases (happy + error path)
4. Run `pytest -q` and stop if red
```
