# Makefile for lazy-code-kb-book — *Harnessing AI: The Craft of Shaping Agents*
#
# Flat layout: Sphinx sources in ./source, helper scripts in ./scripts,
# Poetry metadata (pyproject.toml / poetry.lock / poetry.toml) at the root,
# build output in ./build. The Poetry virtualenv lives at ./.venv
# (configured via poetry.toml: virtualenvs.in-project = true).
#
# Every build / serve / lint target is routed through `poetry run` so the
# toolchain never pollutes the ambient Python. When called from inside
# `poetry shell` / `poetry env activate` (POETRY_ACTIVE=1) the `poetry run`
# prefix is stripped automatically, so `make html` is ergonomic either way.
#
# Quick start:
#
#   make install          # poetry install (one-time)
#   make html             # sphinx-build en + zh_CN (strict)
#   make serve            # serve build/html/ at http://localhost:8000
#   make livehtml         # live-reload preview (English) via sphinx-autobuild
#   make lint             # structural + bibliography checks
#   make intl             # regenerate .pot + merge zh_CN .po catalogs
#   make clean            # remove build/
#   make check            # lint + full html build (CI entry point)
#
# Every short target is mirrored as `book-<name>` for compatibility with
# external callers / prior docs that used the delegator layout.

SPHINXOPTS      ?= -W --keep-going -n
SPHINXBUILD     ?= sphinx-build
SPHINXAUTOBUILD ?= sphinx-autobuild
SOURCEDIR       ?= source
BUILDDIR        ?= build
LANGUAGES       ?= en zh_CN
PORT            ?= 8000
HOST            ?= 127.0.0.1

# Auto-wrap every tool invocation in `poetry run` unless we are already
# inside the venv (Poetry exports POETRY_ACTIVE=1 in that case).
POETRY          ?= poetry
ifndef POETRY_ACTIVE
SPHINXBUILD     := $(POETRY) run $(SPHINXBUILD)
SPHINXAUTOBUILD := $(POETRY) run $(SPHINXAUTOBUILD)
PY              := $(POETRY) run python
SPHINXINTL      := $(POETRY) run sphinx-intl
else
PY              := python
SPHINXINTL      := sphinx-intl
endif

.DEFAULT_GOAL := help

.PHONY: help check \
        install export-requirements shell \
        clean \
        html html-en html-zh \
        gettext update-po build-i18n intl \
        livehtml serve \
        lint linkcheck \
        book-install book-export-requirements book-shell \
        book-clean \
        book-html book-html-en book-html-zh \
        book-gettext book-update-po book-intl book-build-i18n \
        book-livehtml book-serve \
        book-lint book-linkcheck

help: ## Show available targets
	@echo 'lazy-code-kb-book — Sphinx build targets (auto-wrapped in `poetry run`)'
	@echo ''
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z][a-zA-Z0-9_-]*:.*?## / {printf "  %-26s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ''
	@echo 'Tunable variables:  PORT=$(PORT)  HOST=$(HOST)  SPHINXOPTS="$(SPHINXOPTS)"'

# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

install: ## Create/refresh the Poetry virtualenv (./.venv)
	$(POETRY) install --with dev
	@echo "  -> poetry env ready at $$($(POETRY) env info --path 2>/dev/null || echo .venv)"

export-requirements: ## Refresh requirements-docs.txt from poetry.lock (pip fallback)
	@$(POETRY) self show plugins 2>/dev/null | grep -q poetry-plugin-export \
		|| { echo "  !! poetry-plugin-export not installed."; \
		     echo "     install it once with:  poetry self add poetry-plugin-export"; \
		     exit 1; }
	$(POETRY) export --without-hashes --with dev -f requirements.txt -o requirements-docs.txt
	@echo "  -> wrote requirements-docs.txt"

shell: ## Drop into a sub-shell with the venv activated
	@# Poetry 2.x moved `poetry shell` into the poetry-plugin-shell plugin;
	@# prefer the built-in `poetry env activate` when available.
	@if $(POETRY) env activate --help >/dev/null 2>&1; then \
		$(POETRY) env activate; \
	elif $(POETRY) shell --help >/dev/null 2>&1; then \
		$(POETRY) shell; \
	else \
		echo "  !! neither 'poetry env activate' nor 'poetry shell' is available."; \
		echo "     install the shell plugin:  poetry self add poetry-plugin-shell"; \
		exit 1; \
	fi

# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

clean: ## Remove build/ output
	rm -rf "$(BUILDDIR)"

