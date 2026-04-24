<!-- verified: 2026-04-24 · tool-versions: agents.md 2025 · pre-commit 3.7.x -->

# 动手环节 · 03.4 最小马具

Three fragments, ~10 lines each. Read in order:

1. `agents-md.fragment.md` — the **specification** an AI agent reads before it writes code.
2. `pre-commit-config.fragment.yaml` — the **fence** that blocks bad commits regardless of who authors them.
3. `harnesscard.fragment.yaml` — the **observability receipt** a team publishes so outsiders can audit the harness.

Together, these three files compose the smallest possible harness: one
specification (SDD), one gate (TDD), one metric surface (MDD). A solo
developer can ship this in an afternoon. Use `AGENTS.md` as the canonical
entry file; if a client still expects `CLAUDE.md`, keep it as a symlink or
thin mirror.
