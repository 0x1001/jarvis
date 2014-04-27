import unittest

class VoiceTest(unittest.TestCase):
    def setUp(self):
        from voice import Voice

        self.voice = Voice()

    def test_sentence(self):
        from voice import VoiceException

        self.voice.speak("Hello how are you")
        self.voice.speak(["hello","how","are","you"])

        with self.assertRaises(VoiceException):
            self.voice.speak(None)

    def test_volume(self):
        self.voice.volume(0.1)
        self.voice.speak("dummy dummy")
        self.voice.volume(0.5)
        self.voice.speak("dummy dummy")
        self.voice.volume(1.0)
        self.voice.speak("dummy dummy")

    def test_volume_exception(self):
        from voice import VoiceException

        with self.assertRaises(VoiceException):
            self.voice.volume(None)

        with self.assertRaises(VoiceException):
            self.voice.volume(-1)

        with self.assertRaises(VoiceException):
            self.voice.volume(2)

        with self.assertRaises(VoiceException):
            self.voice.volume(2.0)

    def test_rate(self):
        self.voice.rate(200)
        self.voice.speak("Hello how are you")

    def test_rate_exception(self):
        from voice import VoiceException

        with self.assertRaises(VoiceException):
            self.voice.rate(-1)

        with self.assertRaises(VoiceException):
            self.voice.rate(None)