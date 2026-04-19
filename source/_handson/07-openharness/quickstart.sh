#!/usr/bin/env bash
# verified: 2026-04-17 · Ch.07 OpenHarness hands-on · clone → install → first oh session
set -euo pipefail

# 1. clone the reference implementation
git clone https://github.com/HKUDS/OpenHarness.git oh && cd oh

# 2. install (editable) into a fresh venv
python -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"

# 3. configure a minimum-viable session
cp examples/config.yaml.example config.yaml
echo "export OPENAI_API_KEY=${OPENAI_API_KEY:-sk-...}" >> .env

# 4. run a single oh session; the prompt below asks for a trivial diff so
#    the wiring is verified without burning tokens.
oh session run --prompt "list the files in src/ and print the first line of each"
