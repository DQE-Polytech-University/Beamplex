import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from src.jsonloader import *

class TestJSONLoader(unittest.TestCase):

    def testInitCorrect(self):
        try:
            self.loader = JSONLoader("json_test_files\correct.json")
            self.loader.loadJSON()
            self.loader.parseJSONData()
        except Exception, error:
            self.fail(error)

    def testInit(self):
        self.assertRaises(TypeError, JSONLoader, 123)

    def testLoaderPath(self):
        self.loader = JSONLoader("wrong_path")
        with self.assertRaises(IOError):
            self.loader.loadJSON()

    def testLoaderSyntax(self):
        self.loader = JSONLoader("json_test_files\wrong_syntax.json")
        with self.assertRaises(ValueError):
            self.loader.loadJSON()

    def testLoaderStructure(self):
        self.loader1 = JSONLoader("json_test_files\wrong_structure1.json")
        with self.assertRaises(KeyError):
            self.loader1.loadJSON()
            self.loader1.parseJSONData()
        self.loader2 = JSONLoader("json_test_files\wrong_structure2.json")
        with self.assertRaises(IndexError):
            self.loader2.loadJSON()
            self.loader2.parseJSONData()

    def testLoaderLambda(self):
        self.loader1 = JSONLoader("json_test_files\wrong_lambda_type.json")
        with self.assertRaises(TypeError):
            self.loader1.loadJSON()
            self.loader1.parseJSONData()
        self.loader2 = JSONLoader("json_test_files\wrong_lambda_range.json")
        with self.assertRaises(ValueError):
            self.loader2.loadJSON()
            self.loader2.parseJSONData()

    def testLoaderThickness(self):
        self.loader1 = JSONLoader("json_test_files\wrong_thickness_type.json")
        with self.assertRaises(TypeError):
            self.loader1.loadJSON()
            self.loader1.parseJSONData()
        self.loader2 = JSONLoader("json_test_files\wrong_thickness_range.json")
        with self.assertRaises(ValueError):
            self.loader2.loadJSON()
            self.loader2.parseJSONData()

    def testLoaderConcentration(self):
        self.loader1 = JSONLoader("json_test_files\wrong_concentration_type.json")
        with self.assertRaises(TypeError):
            self.loader1.loadJSON()
            self.loader1.parseJSONData()
        self.loader2 = JSONLoader("json_test_files\wrong_concentration_range.json")
        with self.assertRaises(ValueError):
            self.loader2.loadJSON()
            self.loader2.parseJSONData()

if __name__ == '__main__':
    unittest.main()
