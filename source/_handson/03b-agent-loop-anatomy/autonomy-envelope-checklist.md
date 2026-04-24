<!-- verified: 2026-04-24 · Ch.03B hands-on · autonomy envelope checklist -->

# Autonomy Envelope Checklist

Use this before asking an AI coding agent to complete a task with minimal
human correction.

- [ ] **Goal is testable.** The task has tests, screenshots, commands,
      metrics, or a review table that can decide done vs not done.
- [ ] **Boundaries are explicit.** Allowed and forbidden paths are listed in
      `AGENTS.md`, the issue, or the task contract.
- [ ] **Context is trustworthy.** Sources of truth are named; stale docs and
      deprecated paths are marked or blocked.
- [ ] **Tools are sufficient.** The agent can edit, inspect, test, and search
      what it needs.
- [ ] **Tools are not overpowered.** Production, secrets, deploys, and
      destructive commands require approval or are unavailable.
- [ ] **Failures stop the loop.** Red tests, schema mismatches, secret scans,
      and cost caps block further work.
- [ ] **Memory can be refreshed.** Long-term rules have an owner and a Groom
      cadence.
- [ ] **Final output includes evidence.** The agent must report changed files,
      commands run, results, and remaining risks.

If fewer than six boxes are checked, keep a human in the loop. If all eight
are checked, the task is inside the autonomy envelope.
