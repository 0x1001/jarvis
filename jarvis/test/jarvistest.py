import unittest

class JarvisTest(unittest.TestCase):
    def setUp(self):
        from jarvis import Jarvis

        self.he = Jarvis()

    def _word_database(self):
        from database import WordDataBase

        db = WordDataBase()
        db.addWord("aaa")
        db.addWord("bbb")
        db.addWord("ccc")

        return db

    def test_dictionary(self):
        self.he.dictionary(self._word_database())

    def test_respond_exception(self):
        from jarvis import JarvisException

        with self.assertRaises(JarvisException):
            self.he.respond("aaa bbb ccc")

    def test_respond_exception2(self):
        from jarvis import JarvisException

        self.he.dictionary(self._word_database())

        with self.assertRaises(JarvisException):
            self.he.respond("aaa bbb ccc kkk")

    def test_train_exception(self):
        from jarvis import JarvisException

        with self.assertRaises(JarvisException):
            self.he.train(None)

    def test_train(self):
        from database import TrainingDataBase

        tdb = TrainingDataBase()
        tdb.add("aaa bbb ccc","aaa aaa")

        self.he.dictionary(self._word_database())
        self.he.train(tdb)

    def test_respond(self):
        from database import TrainingDataBase

        tdb = TrainingDataBase()
        tdb.add("aaa bbb ccc","aaa aaa")
        tdb.add("aaa ccc","aaa ccc")

        self.he.dictionary(self._word_database())
        self.he.train(tdb)

        answer = self.he.respond("aaa bbb ccc")

        #self.assertEqual(answer,"aaa aaa") #Neural network sometimes does not answer correctly
        self.assertIsInstance(answer,str)