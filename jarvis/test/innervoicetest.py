import unittest

class InnerVoiceTest(unittest.TestCase):
    def setUp(self):
        from neural import InnerVoice

        self.innervoice = InnerVoice()

    def test_start(self):
        import jarvis
        from database import InnerVoiceDataBase

        he = jarvis.Jarvis()
        he.respond = lambda request: []

        self.innervoice.innerVoices(InnerVoiceDataBase())
        self.innervoice.jarvis(he)

        self.innervoice.start()
        self.innervoice.stop()

    def test_innervoice(self):
        self.assertTrue(hasattr(self.innervoice,"_innervoice"))
