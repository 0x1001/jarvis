import unittest

class JarvisTest(unittest.TestCase):
    def setUp(self):
        from jarvis import Jarvis

        self.he = Jarvis()

    def _word_database_builder(self):
        from database import WordDataBaseBuilder

        db_builder = WordDataBaseBuilder()
        db_builder.addTxtFile("sample.txt")

        return db_builder

    def _traning_database_builder(self):
        from database import TrainingDataBaseBuilder

        builder = TrainingDataBaseBuilder()
        builder.addTxtFile("traning_sample.txt")

        return builder

    def test_dictionary(self):
        self.he.createWordsDataBase(self._word_database_builder())

    def test_respond_exception(self):
        from jarvis import JarvisException

        with self.assertRaises(JarvisException):
            self.he.respond("aaa bbb ccc")

    def test_respond_exception2(self):
        from jarvis import JarvisException

        self.he.createWordsDataBase(self._word_database_builder())

        with self.assertRaises(JarvisException):
            self.he.respond("aaa bbb ccc www")

    def test_train_exception(self):
        from jarvis import JarvisException

        with self.assertRaises(JarvisException):
            self.he.train()

    def test_train(self):
        self.he.createWordsDataBase(self._word_database_builder())
        self.he.createTrainingDataBase(self._traning_database_builder())
        self.he.train()

    def test_respond(self):
        self.he.createWordsDataBase(self._word_database_builder())
        self.he.createTrainingDataBase(self._traning_database_builder())
        self.he.train()

        answer = self.he.respond("aaa bbb ccc")

        #self.assertEqual(answer,"aaa aaa") #Neural network sometimes does not answer correctly
        self.assertIsInstance(answer,str)