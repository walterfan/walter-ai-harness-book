<!-- verified: 2026-04-17 · MDD × Paddock · pre-release SLI gate -->

# Release SLI Gate

A release candidate is blocked from production until these SLIs meet their
targets for a rolling 24h window in staging:

| SLI                        | Target       | Window  |
|----------------------------|--------------|---------|
| p99 latency (user paths)   | ≤ 400 ms     | 24h     |
| error rate                 | ≤ 0.1 %      | 24h     |
| harness-internal cost/turn | ≤ $0.03      | 24h     |
| spec-vs-prod drift score   | ≤ 2 findings | 24h     |

The paddock is the rolling 24h staging run; crossing the gate requires all
four targets, not three-of-four.
