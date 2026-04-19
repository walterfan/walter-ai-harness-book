"""Sphinx configuration for *Harnessing AI: The Craft of Shaping Agents*.

The authoritative source language is English. Simplified Chinese
(``zh_CN``) is produced as a translation via ``sphinx-intl`` gettext
catalogs under ``source/locale/zh_CN/LC_MESSAGES/``. The Chinese book
title is therefore the localized translation of the English ``project``
string below and lives only in the ``.po`` catalog — never hard-coded
in this file. See the ``docs-tooling`` spec (``book-lint`` check ``(o)``
and the "Book title drift" scenario) for the canonical rule; the
``book-lint`` tool scans this file for the forbidden substrings to
prevent accidental regressions.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Project metadata
# ---------------------------------------------------------------------------

# Canonical English book title. ``book-lint`` asserts this exact string.
project = "Harnessing AI: The Craft of Shaping Agents"
# Author line — kept short for the HTML footer; full attribution lives in
# the Colophon end-page.
author = "Walter Fan"
# Copyright holder + starting year; Sphinx renders "© {copyright}".
copyright = "2026, Walter Fan"
# Semver-ish release identifier surfaced in the sidebar and HTML metadata;
# bumped manually when a named edition ships.
release = "0.1.0-draft"

# ---------------------------------------------------------------------------
# Core language / i18n settings
# ---------------------------------------------------------------------------

# Source language. Translations live under ``locale_dirs``.
language = "en"
# Where sphinx-intl writes and reads ``.po`` catalogs; mirrors the source
# tree (one ``.po`` per source ``.md``).
locale_dirs = ["locale/"]
# Keep one ``.po`` per document so diffs stay small and PRs are reviewable;
# ``True`` would collapse the whole book into a single catalog.
gettext_compact = False
# Extract figure captions, references, and image alt text so translators
# see every user-facing string.
gettext_additional_targets = ["literal-block", "image", "index"]
# UUIDs help sphinx-intl preserve paragraph identity when the English
# source is reordered — guards against fuzzy-match avalanches.
gettext_uuid = True

# ---------------------------------------------------------------------------
# Extensions
# ---------------------------------------------------------------------------
# Order matters only for myst_parser (must precede directives it parses).
extensions = [
    # MyST Markdown is the authoring format for every chapter.
    "myst_parser",
    # "Copy" button on every fenced code block.
    "sphinx_copybutton",
    # Grid, card, and tab components used in the HarnessCard template.
    "sphinx_design",
    # Flowcharts / sequence / state diagrams rendered in-browser.
    "sphinxcontrib.mermaid",
    # Mindmaps and larger architecture diagrams rendered server-side.
    "sphinxcontrib.plantuml",
    # Citations rendered from ``_bib/*.bib`` files via the ``{cite}`` role.
    "sphinxcontrib.bibtex",
]

# ---------------------------------------------------------------------------
# MyST settings
# ---------------------------------------------------------------------------
# Keep the directive surface small and predictable so gettext round-trips
# stay stable. The ``book-structure`` spec codifies the whitelist.
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "substitution",
    "tasklist",
    "attrs_inline",
]
# Generate automatic IDs up to H3 so ``{ref}`` links from the Ch.12
# cheat sheet and from case-study highlight maps resolve.
myst_heading_anchors = 3

# ---------------------------------------------------------------------------
# Bibliography (sphinxcontrib-bibtex)
# ---------------------------------------------------------------------------
# Every citation in the book MUST resolve to an entry in one of these
# files. ``book-lint`` asserts uniqueness across the four files.
bibtex_bibfiles = [
    "_bib/papers.bib",
    "_bib/industry.bib",
    "_bib/essays.bib",
    "_bib/tools.bib",
]
# Alphabetical-style labels (e.g. ``[Kar25]``) read better in a long-form
# book than plain numeric labels.
bibtex_default_style = "alpha"
# The in-text citation renders as "Karpathy (2025)" rather than a bare
# label; this matches the Research Foundations bullet style.
bibtex_reference_style = "author_year"

# ---------------------------------------------------------------------------
# HTML output
# ---------------------------------------------------------------------------
# Read-the-Docs-style theme; widely familiar and plays well with the
# two-language sidebar switcher injected via ``_templates/layout.html``.
html_theme = "sphinx_rtd_theme"
# Short string that surfaces in browser tabs and PDF-printed headers.
# MUST contain the substring ``Harness Engineering`` (book-lint rule).
html_title = "Harnessing AI — Harness Engineering"
# Directory containing ``custom.css``, ``lang-redirect.js``, and other
# static assets.
html_static_path = ["_static"]
# Override-directory for theme templates (e.g. ``layout.html``).
templates_path = ["_templates"]

# Hands-on artefacts and bibliographic sources live next to the prose so
# authors can reference them with ``{literalinclude}``, but they are not
# standalone pages — excluding them here keeps them out of the toctree and
# silences ``toc.not_included`` warnings.
exclude_patterns = [
    "_handson/**",
    "_bib/**",
    "_diagrams/**",
]

# Custom CSS loaded on every page; styles the language switcher.
html_css_files = ["custom.css"]
# Options tuned for a long-form narrative: collapse deep TOCs, show
# sticky navigation, and hide the "View page source" link since readers
# are pointed to the repo via the Colophon instead.
html_theme_options = {
    "navigation_depth": 2,
    "collapse_navigation": True,
    "sticky_navigation": True,
    # `display_version` was removed in sphinx_rtd_theme 3.x; the release
    # is now surfaced via `html_context` if desired.
    "prev_next_buttons_location": "bottom",
}
# Turn off the default "View source" link; we point readers at the repo
# instead via the Colophon end-page.
html_show_sourcelink = False

# ---------------------------------------------------------------------------
# Mermaid / PlantUML
# ---------------------------------------------------------------------------
# Render Mermaid via the bundled client-side script; zero server deps.
mermaid_version = "10.9.1"
# PlantUML JAR is resolved at build time; override via the
# ``PLANTUML`` environment variable if the default system install differs.
plantuml = os.environ.get("PLANTUML", "plantuml")
# Emit SVG so diagrams scale with the reader's font size.
plantuml_output_format = "svg"

# ---------------------------------------------------------------------------
# Strict-mode knobs (complement ``sphinx-build -W``)
# ---------------------------------------------------------------------------
# Fail the build on any missing cross-reference; the ``book-lint`` script
# runs after the build and depends on a clean warning set.
nitpicky = True
# These reference domains are known-unstable and are whitelisted from
# ``nitpicky`` complaints so the build stays green.
nitpick_ignore = [
    ("py:class", "optional"),
    ("myst", "xref"),
]

# ---------------------------------------------------------------------------
# Sphinx build hooks (registered in a later task; 13.4 in tasks.md).
# This section reserves the hookup point so future `make book-lint`
# integration lands in a single, obvious location.
# ---------------------------------------------------------------------------

# Make the ``scripts/`` directory importable so book_lint.py and
# forthcoming dual-track-check hooks can be wired in via ``setup(app)``.
_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if _SCRIPTS_DIR.is_dir() and str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))


def setup(app):  # noqa: D401 — Sphinx extension convention
    """Register book-specific build hooks.

    This is intentionally a thin shim so the heavy lifting can land in
    ``scripts/book_lint.py`` (task 13.4) without churning ``conf.py``.
    """
    # Translation-freshness banner context. A later task (§3.5) fills in
    # the implementation; until then the hook is a no-op so the build
    # stays green.
    try:
        from translation_banner import configure  # type: ignore
    except ImportError:
        pass
    else:
        configure(app)

    return {
        "version": release,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
