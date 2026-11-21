@echo off
setlocal
cd /d "%~dp0latex"

echo [1/2] Compiling LaTeX document (Pass 1)...
pdflatex -interaction=nonstopmode main.tex > nul

if "%1"=="full" (
    echo [2/2] Running Pass 2 for TOC and references...
    pdflatex -interaction=nonstopmode main.tex > nul
)

if exist main.pdf (
    echo [OK] Compilation successful!
    copy /y main.pdf "..\GovtITPrepNote.pdf" > nul
    echo [OK] Updated GovtITPrepNote.pdf
) else (
    echo [ERROR] Compilation failed. Check latex\main.log for details.
)

endlocal
