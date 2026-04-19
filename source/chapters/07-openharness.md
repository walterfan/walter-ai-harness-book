---
status: draft
chapter-type: case-study
case-study-kind: open-source
---

# Case Study: OpenHarness

> *The closest thing to a textbook harness that ships as open source.*

OpenHarness, authored by the HKU Data Science Lab (HKUDS) and released
as MIT-licensed open source {cite}`hkuds2025openharness`, is the
reference implementation the book returns to most often. It reads as if
its authors had already written Chapter 05: the repository is neatly
divided into ten subsystems, each of which maps onto a specific cell or
small cluster of cells in the three-guardian × four-zone matrix. This
chapter walks through those subsystems, quotes the Agent Loop core, and
scores the whole project against the Ch.05 matrix.

## §07.1 — Ten subsystems at a glance

OpenHarness as of the 2026-03 snapshot is organised around ten
subsystems that roughly correspond to the ten directories under
`src/openharness/` in the upstream tree:

1. `api/` — OpenAI-compatible clients and Copilot auth adapters.
2. `autopilot/` — the long-running agent service that the book's Chapter
   02 stage-4 example alludes to.
3. `channels/` — integrations with Slack, Discord, Feishu, Telegram, and
   eight more messaging surfaces.
4. `config/` — schema + settings + path helpers; a textbook SDD × Fence.
5. `coordinator/` — agent-definition registry.
6. `engine/` — the Agent Loop itself (see §07.2 below).
7. `hooks/` — event bus powering the hook-driven fence.
8. `mcp/` — MCP client wiring; the channel for tool use.
9. `memory/` — conversation memory manager.
10. `sandbox/` — Docker-backed execution isolation; a Runtime-layer paddock.

