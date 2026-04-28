@ECHO OFF
REM Robust make.bat for Sphinx (Windows cmd). Uses delayed expansion to avoid parse-time issues.

pushd %~dp0
setlocal ENABLEDELAYEDEXPANSION

REM Defaults (override by setting env vars before calling)
if "%SPHINXBUILD%"=="" set "SPHINXBUILD=sphinx-build"
if "%SPHINXOPTS%"=="" set "SPHINXOPTS="
if "%SOURCEDIR%"=="" set "SOURCEDIR=source"
if "%BUILDDIR%"=="" set "BUILDDIR=public"

REM Check sphinx-build exists (use where so full paths are resolved)
where "%SPHINXBUILD%" >NUL 2>&1
if errorlevel 1 (
  echo.
  echo The '%SPHINXBUILD%' command was not found. Make sure Sphinx is installed and on PATH.
  echo Try: pip install sphinx
  endlocal
  popd
  exit /b 1
)

REM If no argument -> show help
if "%~1"=="" goto help

set "TARGET=%~1"

if /I "%TARGET%"=="help" goto help
if /I "%TARGET%"=="clean" goto clean
if /I "%TARGET%"=="html" goto html
if /I "%TARGET%"=="livehtml" goto livehtml

REM Catch-all: forward unknown targets to sphinx-build -M <target>
echo Running: %SPHINXBUILD% -M %TARGET% "%SOURCEDIR%" "%BUILDDIR%" !SPHINXOPTS! !O!
%SPHINXBUILD% -M %TARGET% "%SOURCEDIR%" "%BUILDDIR%" !SPHINXOPTS! !O!
if not exist "%BUILDDIR%" goto end
type nul > "%BUILDDIR%\.no-jekyll"
goto end

:clean
if exist "%BUILDDIR%" (
  echo Removing "%BUILDDIR%"...
  rmdir /s /q "%BUILDDIR%"
) else (
  echo Nothing to clean: "%BUILDDIR%" does not exist.
)
goto end

:html
echo Building HTML:
%SPHINXBUILD% -b html "%SOURCEDIR%" "%BUILDDIR%" !SPHINXOPTS!
if errorlevel 1 (
  echo sphinx-build returned an error. See messages above.
  goto end
)
if not exist "%BUILDDIR%" mkdir "%BUILDDIR%"
type nul > "%BUILDDIR%\.no-jekyll"
goto end

:livehtml
REM prefer installed command 'sphinx-autobuild' if available, otherwise try python -m
where "sphinx-autobuild" >NUL 2>&1
if errorlevel 1 (
  echo "sphinx-autobuild" not found on PATH. Trying python -m sphinx_autobuild...
  python -m sphinx_autobuild "%SOURCEDIR%" "%BUILDDIR%" !SPHINXOPTS! !O!
  if errorlevel 1 (
    echo.
    echo.You need 'sphinx-autobuild' installed to use livehtml. Try: pip install sphinx-autobuild
    goto end
  )
) else (
  sphinx-autobuild "%SOURCEDIR%" "%BUILDDIR%" !SPHINXOPTS! !O!
)
goto end

:help
%SPHINXBUILD% -M help "%SOURCEDIR%" "%BUILDDIR%" !SPHINXOPTS! !O!
goto end

:end
endlocal
popd