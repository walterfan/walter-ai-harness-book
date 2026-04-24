#!/usr/bin/env python3
"""book-lint — structural and bibliographic lint for the Harnessing AI book.

Runs as ``make book-lint`` (see the repository root ``Makefile``).

The canonical spec lives at
``openspec/changes/harness-engineering-book/specs/docs-tooling/spec.md``;
this implementation follows the check IDs (a)-(o) from that spec verbatim,
plus the ``book_lint.py`` coverage matrix in
``openspec/changes/harness-engineering-book/tasks.md`` (task 13.3).

Design principles
-----------------

1.  **Error vs. warning split follows the spec.**  Anything the spec says
    "exits non-zero" produces an error; anything it says "emits a warning"
    or "warning-only" produces a warning and does not fail the run.
2.  **Status-aware enforcement.**  Structural checks that require full
    content (research foundations / 研究脉络, hands-on / 动手环节, matrix cells, HarnessCards,
    etc.) only hard-fail on files whose front-matter declares
    ``status: complete``.  ``status: draft`` / ``status: review`` files
    still get scanned, but missing sections downgrade to warnings so the
    repository can build long before the book is finished.
3.  **Zero external dependencies at the pure-stdlib layer.**  The one
    optional import is ``pybtex`` for robust ``.bib`` parsing; it falls
    back to a regex scanner if ``pybtex`` is not installed, so the script
    is runnable even outside the book venv.
4.  **Stable, grep-friendly output.**  Every finding is printed on a single
    line in the form ``LEVEL  CHECK  PATH[:LINE]  MESSAGE``; a summary
    tail reports counts and exits ``0`` if no errors, ``1`` otherwise.

Usage
-----

::

    python3 scripts/book_lint.py source

The path argument defaults to ``source`` relative to the
repository root when invoked through the Makefile.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Canonical constants (keep these in sync with the docs-tooling spec)
# ---------------------------------------------------------------------------

CANONICAL_EN_TITLE = "Harnessing AI: The Craft of Shaping Agents"
CANONICAL_ZH_TITLE = "《驾驭工程：给 AI 套上缰绳》"
CANONICAL_ZH_H1 = "驾驭工程：给 AI 套上缰绳"
CANONICAL_SOURCE_TITLES = (CANONICAL_EN_TITLE, CANONICAL_ZH_H1)

# Chapters that are exempt from dual-track enforcement (see check (d)).
DUAL_TRACK_EXEMPT = {
    "chapters/01-foreword.md",
    "colophon.md",
}
DUAL_TRACK_EXEMPT_PREFIXES = (
    "chapters/00-presentation/",
    "chapters/13-appendices/",
)

# Expected appendix filenames in alphabetical order (check (m)).
EXPECTED_APPENDICES = [
    "a-faq.md",
    "b-glossary.md",
    "c-reading-list.md",
    "d-harnesscard.md",
    "e-claude-md.md",
    "f-engineer-playbook.md",
]

# Citation-key convention for check (e).  Accepts:
#   lastname + YYYY + slug   e.g. brown2020gpt3
#   lastname + _YYYY_ + slug e.g. brown_2020_gpt3
#   org/team + YYYY + slug   e.g. langchain2026tbench
# At least 3 lowercase letters, then a 4-digit year, then at least 2 alnum
# characters for the slug.  Case-insensitive on the year suffix side is
# intentionally *not* allowed; BibTeX conventionally uses all-lowercase keys.
BIBKEY_CONVENTION = re.compile(r"^[a-z][a-z0-9]{2,}_?\d{4}_?[a-z0-9]{2,}$")

RESEARCH_FOUNDATIONS_H2 = ("research foundations", "研究脉络")
HANDS_ON_H2 = ("hands-on", "hands on", "动手环节")


# ---------------------------------------------------------------------------
# Finding model
# ---------------------------------------------------------------------------


@dataclass
class Finding:
    """A single lint finding.

    Attributes
    ----------
    level
        ``"error"`` (contributes to non-zero exit) or ``"warning"`` (advisory).
    check
        Letter ID from the spec (``a``-``o``) or a descriptive slug.
    path
        File the finding is attached to, relative to the book source root.
    message
        Human-readable explanation of what went wrong and, where possible,
        how to fix it.
    line
        1-based line number if the finding has a specific location;
        otherwise ``None``.
    """

    level: str
    check: str
    path: str
    message: str
    line: Optional[int] = None

    def render(self) -> str:
        loc = f"{self.path}:{self.line}" if self.line else self.path
        tag = "ERROR  " if self.level == "error" else "WARN   "
        return f"{tag}({self.check})  {loc}  {self.message}"


@dataclass
class LintRun:
    source_root: Path
    repo_root: Path
    findings: List[Finding] = field(default_factory=list)

    def error(self, check: str, path: Path, msg: str, line: Optional[int] = None) -> None:
        self.findings.append(
            Finding("error", check, self._rel(path), msg, line)
        )

    def warn(self, check: str, path: Path, msg: str, line: Optional[int] = None) -> None:
        self.findings.append(
            Finding("warning", check, self._rel(path), msg, line)
        )

    def _rel(self, path: Path) -> str:
        try:
            return str(path.relative_to(self.source_root))
        except ValueError:
            try:
                return str(path.relative_to(self.repo_root))
            except ValueError:
                return str(path)

    @property
    def errors(self) -> int:
        return sum(1 for f in self.findings if f.level == "error")

    @property
    def warnings(self) -> int:
        return sum(1 for f in self.findings if f.level == "warning")


# ---------------------------------------------------------------------------
# BibTeX scanning
# ---------------------------------------------------------------------------


def parse_bib_keys(bib_path: Path) -> List[Tuple[str, int]]:
    """Return list of ``(key, line_number)`` tuples defined in ``bib_path``.

    Uses ``pybtex`` when available so the key set matches what Sphinx sees;
    otherwise falls back to a simple regex scan.
    """
    keys: List[Tuple[str, int]] = []
    try:
        from pybtex.database import parse_file  # type: ignore
    except ImportError:
        parse_file = None  # type: ignore[assignment]

    if parse_file is not None:
        try:
            db = parse_file(str(bib_path), "bibtex")
        except Exception:
            # Parsing failure is its own finding; return regex-scanned keys
            # for at least check (a) to function.
            db = None
        if db is not None:
            lines = bib_path.read_text(encoding="utf-8").splitlines()
            # pybtex strips line info; resolve lines via regex so (c) output
            # stays useful.
            for m in re.finditer(
                r"^\s*@\w+\s*\{\s*([^,\s]+)\s*,", "\n".join(lines), re.MULTILINE
            ):
                keys.append((m.group(1), _line_at(lines, m.start())))
            return keys

    lines = bib_path.read_text(encoding="utf-8").splitlines()
    for idx, line in enumerate(lines, start=1):
        m = re.match(r"\s*@\w+\s*\{\s*([^,\s]+)\s*,", line)
        if m:
            keys.append((m.group(1), idx))
    return keys


def _line_at(lines: List[str], char_offset: int) -> int:
    total = 0
    for idx, line in enumerate(lines, start=1):
        total += len(line) + 1
        if total > char_offset:
            return idx
    return max(1, len(lines))


# ---------------------------------------------------------------------------
# Chapter scanning
# ---------------------------------------------------------------------------

FRONT_MATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
CITE_ROLE_RE = re.compile(r"\{cite[a-z:]*\}`([^`\n]+)`")
H2_RE = re.compile(r"^##\s+(.*?)\s*$", re.MULTILINE)


@dataclass
class ChapterInfo:
    path: Path
    front_matter: Dict[str, str]
    body: str
    h2_headings: List[str]
    cite_keys: Set[str]

    @property
    def status(self) -> str:
        return (self.front_matter.get("status") or "draft").strip().strip('"')

    @property
    def chapter_type(self) -> str:
        return (self.front_matter.get("chapter-type") or "").strip().strip('"')


def scan_chapter(path: Path) -> ChapterInfo:
    text = path.read_text(encoding="utf-8")
    fm: Dict[str, str] = {}
    body = text
    m = FRONT_MATTER_RE.match(text)
    if m:
        for line in m.group("body").splitlines():
            if ":" in line and not line.lstrip().startswith("#"):
                k, _, v = line.partition(":")
                fm[k.strip()] = v.strip()
        body = text[m.end():]
    # sphinxcontrib-bibtex accepts comma-separated key lists inside a single
    # ``{cite}`...`` role (e.g. ``{cite}`key_a,key_b```); flatten them so each
    # individual key is validated against ``known_keys``.
    cites: Set[str] = set()
    for raw in CITE_ROLE_RE.findall(body):
        for key in raw.split(","):
            key = key.strip()
            if key:
                cites.add(key)
    # strip inline code spans before grabbing H2 headings so we don't trip on
    # ``## examples`` inside a backtick block
    clean_body = re.sub(r"`[^`]*`", "", body)
    h2 = [m.group(1).strip() for m in H2_RE.finditer(clean_body)]
    return ChapterInfo(
        path=path,
        front_matter=fm,
        body=body,
        h2_headings=h2,
        cite_keys=cites,
    )


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------


def check_duplicate_bib_keys(run: LintRun, bib_files: List[Path]) -> Dict[str, Path]:
    """Check (a): duplicate BibTeX keys across ``_bib/*.bib``."""
    owner: Dict[str, Path] = {}
    for bib in bib_files:
        for key, line in parse_bib_keys(bib):
            prior = owner.get(key)
            if prior is not None:
                run.error(
                    "a",
                    bib,
                    f"duplicate BibTeX key '{key}' (also defined in {prior.name})",
                    line,
                )
            else:
                owner[key] = bib
    return owner


def check_cite_key_references(
    run: LintRun, chapters: List[ChapterInfo], known_keys: Set[str]
) -> Set[str]:
    """Checks (b) unknown cites and (c) unused bib entries."""
    used: Set[str] = set()
    for ch in chapters:
        for key in ch.cite_keys:
            if key not in known_keys:
                suggestion = _closest_key(key, known_keys)
                hint = f" — did you mean '{suggestion}'?" if suggestion else ""
                run.error(
                    "b",
                    ch.path,
                    f"unknown citation key {{cite}}`{key}`{hint}",
                )
            else:
                used.add(key)
    unused = known_keys - used
    for key in sorted(unused):
        run.warn(
            "c",
            Path("_bib"),
            f"BibTeX key '{key}' defined but never cited (will not appear in prose; "
            f"OK while the book is in draft — cite it or remove it before archiving)",
        )
    return used


def _closest_key(target: str, known: Iterable[str]) -> Optional[str]:
    import difflib

    cands = difflib.get_close_matches(target, list(known), n=1, cutoff=0.7)
    return cands[0] if cands else None


def check_bibkey_convention(run: LintRun, bib_files: List[Path]) -> None:
    """Check (e): BibTeX key naming convention."""
    for bib in bib_files:
        for key, line in parse_bib_keys(bib):
            if not BIBKEY_CONVENTION.match(key):
                run.warn(
                    "e",
                    bib,
                    f"BibTeX key '{key}' does not match convention "
                    f"`lastauthor_year_shortslug` (downgraded to warning while the "
                    f"key namespace is being seeded; will promote to error after 13.1 lands)",
                    line,
                )


def check_dual_track(run: LintRun, chapters: List[ChapterInfo]) -> None:
    """Check (d): research foundations + hands-on presence.

    Exempts the Foreword, Appendices, and Colophon.  Missing sections hard-fail
    only on ``status: complete`` chapters; ``status: draft`` / ``status: review``
    produce warnings so the scaffolded book can still build.
    """
    for ch in chapters:
        rel = _book_rel(run, ch.path)
        if rel in DUAL_TRACK_EXEMPT:
            continue
        if any(rel.startswith(pref) for pref in DUAL_TRACK_EXEMPT_PREFIXES):
            continue
        headings_lower = {h.lower() for h in ch.h2_headings}
        missing: List[str] = []
        if not any(
            needle in h
            for h in headings_lower
            for needle in RESEARCH_FOUNDATIONS_H2
        ):
            missing.append("## 研究脉络")
        if not any(
            needle in h
            for h in headings_lower
            for needle in HANDS_ON_H2
        ):
            missing.append("## 动手环节")
        for sect in missing:
            msg = f"dual-track chapter is missing required section '{sect}'"
            if ch.status == "complete":
                run.error("d", ch.path, msg)
            else:
                run.warn("d", ch.path, f"{msg} (downgraded: status={ch.status})")


def check_appendix_order(run: LintRun, appendix_dir: Path) -> None:
    """Check (m) part 1: Appendix filename order."""
    if not appendix_dir.is_dir():
        return
    md_files = sorted(
        p.name for p in appendix_dir.iterdir()
        if p.is_file() and p.suffix == ".md" and p.name != "index.md"
    )
    if md_files != EXPECTED_APPENDICES:
        run.error(
            "m",
            appendix_dir,
            "appendix filenames do not match canonical order.\n"
            f"         expected: {EXPECTED_APPENDICES}\n"
            f"         found:    {md_files}",
        )


def check_toctree_positions(run: LintRun, index_md: Path) -> None:
    """Check (m) part 2: references.md must follow appendices/index;
    colophon.md must follow references.md."""
    if not index_md.is_file():
        return
    text = index_md.read_text(encoding="utf-8")
    # toctree lines are the contiguous block of non-blank, non-directive
    # lines inside a ``{toctree}`` fence.  The root index may now contain
    # multiple toctrees (Part 0 presentation is its own block), so we scan
    # every toctree and pick the one that carries the appendices entry.
    entries: List[str] = []
    for m in re.finditer(
        r"^```\{toctree\}.*?^(?P<body>.*?)^```",
        text,
        re.MULTILINE | re.DOTALL,
    ):
        body = m.group("body")
        block = [
            ln.strip()
            for ln in body.splitlines()
            if ln.strip() and not ln.strip().startswith(":")
        ]
        if any(e.startswith("chapters/13-appendices") for e in block):
            entries = block
            break
    if not entries:
        return
    try:
        i_app = next(
            i for i, e in enumerate(entries)
            if e.startswith("chapters/13-appendices")
        )
        i_ref = entries.index("references")
        i_col = entries.index("colophon")
    except (StopIteration, ValueError):
        return
    if i_ref != i_app + 1:
        run.error(
            "m",
            index_md,
            f"'references' must immediately follow "
            f"'chapters/13-appendices/index' in the toctree; "
            f"found at position {i_ref}, appendices at {i_app}",
        )
    if i_col != i_ref + 1:
        run.error(
            "m",
            index_md,
            f"'colophon' must immediately follow 'references' in the toctree; "
            f"found at position {i_col}, references at {i_ref}",
        )


def check_book_title_drift(run: LintRun) -> None:
    """Check (o): canonical book title consistency."""
    src = run.source_root

    conf_py = src / "conf.py"
    if conf_py.is_file():
        text = conf_py.read_text(encoding="utf-8")
        project_ok = any(
            f'project = "{title}"' in text or f"project = '{title}'" in text
            for title in CANONICAL_SOURCE_TITLES
        )
        if not project_ok:
            run.error(
                "o",
                conf_py,
                "conf.py must set `project` to the canonical English or "
                "Chinese book title",
            )

    index_md = src / "index.md"
    if index_md.is_file():
        first_h1 = _first_h1(index_md.read_text(encoding="utf-8"))
        if first_h1 not in CANONICAL_SOURCE_TITLES:
            run.error(
                "o",
                index_md,
                f"H1 must be either '# {CANONICAL_EN_TITLE}' or "
                f"'# {CANONICAL_ZH_H1}' "
                f"(found: '# {first_h1 or '<none>'}')",
            )

    readme = src.parent / "README.md"  # book/README.md
    if readme.is_file():
        head = "\n".join(readme.read_text(encoding="utf-8").splitlines()[:5])
        if CANONICAL_EN_TITLE not in head:
            run.error(
                "o", readme,
                f"the English title '{CANONICAL_EN_TITLE}' must appear within "
                f"the first five lines of book/README.md",
            )
        if CANONICAL_ZH_TITLE not in head:
            run.error(
                "o", readme,
                f"the Chinese title {CANONICAL_ZH_TITLE} must appear within "
                f"the first five lines of book/README.md",
            )


def check_tauri_chapter_misplacement(run: LintRun, chapters_dir: Path) -> None:
    """Check (i) part 2: no dedicated ``*-tauri-*.md`` under chapters/."""
    if not chapters_dir.is_dir():
        return
    for p in chapters_dir.rglob("*-tauri-*.md"):
        run.warn(
            "i",
            p,
            "dedicated Tauri chapter detected — the Tauri-Todo hands-on was "
            "merged into Ch.06; move this content under "
            "_handson/06-operating-a-harness/tauri-todo/ and reference it from "
            "Chapter 06's ## 动手环节 section",
        )


def check_closed_source_disclaimer(run: LintRun, chapters: List[ChapterInfo]) -> None:
    """Check (n): reverse-engineering disclaimer for closed-source case studies."""
    needle = "reverse-engineer"
    for ch in chapters:
        kind = (ch.front_matter.get("case-study-kind") or "").strip().strip('"')
        body_lower = ch.body.lower()
        has_disclaimer = needle in body_lower
        if kind == "closed-source":
            if not has_disclaimer and ch.status == "complete":
                run.error(
                    "n",
                    ch.path,
                    "closed-source case study must carry a reverse-engineering "
                    "disclaimer (paragraph containing the word 'reverse-engineer')",
                )
            elif not has_disclaimer:
                run.warn(
                    "n",
                    ch.path,
                    f"closed-source case study will need a reverse-engineering "
                    f"disclaimer before going 'status: complete' "
                    f"(currently status={ch.status})",
                )
        elif has_disclaimer and kind not in ("closed-source", ""):
            run.warn(
                "n",
                ch.path,
                f"reverse-engineering language found in a "
                f"case-study-kind={kind!r} chapter — consider removing or "
                f"changing case-study-kind to closed-source",
            )


# ---------------------------------------------------------------------------
# Check (f): Chapter 03 definition-chapter structure
# ---------------------------------------------------------------------------

# Order-sensitive prefixes of the mandatory H2s in Chapter 03.
_CH03_REQUIRED_H2_PREFIXES: List[str] = ["03.1", "03.2", "03.3", "03.4"]
_CH03_OPTIONAL_H2_PREFIX: str = "03.5"


def _word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-]*", text))


def check_chapter_03_structure(run: LintRun, chapters: List[ChapterInfo]) -> None:
    """Check (f): Chapter 03 definition-chapter structure.

    Rules (all gated on ``status: complete``; downgraded to warnings for draft):

    1. Four mandatory H2 sections present and appearing in the order
       03.1 → 03.2 → 03.3 → 03.4.
    2. 03.1 contains a single ``> ...`` blockquote of ≤ 40 words (the
       one-sentence field definition) followed by elaboration prose whose first
       paragraph is ≤ 150 words.
    3. 03.3 contains a comparison table — either a MyST ``{list-table}``
       directive or a pipe table — and each non-header row carries ≥ 1
       ``{cite}`` role.
    4. 03.4's minimal example, taken as the total non-blank lines of embedded
       fenced code / ``{literalinclude}`` blocks within 03.4, is ≤ 40 lines
       (the three 10-line fragments plus headroom).
    """

    target = next(
        (
            ch
            for ch in chapters
            if ch.path.name == "03-what-is-harness-engineering.md"
        ),
        None,
    )
    if target is None:
        return

    is_complete = target.status == "complete"

    def fail(msg: str) -> None:
        if is_complete:
            run.error("f", target.path, msg)
        else:
            run.warn(
                "f",
                target.path,
                f"{msg} (downgraded: status={target.status})",
            )

    # ---- 1. Mandatory H2 ordering ------------------------------------------
    headings = target.h2_headings
    seen_indices: Dict[str, int] = {}
    for prefix in _CH03_REQUIRED_H2_PREFIXES:
        matches = [i for i, h in enumerate(headings) if h.startswith(prefix)]
        if not matches:
            fail(f"Chapter 03 is missing mandatory H2 '{prefix} ...'")
        else:
            seen_indices[prefix] = matches[0]

    if len(seen_indices) == len(_CH03_REQUIRED_H2_PREFIXES):
        ordered = [seen_indices[p] for p in _CH03_REQUIRED_H2_PREFIXES]
        if ordered != sorted(ordered):
            fail(
                "Chapter 03 mandatory H2s are out of order; expected "
                + " → ".join(_CH03_REQUIRED_H2_PREFIXES)
            )

    # Slice the body into per-H2 sections so later rules can target one H2.
    sections: Dict[str, str] = {}
    current_key: Optional[str] = None
    buf: List[str] = []
    for line in target.body.splitlines(keepends=True):
        hm = re.match(r"^##\s+(.*?)\s*$", line)
        if hm:
            if current_key is not None:
                sections[current_key] = "".join(buf)
            title = hm.group(1).strip()
            # Key sections by the XX.Y prefix when present so lookup is stable.
            prefix_match = re.match(r"(0?3\.\d)", title)
            current_key = prefix_match.group(1) if prefix_match else title
            buf = []
        else:
            if current_key is not None:
                buf.append(line)
    if current_key is not None:
        sections[current_key] = "".join(buf)

    # ---- 2. 03.1 length bounds --------------------------------------------
    s1 = sections.get("03.1")
    if s1 is not None:
        quote_match = re.search(
            r"(?:^|\n)\s*>\s*(.+?)(?=\n\s*\n|\Z)", s1, re.DOTALL
        )
        if not quote_match:
            fail("03.1 must open with a '> ...' blockquote one-sentence definition")
        else:
            quote_text = re.sub(r"\s+", " ", quote_match.group(1)).strip(" *")
            wc = _word_count(quote_text)
            if wc > 40:
                fail(
                    f"03.1 blockquote definition is {wc} words "
                    f"(must be ≤ 40)"
                )
            rest = s1[quote_match.end():].lstrip()
            first_para = re.split(r"\n\s*\n", rest, maxsplit=1)[0] if rest else ""
            fp_wc = _word_count(first_para)
            if fp_wc > 150:
                fail(
                    f"03.1 first elaboration paragraph is {fp_wc} words "
                    f"(must be ≤ 150)"
                )

    # ---- 3. 03.3 comparison table + per-row citations ---------------------
    s3 = sections.get("03.3")
    if s3 is not None:
        has_list_table = "```{list-table}" in s3 or "```{csv-table}" in s3
        pipe_rows = [
            ln for ln in s3.splitlines()
            if re.match(r"^\s*\|.+\|\s*$", ln)
        ]
        has_pipe_table = len(pipe_rows) >= 3  # header + separator + ≥1 data
        if not (has_list_table or has_pipe_table):
            fail("03.3 must contain a comparison table (list-table or pipe table)")
        else:
            # For list-tables, a data row starts with '* - ' at column 0 and
            # subsequent '  - ' continuation rows belong to the same row.
            # We split on leading '* -' markers, skip the header row (first),
            # and require each remaining row to include at least one {cite}.
            if has_list_table:
                m = re.search(
                    r"```\{list-table\}.*?\n(.*?)```", s3, re.DOTALL
                )
                block = m.group(1) if m else ""
                row_chunks = re.split(r"(?m)^\s*\*\s*-\s*", block)[1:]
                if len(row_chunks) <= 1:
                    fail("03.3 comparison table must have ≥ 1 data row under its header")
                else:
                    for idx, chunk in enumerate(row_chunks[1:], start=1):
                        if "{cite" not in chunk:
                            fail(
                                f"03.3 comparison-table data row #{idx} "
                                f"must carry ≥ 1 `{{cite}}` role"
                            )

    # ---- 4. 03.4 artefact line budget -------------------------------------
    s4 = sections.get("03.4")
    if s4 is not None:
        total_code_lines = 0
        # Count fenced code blocks.
        for block in re.findall(r"```[^\n]*\n(.*?)```", s4, re.DOTALL):
            total_code_lines += sum(1 for ln in block.splitlines() if ln.strip())
        # ``{literalinclude}`` references pull in external files; count those too.
        for inc_match in re.finditer(
            r"\{literalinclude\}\s*`([^`]+)`", s4
        ):
            inc_rel = inc_match.group(1).strip()
            inc_path = (target.path.parent / inc_rel).resolve()
            if inc_path.is_file():
                total_code_lines += sum(
                    1 for ln in inc_path.read_text(encoding="utf-8").splitlines()
                    if ln.strip()
                )
        if total_code_lines > 40:
            fail(
                f"03.4 minimal example totals {total_code_lines} non-blank "
                f"code lines (must be ≤ 40 — three 10-line fragments plus headroom)"
            )


# ---------------------------------------------------------------------------
# Stubs for structural checks that are only meaningful once prose lands.
# Each stub emits a single info-level reminder so reviewers know the check
# exists but is deferred until the corresponding chapter goes 'status: complete'.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 13.3.g/h — Chapter 05 structural checks (live)
# ---------------------------------------------------------------------------

_CH05_EXPECTED_CELLS: List[str] = [
    "SDD × Bridle", "SDD × Fence", "SDD × Paddock", "SDD × Groom",
    "TDD × Bridle", "TDD × Fence", "TDD × Paddock", "TDD × Groom",
    "MDD × Bridle", "MDD × Fence", "MDD × Paddock", "MDD × Groom",
]

_ZONE_ZH_TO_EN = {
    "缰绳": "Bridle",
    "护栏": "Fence",
    "牧场": "Paddock",
    "梳理": "Groom",
}


def _canonical_cell_key(title: str) -> str:
    """Return the canonical English Guardian × Zone key from an H3 title."""
    key = re.split(r"\s+[—-]+\s+", title, maxsplit=1)[0].strip()
    for zh, en in _ZONE_ZH_TO_EN.items():
        key = key.replace(zh, en)
    return key


def check_chapter_05_structure(run: LintRun, chapters: List[ChapterInfo]) -> None:
    """Checks (g) Provenance + ≥3 cross-framework cites; (h) 12-cell H3s.

    Warnings while ``status`` is ``draft`` / ``review``, errors at
    ``status: complete``.
    """
    target = next(
        (ch for ch in chapters if ch.path.name == "05-harness-anatomy.md"),
        None,
    )
    if target is None:
        return

    is_complete = target.status == "complete"

    def report(cid: str, msg: str) -> None:
        if is_complete:
            run.error(cid, target.path, msg)
        else:
            run.warn(cid, target.path, f"{msg} (downgraded: status={target.status})")

    # (g) Provenance section presence + ≥3 distinct cite keys inside it.
    prov_re = re.compile(r"^##\s+(?:Provenance\b|出处\b).*?$(.*?)(?=^##\s|\Z)",
                         re.MULTILINE | re.DOTALL)
    m = prov_re.search(target.body)
    if not m:
        report("g", "Chapter 05 is missing '## Provenance' section")
    else:
        body = m.group(1)
        cite_keys: Set[str] = set()
        for raw in CITE_ROLE_RE.findall(body):
            for key in raw.split(","):
                key = key.strip()
                if key:
                    cite_keys.add(key)
        if len(cite_keys) < 3:
            report(
                "g",
                f"Chapter 05 Provenance section has only {len(cite_keys)} "
                f"distinct `{{cite}}` keys (must be ≥ 3 cross-framework cites)",
            )

    # (h) twelve H3 cells in expected order, each with ≥1 {cite} and
    # ≥1 {literalinclude}.
    h3_re = re.compile(r"^###\s+(.+?)\s*$", re.MULTILINE)
    h3_matches = list(h3_re.finditer(target.body))
    # Each cell's body = slice from this H3 start to the next H3 or next H2.
    next_h2 = re.compile(r"^##\s+", re.MULTILINE)

    def cell_body(start_idx: int, end_idx: int) -> str:
        return target.body[start_idx:end_idx]

    found_cells: List[Tuple[str, int, int]] = []
    for i, m3 in enumerate(h3_matches):
        title = m3.group(1).strip()
        start = m3.end()
        # next boundary = next H3 OR next H2, whichever comes first.
        next_boundary = len(target.body)
        if i + 1 < len(h3_matches):
            next_boundary = min(next_boundary, h3_matches[i + 1].start())
        nh2 = next_h2.search(target.body, start)
        if nh2:
            next_boundary = min(next_boundary, nh2.start())
        found_cells.append((title, start, next_boundary))

    found_keys = [_canonical_cell_key(t) for (t, _, _) in found_cells]
    missing = [c for c in _CH05_EXPECTED_CELLS if c not in found_keys]
    if missing:
        report(
            "h",
            f"Chapter 05 is missing {len(missing)} of the 12 matrix H3 cells: "
            + ", ".join(missing),
        )

    # Order: the 12 expected cells must appear in the listed order.
    filtered = [k for k in found_keys if k in _CH05_EXPECTED_CELLS]
    if filtered and filtered != _CH05_EXPECTED_CELLS[:len(filtered)]:
        # crude order check against the canonical list
        expected_sub = [c for c in _CH05_EXPECTED_CELLS if c in filtered]
        if filtered != expected_sub:
            report(
                "h",
                "Chapter 05 matrix H3 cells are out of canonical order "
                "(SDD×Bridle..Groom, TDD×Bridle..Groom, MDD×Bridle..Groom)",
            )

    # Per-cell: ≥1 {cite} + ≥1 {literalinclude}.
    for title, start, end in found_cells:
        key = _canonical_cell_key(title)
        if key not in _CH05_EXPECTED_CELLS:
            continue
        body = cell_body(start, end)
        if not CITE_ROLE_RE.search(body):
            report("h", f"Chapter 05 cell '{key}' has no `{{cite}}` role")
        if "{literalinclude}" not in body:
            report(
                "h",
                f"Chapter 05 cell '{key}' has no `{{literalinclude}}` artefact",
            )


# ---------------------------------------------------------------------------
# 13.3.j — Case-study 12-cell highlight map
# ---------------------------------------------------------------------------

def check_case_study_highlight_map(
    run: LintRun, chapters: List[ChapterInfo]
) -> None:
    """Check (j): case-study chapters must carry a 12-cell highlight map."""
    for ch in chapters:
        if ch.chapter_type != "case-study":
            continue
        # Worked-example chapters (e.g. Ch.11) carry their own four-act
        # structure with before-and-after HarnessCards rather than a single
        # 12-cell map; skip them here (check (k) enforces their shape).
        if (ch.front_matter.get("worked-example") or "").strip().lower() \
                in ("true", "yes", "1"):
            continue
        is_complete = ch.status == "complete"

        def report(msg: str, _ch: ChapterInfo = ch, _ic: bool = is_complete) -> None:
            if _ic:
                run.error("j", _ch.path, msg)
            else:
                run.warn("j", _ch.path, f"{msg} (downgraded: status={_ch.status})")

        # Find a H2 mentioning "highlight map" or "12-cell".
        h2_re = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
        map_h2 = None
        for m in h2_re.finditer(ch.body):
            title_lower = m.group(1).lower()
            if ("highlight map" in title_lower) or ("12-cell" in title_lower) \
                    or ("twelve-cell" in title_lower) \
                    or ("十二格" in title_lower and "亮点" in title_lower):
                map_h2 = m
                break
        if map_h2 is None:
            report("case-study chapter is missing a '12-cell highlight map' H2")
            continue

        # Section body up to next H2.
        start = map_h2.end()
        nxt = re.search(r"^##\s+", ch.body[start:], re.MULTILINE)
        section = ch.body[start:start + nxt.start()] if nxt else ch.body[start:]
        # Count distinct "Guardian × Zone" labels in the map.
        canonical_section = section
        for zh, en in _ZONE_ZH_TO_EN.items():
            canonical_section = canonical_section.replace(zh, en)
        covered = [c for c in _CH05_EXPECTED_CELLS if c in canonical_section]
        if len(covered) < 12:
            missing = [c for c in _CH05_EXPECTED_CELLS if c not in covered]
            report(
                "highlight map covers only "
                f"{len(covered)}/12 cells; missing: " + ", ".join(missing)
            )


# ---------------------------------------------------------------------------
# 13.3.k — Chapter 11 four-act structure + commit SHA resolution
# ---------------------------------------------------------------------------

_CH11_EXPECTED_ACTS: List[str] = [
    "Act 1", "Act 2", "Act 3", "Act 4",
]
_CH11_EXPECTED_ACT_ALIASES: Dict[str, Tuple[str, ...]] = {
    "Act 1": ("Act 1", "第一幕"),
    "Act 2": ("Act 2", "第二幕"),
    "Act 3": ("Act 3", "第三幕"),
    "Act 4": ("Act 4", "第四幕"),
}

_SHA_RE = re.compile(r"\b([0-9a-f]{7,40})\b")


def check_chapter_11_structure(run: LintRun, chapters: List[ChapterInfo],
                               repo_root: Path) -> None:
    """Check (k): Chapter 11 four-act H2 structure and commit SHA resolution."""
    target = next(
        (ch for ch in chapters if ch.path.name == "11-lazy-ai-coder.md"),
        None,
    )
    if target is None:
        return

    is_complete = target.status == "complete"

    def report(msg: str) -> None:
        if is_complete:
            run.error("k", target.path, msg)
        else:
            run.warn("k", target.path, f"{msg} (downgraded: status={target.status})")

    # Four-act order.
    act_indices: List[int] = []
    for act in _CH11_EXPECTED_ACTS:
        aliases = _CH11_EXPECTED_ACT_ALIASES[act]
        found = next(
            (
                i for i, h in enumerate(target.h2_headings)
                if any(h.startswith(alias) for alias in aliases)
            ),
            None,
        )
        if found is None:
            report(f"Chapter 11 missing mandatory H2 starting with '{act}'")
            return
        act_indices.append(found)
    if act_indices != sorted(act_indices):
        report("Chapter 11 Acts 1–4 are out of order")

    # Act 3 commit SHA resolution (only when book status is complete).
    # In draft/review, we warn on TBD / placeholder SHAs but don't fail.
    sections = _split_by_h2(target.body)
    act3_aliases = _CH11_EXPECTED_ACT_ALIASES["Act 3"]
    act3 = next(
        (
            sec for title, sec in sections
            if any(title.startswith(alias) for alias in act3_aliases)
        ),
        "",
    )
    placeholder_markers = ("TBD", "tbd", "xxxxxxx", "TODO", "<commit>")
    has_placeholder = any(p in act3 for p in placeholder_markers)

    if is_complete:
        # Try to resolve every 7-40 char hex SHA via git cat-file.
        unresolved: List[str] = []
        for sha in set(_SHA_RE.findall(act3)):
            # Filter common hex-looking words that aren't SHAs (e.g. colours).
            if len(sha) < 7:
                continue
            try:
                import subprocess
                res = subprocess.run(
                    ["git", "cat-file", "-e", sha],
                    cwd=str(repo_root),
                    capture_output=True,
                    timeout=5,
                )
                if res.returncode != 0:
                    unresolved.append(sha)
            except Exception:
                unresolved.append(sha)
        if unresolved:
            report(
                "Chapter 11 Act 3 references unresolved commit SHAs: "
                + ", ".join(unresolved[:5])
                + ("…" if len(unresolved) > 5 else "")
            )
        if has_placeholder:
            report("Chapter 11 Act 3 still contains placeholder SHAs (TBD/TODO)")
    else:
        if has_placeholder:
            run.warn(
                "k", target.path,
                "Chapter 11 Act 3 still contains placeholder SHAs (TBD/TODO) "
                f"— must be resolved before status=complete (current: {target.status})",
            )


def _split_by_h2(body: str) -> List[Tuple[str, str]]:
    """Return [(h2 title, body up to next h2)]."""
    out: List[Tuple[str, str]] = []
    current_title: Optional[str] = None
    buf: List[str] = []
    for line in body.splitlines(keepends=True):
        hm = re.match(r"^##\s+(.+?)\s*$", line)
        if hm:
            if current_title is not None:
                out.append((current_title, "".join(buf)))
            current_title = hm.group(1).strip()
            buf = []
        else:
            if current_title is not None:
                buf.append(line)
    if current_title is not None:
        out.append((current_title, "".join(buf)))
    return out


# ---------------------------------------------------------------------------
# 13.3.l — Chapter 12 conclusion structure
# ---------------------------------------------------------------------------

_CH12_REQUIRED_H2_PREFIXES = ["12.1", "12.2", "12.3"]


def check_chapter_12_structure(run: LintRun, chapters: List[ChapterInfo]) -> None:
    """Check (l): Chapter 12 conclusion mandatory sections + refs.

    • 12.1 contains ≥ 12 ``{ref}`` roles pointing into Ch.05 (cell labels).
    • 12.2 every bullet carries a matrix-cell ``{ref}`` + a ``_handson/``
      pointer; Day 61–90 sub-section references Appendix D.
    • 12.3 per-bullet ≥ 1 ``{cite}``; ≤ 7 bullets total.
    """
    target = next(
        (ch for ch in chapters if ch.path.name == "12-where-we-go-from-here.md"),
        None,
    )
    if target is None:
        return

    is_complete = target.status == "complete"

    def report(msg: str) -> None:
        if is_complete:
            run.error("l", target.path, msg)
        else:
            run.warn("l", target.path, f"{msg} (downgraded: status={target.status})")

    # Order of mandatory H2s.
    seen: Dict[str, int] = {}
    for prefix in _CH12_REQUIRED_H2_PREFIXES:
        idx = next(
            (i for i, h in enumerate(target.h2_headings) if h.startswith(prefix)),
            None,
        )
        if idx is None:
            report(f"Chapter 12 missing mandatory H2 '{prefix} ...'")
        else:
            seen[prefix] = idx
    if len(seen) == len(_CH12_REQUIRED_H2_PREFIXES):
        ordered = [seen[p] for p in _CH12_REQUIRED_H2_PREFIXES]
        if ordered != sorted(ordered):
            report(
                "Chapter 12 mandatory H2s out of order; expected "
                + " → ".join(_CH12_REQUIRED_H2_PREFIXES)
            )

    sections = dict(
        (title, body) for title, body in _split_by_h2(target.body)
    )

    def section_starting_with(prefix: str) -> Optional[str]:
        for title, body in sections.items():
            if title.startswith(prefix):
                return body
        return None

    # 12.1 ≥ 12 {ref} roles.
    s1 = section_starting_with("12.1")
    if s1 is not None:
        ref_count = len(re.findall(r"\{ref\}`[^`]+`", s1))
        if ref_count < 12:
            report(
                f"12.1 carries only {ref_count} `{{ref}}` roles; "
                "must reference all 12 Ch.05 matrix cells"
            )

    # 12.2 bullets: each bullet ≥ 1 {ref} and a `_handson/` pointer.
    s2 = section_starting_with("12.2")
    if s2 is not None:
        # A "bullet" is any line starting with "- " or "* " at col 0-3.
        bullet_re = re.compile(r"^\s{0,3}[-*]\s+(.+?)(?=\n(?:\s{0,3}[-*]\s|\s*\n|##|\Z))",
                               re.MULTILINE | re.DOTALL)
        bullets = [m.group(1) for m in bullet_re.finditer(s2)]
        missing_ref: List[int] = []
        missing_handson: List[int] = []
        for i, b in enumerate(bullets, start=1):
            if "{ref}`" not in b:
                missing_ref.append(i)
            if "_handson/" not in b:
                missing_handson.append(i)
        if missing_ref:
            report(
                f"12.2 has {len(missing_ref)} bullet(s) without a "
                f"`{{ref}}` to a Ch.05 matrix cell (bullet #s: "
                + ", ".join(str(i) for i in missing_ref[:8])
                + ")"
            )
        if missing_handson:
            report(
                f"12.2 has {len(missing_handson)} bullet(s) without a "
                f"`_handson/` pointer (bullet #s: "
                + ", ".join(str(i) for i in missing_handson[:8])
                + ")"
            )
        # Day 61–90 sub-section references Appendix D.
        day_61_90 = re.search(
            r"(###\s+Day\s*61[–\-].*?)(?=\n###|\Z)", s2, re.DOTALL | re.IGNORECASE,
        )
        if day_61_90 is None:
            report("12.2 is missing a 'Day 61–90' sub-section")
        else:
            sub = day_61_90.group(1)
            if "apd-harnesscard-template" not in sub \
                    and "Appendix D" not in sub \
                    and "harnesscard" not in sub.lower():
                report(
                    "12.2 Day 61–90 sub-section must reference Appendix D "
                    "(HarnessCard template)"
                )

    # 12.3 bullets: ≤ 7, each ≥ 1 {cite}.
    s3 = section_starting_with("12.3")
    if s3 is not None:
        bullets = re.findall(r"^\s{0,3}[-*]\s+(.+?)(?=\n(?:\s{0,3}[-*]\s|\s*\n##|\s*\n\Z))",
                             s3, re.MULTILINE | re.DOTALL)
        if len(bullets) > 7:
            report(
                f"12.3 has {len(bullets)} bullets (maximum allowed is 7)"
            )
        for i, b in enumerate(bullets, start=1):
            if "{cite" not in b:
                report(
                    f"12.3 bullet #{i} has no `{{cite}}` role "
                    "(every open question must cite prior art)"
                )


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------


def _first_h1(text: str) -> Optional[str]:
    m = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    return m.group(1) if m else None


def _first_line_containing(text: str, needle: str) -> Optional[int]:
    for idx, line in enumerate(text.splitlines(), start=1):
        if needle in line:
            return idx
    return None


def _book_rel(run: LintRun, path: Path) -> str:
    try:
        return str(path.relative_to(run.source_root))
    except ValueError:
        return str(path)


def _collect_chapters(chapters_root: Path, extras: List[Path]) -> List[ChapterInfo]:
    files: List[Path] = []
    if chapters_root.is_dir():
        files.extend(sorted(chapters_root.rglob("*.md")))
    files.extend(p for p in extras if p.is_file())
    return [scan_chapter(p) for p in files]


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Lint the Harnessing AI book source tree.")
    parser.add_argument(
        "source",
        nargs="?",
        default="source",
        type=Path,
        help="Path to source (default: %(default)s)",
    )
    args = parser.parse_args(argv)

    source_root: Path = args.source.resolve()
    if not source_root.is_dir():
        print(f"book-lint: source path not found: {source_root}", file=sys.stderr)
        return 2

    # Derive a repo root so error messages can render short paths.
    # We treat the first ancestor containing ``.git`` OR ``openspec`` as root;
    # if neither is found, fall back to the source_root.
    repo_root = source_root
    for anc in source_root.parents:
        if (anc / ".git").exists() or (anc / "openspec").exists():
            repo_root = anc
            break

    run = LintRun(source_root=source_root, repo_root=repo_root)

    bib_dir = source_root / "_bib"
    bib_files = sorted(bib_dir.glob("*.bib")) if bib_dir.is_dir() else []
    chapters_dir = source_root / "chapters"
    chapters = _collect_chapters(chapters_dir, extras=[source_root / "colophon.md"])

    # Check (a)
    owner = check_duplicate_bib_keys(run, bib_files)
    known_keys: Set[str] = set(owner.keys())

    # Checks (b), (c)
    check_cite_key_references(run, chapters, known_keys)

    # Check (e)
    check_bibkey_convention(run, bib_files)

    # Check (d)
    check_dual_track(run, chapters)

    # Check (m)
    check_appendix_order(run, chapters_dir / "13-appendices")
    check_toctree_positions(run, source_root / "index.md")

    # Check (o)
    check_book_title_drift(run)

    # Check (i) part 2
    check_tauri_chapter_misplacement(run, chapters_dir)

    # Check (n)
    check_closed_source_disclaimer(run, chapters)

    # Check (f)
    check_chapter_03_structure(run, chapters)

    # Checks (g) + (h)
    check_chapter_05_structure(run, chapters)

    # Check (j)
    check_case_study_highlight_map(run, chapters)

    # Check (k)
    check_chapter_11_structure(run, chapters, repo_root)

    # Check (l)
    check_chapter_12_structure(run, chapters)

    # ------------------------------------------------------------------
    # Render
    # ------------------------------------------------------------------
    print(f"book-lint scanning: {source_root}")
    print(f"  _bib files: {len(bib_files)}   chapters: {len(chapters)}   "
          f"known keys: {len(known_keys)}")
    print()

    if not run.findings:
        print("  no issues found.")
    else:
        # Sort: errors first, then warnings; stable within each.
        errs = [f for f in run.findings if f.level == "error"]
        warns = [f for f in run.findings if f.level == "warning"]
        for f in errs + warns:
            print("  " + f.render())

    print()
    print(f"  errors:   {run.errors}")
    print(f"  warnings: {run.warnings}")

    return 0 if run.errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
