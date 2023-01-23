import unittest, pathlib, tomllib
from spuring.template import *

class TestTemplate(unittest.TestCase):

    def setUp(self) -> None:
        _file_name = "TestTemplate.toml"
        path = pathlib.Path(__file__).parent / _file_name
        self.testtoml = tomllib.loads(path.read_text())
        self.template = Template(self.testtoml)

    def test_meta(self):
        self.assertEqual(self.template.name, "test")
        self.assertEqual(self.template.description, "pony")
        self.assertEqual(self.template.narrative, "rainbow")

    def test_folders(self):
        self.assertEqual(self.template.folders["src"], "{{ project }}")
        self.assertEqual(self.template.folders["test"], "testfolder")

    def test_files(self):
        pyinit = self.template.files["pyinit"] 
        self.assertIsInstance(pyinit,dict)
        self.assertEqual(pyinit["path"], "{{project}}/__init__.py")
        self.assertNotIn("content", pyinit)
        testtemplate = self.template.files["testTemplate"] 
        self.assertIsInstance(testtemplate,dict)
        self.assertEqual(testtemplate["path"], "test/Test{{project | title }}.py")
        self.assertIn("content", testtemplate)
        self.assertEqual(testtemplate["content"], "_obj:testTemplate")

    def test_content(self):
        content = self.template.content
        self.assertIn("testTemplate", content)
        self.assertEqual(content["testTemplate"], "import unittest\n")

    def test_scripts(self):
        self.assertEqual(self.template.scripts["venv"],".venv")

class TestTemplateManager(unittest.TestCase):
    #TODO
    pass

if __name__ == '__main__':
    unittest.main()
