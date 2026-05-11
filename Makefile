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
# Publish to GitHub Pages (gh-pages branch approach)
# ---------------------------------------------------------------------------
#
# We build the HTML locally with `make check` (lint + strict Sphinx), then
# force-push the build output onto a dedicated `gh-pages` branch of the
# GitHub remote. GitHub Pages on that repo must be set to:
#
#   Settings -> Pages -> Source: "Deploy from a branch"
#                         Branch: gh-pages / (root)
#
# This avoids GitHub Actions Pages permissions entirely. Pattern mirrors
# walter/webrtc_primer/tutorial/Makefile which is known to work.

PUBLISH_REMOTE      ?= origin
PUBLISH_PAGES_BRANCH?= gh-pages
# Pull the github.com slug (owner/repo) out of the remote URL — supports
# both git@github.com:owner/repo.git and https://github.com/owner/repo(.git).
# Use '|' as sed separator because '#' would start a Make comment inside
# $(shell ...). The $$ is correctly passed as $ to the shell.
PUBLISH_SLUG        ?= $(shell git remote get-url $(PUBLISH_REMOTE) 2>/dev/null | sed -E -e 's|^git@github\.com:||' -e 's|^https?://github\.com/||' -e 's|\.git$$||')
PUBLISH_OWNER       ?= $(firstword $(subst /, ,$(PUBLISH_SLUG)))
PUBLISH_REPO        ?= $(lastword $(subst /, ,$(PUBLISH_SLUG)))

publish: check ## Build, then force-push build/html/ to the gh-pages branch
	@if [ ! -d "$(BUILDDIR)/html" ]; then \
		echo "  !! $(BUILDDIR)/html/ missing after 'make check'"; exit 1; \
	fi
	@REMOTE_URL="$$(git remote get-url $(PUBLISH_REMOTE) 2>/dev/null)"; \
	if [ -z "$$REMOTE_URL" ]; then \
		echo "  !! could not resolve remote '$(PUBLISH_REMOTE)'"; exit 1; \
	fi; \
	TMPDIR="$$(mktemp -d)"; \
	trap 'rm -rf "$$TMPDIR"' EXIT; \
	cp -R "$(BUILDDIR)/html/." "$$TMPDIR/"; \
	touch "$$TMPDIR/.nojekyll"; \
	echo "  -> publishing $(BUILDDIR)/html/ to $$REMOTE_URL ($(PUBLISH_PAGES_BRANCH))"; \
	cd "$$TMPDIR" && \
		git init -q && \
		git checkout -q -b "$(PUBLISH_PAGES_BRANCH)" && \
		git add -A && \
		git -c user.name="$$(git -C "$(CURDIR)" config user.name)" \
		    -c user.email="$$(git -C "$(CURDIR)" config user.email)" \
		    commit -q -m "publish: $$(date -u +%Y-%m-%dT%H:%M:%SZ)" && \
		git push --force "$$REMOTE_URL" "$(PUBLISH_PAGES_BRANCH):$(PUBLISH_PAGES_BRANCH)"
	@echo ""
	@echo "  -> deployed site:  https://$(PUBLISH_OWNER).github.io/$(PUBLISH_REPO)/"
	@echo "     (first publish? enable Pages: https://github.com/$(PUBLISH_SLUG)/settings/pages"
	@echo "      -> Source: 'Deploy from a branch' -> Branch: '$(PUBLISH_PAGES_BRANCH)' / root)"

publish-status: ## Print URLs for the Pages settings, gh-pages branch, and deployed site
	@if [ -z "$(PUBLISH_SLUG)" ]; then \
		echo "  !! could not detect github.com slug from remote '$(PUBLISH_REMOTE)'"; \
		exit 1; \
	fi
	@echo "  Pages settings:  https://github.com/$(PUBLISH_SLUG)/settings/pages"
	@echo "  gh-pages branch: https://github.com/$(PUBLISH_SLUG)/tree/$(PUBLISH_PAGES_BRANCH)"
	@echo "  Deployed site:   https://$(PUBLISH_OWNER).github.io/$(PUBLISH_REPO)/"

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
