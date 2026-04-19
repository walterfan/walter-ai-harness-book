<!-- verified: 2026-04-17 · tool-versions: claude-code 0.9.x · pre-commit 3.7.x -->

# Hands-On · §03.4 Minimal Harness

Three fragments, ~10 lines each. Read in order:

1. `claude-md.fragment.md` — the **specification** an AI agent reads before it writes code.
2. `pre-commit-config.fragment.yaml` — the **fence** that blocks bad commits regardless of who authors them.
3. `harnesscard.fragment.yaml` — the **observability receipt** a team publishes so outsiders can audit the harness.

Together, these three files compose the smallest possible harness: one
specification (SDD), one gate (TDD), one metric surface (MDD). A solo
developer can ship this in an afternoon.
