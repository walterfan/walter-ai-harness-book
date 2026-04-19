@ECHO OFF

REM Windows equivalent of book/Makefile. Intentionally minimal —
REM macOS / Linux authors should prefer `make -C book <target>`.

pushd %~dp0

if "%SPHINXBUILD%" == "" (
    set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build
set SPHINXOPTS=-W --keep-going -n

if "%1" == "" goto help

if "%1" == "html" (
    %SPHINXBUILD% -b html -D language=en %SOURCEDIR% %BUILDDIR%\html\en %SPHINXOPTS%
    if errorlevel 1 goto end
    %SPHINXBUILD% -b html -D language=zh_CN %SOURCEDIR% %BUILDDIR%\html\zh_CN %SPHINXOPTS%
    goto end
)

if "%1" == "clean" (
    if exist %BUILDDIR% rd /s /q %BUILDDIR%
    goto end
)

if "%1" == "gettext" (
    %SPHINXBUILD% -b gettext %SOURCEDIR% %BUILDDIR%\gettext %SPHINXOPTS%
    goto end
)

:help
echo Harnessing AI - book build helper
echo.
echo Targets: html  clean  gettext

:end
popd
