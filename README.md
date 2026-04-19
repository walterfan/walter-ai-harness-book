# Harnessing AI: The Craft of Shaping Agents
## 《驾驭工程：给 AI 套上缰绳》

A long-form, bilingual (English source + Simplified Chinese translation) technical book about **Harness Engineering** — the deliberate practice of shaping the environment in which AI coding agents operate so the software they produce is verifiable, observable, and understandable.

This directory holds the Sphinx + MyST + `sphinx-intl` + `sphinxcontrib-bibtex` source. Once built, the site is published at `book/build/html/{en,zh_CN}/`; run `make book-html` from the repository root to produce it locally.

## Quick build

From the repository root:

```bash
make book-install       # one-time: poetry install into the book's own venv
make book-html          # build en/ and zh_CN/ HTML trees
make book-intl          # regenerate .pot + merge zh_CN .po catalogs
make book-lint          # structural + bibliography checks
make book-serve         # serve book/build/html/ at http://localhost:8000
make book-livehtml      # live-reload preview via sphinx-autobuild
make book-shell         # drop into a sub-shell with the book's venv activated
```

## Toolchain: Poetry

The book has its own [`pyproject.toml`](./pyproject.toml) so the Sphinx toolchain stays isolated from the repo-root Go/test environment. Poetry picks up this file automatically; every `book-*` Makefile target invokes its command as `poetry --directory=book run ...`, which means:

- There is **no** `book/.venv` to activate by hand — `poetry run` handles it.
- The repo-root `VIRTUAL_ENV` (if set, e.g. `wfenv`) is stripped before each call so Poetry always resolves to the book's own virtualenv.
- Adding a dependency is `poetry add --directory=book <pkg>`; removing is `poetry remove`.

### pip fallback

Contributors (or CI jobs) without Poetry can use the auto-exported [`requirements-docs.txt`](./requirements-docs.txt):

```bash
python3 -m venv book/.venv
source book/.venv/bin/activate
pip install -r book/requirements-docs.txt
```

To refresh the fallback file from the current `poetry.lock`:

```bash
poetry self add poetry-plugin-export    # one-time
make book-export-requirements
```

See `CONTRIBUTING.md` (added in a later task) for authoring conventions, the MyST directive whitelist, the three-guardian × four-zone cell rubric, and the translation workflow.
