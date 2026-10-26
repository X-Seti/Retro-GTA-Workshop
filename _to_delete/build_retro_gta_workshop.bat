@echo off
rem this belongs in root /build_retro_gta_workshop.bat - Version: 1
rem X-Seti - October 24 2026 - Retro GTA Workshop - Windows exe build
rem Output: dist\Retro_GTA_Workshop\Retro_GTA_Workshop.exe (ffmpeg on PATH for STR video)
cd /d "%~dp0"
python -m pip install --upgrade pyinstaller PyQt6 numpy pillow
python -m PyInstaller --noconfirm retro_gta_workshop.spec
if errorlevel 1 exit /b 1
echo Built dist\Retro_GTA_Workshop\Retro_GTA_Workshop.exe
