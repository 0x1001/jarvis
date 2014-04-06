import unittest

class WordDataBaseTest(unittest.TestCase):
    def setUp(self):
        from database import WordDataBase
        from database import WordRecord
        self.db = WordDataBase()

        self.db.addWord(WordRecord("ccc"))
        self.db.addWord(WordRecord("bbb"))
        self.db.addWord(WordRecord("aaa"))

    def test_wordId_invalidword(self):
        from database import DataBaseException
        from database import WordRecord

        with self.assertRaises(DataBaseException):
            self.db.wordId(None)

        with self.assertRaises(DataBaseException):
            self.db.wordId(WordRecord("ddd"))

    def test_wordId_validword(self):
        from database import DataBaseException
        from database import WordRecord

        self.assertEqual(self.db.wordId(WordRecord("ccc")),0)
        self.assertEqual(self.db.wordId(WordRecord("bbb")),1)
        self.assertEqual(self.db.wordId(WordRecord("aaa")),2)

    def test_addWord_invalidword(self):
        from database import WordRecord
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            self.db.addWord(None)

        with self.assertRaises(DataBaseException):
            self.db.addWord(WordRecord("ccc"))

    def test_idWord_invalidinput(self):
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            self.db.idWord(None)

        with self.assertRaises(DataBaseException):
            self.db.idWord(3)

        with self.assertRaises(DataBaseException):
            self.db.idWord(-5)

    def test_multipleWordId(self):
        from database import WordRecord
        ids = self.db.multipleWordId([WordRecord("aaa"),WordRecord("bbb"),WordRecord("ccc")])
        self.assertEqual(ids[0],2)
        self.assertEqual(ids[1],1)
        self.assertEqual(ids[2],0)

    def test_multipleWordId_exception(self):
        from database import WordRecord
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            ids = self.db.multipleWordId([WordRecord("kkk"),WordRecord("hhh"),WordRecord("www")])

    def test_multipleIdWord(self):
        from database import WordRecord

        words = self.db.multipleIdWord([2,1,0,0])
        self.assertEqual(words[0],WordRecord("aaa"))
        self.assertEqual(words[1],WordRecord("bbb"))
        self.assertEqual(words[2],WordRecord("ccc"))
        self.assertEqual(words[3],WordRecord("ccc"))

    def test_multipleIdWord_exception(self):
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            words = self.db.multipleIdWord([5,5,5])
