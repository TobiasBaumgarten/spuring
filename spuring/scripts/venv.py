from pathlib import Path
from typing import Any
from venv import create

from spuring import Template


def process(template: Template, wd: Path):
    if "venv" not in template.scripts:
        return
    # simple venv creation
    dir = wd / template.scripts["venv"]
    create(dir,with_pip=True)

