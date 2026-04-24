#!/usr/bin/env bash
# verified: 2026-04-24 · SDD × Groom · weekly agent-spec refresh job
# Refreshes living documentation so the spec surface the agent reads does
# not silently drift from the code it describes.
set -euo pipefail

make book-linkcheck || echo "::warning::broken links surfaced"

# Keep AGENTS.md small, current, and connected to real repo facts.
test -f AGENTS.md || { echo "::error::AGENTS.md missing"; exit 1; }
grep -q "last_updated" AGENTS.md || echo "::warning::AGENTS.md missing last_updated"
grep -Eq "pytest|npm test|go test|cargo test|make test" AGENTS.md \
  || echo "::warning::AGENTS.md lists no recognizable test command"

# Re-run the agents-md-generate skill after layout or command changes; commit
# the refreshed AGENTS.md only after reviewing the diff.
make book-lint
