#!/usr/bin/env bash
# verified: 2026-04-17 · Ch.11 hands-on · reproduce the HarnessCard delta
# Run from a fresh clone of walterfan/async-harness-book at the Act-4 SHA.
set -euo pipefail

# 1. SDD × Fence — prompts-lint validates config/prompts.yaml
make prompts-lint

# 2. TDD × Fence — MCP tool schema-vs-handler consistency check
make mcp-schema-check

# 3. TDD × Fence — pre-commit hooks refuse secrets
make secrets-check

echo "If all three targets exited 0, the harness is at its Act-4 score."
