import unittest

class AbilitiesDataBaseBuilderTest(unittest.TestCase):
    def setUp(self):
        from database import AbilitiesDataBaseBuilder
        import jarvis

        self.ab = AbilitiesDataBaseBuilder()
        self.ab.jarvis(jarvis.Jarvis())

    def test_generate(self):
        from database import AbilitiesDataBase

        ab_list = self.ab.generateDataBase()

        self.assertIsInstance(ab_list,AbilitiesDataBase)

    def test_generate_exception(self):
        from database import AbilitiesDataBaseBuilder
        from database import DataBaseBuilderException

        ab = AbilitiesDataBaseBuilder()

        with self.assertRaises(DataBaseBuilderException):
            ab.generateDataBase()