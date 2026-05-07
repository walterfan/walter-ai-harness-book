# Agent Memory Groom Checklist

Use this checklist weekly for active agent projects, and before any release that
changes prompts, rules, tools, test commands, or architecture.

## Long-Term Memory

- [ ] Every durable rule points to a reviewable source: `AGENTS.md`, `SKILL.md`, ADR, PKB, runbook, or issue.
- [ ] Every best practice has a `memory_key`, `summary`, `source`, `verified_at`, `importance`, and `tags`.
- [ ] Every common pitfall names the failing behavior and the guardrail that should catch it next time.
- [ ] No long-term memory exists only in a vector index, database row, or chat transcript.
- [ ] Superseded rules are overwritten by key, not duplicated as natural-language variants.
- [ ] Stale long-term memories are marked stale or refreshed; they are not silently left as authority.

## Short-Term And Temp Memory

- [ ] Expired transient memories were deleted.
- [ ] Short-term memories older than the retention window were archived or pruned.
- [ ] High-importance short-term memories were promoted to long-term only after source review.
- [ ] Session-scoped memories are excluded from global prompt context.
- [ ] Short-term memories cannot outrank long-term rules during prompt assembly.

## Archive And Budget

- [ ] Archive rows are bounded by age, row count, and store size.
- [ ] Raw content is truncated or omitted when it exceeds the configured byte budget.
- [ ] Low-value embeddings are dropped before useful summaries are deleted.
- [ ] Active memory storage rolls over before it grows without bound.
- [ ] Historical stores remain searchable until pruning policy removes them.

## Privacy And Observability

- [ ] Logs contain operation names and record IDs, not raw memory text.
- [ ] Recall errors do not dump full memory blocks.
- [ ] Maintenance reports include counts, sizes, stale keys, and skipped protected long-term memories.
- [ ] A human owner can answer: "Which memory changed this agent's behavior this week?"

## Promotion Rule

Promote a memory to long-term only if it passes this sentence:

> Future agents should rely on this fact, rule, practice, or pitfall even when
> the current conversation is gone.

If that sentence feels too strong, keep the memory short-term.
