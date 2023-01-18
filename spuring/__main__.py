import argparse
from pathlib import Path
from spuring.template import TemplateManager
import spuring.creation

description = """
This is a Templatebuilder for your projects
"""


def add_arguments(parser: argparse.ArgumentParser):
    parser.add_argument("template")
    parser.add_argument(
        "-d",
        "--description",
        action="store_true",
        help="shows a description for the template\npyinitial [template] -d",
    )
    parser.add_argument("-o", "--outdir", help="defines the project folder")


def list():
    manager = TemplateManager("")
    result = ""
    result += f"\n\n{'Template':25s} 'Description'\n"
    result += "-" * 60 
    for template in manager.templates:
        result += f"\n{template.name:25s} {template.description}"
    result += "\npyinitial [template] -o outdir\n"
    return result


def show_explonation(name: str):
    manager = TemplateManager("")
    print(manager[name].explonation)


def procced_args(args):
    # proceed template creation
    if args.template:

        # if description is choosed, show explonation and return
        if args.description:
            show_explonation(args.template)
            return
        # else create!
        spuring.creation.create_template(args.template, args.outdir)


if __name__ == "__main__":
    desc = description + list()
    parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawTextHelpFormatter)

    add_arguments(parser)
    args = parser.parse_args()
    procced_args(args)
