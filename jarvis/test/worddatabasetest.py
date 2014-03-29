import unittest

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

    def test_multipleWordId(self):
        ids = self.db.multipleWordId(["aaa","bbb","ccc"])
        self.assertEqual(ids[0],2)
        self.assertEqual(ids[1],1)
        self.assertEqual(ids[2],0)

    def test_multipleWordId_exception(self):
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            ids = self.db.multipleWordId(["kkk","hhh","www"])

    def test_multipleIdWord(self):
        words = self.db.multipleIdWord([2,1,0,0])
        self.assertEqual(words[0],"aaa")
        self.assertEqual(words[1],"bbb")
        self.assertEqual(words[2],"ccc")
        self.assertEqual(words[3],"ccc")

    def test_multipleIdWord_exception(self):
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            words = self.db.multipleIdWord([5,5,5])
