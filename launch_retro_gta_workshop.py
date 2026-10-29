#!/usr/bin/env python3
#this belongs in root /launch_retro_gta_workshop.py - Version: 1
# X-Seti - October 23 2026 - Retro GTA Workshop - Root Launcher

import sys
from pathlib import Path

root_dir = Path(__file__).parent.resolve()
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    from apps.methods.imgfactory_svg_icons import SVGIconFactory
    from apps.components.Retro_GTA_Workshop.retro_gta_workshop import open_retro_gta_workshop
    app = QApplication(sys.argv)
    app.setWindowIcon(SVGIconFactory.retro_gta_app_icon(64))
    ws = open_retro_gta_workshop(None, sys.argv[1] if len(sys.argv) > 1 else None)
    ws.setWindowTitle("Retro GTA Workshop - Standalone")
    sys.exit(app.exec())
