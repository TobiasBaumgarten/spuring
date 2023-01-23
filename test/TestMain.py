import os
import unittest
import pathlib
import shutil
import tomllib
from spuring import main, creation
import argparse


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        self.folder = pathlib.Path(__file__).parent.parent / "testFolder"
        self.folder.mkdir()

    def test_default(self):
        creation.create_template("default", self.folder.name)
        files = list(self.folder.glob("*"))
        names = [f.name for f in files]
        self.assertIn("README.md", names)
        self.assertIn("test", names)
        self.assertIn(self.folder.name, names)
        self.assertIn(".venv", names)

    def tearDown(self) -> None:
        shutil.rmtree(self.folder.absolute())


if __name__ == "__main__":
    unittest.main()
