import argparse
from pathlib import Path
import sys
from spuring.template import TemplateManager
import spuring.creation

description = """
This is a Template builder for your projects
"""

# TODO: Make the argument thing better
manager = TemplateManager("")


def add_arguments(parser: argparse.ArgumentParser):
    parser.add_argument("-t", "--template",
                        choices=[t.name for t in manager.templates],
                        help="choose a template. Type 'py -m spuring -t [TEMPLATE] -o [PROJECT-FOLDER]'\nor just type 'py -m spuring -t' to list all templates")
    parser.add_argument(
        "-d",
        "--description",
        action="store_true",
        help="shows a description for the template\nspuring [template] -d",
    )
    parser.add_argument("-o", "--outdir", help="defines the project folder")
    parser.add_argument("-tp", "--templatePath", action="store_true")
    parser.add_argument("-l", "--list", action="store_true")


def list():

    result = ""
    result += f"\n\n{'Template':25s} 'Description'\n"
    result += "-" * 60
    for template in manager.templates:
        result += f"\n{template.name:25s} {template.description}"
    result += "\n\npyinitial [template] -o outdir\n"
    return result


def show_narrative(name: str):
    print(manager[name].narrative)


def print_template_path():
    path = Path(__file__).parent / "templates"
    print(path)


def proceed_args(args):
    if args.templatePath:
        print_template_path()
        return

    if args.list:
        print(list())
        return

    # proceed template creation
    if args.template:
        # if description is choose, show narrative and return
        if args.description:
            show_narrative(args.template)
            return
        # else create!
        spuring.creation.create_template(args.template, args.outdir)


def main(args = None):
    desc = description
    parser = argparse.ArgumentParser(
        description=desc, formatter_class=argparse.RawTextHelpFormatter)

    add_arguments(parser)
    if args == None:
        args = parser.parse_args()
    proceed_args(args)

if __name__ == "__main__":
    sys.exit(main())
