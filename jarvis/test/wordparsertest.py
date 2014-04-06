import unittest

class WordParserTest(unittest.TestCase):
    def setUp(self):
        self.__dummy_file = "dummy.txt"

    def test_wordsList_validinput(self):
        from database import WordParser
        from database import WordRecord, AbilitieRecord

        contents = "  dummy   foo123  _ bar_bar dummy foobar [1] [22] kkk [1 zzz"

        parser = WordParser(contents)
        words = parser.wordsList()

        self.assertIsInstance(words,list)

        self.assertEqual(words[0],WordRecord("dummy"))
        self.assertEqual(words[1],WordRecord("foo"))
        self.assertEqual(words[2],WordRecord("bar"))
        self.assertEqual(words[3],WordRecord("bar"))
        self.assertEqual(words[4],WordRecord("dummy"))
        self.assertEqual(words[5],WordRecord("foobar"))
        self.assertEqual(words[6],AbilitieRecord("[1]"))
        self.assertEqual(words[7],AbilitieRecord("[22]"))
        self.assertEqual(words[8],WordRecord("kkk"))

        self.assertIn(WordRecord("kkk"),words)
        self.assertNotIn(WordRecord("[1"),words)
        self.assertNotIn(WordRecord("foo123"),words)
        self.assertNotIn(WordRecord("bar_bar"),words)
        self.assertNotIn(WordRecord(""),words)

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
        from database import WordRecord

        contents = "dummy foo123 bar_bar dummy foobar"

        parser = WordParser(contents)
        words = parser.wordsSet()

        self.assertIsInstance(words,set)

        self.assertIn(WordRecord("dummy"),words)
        self.assertIn(WordRecord("foobar"),words)
        self.assertNotIn(WordRecord("foo123"),words)
        self.assertNotIn(WordRecord("bar_bar"),words)
        self.assertNotIn(WordRecord(""),words)

    def test_convert_exception(self):
        from database import WordParserException
        from database import WordParser

        parser = WordParser("")

        with self.assertRaises(WordParserException):
            record = parser._convert("1")

        with self.assertRaises(WordParserException):
            record = parser._convert("$A!")

    def test_convert(self):
        from database import WordParser
        from database import AbilitieRecord,WordRecord

        parser = WordParser("")
        record = parser._convert("[1]")
        self.assertIsInstance(record,AbilitieRecord)
        self.assertEqual(record.getValue(),1)

        record = parser._convert("aaa")
        self.assertIsInstance(record,WordRecord)
        self.assertEqual(record.getValue(),"aaa")