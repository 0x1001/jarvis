import unittest

class AbilityTest(unittest.TestCase):
    def setUp(self):
        from abilities import Ability

        self.ab = Ability()

    def test_execute(self):
        from abilities import AbilityException

        with self.assertRaises(AbilityException):
            self.ab.execute()

class TestTest(unittest.TestCase):
    def test_execute(self):
        from abilities.a_test import Test
        from database import WordRecord

        self.assertEqual(Test().execute(),[WordRecord("test")])


class TestTime(unittest.TestCase):
    def test_execute(self):
        from abilities.a_time import Time
        from database import WordRecord

        result = Time().execute()
        for element in result:
            self.assertIsInstance(element,WordRecord)

        self.assertFalse(result == [])