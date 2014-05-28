import unittest

class AbilityTest(unittest.TestCase):
    def setUp(self):
        from abilities import Ability

        self.ab = Ability()

    def test_execute(self):
        from abilities import AbilityException

        with self.assertRaises(AbilityException):
            self.ab.execute()

class TestTest(unittest.TestCase):
    def test_execute(self):
        from abilities.a_test import Test
        from database import WordRecord

        self.assertEqual(Test().execute(),[WordRecord("test")])


class TestTime(unittest.TestCase):
    def test_execute(self):
        from abilities.a_time import Time
        from database import WordRecord

        result = Time().execute()
        for element in result:
            self.assertIsInstance(element,WordRecord)

        self.assertFalse(result == [])

class TestHello(unittest.TestCase):
    def test_execute(self):
        from abilities.a_hello import Hello
        from database import WordRecord

        result = Hello().execute()

        for element in result:
            self.assertIsInstance(element,WordRecord)

        self.assertFalse(result == [])

class TestExit(unittest.TestCase):
    def test_execute(self):
        from abilities.a_exit import Exit
        from database import WordRecord
        import jarvis

        exit_ability = Exit()
        he = jarvis.Jarvis()
        try: he.start()
        except jarvis.JarvisException: pass

        exit_ability.jarvis(he)
        result = exit_ability.execute()

        for element in result:
            self.assertIsInstance(element,WordRecord)

class TestMediaCenter(unittest.TestCase):
    def setUp(self):
        from abilities.a_mediacenter import MediaCenter

        self.mc = MediaCenter()

    def test_factoryBBCRadioStart(self):
        from abilities.a_mediacenter import BBCRadioStart

        ability = self.mc.factoryBBCRadioStart()

        self.assertIsInstance(ability,BBCRadioStart)

    def test_factoryStop(self):
        from abilities.a_mediacenter import Stop

        ability = self.mc.factoryStop()

        self.assertIsInstance(ability,Stop)

    def test_BBCRadioStart(self):
        from abilities.a_mediacenter import BBCRadioStart

        ability = BBCRadioStart()
        ability.player(None)
        ability.execute()

    def test_Stop(self):
        from abilities.a_mediacenter import Stop

        ability = Stop()
        ability.player(None)
        ability.execute()

    def test_mediacenterability(self):
        from abilities.a_mediacenter import MediaCenterAbility

        ability = MediaCenterAbility()
        self.assertFalse(ability._check_player())
        ability.player("dummy")
        self.assertTrue(ability._check_player())
