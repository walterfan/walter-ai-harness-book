#!/usr/bin/env bash
# verified: 2026-04-17 · SDD × Groom · weekly doc-sync job
# Refreshes living documentation so the spec surface the agent reads does
# not silently drift from the code it describes.
set -euo pipefail

make book-linkcheck || echo "::warning::broken links surfaced"

# regenerate AGENTS.md TOC from source chapters
python scripts/gen_agents_toc.py > AGENTS.md.next
diff -u AGENTS.md AGENTS.md.next && rm AGENTS.md.next \
  || { mv AGENTS.md.next AGENTS.md; git add AGENTS.md; }

# re-stamp `verified:` headers in _handson/ artefacts modified this week
python scripts/restamp_verified.py book/source/_handson
