import unittest

class WordParserTest(unittest.TestCase):
    def setUp(self):
        self.__dummy_file = "dummy.txt"

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
