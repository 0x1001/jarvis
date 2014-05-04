import unittest

class InnerVoiceTest(unittest.TestCase):
    def setUp(self):
        from neural import InnerVoice

        self.innervoice = InnerVoice()

    def test_start(self):
        import jarvis
        from database import InnerVoiceDataBase

        self.innervoice.innerVoices(InnerVoiceDataBase())
        self.innervoice.jarvis(jarvis.Jarvis())

        self.innervoice.start()

    def test_innervoice_exception(self):
        from neural import InnerVoiceException

        with self.assertRaises(InnerVoiceException):
            self.innervoice._innervoice()

    def test_innervoice(self):
        self.assertTrue(hasattr(self.innervoice,"_innervoice"))
