import tomllib
from jinja2 import Environment, BaseLoader
import pathlib


_template_attr = [
    "name",
    "description",
    "files",
    "folders",
    "content",
    "explonation",
    "scripts",
]

_to_list_attr = [
    "folders", "files"
]

_templates_dir = pathlib.Path(__file__).parent / "templates"


class Template:
    name: str
    description: str
    files: dict[dict]
    folders:dict
    content: dict
    explonation: str
    scripts: str

    def __init__(self, input_dic) -> None:
        for attr in _template_attr:
            self._from_dict(input_dic, attr)

    def _from_dict(self, d: dict, key: str) -> any:
        if key in d:
            setattr(self, key, d[key])
        else:
            setattr(self, key, None)

    def __str__(self) -> str:
        return f"<{self.name}>"

    def __repr__(self) -> str:
        return f"<{self.name}>"

class TemplateManager:
    name: str
    template_dir: str
    template_paths: list[str]
    templates: list[Template]
    environment: Environment

    def __init__(self, name: str, template_path=None) -> None:
        if template_path == None:
            self.template_dir = _templates_dir

        self.name = name
        self.templates = []
        self._load_template_paths()
        self._load_templates()

    def _load_template_paths(self):
        self.template_paths = []
        for file in self.template_dir.glob("*.toml"):
            self.template_paths.append(file)

    def _load_templates(self):
        for path in self.template_paths:
            file = pathlib.Path(path)
            temp_string = Environment(loader=BaseLoader).from_string(
                file.read_text("utf-8")
            )
            temp_data = temp_string.render(project=self.name)
            toml_dict = tomllib.loads(temp_data)
            self.templates.append(Template(toml_dict))

    def __getitem__(self, key: str):
        return next(t for t in self.templates if t.name == key)
