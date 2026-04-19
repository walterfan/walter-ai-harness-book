---
status: draft
---

# Colophon

## How this book was built

*Harnessing AI: The Craft of Shaping Agents* — rendered in Chinese as
《驾驭工程：给 AI 套上缰绳》 — is produced from a single English
Markdown source tree under ``book/source/``, translated into
Simplified Chinese via ``sphinx-intl`` gettext catalogs, and rendered
to HTML by **Sphinx** + **MyST** + **sphinxcontrib-bibtex** + the
**Read the Docs** theme. Citations live in BibTeX files under
``_bib/``; diagrams are authored as ``{mermaid}`` (inline) or
``{plantuml}`` (separate ``.puml`` file) directives. A structural
linter — ``make book-lint`` — enforces the three-guardian × four-zone
matrix contract, the dual-track chapter skeleton, Chapter 03's
definition sections, Chapter 05's provenance declaration, Chapter 11's
four-act structure, and Chapter 12's 30/60/90 checklist discipline.

## The book is its own harness demonstration

The book is written the way it preaches. We apply the 3×4 matrix to
the book itself, and cross-reference each cell to the chapter that
taught the concept:

* **Bridle (guidance)** — ``_bib/`` supplies the canonical citation
  record; every chapter's Research Foundations section carries
  ``{cite}`` roles resolving to entries here. See {ref}`sdd-x-bridle`
  for the general pattern.
* **Fence (constraints)** — ``make book-lint`` enforces every
  structural contract; the ``book-structure`` spec, in turn,
  enforces what ``book-lint`` must check. See {ref}`sdd-x-fence` for
  the general pattern and {ref}`tdd-x-fence` for the hook-level twin.
* **Paddock (boundaries / acceptance)** — a strict Sphinx build
  (``-W --keep-going -n``) gates every PR touching ``book/**``.
  See {ref}`tdd-x-paddock` for the general pattern.
* **Groom (maintenance)** — ``make book-intl`` keeps the zh_CN ``.po``
  catalogs fresh; the translation-freshness banner surfaces rot
  automatically. See {ref}`sdd-x-groom` and {ref}`mdd-x-groom` for the
  grooming patterns the book's own workflow instantiates.

## License & attribution

* Prose and diagrams authored for this book: **CC-BY-SA-4.0**.
* Code samples authored for this book: **MIT**, matching the rest of
  the host repository.
* Quoted excerpts from third-party sources (OpenHarness, Superpowers,
  《马书》, etc.) retain their upstream licenses; each excerpt carries
  an inline attribution footer naming the source and license.

See ``book/LICENSE`` for the definitive text.

## Author & acknowledgements

Author: Walter Fan. Editorial review, translation, and harness-testing
contributions are credited in the chapter where they land. A rolling
acknowledgement index lives at the bottom of
``book/CONTRIBUTING.md``.

## Credits and thanks

Specific projects, books, and individuals whose work is load-bearing in
this book:

* **HKU Data Science Lab** for **OpenHarness** {cite}`hkuds2025openharness`
  — the open-source reference implementation Chapter 07 treats.
* **Joseph Vincent (David Vincent, `obra`)** for **Superpowers**
  {cite}`vincent2025superpowers` — the skills library Chapter 08 treats.
* **The `lazy-scrum-team` authors** {cite}`lazyscrumteam2026` — whose
  workflow-encoded harness is Chapter 09's canonical treatment.
* **Zhang Handong (张汉东)** for **《马书》** {cite}`zhangbook2026` — the
  reverse-engineering study that makes Chapter 10 tractable.
* **The authors of the CAR / HarnessCard position paper**
  {cite}`car2025decomposition` — whose disclosure format Appendix D
  serialises against.
* **The `walkinglabs/awesome-harness-engineering` curators**
  {cite}`walkinglabs2026awesome` — the ongoing curated list that
  complements this long-form methodology.
