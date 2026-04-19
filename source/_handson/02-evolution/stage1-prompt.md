# Stage 1 · Prompt Engineering

Write a Python CLI that accepts `todo add <title>` and appends the title
to `todos.json` with a UUID, created-at timestamp, and `done: false`.
Use `click` for argument parsing. Keep it under 30 lines. Handle the
file-missing case. Output the new entry as JSON to stdout.
