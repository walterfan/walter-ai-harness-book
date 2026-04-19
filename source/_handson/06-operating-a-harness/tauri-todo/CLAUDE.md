<!-- verified: 2026-04-17 · Tauri-Todo worked arc · Bridle -->

# CLAUDE.md — lazy-todo-app (Tauri 2 + Rust + TypeScript)

## Project shape

- Rust crate `src-tauri/` owns IPC, storage, and OS integration.
- TypeScript app in `src/` owns UI and input validation only.
- Never call OS APIs directly from TS; route through `invoke()` to a
  Rust command.

## Agent rules

- Before editing any `.rs` file, read `tests/rust/` if it exists.
- Never add a dependency without `cargo audit` in the same commit.
- Storage writes must go through `src-tauri/src/storage.rs::save()`;
  direct disk writes elsewhere are rejected by `pre-commit`.

## House style

- `pnpm run fmt` before any commit; `cargo fmt && cargo clippy -- -D warnings` too.
- Errors cross the IPC boundary as `TauriError`, never as `Result<_, String>`.
