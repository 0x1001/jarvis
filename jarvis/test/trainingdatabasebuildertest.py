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

        self.builder.addTxtFile("traning_sample.txt")
        database = self.builder.generateDataBase()

        self.assertIsInstance(database,TrainingDataBase)

        data = database.getAll()
        self.assertIn(("abc abc abc","abc abc abc"),data)
        self.assertIn(("abc abc ccc","abc abc kkk"),data)
        self.assertIn(("zzz","bbb"),data)
        self.assertNotIn(("aaa","aaa"),data)
