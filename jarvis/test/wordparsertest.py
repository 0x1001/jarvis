import unittest

class WordParserTest(unittest.TestCase):
    def setUp(self):
        self.__dummy_file = "dummy.txt"

    def test_wordsList_validinput(self):
        from database import WordParser

        contents = "  dummy   foo123  _ bar_bar dummy foobar [1] [22] kkk [1 zzz"

        parser = WordParser(contents)
        words = parser.wordsList()

        self.assertIsInstance(words,list)

        self.assertEqual(words[0],"dummy")
        self.assertEqual(words[1],"foo")
        self.assertEqual(words[2],"bar")
        self.assertEqual(words[3],"bar")
        self.assertEqual(words[4],"dummy")
        self.assertEqual(words[5],"foobar")
        self.assertEqual(words[6],"[1]")
        self.assertEqual(words[7],"[22]")
        self.assertEqual(words[8],"kkk")
        self.assertNotIn("[1",words)
        self.assertNotIn("foo123",words)
        self.assertNotIn("bar_bar",words)
        self.assertNotIn("",words)

    def test_wordsList_invalidinput(self):
        from database import WordParser,WordParserException

        parser = WordParser(None)
        with self.assertRaises(WordParserException):
            words = parser.wordsList()

    def test_wordsSet_invalidinput(self):
        from database import WordParser,WordParserException

        parser = WordParser(None)
        with self.assertRaises(WordParserException):
            words = parser.wordsSet()

    def test_wordsSet(self):
        from database import WordParser

        contents = "dummy foo123 bar_bar dummy foobar"

        parser = WordParser(contents)
        words = parser.wordsSet()

        self.assertIsInstance(words,set)

        self.assertIn("dummy",words)
        self.assertIn("foobar",words)
        self.assertNotIn("foo123",words)
        self.assertNotIn("bar_bar",words)
        self.assertNotIn("",words)