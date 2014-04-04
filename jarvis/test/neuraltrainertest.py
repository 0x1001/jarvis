import unittest

class NeuralTrainerTest(unittest.TestCase):
    def setUp(self):
        from neural import NeuralTrainer
        from pybrain.tools.shortcuts import buildNetwork
        from pybrain.datasets import SupervisedDataSet

        self.net = buildNetwork(1,10,1)
        data = SupervisedDataSet(1,1)
        data.addSample((1,),(0,))
        data.addSample((0,),(1,))

        self.tr = NeuralTrainer(self.net,data)

    def test_simpleTrain(self):
        self.tr.simpleTrain()

        self.assertEqual(round(self.net.activate([1])),0)
        self.assertEqual(round(self.net.activate([0])),1)