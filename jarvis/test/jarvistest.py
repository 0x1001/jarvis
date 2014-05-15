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

    def _abilities_builder(self):
        from database import AbilitiesDataBaseBuilder

        return AbilitiesDataBaseBuilder()

    def _innervoice_builder(self):
        from database import InnerVoiceDataBaseBuilder

        return InnerVoiceDataBaseBuilder()

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

    def test_createAbilitiesDataBase(self):
        self.he.createAbilitiesDataBase(self._abilities_builder())

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
        self.he.createAbilitiesDataBase(self._abilities_builder())
        self.he.train()

        answer = self.he.respond("aaa bbb_1 ccc")
        self.assertEqual(answer,"abc abc zzz") #Neural network sometimes does not answer correctly

        answer = self.he.respond("abc abc")
        self.assertEqual(answer,"abc test")

    def test_start_stop(self):
        import threading
        import time

        self.he.createInnerVoiceDatabase(self._innervoice_builder())
        start_thread = threading.Thread(target=self.he.start)
        start_thread.start()
        time.sleep(0.5)
        self.he.stop()
        start_thread.join()
        self.assertFalse(start_thread.isAlive())
