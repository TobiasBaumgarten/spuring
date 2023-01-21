import importlib
from code import interact
from pathlib import Path
from typing import Any, Protocol

from spuring.template import Template, TemplateManager


SCRIPT_PATH = Path(__file__).parent / "scripts"

def create_template(name: str, out: str | None = None):
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


def _load_content(crypt_name: str, template: Template) -> str:
    name = crypt_name.split("_obj:")[1]
    return template.content[name]


def _check_and_create_folder(path: Path):
    if not path.parent.exists():
        if not path.parent.parent.exists():
            _check_and_create_folder(path.parent)
        path.parent.mkdir()


def run_scripts(template: Template, wd: Path):
    for plugin_file in SCRIPT_PATH.glob("*.py"):
        name = f"{__package__}.scripts.{plugin_file.stem}"
        plugin = importlib.import_module(name)
        plugin.process(template,wd)

