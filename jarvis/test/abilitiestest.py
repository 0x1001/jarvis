import unittest

class AbilitiesTest(unittest.TestCase):
    def setUp(self):
        from abilities import Abilities

        self.ab = Abilities()

    def test_append_exception(self):
        from abilities import AbilitiesException

        with self.assertRaises(AbilitiesException):
            self.ab.append(None)

    def test_append(self):
        from abilities import AbilitiesException

        def dummy(): pass
        self.ab.append(dummy)
        self.assertEqual(dummy,self.ab[0])