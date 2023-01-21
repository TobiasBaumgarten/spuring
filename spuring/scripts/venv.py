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
