"""Sphinx configuration for 《驾驭工程：给 AI 套上缰绳》.

The authoritative source language is Simplified Chinese. English terms are
kept inline where they are the idiomatic engineering vocabulary, and the book
is built from one Markdown source tree.
"""

from __future__ import annotations

import os

# ---------------------------------------------------------------------------
# Project metadata
# ---------------------------------------------------------------------------

# Canonical book title. ``book-lint`` accepts this Chinese source title.
project = "驾驭工程：给 AI 套上缰绳"
# Author line — kept short for the HTML footer; full attribution lives in
# the Colophon end-page.
author = "Walter Fan"
# Copyright holder + starting year; Sphinx renders "© {copyright}".
copyright = "2026, Walter Fan"
# Semver-ish release identifier surfaced in the sidebar and HTML metadata;
# bumped manually when a named edition ships.
release = "0.1.0-draft"

# ---------------------------------------------------------------------------
# Core language settings
# ---------------------------------------------------------------------------

# Source language for search, generated labels, and theme chrome.
language = "zh_CN"

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
# Keep the directive surface small and predictable. The ``book-structure``
# spec codifies the whitelist.
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
# label; this matches the research-foundations bullet style.
bibtex_reference_style = "author_year"

# ---------------------------------------------------------------------------
# HTML output
# ---------------------------------------------------------------------------
# Read-the-Docs-style theme; widely familiar and plays well with the
# Chinese-first source tree.
html_theme = "sphinx_rtd_theme"
# Short string that surfaces in browser tabs and PDF-printed headers.
# MUST contain the substring ``Harness Engineering`` (book-lint rule).
html_title = "驾驭工程 — Harness Engineering"
# Directory containing ``custom.css`` and other static assets.
html_static_path = ["_static"]
# Override-directory for theme templates.
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

# Custom CSS loaded on every page.
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
# Sphinx build hooks.
# ---------------------------------------------------------------------------

def setup(app):  # noqa: D401 — Sphinx extension convention
    """Register book-specific build hooks.
    """
    return {
        "version": release,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
