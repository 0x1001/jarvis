import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class WordParserTest(unittest.TestCase):
    def setUp(self):
        self.__dummy_file = "dummy.txt"

    def test_wordsList_validinput(self):
        from database import WordParser

        contents = "dummy foo123 bar_bar dummy foobar"

        parser = WordParser(contents)
        words = parser.wordsList()

        self.assertIn("dummy",words)
        self.assertIn("foobar",words)
        self.assertNotIn("foo123",words)
        self.assertNotIn("bar_bar",words)

    def test_wordsList_invalidinput(self):
        from database import WordParser,WordParserException

        parser = WordParser(None)
        with self.assertRaises(WordParserException):
            words = parser.wordsList()

class LowLevelTests(unittest.TestCase):
    def setUp(self):
        self.__dummy_file = "dummy.txt"

    def test_writeFileContents_validinput(self):
        import os
        import lowlevel

        contents = "AaAaba"

        lowlevel.writeFileContents(self.__dummy_file,contents)

        self.assertTrue(os.path.exists(self.__dummy_file))

        os.unlink(self.__dummy_file)

    def test_writeFileContents_invalidinput(self):
        import lowlevel

        contents = None
        path = self.__dummy_file
        with self.assertRaises(lowlevel.LowLevelException):
            lowlevel.writeFileContents(path,contents)

        contents = "AaAaba"
        path = None
        with self.assertRaises(lowlevel.LowLevelException):
            lowlevel.writeFileContents(path,contents)

        contents = "AaAaba"
        path = "c::\ffff:fff"
        with self.assertRaises(lowlevel.LowLevelException):
            lowlevel.writeFileContents(path,contents)

    def test_readFileContents_filenotexists(self):
        import lowlevel

        with self.assertRaises(lowlevel.LowLevelException):
            contents = lowlevel.readFileContents(self.__dummy_file)

    def test_readFileContents_fileexists(self):
        import os
        import lowlevel

        dummy_text = "aaa"

        with open(self.__dummy_file,"w") as fp:
            fp.write(dummy_text)

        contents = lowlevel.readFileContents(self.__dummy_file)

        self.assertEqual(contents,dummy_text)

        os.unlink(self.__dummy_file)

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
        from brain import Brain
        from trainer import TrainerException

        with self.assertRaises(TrainerException):
            self.tr_empty.train(Brain())

    def test_train_validinput(self):
        from brain import Brain
        from trainer import TrainerException

        self.tr_notempty.train(Brain())

    def test_prepareDataSet(self):
        data = self.tr_notempty._prepareDataSet()
        self.assertIn(((0,1,2),(2,1)),data.items())
        self.assertIn(((0, 2),(2, 2)),data.items())

class BrainTest(unittest.TestCase):
    def setUp(self):
        from brain import Brain

        self.br = Brain()

    def test_configure_invalidinput(self):
        from brain import BrainException

        with self.assertRaises(BrainException):
            self.br.configure(None,None)

    def test_configure_validinput(self):
        from brain import BrainException

        self.br.configure(1,1)

    def test_learn_invalidinput(self):
        from brain import BrainException

        with self.assertRaises(BrainException):
            self.br.learn(None)

    def test_learn_validinput(self):
        from brain import BrainException

        self.br.configure(2,2)
        data = {}
        data[(1,2,3)] = (1,2)
        data[(2,2)] = (2,2)
        data[(1,)] = (3,3)

        self.br.learn(data)

if __name__ == "__main__":
    unittest.main()