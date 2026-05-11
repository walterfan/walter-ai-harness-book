# Makefile for async-harness-book — *Harnessing AI: The Craft of Shaping Agents*
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
#   make html             # sphinx-build (strict)
#   make serve            # serve build/html/ at http://localhost:8000
#   make livehtml         # live-reload preview via sphinx-autobuild
#   make lint             # structural + bibliography checks
#   make clean            # remove build/
#   make check            # lint + full html build (CI entry point)
#
# Every short target is mirrored as `book-<name>` for compatibility with
# external callers / prior docs that used the delegator layout.

SPHINXOPTS      ?= -W --keep-going -n
# Bare commands here: `ifndef POETRY_ACTIVE` below prepends `poetry run` once.
# If these defaults already included `poetry run`, the result would be
# `poetry run poetry run sphinx-build`, which can leave extensions unresolved.
SPHINXBUILD     ?= sphinx-build
SPHINXAUTOBUILD ?= sphinx-autobuild
SOURCEDIR       ?= source
BUILDDIR        ?= build
PORT            ?= 7800
HOST            ?= 127.0.0.1

# Auto-wrap every tool invocation in `poetry run` unless we are already
# inside the venv (Poetry exports POETRY_ACTIVE=1 in that case).
POETRY          ?= poetry
ifndef POETRY_ACTIVE
SPHINXBUILD     := $(POETRY) run $(SPHINXBUILD)
SPHINXAUTOBUILD := $(POETRY) run $(SPHINXAUTOBUILD)
PY              := $(POETRY) run python
else
PY              := python
endif

.DEFAULT_GOAL := help

.PHONY: help check \
        install export-requirements shell \
        clean \
        html \
        livehtml serve \
        lint linkcheck \
        publish publish-status \
        book-install book-export-requirements book-shell \
        book-clean \
        book-html \
        book-livehtml book-serve \
        book-lint book-linkcheck \
        book-publish book-publish-status

help: ## Show available targets
	@echo 'async-harness-book — Sphinx build targets (auto-wrapped in `poetry run`)'
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
	@echo "  -> after renaming the repo directory: $(POETRY) env remove --all && $(POETRY) install --with dev  (fixes stale .venv shebangs)"

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

html: ## Build the HTML tree at build/html/ (strict)
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

# ---------------------------------------------------------------------------
# Preview & serve
# ---------------------------------------------------------------------------

livehtml: ## Serve the build with auto-reload on change (sphinx-autobuild)
	$(SPHINXAUTOBUILD) --host $(HOST) --port $(PORT) "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

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
# Publish to GitHub Pages
# ---------------------------------------------------------------------------
#
# The actual build + deploy happens in .github/workflows/publish.yml on the
# GitHub runner, triggered by a push to one of the watched branches.
# `make publish` runs the same checks locally (lint + html) to fail fast on
# broken sources, then pushes the current branch so CI deploys it.
#
# Prerequisites (one-time):
#   - GitHub Pages enabled in repo Settings -> Pages -> Source: "GitHub Actions"
#   - The active branch is one of the branches in publish.yml (main/master)
#   - `origin` points at the GitHub remote and you can push to it

PUBLISH_REMOTE   ?= origin
PUBLISH_BRANCH   ?= $(shell git rev-parse --abbrev-ref HEAD 2>/dev/null)
# Pull the github.com slug (owner/repo) out of the remote URL — supports
# both git@github.com:owner/repo.git and https://github.com/owner/repo(.git).
# Use '|' as sed separator because '#' would start a Make comment inside
# $(shell ...). The $$ is correctly passed as $ to the shell.
PUBLISH_SLUG     ?= $(shell git remote get-url $(PUBLISH_REMOTE) 2>/dev/null | sed -E -e 's|^git@github\.com:||' -e 's|^https?://github\.com/||' -e 's|\.git$$||')
PUBLISH_OWNER    ?= $(firstword $(subst /, ,$(PUBLISH_SLUG)))
PUBLISH_REPO     ?= $(lastword $(subst /, ,$(PUBLISH_SLUG)))

publish: check ## Lint + build, then push current branch so CI deploys to GitHub Pages
	@if [ -z "$(PUBLISH_BRANCH)" ]; then \
		echo "  !! could not detect current git branch"; exit 1; \
	fi
	@case " main master " in *" $(PUBLISH_BRANCH) "*) ;; *) \
		echo "  !! current branch '$(PUBLISH_BRANCH)' is not in publish.yml triggers (main, master)."; \
		echo "     Either switch branch or update .github/workflows/publish.yml."; \
		exit 1; \
	esac
	@if ! git diff --quiet || ! git diff --cached --quiet; then \
		echo "  !! working tree has uncommitted changes. Commit them first:"; \
		echo "       git add -A && git commit -m '...'"; \
		echo "     Then re-run 'make publish'."; \
		exit 1; \
	fi
	@echo "  -> pushing $(PUBLISH_BRANCH) to $(PUBLISH_REMOTE) (this triggers .github/workflows/publish.yml)"
	git push "$(PUBLISH_REMOTE)" "$(PUBLISH_BRANCH)"
	@echo ""
	@echo "  -> workflow runs:  https://github.com/$(PUBLISH_SLUG)/actions/workflows/publish.yml"
	@echo "  -> deployed site:  https://$(PUBLISH_OWNER).github.io/$(PUBLISH_REPO)/"

publish-status: ## Print URLs to view publish workflow runs and deployed site
	@if [ -z "$(PUBLISH_SLUG)" ]; then \
		echo "  !! could not detect github.com slug from remote '$(PUBLISH_REMOTE)'"; \
		exit 1; \
	fi
	@echo "  Workflow runs:  https://github.com/$(PUBLISH_SLUG)/actions/workflows/publish.yml"
	@echo "  Pages settings: https://github.com/$(PUBLISH_SLUG)/settings/pages"
	@echo "  Deployed site:  https://$(PUBLISH_OWNER).github.io/$(PUBLISH_REPO)/"

# Compatibility aliases for callers that use the book-* target names.
book-install: install
book-export-requirements: export-requirements
book-shell: shell
book-clean: clean
book-html: html
book-livehtml: livehtml
book-serve: serve
book-lint: lint
book-linkcheck: linkcheck
book-publish: publish
book-publish-status: publish-status
