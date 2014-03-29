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
        self.db.add("Abc abc abc","Abc abc abc")

    def test_getAll_dbempty(self):
        data = self.db.getAll()
        self.assertEqual(data,[])

    def test_getAll_dbnotempty(self):
        self.db.add("Abc abc abc","Abc abc abc")
        self.db.add("Abc abc abc","kkk kkk kkk")
        self.db.add("bbb bbb bbb","bbb bbb bbb")
        self.db.add("ccc ccc ccc","ccc ccc ccc")

        data = self.db.getAll()
        self.assertNotIn(("Abc abc abc","Abc abc abc"),data)
        self.assertIn(("bbb bbb bbb","bbb bbb bbb"),data)
        self.assertIn(("ccc ccc ccc","ccc ccc ccc"),data)
        self.assertIn(("Abc abc abc","kkk kkk kkk"),data)

    def test_maxRequestWordCount(self):
        self.db.add("Abc abc abc ccc","Abc abc abc")
        self.db.add("Abc abc abc","Abc abc")
        size = self.db.maxRequestWordCount()
        self.assertEqual(size,4)

    def test_maxAnswerWordCount(self):
        self.db.add("Abc abc abc ccc","Abc abc abc")
        self.db.add("Abc abc abc","Abc abc")
        size = self.db.maxAnswerWordCount()
        self.assertEqual(size,3)

    def test_maxRequestWordCount_empty(self):
        size = self.db.maxRequestWordCount()
        self.assertEqual(size,0)

    def test_maxAnswerWordCount_empty(self):
        size = self.db.maxAnswerWordCount()
        self.assertEqual(size,0)

