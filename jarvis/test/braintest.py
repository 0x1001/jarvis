import unittest

class BrainTest(unittest.TestCase):
    def setUp(self):
        from brain import Brain

        self.br = Brain()

    def test_configure_invalidinput(self):
        from brain import BrainException

        with self.assertRaises(BrainException):
            self.br.configure(None,None)

    def test_configure_validinput(self):
        from brain import BrainException

        self.br.configure(1,1)

    def test_learn_invalidinput(self):
        from brain import BrainException

        with self.assertRaises(BrainException):
            self.br.learn(None)

    def test_learn_validinput(self):
        from brain import BrainException

        self.br.configure(2,2)
        data = {}
        data[(1,2,3)] = (1,2)
        data[(2,2)] = (2,2)
        data[(1,)] = (3,3)

        self.br.learn(data)

    def test_normalize(self):
        normalized_data = self.br._normalize([1,2,3],5)
        self.assertEqual(normalized_data,[1,2,3,0,0])

        normalized_data = self.br._normalize([1,2,3],2)
        self.assertEqual(normalized_data,[1,2])

        normalized_data = self.br._normalize([1,2,3],3)
        self.assertEqual(normalized_data,[1,2,3])
