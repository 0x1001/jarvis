################################################################################
################################### Class ######################################
################################################################################
class BrainException(Exception): pass

class Brain(object):
    """
        Brain class - Neural network abstraction

        Attributes:
        _net        - Neural network
        _input      - Network inputs count
        _output     - Network outputs count
        _hidden     - Network hidden nodes count
    """
    def __init__(self):
        self._net = None
        self._input = 0
        self._output = 0
        self._hidden = 0

    def configure(self,input,output,hidded):
        """
            This function configures brain

            Input:
            Nothing

            Returns:
            Nothing
        """
        from pybrain.tools.shortcuts import buildNetwork

        if not isinstance(input,int) or not isinstance(output,int) or not isinstance(hidded,int):
            raise BrainException("Bad input. Three int expected.")

        self._input = input
        self._output = output
        self._hidden = hidded

        self._net = buildNetwork(input,output,hidded)

    def learn(self,dataset):
        """
            This function trains network

            Input:
            dataset     - Dataset to train network

            Returns:
            Nothing
        """
        from pybrain.supervised.trainers import BackpropTrainer
        from pybrain.datasets import SupervisedDataSet

        if self._net == None: raise BrainException("Brain is not configured!")

        data = SupervisedDataSet(self._input,self._output)
        for input,output in dataset.items():
            if len(input) > self._input:
                input = input[:self._input]
            elif len(input) < self._input:
                input += (0,)*(self._input - len(input))

            if len(output) > self._output:
                output = output[:self._output]
            elif len(output) < self._output:
                output += (0,)*(self._output - len(output))

            data.addSample(input,output)
            data.addSample(input,output)

        trainer = BackpropTrainer(self._net, data)
        trainer.trainUntilConvergence()

##class Brain(object):
##    """
##        Brain class - Neural network abstraction
##
##        Variables:
##        _net        - Neural network
##    """
##    __INPUT = 8
##    __OUTPUT = 8
##    __HIDDEN = 200
##
##    def __init__(self):
##        from pybrain.tools.shortcuts import buildNetwork
##
##        self._net = buildNetwork(self.__INPUT, self.__HIDDEN, self.__OUTPUT)
##
##    def think(self,data):
##        """
##            Activates neural network
##
##            Input:
##            data    - List of input numbers
##
##            Returns:
##            Numbers list created by neural network
##        """
##        if len(data) > self.__INPUT:
##            data = data[:self.__INPUT]
##        elif len(data) < self.__INPUT:
##            data += (0,)*(self.__INPUT - len(data))
##
##        return map(int,map(round,self._net.activate(data)))
##
##    def learn(self,dataset):
##        """
##            Trains neural network
##
##            Input:
##            dataset     - dict of input and expected output
##
##            Returns:
##            Nothing
##        """
##        from pybrain.supervised.trainers import BackpropTrainer
##        from pybrain.datasets import SupervisedDataSet
##
##        data = SupervisedDataSet(self.__INPUT,self.__OUTPUT)
##        for input,output in dataset.items():
##            if len(input) > self.__INPUT:
##                input = input[:self.__INPUT]
##            elif len(input) < self.__INPUT:
##                input += (0,)*(self.__INPUT - len(input))
##
##            if len(output) > self.__OUTPUT:
##                output = output[:self.__OUTPUT]
##            elif len(output) < self.__OUTPUT:
##                output += (0,)*(self.__OUTPUT - len(output))
##
##            data.addSample(input,output)
##            data.addSample(input,output)
##
##        trainer = BackpropTrainer(self._net, data)
##        trainer.trainUntilConvergence()
