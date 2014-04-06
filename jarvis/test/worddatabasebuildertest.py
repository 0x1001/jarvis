import unittest

class WordDataBaseBuilderTest(unittest.TestCase):
    def setUp(self):
        from database import WordDataBaseBuilder

        self.builder = WordDataBaseBuilder()

    def test_generateDataBase_empty(self):
        from database import WordDataBase,DataBaseException

        database = self.builder.generateDataBase()
        self.assertIsInstance(database,WordDataBase)

        with self.assertRaises(DataBaseException):
            database.wordId("aaa")

    def test_generateDataBase(self):
        from database import WordDataBase,DataBaseException
        from database import WordRecord

        self.builder.addTxtFile("sample.txt")
        database = self.builder.generateDataBase()

        self.assertIsInstance(database,WordDataBase)

        database.wordId(WordRecord("aaa"))
        database.wordId(WordRecord("bbb"))

        with self.assertRaises(DataBaseException):
            database.wordId(WordRecord("www"))

