---
status: draft
chapter-type: appendix
---

# Appendix D — HarnessCard Template

The HarnessCard format is a standardised disclosure proposed by the CAR
decomposition paper {cite}`car2025decomposition`. This appendix carries
three pieces: a **blank template** (copy into your repo), two **filled
instances** from Chapter 11 shown side-by-side for delta reading, and a
**rubric** defining what each 0–5 score means.

(apd-harnesscard-template)=
## Blank template

Copy the block below into a `HarnessCard.md` at your repo root. Replace
every `…` with evidence specific to your harness.

```markdown
# HarnessCard — <project name>

**Schema version.** CAR-HarnessCard v0.2.
**Subject.** <repo URL> at commit <SHA>.
**Observation window.** <YYYY-MM-DD> – <YYYY-MM-DD>.
**License.** <SPDX identifier>.

## Layer notes (CAR)

| Layer    | Notes                                                    |
|----------|----------------------------------------------------------|
| Control  | …                                                        |
| Agency   | …                                                        |
| Runtime  | …                                                        |

## Zone notes (Bridle / Fence / Paddock / Groom)

| Zone    | Notes                                                     |
|---------|-----------------------------------------------------------|
| Bridle  | …                                                         |
| Fence   | …                                                         |
| Paddock | …                                                         |
| Groom   | …                                                         |

## 3 × 4 scorecard

| Cell            | Score (0–5) | Evidence (file / URL)           |
|-----------------|-------------|----------------------------------|
| SDD × Bridle    | …           | …                                |
| SDD × Fence     | …           | …                                |
| SDD × Paddock   | …           | …                                |
| SDD × Groom     | …           | …                                |
| TDD × Bridle    | …           | …                                |
| TDD × Fence     | …           | …                                |
| TDD × Paddock   | …           | …                                |
| TDD × Groom     | …           | …                                |
| MDD × Bridle    | …           | …                                |
| MDD × Fence     | …           | …                                |
| MDD × Paddock   | …           | …                                |
| MDD × Groom     | …           | …                                |

**Means.** SDD = …, TDD = …, MDD = …, Overall = …

**Primary citation.** ``<BibTeX key>``.
```

## Two filled instances — Chapter 11 Act 1 vs Act 4

The two HarnessCards below are the Chapter 11 worked example's
before-and-after pair, shown side-by-side with a delta column. The full
cards live at `_handson/11-lazy-ai-coder/HarnessCard-Act1.md` and
`_handson/11-lazy-ai-coder/HarnessCard-Act4.md`.

```{list-table}
:header-rows: 1
:widths: 24 14 14 12 36

* - Cell
  - Act 1
  - Act 4
  - Delta
  - Fix (from §14)
* - SDD × Bridle
  - 3
  - 3
  - 0
  - unchanged
* - SDD × Fence
  - 1
  - 4
  - +3
  - `make prompts-lint` + schema validator (§14.1)
* - SDD × Paddock
  - 2
  - 2
  - 0
  - unchanged
* - SDD × Groom
  - 1
  - 3
  - +2
  - `sources-of-truth.md` index (§14.3)
* - TDD × Bridle
  - 2
  - 2
  - 0
  - unchanged
* - TDD × Fence
  - 1
  - 4
  - +3
  - MCP schema check + gitleaks (§14.2 + §14.4)
* - TDD × Paddock
  - 3
  - 3
  - 0
  - unchanged
* - TDD × Groom
  - 2
  - 2
  - 0
  - unchanged
* - MDD × Bridle
  - 1
  - 1
  - 0
  - out of §14 scope
* - MDD × Fence
  - 2
  - 2
  - 0
  - unchanged
* - MDD × Paddock
  - 2
  - 2
  - 0
  - unchanged
* - MDD × Groom
  - 1
  - 1
  - 0
  - unchanged
```

**SDD mean.** 1.75 → 3.00 (+1.25).
**TDD mean.** 2.00 → 2.75 (+0.75).
**MDD mean.** 1.50 → 1.50 (+0.00).
**Overall.** 1.75 → 2.42 (+0.67).

## Rubric — what each score means

Every cell score is a 0–5 integer. The rubric is pinned to CAR-HarnessCard
v0.2 {cite}`car2025decomposition` and applies uniformly across all
twelve cells.

| Score | Meaning                                                                                  |
|-------|-------------------------------------------------------------------------------------------|
| **0** | No artefact of any kind for this cell. The guardian × zone intersection is absent.        |
| **1** | An ad-hoc artefact exists but is not invoked on a cadence and carries no owner.           |
| **2** | A committed artefact exists; a named role owns it; review cadence is irregular.           |
| **3** | Artefact, owner, and cadence all present; the artefact is read by agents (SDD/TDD rows) or scraped (MDD row). |
| **4** | Artefact is *enforced* — failure blocks commits, merges, or releases as appropriate.      |
| **5** | Enforced **and** machine-verifiable **and** the artefact itself is revised on a declared cadence (quarterly or faster). |

A score of 4 requires an enforcement mechanism; a score of 5 additionally
requires a meta-review schedule. Teams that cannot point to an
enforcement artefact should score a 3, not a 4.
