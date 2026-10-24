# -*- mode: python ; coding: utf-8 -*-
#this belongs in root /retro_gta_workshop.spec - Version: 1
# X-Seti - October 24 2026 - Retro GTA Workshop - PyInstaller build spec (Windows)

"""
PyInstaller spec for the standalone Retro GTA Workshop Windows build.
Build: pyinstaller retro_gta_workshop.spec  ->  dist/Retro_GTA_Workshop/Retro_GTA_Workshop.exe
"""

##Methods list -
# _app_data
# _make_icon
# _version_file

import os

from PyInstaller.utils.hooks import collect_submodules

ROOT = os.path.abspath(SPECPATH)


def _app_data(): #vers 1
    """Every non-Python file under apps/, kept at the same relative path."""
    out = []
    for base, dirs, files in os.walk(os.path.join(ROOT, 'apps')):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for name in files:
            if name.endswith(('.py', '.pyc', '.log')):
                continue
            out.append((os.path.join(base, name), os.path.relpath(base, ROOT)))
    return out


def _make_icon(): #vers 1
    """Render the Retro GTA Workshop SVG app icon to build/retro_gta_workshop.ico."""
    import sys
    os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
    sys.path.insert(0, ROOT)
    from PyQt6.QtWidgets import QApplication
    app = QApplication.instance() or QApplication([])
    from apps.methods.imgfactory_svg_icons import SVGIconFactory
    out = os.path.join(ROOT, 'build', 'retro_gta_workshop.ico')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if not SVGIconFactory.retro_gta_app_icon(256).pixmap(256, 256).toImage().save(out, 'ICO'):
        raise RuntimeError('ICO write failed')
    return out


def _version_file(): #vers 1
    """Windows version resource (company, product, version) for the exe."""
    out = os.path.join(ROOT, 'build', 'version_info.txt')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fields = {'CompanyName': 'X-Seti', 'FileDescription': 'Retro GTA Workshop',
              'FileVersion': '1.6.0.0', 'InternalName': 'Retro_GTA_Workshop',
              'LegalCopyright': 'X-Seti, GPL-3.0', 'OriginalFilename': 'Retro_GTA_Workshop.exe',
              'ProductName': 'Retro GTA Workshop', 'ProductVersion': '1.6.0.0'}
    strings = ',\n'.join(f"            StringStruct('{k}', '{v}')" for k, v in fields.items())
    text = f"""VSVersionInfo(
  ffi=FixedFileInfo(filevers=(1, 6, 0, 0), prodvers=(1, 6, 0, 0), mask=0x3f, flags=0x0,
                    OS=0x40004, fileType=0x1, subtype=0x0, date=(0, 0)),
  kids=[
    StringFileInfo([StringTable('080904B0', [
{strings}
    ])]),
    VarFileInfo([VarStruct('Translation', [2057, 1200])])
  ]
)
"""
    with open(out, 'w', encoding='utf-8') as f:
        f.write(text)
    return out


a = Analysis(
    ['launch_retro_gta_workshop.py'],
    pathex=[ROOT],
    binaries=[],
    datas=_app_data(),
    hiddenimports=['PyQt6.QtSvg', 'PyQt6.QtMultimedia', 'numpy', 'PIL.Image']
                  + collect_submodules('apps.components.DP5_Workshop.plugins'),   # loaded at run time
    excludes=['tkinter'],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, [],
    exclude_binaries=True,
    name='Retro_GTA_Workshop',
    console=False,
    icon=_make_icon(),
    version=_version_file(),
    upx=False,
)
coll = COLLECT(exe, a.binaries, a.datas, upx=False, name='Retro_GTA_Workshop')
