# Hands-On: Four Stages on One Task

> verified: 2026-04-17 / tool-version: claude-code 2.0 / cursor 1.3

The same tiny task — *add a `todo add <title>` command to a Python CLI* —
solved four ways, one per stage. Read the files in order:

1. `stage1-prompt.md`       — zero-shot prompt, Prompt Engineering style
2. `stage2-context.md`      — same prompt, now fed with project context
3. `stage3-skill.md`        — a `SKILL.md` excerpt that encodes the workflow
4. `stage4-harness-claude.md` — a `CLAUDE.md` fragment that wires skills,
   lint, hooks, and pre-commit into one coherent harness

Total artefact budget: ≤ 40 lines across the four files. The progression
shows how the author's effort moves — from **writing a clever prompt** to
**shaping an environment the agent cannot leave unshaped**.
