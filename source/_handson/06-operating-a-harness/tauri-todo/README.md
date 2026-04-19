<!-- verified: 2026-04-17 · Tauri-Todo worked arc -->

# Tauri-Todo Hands-On

A minimal end-to-end harness for a real Tauri 2 + Rust + TypeScript
desktop-todo project. The three files in this directory —
`CLAUDE.md`, `pre-commit-config.yaml`, `AGENTS.md` — stitch the four
operating concerns from Ch.06 into one working story:

- Bridle — `CLAUDE.md` steers the agent before it writes.
- Fence — `pre-commit-config.yaml` refuses bad commits regardless of
  author.
- Paddock + Groom — `AGENTS.md` names the role cast, the gate contract,
  and the weekly Groom schedule.

The runnable companion repository is at **`walterfan/lazy-todo-app`**.
This hands-on directory ships only the three harness fragments; the repo
holds the full Tauri app, a working CI, and the history of HarnessCard
deltas across its first ten tagged releases.
