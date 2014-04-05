import unittest

class AbilitieTest(unittest.TestCase):
    def setUp(self):
        from abilities import Abilitie

        self.ab = Abilitie()

    def test_execute(self):
        from abilities import AbilitieException

        with self.assertRaises(AbilitieException):
            self.ab.execute()
