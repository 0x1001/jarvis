import unittest

class AbilitiesDataBaseTest(unittest.TestCase):
    def setUp(self):
        from database import AbilitiesDataBase

        self.a_db = AbilitiesDataBase()

    def test_addAbilitie_exception(self):
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            self.a_db.addAbilitie(None)

    def test_addAbilitie(self):
        from abilities import Abilitie
        ab = Abilitie()

        self.a_db.addAbilitie(ab)
        self.assertEqual(ab,self.a_db.getAbilitie(0))

    def test_getAbilitie_exception(self):
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            self.a_db.getAbilitie(0)

