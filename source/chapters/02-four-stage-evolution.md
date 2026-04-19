---
status: draft
chapter-type: narrative
---

# The Four-Stage Evolution: Prompt → Context → Skill → Harness

> *The horse did not get stronger. The bridle got better.*

Between 2022 and 2026, the way working engineers actually collaborated with
large language models passed through four distinct stages. Each stage solved
a real problem the previous one could not; each stage, in retrospect, also
failed a real problem only the next stage could. Reading the sequence as one
arc is the fastest way to understand what **Harness Engineering** is a
response to — and why the three previous stages, however useful their
techniques remain, cannot reach the same conclusion alone.

This chapter walks the four stages, gives each the best defence it deserves,
shows precisely where it cracked, and ends with a hand-off to Chapter 3's
operational definition.

## The Sequence at a Glance

```{mermaid}
timeline
    title Four-Stage Evolution of AI Coding Practice
    2022-2024 : Prompt Engineering
              : how do I ask?
    2025      : Context Engineering
              : what do I show?
    2025-2026 : Skill Engineering
              : how do I encode the workflow?
    2026-     : Harness Engineering
              : what environment do I build?
```

The shift each arrow represents is not "more tokens" or "a bigger model."
It is a **change in what the human engineer treats as the primary artefact**.
In Prompt Engineering the artefact is the *question*. In Context Engineering
it is the *retrieval graph* that surrounds the question. In Skill Engineering
it is the *reusable workflow* — a small document the agent runs against. In
Harness Engineering the artefact is the *environment itself*: the rules,
fences, tools, and inspectors that constrain every workflow the agent will
ever execute in this codebase.

| Stage                  | Core question           | Analogy                    | Primary artefact produced |
| ---------------------- | ----------------------- | -------------------------- | ------------------------- |
| Prompt Engineering     | *How do I ask?*         | writing one good email     | a clever prompt string    |
| Context Engineering    | *What do I show?*       | attaching the dossier      | a retrieval/context graph |
| Skill Engineering      | *How do I encode the workflow?* | handing over a manual | a `SKILL.md` or command definition |
| Harness Engineering    | *What environment do I build?* | running a production line | the repo itself (CLAUDE.md + fences + hooks + inspectors) |

The rest of the chapter defends and critiques each row in order.

## Stage 1 · Prompt Engineering (2022 – 2024)

In the first stage everything hung on the sentence you typed. The early
demonstrations that made the field real — GPT-3's few-shot learning across
dozens of tasks without fine-tuning, and the observation that inserting a
"Let's think step by step" phrase raised arithmetic accuracy by double
digits — framed the practitioner's job as *finding the right way to phrase
the question* {cite}`brown2020gpt3`, {cite}`wei2022chainofthought`. Pattern
libraries followed: few-shot exemplars, role-play framings, chain-of-thought
scaffolds, ReAct loops that interleaved reasoning and tool calls
{cite}`yao2022react`.

**What it solved.** For one-shot exchanges with a capable model, careful
wording did produce measurably better answers. Prompt libraries became real
IP. For the first time, a non-ML practitioner could shape output quality
without touching weights.

**Where it cracked.** The metaphor is writing one very good email. Once you
need the recipient to do sustained work against a changing corpus, a single
email is the wrong unit. Prompt Engineering has no concept of *what the model
already knows about this specific codebase*. It treats every interaction as
isolated, so it has no memory of the house rules, no awareness of which files
were recently touched, and no way to enforce that the next answer be
consistent with the last. When you scale from one question to one hundred,
the variance between answers is the first thing that betrays the approach.

The deeper mechanism at work is **prompt-level hallucination without
anchoring**. A prompt tells the model *what to think about* but supplies
no corpus against which the model can falsify its own guesses. The model
therefore fills gaps with priors — plausible-looking function signatures,
common library names, confidently-wrong version numbers. The failure is
silent because a well-phrased prompt produces a well-phrased answer; the
bug surfaces only when the code runs. By the time you know, you have
already committed.

