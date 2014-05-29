import unittest

class AbilitiesDataBaseTest(unittest.TestCase):
    def setUp(self):
        from database import AbilitiesDataBase

        self.a_db = AbilitiesDataBase()

    def test_addAbility_exception(self):
        from database import DataBaseException
        from abilities import Ability

        with self.assertRaises(DataBaseException):
            self.a_db.addAbility(0,None)

        ab1 = Ability()
        ab2 = Ability()
        id1 = id2 =  1
        self.a_db.addAbility(id1,ab1)

        with self.assertRaises(DataBaseException):
            self.a_db.addAbility(id1,ab2)

    def test_addAbility(self):
        from abilities import Ability
        ab = Ability()

        id = 0
        self.a_db.addAbility(id,ab)
        self.assertEqual(ab,self.a_db.getAbility(id))

    def test_getAbility_exception(self):
        from database import DataBaseException

        with self.assertRaises(DataBaseException):
            self.a_db.getAbility(0)

