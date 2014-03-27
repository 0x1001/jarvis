import unittest

class WordParserTest(unittest.TestCase):
    def setUp(self):
        import sys
        import os

        self.__path = sys.path
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        self.__dummy_file = "dummy.txt"

    def tearDown(self):
        import sys

        sys.path = self.__path

    def test_wordsList_validinput(self):
        from database import WordParser

        contents = "dummy foo123 bar_bar dummy foobar"

        parser = WordParser(contents)
        words = parser.wordsList()

        self.assertIn("dummy",words)
        self.assertIn("foobar",words)
        self.assertNotIn("foo123",words)
        self.assertNotIn("bar_bar",words)

    def test_wordsList_invalidinput(self):
        from database import WordParser,WordParserException

        parser = WordParser(None)
        with self.assertRaises(WordParserException):
            words = parser.wordsList()

class LowLevelTests(unittest.TestCase):
    def setUp(self):
        import sys
        import os

        self.__path = sys.path
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        self.__dummy_file = "dummy.txt"

    def tearDown(self):
        import sys

        sys.path = self.__path

    def test_writeFileContents_validinput(self):
        import os
        import lowlevel

        contents = "AaAaba"

        lowlevel.writeFileContents(self.__dummy_file,contents)

        self.assertTrue(os.path.exists(self.__dummy_file))

        os.unlink(self.__dummy_file)

    def test_writeFileContents_invalidinput(self):
        import lowlevel

        contents = None
        path = self.__dummy_file
        with self.assertRaises(lowlevel.LowLevelException):
            lowlevel.writeFileContents(path,contents)

        contents = "AaAaba"
        path = None
        with self.assertRaises(lowlevel.LowLevelException):
            lowlevel.writeFileContents(path,contents)

        contents = "AaAaba"
        path = "c::\ffff:fff"
        with self.assertRaises(lowlevel.LowLevelException):
            lowlevel.writeFileContents(path,contents)

    def test_readFileContents_filenotexists(self):
        import lowlevel

        with self.assertRaises(lowlevel.LowLevelException):
            contents = lowlevel.readFileContents(self.__dummy_file)

    def test_readFileContents_fileexists(self):
        import os
        import lowlevel

        dummy_text = "aaa"

        with open(self.__dummy_file,"w") as fp:
            fp.write(dummy_text)

        contents = lowlevel.readFileContents(self.__dummy_file)

        self.assertEqual(contents,dummy_text)

        os.unlink(self.__dummy_file)

class WordDataBaseTest(unittest.TestCase):
    def setUp(self):
        from database import WordDataBase
        self.db = WordDataBase()

        self.db.addWord("ccc")
        self.db.addWord("bbb")
        self.db.addWord("aaa")

    def test_wordId_invalidword(self):
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            self.db.wordId(None)

        with self.assertRaises(DataBaseException):
            self.db.wordId("ddd")

    def test_wordId_validword(self):
        from database import DataBaseException

        self.assertEqual(self.db.wordId("ccc"),0)
        self.assertEqual(self.db.wordId("bbb"),1)
        self.assertEqual(self.db.wordId("aaa"),2)

    def test_addWord_invalidword(self):
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            self.db.addWord(None)

        with self.assertRaises(DataBaseException):
            self.db.addWord("ccc")

    def test_idWord_invalidinput(self):
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            self.db.idWord(None)

        with self.assertRaises(DataBaseException):
            self.db.idWord(3)

        with self.assertRaises(DataBaseException):
            self.db.idWord(-5)


if __name__ == "__main__":
    unittest.main()