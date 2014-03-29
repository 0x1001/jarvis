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

    def configure(self,input,output):
        """
            This function configures brain

            Input:
            input       - Input size
            output      - Output size

            Returns:
            Nothing
        """
        from pybrain.tools.shortcuts import buildNetwork

        if not isinstance(input,int) or not isinstance(output,int):
            raise BrainException("Bad input. Three int expected.")

        self._input = input
        self._output = output
        self._hidden = int(round((input + output)*2/3))

        self._net = buildNetwork(self._input,self._hidden,self._output)

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
        if dataset == {}: raise BrainException("Dataset for learning is empty.")

        data = SupervisedDataSet(self._input,self._output)
        for input,output in dataset.items():
            input = self._normalize(input,self._input)
            output = self._normalize(output,self._output)
            data.addSample(input,output)
            data.addSample(input,output)

        trainer = BackpropTrainer(self._net, data)
        trainer.trainUntilConvergence()

    def _normalize(self,data,norm):
        """
            Adjust data to proper length

            Input:
            data        - List to adjust
            norm        - Norm used for adjusting

            Returns:
            adjusted data
        """
        if len(data) > norm:
            data = data[:norm]
        elif len(data) < norm:
            data += (0,)*(norm - len(data))

        return data

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
