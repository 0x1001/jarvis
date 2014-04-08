import unittest

class AbilityTest(unittest.TestCase):
    def setUp(self):
        from abilities import Ability

        self.ab = Ability()

    def test_execute(self):
        from abilities import AbilityException

        with self.assertRaises(AbilityException):
            self.ab.execute()
