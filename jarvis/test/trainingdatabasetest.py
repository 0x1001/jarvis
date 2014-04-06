import unittest

class TrainingDataBaseTest(unittest.TestCase):
    def setUp(self):
        from database import TrainingDataBase
        self.db = TrainingDataBase()

    def test_add_invalidinput(self):
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            self.db.add(None,None)

    def test_add_validinput(self):
        from database import WordRecord
        self.db.add([WordRecord("Abc"),WordRecord("abc"),WordRecord("abc")],[WordRecord("Abc"),WordRecord("abc"),WordRecord("abc")])

    def test_getAll_dbempty(self):
        data = self.db.getAll()
        self.assertEqual(data,[])

    def test_getAll_dbnotempty(self):
        from database import WordRecord
        self.db.add([WordRecord("Abc"),WordRecord("abc"),WordRecord("abc")],[WordRecord("Abc"),WordRecord("abc"),WordRecord("abc")])
        self.db.add([WordRecord("Abc"),WordRecord("abc"),WordRecord("abc")],[WordRecord("kkk"),WordRecord("kkk"),WordRecord("kkk")])
        self.db.add([WordRecord("bbb"),WordRecord("bbb"),WordRecord("bbb")],[WordRecord("bbb"),WordRecord("bbb"),WordRecord("bbb")])
        self.db.add([WordRecord("ccc"),WordRecord("ccc"),WordRecord("ccc")],[WordRecord("ccc"),WordRecord("ccc"),WordRecord("ccc")])

        data = self.db.getAll()
        self.assertNotIn(([WordRecord("Abc"),WordRecord("abc"),WordRecord("abc")],[WordRecord("Abc"),WordRecord("abc"),WordRecord("abc")]),data)
        self.assertIn(([WordRecord("bbb"),WordRecord("bbb"),WordRecord("bbb")],[WordRecord("bbb"),WordRecord("bbb"),WordRecord("bbb")]),data)
        self.assertIn(([WordRecord("ccc"),WordRecord("ccc"),WordRecord("ccc")],[WordRecord("ccc"),WordRecord("ccc"),WordRecord("ccc")]),data)
        self.assertIn(([WordRecord("Abc"),WordRecord("abc"),WordRecord("abc")],[WordRecord("kkk"),WordRecord("kkk"),WordRecord("kkk")]),data)

    def test_maxRequestWordCount(self):
        from database import WordRecord
        self.db.add([WordRecord("Abc"),WordRecord("abc"),WordRecord("abc"),WordRecord("ccc")],[WordRecord("Abc"),WordRecord("abc"),WordRecord("abc")])
        self.db.add([WordRecord("Abc"),WordRecord("abc"),WordRecord("abc")],[WordRecord("Abc"),WordRecord("abc")])
        size = self.db.maxRequestWordCount()
        self.assertEqual(size,4)

    def test_maxAnswerWordCount(self):
        from database import WordRecord
        self.db.add([WordRecord("Abc"),WordRecord("abc"),WordRecord("abc"),WordRecord("ccc")],[WordRecord("Abc"),WordRecord("abc"),WordRecord("abc")])
        self.db.add([WordRecord("Abc"),WordRecord("abc"),WordRecord("abc")],[WordRecord("Abc"),WordRecord("abc")])
        size = self.db.maxAnswerWordCount()
        self.assertEqual(size,3)

    def test_maxRequestWordCount_empty(self):
        size = self.db.maxRequestWordCount()
        self.assertEqual(size,0)

    def test_maxAnswerWordCount_empty(self):
        size = self.db.maxAnswerWordCount()
        self.assertEqual(size,0)