A reader who wanted to verify every claim in this chapter would `ls
src/openharness/` in a fresh clone of
[`HKUDS/OpenHarness`](https://github.com/HKUDS/OpenHarness) and see the
same ten names. The taxonomy is extracted *from the code*, not imposed
on it.

## §07.2 — The Agent Loop (≤ 20 lines, MIT-attributed)

The heart of any harness is its agent loop. OpenHarness's
`engine/query_engine.py` compresses the ReAct-style loop
{cite}`yao2022react` into a form that is easy to audit and easy to
instrument. The shape of the loop — slightly shortened here for
exposition — is:

```python
# Adapted from OpenHarness/src/openharness/engine/query_engine.py
# MIT License, Copyright (c) 2025 HKUDS.
def step(self, state):
    messages = self.memory.window(state)
    plan = self.model.complete(messages, tools=self.tools.schemas())
    if plan.tool_calls:
        outputs = [self.tools.invoke(c) for c in plan.tool_calls]
        state = self.memory.extend(state, plan, outputs)
        return state, "continue"
    return self.memory.extend(state, plan, []), "halt"
```

What matters for the book's argument is not the ≤ 20 lines themselves
but the three decisions they encode: (a) the model emits tool-calls as
first-class structured output rather than free-form text; (b) the memory
manager owns the context-window policy; (c) the loop *explicitly
distinguishes* "continue" from "halt" states. All three decisions are
visible to the human reviewer, which is what makes this harness
auditable.

## §07.3 — The 43-tool taxonomy (Toolformer-style)

OpenHarness ships 43 first-party tools at the 2026-03 snapshot
{cite}`hkuds2025openharness`. A partial grouping:

```{list-table}
:header-rows: 1
:widths: 30 25 45

* - Group
  - Count
  - Examples
* - File & code navigation
  - 9
  - `read_file`, `grep`, `list_dir`, `semantic_search`
* - Editing
  - 6
  - `write_file`, `str_replace`, `apply_patch`, `delete_file`
* - Shell & process
  - 5
  - `run_command`, `await_job`, `tail_terminal`, `kill_job`, `cat_terminal`
* - VCS
  - 4
  - `git_status`, `git_diff`, `git_commit`, `git_log`
* - Web & fetch
  - 3
  - `web_search`, `web_fetch`, `read_lints`
* - MCP client
  - 3
  - `mcp_call`, `mcp_fetch_resource`, `mcp_list_resources`
* - Miscellaneous
  - 13
  - memory, sandbox, channel, notebook, and helper tools
```

The grouping makes a Toolformer-style {cite}`schick2023toolformer`
argument concrete: the tools are not an afterthought, they are the
primary surface the agent acts through. The MCP specification
{cite}`anthropic2024mcp` extends this surface to third-party tools.

## §07.4 — 12-cell highlight map

Every case-study chapter in the book scores the harness against the
twelve Ch.05 cells on a 0–5 scale, with 1–3 sentences of evidence citing
specific files under `oss/OpenHarness/`.

```{list-table}
:header-rows: 1
:widths: 20 8 72

* - Cell
  - Score
  - Evidence
* - SDD × Bridle
  - 4
  - `README.md`, `src/openharness/prompts/system_prompt.py` and the
    `openharness/prompts/context.py` bundle steer agent behaviour.
* - SDD × Fence
  - 4
  - `config/schema.py` + `config/settings.py` validate every launch-time
    config; bad config aborts the process.
* - SDD × Paddock
  - 3
  - No explicit acceptance-table pattern; review relies on upstream PR
    review + the `autopilot/service.py` state machine.
* - SDD × Groom
  - 3
  - `plugins/loader.py` and `commands/registry.py` refresh in-process
    registries but living-doc grooming is ad-hoc.
* - TDD × Bridle
  - 3
  - Upstream test suite under `tests/` is substantial but not
    committed-red-first; agent context does not read tests by default.
* - TDD × Fence
  - 4
  - `sandbox/adapter.py` + `sandbox/docker_backend.py` refuse code
    execution outside Docker; `permissions/checker.py` refuses tool
    calls by policy.
* - TDD × Paddock
  - 3
  - CI runs `pytest` on PR; no fault-injection or adversarial suite.
* - TDD × Groom
  - 2
  - No published flaky-test quarantine; upstream triage is manual.
* - MDD × Bridle
  - 3
  - `engine/stream_events.py` and `services/__init__.py` expose event
    streams — a good *potential* north-star but not a declared one.
* - MDD × Fence
  - 4
  - `permissions/checker.py` + `sandbox/path_validator.py` are cost and
    blast-radius caps implemented as code.
* - MDD × Paddock
  - 3
  - Release staging exists (tag + changelog); no public SLI gate.
* - MDD × Groom
  - 2
  - No public weekly-audit script; dashboards are self-hosted by ops
    who deploy OpenHarness.
```

Strongest columns: **Fence** (mean 4) and **Bridle** (mean 3.3). Weakest
column: **Groom** (mean 2.3). The pattern is consistent with a
research-leaning open-source project: gates and context are excellent,
recurring maintenance is left to the operator.

## §07.5 — What to copy, what to skip

- **Copy.** The 10-subsystem directory split, the Agent Loop shape
  ({cite}`yao2022react`), the permissions-as-code in `permissions/`, and
  the sandbox isolation in `sandbox/`.
- **Skip** (or treat as scaffolding). The eleven channel adapters in
  `channels/impl/` — they are valuable in their own right but they are
  not part of the *harness core*; a reader trying to build a harness
  for a different product can delete the `channels/` directory on day
  one and lose nothing methodological.

### What OpenHarness is *not* a model of

A case study loses its teaching value the moment it becomes hagiography;
three OpenHarness weaknesses deserve naming so the reader copies its
strengths without the blind spots.

- **Grooming is left to the operator.** The `Groom` column's 2.3 mean
  score in §07.4 is the honest signal: the project ships an engine and
  a sandbox, not a maintenance discipline. A team adopting OpenHarness
  wholesale without adding its own weekly audit, its own doc-sync check,
  and its own HarnessCard cadence will find the harness decays at the
  same rate as any other unattended repository — Ch.06's entropy
  concern is *not* supplied by the framework.
- **No north-star metric is declared.** §07.4 scores MDD × Bridle at 3
  (*"event streams exist, not a declared north-star"*). The Chapter 04
  warning applies: a harness without an owned, threshold-gated north-
  star will collect dashboards and steer by none of them. OpenHarness
  gives you the raw material; declaring the metric is your job.
- **The 43-tool surface is a double-edged gift.** A rich tool surface
  lowers the cost of building an agent but raises the cost of
  *reasoning about what the agent can do*. A team that ships all 43
  tools into production without pruning has implicitly accepted 43
  attack surfaces, 43 cost centres, and 43 places where a schema drift
  would silently break something. The harness engineering move is to
  adopt a small subset first and widen it by demand.

```{admonition} Pitfall — Cargo-culting the directory layout
:class: warning

A team reads §07.1, creates ten top-level directories in their own
repo matching OpenHarness's names — `autopilot/`, `channels/`,
`coordinator/`, etc. — and ships the skeleton. Six weeks later
the directories contain either nothing (because the team's product
does not need a coordinator) or convoluted glue code (because the
team's coordinator does not map onto OpenHarness's abstraction).
**Why**: the ten-subsystem layout is an *emergent* property of
OpenHarness's problem space (multi-channel long-running agent
service); imposing it on a different problem is Conway's law
{cite}`conway1968law` applied in reverse. **Fix**: copy the
*principles* (permissions as code, sandbox isolation, auditable
agent loop) into whatever directory structure your product
actually needs. A harness is a shape that fits a specific load;
borrow the pattern of thought, not the filename list.
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
  - OpenHarness, 2026-03 snapshot {cite}`hkuds2025openharness`
* - License
  - MIT (code), CC-BY-4.0 (docs)
* - Control layer (CAR)
  - Opinionated; `coordinator/agent_definitions.py` + `prompts/` set strong defaults.
* - Agency layer (CAR)
  - 43 tools behind explicit permissions and a Docker sandbox.
* - Runtime layer (CAR)
  - Python 3.11, Docker-backed sandbox, pluggable LLM backends.
* - SDD (0–5, mean of Bridle/Fence/Paddock/Groom)
  - 3.5
* - TDD (0–5)
  - 3.0
* - MDD (0–5)
  - 3.0
* - Primary citation
  - {cite}`hkuds2025openharness`
```

## Research Foundations

- **ReAct** {cite}`yao2022react` — the academic lineage of the Agent
  Loop at the heart of OpenHarness.
- **Toolformer** {cite}`schick2023toolformer` — the academic lineage for
  first-class tool use as a primary action surface.
- **MCP specification** {cite}`anthropic2024mcp` — the industry
  specification that lets OpenHarness plug into third-party tool
  ecosystems without bespoke glue.
- **Upstream OpenHarness README** {cite}`hkuds2025openharness` — the
  canonical record of what ships in the repository and under what
  license; cited as primary source throughout.
- **Anthropic Claude Code launch post** {cite}`anthropic2024claudecode`
  — the industry context OpenHarness positions itself against.

## Hands-On

Two copyable artefacts live under
`book/source/_handson/07-openharness/`:

- `quickstart.sh` — clone → install → run one verification session.
- `custom-tool.py` — a minimum-viable "Add a Custom Tool" example
  adapted from upstream docs with attribution.
