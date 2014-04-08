import unittest

class BodyTest(unittest.TestCase):
    def setUp(self):
        from body import Body
        from database import AbilitiesDataBase
        from abilities import test

        ab_db = AbilitiesDataBase()
        ab_db.addAbility(test.Test())

        self.b = Body()
        self.b.abilitiesDataBase(ab_db)

    def test_abilitiesDataBase(self):
        from database import AbilitiesDataBase
        ab_db = AbilitiesDataBase()
        self.b.abilitiesDataBase(ab_db)

    def test_do_empty(self):
        data = self.b.do([])
        self.assertEqual(data,[])

    def test_do(self):
        from database import AbilityRecord,WordRecord

        answer = self.b.do([AbilityRecord("[0]")])

        for word in answer:
            self.assertIsInstance(word,WordRecord)

        answer = self.b.do([WordRecord("aaa"),WordRecord("bbb")])

        self.assertIsInstance(answer[0],WordRecord)
        self.assertIsInstance(answer[1],WordRecord)

        self.assertEqual(answer[0],WordRecord("aaa"))
        self.assertEqual(answer[1],WordRecord("bbb"))

    def test_do_exception(self):
        from database import AbilityRecord,WordRecord
        from body import Body,BodyException

        b = Body()
        with self.assertRaises(BodyException):
            b.do([AbilityRecord("[0]")])
