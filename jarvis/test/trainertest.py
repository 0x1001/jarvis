import unittest

class TrainerTest(unittest.TestCase):
    def setUp(self):
        from trainer import Trainer
        from database import TrainingDataBase,WordDataBase,WordRecord

        self.tr_empty = Trainer(WordDataBase(),TrainingDataBase())

        wdb = WordDataBase()
        wdb.addWord(WordRecord("aaa"))
        wdb.addWord(WordRecord("bbb"))
        wdb.addWord(WordRecord("ccc"))
        tdb = TrainingDataBase()
        tdb.add([WordRecord("aaa"),WordRecord("bbb"),WordRecord("ccc")],[WordRecord("ccc"),WordRecord("bbb")])
        tdb.add([WordRecord("aaa"),WordRecord("ccc")],[WordRecord("ccc"),WordRecord("ccc")])

        self.tr_notempty = Trainer(wdb,tdb)

    def test_init_invalidinput(self):
        from trainer import Trainer,TrainerException

        with self.assertRaises(TrainerException):
            tr = Trainer(None,None)

    def test_train_invalidinput(self):
        from trainer import TrainerException
        with self.assertRaises(TrainerException):
            self.tr_empty.train(None)

    def test_train_validinput_empty_neuralbrain(self):
        from neural import NeuralBrain
        from trainer import TrainerException

        with self.assertRaises(TrainerException):
            self.tr_empty.train(NeuralBrain())

    def test_train_validinput_neuralbrain(self):
        from neural import NeuralBrain
        from trainer import TrainerException

        self.tr_notempty.train(NeuralBrain())

    def test_train_validinput_empty_lookuptablebrain(self):
        from neural import LookUpTableBrain
        from trainer import TrainerException

        with self.assertRaises(TrainerException):
            self.tr_empty.train(LookUpTableBrain())

    def test_train_validinput_lookuptablebrain(self):
        from neural import LookUpTableBrain
        from trainer import TrainerException

        self.tr_notempty.train(LookUpTableBrain())

    def test_prepareDataSet(self):
        data = self.tr_notempty._prepareDataSet()
        self.assertIn(((0,1,2),(2,1)),data.items())
        self.assertIn(((0, 2),(2, 2)),data.items())
