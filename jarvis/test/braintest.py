import unittest

class BrainTest(unittest.TestCase):
    def setUp(self):
        from neural import Brain

        self.br = Brain()

    def test_learn(self):
        from neural import BrainException

        with self.assertRaises(BrainException):
            self.br.learn(None)

    def test_configure(self):
        from neural import BrainException

        with self.assertRaises(BrainException):
            self.br.configure()

    def test_think(self):
        from neural import BrainException

        with self.assertRaises(BrainException):
            self.br.think(None)