import unittest

class WordParser(unittest.TestCase):
    def setUp(self):
        import sys
        import os

        self.__path = sys.path
        sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"utilities"))

        self.__dummy_file = "dummy.txt"

    def tearDown(self):
        import sys

        sys.path = self.__path

    def test_readFileContents_filenotexists(self):
        import word_parser

        with self.assertRaises(word_parser.WordParseException):
            contents = word_parser.readFileContents(self.__dummy_file)

    def test_readFileContents_fileexists(self):
        import os
        import word_parser

        dummy_text = "aaa"

        with open(self.__dummy_file,"w") as fp:
            fp.write(dummy_text)

        contents = word_parser.readFileContents(self.__dummy_file)

        self.assertEqual(contents,dummy_text)

        os.unlink(self.__dummy_file)

    def test_parseContents_invalidinput(self):
        import word_parser

        with self.assertRaises(word_parser.WordParseException):
            word_parser.parseContents(None)

    def test_parseContents_validinput(self):
        import word_parser

        contents = "dummy foo123 bar_bar dummy foobar"

        words = word_parser.parseContents(contents)

        self.assertIn("dummy",words)
        self.assertIn("foobar",words)
        self.assertNotIn("foo123",words)
        self.assertNotIn("bar_bar",words)

    def test_writeContents_validinput(self):
        import os
        import word_parser

        contents = "AaAaba"

        word_parser.writeFileContents(self.__dummy_file,contents)

        self.assertTrue(os.path.exists(self.__dummy_file))

        os.unlink(self.__dummy_file)

    def test_writeContents_invalidinput(self):
        import word_parser

        contents = None
        path = self.__dummy_file
        with self.assertRaises(word_parser.WordParseException):
            word_parser.writeFileContents(path,contents)

        contents = "AaAaba"
        path = None
        with self.assertRaises(word_parser.WordParseException):
            word_parser.writeFileContents(path,contents)

        contents = "AaAaba"
        path = "c::\ffff:fff"
        with self.assertRaises(word_parser.WordParseException):
            word_parser.writeFileContents(path,contents)

    def test_createDatabase_validinput(self):
        import word_parser

        data_list = ["foo","bar","zak"]
        data_string = word_parser.createDatabase(data_list)

        self.assertIsInstance(data_string,str)

    def test_createDatabase_invalidinput(self):
        import word_parser

        data_list = None
        with self.assertRaises(word_parser.WordParseException):
            data_string = word_parser.createDatabase(data_list)

        data_list = [None]
        with self.assertRaises(word_parser.WordParseException):
            data_string = word_parser.createDatabase(data_list)

if __name__ == "__main__":
    unittest.main()