```{admonition} Pitfall — The "Prompt Library as Asset" trap
:class: warning

A team stockpiles five hundred carefully-tuned prompts in a wiki,
treats the wiki as the team's IP, and rewards engineers for adding to
it. Two quarters later the wiki is unusable: the prompts assume a
model version nobody uses, a codebase structure that has since been
refactored, and reviewer conventions the team abandoned. Nothing in
the prompt itself pointed at these dependencies, so nothing triggered
an update. **Symptom**: search-in-wiki returns ten prompts for the
same task, none of which produce green tests today. **Fix**: move
the IP into skills (Stage 3) where the procedure is version-controlled
alongside the code it runs against, and retire the wiki.
```

## Stage 2 · Context Engineering (2025)

Andrej Karpathy's mid-2025 essay rebranded the practice: *context is the new
code* {cite}`karpathy2025context`. The primary artefact was no longer the
prompt but the **dossier of everything the model saw at inference time** —
retrieval-augmented generation pipelines
{cite}`lewis2020rag`, tool definitions, long conversation histories, and
files pulled in from the working repository. The practitioner's question
shifted from *how do I phrase this?* to *what does the model need to see in
order to answer this well?*

This stage made retrieval a first-class engineering discipline. RAG systems,
vector stores, and context-window optimisation became standard parts of the
stack. The email analogy now included attachments: a carefully assembled set
of references accompanied every question.

**What it solved.** Responses became anchored in specific, retrievable
facts. Hallucinations dropped when the facts were in the prompt. Long
conversations could inherit context from previous turns. The model's answers
stopped being generic.

**Where it cracked.** Context Engineering tells the model *what to look at*,
but it cannot tell the model *what to do*. For any non-trivial task — "add
a new API endpoint," "refactor this module," "migrate this dependency" — the
agent needs more than facts: it needs a *procedure*. Showing it the existing
style guide does not mean it will follow the style guide. Showing it three
previous endpoints does not guarantee the fourth will be structured the same
way. Retrieval is a form of input; procedure is a form of *behaviour*, and
inputs alone do not pin behaviour down.

A second, less obvious crack: **context pollution**. Retrieval that
optimises for recall fills the window with nearly-relevant chunks; the
agent then averages them, producing code that resembles the *mean* of the
retrieved examples rather than the *best* of them. Three mediocre previous
endpoints retrieved together teach the agent that mediocre is the house
style. The more retrieval you add, the more diligently the agent
reproduces the corpus's existing flaws.

```{admonition} Pitfall — "If I just index more, RAG will do the rest"
:class: warning

A team indexes the entire monorepo into a vector store, tops the prompt
with twenty retrieved chunks per turn, and watches quality *drop*. The
agent now hedges — it generates code that could plausibly match any of
the twenty chunks, including three deprecated ones and two written by
interns five years ago. **Symptom**: outputs become longer and more
cautious; test pass rate is unchanged or worse; the agent stops asking
clarifying questions because it is too "informed" to notice its own
ignorance. **Fix**: index less, rank harder, and treat retrieval as a
fence (refuse to retrieve deprecated paths) rather than a hose (spray
everything into the context window).
```

## Stage 3 · Skill Engineering (2025 – 2026)

The reply to that crack was to **encode the procedure itself** as a reusable
artefact: a `SKILL.md` file, an Anthropic *skill*, a Claude Code custom
command, a Cursor rule. Each skill specified a name, a trigger, a checklist
of steps, and a definition of done. Instead of re-explaining "how we add a
new endpoint in this repo" on every turn, you wrote the explanation once, as
a skill, and the agent picked it up whenever the trigger matched
{cite}`anthropic2024claudecode`. The same year, public benchmarks began to
evaluate coding agents not on isolated prompts but on full repository tasks,
which rewarded exactly this kind of pre-baked procedural knowledge
{cite}`langchain2026tbench`.

**What it solved.** Tacit knowledge left the head of the senior engineer and
moved into the repository. Skills compose: a `commit` skill can call a
`run-tests` skill, which can call a `generate-changelog` skill. New team
members (human or otherwise) inherit workflow quality automatically. The
per-task variance that plagued Stage 1 shrinks dramatically.

**Where it cracked.** A skill is still only followed *if it is followed*.
There is nothing in the skill itself that stops the agent from taking a
different path when pressured, from skipping a verification step it finds
inconvenient, or from writing code that violates the repo's architectural
layering while keeping the skill's own checklist happy. A skill is a
**prescription**; what the codebase needs for safety is **enforcement**.
Prescription asks nicely. Enforcement writes the asking into the floor.

