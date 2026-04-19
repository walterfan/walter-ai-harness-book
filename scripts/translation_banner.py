"""Sphinx extension — per-document translation-freshness banner.

Runs only when building in a non-source language (i.e. ``zh_CN``).
For each document, it inspects the matching ``.po`` file under
``source/locale/<lang>/LC_MESSAGES/`` and sets a Jinja context
variable ``translation_state`` to one of:

* ``None`` — catalog is absent AND we are rendering the source
  language. No banner.
* ``'missing'`` — catalog is absent OR empty for this document while
  rendering a translated language. Banner: "Translation in progress".
* ``'stale'`` — catalog has ``fuzzy`` entries > 0 OR untranslated
  entries ≥ 10 % of total. Banner: "Translation out of date".
* ``None`` — catalog is fully translated. No banner.

The extension is wired in via ``conf.py`` ``setup()``; if the module
import fails (e.g. in a reduced environment), conf.py falls back to a
no-op so the main build still succeeds.
"""

from __future__ import annotations

import pathlib
from typing import Any

FUZZY_THRESHOLD = 0          # any fuzzy entry → stale
UNTRANSLATED_PERCENT = 10.0  # ≥ 10% untranslated → stale


def _count_po(path: pathlib.Path) -> tuple[int, int, int]:
    total = fuzzy = untranslated = 0
    in_msgid = in_msgstr = False
    flag_fuzzy = False
    msgstr_empty = True
    msgid_empty = True

    def flush():
        nonlocal total, fuzzy, untranslated, flag_fuzzy, msgstr_empty, msgid_empty
        if not msgid_empty:
            total += 1
            if flag_fuzzy:
                fuzzy += 1
            if msgstr_empty:
                untranslated += 1
        flag_fuzzy = False
        msgstr_empty = True
        msgid_empty = True

    try:
        with path.open(encoding="utf-8") as fh:
            for raw in fh:
                line = raw.rstrip("\n")
                if line.startswith("#,") and "fuzzy" in line:
                    flag_fuzzy = True
                    continue
                if line.startswith("#") or not line.strip():
                    if not line.strip() and (in_msgid or in_msgstr):
                        flush()
                        in_msgid = in_msgstr = False
                    continue
                if line.startswith("msgid "):
                    if in_msgid or in_msgstr:
                        flush()
                    in_msgid, in_msgstr = True, False
                    msgid_empty = line == 'msgid ""'
                    continue
                if line.startswith("msgstr "):
                    in_msgid, in_msgstr = False, True
                    msgstr_empty = line == 'msgstr ""'
                    continue
                if in_msgstr and line.startswith('"') and line != '""':
                    msgstr_empty = False
                if in_msgid and line.startswith('"') and line != '""':
                    msgid_empty = False
        if in_msgid or in_msgstr:
            flush()
    except FileNotFoundError:
        return 0, 0, 0
    return total, fuzzy, untranslated


def _classify(po_path: pathlib.Path) -> str | None:
    total, fuzzy, untranslated = _count_po(po_path)
    if total == 0:
        # Either the .po is missing or it has only header entries.
        return "missing" if not po_path.exists() else "missing"
    if fuzzy > FUZZY_THRESHOLD:
        return "stale"
    if untranslated == total:
        return "missing"
    if (100.0 * untranslated / total) >= UNTRANSLATED_PERCENT:
        return "stale"
    return None


def _on_html_page_context(
    app: Any,
    pagename: str,
    templatename: str,
    context: dict,
    doctree: Any,
) -> None:
    lang = getattr(app.config, "language", "en") or "en"
    # Only annotate translated builds.
    if lang == "en":
        context.setdefault("translation_state", None)
        return
    srcdir = pathlib.Path(app.srcdir)
    po_path = srcdir / "locale" / lang / "LC_MESSAGES" / f"{pagename}.po"
    context["translation_state"] = _classify(po_path)


def configure(app: Any) -> None:
    """Public entry point called from ``conf.py:setup()``."""
    app.connect("html-page-context", _on_html_page_context)
