import unittest

class AbilitiesDataBaseTest(unittest.TestCase):
    def setUp(self):
        from database import AbilitiesDataBase

        self.a_db = AbilitiesDataBase()

    def test_addAbility_exception(self):
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            self.a_db.addAbility(None)

    def test_addAbility(self):
        from abilities import Ability
        ab = Ability()

        self.a_db.addAbility(ab)
        self.assertEqual(ab,self.a_db.getAbility(0))

    def test_getAbility_exception(self):
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            self.a_db.getAbility(0)