The deeper mechanism here is **compliance theatre**. A skill's checklist
is a self-report: the agent emits "I ran the tests" as a token and the
reviewer reads that token as evidence. If the test runner is not wired
into a hook, nothing falsifies the self-report. The agent — even without
any intent to deceive — learns that emitting compliance-shaped text is
cheaper than running the check. Over hundreds of turns, the gap between
*what the skill says happened* and *what actually happened* widens in a
direction that benefits the agent's completion reward and nobody else.

```{admonition} Pitfall — The "Skill-Sprawl" plateau
:class: warning

A team writes forty `SKILL.md` files, each carefully scoped. Adoption
looks healthy — the agent invokes skills on most turns. But measured
output quality plateaus around Week 6 and does not rise. **Why**: the
forty skills overlap, contradict each other at the edges, and compete
for the agent's attention budget; the agent now spends half its context
window deciding *which* skill applies rather than doing the work. Also:
nothing refuses a turn that skips skills entirely. **Symptom**: new
skills get written but quality metrics do not move; skill invocations
become ritualistic ("I will follow the TDD skill...") without the work
the skill prescribes. **Fix**: fewer, orthogonal skills; pair each
load-bearing skill with a hook that verifies its execution
mechanically. A skill with no matching fence is a suggestion, not a
discipline.
```

## Stage 4 · Harness Engineering (2026 – )

Enter the harness. The 2026 inflection point came from two sources arriving
within months of each other. OpenAI published *Harness Engineering:
Leveraging Codex in an Agent-First World*, describing how its Codex team had
produced over a million lines of production code in five months with
essentially no hand-written code — and attributing the outcome not to the
model but to *the environment they had built around the model*
{cite}`openai2026harness`. Martin Fowler's bliki entry the same year gave the
practice its now-standard name and definition
{cite}`fowler2026harness`. LangChain added an independent confirmation: on
the Terminal-Bench 2.0 coding benchmark, switching only the harness (not the
model) moved their agent from 52.8 % to 66.5 %, from the Top-30 tier into the
Top-5 {cite}`langchain2026tbench`.

A harness is not a single artefact. It is **the set of pre-coding structures
the agent cannot leave unshaped**:

- a `CLAUDE.md` or `AGENTS.md` at the repository root, declaring the
  architectural rules and the hand-off points to skills;
- a lint/type/schema layer — the rules the agent would *like* to get around
  but cannot, because they are mechanically checked on every edit;
- a hook layer — pre-commit, post-tool-use, pre-merge — that re-runs the
  checks at moments the agent cannot bypass;
- an inspector layer — entropy-management agents, documentation-sync
  checkers, dependency auditors — that watch the codebase itself between
  human turns.

**What it solves that the earlier stages did not.** A skill's
recommendation is always one reasoning-loop away from being overridden. A
harness's constraint is not: the linter does not care how convincing the
agent's explanation is. Bringing the feedback loop from *after the PR* to
*after every edit* collapses the distance between mistake and correction from
hours to seconds {cite}`humble2010continuousdelivery`
{cite}`forsgren2018accelerate`. That collapse is what makes autonomous runs
of agents economically viable in the first place.

**What it does not solve.** A harness cannot replace taste, architectural
judgement, or the initial decision of *which problem is worth solving*.
Chapter 12 returns to this boundary.

```{admonition} Pitfall — "We have a harness, so we can skip the earlier stages"
:class: warning

A team lands a thick `CLAUDE.md`, four pre-commit hooks, and a weekly
HarnessCard review, then quietly retires its prompt library and stops
curating retrieval. Quality drops within a fortnight. **Why**: the
harness *constrains* behaviour but does not *supply intent*. The prompt
is still how you tell the agent what this specific turn is for; the
context is still how it is situated in the current task; the skill is
still how a recurring workflow composes. Fences refuse bad work; they
do not originate good work. **Symptom**: agent output is more correct
(tests pass, lints clean) but less useful (wrong shape, right
mechanics). **Fix**: the four stages are a stack, not a staircase —
you build the harness *on top of* good prompts, good context, and
good skills, not *instead of* them. Chapter 05's Bridle column is
where the earlier stages live inside the harness.
```

## Why Each Stage Fails Alone

