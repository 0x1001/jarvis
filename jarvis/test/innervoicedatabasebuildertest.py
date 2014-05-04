import unittest

class InnerVoiceDataBaseBuilderTest(unittest.TestCase):
    def setUp(self):
        from database import InnerVoiceDataBaseBuilder

        self.builder = InnerVoiceDataBaseBuilder()

    def test_generateDataBase_empty(self):
        from database import InnerVoiceDataBase

        database = self.builder.generateDataBase()
        self.assertIsInstance(database,InnerVoiceDataBase)

        self.assertEqual(database.getAll(),[])


    def test_generateDataBase(self):
        from database import InnerVoiceDataBase

        self.builder.addTxtFile("innervoice_sample.txt")
        database = self.builder.generateDataBase()
        self.assertIsInstance(database,InnerVoiceDataBase)

        self.assertIn("aaa aaa",database.getAll())
        self.assertIn("aaa bbb",database.getAll())
        self.assertNotIn("aaa ccc",database.getAll())