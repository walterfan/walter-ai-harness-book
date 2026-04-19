# Makefile for the "Harnessing AI / 驾驭工程" Sphinx book.
#
# The repo root exposes higher-level targets (book-install / book-html /
# book-i18n / book-serve / book-clean / book-lint) that delegate here.
# Direct usage from this directory is also supported for iterative
# authoring; see `make help`.

SPHINXOPTS      ?= -W --keep-going -n
SPHINXBUILD     ?= sphinx-build
SOURCEDIR       = source
BUILDDIR        = build
LANGUAGES       ?= en zh_CN

.PHONY: help clean html html-en html-zh gettext update-po build-i18n livehtml linkcheck

help: ## Show available targets
	@echo 'Harnessing AI — book build targets'
	@echo ''
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-18s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

clean: ## Remove build/ output
	rm -rf "$(BUILDDIR)"

html-en: ## Build the English HTML tree at build/html/en/
	$(SPHINXBUILD) -b html -D language=en "$(SOURCEDIR)" "$(BUILDDIR)/html/en" $(SPHINXOPTS)

html-zh: ## Build the Simplified Chinese HTML tree at build/html/zh_CN/
	$(SPHINXBUILD) -b html -D language=zh_CN "$(SOURCEDIR)" "$(BUILDDIR)/html/zh_CN" $(SPHINXOPTS)

html: html-en html-zh ## Build both language HTML trees
	@if [ -f "$(SOURCEDIR)/_static/root-index.html.template" ]; then \
		cp "$(SOURCEDIR)/_static/root-index.html.template" "$(BUILDDIR)/html/index.html"; \
		echo "  -> wrote $(BUILDDIR)/html/index.html (language chooser)"; \
	fi

gettext: ## Extract translatable strings to build/gettext/*.pot
	$(SPHINXBUILD) -b gettext "$(SOURCEDIR)" "$(BUILDDIR)/gettext" $(SPHINXOPTS)

update-po: gettext ## Merge new strings into source/locale/zh_CN/LC_MESSAGES/*.po
	sphinx-intl update -p "$(BUILDDIR)/gettext" -l zh_CN -d "$(SOURCEDIR)/locale"
	@echo "  -> updated source/locale/zh_CN/LC_MESSAGES/"

build-i18n: update-po ## Regenerate .pot + merge into zh_CN .po and summarize
	@python3 scripts/po_summary.py "$(SOURCEDIR)/locale/zh_CN/LC_MESSAGES"

livehtml: ## Serve the English build with auto-reload on change
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html/en" $(SPHINXOPTS)

linkcheck: ## Report dead external links without failing the main build
	$(SPHINXBUILD) -b linkcheck "$(SOURCEDIR)" "$(BUILDDIR)/linkcheck"
