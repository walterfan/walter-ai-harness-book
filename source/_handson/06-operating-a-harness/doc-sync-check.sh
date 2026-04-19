#!/usr/bin/env bash
# verified: 2026-04-17 · entropy · refuse the merge when docs and code drift
set -euo pipefail

# Any source file touched in this MR that has a docstring-exposed API must
# also have been listed in the MR's doc-update checklist.
changed=$(git diff --name-only origin/main...HEAD)
undoc=$(python scripts/which_need_docs.py <<<"$changed" || true)
if [ -n "$undoc" ]; then
  echo "::error::the following changed files export public symbols but have no matching doc update:"
  echo "$undoc"
  exit 1
fi
