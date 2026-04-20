# Harnessing AI: The Craft of Shaping Agents
## 《驾驭工程：给 AI 套上缰绳》

A long-form, bilingual (English source + Simplified Chinese translation) technical book about **Harness Engineering** — the deliberate practice of shaping the environment in which AI coding agents operate so the software they produce is verifiable, observable, and understandable.

This repository holds the Sphinx + MyST + `sphinx-intl` + `sphinxcontrib-bibtex` source. Once built, the site is published at `build/html/{en,zh_CN}/`; run `make html` to produce it locally.

## Quick build

```bash
make install       # one-time: poetry install into ./.venv
make html          # build en/ and zh_CN/ HTML trees (strict, recompiles .mo)
make serve         # serve build/html/ at http://localhost:8000
make livehtml      # live-reload preview (English) via sphinx-autobuild
make lint          # structural + bibliography checks
make intl          # regenerate .pot + merge zh_CN .po catalogs
make check         # lint + full html build (CI entry point)
make clean         # remove build/
```

Run `make help` for the full target list, including single-language
builds (`html-en`, `html-zh`), `gettext`, `update-po`, `linkcheck`, and
`export-requirements`.

All `book-*` aliases (e.g. `make book-html`, `make book-serve`) remain
accepted for compatibility with earlier docs.

## Toolchain: Poetry

The Sphinx toolchain is managed by [`pyproject.toml`](./pyproject.toml) + [`poetry.lock`](./poetry.lock). The virtualenv is kept **in-project** (see [`poetry.toml`](./poetry.toml): `virtualenvs.in-project = true`) so it lives at `./.venv/`. Every Makefile target auto-wraps its command in `poetry run`, which means:

- There is **no** `.venv` to activate by hand — `make html` works from a plain shell.
- Inside `poetry shell` / `poetry env activate` the `poetry run` prefix is stripped automatically (detected via `POETRY_ACTIVE`), so `make html` stays ergonomic either way.
- Adding a dependency: `poetry add <pkg>`; removing: `poetry remove <pkg>`.

### pip fallback

Contributors or CI jobs without Poetry can use the auto-exported [`requirements-docs.txt`](./requirements-docs.txt):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt
```

To refresh `requirements-docs.txt` from the current `poetry.lock`:

```bash
poetry self add poetry-plugin-export    # one-time
make export-requirements
```

See `CONTRIBUTING.md` (added in a later task) for authoring conventions, the MyST directive whitelist, the three-guardian × four-zone cell rubric, and the translation workflow.
