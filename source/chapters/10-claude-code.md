---
status: draft
chapter-type: case-study
case-study-kind: closed-source
---

# Case Study: Claude Code via《马书》

> *The only closed-source case study in this book. Read it knowing that.*

## Reverse-Engineering Disclaimer

The Claude Code product is closed source. This chapter's analysis
relies on three evidence classes, in descending order of authority:

1. **Anthropic's official public documentation and launch post**
   {cite}`anthropic2024claudecode` and the MCP specification
   {cite}`anthropic2024mcp` — primary authority.
2. **Observed runtime behaviour** of the Claude Code CLI across the
   2026-03 through 2026-04 observation window on macOS and Linux,
   captured in author session logs.
3. **Zhang Handong's《马书》 2026 reverse-engineering analysis**
   {cite}`zhangbook2026` — hereafter *Ma's book* — a publicly
   available Chinese-language study of Claude Code's bundled prompt,
   skill library, hooks contract, and tool schemas.

**Observation window.** All claims below reflect Claude Code's
behaviour between **2026-03-01 and 2026-04-15**. Behaviour outside this
window is not guaranteed to match.

**Retraction commitment.** If Anthropic publishes official documentation
or makes a public statement that contradicts any claim below, this
chapter will be updated within 30 days and the retracted claim will be
struck through with a dated note explaining the change. The book treats
reverse-engineered observation as *provisional*, not authoritative.

**Licensing.** Neither《马书》 nor Claude Code's internal bundle is
reproduced verbatim in this chapter beyond the standard fair-use excerpt
limit of ≤ 20 lines per quoted passage, with attribution to《马书》's
page numbers where applicable.

## §10.1 — Reading Claude Code through the matrix

Claude Code, as observed and as described by《马书》, distributes
harness responsibility across three overlapping surfaces:

- **The bundled system prompt** (Bridle, primarily SDD) — a multi-kilobyte
  document that《马书》 reproduces and annotates across several chapters;
  it includes role framing, tool-use heuristics, citation formatting
  rules, and explicit red-flag self-questions.
- **The hooks contract** (Fence, spanning TDD and MDD) — `hooks.json`
  under `.claude/` supports `PreToolUse`, `PostToolUse`, `SessionEnd`,
  and `UserPromptSubmit` matchers; a non-zero exit code from a
  `PreToolUse` hook refuses the tool call.
- **The skills system** (Bridle + Paddock, mostly SDD) — `SKILL.md`
  files under `~/.claude/skills/` the agent auto-discovers and invokes
  based on the `description:` front-matter.

