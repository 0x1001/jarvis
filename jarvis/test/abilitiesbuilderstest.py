import unittest

class AbilitiesBuilderTest(unittest.TestCase):
    def setUp(self):
        from abilities import AbilitiesBuilder

        self.ab = AbilitiesBuilder()

    def test_generate(self):
        from abilities import Abilities

        ab_list = self.ab.generate()

        self.assertIsInstance(ab_list,Abilities)
        self.assertTrue(hasattr(ab_list[0],"__call__"))