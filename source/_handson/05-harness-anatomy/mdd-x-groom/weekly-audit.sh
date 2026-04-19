#!/usr/bin/env bash
# verified: 2026-04-17 · MDD × Groom · weekly audit that tends the metric surface
# Not "collect more metrics" — prune stale ones and verify the living ones
# still steer something.
set -euo pipefail

echo "== metrics retention =="
python scripts/audit_metrics.py --older-than 90d --action list-unused

echo "== dashboard coverage =="
python scripts/audit_dashboards.py --require-owner --require-runbook

echo "== cost trend =="
python scripts/cost_trend.py --since "$(date -d '7 days ago' +%F)"

echo "write the findings to metrics-review-$(date +%F).md and open a PR"
