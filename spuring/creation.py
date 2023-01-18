import os
import sys
from pathlib import Path

from spuring.template import Template, TemplateManager


def create_template(name: str, out: str = None):
    if out != None:
        wd = create_wd(out)
        manager = TemplateManager(out)
    else:
        wd = Path().cwd()
        manager = TemplateManager(Path().cwd().name)
    temp = manager[name]

    create_folders(temp, wd)
    create_files(temp, wd)
    run_scripts(temp, wd)


def create_wd(new_workingdir: str) -> Path:
    wd = Path().cwd() / new_workingdir
    if not wd.exists():
        wd.mkdir()
    return wd


def create_folders(template: Template, wd: Path):
    for _, folder in template.folders.items():
        f = wd / Path(folder)
        _check_and_create_folder(f)


def create_files(template: Template, wd: Path):
    for _, file in template.files.items():
        f = wd / Path(file["path"])
        _check_and_create_folder(f)

        content = ""
        if "content" in file:
            content = file["content"]
            if content.startswith("_obj:"):
                content = _load_content(content, template)
        f.write_text(content)


def run_scripts(template: Template, wd: Path):
    exe = sys.executable
    if "venv" in template.scripts:
        print(exe)
        dir = wd / template.scripts["venv"]
        os.system(f"{exe} -m venv {dir}")
        if "pip" in template.scripts:
            if os.name == "nt":
                exe = dir / "Scripts" / "python.exe"
                req = wd / template.scripts["pip"]
                print(exe)
                os.system(f"{exe} -m pip install -U pip")
                os.system(f"{exe} -m pip install -r {req}")
    else:
        if "pip" in template.scripts:
            req = wd / template.scripts["pip"]
            os.system(f"{exe} -m pip install -U pip")
            os.system(f"{exe} -m pip install -r {req}")

    if "code" in template.scripts:
        os.system(f"code {wd}")


def _load_content(crypt_name: str, template: Template) -> str:
    name = crypt_name.split("_obj:")[1]
    return template.content[name]


def _check_and_create_folder(path: Path):
    if not path.parent.exists():
        if not path.parent.parent.exists():
            _check_and_create_folder(path.parent)
        path.parent.mkdir()
