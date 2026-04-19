<!-- verified: 2026-04-17 · Ch.11 hands-on -->

# Hands-On · Ch.11 Lazy AI Coder

Four files tracking the four-act worked example:

- `HarnessCard-Act1.md` — Act 1 baseline audit.
- `HarnessCard-Act4.md` — Act 4 post-fix re-audit with delta.
- `reproduce.sh` — run `make prompts-lint`, `make mcp-schema-check`,
  `make secrets-check` against a fresh clone at the Act-4 SHA.
- `pre-commit-config.yaml` — the symlink-safe copy of the final
  pre-commit baseline landed under §14.4.

The chapter stays `status: draft` until the §14 commits land on `main`;
once they do, the HarnessCards are re-scored and the chapter flips to
`status: complete` per §14.5.
