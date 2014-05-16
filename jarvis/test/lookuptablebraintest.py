import unittest

class LookUpTableBrainTest(unittest.TestCase):
    def setUp(self):
        from neural import LookUpTableBrain
        self._brain = LookUpTableBrain()

    def test_learn_exception(self):
        self._brain.learn(None)

    def test_learn(self):
        dataset = {(0,0): (1,1)}
        self._brain.learn(dataset)

    def test_think_exception(self):
        from neural import LookUpTableBrainException

        with self.assertRaises(LookUpTableBrainException):
            self._brain.think(0)

    def test_think_exception(self):
        from neural import LookUpTableBrainException

        with self.assertRaises(LookUpTableBrainException):
            self._brain.think((0,0))

    def test_think(self):
        from neural import LookUpTableBrainException

        dataset = {(0,0): (1,1),(0,1): (1,2)}
        self._brain.learn(dataset)

        output_data = self._brain.think((0,0))
        self.assertEqual(output_data[0],1)
        self.assertEqual(output_data[1],1)

        output_data = self._brain.think((0,1))
        self.assertEqual(output_data[0],1)
        self.assertEqual(output_data[1],2)