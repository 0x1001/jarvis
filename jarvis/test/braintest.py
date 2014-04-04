import unittest

class BrainTest(unittest.TestCase):
    def setUp(self):
        from neural import Brain

        self.br = Brain()

    def test_configure_invalidinput(self):
        from neural import BrainException

        with self.assertRaises(BrainException):
            self.br.configure(None,None)

    def test_configure_validinput(self):
        from neural import BrainException

        self.br.configure(1,1)

    def test_learn_invalidinput(self):
        from neural import BrainException

        with self.assertRaises(BrainException):
            self.br.learn(None)

    def test_learn_validinput(self):
        from neural import BrainException

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

    def test_denormalize(self):
        denormalized_data = self.br._denormalize([1,2,3])
        self.assertEqual(denormalized_data,[1,2,3])

        denormalized_data = self.br._denormalize([1,2,0,3,0])
        self.assertEqual(denormalized_data,[1,2,3])

        denormalized_data = self.br._denormalize([0,0,1,2,3])
        self.assertEqual(denormalized_data,[1,2,3])

        denormalized_data = self.br._denormalize([0,0,0])
        self.assertEqual(denormalized_data,[])

    def test_think_exception(self):
        from neural import BrainException

        with self.assertRaises(BrainException):
            self.br.think((1,1))

    def test_think(self):
        from neural import BrainException

        self.br.configure(2,2)
        data = {}
        data[(1,2,3)] = (1,2)
        data[(2,2)] = (2,2)
        data[(1,)] = (3,3)

        self.br.learn(data)

        output_data = self.br.think((1,1))

        self.assertEqual(len(output_data),2)
        self.assertIsInstance(output_data[0],int)
        self.assertIsInstance(output_data[1],int)