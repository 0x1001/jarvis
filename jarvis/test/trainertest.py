import unittest

class TrainerTest(unittest.TestCase):
    def setUp(self):
        from trainer import Trainer
        from database import TrainingDataBase,WordDataBase

        self.tr_empty = Trainer(WordDataBase(),TrainingDataBase())

        wdb = WordDataBase()
        wdb.addWord("aaa")
        wdb.addWord("bbb")
        wdb.addWord("ccc")
        tdb = TrainingDataBase()
        tdb.add("aaa bbb ccc","ccc bbb")
        tdb.add("aaa ccc","ccc ccc")

        self.tr_notempty = Trainer(wdb,tdb)

    def test_init_invalidinput(self):
        from trainer import Trainer,TrainerException

        with self.assertRaises(TrainerException):
            tr = Trainer(None,None)

    def test_train_invalidinput(self):
        from trainer import TrainerException
        with self.assertRaises(TrainerException):
            self.tr_empty.train(None)

    def test_train_validinput_empty(self):
        from neural import Brain
        from trainer import TrainerException

        with self.assertRaises(TrainerException):
            self.tr_empty.train(Brain())

    def test_train_validinput(self):
        from neural import Brain
        from trainer import TrainerException

        self.tr_notempty.train(Brain())

    def test_prepareDataSet(self):
        data = self.tr_notempty._prepareDataSet()
        self.assertIn(((0,1,2),(2,1)),data.items())
        self.assertIn(((0, 2),(2, 2)),data.items())
