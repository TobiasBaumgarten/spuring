import os
from pathlib import Path
import sys
from typing import Any

from spuring.template import Template


def process(template: Template, wd: Path):
    if "venv" not in template.scripts:
        return
    # simple venv creation
    venv = False
    exe = sys.executable
    dir = wd / template.scripts["venv"]
    os.system(f"{exe} -m venv {dir}")
    venv = True

    
    if "pip" not in template.scripts:
        return
    # pip dependencie installation
    exe = sys.executable
    if venv:
        dir = wd / template.scripts["venv"]
        dir /= "Scripts" if os.name == "nt" else "bin"
        os.system(f"{exe} -m pip install -U pip")
        req = wd / template.scripts['pip']
        os.system(f"{exe} -m pip install -r {req}")