html-en: ## Build the English HTML tree at build/html/en/
	$(SPHINXBUILD) -b html -D language=en "$(SOURCEDIR)" "$(BUILDDIR)/html/en" $(SPHINXOPTS)

# `sphinx-intl build` compiles .po -> .mo. .mo files are gitignored so we
# always regenerate before a Chinese build. Idempotent and fast.
html-zh: ## Build the Simplified Chinese HTML tree at build/html/zh_CN/ (recompiles .mo)
	$(SPHINXINTL) build -d "$(SOURCEDIR)/locale"
	$(SPHINXBUILD) -b html -D language=zh_CN "$(SOURCEDIR)" "$(BUILDDIR)/html/zh_CN" $(SPHINXOPTS)

html: html-en html-zh ## Build both language HTML trees (strict, recompiles .mo)
	@if [ -f "$(SOURCEDIR)/_static/root-index.html.template" ]; then \
		cp "$(SOURCEDIR)/_static/root-index.html.template" "$(BUILDDIR)/html/index.html"; \
		echo "  -> wrote $(BUILDDIR)/html/index.html (language chooser)"; \
	fi

# ---------------------------------------------------------------------------
# Internationalisation
# ---------------------------------------------------------------------------

gettext: ## Extract translatable strings to build/gettext/*.pot
	$(SPHINXBUILD) -b gettext "$(SOURCEDIR)" "$(BUILDDIR)/gettext" $(SPHINXOPTS)

update-po: gettext ## Merge new strings into source/locale/zh_CN/LC_MESSAGES/*.po
	$(SPHINXINTL) update -p "$(BUILDDIR)/gettext" -l zh_CN -d "$(SOURCEDIR)/locale"
	@echo "  -> updated $(SOURCEDIR)/locale/zh_CN/LC_MESSAGES/"

build-i18n: update-po ## Regenerate .pot + merge zh_CN .po and summarise coverage
	$(PY) scripts/po_summary.py "$(SOURCEDIR)/locale/zh_CN/LC_MESSAGES"

intl: build-i18n ## Alias: build-i18n

# ---------------------------------------------------------------------------
# Preview & serve
# ---------------------------------------------------------------------------

livehtml: ## Serve the English build with auto-reload on change (sphinx-autobuild)
	$(SPHINXAUTOBUILD) --host $(HOST) --port $(PORT) "$(SOURCEDIR)" "$(BUILDDIR)/html/en" $(SPHINXOPTS)

serve: ## Serve build/html/ statically at http://$(HOST):$(PORT)/
	@if [ ! -d "$(BUILDDIR)/html" ]; then \
		echo "  !! $(BUILDDIR)/html/ does not exist — run 'make html' first"; \
		exit 1; \
	fi
	@echo "  -> serving $(BUILDDIR)/html/ at http://$(HOST):$(PORT)/"
	@echo "     (Ctrl-C to stop)"
	$(PY) -m http.server $(PORT) --bind $(HOST) --directory "$(BUILDDIR)/html"

# ---------------------------------------------------------------------------
# Quality gates
# ---------------------------------------------------------------------------

lint: ## Run structural + bibliographic lint (scripts/book_lint.py)
	$(PY) scripts/book_lint.py "$(SOURCEDIR)"

linkcheck: ## Report dead external links without failing the main build
	$(SPHINXBUILD) -b linkcheck "$(SOURCEDIR)" "$(BUILDDIR)/linkcheck"

check: lint html ## Lint + full build (used by CI)

# ---------------------------------------------------------------------------
# `book-*` aliases — compatibility with prior docs / the (now removed)
# top-level delegator layout. Each alias dispatches to its short target.
# ---------------------------------------------------------------------------

book-install:              install              ## Alias: install
book-export-requirements:  export-requirements  ## Alias: export-requirements
book-shell:                shell                ## Alias: shell
book-clean:                clean                ## Alias: clean
book-html:                 html                 ## Alias: html
book-html-en:              html-en              ## Alias: html-en
book-html-zh:              html-zh              ## Alias: html-zh
book-gettext:              gettext              ## Alias: gettext
book-update-po:            update-po            ## Alias: update-po
book-build-i18n:           build-i18n           ## Alias: build-i18n
book-intl:                 intl                 ## Alias: intl
book-livehtml:             livehtml             ## Alias: livehtml
book-serve:                serve                ## Alias: serve
book-lint:                 lint                 ## Alias: lint
book-linkcheck:            linkcheck            ## Alias: linkcheck
