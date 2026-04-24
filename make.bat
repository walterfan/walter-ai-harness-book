@ECHO OFF
REM Windows helper for async-harness-book — Harnessing AI Sphinx book.
REM
REM Flat layout: source/ scripts/ pyproject.toml poetry.lock poetry.toml at
REM the repo root; build output at build/. Every command is routed through
REM `poetry run` so the Poetry virtualenv (./.venv) is always used.
REM
REM macOS / Linux authors should prefer `make <target>`.

setlocal
pushd %~dp0

if "%SPHINXBUILD%" == "" set SPHINXBUILD=sphinx-build
if "%SPHINXAUTOBUILD%" == "" set SPHINXAUTOBUILD=sphinx-autobuild
set SOURCEDIR=source
set BUILDDIR=build
set SPHINXOPTS=-W --keep-going -n
if "%PORT%" == "" set PORT=8000
if "%HOST%" == "" set HOST=127.0.0.1

if "%1" == "" goto help

if /I "%1" == "help"                 goto help
if /I "%1" == "install"              goto install
if /I "%1" == "book-install"         goto install
if /I "%1" == "export-requirements"  goto export_requirements
if /I "%1" == "book-export-requirements" goto export_requirements
if /I "%1" == "clean"                goto clean
if /I "%1" == "book-clean"           goto clean
if /I "%1" == "html"                 goto html
if /I "%1" == "book-html"            goto html
if /I "%1" == "html-en"              goto html_en
if /I "%1" == "book-html-en"         goto html_en
if /I "%1" == "html-zh"              goto html_zh
if /I "%1" == "book-html-zh"         goto html_zh
if /I "%1" == "gettext"              goto gettext
if /I "%1" == "book-gettext"         goto gettext
if /I "%1" == "update-po"            goto update_po
if /I "%1" == "book-update-po"       goto update_po
if /I "%1" == "build-i18n"           goto build_i18n
if /I "%1" == "book-build-i18n"      goto build_i18n
if /I "%1" == "intl"                 goto build_i18n
if /I "%1" == "book-intl"            goto build_i18n
if /I "%1" == "serve"                goto serve
if /I "%1" == "book-serve"           goto serve
if /I "%1" == "livehtml"             goto livehtml
if /I "%1" == "book-livehtml"        goto livehtml
if /I "%1" == "lint"                 goto lint
if /I "%1" == "book-lint"            goto lint
if /I "%1" == "linkcheck"            goto linkcheck
if /I "%1" == "book-linkcheck"       goto linkcheck
if /I "%1" == "check"                goto check

echo Unknown target: %1
goto help

:install
poetry install --with dev
goto end

:export_requirements
poetry export --without-hashes --with dev -f requirements.txt -o requirements-docs.txt
echo   -^> wrote requirements-docs.txt
goto end

:clean
if exist %BUILDDIR% rd /s /q %BUILDDIR%
goto end

:html_en
poetry run %SPHINXBUILD% -b html -D language=en %SOURCEDIR% %BUILDDIR%\html\en %SPHINXOPTS%
goto end

:html_zh
poetry run sphinx-intl build -d %SOURCEDIR%\locale
if errorlevel 1 goto end
poetry run %SPHINXBUILD% -b html -D language=zh_CN %SOURCEDIR% %BUILDDIR%\html\zh_CN %SPHINXOPTS%
goto end

:html
poetry run sphinx-intl build -d %SOURCEDIR%\locale
if errorlevel 1 goto end
poetry run %SPHINXBUILD% -b html -D language=en %SOURCEDIR% %BUILDDIR%\html\en %SPHINXOPTS%
if errorlevel 1 goto end
poetry run %SPHINXBUILD% -b html -D language=zh_CN %SOURCEDIR% %BUILDDIR%\html\zh_CN %SPHINXOPTS%
if errorlevel 1 goto end
if exist %SOURCEDIR%\_static\root-index.html.template (
    copy /Y %SOURCEDIR%\_static\root-index.html.template %BUILDDIR%\html\index.html >nul
    echo   -^> wrote %BUILDDIR%\html\index.html
)
goto end

:gettext
poetry run %SPHINXBUILD% -b gettext %SOURCEDIR% %BUILDDIR%\gettext %SPHINXOPTS%
goto end

:update_po
call :gettext
if errorlevel 1 goto end
poetry run sphinx-intl update -p %BUILDDIR%\gettext -l zh_CN -d %SOURCEDIR%\locale
goto end

:build_i18n
call :update_po
if errorlevel 1 goto end
poetry run python scripts\po_summary.py %SOURCEDIR%\locale\zh_CN\LC_MESSAGES
goto end

:serve
if not exist %BUILDDIR%\html (
    echo   !! %BUILDDIR%\html\ does not exist -- run `make.bat html` first
    goto end
)
echo   -^> serving %BUILDDIR%\html\ at http://%HOST%:%PORT%/
poetry run python -m http.server %PORT% --bind %HOST% --directory %BUILDDIR%\html
goto end

:livehtml
poetry run %SPHINXAUTOBUILD% --host %HOST% --port %PORT% %SOURCEDIR% %BUILDDIR%\html\en %SPHINXOPTS%
goto end

:lint
poetry run python scripts\book_lint.py %SOURCEDIR%
goto end

:linkcheck
poetry run %SPHINXBUILD% -b linkcheck %SOURCEDIR% %BUILDDIR%\linkcheck
goto end

:check
call :lint
if errorlevel 1 goto end
call :html
goto end

:help
echo async-harness-book - Sphinx build helper (poetry run)
echo.
echo Targets:
echo   install             - poetry install (one-time)
echo   html                - build en/ + zh_CN/ HTML trees
echo   html-en             - build English HTML only
echo   html-zh             - build Simplified Chinese HTML only
echo   serve               - serve build\html\ at http://%HOST%:%PORT%/
echo   livehtml            - live-reload preview (English) via sphinx-autobuild
echo   gettext             - extract translatable strings
echo   update-po           - regenerate + merge zh_CN .po
echo   build-i18n / intl   - update-po + summarise translation coverage
echo   lint                - run scripts\book_lint.py
echo   linkcheck           - report dead external links
echo   check               - lint + html (CI)
echo   clean               - remove build\ output
echo   export-requirements - refresh requirements-docs.txt
echo.
echo All `book-*` aliases are accepted for compatibility.

:end
popd
endlocal
