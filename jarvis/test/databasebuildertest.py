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