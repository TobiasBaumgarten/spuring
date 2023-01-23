import tomllib
from jinja2 import Environment, BaseLoader, PackageLoader, select_autoescape
import pathlib


_TEMPLATEATTRIBUTES = [
    "name",
    "description",
    "files",
    "folders",
    "content",
    "narrative",
    "scripts",
    "project"
]


_TEMPLATEDIR = pathlib.Path(__file__).parent / "templates"


class Template:
    name: str
    description: str
    files: dict[dict]
    folders: dict
    content: dict
    narrative: str
    scripts: dict
    project: str

    def __init__(self, input_dic) -> None:
        for attr in _TEMPLATEATTRIBUTES:
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
            self.template_dir = _TEMPLATEDIR

        self.name = name
        self.templates = []
        self._load_template_paths()
        self._load_templates()

    def _load_template_paths(self):
        """ Load all files/templates that are in the folder of templates """
        self.template_paths = []
        for file in self.template_dir.glob("*.toml"):
            self.template_paths.append(file)

    def _load_templates(self):
        for path in self.template_paths:
            file = pathlib.Path(path)
            env = Environment(loader=PackageLoader(__package__),
                              autoescape=select_autoescape())
            template = env.get_template(path.name)
            toml_dict = tomllib.loads(template.render(project=self.name))
            toml_dict["project"] = self.name
            if "name" in toml_dict:
                self.templates.append(Template(toml_dict))

    def __getitem__(self, key: str):
        return next(t for t in self.templates if t.name == key)
