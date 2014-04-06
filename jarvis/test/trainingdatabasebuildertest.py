import unittest

class TrainingDataBaseBuilderTest(unittest.TestCase):
    def setUp(self):
        from database import TrainingDataBaseBuilder
        self.builder = TrainingDataBaseBuilder()

    def test_generateDataBase_empty(self):
        from database import TrainingDataBase,DataBaseException

        database = self.builder.generateDataBase()
        self.assertIsInstance(database,TrainingDataBase)

        self.assertEqual(database.getAll(),[])

    def test_generateDataBase(self):
        from database import TrainingDataBase,DataBaseException
        from database import WordRecord

        self.builder.addTxtFile("traning_sample.txt")
        database = self.builder.generateDataBase()

        self.assertIsInstance(database,TrainingDataBase)

        data = database.getAll()
        self.assertIn(([WordRecord("abc"),WordRecord("abc"),WordRecord("abc")],[WordRecord("abc"),WordRecord("abc"),WordRecord("abc")]),data)
        self.assertIn(([WordRecord("abc"),WordRecord("abc"),WordRecord("ccc")],[WordRecord("abc"),WordRecord("abc"),WordRecord("kkk")]),data)
        self.assertIn(([WordRecord("zzz")],[WordRecord("bbb")]),data)
        self.assertNotIn(([WordRecord("aaa")],[WordRecord("aaa")]),data)
