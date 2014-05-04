import unittest

class InnerVoiceDataBaseTest(unittest.TestCase):
    def setUp(self):
        from database import InnerVoiceDataBase
        self.database = InnerVoiceDataBase()

    def test_add(self):
        self.database.add("aaa bbb")

    def test_getAll(self):
        self.assertEqual(self.database.getAll(),[])

    def test_getRandom(self):
        self.database.add("aaa bbb")
        self.database.add("aaa ccc")

        value = self.database.getRandom()
        self.assertTrue(value == "aaa bbb" or value == "aaa ccc")

    def test_add_no_multiplications(self):
        self.database.add("aaa bbb")
        self.database.add("aaa bbb")
        self.database.add("aaa bbb")
        self.database.add("aaa bbb")

        self.assertEqual(len(self.database.getAll()),1)