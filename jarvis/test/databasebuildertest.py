import unittest

class DataBaseBuilderTest(unittest.TestCase):
    def setUp(self):
        from database.databasebuilder import DataBaseBuilder

        self.builder = DataBaseBuilder()

    def test_addTxtFile(self):
        self.builder.addTxtFile("sample.txt")

    def test_generateDataBase_exception(self):
        from database import DataBaseBuilderException

        with self.assertRaises(DataBaseBuilderException):
            self.builder.generateDataBase()

    def test_readFileContents_exception(self):
        from database import DataBaseBuilderException

        with self.assertRaises(DataBaseBuilderException):
            contents = self.builder._readFileContents("fff.txt")

    def test_readFileContents(self):
        contents = self.builder._readFileContents("sample.txt")

        self.assertIsInstance(contents,str)
        self.assertIn("aaa", contents)
        self.assertIn("ddd", contents)