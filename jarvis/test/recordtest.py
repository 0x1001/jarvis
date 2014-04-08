import unittest

class RecordTest(unittest.TestCase):
    def setUp(self):
        from database import Record

        self.r = Record("Abc")

    def test_getValue(self):
        value = self.r.getValue()
        self.assertEqual(value,"Abc")

    def test__eq__(self):
        from database import Record
        r2 = Record("Abc")
        self.assertEqual(self.r,r2)

    def test___hash__(self):
        from database import Record
        r2 = Record("Abc")
        self.assertEqual(hash(self.r),hash(r2))

    def test_WordRecord(self):
        from database import WordRecord
        from database import Record

        self.assertIsInstance(WordRecord("aaa"),Record)

        self.assertEqual(WordRecord("AAA").getValue(),"aaa")
        self.assertEqual(WordRecord("zzz").getValue(),"zzz")

    def test_AbilityRecord(self):
        from database import AbilityRecord
        from database import Record

        self.assertIsInstance(AbilityRecord("[1]"),Record)
        self.assertEqual(AbilityRecord("[1]").getValue(),1)