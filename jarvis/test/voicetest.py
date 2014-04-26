import unittest

class VoiceTest(unittest.TestCase):
    def setUp(self):
        from voice import Voice

        self.voice = Voice()

    def test_sentence(self):
        from voice import VoiceException

        self.voice.speak("dummy dummy")
        self.voice.speak(["dummy","dummy"])

        with self.assertRaises(VoiceException):
            self.voice.speak(None)

    def test_test(self):
        self.voice._test()