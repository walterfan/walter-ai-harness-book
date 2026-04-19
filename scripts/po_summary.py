#!/usr/bin/env python3
"""Summarize .po catalog state for ``make book-i18n``.

Scans a directory tree of ``.po`` files and prints a per-file breakdown
of translated / fuzzy / untranslated entries, followed by a totals line.
Uses only the Python standard library so it runs inside the book venv
without extra deps.
"""

from __future__ import annotations

import pathlib
import sys


def count_po(path: pathlib.Path) -> tuple[int, int, int]:
    """Return ``(total, fuzzy, untranslated)`` message counts for a .po file.

    A `.po` entry is considered untranslated when its ``msgstr ""`` line
    is empty (for singular strings) and fuzzy when its preceding comment
    block contains a ``#, fuzzy`` flag. The parser here is intentionally
    lightweight — it ignores plural forms since Chinese is single-form
    for our purposes; refine later if plurals are introduced.
    """
    total = fuzzy = untranslated = 0
    in_msgid = in_msgstr = False
    flag_fuzzy = False
    msgstr_empty = True
    msgid_empty = True

    def flush():
        nonlocal total, fuzzy, untranslated, flag_fuzzy, msgstr_empty, msgid_empty
        # Skip the file header (the single empty-msgid entry at the top).
        if not msgid_empty:
            total += 1
            if flag_fuzzy:
                fuzzy += 1
            if msgstr_empty:
                untranslated += 1
        flag_fuzzy = False
        msgstr_empty = True
        msgid_empty = True

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
    return total, fuzzy, untranslated


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: po_summary.py <LC_MESSAGES-dir>", file=sys.stderr)
        return 2
    root = pathlib.Path(argv[1])
    if not root.is_dir():
        print(f"po_summary: {root} is not a directory", file=sys.stderr)
        return 1

    files = sorted(root.rglob("*.po"))
    if not files:
        print(f"i18n summary: no .po files under {root}")
        print("  (expected — run `make book-intl` to create catalogs)")
        return 0

    print(f"i18n summary — {len(files)} .po file(s) under {root}")
    print(f"  {'file':<60} {'total':>6} {'fuzzy':>6} {'untx':>6}")
    grand_total = grand_fuzzy = grand_untx = 0
    for p in files:
        total, fuzzy, untx = count_po(p)
        grand_total += total
        grand_fuzzy += fuzzy
        grand_untx += untx
        rel = p.relative_to(root)
        print(f"  {str(rel):<60} {total:>6} {fuzzy:>6} {untx:>6}")
    translated = grand_total - grand_fuzzy - grand_untx
    pct = (100.0 * translated / grand_total) if grand_total else 0.0
    print(f"  {'TOTAL':<60} {grand_total:>6} {grand_fuzzy:>6} {grand_untx:>6}")
    print(f"  Translated: {translated} ({pct:.1f}%)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
