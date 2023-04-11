import os
from pathlib import Path
import sys
from spuring import Template


def process(template: Template, wd: Path):
    if "pip" not in template.scripts:
        return
    # pip dependencies installation
    exe = sys.executable
    if "venv" in template.scripts:
        dir = wd / template.scripts["venv"]
        # setup the path - windows and linux path are different
        dir /= "Scripts" if os.name == "nt" else "bin"
        exe = dir / "python"
    # update pip

    os.system(f"{exe} -m pip install -U pip")
    # load the value from the pip attribute and run
    req = wd / template.scripts['pip']
    os.system(f"{exe} -m pip install -r {req}")
