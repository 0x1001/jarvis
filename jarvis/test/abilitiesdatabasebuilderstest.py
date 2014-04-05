import unittest

class AbilitiesDataBaseBuilderTest(unittest.TestCase):
    def setUp(self):
        from database import AbilitiesDataBaseBuilder

        self.ab = AbilitiesDataBaseBuilder()

    def test_generate(self):
        from database import AbilitiesDataBase

        ab_list = self.ab.generateDataBase()

        self.assertIsInstance(ab_list,AbilitiesDataBase)
