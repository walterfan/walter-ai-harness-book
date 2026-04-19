<!-- verified: 2026-04-17 · Ch.08 Superpowers hands-on · install → invoke → observe -->

# Install → Invoke → Observe

## 1. Install

```bash
mkdir -p ~/.claude/skills/spec-first-feature
cp SKILL.md ~/.claude/skills/spec-first-feature/SKILL.md
```

## 2. Invoke

In Claude Code, start a fresh conversation in a repo that already has
`specs/`, `tests/`, and an `AGENTS.md`. Ask: *"use the spec-first-feature
skill to scaffold a 'dark-mode toggle' feature"*. The skill will be
auto-discovered and applied.

## 3. Observe

You should see, in order:

1. A message quoting the skill's `## When to use` block (the agent
   announces it is using the skill).
2. A `specs/dark-mode-toggle.md` file appearing under a new commit.
3. An updated `AGENTS.md` with a `dark-mode-toggle:` block.
4. A failing `tests/test_dark_mode_toggle.py`.
5. The agent *pausing* and asking whether to proceed with implementation.

If any of steps 1–5 are missing, the skill silently failed — open
`~/.claude/logs/` and look for the most recent skill-invocation block.