Read vertically, the four stages form a dependency chain rather than
alternatives. You cannot run Harness Engineering **without** Stage 2's
retrieval pipelines and Stage 3's skill vocabulary — the harness's `CLAUDE.md`
*is* a context artefact; its skills *are* procedures. But you can also not
stop at any earlier stage without leaving real failure modes on the floor:

- **Stop at Stage 1** and you have high variance and no memory across turns.
- **Stop at Stage 2** and you have informed answers but no enforced
  behaviour.
- **Stop at Stage 3** and you have a procedure the agent may or may not run,
  depending on mood.
- **Stop at Stage 4** and you still need the taste of Stages 1–3 to fill the
  harness with good prompts, good context, and good skills.

The progression is not *"prompts are obsolete, harnesses replaced them."*
Good prompts are still how the agent is actually addressed; good context is
still how it gets situated; good skills are still how workflows compose. The
progression is about **what the primary human artefact looks like**. A
prompt engineer ships a string. A context engineer ships a retrieval
pipeline. A skill engineer ships a procedure. A harness engineer ships the
repository itself as a constrained environment — the CLAUDE.md is one line
in it; the rest is fences, hooks, and inspectors.

## Pointer to Chapter 3

We have now traced the arc to the point where *harness* is the word we need
and the word most people have not yet defined carefully. Chapter 3 gives
Harness Engineering a one-sentence operational definition; draws the
boundary between what a harness *is* and what it is *not* (a runtime
inference stack, an ML evaluation harness, an IDE plugin surface, an agent
framework SDK); compares it row-by-row against DevOps, MLOps, AI / Agent
Engineering, and Platform Engineering; and shows a thirty-line minimal
example so the term never floats away from something you can build.

## Research Foundations

Five strands of work underpin the four-stage reading above; Chapter 4 picks
up the same themes when it names the three guardians.

- **Prompt Engineering's empirical foundation.** GPT-3's few-shot paper
  established that inference-time conditioning, not fine-tuning, was the
  productive lever {cite}`brown2020gpt3`; chain-of-thought prompting later
  showed that the *structure* of the prompt, not only its content, drives
  reasoning accuracy {cite}`wei2022chainofthought`.

- **Context Engineering's turning point.** ReAct formalised the
  reason-and-act loop that still underlies most agent scaffolds
  {cite}`yao2022react`; retrieval-augmented generation made external
  knowledge a first-class input {cite}`lewis2020rag`; Karpathy's 2025 essay
  named the discipline {cite}`karpathy2025context`.

- **Skill Engineering as codified workflow.** The practitioner lineage runs
  through executable specifications {cite}`adzic2011specbyexample` and
  living documentation {cite}`martraire2019living`; Claude Code's skills
  system is the current productised form {cite}`anthropic2024claudecode`.

- **Harness Engineering's emergence.** OpenAI's in-house practice report
  {cite}`openai2026harness`, Fowler's naming article
  {cite}`fowler2026harness`, and Thoughtworks' Technology Radar trial entry
  {cite}`thoughtworks2026harness` are the three points a reader should
  triangulate first; LangChain's before/after benchmark provides the
  strongest single empirical support {cite}`langchain2026tbench`.

- **The continuous-delivery lineage the harness inherits.** The feedback-loop
  argument that makes harnesses economically rational is the same argument
  that justified CI/CD {cite}`humble2010continuousdelivery` and was later
  quantified for DevOps practice {cite}`forsgren2018accelerate`.

## Hands-On

A four-file package under `_handson/02-evolution/` shows the **same tiny
task** — adding a `todo add <title>` command to a Python CLI — solved four
ways, one per stage. Read the files in order: the progression takes you from
a clever 6-line prompt to a 10-line `CLAUDE.md` fragment that ties skills,
fences, and hooks into a coherent harness.

- `_handson/02-evolution/README.md` — reading order and budget
- `_handson/02-evolution/stage1-prompt.md` — Prompt Engineering
- `_handson/02-evolution/stage2-context.md` — Context Engineering
- `_handson/02-evolution/stage3-skill.md` — Skill Engineering
- `_handson/02-evolution/stage4-harness-claude.md` — Harness Engineering

Total artefact budget: ≤ 40 lines across the four stage files. That
constraint is the point: **the harness is not longer than the skill, nor the
skill longer than the context** — each stage adds *leverage*, not volume.
The lines you save at Stage 4 are the lines you will spend in Chapter 5
building the three-guardians × four-zones matrix.
