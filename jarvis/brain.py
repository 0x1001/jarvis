################################################################################
################################### Class ######################################
################################################################################
class BrainException(Exception): pass

class Brain(object):
    """
        Brain class - Neural network abstraction

        Variables:
        _net        - Neural network
    """
    __INPUT = 8
    __OUTPUT = 8
    __HIDDEN = 200

    def __init__(self):
        from pybrain.tools.shortcuts import buildNetwork

        self._net = buildNetwork(self.__INPUT, self.__HIDDEN, self.__OUTPUT)

    def think(self,data):
        """
            Activates neural network

            Input:
            data    - List of input numbers

            Returns:
            Numbers list created by neural network
        """
        if len(data) > self.__INPUT:
            data = data[:self.__INPUT]
        elif len(data) < self.__INPUT:
            data += (0,)*(self.__INPUT - len(data))

        return map(int,map(round,self._net.activate(data)))

    def learn(self,dataset):
        """
            Trains neural network

            Input:
            dataset     - dict of input and expected output

            Returns:
            Nothing
        """
        from pybrain.supervised.trainers import BackpropTrainer
        from pybrain.datasets import SupervisedDataSet

        data = SupervisedDataSet(self.__INPUT,self.__OUTPUT)
        for input,output in dataset.items():
            if len(input) > self.__INPUT:
                input = input[:self.__INPUT]
            elif len(input) < self.__INPUT:
                input += (0,)*(self.__INPUT - len(input))

            if len(output) > self.__OUTPUT:
                output = output[:self.__OUTPUT]
            elif len(output) < self.__OUTPUT:
                output += (0,)*(self.__OUTPUT - len(output))

            data.addSample(input,output)
            data.addSample(input,output)

        trainer = BackpropTrainer(self._net, data)
        trainer.trainUntilConvergence()