A compact excerpt from《马书》's observation of the bundled prompt
(original is Chinese; translation is the author's own for exposition):

```text
[Excerpt, ≤ 20 lines, translated from《马书》 Chapter 4, §4.2, p. 113]

System message tail:
    - When asked a factual question, cite at least one source.
    - When writing code, prefer edits over creation.
    - Never include a generated-by-AI signature in the output.
    - If a skill applies, read and follow it before answering.
    - Treat user files as authoritative; do not overwrite without confirmation.
```

《马书》 argues — and observed behaviour corroborates — that these
tail-of-prompt rules are the single most load-bearing SDD × Bridle
artefact in the product.

## §10.2 — 12-cell highlight map with confidence bands

Every cell below carries a confidence band: `observed` (directly
verifiable in runtime behaviour), `inferred` (derived from《马书》 +
official docs + observation triangulated), or `speculative` (best-guess
that future disclosure could promote or retract).

```{list-table}
:header-rows: 1
:widths: 18 6 16 60

* - Cell
  - Score
  - Confidence
  - Evidence and what would change the band
* - SDD × Bridle
  - 5
  - observed
  - Bundled prompt + skills system directly shape every turn; corroborated by《马书》 Ch.~4 {cite}`zhangbook2026` and Anthropic docs {cite}`anthropic2024claudecode`.
* - SDD × Fence
  - 3
  - inferred
  - Front-matter schema for `SKILL.md` is undocumented; skills with malformed YAML are silently skipped.《马书》 Ch.~5 reproduces the parser's tolerant mode.
* - SDD × Paddock
  - 3
  - inferred
  - No built-in acceptance ritual; review discipline is delegated to the host team.
* - SDD × Groom
  - 3
  - inferred
  - `/cost`, `/status`, `/clear` slash commands support grooming but cadence is operator-owned.
* - TDD × Bridle
  - 3
  - inferred
  - Test-first framing is encouraged by default skills and《马书》 Ch.~6 but not enforced.
* - TDD × Fence
  - 5
  - observed
  - `PreToolUse` hooks with non-zero exit refuse edits; documented by Anthropic and demonstrated in hands-on `hooks.json`.
* - TDD × Paddock
  - 2
  - speculative
  - Would be promoted to `inferred` if Anthropic published a public CI-integration spec. A shipped `claude-code ci` subcommand with a documented exit protocol would change the band.
* - TDD × Groom
  - 2
  - speculative
  - Would be promoted if Anthropic published release-note signals for model updates that invalidate older test assumptions.
* - MDD × Bridle
  - 4
  - observed
  - `/cost` endpoint + status-line token counter expose a usable north-star candidate.
* - MDD × Fence
  - 3
  - inferred
  - Rate limits exist at the API layer but a *local* cost cap requires operator-authored hooks.《马书》 Ch.~7 documents the default limits.
* - MDD × Paddock
  - 2
  - speculative
  - Release SLI concept absent; Claude Code is a client tool, not a server.
* - MDD × Groom
  - 3
  - inferred
  - Anthropic pushes weekly prompt-library updates that act as an upstream groom signal.
```

At least one cell — **TDD × Paddock** — is explicitly flagged
`speculative`. What would promote it: either a shipped Anthropic
`claude-code ci` subcommand with a documented machine-readable exit
protocol, or an官方 release note that declares the existing behaviour
stable and publicly versioned.

## §10.3 — The hooks contract — Claude Code's primary Fence

Claude Code's `.claude/hooks.json` is the most transferable piece of the
product, because it is purely declarative. The observation is that any
hook exiting with code 2 refuses the in-flight tool call; this is
documented by Anthropic {cite}`anthropic2024claudecode` and matches
observed behaviour.

```{literalinclude} ../_handson/10-claude-code/hooks.json
:language: json
```

The hands-on artefact is *synthesized from public documentation* —
explicitly not a copy of any internal file. Any reader who adopts it
into their own `.claude/` setup is using a reconstruction.

## §10.4 — What transfers, what does not

- **Transfers.** The bundled-prompt discipline (a long, load-bearing
  system message), the `SKILL.md` format (simple markdown with
  front-matter), and the hooks contract (exit-code-driven refusals).
- **Does not transfer directly.** Claude-specific model-provider
  coupling, the slash-command registry, the bundled skill library's
  exact wording (copyright restriction).

Readers who want the *pattern* without paying Anthropic's platform cost
can reproduce (a) in their own agent (any agent that reads a long
system message works), (b) trivially (it's already just markdown), and
(c) by adopting Claude Code's hook grammar in any agent that supports
pre-write callbacks.

### Structural risks of a closed-source harness

The asymmetry of learning from a closed-source system deserves naming
explicitly — not as criticism of Claude Code, but as a warning to
readers about how conclusions from this chapter should (and should
not) be generalised.

- **Observation window bias.** Every claim in §10.2 is indexed to the
  2026-03 through 2026-04 observation window. Anthropic ships prompt-
  library updates weekly; any claim about the *content* of the bundled
  prompt has a half-life measured in weeks, not quarters. This is not
  a defect — it is how the product evolves — but it means a reader
  who treats §10.2 as a static reference will progressively hold an
  out-of-date mental model.
- **Unfalsifiable speculative bands.** Two cells in §10.2 carry the
  `speculative` confidence band. The honest consequence is that the
  scores are guesses; the subtler consequence is that *they cannot be
  falsified without Anthropic's cooperation*. Readers should treat
  speculative cells as placeholders, not evidence.
- **Coupling to Anthropic's release cadence.** Every transfer pattern
  named above assumes Anthropic continues to ship along its current
  trajectory (hooks stay declarative, SKILL.md stays simple markdown,
  the bundled prompt remains overridable). A vendor decision to
  consolidate, simplify, or replace any of these surfaces invalidates
  the corresponding transfer. The harness engineering move is to
  **adopt the pattern, not the surface** — a team that wrote its own
  `PreToolUse`-style hook grammar against a stable abstraction will
  survive a Claude Code 2.0 rewrite; a team that bound directly to
  the current `hooks.json` schema will not.

```{admonition} Pitfall — Mistaking observation for specification
:class: warning

A team reads Chapter 10, copies the synthesised `hooks.json` from
§10.3, and builds six months of tooling on top of the observed
behaviour "exit code 2 refuses the in-flight tool call". Anthropic
later ships a Claude Code update that reserves exit code 2 for
a different semantic and introduces a structured JSON response
instead. Half the tooling silently breaks. **Why**: the observed
behaviour was never an API — it was behaviour, which vendors are
free to change. The chapter's Retraction Commitment covers the
book; nothing covers the team's tooling. **Fix**: wrap every
reverse-engineered interface in your own abstraction *before*
relying on it. A function named `refuse_tool_call(reason)` that
happens to exit 2 today and exits 3 next quarter is resilient to
the vendor's internal evolution; direct calls to `sys.exit(2)` are
not. This is the same discipline Feathers {cite}`feathers2004legacy`
prescribes for legacy interfaces, applied to a system the team does
not own.
```

## HarnessCard

```{list-table}
:header-rows: 1
:widths: 35 65

* - Field
  - Value
* - HarnessCard schema version
  - CAR-HarnessCard v0.2 {cite}`car2025decomposition`
* - Subject
  - Claude Code, 2026-03 – 2026-04 observation window {cite}`anthropic2024claudecode`
* - License
  - Closed source (subject); synthesized examples under MIT
* - Control layer (CAR)
  - Very opinionated; bundled prompt is multi-kilobyte.
* - Agency layer (CAR)
  - Tool access is strongly gated by hooks and user confirmation prompts.
* - Runtime layer (CAR)
  - Cloud LLM + local CLI; optional Docker sandbox via hooks.
* - SDD (mean)
  - 3.5 (observed=1, inferred=3, speculative=0)
* - TDD (mean)
  - 3.0 (observed=1, inferred=1, speculative=2)
* - MDD (mean)
  - 3.0 (observed=1, inferred=2, speculative=1)
* - Primary citation
  - {cite}`zhangbook2026`
```

Every score above carries the confidence band of its corresponding cell
in §10.2.

## Research Foundations

-  **Ma's book** {cite}`zhangbook2026` — primary reverse-engineering
   source for the bundled prompt, skill library, and hooks behaviour.
- **Anthropic Claude Code launch post** {cite}`anthropic2024claudecode`
  — the official documentation of record.
- **MCP specification** {cite}`anthropic2024mcp` — the public
  specification Claude Code's tool ecosystem targets.
- **CAR decomposition** {cite}`car2025decomposition` — the
  HarnessCard schema the chapter serialises against.

## Hands-On

One copyable artefact lives under
`book/source/_handson/10-claude-code/`:

- `hooks.json` — a minimal `.claude/hooks.json` example with a
  stop-on-test-failure `PreToolUse` rule, a diff-capturing `PostToolUse`
  rule, and a `SessionEnd` cost-report trigger. Synthesized from public
  documentation; not a copy of any internal file.
